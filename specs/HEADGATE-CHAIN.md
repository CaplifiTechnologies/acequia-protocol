# Headgate Chain
## Acequia Protocol — Snowflake-to-Inference Governance Spec v0.1

> **Same gate, every link.** The acequia has one governance pattern:
> measure the resource, not the person. Allocate by proportion, not by
> leverage. Record everything. Default protects whoever can least afford
> the gate going wrong. That pattern applies at every headgate from
> snowmelt to inference. The spec is the same. The resource changes.

---

### Origin

A conversation traced the physical supply chain from a snowflake in the
Colorado Rockies to an AI model running inference on a chip washed by
that snowflake's water. Twelve links. The first four have acequia
governance -- 400 years of it. The last eight have contracts, markets,
and terms of service.

This spec builds the eight missing headgates.

The chain is not a metaphor. The water that washes the wafer fell as
snow in Colorado. The governance at link 1 and the governance at link 12
sit on the same physical supply chain. Extending the Acequia Protocol
from water to silicon to inference is not analogy. It is plumbing.

---

### The chain

| # | Link | Resource | Governed? |
|---|------|----------|-----------|
| 1 | Snowflake | Precipitation | Climate (no human gate) |
| 2 | Snowpack | Seasonal storage | Geography (no human gate) |
| 3 | River | Surface flow | Compact governance (governed) |
| 4 | Acequia headgate | Allocated water | Acequia governance (governed) |
| 5 | Distribution | Bulk transport | **SPEC BELOW** |
| 6 | Municipal delivery | Treated water to end users | **SPEC BELOW** |
| 7 | Industrial consumption | Water transformed by process | **SPEC BELOW** |
| 8 | Fabrication | Production capacity | **SPEC BELOW** |
| 9 | Chip distribution | Finished processors | **SPEC BELOW** |
| 10 | Compute access | GPU/compute capacity | **SPEC BELOW** |
| 11 | Training | Model development | **SPEC BELOW** |
| 12 | Inference | Model predictions | **SPEC BELOW** |

---

### Five primitives at every headgate

Every headgate in the chain implements the same five primitives. These
are inherited from the acequia and constrained by SOVEREIGNTY-GATE.md.

**1. Resource.** What flows through this gate. Named, measured, finite.

**2. Parciante standing.** Who has a seat at the junta for this gate.
Standing comes from dependency -- if the resource's allocation affects
you, you are a parciante. Not from purchase volume, market position, or
institutional credential.

**3. Material check.** What the gate measures. Per Sovereignty Gate:
material properties, authorization scope, or measurement. Never identity,
worthiness, or standing beyond what is necessary to verify authorization.

**4. Measurement.** How flow is recorded. Append-only. Public or
auditable by parciantes. The record of what flowed, to whom, under what
authorization. Governance without measurement is aspiration.

**5. Default.** What happens when the gate fails, when information is
missing, or when the system is down. Default protects whoever has least
leverage in that transaction.

---

## Headgate 5: Distribution

### Resource

Bulk water transport from reservoir or river to metropolitan service
area. The Central Arizona Project canal. The All-American Canal. The
Colorado-Big Thompson system. Trunk infrastructure that moves water from
the governed acequia system into metropolitan and industrial supply.

### Parciantes

Every entity that receives water from the distribution system:
municipalities, tribal nations, agricultural districts, industrial
users. Standing is proportional to dependency, not to purchase volume.
A tribal nation whose sole water source is the canal has more at stake
than an industrial user with alternative supply, and that asymmetry is
reflected in governance weight.

### Material check

The gate measures: allocation proportion relative to rights and compact
obligations. Drought tier and curtailment schedule. Delivery volume
and timing.

The gate does not measure: ability to pay premium rates during shortage.
Political alignment between the recipient and the operating authority.
End-use type as a basis for priority (agriculture vs. municipal vs.
industrial) unless the community has explicitly authorized a priority
schedule through the Community Decision Protocol.

### Measurement

Volume delivered to each recipient, recorded continuously. Compact
delivery compliance at state-line gauges. Curtailment events: who was
curtailed, by how much, under what drought tier. All records auditable
by any parciante.

### Default

During shortage, curtailment falls by the schedule the community
authorized. If no schedule exists, curtailment is proportional -- every
parciante takes the same percentage reduction. Default never protects
the largest user at the expense of the smallest.

### Non-conforming

A distribution authority that sells shortage exemptions. A curtailment
schedule that protects industrial users while residential users face
restrictions, without explicit community authorization. A system where
the ability to pay a premium during drought determines who gets water.
A canal authority that makes allocation decisions without parciante
representation.

