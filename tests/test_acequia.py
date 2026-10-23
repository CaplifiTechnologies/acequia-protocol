"""Tests for the 9 acequia inference primitives + TelosConstellation."""

from __future__ import annotations

import math
import unittest

from app.acequia import (
    Weir,
    Capacitor,
    Inductor,
    Oscillator,
    Antenna,
    Manifold,
    Memristor,
    SuperpositionGenerator,
    Spring,
    TelosConstellation,
)


class TestWeir(unittest.TestCase):
    def test_below_crest_yields_zero(self):
        w = Weir(crest=0.5)
        self.assertAlmostEqual(w.flow(0.3), 0.0)
        self.assertAlmostEqual(w.flow(0.5), 0.0)

    def test_above_crest_yields_excess(self):
        w = Weir(crest=0.5)
        self.assertAlmostEqual(w.flow(0.8), 0.3)
        self.assertAlmostEqual(w.flow(1.0), 0.5)

    def test_total_flow_accumulates(self):
        w = Weir(crest=0.5)
        w.flow(0.3)
        w.flow(0.8)
        self.assertAlmostEqual(w.total_flow, 0.3)

    def test_batch_flow(self):
        w = Weir(crest=0.5)
        results = w.batch_flow([0.3, 0.6, 0.9])
        self.assertAlmostEqual(results[0], 0.0)
        self.assertAlmostEqual(results[1], 0.1)
        self.assertAlmostEqual(results[2], 0.4)

    def test_average_flow(self):
        w = Weir(crest=0.0)
        w.flow(1.0)
        w.flow(3.0)
        self.assertAlmostEqual(w.average_flow, 2.0)

    def test_reset(self):
        w = Weir(crest=0.0)
        w.flow(1.0)
        w.reset()
        self.assertAlmostEqual(w.total_flow, 0.0)
        self.assertAlmostEqual(w.average_flow, 0.0)


class TestCapacitor(unittest.TestCase):
    def test_charge_and_discharge(self):
        c = Capacitor()
        c.charge(0.3)
        c.charge(0.5)
        self.assertAlmostEqual(c.stored, 0.8)
        released = c.discharge()
        self.assertAlmostEqual(released, 0.8)
        self.assertAlmostEqual(c.stored, 0.0)

    def test_max_charge(self):
        c = Capacitor(max_charge=1.0)
        c.charge(0.7)
        c.charge(0.5)
        self.assertAlmostEqual(c.stored, 1.0)

    def test_partial_discharge(self):
        c = Capacitor()
        c.charge(1.0)
        released = c.discharge_partial(0.3)
        self.assertAlmostEqual(released, 0.3)
        self.assertAlmostEqual(c.stored, 0.7)

    def test_partial_discharge_more_than_stored(self):
        c = Capacitor()
        c.charge(0.5)
        released = c.discharge_partial(1.0)
        self.assertAlmostEqual(released, 0.5)
        self.assertAlmostEqual(c.stored, 0.0)

    def test_charge_count(self):
        c = Capacitor()
        c.charge(0.1)
        c.charge(0.2)
        c.charge(0.3)
        self.assertEqual(c.charge_count, 3)

    def test_is_full(self):
        c = Capacitor(max_charge=1.0)
        self.assertFalse(c.is_full)
        c.charge(1.0)
        self.assertTrue(c.is_full)

    def test_unlimited_never_full(self):
        c = Capacitor()
        c.charge(999.0)
        self.assertFalse(c.is_full)


class TestInductor(unittest.TestCase):
    def test_first_input_passes_through(self):
        ind = Inductor(inductance=0.5)
        self.assertAlmostEqual(ind.apply(1.0), 1.0)

    def test_resists_change(self):
        ind = Inductor(inductance=0.5)
        ind.apply(1.0)
        effective = ind.apply(0.0)
        self.assertGreater(effective, 0.0)

    def test_direction_property(self):
        ind = Inductor()
        self.assertIsNone(ind.direction)
        ind.apply(0.5)
        self.assertIsNotNone(ind.direction)

    def test_reset(self):
        ind = Inductor()
        ind.apply(1.0)
        ind.reset()
        self.assertIsNone(ind.direction)
        self.assertAlmostEqual(ind.momentum, 0.0)


class TestOscillator(unittest.TestCase):
    def test_period_four_seasons(self):
        osc = Oscillator(period=4, amplitude=1.0)
        seasons = set()
        for _ in range(4):
            seasons.add(osc.season)
            osc.tick()
        self.assertEqual(len(seasons), 4)

    def test_dormant_when_negative(self):
        osc = Oscillator(period=4, amplitude=1.0)
        osc.tick()
        osc.tick()
        osc.tick()
        self.assertTrue(osc.is_dormant)

    def test_tick_n(self):
        osc = Oscillator(period=4)
        vals = osc.tick_n(4)
        self.assertEqual(len(vals), 4)

    def test_reset(self):
        osc = Oscillator(period=4)
        osc.tick_n(3)
        osc.reset()
        self.assertEqual(osc.season, "spring")


