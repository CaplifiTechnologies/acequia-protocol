"""TokenWatch Harvester — collects and archives frontier AI pricing.

The Harvester is the data-collection arm of TokenWatch. It records
pricing snapshots and subscription tiers into the PricingLedger,
creating an append-only, hash-chained archive of how frontier AI
providers price their services over time.

Seed data covers the five eras identified in the pricing arc research:
  Era 1: API-Only (2020-2022)
  Era 2: Subscription Inflection (2023)
  Era 3: Price War (2024)
  Era 4: Premium Divergence (late 2024-2025)
  Era 5: Mature Stack (2025-present)
"""

from __future__ import annotations

from tokenwatch.ledger import PricingLedger
from tokenwatch.schema import Snapshot, SubscriptionTier


class Harvester:
    """Records pricing observations into a PricingLedger."""

    def __init__(self, ledger: PricingLedger):
        self.ledger = ledger

    def record_snapshot(self, snap: Snapshot,
                        provenance: str = "direct") -> None:
        self.ledger.append_snapshot(snap, provenance=provenance)

    def record_subscription(self, tier: SubscriptionTier,
                            provenance: str = "direct") -> None:
        self.ledger.append_subscription(tier, provenance=provenance)

    def seed(self) -> None:
        """Load historical pricing data into the ledger.

        All prices are USD per 1M tokens unless noted.
        Sources: official pricing pages, blog announcements, press releases.
        Provenance marked "archived" — these are historical records,
        not live observations.
        """
        self._seed_era_1_api_only()
        self._seed_era_2_subscription_inflection()
        self._seed_era_3_price_war()
        self._seed_era_4_premium_divergence()
        self._seed_era_5_mature_stack()
        self._seed_subscriptions()

    # ── Era 1: API-Only (2020-2022) ──

    def _seed_era_1_api_only(self):
        prov = "archived"
        snapshots = [
            Snapshot("openai", "gpt-3-davinci",
                     60.00, 60.00, "api", "2020-06-11",
                     notes="Launch price, single-rate"),
            Snapshot("openai", "gpt-3-davinci",
                     20.00, 20.00, "api", "2022-01-01",
                     notes="Price cut from $60"),
            Snapshot("openai", "gpt-3.5-turbo",
                     2.00, 2.00, "api", "2022-11-30",
                     context_window=4096,
                     notes="ChatGPT engine, ~10x cheaper than davinci"),
        ]
        for s in snapshots:
            self.record_snapshot(s, provenance=prov)

    # ── Era 2: Subscription Inflection (2023) ──

    def _seed_era_2_subscription_inflection(self):
        prov = "archived"
        snapshots = [
            Snapshot("openai", "gpt-4",
                     30.00, 60.00, "api", "2023-03-14",
                     context_window=8192,
                     notes="GPT-4 launch, 30x pricier than 3.5-turbo"),
            Snapshot("openai", "gpt-4-32k",
                     60.00, 120.00, "api", "2023-03-14",
                     context_window=32768),
            Snapshot("openai", "gpt-3.5-turbo",
                     1.50, 2.00, "api", "2023-06-13",
                     context_window=16384,
                     notes="16k context, slight price cut"),
            Snapshot("anthropic", "claude-1",
                     11.02, 32.68, "api", "2023-03-14",
                     context_window=9000,
                     notes="Claude 1 launch via API"),
            Snapshot("anthropic", "claude-2",
                     11.02, 32.68, "api", "2023-07-11",
                     context_window=100000,
                     notes="100k context window, same price as Claude 1"),
            Snapshot("google", "palm-2",
                     1.00, 1.00, "api", "2023-05-10",
                     notes="PaLM 2 via Vertex AI, aggressive entry price"),
        ]
        for s in snapshots:
            self.record_snapshot(s, provenance=prov)

    # ── Era 3: Price War (2024) ──

    def _seed_era_3_price_war(self):
        prov = "archived"
        snapshots = [
            # GPT-4 Turbo + price cuts
            Snapshot("openai", "gpt-4-turbo",
                     10.00, 30.00, "api", "2024-01-25",
                     context_window=128000,
                     notes="3x cheaper than GPT-4, 128k context"),
            Snapshot("openai", "gpt-3.5-turbo",
                     0.50, 1.50, "api", "2024-01-25",
                     context_window=16384,
                     notes="Another 3x cut"),

            # Claude 3 family — tiered pricing debut
            Snapshot("anthropic", "claude-3-opus",
                     15.00, 75.00, "api", "2024-03-04",
                     context_window=200000,
                     notes="Frontier, 200k context"),
            Snapshot("anthropic", "claude-3-sonnet",
                     3.00, 15.00, "api", "2024-03-04",
                     context_window=200000,
                     notes="Mid-tier"),
            Snapshot("anthropic", "claude-3-haiku",
                     0.25, 1.25, "api", "2024-03-04",
                     context_window=200000,
                     notes="Speed/cost tier, 60x cheaper than Opus output"),

            # GPT-4o — the price war trigger
            Snapshot("openai", "gpt-4o",
                     5.00, 15.00, "api", "2024-05-13",
                     context_window=128000,
                     notes="50% cheaper than GPT-4 Turbo, multimodal"),

            # Gemini enters
            Snapshot("google", "gemini-1.5-pro",
                     3.50, 10.50, "api", "2024-02-15",
                     context_window=1000000,
                     notes="1M context window, undercut GPT-4"),
            Snapshot("google", "gemini-1.5-flash",
                     0.075, 0.30, "api", "2024-05-14",
                     context_window=1000000,
                     notes="Ultra-cheap, challenged Haiku"),

            # Mini models
            Snapshot("openai", "gpt-4o-mini",
                     0.15, 0.60, "api", "2024-07-18",
                     context_window=128000,
                     notes="Replaced 3.5-turbo, 97% cheaper than GPT-4"),
        ]
        for s in snapshots:
            self.record_snapshot(s, provenance=prov)

    # ── Era 4: Premium Divergence (late 2024-2025) ──

    def _seed_era_4_premium_divergence(self):
        prov = "archived"
        snapshots = [
            # OpenAI reasoning models — new price ceiling
            Snapshot("openai", "o1",
                     15.00, 60.00, "api", "2024-12-05",
                     context_window=200000,
                     notes="Reasoning model, 4x GPT-4o output price"),
            Snapshot("openai", "o1-mini",
                     3.00, 12.00, "api", "2024-09-12",
                     context_window=128000,
                     notes="Cheaper reasoning tier"),

            # Claude 3.5 Sonnet — perf at mid-tier price
            Snapshot("anthropic", "claude-3.5-sonnet",
                     3.00, 15.00, "api", "2024-06-20",
                     context_window=200000,
                     notes="Opus-level perf at Sonnet price"),

            # Gemini 2.0 Flash
            Snapshot("google", "gemini-2.0-flash",
                     0.10, 0.40, "api", "2025-02-25",
                     context_window=1000000,
                     notes="Further Flash deflation"),

            # DeepSeek — open-weight price floor
            Snapshot("deepseek", "deepseek-v3",
                     0.27, 1.10, "api", "2025-01-20",
                     context_window=128000,
                     notes="Open-weight, set new price floor for frontier-class"),
            Snapshot("deepseek", "deepseek-r1",
                     0.55, 2.19, "api", "2025-01-20",
                     context_window=128000,
                     notes="Reasoning model, fraction of o1 price"),

            # Batch pricing becomes standard
            Snapshot("openai", "gpt-4o",
                     2.50, 7.50, "batch", "2024-07-18",
                     context_window=128000,
                     batch_discount=0.5,
                     notes="50% batch discount"),
            Snapshot("anthropic", "claude-3.5-sonnet",
                     1.50, 7.50, "batch", "2024-09-01",
                     context_window=200000,
                     batch_discount=0.5,
                     notes="50% batch discount"),

            # Prompt caching
            Snapshot("anthropic", "claude-3.5-sonnet",
                     0.30, 15.00, "cached", "2024-08-14",
                     context_window=200000,
                     cache_discount=0.9,
                     notes="90% cached-input discount"),
        ]
        for s in snapshots:
            self.record_snapshot(s, provenance=prov)

    # ── Era 5: Mature Stack (2025-present) ──

    def _seed_era_5_mature_stack(self):
        prov = "archived"
        snapshots = [
            # OpenAI current
            Snapshot("openai", "gpt-4.1",
                     2.00, 8.00, "api", "2025-04-14",
                     context_window=1047576,
                     notes="1M context, cheaper than 4o"),
            Snapshot("openai", "gpt-4.1-mini",
                     0.40, 1.60, "api", "2025-04-14",
                     context_window=1047576),
            Snapshot("openai", "gpt-4.1-nano",
                     0.10, 0.40, "api", "2025-04-14",
                     context_window=1047576,
                     notes="Commodity floor from OpenAI"),
            Snapshot("openai", "o3",
                     10.00, 40.00, "api", "2025-04-16",
                     context_window=200000,
                     notes="Latest reasoning, still premium"),
            Snapshot("openai", "o4-mini",
                     1.10, 4.40, "api", "2025-04-16",
                     context_window=200000,
                     notes="Cheap reasoning tier"),

            # Anthropic current
            Snapshot("anthropic", "claude-sonnet-4",
                     3.00, 15.00, "api", "2025-05-22",
                     context_window=200000,
                     notes="Claude 4 generation"),
            Snapshot("anthropic", "claude-opus-4",
                     15.00, 75.00, "api", "2025-05-22",
                     context_window=200000,
                     notes="Frontier reasoning"),
            Snapshot("anthropic", "claude-haiku-3.5",
                     0.80, 4.00, "api", "2025-05-22",
                     context_window=200000,
                     notes="Speed tier"),

            # Google current
            Snapshot("google", "gemini-2.5-pro",
                     1.25, 10.00, "api", "2025-03-25",
                     context_window=1000000,
                     notes="Thinking model, 1M context"),
            Snapshot("google", "gemini-2.5-flash",
                     0.15, 0.60, "api", "2025-04-17",
                     context_window=1000000,
                     notes="Speed tier with thinking"),
        ]
        for s in snapshots:
            self.record_snapshot(s, provenance=prov)

    # ── Subscription tiers ──

    def _seed_subscriptions(self):
        prov = "archived"
        tiers = [
            # OpenAI
            SubscriptionTier("openai", "Plus", 20.00,
                             ["gpt-4o", "gpt-4o-mini", "o4-mini"],
                             usage_multiplier=1.0,
                             observed_at="2025-04-01"),
            SubscriptionTier("openai", "Pro", 200.00,
                             ["gpt-4o", "o3", "o4-mini"],
                             usage_multiplier=5.0,
                             observed_at="2025-04-01",
                             notes="Unlimited* o3 access"),

            # Anthropic
            SubscriptionTier("anthropic", "Pro", 20.00,
                             ["claude-sonnet-4", "claude-haiku-3.5"],
                             usage_multiplier=1.0,
                             observed_at="2025-05-01"),
            SubscriptionTier("anthropic", "Max (5x)", 100.00,
                             ["claude-sonnet-4", "claude-opus-4"],
                             usage_multiplier=5.0,
                             observed_at="2025-05-01"),
            SubscriptionTier("anthropic", "Max (20x)", 200.00,
                             ["claude-sonnet-4", "claude-opus-4"],
                             usage_multiplier=20.0,
                             observed_at="2025-05-01",
                             notes="Highest consumer tier"),

            # Google
            SubscriptionTier("google", "AI Premium", 19.99,
                             ["gemini-2.5-pro", "gemini-2.5-flash"],
                             usage_multiplier=1.0,
                             observed_at="2025-04-01",
                             notes="Bundled with Google One"),
            SubscriptionTier("google", "AI Ultra", 249.99,
                             ["gemini-2.5-pro"],
                             usage_multiplier=10.0,
                             observed_at="2025-04-01",
                             notes="Announced Feb 2025"),
        ]
        for t in tiers:
            self.record_subscription(t, provenance=prov)
