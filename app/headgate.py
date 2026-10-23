#!/usr/bin/env python3
"""Headgate — composable governance gate using acequia primitives.

Every headgate in the chain implements five primitives:
  1. Resource     what flows through this gate (named, measured, finite)
  2. Standing     who has a seat (by dependency, not leverage)
  3. Check        what the gate measures (material, not identity)
  4. Measurement  how flow is recorded (append-only, auditable)
  5. Default      what happens on failure (protects least leverage)

This module implements the gate as code. Each headgate is a composable
unit that can be chained (snowflake to inference, 12 links).

Spec:   specs/HEADGATE-CHAIN.md
Engine: acequia.py (weir, capacitor, memristor)

Usage:
    from headgate import Headgate, Parciante, Record

    gate = Headgate(
        name="municipal-delivery",
        resource="treated water",
        unit="gallons",
        default_action="proportional_curtailment",
    )

    gate.add_parciante("residential", dependency=0.9)
    gate.add_parciante("industrial-fab", dependency=0.3)

    result = gate.check(
        parciante="residential",
        amount=100.0,
        authorization="right",
    )
    # result.allowed = True, result.flow = 100.0

    gate.ledger  # append-only record of every check
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    from acequia import Weir, Memristor
except ImportError:
    try:
        from .acequia import Weir, Memristor
    except ImportError:
        import sys as _sys
        _sys.path.insert(0, str(Path(__file__).resolve().parent))
        from acequia import Weir, Memristor


# ── Parciante ──

@dataclass
class Parciante:
    """Someone with standing at this gate. Standing comes from
    dependency, not from purchase volume or leverage."""
    name: str
    dependency: float  # 0.0-1.0, how much this entity depends on the resource
    share: float = 0.0  # allocated proportion of total flow
    metadata: dict = field(default_factory=dict)

    @property
    def weight(self) -> float:
        return self.dependency


# ── Record ──

@dataclass
class Record:
    """One entry in the gate's append-only ledger."""
    timestamp: float
    parciante: str
    requested: float
    allowed: float
    authorization: str
    gate_name: str
    check_type: str  # "material" | "authorization" | "measurement"
    result: str  # "pass" | "curtail" | "deny"
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "parciante": self.parciante,
            "requested": self.requested,
            "allowed": self.allowed,
            "authorization": self.authorization,
            "gate": self.gate_name,
            "check": self.check_type,
            "result": self.result,
            **self.metadata,
        }


# ── CheckResult ──

@dataclass
class CheckResult:
    """Result of a headgate check."""
    allowed: bool
    flow: float
    curtailed: float
    reason: str
    record: Record


# ── Headgate ──

