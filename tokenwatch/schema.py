"""TokenWatch data schema.

Every record is append-only and hash-chained, matching the headgate
receipt chain pattern from HEADGATE-INFERENCE-SPEC.md §3.

Two record types:
  Snapshot         — point-in-time API or subscription pricing observation
  SubscriptionTier — consumer/enterprise tier structure observation

Both produce PricingRecord entries in the ledger.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Snapshot:
    """A single pricing observation for one model endpoint."""

    provider: str           # "openai", "anthropic", "google"
    model: str              # "gpt-4o", "claude-sonnet-5-5", "gemini-4-argon"
    input_price_per_mtok: float   # USD per 1M input tokens
    output_price_per_mtok: float  # USD per 1M output tokens
    tier: str = "api"       # "api", "batch", "cached", "api-reasoning"
    observed_at: str = ""   # ISO 8601 date, e.g. "2024-05-13"
    context_window: int = 0
    batch_discount: float = 0.0   # 0.0-1.0, e.g. 0.5 for 50% off
    cache_discount: float = 0.0   # discount for cached input tokens
    notes: str = ""
    metadata: dict = field(default_factory=dict)

    @property
    def blended_price(self) -> float:
        """Rough blended price assuming 1:2 input:output ratio."""
        return (self.input_price_per_mtok + 2 * self.output_price_per_mtok) / 3

    def to_dict(self) -> dict:
        d = {
            "provider": self.provider,
            "model": self.model,
            "input_price_per_mtok": self.input_price_per_mtok,
            "output_price_per_mtok": self.output_price_per_mtok,
            "tier": self.tier,
            "observed_at": self.observed_at,
        }
        if self.context_window:
            d["context_window"] = self.context_window
        if self.batch_discount:
            d["batch_discount"] = self.batch_discount
        if self.cache_discount:
            d["cache_discount"] = self.cache_discount
        if self.notes:
            d["notes"] = self.notes
        if self.metadata:
            d["metadata"] = self.metadata
        return d


@dataclass
class SubscriptionTier:
    """A consumer or enterprise subscription pricing observation."""

    provider: str            # "openai", "anthropic", "google"
    tier_name: str           # "Plus", "Pro", "Max", "Ultra", "Enterprise"
    price_usd_monthly: float
    models_included: list[str] = field(default_factory=list)
    usage_multiplier: float = 1.0  # e.g. 5.0 for "5x Pro usage"
    includes_api_credits: bool = False
    api_credit_usd: float = 0.0
    observed_at: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        d = {
            "provider": self.provider,
            "tier_name": self.tier_name,
            "price_usd_monthly": self.price_usd_monthly,
            "usage_multiplier": self.usage_multiplier,
            "observed_at": self.observed_at,
        }
        if self.models_included:
            d["models_included"] = self.models_included
        if self.includes_api_credits:
            d["includes_api_credits"] = True
            d["api_credit_usd"] = self.api_credit_usd
        if self.notes:
            d["notes"] = self.notes
        return d


@dataclass
class PricingRecord:
    """One entry in the hash-chained pricing ledger.

    Matches the receipt chain pattern from headgate.inference/0.1:
      - seq, prev (hash chain)
      - when (timestamp)
      - gate = "tokenwatch"
      - decision codes for conformance checks
    """

    seq: int
    prev: str                # sha256 of previous record
    when: float              # unix timestamp
    record_type: str         # "snapshot" | "subscription" | "routing_advisory"
    data: dict               # the Snapshot or SubscriptionTier, serialized
    provider: str
    model: str = ""
    provenance: str = "direct"  # "direct" (official page), "secondary", "archived"

    def to_dict(self) -> dict:
        return {
            "protocol": "tokenwatch/0.1",
            "seq": self.seq,
            "prev": self.prev,
            "when": self.when,
            "record_type": self.record_type,
            "provider": self.provider,
            "model": self.model,
            "provenance": self.provenance,
            "data": self.data,
        }

    def hash(self) -> str:
        raw = json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(raw.encode()).hexdigest()
