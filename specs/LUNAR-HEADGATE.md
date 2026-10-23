# Lunar Headgate Protocol

**Acequia Protocol governance applied to lunar resource management.**

Status: DRAFT (spec proposal)
Date: 2026-09-13
Depends on: SOVEREIGNTY-GATE.md, HEADGATE-CHAIN.md, COMMUNITY-DECISION.md
Companion research: ~/claude-landing/2026-09-13/lunar-governance-research.md

---

## The problem

Eleven published governance frameworks exist for lunar resources. None of them
solve the actual problem: what happens when two missions want the same ice.

The Artemis Accords have 71 signatories and zero enforcement. The COPUOS Working
Group has been negotiating for five years and will produce non-binding principles
with bracketed (contested) provisions. The PNAS Mining Code presumes an
intergovernmental authority that does not exist. Open Lunar's DLA framework is
the most operationally detailed proposal and still has no institution behind it.

Meanwhile, crewed Artemis landings (~2028) will establish precedent at the south
pole 1-2 years before any governance framework finalizes. Facts on the ground
will precede rules in writing.

The moon has a water problem. Lunar water ice is:

- **Finite** -- deposited over geological time, consumed in hours
- **Concentrated** -- fewer than ten high-value cold trap sites exist
- **Non-renewable** -- on any human timescale
- **Positional** -- you need the crater, not just "lunar water rights"
- **Enabling** -- water = propellant = the logistics backbone for everything deeper

Every existing framework treats water ice the same as regolith. Only two (PNAS
Mining Code, Open Lunar DLAs) address it specifically. Neither solves shortage
allocation, independent verification, or operator accountability.

The gap: no framework answers who cuts back when the ice runs low.

---

## What happened last time

The American West is the closest precedent for what is about to happen on the
moon. A finite, positional, enabling resource (water) in a territory where
sovereignty was contested and the existing governance was overridden by the
most powerful arriving actors.

Three governance models competed:

### 1. Riparian rights (eastern import, 1840s-1860s)

The Eastern model: you have water rights because your land is adjacent to the
stream. Assumes abundance -- there is enough for everyone along the bank.

Collapsed immediately in the West. In an arid landscape, the upstream user could
dry out everyone downstream. Adjacency-based allocation only works when the
resource exceeds demand. The moon has no abundance assumption.

**Lunar analog:** The Outer Space Treaty's "freedom of exploration and use" is
riparian thinking. It assumes the moon is big enough that everyone can operate
without interfering. That assumption fails the moment two missions target the
same permanently shadowed crater.

### 2. Prior appropriation (mining camps, 1850s-present)

"First in time, first in right." You get water rights by diverting it and
putting it to "beneficial use." The first claimant has senior rights; in a
shortage, junior rights get cut before senior rights lose a drop.

Born in California gold camps -- extralegal rules made by miners, later codified
into state law. The Mining Law of 1872 extended the same logic to hard-rock
minerals on public land: discover it, stake it, work it, own it. No rent to the
public. Still in effect.

What it produced:

- **Concentration.** Mining companies and railroads accumulated senior water
  rights across entire basins. The pattern was consistent: the actor with the
  most capital and earliest access captured the resource, then sold access
  to later arrivals.
- **Exclusion.** Indigenous water rights were not recognized until the Winters
  Doctrine (1908), and not enforced for decades after. Acequia water rights
  were systematically overridden by Anglo appropriation courts. Communities
  that had managed water for 250 years were told their use was not
  "beneficial" because it was communal.
- **Interstate conflict.** The Colorado River Compact (1922) took 80 years of
  water wars to negotiate, was based on anomalously wet years, and is now
  failing. The compact allocated more water than the river produces.
- **Regulatory capture.** "Beneficial use" was defined by the dominant users
  (mining, agriculture, municipal) to exclude indigenous, communal, and
  ecological uses. The definition served the definer.

**Lunar analog:** This is what is happening right now.