class Headgate:
    """A composable governance gate. Five primitives, same structure
    at every link in the chain.

    The weir proportions flow. The memristor learns from history.
    The ledger records everything. The default protects the weakest.
    """

    DEFAULTS = {
        "proportional_curtailment": "All parciantes take the same percentage reduction",
        "deny": "Gate closes completely on failure",
        "pass": "Gate opens completely on failure (fail-open)",
    }

    def __init__(self, name: str, resource: str, unit: str = "units",
                 default_action: str = "proportional_curtailment",
                 total_supply: float | None = None,
                 crest: float = 0.0):
        self.name = name
        self.resource = resource
        self.unit = unit
        self.default_action = default_action
        self.total_supply = total_supply

        self._parciantes: dict[str, Parciante] = {}
        self._ledger: list[Record] = []
        self._weir = Weir(crest=crest)
        self._memristor = Memristor(initial_resistance=1.0, weathering_rate=0.005)

        self._curtailment_tier: float = 0.0  # 0.0 = no curtailment, 1.0 = full
        self._checks_forbidden: list[str] = [
            "identity", "worthiness", "political_alignment",
            "ability_to_pay_premium", "end_use_value",
        ]

    # ── Primitive 2: Standing ──

    def add_parciante(self, name: str, dependency: float = 0.5,
                      share: float = 0.0, **metadata) -> Parciante:
        p = Parciante(name=name, dependency=dependency, share=share,
                      metadata=metadata)
        self._parciantes[name] = p
        return p

    def parciante(self, name: str) -> Parciante | None:
        return self._parciantes.get(name)

    @property
    def parciantes(self) -> list[Parciante]:
        return list(self._parciantes.values())

    # ── Primitive 3: Material Check ──

    def check(self, parciante: str, amount: float,
              authorization: str = "right",
              check_type: str = "material") -> CheckResult:
        if parciante not in self._parciantes:
            record = self._record(parciante, amount, 0.0, authorization,
                                  check_type, "deny",
                                  reason="no standing")
            return CheckResult(allowed=False, flow=0.0, curtailed=amount,
                               reason="no standing at this gate", record=record)

        if check_type in self._checks_forbidden:
            record = self._record(parciante, amount, 0.0, authorization,
                                  check_type, "deny",
                                  reason="forbidden check type")
            return CheckResult(allowed=False, flow=0.0, curtailed=amount,
                               reason=f"gate does not measure {check_type}",
                               record=record)

        p = self._parciantes[parciante]

        if self._curtailment_tier > 0:
            curtailed_amount = amount * (1.0 - self._curtailment_tier)
        else:
            curtailed_amount = amount

        if self.total_supply is not None and curtailed_amount > self.total_supply:
            curtailed_amount = self.total_supply

        flow = self._memristor.flow(curtailed_amount)
        reduction = amount - curtailed_amount

        if curtailed_amount > 0:
            result_type = "curtail" if reduction > 0 else "pass"
            reason = (f"curtailed {reduction:.2f} {self.unit}"
                      if reduction > 0 else "full allocation")
            record = self._record(parciante, amount, curtailed_amount,
                                  authorization, check_type, result_type,
                                  reason=reason)
            return CheckResult(allowed=True, flow=curtailed_amount,
                               curtailed=reduction, reason=reason,
                               record=record)
        else:
            record = self._record(parciante, amount, 0.0, authorization,
                                  check_type, "deny", reason="zero allocation")
            return CheckResult(allowed=False, flow=0.0, curtailed=amount,
                               reason="zero allocation after curtailment",
                               record=record)

    # ── Primitive 5: Default ──

    def set_curtailment(self, tier: float) -> None:
        self._curtailment_tier = max(0.0, min(1.0, tier))

    def apply_default(self) -> str:
        if self.default_action == "proportional_curtailment":
            return f"All parciantes take {self._curtailment_tier*100:.0f}% reduction"
        elif self.default_action == "deny":
            return "Gate closed"
        else:
            return "Gate open (fail-open)"

    # ── Primitive 4: Measurement (ledger) ──

    def _record(self, parciante: str, requested: float, allowed: float,
                authorization: str, check_type: str, result: str,
                reason: str = "") -> Record:
        r = Record(
            timestamp=time.time(),
            parciante=parciante,
            requested=requested,
            allowed=allowed,
            authorization=authorization,
            gate_name=self.name,
            check_type=check_type,
            result=result,
            metadata={"reason": reason} if reason else {},
        )
        self._ledger.append(r)
        return r

    @property
    def ledger(self) -> list[Record]:
        return list(self._ledger)

    @property
    def total_flow(self) -> float:
        return sum(r.allowed for r in self._ledger)

    def ledger_for(self, parciante: str) -> list[Record]:
        return [r for r in self._ledger if r.parciante == parciante]

    def save_ledger(self, path: str | Path) -> None:
        path = Path(path)
        records = [r.to_dict() for r in self._ledger]
        path.write_text(json.dumps(records, indent=2))

    # ── Sovereignty Gate conformance ──

    @property
    def is_conforming(self) -> bool:
        has_parciantes = len(self._parciantes) > 0
        has_default = self.default_action in self.DEFAULTS
        has_records = True  # ledger exists by construction
        return has_parciantes and has_default and has_records

    def conformance_report(self) -> dict:
        return {
            "gate": self.name,
            "resource": self.resource,
            "parciantes": len(self._parciantes),
            "checks_recorded": len(self._ledger),
            "total_flow": self.total_flow,
            "curtailment_tier": self._curtailment_tier,
            "default": self.default_action,
            "conforming": self.is_conforming,
            "forbidden_checks": self._checks_forbidden,
        }

    # ── Chain ──

    def summary(self) -> str:
        lines = [
            f"Headgate: {self.name}",
            f"Resource: {self.resource} ({self.unit})",
            f"Parciantes: {len(self._parciantes)}",
            f"Checks: {len(self._ledger)}",
            f"Total flow: {self.total_flow:.2f} {self.unit}",
            f"Curtailment: {self._curtailment_tier*100:.0f}%",
            f"Default: {self.default_action}",
            f"Conforming: {self.is_conforming}",
        ]
        return "\n".join(lines)


# ── HeadgateChain ──

