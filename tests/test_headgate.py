"""Tests for the Headgate composable governance gate."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from app.headgate import Headgate, HeadgateChain, Parciante, Record, CheckResult


class TestHeadgate(unittest.TestCase):
    def setUp(self):
        self.gate = Headgate(
            "test-gate", "water", "gallons",
            total_supply=1000.0,
        )
        self.gate.add_parciante("farm-a", dependency=0.9)
        self.gate.add_parciante("farm-b", dependency=0.5)

    def test_check_with_standing_passes(self):
        result = self.gate.check("farm-a", 100.0)
        self.assertTrue(result.allowed)
        self.assertGreater(result.flow, 0)

    def test_check_without_standing_denied(self):
        result = self.gate.check("outsider", 100.0)
        self.assertFalse(result.allowed)
        self.assertEqual(result.flow, 0.0)
        self.assertIn("no standing", result.reason)

    def test_forbidden_check_type_denied(self):
        result = self.gate.check("farm-a", 100.0, check_type="identity")
        self.assertFalse(result.allowed)
        self.assertIn("identity", result.reason)

    def test_all_forbidden_checks(self):
        for check_type in ["identity", "worthiness", "political_alignment",
                           "ability_to_pay_premium", "end_use_value"]:
            result = self.gate.check("farm-a", 100.0, check_type=check_type)
            self.assertFalse(result.allowed, f"{check_type} should be forbidden")

    def test_curtailment(self):
        self.gate.set_curtailment(0.5)
        result = self.gate.check("farm-a", 100.0)
        self.assertTrue(result.allowed)
        self.assertLess(result.flow, 100.0)

    def test_full_curtailment_denies(self):
        self.gate.set_curtailment(1.0)
        result = self.gate.check("farm-a", 100.0)
        self.assertFalse(result.allowed)

    def test_curtailment_clamps(self):
        self.gate.set_curtailment(1.5)
        self.assertAlmostEqual(self.gate._curtailment_tier, 1.0)
        self.gate.set_curtailment(-0.5)
        self.assertAlmostEqual(self.gate._curtailment_tier, 0.0)

    def test_ledger_records_every_check(self):
        self.gate.check("farm-a", 100.0)
        self.gate.check("farm-b", 50.0)
        self.gate.check("outsider", 100.0)
        self.assertEqual(len(self.gate.ledger), 3)

    def test_ledger_for_parciante(self):
        self.gate.check("farm-a", 100.0)
        self.gate.check("farm-b", 50.0)
        self.gate.check("farm-a", 200.0)
        records = self.gate.ledger_for("farm-a")
        self.assertEqual(len(records), 2)

    def test_total_flow(self):
        self.gate.check("farm-a", 100.0)
        self.gate.check("farm-b", 50.0)
        self.assertGreater(self.gate.total_flow, 0)

    def test_save_ledger(self):
        self.gate.check("farm-a", 100.0)
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            path = f.name
        self.gate.save_ledger(path)
        data = json.loads(Path(path).read_text())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["parciante"], "farm-a")
        Path(path).unlink()

    def test_conforming(self):
        self.assertTrue(self.gate.is_conforming)

    def test_not_conforming_no_parciantes(self):
        empty = Headgate("empty", "nothing")
        self.assertFalse(empty.is_conforming)

    def test_conformance_report(self):
        report = self.gate.conformance_report()
        self.assertEqual(report["gate"], "test-gate")
        self.assertTrue(report["conforming"])
        self.assertIn("identity", report["forbidden_checks"])

    def test_supply_limit(self):
        small_gate = Headgate("small", "water", total_supply=10.0)
        small_gate.add_parciante("big-ask", dependency=0.9)
        result = small_gate.check("big-ask", 1000.0)
        self.assertTrue(result.allowed)
        self.assertLessEqual(result.flow, 10.0)

    def test_summary(self):
        s = self.gate.summary()
        self.assertIn("test-gate", s)
        self.assertIn("water", s)

    def test_parciante_lookup(self):
        p = self.gate.parciante("farm-a")
        self.assertIsNotNone(p)
        self.assertAlmostEqual(p.dependency, 0.9)
        self.assertIsNone(self.gate.parciante("nonexistent"))

    def test_apply_default(self):
        result = self.gate.apply_default()
        self.assertIn("reduction", result)


class TestHeadgateChain(unittest.TestCase):
    def setUp(self):
        self.chain = HeadgateChain("test-chain")
        g1 = Headgate("link-1", "water")
        g1.add_parciante("user-a", dependency=0.8)
        g2 = Headgate("link-2", "data")
        g2.add_parciante("user-b", dependency=0.7)
        self.chain.add_link(g1).add_link(g2)

    def test_chain_length(self):
        self.assertEqual(len(self.chain.links), 2)

    def test_link_by_index(self):
        self.assertEqual(self.chain.link(0).name, "link-1")
        self.assertIsNone(self.chain.link(99))

    def test_link_by_name(self):
        self.assertEqual(self.chain.link_by_name("link-2").name, "link-2")
        self.assertIsNone(self.chain.link_by_name("nonexistent"))

    def test_conforming(self):
        self.assertTrue(self.chain.is_conforming)

    def test_conformance_report(self):
        report = self.chain.conformance_report()
        self.assertEqual(len(report), 2)

    def test_summary(self):
        s = self.chain.summary()
        self.assertIn("test-chain", s)
        self.assertIn("link-1", s)


class TestParciante(unittest.TestCase):
    def test_weight_equals_dependency(self):
        p = Parciante(name="test", dependency=0.7)
        self.assertAlmostEqual(p.weight, 0.7)


class TestRecord(unittest.TestCase):
    def test_to_dict(self):
        r = Record(
            timestamp=1000.0,
            parciante="test",
            requested=100.0,
            allowed=80.0,
            authorization="right",
            gate_name="gate",
            check_type="material",
            result="curtail",
        )
        d = r.to_dict()
        self.assertEqual(d["parciante"], "test")
        self.assertEqual(d["requested"], 100.0)
        self.assertEqual(d["result"], "curtail")


if __name__ == "__main__":
    unittest.main()