| Western prior appropriation | Lunar governance (2026) |
|----|-----|
| Mining claims on public land | Artemis Accords safety zones |
| "Beneficial use" defined by miners | "Space resources" defined by spacefaring nations |
| First-come, first-served | Hague Building Block 7 (priority rights via registry) |
| No rent to the public | No mandatory benefit sharing (Artemis, Hague) |
| Junior rights cut first in shortage | No shortage mechanism at all |
| Mining Law of 1872 | US SPACE Act of 2015 |
| Winters Doctrine (60 years late) | Developing nation participation (TBD) |
| Colorado River Compact (80 years late) | COPUOS framework (still negotiating) |

The Artemis Accords are bilateral agreements between the most powerful
spacefaring nation and its partners. Safety zones are deliberately
underspecified -- no radius, no duration, no revocation conditions. Section 10
affirms that extraction is not appropriation, using the exact same logic as
"beneficial use": we are not claiming the land, just everything we take from it.

China and Russia are building a parallel program (ILRS) with no coordination
mechanism with Artemis. This is the Colorado River Compact problem before the
compact -- multiple sovereigns drawing from the same basin with no shared
accounting.

### 3. Acequia (predated both by 250 years, still operating)

Community-built, community-governed irrigation infrastructure. Operating
continuously in New Mexico and Colorado since the 1600s. Nobody owns the ditch.
The ditch serves the community. The community governs the ditch.

Core mechanics:

- **Proportional allocation.** Water is distributed by proportion of declared
  rights (typically tied to irrigated acreage), not by seniority or wealth.
- **Repartimiento.** When water runs short, everyone cuts proportionally. No
  senior/junior distinction. The rancher with 100 acres cuts ten times more
  than the farmer with 10 acres, but the percentage is the same.
- **Mayordomo accountability.** The ditch boss (operator) is elected by the
  parciantes (community members), serves at their pleasure, and can be
  replaced. The operator does not own the infrastructure or the resource.
- **Community governance.** Access policy is set by the parciantes, not by
  the operator, the state, or the largest user.
- **Compuerta.** Each parciante's own valve. Override belongs to the
  rights-holder, not to the system.

What it produced:

- The most resilient water infrastructure in the American West. Acequia
  communities that maintained their governance have survived droughts that
  collapsed prior-appropriation systems.
- Continuous operation for 400+ years without the concentration, exclusion,
  or interstate conflict produced by prior appropriation.
- A governance model that is pre-partisan: no political faction can claim
  it or oppose it without contradiction.

The acequia was not replaced because it failed. It was replaced because
prior appropriation served the interests of the arriving power. The
governance that worked was overridden by the governance that extracted.

**Lunar analog:** The acequia is the model that skips 150 years of conflict
by starting with community governance instead of arriving at it after the
resource is exhausted.

---

## The spec

### Telos

**Telos:** Lunar water ice is finite shared infrastructure. Its governance
serves the sustained accessibility of the resource for all participants, not
the maximum extraction rate for the first arrival.

**Anti-telos:** Permanent monopoly control of a non-renewable, enabling
resource by the actor with the earliest access and the most capital.

The telos is declared by the participating communities (parciantes), not
by the operators. The operator serves the declared purpose; they do not
get to define it. Human-only minting rule applies: agents, automated
systems, and operator algorithms do not submit teloi.

### Governance roles

Mapped from Acequia Protocol roles (see ~/DitchAI/GOVERNANCE-BY-TELOS.md):

| Acequia role | Lunar Headgate role | Function |
|---|---|---|
| **Ditch Commission** (Ditch AI) | **Lunar Governance Standards Body** | Sets specs, certifies operators, audits compliance. Never touches extraction revenue. Cannot be acquired (structured like a library, not a corporation). |
| **Mayordomo** | **Certified Extraction Operator** | The entity running extraction at a site. Bound to governance spec. Auditable. Fireable. Replaceable. Licensed per-site, not per-organization. SpaceX, CNSA, ISRO, Roscosmos, Astrobotic -- all are mayordomo candidates. None own the resource. |
| **Parciantes** | **Participating Nations/Communities** | The nations and communities with declared rights to the resource zone. Own the access policy. Vote on allocation. Choose and replace the operator. Rights are proportional, not equal -- but proportion is declared and contested through the constellation mechanism, not assigned by who arrived first. |

