"""TokenWatch — inference pricing measurement for the Acequia Protocol.

Headgate 12 (Inference) requires published measurement of:
  - Pricing by user class
  - Availability by user class
  - Content policy changes (versioned)
  - Model provenance summary

TokenWatch is the instrument. It harvests, archives, and publishes
frontier AI pricing data as append-only headgate-conformant records.

Interop:
  - Ditch AI:    Records feed the HeadgateChain measurement primitive.
  - Sir Ornith:  Routing decisions consume TokenWatch data to select
                 the cheapest conforming model for each query class.

Usage:
    from tokenwatch import PricingLedger, Snapshot, Harvester

    ledger = PricingLedger()
    harvester = Harvester(ledger)

    harvester.record_snapshot(Snapshot(
        provider="openai",
        model="gpt-4o",
        input_price_per_mtok=2.50,
        output_price_per_mtok=10.00,
        tier="api",
        observed_at="2024-05-13",
    ))

    # Query the ledger
    ledger.current_prices("openai")
    ledger.price_history("gpt-4o")
    ledger.frontier_premium()  # ratio of newest to commodity
"""

from tokenwatch.schema import (
    Snapshot,
    SubscriptionTier,
    PricingRecord,
)
from tokenwatch.ledger import PricingLedger
from tokenwatch.harvester import Harvester
from tokenwatch.interop import TokenWatchGate

__all__ = [
    "Snapshot",
    "SubscriptionTier",
    "PricingRecord",
    "PricingLedger",
    "Harvester",
    "TokenWatchGate",
]