---

## Headgate 6: Municipal Delivery

### Resource

Treated water delivered from a municipal system to end users within the
service area. Residential, commercial, industrial. The pipe that
connects the distribution trunk to the meter on the wall.

### Parciantes

All ratepayers and users within the municipal service area. Every
connection is a parciante. An industrial user consuming millions of
gallons is a parciante. A household with a quarter-inch line is a
parciante. Standing is by dependency, not by volume.

### Material check

The gate measures: consumption volume by user class. Allocation to each
class as a proportion of total supply. Industrial allocation during
shortage. Rate structure and any preferential pricing.

The gate does not measure: the identity of the industrial user beyond
what is necessary for billing and allocation. The economic value of the
end use. The political relationship between the city and the industrial
user.

### Measurement

Total consumption by user class (residential, commercial, industrial),
published regularly. Individual industrial allocations above a
threshold (configurable by the community), published individually. Any
preferential rate or priority agreement with an industrial user,
published in full. Drought curtailment by class.

This is the transparency headgate. The community cannot govern what it
cannot see. If a chip fab consumes 10% of the city's water supply, the
community knows that. If the fab has a drought exemption, the community
knows that.

### Default

During shortage, industrial users face the same curtailment percentage
as residential users unless the community has explicitly authorized a
different schedule. A bilateral agreement between the city and an
industrial user that exempts the user from curtailment is non-conforming
unless the community authorized it.

### Non-conforming

An industrial water agreement negotiated without public disclosure. A
drought exemption for an industrial user that the community did not
authorize. A rate structure where the largest users pay less per gallon
than the smallest, without community authorization. Any arrangement
where the industrial user's allocation is invisible to the ratepayers
who share the supply.

---

## Headgate 7: Industrial Consumption

### Resource

Water consumed and transformed by an industrial process. In the chip
fabrication context: municipal water taken in, purified to
semiconductor-grade ultrapure water, used to wash wafers, and either
recycled within the process, discharged to the sewer system, or
evaporated. The resource enters the fab as water and leaves as product,
wastewater, and vapor.

### Parciantes

The community whose water supply and environment are affected by the
industrial consumption. The ratepayers who share the supply. The
downstream users of the watershed that receives discharge. The
residents near the facility who breathe the evaporate.

### Material check

The gate measures: total water intake. Recycling rate (what percentage
of intake is reused within the process before discharge). Discharge
volume, destination, and quality. Evaporative loss. Net consumption
(intake minus return flow).

The gate does not measure: the economic value of the product made from
the water. The proprietary details of the manufacturing process. Trade
secrets. The gate measures what goes in and what comes back -- the
resource balance, not the business.

### Measurement

Published regularly: intake volume, recycling rate, discharge volume
and quality, evaporative loss, net consumption. These are the numbers
the community needs to understand the resource cost of the industrial
process. A fab that reports 80% recycling and 20% net consumption gives
the community a different picture than one that reports 30% recycling
and 70% net consumption. Both are on the record.

### Default

A facility that does not report consumption and recycling data is
treated as consuming 100% of intake for allocation purposes. The gate
does not assume efficiency. The burden of demonstrating recycling falls
on the consumer, not the community.

### Non-conforming

Consumption data reported only to regulators, not to the community.
Recycling rates claimed without independent measurement. Discharge
quality self-reported without third-party verification. Any arrangement
where the community that shares the water supply cannot see how much of
it the industrial process consumes.

---

## Headgate 8: Fabrication Capacity

### Resource

Production slots on advanced semiconductor process nodes. The scarce
capacity to turn chip designs into physical silicon. Time on the
machines, measured in wafer starts per month at a given node (3nm, 2nm,
etc.).

This headgate marks the transition from water governance to silicon
governance. The resource upstream is liquid. The resource here is
manufacturing capacity. The governance pattern is the same.

### Parciantes

All entities that depend on chips fabricated at the facility. The
companies that design chips. The governments that subsidized the
facility. The public that funded the subsidy. The downstream users who
depend on the products the chips enable.

When a fab was built with public subsidy (CHIPS Act, state incentives,
tax abatements), the public is a parciante. Public funding creates
public standing. A fab that took $40 billion in public money and
allocates capacity purely by commercial contract is extracting from the
commons without returning governance to it.

### Material check