### Governed resource: lunar water ice zones

Each high-value cold trap site is a governed resource zone. The zone carries:

1. **Telos declaration** -- what the resource is for (submitted by parciantes)
2. **Rights register** -- declared proportional rights of each parciante
3. **Operator license** -- which certified mayordomo runs extraction
4. **Extraction ledger** -- append-only record of what was extracted, by whom, verified independently
5. **Shortage protocol** -- repartimiento rules for when supply falls below demand

Zone boundaries are defined by the resource, not by the operator's footprint.
This is distinct from safety zones (which define the operational buffer around
equipment). The headgate governs the ice; the safety zone governs the hardware.
Conflating them is how "temporary operational buffer" becomes "permanent
territorial control."

### Mechanisms

#### 1. Headgate (access control)

The hard fail-closed edge for the resource zone. Nothing flows without
authorization. Mapped from HEADGATE-CHAIN.md.

- **Deterministic gate.** Access checked against the rights register and
  the operator's license. No discretionary override by the operator.
- **Append-only audit.** Every access event logged with immutable integrity.
  The extraction ledger is the audit trail.
- **Fail-closed default.** If the gate cannot verify authorization, no
  extraction proceeds. This protects the resource, not the operator.
- **Community authorization.** The parciantes set the access policy. The
  operator executes it. The standards body certifies compliance.

#### 2. Repartimiento (shortage allocation)

**The single most important mechanism missing from every published framework.**

When ice supply in a zone falls below aggregate demand:

1. Shortage is declared based on independent measurement (flume, not
   operator self-report).
2. Each parciante's allocation is reduced proportionally to their
   declared rights. A nation with 20% of declared rights takes a 20%
   cut. A nation with 5% takes a 5% cut.
3. No senior/junior distinction. First arrival does not confer shortage
   immunity.
4. Reduction applies to the operator's extraction license, not to the
   parciante's rights. Rights persist; the flow is adjusted.
5. Shortage protocol is declared in advance as part of the zone's
   governance, not negotiated during the crisis.

What this prevents: the scenario where the most powerful actor maintains
full extraction while smaller participants are cut off entirely. This is
what prior appropriation does (senior rights cut last), and it is what
will happen under the Artemis Accords if shortage is negotiated
bilaterally between the US and each signatory.

#### 3. Sovereignty Gate (identity exclusion prevention)

Mapped from SOVEREIGNTY-GATE.md. Three rules applied to every gate in the
protocol:

1. **Material question only.** The gate checks what you are doing (extraction
   rate, compliance with license, environmental limits), not who you are.
   Whether a nation signed the Artemis Accords is not a material question
   for resource access. Whether their operator is certified and their
   extraction is within licensed parameters is.

2. **Default protects least leverage.** When a measurement is missing or a
   system is down, the default preserves the position of the participant
   with the least ability to absorb an adverse outcome. Not always open,
   not always closed -- always protective of the smallest parciante.

3. **Override to rights-holder.** The parciante can open or close their own
   compuerta. Override belongs to the community whose rights are at stake,
   not to the operator, the standards body, or the most powerful signatory.

Anti-pattern: "A gate that can answer 'who are you' will eventually be used
to answer that instead of 'what is this.'" The Artemis Accords are already
an identity gate -- access to coordination is contingent on signing a
bilateral agreement with the United States. The Sovereignty Gate prevents
this by construction.

#### 4. Attestation (independent verification)

No one grades their own work. The party with no stake attests.

- Extraction volumes reported by the operator are verified by an
  independent measurement authority (the flume).
- Compliance with environmental limits is attested by a party that does
  not benefit from the extraction.
- The standards body certifies operators but does not attest to their
  output -- different functions, different parties.