class TestAntenna(unittest.TestCase):
    def test_resonant_frequency_full_coupling(self):
        a = Antenna(resonance=1.0, sensitivity=1.0)
        received = a.receive(1.0, 1.0)
        self.assertAlmostEqual(received, 1.0)

    def test_off_frequency_reduced(self):
        a = Antenna(resonance=1.0, sensitivity=1.0)
        received = a.receive(1.0, 2.0)
        self.assertLess(received, 1.0)

    def test_scan(self):
        a = Antenna(resonance=1.0)
        results = a.scan([(1.0, 1.0), (1.0, 5.0)])
        self.assertEqual(len(results), 2)
        self.assertGreater(results[0], results[1])

    def test_strongest_frequency(self):
        a = Antenna(resonance=1.0)
        a.receive(1.0, 1.0)
        a.receive(1.0, 5.0)
        self.assertAlmostEqual(a.strongest_frequency, 1.0)

    def test_total_received(self):
        a = Antenna(resonance=1.0)
        a.receive(1.0, 1.0)
        a.receive(1.0, 1.0)
        self.assertAlmostEqual(a.total_received, 2.0)

    def test_retune(self):
        a = Antenna(resonance=1.0)
        a.retune(5.0)
        received = a.receive(1.0, 5.0)
        self.assertAlmostEqual(received, 1.0)

    def test_reset(self):
        a = Antenna(resonance=1.0)
        a.receive(1.0, 1.0)
        a.reset()
        self.assertIsNone(a.strongest_frequency)


class TestManifold(unittest.TestCase):
    def test_add_nodes_and_edges(self):
        m = Manifold()
        m.add_node("a").add_node("b").add_edge("a", "b")
        self.assertEqual(m.nodes, ["a", "b"])
        self.assertEqual(len(m.edges), 1)

    def test_path_exists(self):
        m = Manifold()
        m.add_node("a").add_node("b").add_node("c")
        m.add_edge("a", "b").add_edge("b", "c")
        self.assertTrue(m.path_exists("a", "c"))
        self.assertFalse(m.path_exists("a", "d"))

    def test_is_connected(self):
        m = Manifold()
        m.add_node("a").add_node("b").add_edge("a", "b")
        self.assertTrue(m.is_connected)

    def test_disconnected(self):
        m = Manifold()
        m.add_node("a").add_node("b")
        self.assertFalse(m.is_connected)

    def test_reachable(self):
        m = Manifold()
        m.add_node("a").add_node("b").add_node("c")
        m.add_edge("a", "b")
        reachable = m.reachable("a")
        self.assertIn("a", reachable)
        self.assertIn("b", reachable)
        self.assertNotIn("c", reachable)

    def test_neighbors(self):
        m = Manifold()
        m.add_node("a").add_node("b").add_node("c")
        m.add_edge("a", "b", 0.5).add_edge("a", "c", 0.3)
        neighbors = m.neighbors("a")
        self.assertEqual(len(neighbors), 2)

    def test_invalid_edge_raises(self):
        m = Manifold()
        m.add_node("a")
        with self.assertRaises(ValueError):
            m.add_edge("a", "nonexistent")

    def test_empty_is_connected(self):
        m = Manifold()
        self.assertTrue(m.is_connected)


class TestMemristor(unittest.TestCase):
    def test_weathering_reduces_resistance(self):
        m = Memristor(initial_resistance=1.0, weathering_rate=0.1)
        m.flow(1.0)
        self.assertLess(m.resistance, 1.0)

    def test_output_increases_with_weathering(self):
        m = Memristor(initial_resistance=1.0, weathering_rate=0.1)
        first = m.flow(1.0)
        second = m.flow(1.0)
        self.assertGreater(second, first)

    def test_is_seasoned(self):
        m = Memristor(initial_resistance=1.0, weathering_rate=0.1)
        for _ in range(10):
            m.flow(1.0)
        self.assertTrue(m.is_seasoned)

    def test_resistance_floor(self):
        m = Memristor(initial_resistance=0.1, weathering_rate=1.0)
        m.flow(1.0)
        self.assertGreaterEqual(m.resistance, 0.01)

    def test_flow_count(self):
        m = Memristor()
        m.flow(1.0)
        m.flow(2.0)
        self.assertEqual(m.flow_count, 2)

    def test_total_flow(self):
        m = Memristor()
        m.flow(1.0)
        m.flow(2.0)
        self.assertAlmostEqual(m.total_flow, 3.0)

    def test_reset(self):
        m = Memristor()
        m.flow(1.0)
        m.reset()
        self.assertEqual(m.flow_count, 0)


