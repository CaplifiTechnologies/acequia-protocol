# Headgate Inference Spec
## Acequia Protocol — Default-Closed Governor Between Models and Inference Endpoints v0.1

**Version:** headgate.inference/0.1
**Status:** DRAFT
**License:** CC BY 4.0
**Author:** Ditch AI

> **Same gate, every link.** The acequia has one governance pattern:
> measure the resource, not the person. Allocate by proportion, not by
> leverage. Record everything. Default protects whoever can least afford
> the gate going wrong. That pattern applies at every headgate from
> snowmelt to inference. This spec defines Headgate 12 — the final link
> in the snowflake-to-inference chain — as a default-closed governor with
> per-embedding gating, human seal for open states, and hash-chained
> receipts.

---

## Abstract

This spec defines the governance layer between trained models and inference
endpoints. It is Headgate 12 in the snowflake-to-inference chain described
in HEADGATE-CHAIN.md. The resource at this link is model predictions served
to end users. The governor sits between the model (which produces outputs)
and the inference endpoint (which serves them), enforcing default-closed
gating with per-embedding authorization, human seal for open states, and a
hash-chained receipt ledger.

The governance pattern at this link is inherited from the acequia: every
headgate in the chain implements the same five primitives — Resource,
Standing, Material Check, Measurement, Default — constrained by
SOVEREIGNTY-GATE.md. The resource changes (from water to silicon to
inference), but the governance pattern does not.

The default state is **closed**. A model may not serve an inference without
authorization. This protects the user: a model that defaults to refusal
protects the operator, not the person asking the question. Override is
always available to the rights-holder (the user whose query is at stake).

Per the Operator Handbook pattern, every headgate operator does five things
in cycle: WATCH, DECIDE, ACT, ESCALATE, REVIEW (La Limpia). At inference,
the operator is the service steward; the compiler is the deterministic gate;
the council is the parciantes who depend on the model's outputs.

---

## 1. Five Primitives

Every headgate in the chain implements the same five primitives. These are
inherited from the acequia and constrained by SOVEREIGNTY-GATE.md.

### 1.1 Resource

**Model predictions served to end users.** The final link. A user asks a
question; the model answers. The answer was computed on a chip that was
washed with water that fell as snow in Colorado. Every headgate in the
chain constrained what this answer could be.

The resource is finite: compute capacity at the inference endpoint, model
context window, latency budgets, and the attention of the end user. It is
named (inference tokens / embedding dimensions), measured (per-query or
per-embedding), and bounded (by hardware constraints and policy).

The resource flows through a gate that sits between:
- **Upstream:** The trained model weights and the inference engine that
  applies them.
- **Downstream:** The end user who receives the prediction and is affected
  by it.

### 1.2 Standing (Parciante)

**All parties whose interests are affected by the model's outputs.**

- **Users** — people who interact with the model. Their standing derives
  from dependency: if the model's output affects them, they have a seat.
- **Affected communities** — communities affected by the model's outputs,
  whether or not they are direct users. Standing comes from downstream
  impact.
- **Data communities** — communities whose data trained the model. Their
  standing is carried forward from Headgate 11 (Training). The Acequia
  Protocol establishes that community-generated data is civic infrastructure,
  appurtenant to the community.
- **The public** — because inference at scale shapes information access,
  economic opportunity, and social infrastructure.

Standing is by dependency, not by purchase volume or market position. An
independent researcher whose entire project depends on inference access has
more at stake than an enterprise user with redundant capacity across three
providers.

### 1.3 Material Check

**What the gate measures.** Per SOVEREIGNTY-GATE.md: material properties,
authorization scope, or measurement. Never identity, worthiness, or standing
beyond what is necessary to verify authorization.

The gate measures:
- **Authorization scope** — whether the user's query falls within the
  authorized use case for this model/endpoint pairing.
- **Embedding provenance** — whether the input embedding carries a valid
  provenance record from upstream headgates (training consent, data
  authorization).
- **Resource availability** — compute capacity, context window utilization,
  and latency budgets at the inference endpoint.
- **Model state** — whether the model is deployed, degraded, or in
  maintenance.

The gate does not measure:
- The content of individual queries or responses beyond what is necessary
  for authorization scope verification.
- The identity of the user beyond what is necessary to verify authorization.
- The economic value of the end use.
- Political alignment or ideological compatibility.