class HeadgateChain:
    """A chain of headgates from snowflake to inference.
    Same gate, every link. The resource changes; the governance doesn't.
    """

    def __init__(self, name: str = "snowflake-to-inference"):
        self.name = name
        self._links: list[Headgate] = []

    def add_link(self, gate: Headgate) -> HeadgateChain:
        self._links.append(gate)
        return self

    def link(self, index: int) -> Headgate | None:
        if 0 <= index < len(self._links):
            return self._links[index]
        return None

    def link_by_name(self, name: str) -> Headgate | None:
        for g in self._links:
            if g.name == name:
                return g
        return None

    @property
    def links(self) -> list[Headgate]:
        return list(self._links)

    @property
    def is_conforming(self) -> bool:
        return all(g.is_conforming for g in self._links)

    def conformance_report(self) -> list[dict]:
        return [g.conformance_report() for g in self._links]

    def summary(self) -> str:
        lines = [
            f"Chain: {self.name}",
            f"Links: {len(self._links)}",
            f"All conforming: {self.is_conforming}",
            "",
        ]
        for i, gate in enumerate(self._links):
            lines.append(f"  [{i+1}] {gate.name}: {gate.resource}"
                         f" ({len(gate.parciantes)} parciantes,"
                         f" {len(gate.ledger)} checks)")
        return "\n".join(lines)


# ── CLI demo ──

def demo():
    print("=" * 70)
    print("HEADGATE — COMPOSABLE GOVERNANCE GATE")
    print("=" * 70)

    # Build a 4-link chain (links 4-7 from the spec)
    chain = HeadgateChain("acequia-to-industrial")

    # Link 4: Acequia headgate
    acequia = Headgate("acequia", "allocated water", "acre-feet",
                       total_supply=1000.0)
    acequia.add_parciante("farm-a", dependency=0.9, share=0.3)
    acequia.add_parciante("farm-b", dependency=0.8, share=0.3)
    acequia.add_parciante("orchard-c", dependency=0.7, share=0.2)
    acequia.add_parciante("ranch-d", dependency=0.6, share=0.2)
    chain.add_link(acequia)

    # Link 5: Distribution
    dist = Headgate("distribution", "bulk transport", "gallons",
                    total_supply=500000.0)
    dist.add_parciante("city-of-mesa", dependency=0.8)
    dist.add_parciante("tribal-nation", dependency=0.95)
    dist.add_parciante("industrial-district", dependency=0.4)
    chain.add_link(dist)

    # Link 6: Municipal
    muni = Headgate("municipal", "treated water", "gallons",
                    total_supply=200000.0)
    muni.add_parciante("residential", dependency=0.9)
    muni.add_parciante("commercial", dependency=0.5)
    muni.add_parciante("chip-fab", dependency=0.6)
    chain.add_link(muni)

    # Link 7: Industrial
    indust = Headgate("industrial", "process water", "gallons",
                      total_supply=50000.0)
    indust.add_parciante("wafer-wash", dependency=0.95)
    indust.add_parciante("cooling", dependency=0.7)
    indust.add_parciante("facility", dependency=0.3)
    chain.add_link(indust)

    print()
    print(chain.summary())

    # Run some checks
    print(f"\n--- Normal conditions ---")
    for gate in chain.links:
        for p in gate.parciantes:
            result = gate.check(p.name, 100.0)
            print(f"  {gate.name}/{p.name}: "
                  f"{'PASS' if result.allowed else 'DENY'}"
                  f" flow={result.flow:.1f}")

    # Drought
    print(f"\n--- Drought (30% curtailment) ---")
    for gate in chain.links:
        gate.set_curtailment(0.3)

    for gate in chain.links:
        for p in gate.parciantes:
            result = gate.check(p.name, 100.0)
            print(f"  {gate.name}/{p.name}: "
                  f"flow={result.flow:.1f}"
                  f" curtailed={result.curtailed:.1f}"
                  f" ({result.reason})")

    # Try a forbidden check
    print(f"\n--- Forbidden check (identity) ---")
    result = muni.check("residential", 100.0, check_type="identity")
    print(f"  result: {'PASS' if result.allowed else 'DENY'}"
          f" — {result.reason}")

    # Try someone with no standing
    print(f"\n--- No standing ---")
    result = acequia.check("outside-speculator", 1000.0)
    print(f"  result: {'PASS' if result.allowed else 'DENY'}"
          f" — {result.reason}")

    # Conformance
    print(f"\n--- Conformance ---")
    for gate in chain.links:
        report = gate.conformance_report()
        print(f"  {report['gate']}: conforming={report['conforming']}"
              f" checks={report['checks_recorded']}"
              f" flow={report['total_flow']:.1f}")

    print(f"\n{'=' * 70}")
    print("Five primitives. Same gate, every link.")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    demo()