The gate measures: allocation proportion by customer. Allocation
proportion reserved for public-interest production (defense, public
health, research, critical infrastructure). Parciante obligations met
(workforce investment, R&D commitments, supply chain contributions).
Utilization rate.

The gate does not measure: the commercial terms of individual contracts
beyond allocation proportion. The proprietary details of chip designs.
The identity of the end user beyond what is necessary to verify
public-interest reservation compliance.

### Measurement

Published regularly: total capacity by node. Allocation by customer
class (commercial, public-interest, reserved). Utilization rate.
Waitlist depth and average wait time. Public-interest reservation
compliance (did the reserved capacity actually serve public interest,
or was it reallocated to commercial).

Individual customer allocations: reported in proportion (Customer A
holds X% of 3nm capacity), not in absolute design detail.

### Default

When demand exceeds capacity, allocation follows the schedule the
parciante community authorized. If no schedule exists, curtailment
is proportional -- no customer is immune. Public-interest reservations
are curtailed last, because the community that funded the capacity
authorized them as a condition of the subsidy.

### Non-conforming

A publicly subsidized fab that allocates capacity purely by commercial
contract with no public-interest reservation. A facility that took
public money and treats the public as a non-party to allocation
decisions. Allocation that changes based on the customer's willingness
to pay a premium during shortage rather than by the community-authorized
schedule. Any arrangement where the entity that received the subsidy
governs allocation without input from the entity that paid for it.

---

## Headgate 9: Chip Distribution

### Resource

Finished processors distributed from fabrication to buyers. Packaged,
tested chips leaving the fab and entering the market. GPUs, AI
accelerators, mobile processors, automotive chips -- the physical
substrate of computation.

### Parciantes

All downstream users and communities whose infrastructure depends on
chips. National governments (defense, critical infrastructure).
Industrial users (automotive, medical devices, telecommunications).
Compute providers (cloud, HPC). Research institutions. The public,
through its dependency on chip-enabled services.

### Material check

The gate measures: end-use category (commercial, defense, critical
infrastructure, research). Proportional allocation across categories.
Compliance with community-authorized distribution schedule.

Destination jurisdiction is recorded in the measurement layer for
provenance and chain integrity, not used as a gating criterion. A
chip destined for a disfavored jurisdiction flows with its provenance
record intact; the record may carry an UNATTESTED flag if the
downstream headgate is ungoverned, but the gate at the source does
not block on jurisdiction. Blocking on jurisdiction is a political
boundary check, not a material check, and would violate Sovereignty
Gate Rule 1.

The gate does not measure: the political alignment of the buyer. The
ideological compatibility of the end use. The destination jurisdiction
as a gating criterion. The gate checks what the chip will do, not
who the buyer is -- per Sovereignty Gate, the material question only.

### Measurement

Distribution volume by end-use category and destination region.
Published at a cadence that does not compromise competitive information
but gives the parciante community visibility into where the resource
flows. Aggregated quarterly, auditable annually.

### Default

When supply is constrained, distribution follows the community-
authorized priority schedule. If no schedule exists, critical
infrastructure and public health take precedence -- not because those
categories are inherently superior, but because the people who depend
on them have the least leverage to find alternatives.

### Non-conforming

Distribution governance imposed entirely from downstream -- a
government telling the headwater community who they may and may not
serve, without the headwater community's participation in that
decision. Export controls decided in Washington for chips fabricated in
Taiwan are downstream regulation, not source governance. The headgate
belongs at the source.

Also non-conforming: distribution controlled entirely by the fab
operator's commercial interest with no community governance at all.

The conforming arrangement: distribution governance is negotiated
between the source community and downstream parciantes, with the
source community holding the gate and downstream parciantes holding
standing.

---

## Headgate 10: Compute Access

### Resource

GPU and compute capacity in data centers. The ability to run workloads
on the chips that were fabricated upstream. Measured in GPU-hours,
compute units, or equivalent. The resource that AI training and
inference consume.

### Parciantes

All compute users, across every scale:

- **Enterprise** -- large companies with dedicated capacity.
- **Startups** -- early-stage companies building on compute.
- **Research** -- academic and public-interest research institutions.
- **Public sector** -- government agencies, public health, education.
- **Individual** -- independent developers, students, hobbyists.

Standing is by dependency. An independent researcher whose entire
project depends on GPU access has more at stake than an enterprise
user with redundant capacity across three providers.

### Material check

The gate measures: allocation proportion across parciante classes.
Pricing by class (does the smallest user pay more per unit than the
largest?). Waitlist depth and time by class. Public-access minimum
(what proportion of total capacity is available to non-enterprise
users at non-premium pricing?).