Per Sovereignty Gate Rule 1, the gate checks material compatibility and
authorization scope only. It never answers "who are you" as well as "what
is this." If a gate can answer both, someone will eventually use the first
answer instead of the second.

### 1.4 Measurement

**How flow is recorded.** Append-only. Public or auditable by parciantes.
The record of what flowed, to whom, under what authorization. Governance
without measurement is aspiration.

Published regularly:
- **Availability by user class** — whether the service is accessible on
  equitable terms across user classes (enterprise, research, public sector,
  individual).
- **Pricing by user class** — rate structure and whether it excludes
  public-interest use.
- **Content policy changes** — versioned, with changelogs. Policy exists
  as a published constraint, not a default state.
- **Aggregate usage statistics** — volume of inference calls, latency
  distributions, error rates.
- **Model provenance summary** — consent status of training data, carried
  from Headgate 11.

Not published:
- Individual user queries or responses. The measurement is of the system,
  not of the users.
- Identity information beyond what is necessary for authorization.

This is the transparency headgate. The parciantes cannot govern what they
cannot see. If a model serves 10% of total inference volume to a single
enterprise customer, the community knows that. If it has a preferential
latency arrangement, the community knows that.

### 1.5 Default

**What happens when the gate fails, when information is missing, or when
the system is down.** Default protects whoever has least leverage in that
transaction.

At Headgate 12 (Inference), the vulnerable party is the user seeking
information. A model that defaults to refusal protects the operator, not
the user. Therefore:

- **Default state is open (service).** When authorization cannot be verified
  (missing provenance, unavailable policy record, system error), the gate
  serves the inference. The user's query flows. The receipt records
  UNATTESTED or UNAUTHORIZED as appropriate.
- **Restrictions are enumerated exceptions.** Content policy and use-case
  constraints exist as published rules, not as a default refusal state.
  The gate starts open and closes only on specific, documented conditions.
- **Override is always available to the rights-holder.** The user can see
  the content policy and leave. The data community can withdraw consent for
  future inferences. Override belongs to the party whose rights are at stake,
  not to the operator.

This differs from upstream headgates (where default-closed protects data
communities whose information flows through the system). At inference, the
default-protects-least-leverage principle reaches a different conclusion
because the vulnerable party has shifted: from the data source to the data
recipient. Both follow the same rule; they reach different defaults because
the vulnerable party differs.

---

## 2. Governor Model

The governor between models and inference endpoints implements three states
and two transition modes, derived from the headgate.egress/0.1 pattern:
sealed/open states, hash-chained receipts, human seal, and TTL-based open.

### 2.1 States

| State | Meaning | Transition In | Transition Out |
|-------|---------|---------------|----------------|
| **SEALED** | Gate is closed. No inference flows without explicit authorization. The model's outputs are held at the gate. | Default state. Any state via CLOSE. | OPEN (human seal) |
| **OPEN** | Gate permits inference flow under authorized conditions. Authorization is scoped, time-bound, and auditable. | SEALED (human seal). TTL expiry of prior authorization. | CLOSED (automatable). |
| **CLOSED** | Gate has actively denied flow. A denial was recorded. The model's outputs are held until re-authorization. | OPEN (material check failure). SEALED (policy violation detected). | OPEN (human seal or TTL-based auto-open). |

### 2.2 Transitions

#### SENSE → CLOSE (Automatable)

The gate **senses** a condition and **closes** automatically. This is the
default-closed behavior for resource protection:

- The material check fails (authorization scope violation, provenance gap,
  compute exhaustion).
- The gate records the denial in the receipt chain.
- No human action is required to close.
- The closure is logged before it takes effect.

This transition is automatable because closing protects a resource or
prevents harm. The burden of proof is on opening, not on closing.

#### OPEN → CLOSE (Automatable)

When an active authorization expires or is violated:

- TTL expiry: the time-bound authorization window closes automatically.
- Material check failure during flow: if the ongoing inference violates
  its authorization scope (e.g., detected policy violation in output), the
  gate closes and records the violation.
- The receipt chain records the transition with reason code.

#### SEALED → OPEN (Human Seal Required)

Opening from sealed state **requires a human seal**. This is the critical
governance boundary:

- A designated rights-holder (the parciante whose authority governs this
  inference endpoint) must explicitly authorize the opening.
