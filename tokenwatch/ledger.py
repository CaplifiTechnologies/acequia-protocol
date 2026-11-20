"""TokenWatch pricing ledger — append-only, hash-chained.

Same integrity model as the headgate receipt chain:
  - Every record is hash-chained to its predecessor
  - Append-only (no edits, no deletes)
  - Broken chain = integrity failure, system flags it
  - Auditable by any parciante
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from tokenwatch.schema import PricingRecord, Snapshot, SubscriptionTier


GENESIS_HASH = "0" * 64


class PricingLedger:
    """Append-only pricing ledger with hash chain integrity."""

    def __init__(self):
        self._records: list[PricingRecord] = []
        self._last_hash: str = GENESIS_HASH

    def append(self, record_type: str, data: dict,
               provider: str, model: str = "",
               provenance: str = "direct") -> PricingRecord:
        record = PricingRecord(
            seq=len(self._records),
            prev=self._last_hash,
            when=time.time(),
            record_type=record_type,
            data=data,
            provider=provider,
            model=model,
            provenance=provenance,
        )
        self._last_hash = record.hash()
        self._records.append(record)
        return record

    def append_snapshot(self, snap: Snapshot,
                        provenance: str = "direct") -> PricingRecord:
        return self.append(
            record_type="snapshot",
            data=snap.to_dict(),
            provider=snap.provider,
            model=snap.model,
            provenance=provenance,
        )

    def append_subscription(self, tier: SubscriptionTier,
                            provenance: str = "direct") -> PricingRecord:
        return self.append(
            record_type="subscription",
            data=tier.to_dict(),
            provider=tier.provider,
            model="",
            provenance=provenance,
        )

    # ── Queries ──

    @property
    def records(self) -> list[PricingRecord]:
        return list(self._records)

    @property
    def length(self) -> int:
        return len(self._records)

    def by_provider(self, provider: str) -> list[PricingRecord]:
        return [r for r in self._records if r.provider == provider]

    def by_model(self, model: str) -> list[PricingRecord]:
        return [r for r in self._records if r.model == model]

    def snapshots(self) -> list[PricingRecord]:
        return [r for r in self._records if r.record_type == "snapshot"]

    def subscriptions(self) -> list[PricingRecord]:
        return [r for r in self._records if r.record_type == "subscription"]

    def current_prices(self, provider: str) -> list[dict]:
        """Most recent snapshot per model for a provider."""
        latest: dict[str, PricingRecord] = {}
        for r in self._records:
            if r.record_type == "snapshot" and r.provider == provider:
                latest[r.model] = r
        return [r.data for r in latest.values()]

    def price_history(self, model: str) -> list[dict]:
        """All snapshots for a model, chronological."""
        return [r.data for r in self._records
                if r.record_type == "snapshot" and r.model == model]

    def frontier_premium(self) -> dict:
        """Ratio of most expensive to least expensive current model
        across all providers. The core metric for the two-speed
        deflation pattern."""
        snapshots = [r for r in self._records
                     if r.record_type == "snapshot"]
        if not snapshots:
            return {"ratio": 0, "frontier": None, "commodity": None}

        latest: dict[str, PricingRecord] = {}
        for r in snapshots:
            latest[r.model] = r

        if not latest:
            return {"ratio": 0, "frontier": None, "commodity": None}

        by_output = sorted(latest.values(),
                           key=lambda r: r.data.get("output_price_per_mtok", 0))
        cheapest = by_output[0]
        priciest = by_output[-1]

        cheap_price = cheapest.data.get("output_price_per_mtok", 0)
        dear_price = priciest.data.get("output_price_per_mtok", 0)

        ratio = dear_price / cheap_price if cheap_price > 0 else float("inf")

        return {
            "ratio": round(ratio, 1),
            "frontier": {
                "model": priciest.model,
                "output_price": dear_price,
            },
            "commodity": {
                "model": cheapest.model,
                "output_price": cheap_price,
            },
        }

    def deflation_rate(self, model: str) -> float | None:
        """Annualized price change for a model based on its history.
        Negative = deflation (prices falling). Returns None if < 2 observations."""
        history = self.price_history(model)
        if len(history) < 2:
            return None

        first = history[0]
        last = history[-1]
        p0 = first.get("output_price_per_mtok", 0)
        p1 = last.get("output_price_per_mtok", 0)

        if p0 == 0:
            return None

        return (p1 - p0) / p0

    # ── Integrity ──

    def verify_chain(self) -> tuple[bool, str]:
        """Verify hash chain integrity. Returns (valid, message)."""
        if not self._records:
            return True, "empty ledger"

        prev = GENESIS_HASH
        for i, record in enumerate(self._records):
            if record.prev != prev:
                return False, f"chain broken at seq {i}: expected {prev}, got {record.prev}"
            prev = record.hash()

        return True, f"chain intact, {len(self._records)} records"

    # ── Persistence ──

    def save(self, path: str | Path) -> None:
        path = Path(path)
        rows = [r.to_dict() for r in self._records]
        path.write_text(json.dumps(rows, indent=2))

    @classmethod
    def load(cls, path: str | Path) -> PricingLedger:
        path = Path(path)
        rows = json.loads(path.read_text())
        ledger = cls()
        for row in rows:
            record = PricingRecord(
                seq=row["seq"],
                prev=row["prev"],
                when=row["when"],
                record_type=row["record_type"],
                data=row["data"],
                provider=row["provider"],
                model=row.get("model", ""),
                provenance=row.get("provenance", "direct"),
            )
            ledger._records.append(record)
            ledger._last_hash = record.hash()
        return ledger

    # ── Routing advisory (Sir Ornith interface) ──

    def routing_advisory(self, query_class: str = "general") -> dict:
        """Produce a routing advisory for Sir Ornith.

        Returns current pricing data structured for model selection.
        Sir Ornith consumes this to route queries to the cheapest
        conforming model for a given query class.

        Query classes:
          - "general": standard queries, route to cheapest capable model
          - "reasoning": complex queries, route to reasoning tier
          - "batch": async processing, apply batch discounts
          - "local": prefer local/edge inference when available
        """
        snapshots = self.snapshots()
        if not snapshots:
            return {"query_class": query_class, "models": []}

        latest: dict[str, dict] = {}
        for r in snapshots:
            latest[r.model] = r.data

        models = []
        for model, data in latest.items():
            entry = {
                "model": model,
                "provider": data.get("provider", ""),
                "output_price": data.get("output_price_per_mtok", 0),
                "input_price": data.get("input_price_per_mtok", 0),
                "tier": data.get("tier", "api"),
            }

            if query_class == "batch" and data.get("batch_discount", 0) > 0:
                discount = data["batch_discount"]
                entry["effective_output_price"] = entry["output_price"] * (1 - discount)
                entry["effective_input_price"] = entry["input_price"] * (1 - discount)
            else:
                entry["effective_output_price"] = entry["output_price"]
                entry["effective_input_price"] = entry["input_price"]

            models.append(entry)

        models.sort(key=lambda m: m["effective_output_price"])

        return {
            "query_class": query_class,
            "models": models,
            "frontier": models[-1] if models else None,
            "commodity": models[0] if models else None,
        }

    def summary(self) -> str:
        valid, msg = self.verify_chain()
        providers = set(r.provider for r in self._records)
        models = set(r.model for r in self._records if r.model)
        lines = [
            f"TokenWatch Ledger",
            f"Records: {len(self._records)}",
            f"Providers: {', '.join(sorted(providers)) if providers else 'none'}",
            f"Models: {len(models)}",
            f"Chain: {msg}",
        ]
        premium = self.frontier_premium()
        if premium["ratio"]:
            lines.append(
                f"Frontier premium: {premium['ratio']}x"
                f" ({premium['frontier']['model']}"
                f" vs {premium['commodity']['model']})"
            )
        return "\n".join(lines)
