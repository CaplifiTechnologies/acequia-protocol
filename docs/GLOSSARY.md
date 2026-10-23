# Acequia Protocol Glossary

**Version:** 0.1 -- Draft 2026-09-17
**Scope:** Every defined term, role, mechanism, test, data structure, and
named pattern across the Ditch AI project.
**Tier key:** FULL = acequia/protocol jargon (specs and implementers only);
HANDLE = audience-facing language; LABEL = universal one-liner language.

---

## Governance Roles

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Comisionado** | Commissioner on the ditch commission. Elected by parciantes. | FULL | FOUNDING-DOCUMENT |
| **Compiler** | Deterministic code that translates council policy into enforceable rules. Same input, same output, no inference, no discretion. A governed artifact, not a neutral mechanism. | FULL | HANDBOOK-SPEC |
| **Council (La Junta)** | Elected governing body of the parciantes. Sets policy (the WHAT). Never touches the handle. | FULL | HANDBOOK-SPEC |
| **Ditch commission** | Elected body governing an acequia. Three roles: set allocation, manage operations, adjudicate disputes. | FULL | FOUNDING-DOCUMENT |
| **Founding Steward** | Time-limited stewardship role. Caplifi Technologies holds this for Ditch AI; sunsets when a seated table ratifies the charter or after 24 months. The steward is a seat, not the table. | HANDLE | GUIDE |
| **Mayordomo** | Ditch boss. Elected steward who executes policy at the gate. Operates the five-step cycle (Watch, Decide, Act, Escalate, Review). Touches the handle. Does NOT set policy. | FULL | HANDBOOK-SPEC, FOUNDING-DOCUMENT |
| **Monitor (Watcher)** | Separate observation role. Not the operator, compiler, or council. Watches for gaming, circumvention, or slanted use through process-based observation. Recommended split: watchers (distributed, outcome-focused) and auditors (domain-qualified, process-focused). | FULL | HANDBOOK-SPEC |
| **Parciante** | Water rights holder with labor obligations. Has standing by dependency on the resource. At Links 1-4: decreed water users. At Links 5-12: anyone downstream of the flow. | FULL | FOUNDING-DOCUMENT, HANDBOOK-SPEC |

---

## Core Mechanisms

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Acequia** | Community-operated irrigation ditch. The physical infrastructure and the governance system built around it. Predates every American political party. | HANDLE | FOUNDING-DOCUMENT |
| **Acequia madre** | Main ditch. The primary channel from which laterals branch. | FULL | MAYORDOMO-TOOL-SPEC |
| **Acequia Protocol** | Open governance specification for shared infrastructure, modeled on acequia irrigation commons. Governs two flows: the supply chain under AI and community data infrastructure. | HANDLE | GUIDE, FOUNDING-DOCUMENT |
| **Aforo** | Water measurement at the headgate. The act of measuring flow. | FULL | BRAND |
| **Appurtenance** | A right attached to the land, not the person. Water cannot be severed from the community that depends on it. | FULL | WHAT-IT-IS |
| **Beneficial use** | Water must be put to productive use or the right lapses. Use it or lose it. | FULL | FOUNDING-DOCUMENT |
| **Headgate** | Physical or logical structure where allocation happens. The point where a governed decision controls how much resource flows to whom. Every transition in the supply chain is a potential headgate. | HANDLE | HEADGATE-CHAIN, FOUNDING-DOCUMENT |
| **La Limpia** | Annual ditch cleaning and inspection walk. The review phase of the operator cycle. In the chain: cross-link La Limpia walks all 12 links together, making every observer non-local at 11 of 12 links. | FULL | HANDBOOK-SPEC |
| **Lateral** | Branch ditch off the acequia madre. Serves a subset of parcels. | FULL | MAYORDOMO-TOOL-SPEC |
| **Repartimiento** | Water allocation and rotation schedule. Who gets water when, in what order, for how long. The ditch rotation IS the agricultural calendar. | FULL | FOUNDING-DOCUMENT, CALENDRICS-THREADS |
| **Sangria** | Lateral or branch ditch. Alternate term for a smaller diversion channel. | FULL | MAYORDOMO-TOOL-SPEC |
| **Suerte** | Parcel of irrigated land. A unit served by the acequia. | FULL | MAYORDOMO-TOOL-SPEC |

---

