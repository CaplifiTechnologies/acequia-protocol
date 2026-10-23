# Headgate Operator Handbook Series — Specification

**Purpose:** Define what human operators need to know and do at each of the 12 headgates in the snowflake-to-inference chain. No AI in the governance loop. Every judgment call is a human call.

**Design standard:** Expressible in stone. If a procedure can't be carved in granite and understood by someone who has never seen a computer, the procedure is too complicated. Simplify until it can.

---

## The Operator Pattern (same at every gate)

Every headgate operator does five things, in cycle:

### 1. WATCH
Read the signals. The sentinel reports; you interpret.

- What are my gauges? (specific to each link)
- What does normal look like? (baseline, documented)
- What does abnormal look like? (threshold, documented)
- How often do I check? (cadence, documented)

**Cognitive demand:** Literacy. Can you read a gauge and compare it to a number.

### 2. DECIDE
Apply the compiled policy to what you see.

- The policy is a rule, not a suggestion. It was voted on by the council and compiled into a deterministic form. Your job is to apply it, not to reinterpret it.
- If the signal is within policy: the gate stays as it is.
- If the signal crosses a threshold: you act (see step 3).
- If the signal is ambiguous: you escalate (see step 4).
- You never guess. Ambiguity is not your problem to solve alone.

**Cognitive demand:** Judgment. Can you tell the difference between a clear signal and an ambiguous one.

### 3. ACT
Open or close the gate. Or don't.

- Opening requires justification. The default is closed for resource
  allocation gates. (Exception: where Sovereignty Gate analysis shows
  closure harms the least-leverage party -- see Headgate 12, where
  default is service because refusal harms the user, not the community.
  The principle is the same: default protects least leverage. The
  direction differs because the vulnerable party differs.)
- Closing requires no justification at resource allocation gates.
  Closed is the resting state.
- Every action is logged before it takes effect. You write it down, then you turn the handle. Not the other way.
- Irreversible actions require a second operator's witness. If you can't undo it alone, you can't do it alone.

**Cognitive demand:** Discipline. Can you write before you act, every time, even when it's urgent.

### 4. ESCALATE
When you don't know, say so.

- Ambiguous signal → escalate to the adjacent gate operator.
- Novel signal (never seen before) → escalate to the council.
- Conflicting policy (two rules point different directions) → escalate to the council. Do NOT pick one.
- Emergency (the flow is causing harm right now) → close the gate first, escalate second. Default-closed is the emergency procedure.

**Cognitive demand:** Honesty. Can you say "I don't know" instead of making something up.

### 5. REVIEW (La Limpia)
Walk the whole channel. Periodically.

- Every operator walks their link with the adjacent operators present.
- The walk is physical (or its digital equivalent: a line-by-line audit of every signal, policy, and log entry since the last review).
- Findings are published. Not summarized, not filtered. Published.
- The review is the moment the community verifies that the governance is actually working. It is not optional and it is not delegable.

**Cognitive demand:** Thoroughness. Can you check every fitting on a ditch you've walked a hundred times and still find the one that's leaking.

---

## The Twelve Handbooks

Each handbook covers one link. Each follows the same five-section structure (Watch, Decide, Act, Escalate, Review) with link-specific content.

### Link 1: Snowpack / Headwater
**Operator:** Watershed steward (existing role)
**Gauges:** Snowpack telemetry (SNOTEL), precipitation, temperature
**Policy:** Prior appropriation, interstate compact obligations
**Already governed:** 150+ years of Colorado water law. Handbook exists as custom.

### Link 2: River / Conveyance
**Operator:** Ditch rider / mayordomo (existing role)
**Gauges:** Stream gauges (USGS), diversion records (CDSS), call status
**Policy:** Decree, priority date, beneficial use
**Already governed:** 400+ years of acequia custom. Handbook is the tradition itself.

### Link 3: Storage / Reservoir
**Operator:** Dam operator (existing role, regulated)
**Gauges:** Reservoir level, inflow/outflow, evaporation
**Policy:** Storage right, compact accounting, flood rule curves
**Already governed:** Bureau of Reclamation, state engineer.

### Link 4: Allocation / Distribution
**Operator:** Water commissioner (existing role, state-appointed)
**Gauges:** Diversion headgate readings, curtailment orders
**Policy:** Priority administration, augmentation plans
**Already governed:** State engineer's office. The most mature headgate in the chain.