class TestSuperpositionGenerator(unittest.TestCase):
    def test_load_and_collapse(self):
        sg = SuperpositionGenerator()
        sg.load("path_a", 1.0).load("path_b", 0.5)
        result = sg.collapse(lambda p: 1.0 if p == "path_a" else 0.5)
        self.assertEqual(result, "path_a")
        self.assertTrue(sg.is_collapsed)

    def test_collapse_empty_raises(self):
        sg = SuperpositionGenerator()
        with self.assertRaises(RuntimeError):
            sg.collapse(lambda p: 1.0)

    def test_load_after_collapse_raises(self):
        sg = SuperpositionGenerator()
        sg.load("a")
        sg.collapse(lambda p: 1.0)
        with self.assertRaises(RuntimeError):
            sg.load("b")

    def test_path_count(self):
        sg = SuperpositionGenerator()
        sg.load("a").load("b").load("c")
        self.assertEqual(sg.path_count, 3)

    def test_paths_list(self):
        sg = SuperpositionGenerator()
        sg.load("x").load("y")
        self.assertEqual(sg.paths, ["x", "y"])

    def test_result_before_collapse_is_none(self):
        sg = SuperpositionGenerator()
        sg.load("a")
        self.assertIsNone(sg.result)

    def test_reset(self):
        sg = SuperpositionGenerator()
        sg.load("a")
        sg.collapse(lambda p: 1.0)
        sg.reset()
        self.assertFalse(sg.is_collapsed)
        self.assertEqual(sg.path_count, 0)

    def test_load_many(self):
        sg = SuperpositionGenerator()
        sg.load_many(["a", "b", "c"])
        self.assertEqual(sg.path_count, 3)


class TestSpring(unittest.TestCase):
    def test_charge_and_trigger(self):
        s = Spring(telos="test", crest=0.5)
        s.charge(1.0)
        self.assertTrue(s.is_charged)
        result = s.trigger(alignment=0.8)
        self.assertTrue(result["fired"])
        self.assertGreater(result["flow"], 0)

    def test_below_crest_does_not_fire(self):
        s = Spring(telos="test", crest=0.5)
        s.charge(1.0)
        result = s.trigger(alignment=0.3)
        self.assertFalse(result["fired"])

    def test_trigger_with_paths(self):
        s = Spring(telos="test", crest=0.5)
        s.charge(1.0)
        s.load_path("path_a").load_path("path_b")
        result = s.trigger(alignment=0.8)
        self.assertTrue(result["fired"])
        self.assertIn("collapsed_to", result)

    def test_trigger_count(self):
        s = Spring(telos="test", crest=0.0)
        s.trigger(alignment=0.5)
        s.trigger(alignment=0.5)
        self.assertEqual(s.trigger_count, 2)

    def test_history(self):
        s = Spring(telos="test", crest=0.0)
        s.trigger(alignment=0.5)
        self.assertEqual(len(s.history), 1)


class TestTelosConstellation(unittest.TestCase):
    def test_add_stars_and_connect(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a")
        c.add_star("b", "purpose b")
        c.connect("a", "b")
        self.assertEqual(c.stars, ["a", "b"])
        self.assertTrue(c.is_bound)

    def test_alignment(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a", weight=1.0)
        c.add_star("b", "purpose b", weight=1.0)
        score = c.alignment({"a": 1.0, "b": 0.5})
        self.assertAlmostEqual(score, 0.75)

    def test_charge_and_trigger_star(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a", crest=0.5)
        c.charge_star("a", 1.0)
        result = c.trigger_star("a", 0.8)
        self.assertTrue(result["fired"])

    def test_invalid_star_raises(self):
        c = TelosConstellation("test")
        with self.assertRaises(ValueError):
            c.charge_star("nonexistent", 1.0)

    def test_season_and_tick(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a")
        season = c.season()
        self.assertIn(season, ["spring", "summer", "fall", "winter"])
        c.tick()

    def test_inertia(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a")
        result = c.inertia(1.0)
        self.assertAlmostEqual(result, 1.0)

    def test_receive(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a")
        received = c.receive(1.0, 1.0)
        self.assertIsInstance(received, float)

    def test_unbound_when_empty(self):
        c = TelosConstellation("test")
        self.assertFalse(c.is_bound)

    def test_summary(self):
        c = TelosConstellation("test")
        c.add_star("a", "purpose a")
        s = c.summary()
        self.assertIn("test", s)
        self.assertIn("purpose a", s)


if __name__ == "__main__":
    unittest.main()