## Protocol Specs

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Community Decision Protocol** | "Degrade to democracy." Governance decision framework with four confidence tiers (T0-T3). Community decides when confidence is high; governing body decides when signal is weak. Deliberate non-decision is a first-class outcome. | HANDLE | COMMUNITY-DECISION |
| **DAC-1** | Referenced canonical standard designation for the Acequia Protocol. Not yet produced as a consolidated document. | HANDLE | GUIDE |
| **Governed Autonomy** | Conformance spec for AI systems operating under the Acequia Protocol. Draft v4. | FULL | TELOS, GUIDE |
| **Headgate Chain** | 12-link governance chain from snowflake to inference. Same five primitives at every link. The first four links have 400+ years of acequia governance; the last eight are new. | HANDLE | HEADGATE-CHAIN |
| **Neutral Contract** | Contract where the vendor is a swappable seat. The contract survives when the vendor changes. | HANDLE | TELOS, GUIDE |
| **Resilience Gate** | Crisis governance spec based on the Gary, Indiana derecho (Aug 2026). Six layers ensuring infrastructure survives sustained outage. | FULL | RESILIENCE-GATE |
| **Sovereignty Gate** | Three rules governing every gate in the protocol: (1) material question only, (2) default protects least leverage, (3) override to rights-holder. | HANDLE | SOVEREIGNTY-GATE |

---

## Sovereignty Gate Terms

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Default protects least leverage** | When a gate fails, the failure mode protects the party who can least afford the gate going wrong. For data: default-closed (protects the individual). For inference service: default-open (protects the user). Same principle, different default, because the vulnerable party differs. | HANDLE | SOVEREIGNTY-GATE, HEADGATE-CHAIN |
| **Material question** | What the gate checks: resource attributes, volume, composition, provenance, authorization scope. The gate measures the resource, not the person. | FULL | SOVEREIGNTY-GATE |
| **Override to rights-holder** | Override is always available to the party whose rights are at stake, not to the operator. The parciante can challenge allocation; the data community can withdraw consent; the user can see policy and leave. | FULL | SOVEREIGNTY-GATE |
| **Social function** | What the gate must NOT acquire: identity checks, worthiness tests, network membership requirements, standing gates. A material gate that acquires a social function is non-conforming. | FULL | SOVEREIGNTY-GATE |
| **UNATTESTED** | Flag for a component or link with unknown or unverifiable provenance. A non-attested component flows through the gate with the flag; it is not blocked. | FULL | SOVEREIGNTY-GATE, HEADGATE-CHAIN |

---

## Community Decision Protocol Terms

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Degrade to democracy** | Design principle: start with acclamation, fall through to ranked choice, then to governing body with lean visible, then to explicit non-decision. Each tier is a fallback, not a replacement. | HANDLE | COMMUNITY-DECISION |
| **Non-decision** | Deliberate choice not to decide. A first-class outcome, not a failure. Carries explicit documentation: what was proposed, why no decision, what would reopen. | FULL | COMMUNITY-DECISION |
| **Proposal** | The thing being decided. Two origins: council-initiated or community-initiated (petition). | FULL | COMMUNITY-DECISION |
| **T0 (Acclamation)** | Community preference is obvious. No formal vote needed. Schedule is definitive. | FULL | COMMUNITY-DECISION |
| **T1 (Ranked Choice)** | Ranked-choice voting produces a clear winner above confidence threshold. Schedule is definitive. | FULL | COMMUNITY-DECISION |
| **T2 (Narrow Margin)** | Ranked choice produces a winner but margin is thin. Governing body decides with community lean visible. | FULL | COMMUNITY-DECISION |
| **T3 (Inconclusive)** | Signal is inconclusive. Governing body decides, re-opens, or tables. Every path is on the record. | FULL | COMMUNITY-DECISION |
| **Town Council** | Governing body in the Community Decision Protocol. Analogous to La Junta. | FULL | COMMUNITY-DECISION |

---

## The Twelve Links (Headgate Chain)

| Link | Name | Operator | Status | Source |
|------|------|----------|--------|--------|
| 1 | Snowpack / Headwater | Watershed steward | Already governed (150+ years) | HEADGATE-CHAIN |
| 2 | River / Conveyance | Ditch rider / mayordomo | Already governed (400+ years) | HEADGATE-CHAIN |
| 3 | Storage / Reservoir | Dam operator | Already governed (Bureau of Reclamation) | HEADGATE-CHAIN |
| 4 | Allocation / Distribution | Water commissioner | Already governed (state engineer) | HEADGATE-CHAIN |
| 5 | Bulk Transport | Pipeline/canal steward | NEW -- proportional curtailment | HEADGATE-CHAIN |
| 6 | Municipal Delivery | Municipal utility operator | NEW -- transparency headgate | HEADGATE-CHAIN |
| 7 | Industrial Consumption | Compliance officer | NEW -- self-governance, burden on consumer | HEADGATE-CHAIN |
| 8 | Fabrication Capacity | Fab allocation steward | NEW -- public subsidy creates public standing | HEADGATE-CHAIN |
| 9 | Chip Distribution | Source allocation steward | NEW -- source governance, not export controls | HEADGATE-CHAIN |
| 10 | Compute Access | Datacenter allocation steward | NEW -- proportional across user classes | HEADGATE-CHAIN |
| 11 | Training | Training run steward | NEW -- provenance follows the model | HEADGATE-CHAIN |
| 12 | Inference | Service steward | NEW -- default is service (open) | HEADGATE-CHAIN |