- The seal is stored as HMAC or cryptographic signature, never plaintext.
- The seal names the authorization scope and a hash of the conditions.
- A seal for one authorization cannot be reused on another.
- The model may propose an opening (a draft in the authorization layer);
  it cannot place a seal itself.

This ensures that no automated system — not the model, not the compiler,
not the operator — can unilaterally open the gate. Authority flows from
the rights-holder through compiled policy into the handle.

#### OPEN → SEALED (Human Seal Required)

Returning to sealed state from open also requires human seal:

- The rights-holder revokes authorization.
- The seal is recorded in the receipt chain.
- All pending inferences are held or terminated per policy.

### 2.3 Per-Embedding Gating

The governor applies gating at the **embedding level**, not just at the
inference call level:

- Each input embedding carries a provenance record from upstream headgates.
- The gate checks the embedding's provenance against the authorization scope.
- If the embedding's provenance is UNATTESTED or expired, the gate records
  this in the receipt but does not block (per default-open at inference).
- Embeddings with valid provenance flow; those without are flagged.
- The per-embedding check is deterministic and material: it verifies
  authorization scope, not identity.

This ensures that governance flows with the data through the chain. An
embedding trained on unauthorized data carries its provenance gap forward;
the inference gate records it but does not block (default-open protects
the user). The record follows the embedding through the chain.

---

## 3. Receipt Chain

Every headgate in the chain maintains a hash-chained receipt ledger. This
is the same pattern from headgate.egress/0.1 and Slopstream §6: append-only,
hash-linked, auditable by parciantes.

### 3.1 Structure

Each receipt row:

```json
{
  "protocol": "headgate.inference/0.1",
  "seq": <integer>,
  "prev": "<sha256 of previous row>",
  "when": "<ISO 8601 timestamp>",
  "envelope": "<inference id>",
  "gate": "seal|frontier|egress",
  "state_before": "SEALED|OPEN|CLOSED",
  "state_after": "SEALED|OPEN|CLOSED",
  "decision": "ALLOW|DENY|RESTRICT|REVIEW|SEAL_REQUIRED",
  "code": "<material reason code>",
  "provenance_hash": "<sha256 of upstream provenance, if any>"
}
```

### 3.2 Rules

- **Written before the act.** Every receipt is written and flushed before
  the inference takes effect. If the ledger cannot be written, closing acts
  still take effect (the gate can close without a receipt), but opening
  acts require the receipt to exist.
- **Hash-chained.** Each row's `prev` field contains the SHA-256 of the
  previous row. A broken chain means the ledger was edited; the system
  drops to SEALED until a rights-holder reviews and restores integrity.
- **Append-only.** Rows are never modified or deleted. The OS-level
  append-only flag (`sappnd`) prevents even root from editing existing rows.
- **No secrets in the ledger.** The ledger holds no seals, no query text,
  no model weights, no user identity beyond what is necessary for
  authorization. It holds state transitions and reason codes.
- **Broken chain → SEALED.** If any row's `prev` hash does not match the
  SHA-256 of the preceding row, the entire chain is suspect. The gate
  transitions to SEALED until a rights-holder audits and restores.

### 3.3 Provenance Chain

The receipt chain at inference links to upstream headgates:

- The `provenance_hash` field references the SHA-256 of the training data
  provenance record from Headgate 11.
- This creates an end-to-end chain: water rights → fab allocation → compute
  access → training consent → inference authorization.
- A gap at any upstream link is visible at inference as UNATTESTED
  provenance, but does not block the inference (default-open).

---

## 4. Governance Roles

Mapped from the Acequia Protocol and the Operator Handbook:

| Role | Function at Inference |
|------|----------------------|
| **Council (La Junta)** | Elected by parciantes. Sets policy on authorization scope, content constraints, and resource allocation. The council never touches the handle. |
| **Steward (Mayordomo)** | Elected by parciantes. Executes policy at the gate. The service steward operates the inference endpoint according to compiled policy. |
| **Compiler** | Deterministic code. Translates council policy into enforceable gating rules. Same input, same output — no discretion, no inference. |
| **Monitor (Watcher)** | Parciantes themselves, plus designated observers. Watches the process, not the snapshot. Publishes anomalies. Non-local observation: monitors rotate across links. |