The gate does not measure: the content or purpose of the workload
beyond what is necessary for capacity planning and priority scheduling.
The gate allocates compute, not permission.

### Measurement

Published regularly: total available capacity. Allocation by parciante
class. Pricing by class. Waitlist metrics by class. Public-access
utilization. Outage and curtailment events by class.

### Default

When capacity is constrained, curtailment is proportional across
classes unless the community has authorized a priority schedule.
Enterprise users do not get immunity from curtailment because they
pay more. Public-access capacity is curtailed last, because the users
in that class have the least leverage to find alternatives.

### Non-conforming

A compute provider that prices public-interest users out of access. A
waitlist system where enterprise users bypass the queue. A capacity
allocation model where 95% of compute goes to five customers and
everyone else competes for the remainder with no governance. Any
arrangement where the parciante class with least leverage bears
disproportionate curtailment.

---

## Headgate 11: Training

### Resource

Model development -- the process of training a foundation model on
data, using compute, to produce a set of weights that encode learned
patterns. The resource consumed is compute (Headgate 10), data
(existing Acequia Protocol), and the resulting model's capabilities
and limitations.

This headgate is where the existing Acequia Protocol for community data
(WHAT-IT-IS.md) intersects the supply chain. Training data governance
IS Acequia Protocol governance. The headgate here connects the chain
to the protocol's origin.

### Parciantes

- **Data communities** -- communities whose data contributed to
  training, whether through direct collection, public datasets, or
  web scraping. The parciante standing of data communities is
  established by the existing Acequia Protocol: community-generated
  data is civic infrastructure, appurtenant to the community.
- **Compute providers** -- the entities whose capacity is consumed
  by training (their governance is Headgate 10).
- **Downstream users** -- everyone who will use the trained model.
  Training decisions constrain what the model can and cannot do;
  downstream users have standing because they bear the consequences.
- **Affected communities** -- communities that will be
  disproportionately affected by the model's capabilities or
  failures, whether or not they contributed data.

### Material check

The gate measures: data authorization (did the source community
consent to this use, per Acequia Protocol?). Training data composition
(what proportion from consented sources vs. unconsented). Compute
consumed. Stated training objectives. Evaluation results against
published benchmarks.

The gate does not measure: the commercial strategy of the training
entity. The proprietary architecture of the model. Trade secrets of
the training process. The gate measures inputs (data, compute) and
outputs (capabilities, evaluations) -- not the mechanism.

### Measurement

Published before training begins: data sources and consent status.
Compute budget. Stated objectives. Planned evaluations.

Published after training completes: evaluation results. Data
composition summary. Compute consumed. Known limitations and failure
modes.

This is the most measurement-heavy headgate in the chain, because
the resource being produced (a trained model) has effects on every
headgate downstream.

### Default

A model trained on data without community authorization is treated as
having unresolved provenance. The model functions, but every downstream
headgate (compute access, inference) records the provenance gap. The
gate does not block training -- it records consent status, and the
record follows the model through the chain.

### Non-conforming

Training on community data without community authorization and without
recording the provenance gap. Opaque training data composition (the
community cannot determine whether its data was used). Evaluation
results published only to regulators, not to the public. Any
arrangement where the entity doing the training is the sole authority
on whether the training was authorized.

---

## Headgate 12: Inference

### Resource

Model predictions served to end users. The final link. A user asks a
question; the model answers. The answer was computed on a chip that was
washed with water that fell as snow in Colorado. Every headgate in the
chain constrained what this answer could be.

### Parciantes

- **Users** -- people who interact with the model.
- **Affected communities** -- communities affected by the model's
  outputs, whether or not they are users.
- **Data communities** -- communities whose data trained the model
  (standing carried forward from Headgate 11).
- **The public** -- because inference at scale shapes information
  access, economic opportunity, and social infrastructure.

### Material check

The gate measures: access fairness (is the service available on
equitable terms?). Content policy transparency (are the rules
published and comprehensible?). Rate and pricing structure across
user classes. Provenance (does the model carry a clean record from
Headgate 11, or are there unresolved data authorization gaps?).

The gate does not measure: the content of individual queries or
responses. The gate governs the system, not the conversation. Mass
surveillance of inference is non-conforming, even in the name of
safety. Per Sovereignty Gate: the gate checks material scope, not
content.

### Measurement

Published regularly: availability by user class. Pricing by user
class. Content policy changes (versioned, with changelogs). Aggregate
usage statistics. Model provenance summary (consent status of training
data, carried from Headgate 11).