---

## Five Primitives (per headgate)

| Primitive | Definition | Source |
|-----------|-----------|--------|
| **Resource** | What flows through the gate. Water, chips, compute, data, inference. | HEADGATE-CHAIN |
| **Parciante standing** | Who has governance rights at this gate. Determined by dependency on the resource. | HEADGATE-CHAIN |
| **Material check** | What the gate measures. Resource attributes only, never identity. | HEADGATE-CHAIN |
| **Measurement** | What gets published. Transparent, regular, auditable. | HEADGATE-CHAIN |
| **Default** | Failure mode behavior. Protects whoever can least afford the gate going wrong. | HEADGATE-CHAIN |

---

## Operator Cycle

| Step | Definition | Cognitive demand | Source |
|------|-----------|------------------|--------|
| **1. Watch** | Read the signals. The sentinel reports; you interpret. | Literacy (read a gauge, compare to a number) | HANDBOOK-SPEC |
| **2. Decide** | Apply compiled policy to what you see. Clear signal = act. Ambiguous = escalate. Never guess. | Judgment (clear vs ambiguous) | HANDBOOK-SPEC |
| **3. Act** | Open or close the gate. Log before acting. Irreversible actions require a second operator's witness. | Discipline (write then turn the handle) | HANDBOOK-SPEC |
| **4. Escalate** | When you don't know, say so. Ambiguous = adjacent operator. Novel or conflicting = council. Emergency = close first, escalate second. | Honesty (say "I don't know") | HANDBOOK-SPEC |
| **5. Review (La Limpia)** | Walk the whole channel periodically. Physical or digital audit. Publish findings. Not optional, not delegable. | Thoroughness (check every fitting) | HANDBOOK-SPEC |

---

## Tests

| Test | Definition | Source |
|------|-----------|--------|
| **Derecho Test** | 8 criteria for crisis governance readiness, derived from the Gary, Indiana derecho (Aug 2026, 14-day outage). Tests whether infrastructure can survive sustained power/communications failure while maintaining governed data custody. | RESILIENCE-GATE |
| **Granite Test** | "Can this instruction be carved in stone and understood by an operator who has never seen the technology that flows through the channel?" Design standard for handbook procedures. Some gates are irreducibly complex and need accredited technical stewards; the granite test is the aspiration, the complexity taxonomy says where it cannot yet be met. | HANDBOOK-SPEC |
| **Williams Test** | Named after the Kenneth Williams incident during the Gary derecho. Tests whether governance survives the intersection of infrastructure failure and civil emergency. | RESILIENCE-GATE |

---

## Resilience Gate Layers

| Layer | Definition | Source |
|-------|-----------|--------|
| **Collection continuity** | Data keeps flowing during crisis. Sensors and collection points have local fallback. | RESILIENCE-GATE |
| **Custody during crisis** | Data stays in governed custody when systems fail. No unattended handoff to vendor or cloud. | RESILIENCE-GATE |
| **Governed restoration priority** | When systems come back, restoration order is governed, not ad hoc. | RESILIENCE-GATE |
| **Vendor dependency** | The system must function (degraded) without the vendor's cloud/support. | RESILIENCE-GATE |
| **Crisis governance mode** | Governance continues under crisis conditions. Reduced but not absent. | RESILIENCE-GATE |
| **Inverted headgate** | Crisis reverses normal flow priorities. Emergency access overrides normal allocation. | RESILIENCE-GATE |

---

## Brand and ORIGAMI

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Base figure** | The unfolded standard. The full truth before any audience fold is applied. | FULL | BRAND |
| **Crease** | A declared fold variant. Each crease hides detail but never changes the claim. 27+ creases declared across 6 dimensions. | FULL | BRAND |
| **Fan-copy ban** | Internal terms that must never appear in public copy: headgate, DAC-1, Founding Steward, INSTIGATE, parciante, comisionado, mayordomo, repartimiento, aforo, etc. | FULL | BRAND, GUIDE |
| **Five flows** | Supply chain, community data, water, labor, AI governance. The five governed flows in the Acequia Protocol, each with telos/anti-telos pairs. | FULL | BRAND |
| **Fold rule** | Every tier must be true. A HANDLE pitch that promises something the FULL spec does not support is non-conforming. Folding hides detail, never changes the claim. | FULL | BRAND, GUIDE |
| **FULL tier** | The spec itself. Acequia terms allowed. For parciantes, implementers, and counsel -- never for a landing page. | FULL | BRAND, GUIDE |
| **HANDLE tier** | The audience's own problem. Same positioning spine, different problem statement and examples for each audience. | HANDLE | BRAND, GUIDE |
| **LABEL tier** | The one-liner for everyone. "Nobody owns the ditch." No jargon, no audience-specific language. Always safe to print. | LABEL | BRAND, GUIDE |
| **ORIGAMI fold grammar** | Brand architecture where variants are declared folds on one sheet across six dimensions (visual, structural, focus, surface, privacy, language). Same truth at every tier, different fidelity for each audience. | FULL | BRAND |
| **Positioning spine** | Three phrases, in order: (1) Commons body, (2) Independent check, (3) Swappable vendor. Holds at every ORIGAMI tier. | HANDLE | GUIDE |
| **Voice test** | "Phone in a parking lot after a basin meeting." Every sentence Ditch AI publishes should sound like something a water district director would say to a neighbor after a long meeting -- plain, specific, no pitch. | FULL | GUIDE |