What this prevents: every existing framework relies on operator
self-reporting. The Artemis Accords require "notification" of safety zones
but no independent verification of what happens inside them. The PNAS
Mining Code requires a governing authority but does not separate the
authority from the attestor.

#### 5. Neutral contract (survive political change)

Resource agreements are bound to the zone's telos, not to the bilateral
relationship between nations. When the US-Japan relationship shifts, the
ice-sharing agreement at Shackleton Crater does not renegotiate from zero.

- Measurement lives in the contract, not in the operator's stack.
- Compliance criteria reference the telos, not the signatory list.
- Operator replacement does not void the contract. The new mayordomo
  inherits the license terms.

What this prevents: the Artemis Accords are bilateral agreements with the
US. If a signatory's relationship with the US deteriorates, their "access
to coordination" is contingent on a political relationship, not on their
resource rights. Neutral contracts make the resource agreement independent
of the bilateral relationship.

#### 6. Provenance (extraction-to-use chain)

Verifiable chain from extraction to processing to use. Not marketing
claims -- receipts.

- Every unit of extracted ice carries provenance from the zone, through
  processing (electrolysis, propellant production), to end use.
- Provenance is the basis for repartimiento accounting: you cannot share
  shortage proportionally if you cannot measure extraction accurately.

### Custody

Who holds the extraction ledger, the rights register, the conflict records?

The acequia answer: custody belongs to the institution that cannot be
acquired. Not a corporation (fiduciary duty to shareholders, acquirable).
Not an operator (conflict of interest). Not a single nation (sovereignty
claims).

For lunar governance, the custodial institution must be:

- **Non-acquirable.** No shareholder structure, no fiduciary duty to
  maximize extraction.
- **Professionally bound to custody.** Betrayal of custodial duty is a
  professional ethics violation, not just a contract breach.
- **Historically credible.** Demonstrated refusal to surrender records
  under pressure.

The library model from the Acequia Protocol applies. The specific
institutional form for space governance is an open question, but the
structural requirements are not.

### Relationship to existing frameworks

The Lunar Headgate Protocol does not replace existing frameworks. It fills
the gaps they leave:

| Gap in existing frameworks | Lunar Headgate mechanism |
|---|---|
| No shortage allocation | Repartimiento |
| Operator self-reporting | Attestation (independent verification) |
| Bilateral → political dependency | Neutral contract (telos-bound) |
| Safety zone → territorial creep | Headgate separates resource governance from operational buffer |
| Identity-based access (signatory status) | Sovereignty Gate (material question only) |
| No operator accountability | Mayordomo model (certified, auditable, replaceable) |
| No community governance | Parciante model (rights-holders set policy) |
| No custody architecture | Non-acquirable custodial institution |
| Extraction volumes unverified | Provenance chain + flume measurement |

### Compatibility

The protocol is designed to layer onto existing frameworks, not replace them:

- **Artemis Accords:** Safety zones remain as operational deconfliction.
  The Lunar Headgate governs the resource within the zone. The two
  functions are separated, not merged.
- **Open Lunar DLAs:** The three-ring framework (core/harmonization/
  coordination) provides spatial structure. The Lunar Headgate provides
  resource governance within that structure.
- **PNAS Mining Code:** The grid-based licensing system provides spatial
  granularity. The Lunar Headgate provides the governing authority the
  Mining Code presumes but does not define.
- **COPUOS principles:** Non-binding principles provide normative
  direction. The Lunar Headgate provides operational mechanisms.
- **Hague Building Blocks:** Priority rights via registry are replaced
  by proportional rights via telos-bound declaration. The registry
  itself (as infrastructure) is compatible.

### What makes this different

Every existing framework assumes one of two things:

1. **Abundance** (there is enough for everyone). The Outer Space Treaty
   and the Artemis Accords both assume the moon is big enough. For
   regolith, maybe. For south pole water ice, no.

2. **Authority** (an intergovernmental body will decide). The PNAS Mining
   Code and the Vancouver Recommendations both presume an authority that
   does not exist and that the most powerful actors have no incentive
   to create.

