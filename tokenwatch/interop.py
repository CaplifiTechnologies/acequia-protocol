"""TokenWatch interop — bridges to HeadgateChain and Sir Ornith.

TokenWatchGate wraps a PricingLedger as a Headgate-conformant gate
that plugs into HeadgateChain at link 12 (Inference). It satisfies
the Measurement primitive by exposing the hash-chained pricing ledger.

Sir Ornith interface:
  Sir Ornith handles local-first routing between Headgate 10 (Compute)
  and Headgate 12 (Inference). TokenWatch provides the pricing data
  Sir Ornith needs to make routing decisions. The routing_advisory()
  method on PricingLedger is the interface Sir Ornith consumes.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

from tokenwatch.ledger import PricingLedger

# Import Headgate from the app package
_app_dir = str(Path(__file__).resolve().parent.parent / "app")
if _app_dir not in sys.path:
    sys.path.insert(0, _app_dir)

from headgate import Headgate, HeadgateChain, Parciante


class TokenWatchGate:
    """Bridges TokenWatch to the HeadgateChain as link 12 (Inference).

    Implements the five headgate primitives using the pricing ledger:
      1. Resource:    inference access (measured in tokens)
      2. Standing:    providers as parciantes (by user dependency)
      3. Check:       pricing conformance (material: is the price published?)
      4. Measurement: the PricingLedger itself (append-only, hash-chained)
      5. Default:     OPEN (protects the user, per HEADGATE-INFERENCE-SPEC)
    """

    def __init__(self, ledger: PricingLedger):
        self.ledger = ledger
        self._gate = Headgate(
            name="inference",
            resource="inference access",
            unit="tokens",
            default_action="pass",
        )

    @property
    def gate(self) -> Headgate:
        return self._gate

    def register_provider(self, provider: str, dependency: float = 0.5,
                          share: float = 0.0) -> None:
        """Register an inference provider as a parciante.

        Dependency reflects how much users depend on this provider:
          - High (0.8-1.0): sole provider, no alternatives
          - Medium (0.4-0.7): one of several options
          - Low (0.1-0.3): commodity, easily substituted
        """
        self._gate.add_parciante(provider, dependency=dependency, share=share)

    def register_providers_from_ledger(self) -> None:
        """Auto-register all providers found in the ledger."""
        providers = set(r.provider for r in self.ledger.records)
        for p in sorted(providers):
            prices = self.ledger.current_prices(p)
            n_models = len(prices)
            # More models = lower dependency on any single one
            dep = max(0.2, 0.8 - (n_models * 0.1))
            self.register_provider(p, dependency=dep)

    def check_pricing_published(self, provider: str) -> dict:
        """Headgate material check: has this provider published pricing?

        This is the core conformance check for Headgate 12.
        A provider that hasn't published pricing fails the gate.
        """
        prices = self.ledger.current_prices(provider)
        published = len(prices) > 0

        result = self._gate.check(
            parciante=provider,
            amount=1.0,
            authorization="published_pricing" if published else "none",
            check_type="material",
        )

        return {
            "provider": provider,
            "pricing_published": published,
            "models_priced": len(prices),
            "gate_result": result.allowed,
            "record": result.record.to_dict() if result.record else None,
        }

    def attach_to_chain(self, chain: HeadgateChain) -> HeadgateChain:
        """Attach this gate as link 12 (Inference) on a HeadgateChain."""
        chain.add_link(self._gate)
        return chain

    # ── Sir Ornith interface ──

    def routing_advisory(self, query_class: str = "general") -> dict:
        """Produce routing data for Sir Ornith.

        Delegates to the ledger's routing_advisory() and adds
        gate conformance metadata.
        """
        advisory = self.ledger.routing_advisory(query_class)
        advisory["gate"] = "inference"
        advisory["gate_conforming"] = self._gate.is_conforming
        advisory["chain_integrity"] = self.ledger.verify_chain()[0]
        advisory["protocol"] = "tokenwatch/0.1"
        return advisory

    def model_recommendation(self, query_class: str = "general",
                             max_price: float | None = None) -> dict | None:
        """Recommend a single model for Sir Ornith to route to.

        Applies price ceiling if given. Returns None if no model qualifies.
        """
        advisory = self.ledger.routing_advisory(query_class)
        models = advisory.get("models", [])

        if max_price is not None:
            models = [m for m in models
                      if m["effective_output_price"] <= max_price]

        if not models:
            return None

        # Cheapest conforming model
        return models[0]

    # ── Conformance reporting ──

    def measurement_report(self) -> dict:
        """Headgate Measurement primitive: report on the pricing ledger.

        This is what Headgate 12 publishes as its measurement record.
        """
        valid, msg = self.ledger.verify_chain()
        premium = self.ledger.frontier_premium()

        providers = set(r.provider for r in self.ledger.records)
        provider_coverage = {}
        for p in providers:
            prices = self.ledger.current_prices(p)
            provider_coverage[p] = {
                "models_tracked": len(prices),
                "pricing_published": len(prices) > 0,
            }

        return {
            "protocol": "tokenwatch/0.1",
            "gate": "inference",
            "timestamp": time.time(),
            "ledger_records": self.ledger.length,
            "chain_valid": valid,
            "chain_message": msg,
            "frontier_premium": premium,
            "provider_coverage": provider_coverage,
            "gate_conforming": self._gate.is_conforming,
        }

    def summary(self) -> str:
        report = self.measurement_report()
        lines = [
            "TokenWatch Gate (Headgate 12: Inference)",
            f"Ledger: {report['ledger_records']} records",
            f"Chain: {report['chain_message']}",
            f"Gate conforming: {report['gate_conforming']}",
            f"Providers: {', '.join(sorted(report['provider_coverage'].keys()))}",
        ]
        premium = report["frontier_premium"]
        if premium.get("ratio"):
            lines.append(
                f"Frontier premium: {premium['ratio']}x"
            )
        return "\n".join(lines)