Not published: individual user queries or responses. The measurement
is of the system, not of the users.

### Default

The model serves. Default is open -- because the user asking the
question is the party with least leverage if the gate fails. A model
that defaults to refusal protects the operator, not the user.

Content policy exists, but it is a published constraint, not a default
state. The default state is service. Restrictions are enumerated
exceptions, not the starting position.

### Non-conforming

Governance by the same entity that profits from the service, with no
external accountability. Terms of service that change unilaterally
without versioned changelogs. Content policy enforced inconsistently
across user classes (premium users get fewer restrictions). Access
pricing that excludes public-interest use. Individual query logging
used for purposes beyond service delivery without user consent.

The deepest non-conformance: an inference service that governs itself.
The mayordomo is accountable to the parciantes. A platform that writes
its own rules, enforces its own rules, and adjudicates disputes about
its own rules is not governed. It is sovereign. And the Acequia
Protocol does not recognize unaccountable sovereignty over a shared
resource.

---

## Chain integrity

The headgates are linked. Each gate's measurement record flows
downstream. A chip's provenance includes the water governance that
enabled its fabrication. A model's provenance includes the data
governance that authorized its training. An inference response carries
the full chain: water rights, fab allocation, compute access, training
consent, content policy.

No headgate operates in isolation. A fab that passes Headgate 8
conformance but uses water from a non-conforming Headgate 6 (opaque
industrial allocation) is operating on a chain with a broken link.
Conformance is end-to-end or it is incomplete.

This does not mean every headgate must be fully conforming before any
headgate is useful. Each gate built is an improvement over the current
state (no gate at all). But the chain is the goal, and partial
conformance is reported honestly, not claimed as full compliance.

---

## Sovereignty Gate conformance (all eight)

Per SOVEREIGNTY-GATE.md, every headgate in the chain satisfies:

1. **Material question only.** Each gate measures the resource: volume,
   proportion, composition, provenance. No gate measures the identity,
   worthiness, or political alignment of the party.

2. **Default protects least leverage.** Water defaults to proportional
   curtailment. Compute defaults to proportional curtailment. Inference
   defaults to service. In every case, the party who can least afford the
   gate going wrong is the one the default protects.

   This means the default is not a universal setting. It varies by
   headgate because the vulnerable party varies. At a community data
   headgate (Headgates 6-7, 11 data provisions), the vulnerable party
   is the individual or community whose data flows through the gate;
   default-closed protects them. At an inference service headgate
   (Headgate 12), the vulnerable party is the user seeking information;
   default-open protects them. The Operator Handbook's "default is
   closed" describes the general resting state for resource allocation
   gates. Headgate 12's "default is service" is the specific application
   of the same Sovereignty Gate principle -- protect least leverage --
   to a gate where closure harms the user, not the community. Both
   follow the same rule. The default they reach is different because
   the vulnerable party is different.

3. **Override to rights-holder.** The parciante can challenge their
   allocation. The data community can withdraw consent. The user can see
   the content policy and leave. Override is always available to the
   party whose rights are at stake, not to the operator.

---

## Community Decision Protocol integration

Each headgate's allocation schedule, priority order, and curtailment
rules are set through the Community Decision Protocol
(COMMUNITY-DECISION.md). The protocol degrades to democracy:

- If the community's preference is obvious (T0), the schedule is
  definitive.
- If ranked choice produces a clear winner (T1), the schedule is
  definitive.
- If the margin is thin (T2), the governing body decides with the
  community lean visible.
- If signal is inconclusive (T3), the governing body decides, re-opens,
  or tables. Every path is on the record.

No headgate's allocation rules are set by the operator unilaterally.
The operator operates the gate. The community configures it.

---

## What this prevents

A supply chain where governance exists at the top (water) and nowhere
else. Where the resource transitions from community-governed commons
to commercially allocated commodity the moment it leaves the ditch. Where
400 years of acequia governance protects the water and then the silicon,
compute, training, and inference built on that water are governed by
contracts and terms of service.

The chain says: if the resource is the same resource flowing through
different forms, the governance should flow with it. Water becomes
ultrapure water becomes clean silicon becomes a chip becomes compute
becomes a model becomes a prediction. At every transition, someone
decides who gets how much. That someone should be accountable to the
community that depends on the resource, from snowflake to inference.

---

*Ditch AI specs. Draft 2026-09-13. Not ratified.*
*Governing principle: Same gate, every link.*
