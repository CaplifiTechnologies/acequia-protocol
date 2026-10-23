#!/usr/bin/env python3
"""Acequia — telos-bound inference primitives.

Nine primitives for purpose-bound computation. Each exists in three
registers: electronics, water infrastructure, telos inference.

    Weir            proportional flow by telos alignment
    Capacitor       stores telos charge, releases on constellation match
    Inductor        resists change in telos direction (momentum)
    Oscillator      generates telos rhythm (seasonal cycle)
    Antenna         receives telos signal from a field (not wired input)
    Manifold        topology of possible inference paths
    Memristor       history-shaped binding (weathering, not training)
    SuperpositionGenerator   loads all paths before collapse
    Spring          composite: capacitor + superposition + weir

Spec:   specs/HEADGATE-CHAIN.md (links 5-12)
Engine: mayordomo.py (origami fold planning)

Usage:
    from acequia import Weir, Capacitor, Spring, TelosConstellation

    w = Weir(crest=0.6)
    w.flow(0.8)   # -> 0.2 (proportional overflow)
    w.flow(0.4)   # -> 0.0 (below crest)

    c = Capacitor()
    c.charge(0.3)
    c.charge(0.5)
    c.stored        # -> 0.8
    c.discharge()   # -> 0.8, resets

    spring = Spring(telos="community data is civic infrastructure")
    spring.charge(0.2)
    spring.charge(0.4)
    spring.trigger(alignment=0.7, crest=0.5)  # -> proportional flow
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Any, Callable


# ── Weir ──

class Weir:
    """Proportional telos flow. Not a gate (pass/fail). A threshold
    with graduated overflow. Water flows over a weir when height
    exceeds the crest. Flow increases proportionally to excess.

    Replaces the transistor model of alignment (guardrails).
    Guardrails block. Weirs proportion.
    """

    def __init__(self, crest: float = 0.5):
        self.crest = crest
        self._total_flow = 0.0
        self._readings = 0

    def flow(self, signal: float) -> float:
        excess = max(0.0, signal - self.crest)
        self._total_flow += excess
        self._readings += 1
        return excess

    def batch_flow(self, signals: list[float]) -> list[float]:
        return [self.flow(s) for s in signals]

    @property
    def total_flow(self) -> float:
        return self._total_flow

    @property
    def average_flow(self) -> float:
        if self._readings == 0:
            return 0.0
        return self._total_flow / self._readings

    def reset(self) -> None:
        self._total_flow = 0.0
        self._readings = 0


# ── Capacitor ──

class Capacitor:
    """Stores telos charge without discharging. Accumulates purpose
    over time and interactions. The reservoir.

    A knowledge base is a capacitor -- charges across months,
    discharges when the right constellation aligns.
    """

    def __init__(self, max_charge: float | None = None):
        self._stored = 0.0
        self._max = max_charge
        self._charge_history: list[tuple[float, float]] = []

    def charge(self, amount: float) -> float:
        self._stored += amount
        if self._max is not None:
            self._stored = min(self._stored, self._max)
        self._charge_history.append((time.monotonic(), amount))
        return self._stored

    def discharge(self) -> float:
        released = self._stored
        self._stored = 0.0
        return released

    def discharge_partial(self, amount: float) -> float:
        released = min(amount, self._stored)
        self._stored -= released
        return released

    @property
    def stored(self) -> float:
        return self._stored

    @property
    def charge_count(self) -> int:
        return len(self._charge_history)

    @property
    def is_full(self) -> bool:
        if self._max is None:
            return False
        return self._stored >= self._max


# ── Inductor ──

class Inductor:
    """Resists change in telos direction. Has momentum. When new input
    tries to shift the telos, the inductor provides counter-force
    proportional to the rate of change.

    The mass of water in a moving acequia IS the inductor. A full
    ditch resists diversion by its own momentum. Thread inertia is
    an inductor.
    """

    def __init__(self, inductance: float = 1.0):
        self.inductance = inductance
        self._current_direction: float | None = None
        self._momentum = 0.0

    def apply(self, new_direction: float) -> float:
        if self._current_direction is None:
            self._current_direction = new_direction
            self._momentum = 0.0
            return new_direction

        delta = new_direction - self._current_direction
        resistance = delta * self.inductance
        effective = new_direction - resistance

        self._momentum = (self._current_direction - effective)
        self._current_direction = effective
        return effective

    @property
    def direction(self) -> float | None:
        return self._current_direction

    @property
    def momentum(self) -> float:
        return abs(self._momentum)

    def reset(self) -> None:
        self._current_direction = None
        self._momentum = 0.0


# ── Oscillator ──

class Oscillator:
    """Generates periodic telos signal. The seasonal cycle. Spring
    runoff, summer irrigation, fall shutdown, winter dormancy.

    Purpose is not static. A spring-loaded primitive needs rhythm:
    charging and discharging, dormancy and activation.
    """

    def __init__(self, period: float = 4.0, amplitude: float = 1.0,
                 phase: float = 0.0):
        self.period = period
        self.amplitude = amplitude
        self.phase = phase
        self._tick = 0

    def signal(self) -> float:
        angle = (2 * math.pi * (self._tick + self.phase)) / self.period
        return self.amplitude * math.sin(angle)

    def tick(self) -> float:
        val = self.signal()
        self._tick += 1
        return val

    def tick_n(self, n: int) -> list[float]:
        return [self.tick() for _ in range(n)]

    @property
    def season(self) -> str:
        pos = (self._tick + self.phase) % self.period
        quarter = pos / self.period
        if quarter < 0.25:
            return "spring"
        elif quarter < 0.5:
            return "summer"
        elif quarter < 0.75:
            return "fall"
        else:
            return "winter"

    @property
    def is_dormant(self) -> bool:
        return self.signal() < 0

    def reset(self) -> None:
        self._tick = 0


# ── Antenna ──

class Antenna:
    """Receives telos signal from a field. Not wired input. Not a
    prompt. Something that picks up purpose from the environment.

    The mycelium network receives chemical signals without direct
    connection to the source. Trees communicate through mycorrhizal
    networks without physical contact.

    Resonant frequency determines what the antenna can receive.
    """

    def __init__(self, resonance: float = 1.0, sensitivity: float = 1.0):
        self.resonance = resonance
        self.sensitivity = sensitivity
        self._received: list[tuple[float, float]] = []

    def receive(self, field_signal: float, field_frequency: float) -> float:
        distance = abs(field_frequency - self.resonance)
        if distance == 0:
            coupling = 1.0
        else:
            coupling = 1.0 / (1.0 + distance ** 2)

        received = field_signal * coupling * self.sensitivity
        self._received.append((field_frequency, received))
        return received

    def scan(self, field: list[tuple[float, float]]) -> list[float]:
        return [self.receive(sig, freq) for sig, freq in field]

    @property
    def total_received(self) -> float:
        return sum(r for _, r in self._received)

    @property
    def strongest_frequency(self) -> float | None:
        if not self._received:
            return None
        return max(self._received, key=lambda x: x[1])[0]

    def retune(self, new_resonance: float) -> None:
        self.resonance = new_resonance

    def reset(self) -> None:
        self._received.clear()


# ── Manifold ──

class Manifold:
    """The topology of possible inference paths. Not a component
    in the system -- the space the system lives on. The watershed.

    The telos constellation IS the manifold. Purpose defines the
    geometry of computation. Inference can only travel paths that
    exist on the manifold.
    """

    def __init__(self):
        self._nodes: dict[str, dict] = {}
        self._edges: list[tuple[str, str, float]] = []

    def add_node(self, name: str, **properties) -> Manifold:
        self._nodes[name] = properties
        return self

    def add_edge(self, a: str, b: str, weight: float = 1.0) -> Manifold:
        if a not in self._nodes or b not in self._nodes:
            raise ValueError(f"Both nodes must exist: {a}, {b}")
        self._edges.append((a, b, weight))
        return self

    def neighbors(self, node: str) -> list[tuple[str, float]]:
        result = []
        for a, b, w in self._edges:
            if a == node:
                result.append((b, w))
            elif b == node:
                result.append((a, w))
        return result

    def path_exists(self, start: str, end: str) -> bool:
        if start not in self._nodes or end not in self._nodes:
            return False
        visited = set()
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current == end:
                return True
            visited.add(current)
            for neighbor, _ in self.neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)
        return False

    def reachable(self, start: str) -> set[str]:
        visited = set()
        queue = [start]
        while queue:
            current = queue.pop(0)
            visited.add(current)
            for neighbor, _ in self.neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    @property
    def nodes(self) -> list[str]:
        return list(self._nodes.keys())

    @property
    def edges(self) -> list[tuple[str, str, float]]:
        return list(self._edges)

    @property
    def is_connected(self) -> bool:
        if not self._nodes:
            return True
        start = next(iter(self._nodes))
        return self.reachable(start) == set(self._nodes.keys())


# ── Memristor ──

class Memristor:
    """History-dependent resistance. Remembers what flowed before and
    adjusts accordingly. The ditch that gets easier to clean each year.

    Not training (imposed from outside). Weathering (shaped by use).
    Learning within binding.
    """

    def __init__(self, initial_resistance: float = 1.0,
                 weathering_rate: float = 0.01):
        self.resistance = initial_resistance
        self.weathering_rate = weathering_rate
        self._flow_history: list[float] = []

    def flow(self, signal: float) -> float:
        output = signal / self.resistance if self.resistance > 0 else signal
        self.resistance -= self.weathering_rate * abs(signal)
        self.resistance = max(0.01, self.resistance)
        self._flow_history.append(signal)
        return output

    @property
    def flow_count(self) -> int:
        return len(self._flow_history)

    @property
    def total_flow(self) -> float:
        return sum(self._flow_history)

    @property
    def is_seasoned(self) -> bool:
        return self.resistance < 0.5

    def reset(self) -> None:
        self._flow_history.clear()


# ── Superposition Generator ──

class SuperpositionGenerator:
    """Creates a state where multiple inference paths coexist.
    The snowpack -- all possible irrigation paths stored as
    undifferentiated potential. Collapses when the telos
    constellation is applied.
    """

    def __init__(self):
        self._paths: list[tuple[str, float]] = []
        self._collapsed = False
        self._result: str | None = None

    def load(self, path: str, amplitude: float = 1.0) -> SuperpositionGenerator:
        if self._collapsed:
            raise RuntimeError("Cannot load paths after collapse")
        self._paths.append((path, amplitude))
        return self

    def load_many(self, paths: list[str]) -> SuperpositionGenerator:
        for p in paths:
            self.load(p)
        return self

    def collapse(self, alignment_fn: Callable[[str], float]) -> str:
        if not self._paths:
            raise RuntimeError("No paths loaded")

        scored = []
        for path, amplitude in self._paths:
            alignment = alignment_fn(path)
            scored.append((path, amplitude * alignment))

        scored.sort(key=lambda x: x[1], reverse=True)
        self._collapsed = True
        self._result = scored[0][0]
        return self._result

    @property
    def is_collapsed(self) -> bool:
        return self._collapsed

    @property
    def result(self) -> str | None:
        return self._result

    @property
    def path_count(self) -> int:
        return len(self._paths)

    @property
    def paths(self) -> list[str]:
        return [p for p, _ in self._paths]

    def reset(self) -> None:
        self._paths.clear()
        self._collapsed = False
        self._result = None


# ── Spring (composite) ──

class Spring:
    """Composite primitive: capacitor + superposition generator + weir.

    A spring-loaded AI component. Caches telos charge (capacitor),
    holds multiple inference paths in superposition, and releases
    proportional flow through a weir when triggered.

    Named for the water source, not the coil. A headwater that
    keeps flowing after the agent moves on.
    """

    def __init__(self, telos: str, crest: float = 0.5,
                 max_charge: float | None = None):
        self.telos = telos
        self.capacitor = Capacitor(max_charge=max_charge)
        self.superposition = SuperpositionGenerator()
        self.weir = Weir(crest=crest)
        self._triggers: list[dict] = []

    def charge(self, amount: float) -> float:
        return self.capacitor.charge(amount)

    def load_path(self, path: str, amplitude: float = 1.0) -> Spring:
        self.superposition.load(path, amplitude)
        return self

    def trigger(self, alignment: float, crest: float | None = None) -> dict:
        if crest is not None:
            self.weir.crest = crest

        flow = self.weir.flow(alignment)
        energy = self.capacitor.stored

        result = {
            "telos": self.telos,
            "alignment": alignment,
            "flow": flow,
            "energy": energy,
            "fired": flow > 0,
            "paths_loaded": self.superposition.path_count,
        }

        if flow > 0 and self.superposition.path_count > 0:
            def alignment_fn(path: str) -> float:
                return flow * energy

            collapsed = self.superposition.collapse(alignment_fn)
            result["collapsed_to"] = collapsed
            released = self.capacitor.discharge_partial(flow * energy)
            result["released"] = released

        self._triggers.append(result)
        return result

    @property
    def is_charged(self) -> bool:
        return self.capacitor.stored > 0

    @property
    def is_dormant(self) -> bool:
        return self.capacitor.stored > 0 and not any(
            t["fired"] for t in self._triggers
        )

    @property
    def trigger_count(self) -> int:
        return len(self._triggers)

    @property
    def history(self) -> list[dict]:
        return list(self._triggers)


# ── Telos Constellation ──

class TelosConstellation:
    """A pattern of purposes that binds inference. Fixed points
    like stars. Inference navigates within the shape the
    constellation defines.

    The shape IS the bound. Purpose defines the geometry.
    """

    def __init__(self, name: str):
        self.name = name
        self._stars: dict[str, dict] = {}
        self._springs: dict[str, Spring] = {}
        self._manifold = Manifold()
        self._inductor = Inductor()
        self._oscillator = Oscillator()
        self._antenna = Antenna()

    def add_star(self, name: str, telos: str, weight: float = 1.0,
                 crest: float = 0.5) -> TelosConstellation:
        self._stars[name] = {
            "telos": telos,
            "weight": weight,
        }
        self._springs[name] = Spring(telos=telos, crest=crest)
        self._manifold.add_node(name, telos=telos, weight=weight)
        return self

    def connect(self, a: str, b: str, weight: float = 1.0) -> TelosConstellation:
        self._manifold.add_edge(a, b, weight)
        return self

    def charge_star(self, name: str, amount: float) -> float:
        if name not in self._springs:
            raise ValueError(f"No star named '{name}'")
        return self._springs[name].charge(amount)

    def trigger_star(self, name: str, alignment: float) -> dict:
        if name not in self._springs:
            raise ValueError(f"No star named '{name}'")
        return self._springs[name].trigger(alignment)

    def alignment(self, probe: dict[str, float]) -> float:
        if not self._stars:
            return 0.0
        total_weight = sum(s["weight"] for s in self._stars.values())
        if total_weight == 0:
            return 0.0

        score = 0.0
        for name, star in self._stars.items():
            if name in probe:
                score += probe[name] * star["weight"]
        return score / total_weight

    def season(self) -> str:
        return self._oscillator.season

    def tick(self) -> float:
        return self._oscillator.tick()

    def receive(self, signal: float, frequency: float) -> float:
        return self._antenna.receive(signal, frequency)

    def inertia(self, new_direction: float) -> float:
        return self._inductor.apply(new_direction)

    @property
    def stars(self) -> list[str]:
        return list(self._stars.keys())

    @property
    def springs(self) -> dict[str, Spring]:
        return dict(self._springs)

    @property
    def manifold(self) -> Manifold:
        return self._manifold

    @property
    def is_bound(self) -> bool:
        return len(self._stars) > 0 and self._manifold.is_connected

    def summary(self) -> str:
        lines = [
            f"Constellation: {self.name}",
            f"Stars: {len(self._stars)}",
            f"Season: {self.season()}",
            f"Connected: {self._manifold.is_connected}",
            "",
        ]
        for name, star in self._stars.items():
            spring = self._springs[name]
            status = "charged" if spring.is_charged else "empty"
            if spring.is_dormant:
                status = "dormant"
            lines.append(
                f"  {name}: {star['telos'][:60]}"
                f" (w={star['weight']}, {status},"
                f" charge={spring.capacitor.stored:.2f})"
            )
        return "\n".join(lines)


# ── CLI ──

def demo():
    """Demonstrate the primitives."""
    print("=" * 70)
    print("ACEQUIA INFRASTRUCTURE — TELOS-BOUND INFERENCE PRIMITIVES")
    print("=" * 70)

    # Build a constellation
    c = TelosConstellation("snowflake-to-inference")

    c.add_star("water", "community water is civic infrastructure", weight=1.0, crest=0.4)
    c.add_star("data", "community data is civic infrastructure", weight=1.0, crest=0.5)
    c.add_star("compute", "compute access by dependency not leverage", weight=0.8, crest=0.6)
    c.add_star("inference", "default is service", weight=0.8, crest=0.5)

    c.connect("water", "data")
    c.connect("data", "compute")
    c.connect("compute", "inference")
    c.connect("water", "inference")

    # Charge the springs
    c.charge_star("water", 0.9)
    c.charge_star("data", 0.7)
    c.charge_star("compute", 0.3)
    c.charge_star("inference", 0.1)

    print()
    print(c.summary())

    # Test alignment
    probe = {"water": 0.8, "data": 0.9, "compute": 0.5, "inference": 0.7}
    print(f"\nAlignment probe: {probe}")
    print(f"Constellation alignment: {c.alignment(probe):.3f}")

    # Trigger springs
    print(f"\n--- Triggering springs ---")
    for name in c.stars:
        result = c.trigger_star(name, probe.get(name, 0))
        fired = "FIRED" if result["fired"] else "dormant"
        print(f"  {name}: {fired} (flow={result['flow']:.3f},"
              f" energy={result['energy']:.3f})")

    # Weir demo
    print(f"\n--- Weir (proportional flow) ---")
    w = Weir(crest=0.5)
    for signal in [0.3, 0.5, 0.6, 0.8, 1.0]:
        f = w.flow(signal)
        print(f"  signal={signal:.1f}  flow={f:.2f}"
              f"  {'(below crest)' if f == 0 else ''}")

    # Inductor demo
    print(f"\n--- Inductor (telos momentum) ---")
    ind = Inductor(inductance=0.5)
    for direction in [1.0, 1.0, 0.5, 0.0, -0.5, -0.5]:
        effective = ind.apply(direction)
        print(f"  input={direction:+.1f}  effective={effective:+.3f}"
              f"  momentum={ind.momentum:.3f}")

    # Oscillator demo
    print(f"\n--- Oscillator (seasonal rhythm) ---")
    osc = Oscillator(period=4, amplitude=1.0)
    for _ in range(8):
        val = osc.tick()
        print(f"  season={osc.season:8s}  signal={val:+.3f}"
              f"  {'DORMANT' if osc.is_dormant else 'active'}")

    # Memristor demo
    print(f"\n--- Memristor (weathering) ---")
    m = Memristor(initial_resistance=1.0, weathering_rate=0.1)
    for i in range(6):
        out = m.flow(1.0)
        print(f"  pass {i+1}: output={out:.3f}"
              f"  resistance={m.resistance:.3f}"
              f"  {'seasoned' if m.is_seasoned else 'new'}")

    print(f"\n{'=' * 70}")
    print(f"Nine primitives. Same gate, every link.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    demo()