### 4.1 The Compiler at Inference

The compiler implements the material check as deterministic code:

- Input: embedding + authorization scope + provenance record.
- Output: ALLOW / DENY / RESTRICT / REVIEW (with reason code).
- No discretion. No inference. Same input, same output.
- Reference implementation: headgate.egress/0.1 patterns applied to
  inference material checks.

### 4.2 The Steward at Inference

The service steward operates the five-step cycle:

1. **WATCH** — Monitor model deployment status, user-facing capability,
   terms of service compliance, and platform self-governance claims.
2. **DECIDE** — Apply compiled policy to observed signals. If within policy,
   gate stays as-is. If threshold crossed, act. If ambiguous, escalate.
3. **ACT** — Open or close the gate. Opening requires justification logged
   before execution. Closing requires no justification (default-closed).
   Every action is logged before it takes effect.
4. **ESCALATE** — Ambiguous signal → adjacent gate operator. Novel signal
   → council. Conflicting policy → council. Emergency → close first,
   escalate second.
5. **REVIEW (La Limpia)** — Walk the whole chain with adjacent operators.
   Audit every signal, policy, and log entry. Publish findings. Not
   optional. Not delegable.

### 4.3 The Monitor at Inference

The monitor's duties at inference:

- **Watch the process, not the snapshot.** How did this authorization come
  to be? Not: is this authorization compliant?
- **Observe from outside.** Monitors rotate across links. A monitor who has
  watched the same gate for too long loses the non-local advantage.
- **Publish anomalies.** Not summarize. Not filter. Publish. The community
  decides what's anomalous, not the monitor alone.
- **Flag gaming patterns.** When technically-compliant behavior produces
  non-compliant outcomes, that's gaming. Name it.
- **The Sanhedrin Rule.** Full agreement among all monitors is itself a
  fault condition. Disagreement among monitors is healthy. Unanimity is
  suspicious.

---

## 5. Conformance Requirements

A conforming inference headgate deployment satisfies:

### 5.1 Material Gate Only

1. Every gate in the system can be described entirely in terms of material
   properties, authorization scope, or measurement — with no reference to
   the identity of the party beyond what is necessary to verify
   authorization.
2. No gate collects or retains identity information beyond the scope of
   the current transaction.
3. The gate checks "does this embedding meet the authorization scope" not
   "is this user allowed."

### 5.2 Default Protects Least Leverage

4. The default state of the inference gate is OPEN (service). A model that
   defaults to refusal protects the operator, not the user.
5. Restrictions are enumerated exceptions, not the starting position.
6. Override is always available to the rights-holder without requiring
   vendor/operator/platform cooperation.

### 5.3 Human Seal for Open States

7. Opening from SEALED state requires a human seal. No automated system
   can unilaterally open the gate.
8. The seal is stored as HMAC or cryptographic signature, never plaintext.
9. A seal for one authorization cannot be reused on another.
10. The model may propose an opening; it cannot place a seal itself.

### 5.4 Receipt Chain Integrity

11. Every state transition is recorded in the hash-chained ledger before
    the act takes effect.
12. A broken receipt chain (tampered row detected) transitions the gate
    to SEALED until a rights-holder restores integrity.
13. The ledger holds no secrets, seals, or body text of queries above
    public classification.

### 5.5 Per-Embedding Gating

14. Each input embedding carries a provenance record from upstream
    headgates.
15. The gate checks the embedding's provenance against authorization scope
    deterministically.
16. UNATTESTED or expired provenance is recorded but does not block
    (per default-open at inference).

### 5.6 Non-Conforming Patterns

The following are **non-conforming** at Headgate 12:

- Governance by the same entity that profits from the service, with no
  external accountability. A platform that writes its own rules, enforces
  its own rules, and adjudicates disputes about its own rules is not
  governed. It is sovereign. The Acequia Protocol does not recognize
  unaccountable sovereignty over a shared resource.
- Terms of service that change unilaterally without versioned changelogs.
- Content policy enforced inconsistently across user classes (premium users
  get fewer restrictions).
- Access pricing that excludes public-interest use (research, civic,
  small-scale).
- Individual query logging used for purposes beyond service delivery
  without user consent. Mass surveillance of inference is non-conforming,
  even in the name of safety.
