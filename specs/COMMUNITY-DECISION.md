# Community Decision Protocol
## Acequia Protocol — Mundane Governance Spec v0.1

> **Degrade to democracy.** The protocol tries the lightest governance
> first. When consensus is clear, the community speaks and the answer is
> obvious. When signal is weak, the protocol degrades through heavier
> democratic mechanisms until the decision resolves. Democracy is the
> safety net, not the starting position.

---

### Origin

A parks department wants to decide what color to paint a light post. The
board will make the final call, but the community should participate and
see the outcome transparently. The options should be reasonable (not
user-generated chaos), but the system should not require a gatekeeper to
curate them.

The solution: anyone can propose, upvotes do the pruning, and the
protocol produces a result with a confidence tier that determines what
happens next.

This protocol governs decisions where community input is valuable but
not every decision needs the same weight of process. A light post color
and a park closure are different decisions. The protocol is the same; the
configuration differs.

---

### Governing principle

**Degrade to democracy.**

The best outcome is that the answer is obvious and no formal process is
needed. The next best outcome is that ranked choice produces a clear
winner. When neither happens, the protocol degrades gracefully:

| Tier | Signal | What happens |
| --- | --- | --- |
| **T0 — Acclamation** | One option holds supermajority after pruning | Result is definitive. Action fires if action-type. No Council review needed. |
| **T1 — Clear** | Ranked choice produces a winner by standard elimination | Result is definitive. Council may note but not override without public record. |
| **T2 — Close** | Winner exists but margin is below confidence threshold | Result goes advisory. Council decides, sees community lean, decision is on the record. |
| **T3 — Inconclusive** | No option crosses minimum threshold or tie persists | Full democratic fallback. Council may re-open with narrowed options, decide unilaterally, or table. Every path is on the record. |

The tier is computed by the protocol, not chosen by the Council. The
Council configures the thresholds, but once voting closes the tier is
deterministic.

---

### Core primitives

#### Community

A group of participants bound by geography, interest, or institution.
Each community has a Town Council that manages configuration. A
community is sovereign — it does not answer to a parent community unless
it chooses to federate.

#### Town Council

The elected or appointed governance body of a community. The Council:

- Configures protocol parameters (thresholds, voting method, result types)
- Can override T2/T3 results (override is always on the record)
- Cannot override T0/T1 results without a public escalation process
- Cannot prevent proposals from being submitted
- Cannot remove options that have crossed the pruning threshold

The Council governs the *rules of the game*, not the *outcome of the
game*. Sovereignty Gate applies: the Council checks material scope, not
identity.

#### Proposal origin

Every proposal has an origin that determines how it enters the system:

**Official decision** (`origin: council`) -- created by the Town Council,
a department, or a working group with delegated authority. The Council
sets the title, initial options, and timeline. The community still
submits additional options, votes, and produces the result. The
difference: an official decision carries the Council's imprimatur that
the question was asked and that the result will be considered as part of
the governing process.

**Community petition** (`origin: community`) -- created by any community
member. A petition enters pruning the same way, goes through the same
voting process, and produces the same tiered result. The difference: a
petition is initiated by a resident, not the governing body. The Council
is not obligated to act on the result, but the result is on the record
either way.

Both origins run through the same protocol. The same ranked choice
voting, the same pruning, the same degradation tiers. What differs is
who asked the question and what the result binds. A community petition
that produces T0 is a documented community mandate whether the Council
initiated it or not.

#### Proposal

A decision to be made. Anyone in the community can submit a proposal.

Properties:
- `title` — what is being decided
- `description` — context, constraints, why this matters
- `proposer` — who submitted it
- `origin` — council | community
- `type` — poll | ranked-choice | action
- `status` — draft | pruning | voting | decided | tabled
- `created` — timestamp
- `deadline` — voting closes (set by Council config or proposer within bounds)

A proposal enters `pruning` once submitted. It advances to `voting` when
either: (a) enough options exist and the pruning period expires, or (b)
the Council manually advances it.

#### Option

A choice within a proposal. Anyone in the community can submit an
option to an open proposal.