---

## Campaign Sentinel

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **G0 (Walkthrough)** | Synthetic stack demo. Claimed vs measured. No live systems. Free. | HANDLE | CAMPAIGN-SENTINEL |
| **G1 (Town brief)** | Manual read: what is claimed, what is measured, which paths can still close. Named only under signed annex. | HANDLE | CAMPAIGN-SENTINEL |
| **G2 (Independent check)** | Attestation by a party with no stake. Product, vendor, mark. | HANDLE | CAMPAIGN-SENTINEL |
| **G3 (Swappable contract)** | Measurement, pay, and proof in the book. The vendor is a seat. Contract survives vendor change. | HANDLE | CAMPAIGN-SENTINEL |
| **Scan-Score-Ledger-Hand** | Four engine verbs. Scan: claimed vs measured. Score: whether the balance was chosen. Ledger: append-only, hash-chained. Hand it over: warning goes to the rights-holder, not the vendor or a buyer. | HANDLE | CAMPAIGN-SENTINEL |
| **The Wall** | Three surfaces with different disclosure levels: Public (anonymized, no names), Signed brief (real stack, named), Town's own report (theirs, not sold). Four extra rules: people are not the plant, disclosure guaranteed, no self-attestation, no fake backtest. | FULL | CAMPAIGN-SENTINEL |
| **Warn does not equal capture the seat** | The one who warns never buys. A warning that becomes a capability manual is diesel for the other cab. | HANDLE | CAMPAIGN-SENTINEL |

---

## Telos

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Anti-telos** | What the project exists to prevent. The failure mode that governance is designed to block. Each flow and spec has a declared anti-telos. | FULL | TELOS files, GOVERNANCE-BY-TELOS |
| **Bindings** | Connections between a telos declaration and agents, projects, or products. A telos without bindings is aspirational. | FULL | TELOS files |
| **Telos** | Declared purpose binding agents and projects. Purpose replaces intent; human-only submit; publish gate. A telos is what a thing is FOR, tested by whether the work serves or undermines it. | FULL | GOVERNANCE-BY-TELOS, TELOS files |
| **Telos commons** | Open-published telos declarations. Ditch AI is the publisher. Phase 6 of the ALMI telos build plan. | FULL | GOVERNANCE-BY-TELOS |

---

## Mayordomo Tool

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Crease pattern** | Full layout of all ditches in a valley. Equivalent to a ditch network map. | FULL | MAYORDOMO-TOOL-SPEC |
| **Delivery contact** | Two parcels sharing water infrastructure through the fold topology. The output of the Route operation. | FULL | MAYORDOMO-TOOL-SPEC, mayordomo.py |
| **Design operation** | Specify which parcels need water delivery, derive the ditch layout that provides it. Inverse of Route. Maps to E8 hypothesis H3. | FULL | MAYORDOMO-TOOL-SPEC |
| **Divergence metric** | Measure of how much delivery topology changes when a ditch is moved or removed. 0 = no change, 1 = completely different. | FULL | mayordomo.py |
| **Impact operation** | Change a ditch, measure what breaks. Which parcels gain or lose water delivery. Maps to E8 hypothesis H2. | FULL | MAYORDOMO-TOOL-SPEC |
| **Mediation ratio** | Fraction of deliveries requiring intermediate ditches. Measures infrastructure dependency. | FULL | MAYORDOMO-TOOL-SPEC, mayordomo.py |
| **origami.fold/0.1** | Document format for valley files. JSON with grid, creases, content assignments, and topology. Acequia vocabulary is an extension layer. | FULL | MAYORDOMO-TOOL-SPEC |
| **Route operation** | Draw ditches on a valley, see which parcels get water delivery. Maps to E8 hypothesis H1. | FULL | MAYORDOMO-TOOL-SPEC |
| **Stack depth** | How many ditch crossings deep the fold topology goes. Measures ditch complexity. | FULL | MAYORDOMO-TOOL-SPEC |
| **Valley** | The land being irrigated, modeled as a grid. Each cell is a parcel (suerte). The substrate on which ditches (creases) are drawn. | FULL | MAYORDOMO-TOOL-SPEC, mayordomo.py |