### Link 5: Bulk Transport (NEW)
**Operator:** Pipeline/canal steward
**Gauges:** Flow meters, pressure, water quality at intake/discharge
**Policy:** Proportional curtailment during shortage. No user class exempt.
**Key decision:** When shortage triggers curtailment, who gets reduced first? The policy answers this. The operator executes it.
**Handbook note:** This is the first link where the operator may face pressure from large industrial users. The policy is the shield. "I don't make the allocation. The policy does. I turn the handle."

### Link 6: Municipal Delivery (NEW)
**Operator:** Municipal water utility operator
**Gauges:** System demand, per-user consumption, industrial vs residential split
**Policy:** Transparency mandate -- if any single user takes >X% of municipal supply, the community knows. Published, not summarized.
**Key decision:** When to publish an industrial consumption report that a large user would prefer to keep quiet.
**Handbook note:** The transparency headgate. The operator's job is to make the invisible visible. The hardest skill here is not technical -- it's the willingness to publish data that powerful users don't want published.

### Link 7: Industrial Consumption (NEW)
**Operator:** Industrial compliance officer (facility-level)
**Gauges:** Intake volume, recycling rate, discharge quality, efficiency benchmarks
**Policy:** Burden of demonstrating efficiency falls on the consumer, not the regulator. You prove you're using it well; nobody has to prove you're wasting it.
**Key decision:** Whether a facility's efficiency claim is substantiated by the data.
**Handbook note:** The operator is inside the facility, not outside it. This is the self-governance headgate. The ledger makes honest reporting easier than dishonest reporting because the chain verifies upstream and downstream.

### Link 8: Fabrication Capacity (NEW)
**Operator:** Fab allocation steward
**Gauges:** Wafer starts, capacity utilization, customer allocation queue, public subsidy accounting
**Policy:** Public subsidy creates public standing. A $40B fab that allocates purely by contract is extracting from the commons. Community allocation share proportional to public investment.
**Key decision:** Whether to allocate contested capacity to a commercial customer or to a public-interest use.
**Handbook note:** This is where the chain crosses from water to silicon. The operator needs to understand both: the water that feeds the fab AND the chips that come out. The gauges are different but the governance pattern is identical to Link 4.

### Link 9: Chip Distribution (NEW)
**Operator:** Source allocation steward (at the foundry, not downstream)
**Gauges:** Chip shipment manifests, destination declarations, export control status
**Policy:** Source governance, not downstream export controls. The headgate belongs where the chips are made, not where they're shipped to.
**Key decision:** Whether a shipment declaration is accurate and policy-conforming.
**Handbook note:** This is Plan A's chip-tracking problem. The operator is the person at the foundry gate who checks the manifest. The skill is the same as a ditch rider checking diversion records: does the declared take match the actual take?

### Link 10: Compute Access (NEW)
**Operator:** Datacenter allocation steward
**Gauges:** Compute utilization by user class, queue depth, pricing tiers, public-interest allocation
**Policy:** Proportional allocation across user classes. Pricing out public-interest users (researchers, civic institutions, small businesses) is non-conforming.
**Key decision:** Whether a pricing or queuing change effectively excludes a user class the policy protects.
**Handbook note:** This is the headgate most likely to face gaming. The operator needs to understand that a technically-compliant pricing structure can be functionally exclusionary. The test is outcome, not structure: are the protected user classes actually getting access?

### Link 11: Training (NEW)
**Operator:** Training run steward
**Gauges:** Workload declarations, compute consumption, dataset provenance, capability benchmarks (pre and post)
**Policy:** Provenance follows the model. Every training run declares its data sources, compute budget, and intended capability. Safety case burden of proof on the trainer.
**Key decision:** Whether a safety case is substantiated before a training run proceeds.
**Handbook note:** This is Plan A's workload approval pipeline. The operator reads the safety case, checks it against the policy, and opens or closes the gate. The hardest part: saying no to a well-funded team with a plausible-sounding safety case that doesn't actually meet the bar. "Plausible" is not the standard. "Substantiated" is.

### Link 12: Inference (NEW)
**Operator:** Service steward
**Gauges:** Model deployment status, user-facing capability, terms of service, platform self-governance claims
**Policy:** Default is service. A platform that governs itself is not governed. Community has standing in how deployed models interact with the public.
**Key decision:** Whether a deployed model's actual behavior matches its declared capability and safety posture.
**Handbook note:** The last headgate. The operator is watching what the AI actually does in the world, not what its makers say it does. The gauge is behavior, not documentation. This is the hardest link to operate because the signals are the most ambiguous and the pressure to "let it flow" is the strongest.

