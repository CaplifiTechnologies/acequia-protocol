"""DitchAI — acequia protocol infrastructure.

Modules:
    acequia     telos-bound inference primitives (weir, capacitor, etc.)
    headgate    composable governance gate (5 primitives, chain)
    mayordomo   valley/ditch planning (origami fold engine)
"""

from .acequia import (
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

from .headgate import (
    Headgate,
    HeadgateChain,
    Parciante,
    Record,
    CheckResult,
)

__version__ = "0.2"