---

## Research / Calendrics

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Bilateral fold** | Year folded in half across the growing season. Reveals which months "mirror" each other in water allocation. | FULL | d72_fold_calendar.py |
| **D72** | Water Division 72 (North Fork, Grand Junction area). The shakedown dataset for fold calendar research. | FULL | d72_fold_calendar.py |
| **Infrastructure calendrics** | Hypothesis that ancient infrastructure coordinates and mandala geometry encode planting/harvest schedules. Angular proportions in radial divisions are crop-timing data. | FULL | CALENDRICS-THREADS |
| **Quarterly fold** | Year folded into quarters. Cross-quarter contacts show which seasons share infrastructure. | FULL | d72_fold_calendar.py |
| **Seniority band** | Water right priority grouping by appropriation date (senior 1882-1910, mid 1911-1950, junior 1951-2011). | FULL | d72_fold_calendar.py |
| **Valley fold (6x6)** | Full valley model with 36 faces (12 months x 3 seniority bands). E8-compatible grid matching the proven experiment. | FULL | d72_fold_calendar.py |

---

## Lunar Headgate

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Acequia model (lunar)** | Community allocation by need and season applied to lunar water ice. Third governance model considered (after riparian and prior appropriation). | FULL | LUNAR-HEADGATE |
| **DLA** | Development Lease Agreement. Open Lunar Foundation framework for lunar resource governance. | FULL | LUNAR-HEADGATE |
| **Prior appropriation** | "First in time, first in right." Western US water doctrine. One of three models compared for lunar application. | FULL | LUNAR-HEADGATE |
| **Riparian doctrine** | Water rights by land adjacency. Eastern US doctrine. One of three models compared for lunar application. | FULL | LUNAR-HEADGATE |

---

## Review-Coined Terms (accepted into project vocabulary)

| Term | Definition | Origin | Source |
|------|-----------|--------|--------|
| **Anomaly triage protocol** | Reputation-weighted, materiality-classified system for handling published anomalies. Replaces "publish everything" which is a DoS surface. | Review-coined | RED-TEAM |
| **Capture (social / economic / technical)** | Adversarial takeover of governance roles. Social: personal relationships. Economic: financial dependency. Technical: controlling logs or process data. | Review-coined | RED-TEAM |
| **Complexity taxonomy** | Classification of gates by operational complexity. Some pass the granite test; others require accredited technical stewards. The taxonomy admits this. | Review-coined | RED-TEAM |
| **Conformance Level 1 (Gate exists)** | Measurements published, defaults documented. Minimum conformance. | Review-coined | CHAIN-REVIEW |
| **Conformance Level 2 (Community-authorized)** | Allocation rules set through Community Decision Protocol. | Review-coined | CHAIN-REVIEW |
| **Conformance Level 3 (Chain-linked)** | Provenance records published and cryptographically bound to upstream records. Full conformance. | Review-coined | CHAIN-REVIEW |
| **Custodial separation** | The monitored entity cannot be the sole custodian of the process data the Monitor watches. Third-party custody of logs. | Review-coined | RED-TEAM |
| **Federation primitive** | Multi-community/multi-jurisdiction governance mechanism for headgates whose parciantes span multiple governance bodies. Standalone companion spec, not yet written. | Review-coined | CHAIN-REVIEW |
| **Orphaned provenance** | Training data from unidentifiable communities (e.g., Common Crawl). Marked `provenance: unresolved-orphaned` -- distinct from `unauthorized-known-community`. Higher-risk input. | Review-coined | CHAIN-REVIEW |
| **Shadow process** | Adversary runs a clean process for inspection while the real work happens on an unlogged continuation. Process-based observation only catches this with custodial separation. | Review-coined | RED-TEAM |
| **Standing enrollment** | Enrolled, accountable representation replacing diffuse dependency-standing at Links 8-12 where the parciante community is unbounded. | Review-coined | RED-TEAM |

---

## Ditch AI Identity

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Ditch AI** | A commons: open-standards body governing the Acequia Protocol. Not a product, platform, company, or protocol token. Two words, always capitalized as shown. | LABEL | GUIDE |
| **"Nobody owns the ditch"** | The one-liner. Works for any audience. The LABEL tier. | LABEL | GUIDE |
| **"The vendor is a seat. The water is not."** | Gold line. The vendor participates; the resource is not the vendor's to own. | HANDLE | GUIDE |
| **Three jobs** | Hold the specs, check independently, write a swappable contract. What Ditch AI does. | HANDLE | GUIDE |

---

## Banned Words

These words are banned from all Ditch AI copy per the brand guide:

| Word | Reason |
|------|--------|
| seamless | Nothing is seamless. Name the seam. |
| ecosystem | The word that means nothing. Use "mesh" or "supply chain." |
| unlock | Ditch AI does not unlock anything. It holds specs. |
| cutting-edge | Standards bodies are not cutting-edge. They are deliberate. |
| game-changer | No. |
| revolutionize | No. |
| tokenize | Ditch AI does not issue a fungible token. |
| play-to-earn | Not even adjacent. |

---

## Data Governance Primitives

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Community-generated data** | Data produced by municipal surveillance cameras, license plate readers, sensor networks in public spaces. Belongs to the same category as roads -- public infrastructure funded by and operating in the community's interest. | HANDLE | FOUNDING-DOCUMENT, HEADGATE-PAPERS |
| **Civic custody** | Community data physically lives in a civic institution (the local library), not a vendor's cloud, state server, or acquirable platform. Structural inalienability. | HANDLE | WHAT-IT-IS, HEADGATE-PAPERS |
| **Custodial immune system** | Institutional defenses of commons institutions (libraries) against extraction. Publicly funded, locally governed, no shareholders, no fiduciary duty to maximize extraction. | FULL | FOUNDING-DOCUMENT |
| **Custodial independence** | The library's century-plus tradition of refusing to surrender patron records. Librarians treat custodial betrayal as a professional ethics violation, not a procurement decision. | HANDLE | WHAT-IT-IS |
| **Warrant-based access** | Legitimate law enforcement access through the headgate. A detective with a warrant can query the system for scoped, authorized requests; the headgate opens and logs the access. | HANDLE | WHAT-IT-IS, HEADGATE-PAPERS |
| **Scoped query** | A specific question to a specific dataset in a specific window -- e.g., "was this plate seen in this corridor during this window." The governed alternative to bulk access. | HANDLE | WHAT-IT-IS, HEADGATE-PAPERS |
| **Governed federation** | Inter-jurisdictional data sharing where both communities authorize the reciprocal arrangement, queries are scoped to active investigations, and both audit logs record the exchange. Mutual aid, not mutual surveillance. | FULL | WHAT-IT-IS, HEADGATE-PAPERS |
| **Chain of custody** | Evidence integrity maintained because data never left a governed system. Append-only audit ledger with civic custody creates provenance that prosecutors can defend. | HANDLE | WHAT-IT-IS, HEADGATE-PAPERS |
| **Retention discipline** | Community-decided data retention periods (30, 60, 90 days -- voted on and revisable). Contrasted with vendor systems that retain everything because retention is inventory and inventory is the product. | FULL | HEADGATE-PAPERS |
| **Control record** | A public file of who can spend, sign, or launch. Water has CDSS HydroBase. Most towns have no equivalent for AI/compute. The absence of this record is the founding finding. | FULL | CAMPAIGN-SENTINEL |
| **Append-only ledger** | Audit log recording every access: who accessed what, when, under what authorization, for what stated purpose. Hash-chained. Creates chain of custody that holds up in court. | FULL | FOUNDING-DOCUMENT, CAMPAIGN-SENTINEL |
| **Deterministic gate** | A gate whose behavior is determined by rules, not discretion. Does not distinguish between threat sources -- applies the same test to all. | FULL | FOUNDING-DOCUMENT, WHAT-IT-IS |

---

## Anti-Patterns and Failure Modes

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Buy-and-dry** | Severing water rights from agricultural land, drying up the community. The data equivalent: severing community data for sale. | HANDLE | FOUNDING-DOCUMENT |
| **Betrayal of office** | When the mayordomo allows unauthorized diversion through negligence or corruption. Worse than simple theft: the community trusted someone with the headgate and they opened it for someone else's benefit. | FULL | FOUNDING-DOCUMENT |
| **Resale pipeline** | Vendor business model: collect license plate data from municipal cameras, aggregate across jurisdictions into a national movement database no single community authorized, and resell. The cameras are the loss leader; the revenue is in the resale. | HANDLE | HEADGATE-PAPERS |
| **Scope creep without consent** | Systems deployed for narrow purposes (stolen vehicles, Amber Alerts) silently expanding to civil process, debt collection, repossession, insurance fraud. None of the expanded uses were voted on. The headgate was opened for one purpose and never closed. | HANDLE | HEADGATE-PAPERS |
| **Warrantless bulk access** | Federal agencies purchasing commercial surveillance data to circumvent warrant requirements. If data is "commercially available," Fourth Amendment protections erode. Not a loophole -- the business model. | HANDLE | HEADGATE-PAPERS |
| **Laundering mechanism** | What local government becomes when vendors collect at the municipal level under public safety justification, then sell to federal agencies who could not legally collect the same data directly. | HANDLE | HEADGATE-PAPERS |
| **The officer problem** | Individual law enforcement officers using surveillance databases for personal purposes (stalking, surveilling opponents, running plates on neighbors). Documented, repeated incidents. Systems lack governance to prevent this because they were designed to maximize access. | HANDLE | HEADGATE-PAPERS |
| **Rogue control** | Unnoticed or unchosen automation. Even when the brochure is friendly, control that nobody chose is rogue. The Score measures whether the balance was intentional. | HANDLE | CAMPAIGN-SENTINEL |
| **Mutual surveillance** | What results when two towns share data through a vendor -- they have outsourced governance to a private company. The governed alternative is mutual aid. | HANDLE | WHAT-IT-IS, HEADGATE-PAPERS |
| **Presumed open** | Predicted failure mode of default-closed: because the chain exists to deliver resources, operators develop informal "always open" customs written nowhere. The adversary exploits the gap between formal default-closed and informal default-open. | FULL | RED-TEAM |