The Acequia Protocol assumes neither. It assumes:

- **Scarcity.** The resource is finite and will run short.
- **Community governance.** The people with rights govern the resource.
  No external authority is required because governance is intrinsic to
  the commons.
- **Operator accountability.** The operator serves the community, not
  the other way around.
- **Telos over rules.** Compliance is measured against purpose, not
  against a checklist. An operator whose extraction serves the declared
  telos is compliant. One whose extraction monopolizes the resource is
  not, regardless of how many boxes they check.

The acequia has operated for 400 years without a central authority, without
a treaty, and without the cooperation of the dominant legal system. It
works because the governance is in the infrastructure, not above it.

The moon needs a headgate because the alternative is the Colorado River
Compact -- 80 years late, based on bad data, and failing.

---

## Open questions

1. **Rights declaration.** How are proportional rights initially allocated
   among parciantes? The acequia uses irrigated acreage. What is the
   lunar equivalent? Invested capital? Scientific contribution? Population?
   Need? This is the hardest political question and the one most likely
   to block adoption.

2. **Institutional form.** The library model provides structural
   requirements for the custodial institution, but the specific form
   for an international space governance custodian does not exist. Is
   it a new institution, a function of UNOOSA, or a federated network?

3. **Enforcement.** The acequia enforces through community sanction --
   the mayordomo can shut your compuerta. What is the enforcement
   mechanism for a lunar extraction operator that violates their license?
   The Outer Space Treaty assigns state responsibility, but enforcement
   against a non-signatory state is unresolved.

4. **China-Russia participation.** The ILRS program operates outside the
   Artemis framework. The Sovereignty Gate's "material question only"
   principle means Artemis signatory status is irrelevant to resource
   access -- but this requires both frameworks to accept the protocol.
   Designing for inclusion is necessary but not sufficient.

5. **Temporal scope.** The acequia operates on seasonal cycles. Lunar
   ice extraction is continuous. How does the repartimiento cycle work
   -- annual review? Per-mission? Continuous adjustment?

6. **Scale.** The acequia governs a single ditch serving a single
   community. Lunar governance spans multiple sites, multiple nations,
   and multiple operators. Federation (governed inter-jurisdictional
   queries) is specified in HEADGATE-CHAIN.md but has not been tested
   at planetary scale.

---

## Telos declarations (proposed, awaiting human submit)

```yaml
id: lunar-ice-governance
declared_by: PROPOSED (awaiting human submit)
declared_at: 2026-09-13
status: proposed
telos: >
  Lunar water ice is finite shared infrastructure. Its governance serves the
  sustained accessibility of the resource for all participants, not the
  maximum extraction rate for the first arrival.
anti_telos: >
  Permanent monopoly control of a non-renewable, enabling resource by the
  actor with the earliest access and the most capital.
bindings:
  projects:
    - ditch-ai
    - lunar-headgate-protocol
```

```yaml
id: lunar-operator-accountability
declared_by: PROPOSED (awaiting human submit)
declared_at: 2026-09-13
status: proposed
telos: >
  Extraction operators serve the community that authorized them. They are
  certified, audited, and replaceable. They do not own the resource,
  the infrastructure, or the governance.
anti_telos: >
  An extraction operator whose commercial interest in the resource gives
  them de facto control over access policy, shortage allocation, and
  compliance measurement.
bindings:
  projects:
    - ditch-ai
    - lunar-headgate-protocol
```

```yaml
id: lunar-shortage-sharing
declared_by: PROPOSED (awaiting human submit)
declared_at: 2026-09-13
status: proposed
telos: >
  When the resource runs short, shortage is shared by proportion of
  declared rights. No participant is immune by virtue of arrival order,
  capital, or political leverage.
anti_telos: >
  A shortage regime where the most powerful actor maintains full extraction
  while smaller participants are cut off entirely.
bindings:
  projects:
    - ditch-ai
    - lunar-headgate-protocol
```
