"""Tests for the tokenwatch module."""

import json
import tempfile
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tokenwatch import (
    PricingLedger, Snapshot, SubscriptionTier, PricingRecord,
    Harvester, TokenWatchGate,
)


def test_snapshot_to_dict():
    s = Snapshot("openai", "gpt-4o", 2.50, 10.00, "api", "2024-05-13",
                 context_window=128000, batch_discount=0.5)
    d = s.to_dict()
    assert d["provider"] == "openai"
    assert d["model"] == "gpt-4o"
    assert d["input_price_per_mtok"] == 2.50
    assert d["batch_discount"] == 0.5
    assert d["context_window"] == 128000


def test_blended_price():
    s = Snapshot("anthropic", "claude-sonnet-4", 3.00, 15.00)
    assert s.blended_price == (3.00 + 2 * 15.00) / 3


def test_pricing_record_hash_chain():
    r1 = PricingRecord(0, "0" * 64, 1000.0, "snapshot",
                        {"price": 10}, "openai", "gpt-4o")
    r2 = PricingRecord(1, r1.hash(), 1001.0, "snapshot",
                        {"price": 5}, "openai", "gpt-4o-mini")
    assert r1.hash() != r2.hash()
    assert r2.prev == r1.hash()
    assert r1.to_dict()["protocol"] == "tokenwatch/0.1"


def test_ledger_append_and_verify():
    ledger = PricingLedger()
    snap = Snapshot("openai", "gpt-4o", 2.50, 10.00, "api", "2024-05-13")
    ledger.append_snapshot(snap)

    valid, msg = ledger.verify_chain()
    assert valid
    assert ledger.length == 1
    assert ledger.records[0].provider == "openai"


def test_ledger_chain_integrity():
    ledger = PricingLedger()
    for i in range(5):
        snap = Snapshot("openai", f"model-{i}", float(i), float(i * 2))
        ledger.append_snapshot(snap)

    valid, _ = ledger.verify_chain()
    assert valid

    # Tamper with a record
    ledger._records[2].data["price"] = 999
    valid, msg = ledger.verify_chain()
    assert not valid
    assert "chain broken" in msg


def test_ledger_queries():
    ledger = PricingLedger()
    ledger.append_snapshot(Snapshot("openai", "gpt-4o", 5.00, 15.00))
    ledger.append_snapshot(Snapshot("openai", "gpt-4o-mini", 0.15, 0.60))
    ledger.append_snapshot(Snapshot("anthropic", "claude-sonnet-4", 3.00, 15.00))

    assert len(ledger.by_provider("openai")) == 2
    assert len(ledger.by_model("gpt-4o")) == 1
    assert len(ledger.snapshots()) == 3
    assert len(ledger.current_prices("openai")) == 2


def test_frontier_premium():
    ledger = PricingLedger()
    ledger.append_snapshot(Snapshot("openai", "gpt-4o", 5.00, 15.00))
    ledger.append_snapshot(Snapshot("google", "gemini-flash", 0.075, 0.30))

    premium = ledger.frontier_premium()
    assert premium["ratio"] == 50.0
    assert premium["frontier"]["model"] == "gpt-4o"
    assert premium["commodity"]["model"] == "gemini-flash"


def test_ledger_save_load():
    ledger = PricingLedger()
    ledger.append_snapshot(Snapshot("openai", "gpt-4o", 5.00, 15.00))
    ledger.append_snapshot(Snapshot("anthropic", "claude-sonnet-4", 3.00, 15.00))

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        path = f.name

    ledger.save(path)
    loaded = PricingLedger.load(path)

    assert loaded.length == 2
    valid, _ = loaded.verify_chain()
    assert valid
    assert loaded.records[0].provider == "openai"
    Path(path).unlink()


def test_harvester_seed():
    ledger = PricingLedger()
    harvester = Harvester(ledger)
    harvester.seed()

    assert ledger.length > 30
    valid, _ = ledger.verify_chain()
    assert valid

    providers = set(r.provider for r in ledger.records)
    assert "openai" in providers
    assert "anthropic" in providers
    assert "google" in providers
    assert "deepseek" in providers

    subs = ledger.subscriptions()
    assert len(subs) > 0


def test_tokenwatch_gate():
    ledger = PricingLedger()
    harvester = Harvester(ledger)
    harvester.seed()

    gate = TokenWatchGate(ledger)
    gate.register_providers_from_ledger()

    assert gate.gate.is_conforming

    check = gate.check_pricing_published("openai")
    assert check["pricing_published"]
    assert check["gate_result"]

    check_missing = gate.check_pricing_published("nonexistent")
    assert not check_missing["pricing_published"]


def test_routing_advisory():
    ledger = PricingLedger()
    ledger.append_snapshot(Snapshot("openai", "gpt-4o", 5.00, 15.00))
    ledger.append_snapshot(Snapshot("google", "gemini-flash", 0.075, 0.30,
                                   batch_discount=0.5))

    gate = TokenWatchGate(ledger)
    gate.register_providers_from_ledger()

    advisory = gate.routing_advisory("general")
    assert advisory["query_class"] == "general"
    assert len(advisory["models"]) == 2
    assert advisory["commodity"]["model"] == "gemini-flash"
    assert advisory["gate_conforming"]

    # Batch advisory applies discount
    batch = gate.routing_advisory("batch")
    gemini = [m for m in batch["models"] if m["model"] == "gemini-flash"][0]
    assert gemini["effective_output_price"] == 0.15


def test_model_recommendation():
    ledger = PricingLedger()
    ledger.append_snapshot(Snapshot("openai", "gpt-4o", 5.00, 15.00))
    ledger.append_snapshot(Snapshot("google", "gemini-flash", 0.075, 0.30))
    ledger.append_snapshot(Snapshot("openai", "o3", 10.00, 40.00))

    gate = TokenWatchGate(ledger)
    gate.register_providers_from_ledger()

    rec = gate.model_recommendation("general")
    assert rec["model"] == "gemini-flash"

    rec_capped = gate.model_recommendation("general", max_price=20.0)
    assert rec_capped["model"] == "gemini-flash"

    rec_none = gate.model_recommendation("general", max_price=0.01)
    assert rec_none is None


def test_measurement_report():
    ledger = PricingLedger()
    harvester = Harvester(ledger)
    harvester.seed()

    gate = TokenWatchGate(ledger)
    gate.register_providers_from_ledger()

    report = gate.measurement_report()
    assert report["protocol"] == "tokenwatch/0.1"
    assert report["gate"] == "inference"
    assert report["chain_valid"]
    assert report["gate_conforming"]
    assert "openai" in report["provider_coverage"]


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except Exception as e:
            print(f"  FAIL  {t.__name__}: {e}")
            raise
    print(f"\n{len(tests)} tests passed")