---

## Attack Patterns (review-coined)

| Term | Definition | Source |
|------|-----------|--------|
| **Staged process attack** | Adversary runs a clean process for inspection and a shadow process for actual production. Examples: dual MES instances at a fab, unlogged continuation training runs, different model artifacts served to dashboards vs production. | RED-TEAM |
| **Economic capture** | Adversary does not buy the non-local monitor directly but captures the monitor's home institution (buying municipal bonds, funding the department, threatening relocation). Monitor independence depends on institutional independence, which the spec does not protect. | RED-TEAM |
| **Capture club** | Adjacent links share an employer or governance chain, turning escalation between them into a rubber stamp. Example: Links 7 and 8 operated by the same water district/economic development authority. | RED-TEAM |
| **Infinite dilution** | Failure mode when parciante standing is defined by dependency alone at global scale: anyone downstream can claim standing, making the voter base so large it is unenforceable or susceptible to flooding with shell dependents. | RED-TEAM |
| **Virtual La Limpia attack** | Host offers a remote version of the cross-link walk using polished dashboards and video tours. Observers accept because travel is expensive, and the walk degrades from inspection to webinar. | RED-TEAM |
| **Monitor Support Foundation attack** | Monitored entity funds a foundation that nominates monitors, pays their expenses, provides legal insurance, and sets publication guidelines. Monitors are technically independent but their incentive structure is captured. | RED-TEAM |
| **Dual-use laundering** | Foundry labels chips bound for a prohibited end-use as a different category (e.g., supercomputer chips labeled "general commercial GPUs"). Non-local observers see a complete manifest but cannot detect the false end-use classification. | HANDBOOK-REVIEW |
| **Split manifests / shell consignees** | Gaming tactics at chip distribution: splitting shipment records to obscure total volume, or routing through intermediary entities to hide the true recipient. | HANDBOOK-REVIEW |
| **Gadfly dissent** | One monitor files trivial disagreements on irrelevant points to avoid triggering the Sanhedrin Rule (unanimous agreement fault condition), while substantive agreement on actual gaming is never surfaced. | RED-TEAM |

---

## ORIGAMI Fold Dimensions

| Dimension | Values | Source |
|-----------|--------|--------|
| **Flow** | supply-chain, community-data, water, labor, ai-governance | BRAND |
| **Audience** | city-council, library, law-enforcement, water-district, mining, energy, fabrication, compute, civil, labor, policymaker, general | BRAND |
| **Relationship** | outsider, prospect, parciante, comisionado | BRAND |
| **Channel** | landing-page, paper, email, spec, agreement, presentation | BRAND |
| **Stage** | draft, namespace, founding-table, first-contract, seated | BRAND |
| **Tier** | LABEL, HANDLE, FULL | BRAND |

---

## Caucuses

| Caucus | Scope | Source |
|--------|-------|--------|
| **Water** | Irrigation, municipal water, watershed governance | BRAND |
| **Extraction** | Mining, mineral supply chain | BRAND |
| **Fabrication** | Semiconductor manufacturing, fab capacity | BRAND |
| **Energy** | Power generation and distribution | BRAND |
| **Compute** | Data centers, cloud allocation, training runs | BRAND |
| **Civil** | Municipal governance, community data, public safety | BRAND |

---

## Campaign Sentinel Engine

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **Kernel** | The shared operating pattern between Water Sentinel and AI Sentinel: claimed vs measured, hash-chained ledger, deterministic gates. Same kernel, different clock. | FULL | CAMPAIGN-SENTINEL |
| **The Clock** | The timeline of governance drift. The paperwork still says a person is watching, but the clock runs anyway. Sentinel is how a town hears while the flag still says active. | HANDLE | CAMPAIGN-SENTINEL |
| **The Flag** | Status indicator that still says "active" or "human-operated" when the reality may have shifted. The gap between the flag and the measurement is the finding. | HANDLE | CAMPAIGN-SENTINEL |
| **Copy gate** | Editorial quality check for public artifacts. Scans page content for compliance with brand and disclosure rules. Fail-closed. | FULL | CAMPAIGN-SENTINEL |
| **Cohesion pass** | Brand consistency check for public artifacts. Ensures public copy aligns with Ditch AI identity. Fail-closed. | FULL | CAMPAIGN-SENTINEL |
| **Signed brief / annex** | Qualified disclosure containing the real stack, real contract clauses, real key register. Not before qualification. Not public. | FULL | CAMPAIGN-SENTINEL |
| **Town's own report** | The town's private assessment of their own systems, fully named. It is theirs. It is not sold. | HANDLE | CAMPAIGN-SENTINEL |
| **Engine braking** | Operational metaphor: staying in control on a steep grade. The campaign is the radio to the towns about clearing lethal paths. | FULL | CAMPAIGN-SENTINEL |