---

## Governance Model (Acequia Protocol)

Operators do not self-authorize. Authority flows from election, through compiled policy, into the handle.

### Four roles at every link (from the Acequia Protocol)

**Council (La Junta)** — elected by the parciantes (the community of users who depend on the flow at this link). Sets policy. The policy is the WHAT. The council never touches the handle.

**Steward (Mayordomo)** — elected by the parciantes. Executes policy at the gate. The steward is the operator described in the five-step cycle above (Watch, Decide, Act, Escalate, Review). The steward touches the handle. The steward does NOT set policy.

**Compiler** — deterministic code. Translates council policy into enforceable rules. Same input, same output, no inference, no discretion. The compiler is the gate mechanism itself. It does not decide; it executes what the council decided.

**Monitor (Watcher)** — the parciantes themselves, plus any designated observers. The monitor is NOT the operator, NOT the compiler, NOT the council. The monitor is a separate role whose entire job is process-based observation of the system for gaming, circumvention, or slanted use. See "Two principles of observation" below.

**Prior art note:** Aten Security ships a Go SDK called "Thoth"
(github.com/atensecurity/thoth-go) that wraps AI agent tool calls with
policy enforcement, pre-execution checks, and post-execution event
monitoring. Evaluate as a reference for deterministic tooling at the
Compiler layer (policy enforcement, pre-execution checks). Thoth is
NOT a candidate for the Monitor layer: the Monitor is a human
observation role, and placing AI in the governance loop -- even as
substrate -- violates the no-AI-in-governance rule below. Deterministic,
non-discretionary tooling (log aggregation, threshold alerts, format
validation) is permitted as operator infrastructure; AI that interprets,
judges, or decides is not.

### Why the Monitor is a separate role

The Compiler is gameable. "Enforceable rules" is gameable. A sufficiently motivated agent (or corporation, or nation-state) will direct its full resources at circumventing enforceable rules. This is not speculation -- it is the history of every regulatory system ever built. You don't break the law. You shape what the law sees.

The defense is NOT more complex rules. More complexity = more attack surface = more workaround options. The defense is:

1. **The rules stay simple.** Default closed. Opening requires justification. Every action logged before execution. Three rules. Hard to game three rules.
2. **The watching stays complex.** Many eyes, not one inspector. The open ditch. Every parciante can see the flow. Gaming one inspector is a focused problem. Gaming every user who can see the channel is a distributed problem that doesn't scale for the attacker.
3. **The watcher looks at outcomes, not inputs.** The Compiler checks: "Did you file the correct paperwork?" The watcher asks: "Your paperwork is perfect, but your downstream neighbor is dry." A rogue agent can game inputs. It cannot game the fact that someone downstream isn't getting water.
4. **The watcher is a different computational class than what it watches.** Humans watching AI. Deterministic code watching inferential systems. Never AI watching AI at the governance layer -- that's circular and prompt-injectable.

### The Compiler/Monitor tension

This is the design problem the handbooks must solve at every link:

- **Too simple (Compiler only, no Monitor):** Easy to game. The rules are predictable, the inputs are shapeable, and nobody is watching outcomes.
- **Too complex (elaborate rules, single inspector):** More attack surface. One inspector can be captured, bribed, overwhelmed, or simply wrong.
- **Right balance (simple rules + distributed watching):** The rules are hard to game because there's nothing to game. The watching catches what slips through because many independent eyes are observing outcomes, not inputs.

### Two principles of observation

**Process-based observation.** Don't audit snapshots. Watch the process.

A snapshot audit asks: "Is this compliant?" A process audit asks: "How did this become compliant?" Gaming works by manufacturing inputs that produce compliant outputs. If the observer watches the manufacturing -- the process of constructing the input, the sequence of decisions that led to this state, the flow over time rather than the level at a moment -- the gaming itself becomes the anomaly. You don't need to prove the output is wrong. You can see the input being shaped.

At the gate: the monitor doesn't check the ledger entry. The monitor watches how the ledger entry was produced. The difference between "this entry is correct" and "this entry was constructed to appear correct" is visible only in the process.

**Non-local observer.** The watcher at your gate should not be from your gate.

A local observer normalizes. They acclimate. They accept "that's just how we do it here" because they've been here long enough to stop seeing it. A non-local observer -- a parciante from a different link, a mayordomo from a neighboring ditch -- notices what the locals stopped seeing. They have no stake in local accommodations and no relationship with the people they're observing.