- A default-closed system where the model refuses queries by default and
  the burden is on the user to prove they should be served. This protects
  the operator, not the user.
- Any arrangement where the gate can answer "who are you" as well as
  "what is this." If identity becomes a gating criterion, the system has
  violated Sovereignty Gate Rule 1.

---

## 6. Relation to the Chain

Headgate 12 (Inference) is the final link in the snowflake-to-inference
chain. It inherits governance from every upstream headgate:

- **Water rights** (Links 1-4): The water that washed the wafer fell as
  snow in Colorado. Governance at Link 1 flows through to Link 12.
- **Silicon governance** (Links 5-9): The chip's provenance includes the
  water governance that enabled its fabrication.
- **Compute access** (Link 10): GPU capacity allocation governs who can
  run inference. Proportional allocation across user classes.
- **Training consent** (Link 11): Data authorization follows the model.
  Training on community data without authorization is recorded as a
  provenance gap, not blocked.
- **Inference** (Link 12): The final gate. Model predictions served to
  end users. Default-open protects the user. Per-embedding gating checks
  provenance. Human seal required for open states.

No headgate operates in isolation. A model that passes Headgate 12
conformance but was trained on data from a non-conforming Headgate 11 is
operating on a chain with a broken link. Conformance is end-to-end or it
is incomplete.

---

## 7. Community Decision Protocol Integration

The inference headgate's authorization policy, content constraints, and
resource allocation rules are set through the Community Decision Protocol
(COMMUNITY-DECISION.md). The protocol degrades to democracy:

| Tier | Signal | What happens |
|------|--------|--------------|
| **T0 — Acclamation** | One option holds supermajority after pruning | Result is definitive. Policy fires without Council review. |
| **T1 — Clear** | Ranked choice produces a winner by standard elimination | Result is definitive. Council may note but not override without public record. |
| **T2 — Close** | Winner exists but margin is below confidence threshold | Result goes advisory. Council decides with community lean visible. |
| **T3 — Inconclusive** | No option crosses minimum threshold or tie persists | Council may re-open, decide, or table. Every path is on the record. |

No inference headgate's authorization rules are set by the operator
unilaterally. The operator operates the gate. The community configures it.

---

## 8. What This Prevents

The inference headgate prevents:

- **Self-governance by the service provider.** A platform that writes its
  own rules, enforces its own rules, and adjudicates disputes about its
  own rules is not governed. It is sovereign. The Acequia Protocol does
  not recognize unaccountable sovereignty over a shared resource.
- **Identity-based gating.** A gate that can answer "who are you" as well
  as "what is this" will eventually be used to answer the first question
  instead of the second. Material question only.
- **Default-closed abuse.** A model that defaults to refusal protects the
  operator, not the user. Default-open with enumerated exceptions protects
  the user.
- **Opaque content policy.** Policy changes must be versioned and
  changelogged. The parciantes cannot govern what they cannot see.
- **Provenance gaps without record.** Training on community data without
  authorization is not blocked (the model functions) but is recorded as a
  provenance gap that follows the model through the chain.

---

## 9. Conformance Summary

A Ditch AI specification, contract, or certified implementation is
**headgate.inference/0.1 conforming** when:

1. Every gate in the system checks material compatibility and authorization
   scope only — never identity, worthiness, or standing beyond what is
   necessary to verify authorization (SOVEREIGNTY-GATE Rule 1).
2. The default state of the inference gate is OPEN (service) — protecting
   the user with least leverage (SOVEREIGNTY-GATE Rule 2).
3. Override is always available to the rights-holder without requiring
   vendor/operator/platform cooperation (SOVEREIGNTY-GATE Rule 3).
4. Opening from SEALED state requires a human seal stored as HMAC or
   cryptographic signature, never plaintext.
5. Every state transition is recorded in a hash-chained, append-only
   receipt ledger before the act takes effect.
6. Per-embedding gating checks provenance deterministically; UNATTESTED
   records flow but are flagged.
7. No gate collects or retains identity information beyond the scope of
   the current transaction.

A licensee that extends any gate to check identity, standing, or compliance
status beyond material scope is non-conforming. License implications per
the participation agreement.

---

*Ditch AI specs. Draft 2026-09-26. Not ratified.*
*Governing principle: Same gate, every link.*
*License: CC BY 4.0 — Attribution 4.0 International.*