Properties:
- `label` — short name (e.g., "Forest green")
- `description` — optional detail
- `submitter` — who proposed it
- `upvotes` — community support during pruning phase
- `pruned` — whether this option survived pruning

**Pruning:** During the pruning phase, the community upvotes options.
Options that cross the pruning threshold (configured by the Council)
appear on the ballot. Options below the threshold are visible but
marked as pruned. This is gravity, not gatekeeping — the community's
own attention determines what rises.

Minimum ballot size: if fewer than 2 options survive pruning, the
proposal is tabled automatically. The community did not generate enough
viable options for a meaningful vote.

Maximum ballot size: configurable by the Council. If more options
survive than the max, the top N by upvotes appear on the ballot.

#### Vote

A participant's expression of preference within a proposal.

Voting method is configurable per community:

- **Poll** — simple approval. Each participant votes for one or more
  options. Result is a count.
- **Ranked choice** — participants rank options by preference. Instant
  runoff elimination until a winner emerges or signal degrades.
- **Approval** — participants approve all acceptable options. Winner is
  most-approved.

Each method produces a result and a confidence tier.

#### Result

The outcome of a completed proposal.

Properties:
- `winner` — the option that won (if any)
- `tier` — T0, T1, T2, or T3
- `distribution` — full vote breakdown, always public
- `council_action` — what the Council did (honored, overrode, tabled, re-opened)
- `action_taken` — if action-type, what was triggered
- `timestamp` — when decided

The result is an immutable record. The distribution is always public.
If the Council overrides, the override is recorded alongside the
community signal. Transparency is the mechanism, not enforcement.

---

### Result types

Configurable per community by the Town Council:

**Poll result** — the output is informational. "The community preferred
forest green." No action is triggered. The Council or the relevant
authority uses the result as input to their own process.

**Ranked choice with degradation** — the output includes the tier. T0/T1
results carry weight. T2/T3 results are advisory. The degradation tier
tells everyone how much signal the community actually produced.

**Action** — the output triggers a concrete action. A work order, a
budget line, a policy change. Action-type results require T0 or T1 to
fire automatically. T2/T3 action-type results require Council
confirmation before the action triggers.

---

### Configurable knobs

The Town Council sets these per community. Defaults in brackets.

| Parameter | Description | Default |
| --- | --- | --- |
| `voting_method` | poll, ranked-choice, approval | ranked-choice |
| `result_type` | poll, ranked, action | poll |
| `pruning_threshold` | upvotes needed to reach ballot | 3 |
| `pruning_period` | duration of pruning phase | 7 days |
| `voting_period` | duration of voting phase | 7 days |
| `min_ballot_size` | minimum options to proceed | 2 |
| `max_ballot_size` | maximum options on ballot | 6 |
| `t0_threshold` | supermajority % for acclamation | 75% |
| `t1_confidence` | margin % for clear result | 10% |
| `t2_minimum` | minimum participation for signal | 25% of community |
| `council_override` | whether Council can override T0/T1 | false |
| `override_escalation` | if override enabled, require public escalation | true |
| `action_auto_fire` | action-type auto-triggers on T0/T1 | true |
| `proposal_open` | anyone can propose (vs Council only) | true |
| `option_open` | anyone can submit options (vs Council only) | true |

A community can lock any knob — meaning the Council itself cannot change
it without a community vote using this protocol. Locking is itself a
proposal.

---

### Lifecycle

```
 ┌─────────┐
 │  Draft   │  proposer writes title + description
 └────┬─────┘
      │ submit
 ┌────▼─────┐
 │ Pruning  │  community submits + upvotes options
 └────┬─────┘
      │ threshold met or period expires
      │
      ├── < 2 options survived ──► TABLED
      │
 ┌────▼─────┐
 │ Voting   │  community votes (method per config)
 └────┬─────┘
      │ period expires
      │
 ┌────▼─────┐
 │ Decided  │  result + tier computed
 └────┬─────┘
      │
      ├── T0/T1 + action-type ──► ACTION FIRES
      ├── T0/T1 + poll/ranked  ──► RESULT PUBLISHED
      ├── T2 ──► COINCEL REVIEWS (community lean visible)
      └── T3 ──► COINCEL: re-open | decide | table
```

---

### Sovereignty Gate conformance