At the gate: Link 9 (Chip Distribution) is watched by parciantes from Link 6 (Municipal Delivery) and Link 12 (Inference). They don't work at the foundry. They don't know the foundry's culture. They don't accept the foundry's explanations. They know what the flow looks like from where they stand, and they can see when it doesn't match what the foundry says is happening.

Cross-link La Limpia is the mechanism: when the whole chain walks together, every observer is non-local at eleven of twelve links. That's not a bug in the review process. That's the security model.

### The Monitor's duties

- **Watch the process, not the snapshot.** How did this state come to be? Not: is this state compliant?
- **Observe from outside.** Monitors rotate across links. A monitor who has watched the same gate for too long is a local observer and has lost the non-local advantage.
- **Publish anomalies.** Not summarize. Not filter. Publish. The community decides what's anomalous, not the monitor alone.
- **Flag gaming patterns.** When technically-compliant behavior produces non-compliant outcomes, that's gaming. When the process of producing compliant inputs is itself anomalous, that's gaming. Name it.
- **The Sanhedrin Rule (from HP-001).** Full agreement among all monitors is itself a fault condition. It means the observation space is too narrow or the monitors are captured. Disagreement among monitors is healthy. Unanimity is suspicious.

### Who are the parciantes at each link?

Links 1-4: Already defined. Water users with decreed rights. 400 years of precedent.

Links 5-7: The users of the transported/delivered/consumed resource. Municipal customers. Industrial neighbors. Communities whose water or power is affected by the facility's consumption.

Links 8-12 (the hard question): Who has standing in a chip fab? In a datacenter? In a training run?

The acequia answer: **anyone downstream of the flow has standing as a parciante.** A chip fab's parciantes are not just its shareholders -- they are everyone who depends on the chips it produces, and everyone whose resources (water, power, land) it consumes. A datacenter's parciantes include the researchers, civic institutions, and small businesses whose access is affected by allocation decisions. A training run's parciantes include everyone who will interact with the resulting model.

This is the radical claim: **public subsidy creates public standing, and downstream dependency creates downstream standing.** A $40B publicly subsidized fab that allocates purely by private contract is extracting from the commons. The parciantes have standing not because they own shares but because they depend on the output and funded the input.

This is an open question, not a settled answer. The handbooks must define parciante standing at each link before the governance model can function. The election of council and steward depends on knowing who votes.

---

## Operator Qualification

Same pattern at every link:

1. **Walk the channel.** Before you operate a gate, you walk the entire chain -- upstream and downstream of your link. You understand where the flow comes from and where it goes.
2. **Apprentice.** Operate alongside a qualified operator for one full La Limpia cycle before operating alone.
3. **Pass the granite test.** Explain your gate's Watch-Decide-Act-Escalate-Review cycle in words simple enough to carve in stone. If you need jargon, you don't understand it yet.
4. **Recertify at La Limpia.** Every review cycle, every operator demonstrates competence. Not a test -- a walk. Show the community your link works.

---

## Coordination Model

No operator works alone. The chain only works if adjacent operators talk to each other.

- **Upstream handoff:** When your upstream operator changes the flow (opens, closes, curtails), they notify you before the change reaches your gate. You never discover a flow change by seeing it arrive.
- **Downstream accountability:** Your downstream operator can see your ledger. You can see theirs. The chain is transparent in both directions.
- **Cross-link La Limpia:** Periodically, the ENTIRE chain walks together. Not just adjacent links -- all twelve. This is the moment where the snowflake-to-inference chain is verified as a chain, not twelve separate gates.
- **Conflict resolution:** When two operators disagree, the council decides. Not the senior operator, not the one with more experience, not the one at the upstream link. The council. Seniority does not override governance.

---

## The Granite Test

Every procedure in every handbook must pass this:

> Can this instruction be carved in stone, mounted at the gate, and understood by an operator who has never seen the technology that flows through the channel?

If yes: it belongs in the handbook.
If no: simplify until it can, or admit it's a temporary procedure that will be replaced when you find the permanent one.

The acequia customs survived because they're simple enough to teach by walking the ditch. The headgate chain handbooks survive the same way: by being simple enough to carve.

---

*Draft. Not ratified. The handbooks themselves are the next build.*
*See: HEADGATE-CHAIN.md (architecture), SNOWFLAKE-TO-INFERENCE.md (supply chain), acequia-protocol.md (governance model)*