---

## Additional Review-Coined Mechanisms

| Term | Definition | Source |
|------|-----------|--------|
| **Irreversibility inventory** | Required catalogue per handbook of which actions at each link are irreversible and therefore require the two-witness rule. The spec asserts the witness requirement but never lists which actions qualify. | HANDBOOK-REVIEW |
| **Escalation timeout** | Every escalation path must define a time limit; if the Council does not respond within N hours, the Steward defaults to a protective (closed) state. Without this, manufactured escalation becomes a weaponizable delay tactic. | RED-TEAM, HANDBOOK-REVIEW |
| **Watcher/auditor split** | Decomposition of the Monitor role: watchers (distributed parciantes, outcome-focused) and auditors (domain-qualified, process-focused). Both required to avoid the competence-independence tradeoff. | HANDBOOK-REVIEW |
| **Monitor economics** | Requirement that monitors have a defined funding source, insulation from retaliation, and access to forensic expertise. Without these, monitoring is a "faith-based security model." | RED-TEAM |
| **Materiality classification** | Enhancement to the Sanhedrin Rule: disagreement among monitors must be classified by materiality (significance of the disputed point), not merely counted. Trivial manufactured dissent satisfies the rule's letter while hiding substantive agreement on gaming. | RED-TEAM |
| **Headgate 4.5** | Proposed intermediate gate between acequia headgate (HG4) and bulk distribution (HG5) covering water districts, conservancy districts, or mutual ditch companies that aggregate acequia/compact shares. | CHAIN-REVIEW |
| **Grace/contest mechanism** | Proposed addition to HG7: a path for the penalized facility to trigger an independent audit to rebut the 100%-assumed-consumption default, with costs allocated by outcome. | CHAIN-REVIEW |
| **Constitutional sketch vs operational spec** | Assessment of the handbook spec's current state: strong as a normative architecture, weak as an operational specification. Risk: implementing the form of acequia governance while preserving the substance of industrial capture. | HANDBOOK-REVIEW |

---

## Lunar Headgate Terms

| Term | Definition | Tier | Source |
|------|-----------|------|--------|
| **DLA** | Development Lease Agreement. Open Lunar Foundation framework for lunar resource governance. | FULL | LUNAR-HEADGATE |
| **Riparian doctrine** | Water rights by land adjacency. Eastern US doctrine. One of three models compared for lunar application. | FULL | LUNAR-HEADGATE |
| **Prior appropriation** | "First in time, first in right." Western US water doctrine. Also the ungoverned default at Links 8-12 of the chain. | FULL | LUNAR-HEADGATE, HEADGATE-CHAIN |
| **Artemis Accords** | US-led international framework for lunar exploration. Referenced as precedent in lunar headgate governance. | FULL | LUNAR-HEADGATE |
| **Constellation mechanism** | Governance structure for lunar resources where multiple participating nations share allocation through acequia-modeled governance. | FULL | LUNAR-HEADGATE |

---

## Typography and Color

| Token | Value | Use |
|-------|-------|-----|
| Sand | `#efe6d4` | Page background |
| Cream | `#f7f1e4` | Cards, hero text, button fills |
| Ink | `#1b241c` | Body text |
| Muted | `#5a6658` | Secondary text |
| Water | `#3d6b78` | Links, accents, numbers |
| Water Deep | `#1f3f48` | Nav wordmark, Join section background |
| Earth | `#8a6a48` | Hover accent |
| Mesa | `#6b5a48` | Tertiary accent |
| Fraunces | Display/heading typeface | Variable optical serif |
| Source Sans 3 | Body typeface | Workhorse sans-serif |

---

*Glossary compiled from full content audit of 34+ files across
~/DitchAI/: 7 specs, 2 founding documents, 2 papers, 2 brand guides,
1 campaign spec, 11 telos declarations, 2 research files, 1 app,
1 explorer, 3 reviews, 2 review responses, and 1 ditch walk report.
Four parallel extraction agents plus manual audit. ~200 terms total.*

*Review-coined terms included where accepted in
REVIEW-RESPONSES-2026-09-17.md. Attack patterns included as reference
even where not yet formally addressed -- they define the adversarial
design space the v0.2 specs must survive.*

*Draft. Not ratified. Update when decisions land.*