Per SOVEREIGNTY-GATE.md:

1. **Material question only.** The vote checks preference, not identity.
   Participation requires community membership, but membership is the
   only identity check. The vote itself is anonymous or pseudonymous per
   community config.
2. **Default protects least leverage.** If the system is down, no result
   is recorded. A failed vote does not produce a default winner.
3. **Override to rights-holder.** The community can lock any knob. The
   Council cannot remove a lock without a community vote. A Council
   override of T0/T1 requires public escalation.

---

### The deliberate non-decision

A proposal can also resolve as a **deliberate non-governance decision**.
The community votes on whether to govern something, and the answer is
"no, leave this ungoverned." That result is recorded the same way:

- The proposal was made
- The community participated
- The outcome was: we choose not to govern this
- The record is public

This is different from something being ungoverned by neglect. The
protocol can express "we looked at this and decided it does not need
governance" as a first-class outcome. The absence of a rule is itself
a community decision, not a gap.

---

### Application: development moratorium and standards

When a community faces a large-scale development proposal -- a data
center, an extraction operation, an industrial campus -- the protocol
handles the full lifecycle, not just a single up-or-down vote.

**Phase 1: The moratorium decision.** A proposal is filed: "Should we
pause [development type] while we write enforceable standards?" The
community votes. If the result is T0 or T1, the moratorium is not just
a council action -- it is a documented community mandate with a
confidence tier on the record.

**Phase 2: Standards proposals.** During the moratorium, each provision
of the eventual ordinance becomes its own community decision. Each one
runs through the full protocol: proposals, pruning, voting, tier.

Example provisions for a data center ordinance:

| Proposal | Options pattern |
| --- | --- |
| Noise limit at nearest residence | 55 dB / 65 dB / no cap |
| Water: require binding will-serve letter | Yes / No / Defer |
| Who pays for grid upgrades | Developer / Ratepayers / Shared |
| Require special exception (public hearing) | Yes, always / Only above 20 MW / No |
| Decommissioning bond | Required / Optional / Not needed |
| Prohibit NDAs binding county officials | Yes / No |
| Require end user named before approval | Yes / No |
| Minimum setback from residences | 200 ft / 500 ft / 1000 ft |

Each resolved proposal carries a tier. Provisions the community was
unified on (T0/T1) have documented community backing. Close calls (T2)
went to the Council with the community lean visible. The record is
permanent.

**Phase 3: The ordinance.** When the drafting body adopts the final
ordinance, every provision has a community decision attached to it.
Weakening a T0 provision requires a public explanation. Strengthening
a T3 provision has documented justification. The ordinance is not a
staff product -- it is a community product with staff drafting.

**What this prevents.** A handful of people with a financial interest
cannot drive a decision the community opposes, because the community's
position is documented and tiered. A developer cannot claim the
community did not participate, because participation is measured and on
the record. A future council cannot quietly weaken a standard, because
the original community vote sits next to any amendment.

The protocol does not decide the outcome. It makes the outcome
transparent and traceable. A community that votes T0 to allow
development with strong standards has the same documentation as one
that votes T0 to block it. The protocol serves the decision, not a
position.

---

### Example: light post color

1. Parks department employee proposes: "What color should we paint the
   light posts on Main Street?"
2. Community members submit options: Forest green, Black, Navy blue,
   Burnt orange, Leave them as-is
3. Pruning phase (3 days): Forest green gets 47 upvotes, Black gets 31,
   Navy gets 22, Burnt orange gets 4 (below threshold), Leave as-is
   gets 18
4. Ballot: Forest green, Black, Navy blue, Leave as-is
5. Ranked choice voting (5 days): Forest green wins in round 2 after
   Navy eliminated, margin 58-42 over Black
6. Result: T1 (Clear). Forest green. Distribution published.
7. Parks board sees the result, honors it. Record shows: community
   chose forest green, board honored.

If the vote had been 51-49, it would have been T2. The board would
still see the lean, but the protocol would not call it definitive.
The board decides, and whatever they pick is on the record next to
what the community said.

---

*Ditch AI specs. Draft 2026-09-11. Not ratified.*
*Governing principle: Degrade to democracy.*
