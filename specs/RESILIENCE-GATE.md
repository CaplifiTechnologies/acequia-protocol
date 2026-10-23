# Resilience Gate
## Acequia Protocol -- Infrastructure Continuity Spec v0.1

> **A headgate that only works when the grid is on is not a headgate. It
> is a vendor dependency with a nice name.**

---

### Origin: Gary, Indiana -- August 2026

On August 11, 2026, a derecho with straight-line winds up to 99 mph struck
Northwest Indiana. Gary was the hardest hit. Over 63,500 residents lost
power. Full restoration did not come until August 25-26 -- fourteen days
later.

Gary operates a Real Time Crime Center (RTCC) integrating live
surveillance cameras, license plate readers (Flock-pattern), Computer
Aided Dispatch, and Raven shot-detection sensors. The city completed a
four-year DOJ National Public Safety Partnership and received over
$1 million in federal funding for Operation Safe Zone surveillance
expansion.

Every one of those systems is grid-dependent and vendor-cloud-dependent.
When the derecho hit, the community lost all of it -- during exactly the
kind of crisis the systems were sold to handle. For fourteen days, a city
that had invested heavily in networked public safety technology had
neither the technology nor the power to run it.

Compounding factors:

- A NIPSCO utility vehicle was fired upon on August 15, halting repair
  crews temporarily
- Schools closed, businesses shuttered, fuel shortages hit gas stations
- Residents described conditions as "survival mode"
- The slow restoration disproportionately affected a majority-Black city,
  raising equity dimensions alongside the infrastructure ones

The community had no governance over restoration priority. That was
NIPSCO's call -- a private utility company with no contractual obligation
to prioritize public safety infrastructure. The city council that
approved the surveillance expansion had no mechanism to demand that
the RTCC come back online before other loads.

Then, on August 28 -- three days after power was nominally restored --
nine officers (six Gary PD, three Lake County Sheriff's deputies) shot
and killed Kenneth Williams Sr., a 67-year-old Black Army and National
Guard veteran working as an armed security guard at the Gary Metro
Center transit station. At least 100 evidence markers were placed at
the scene. The metro station's surveillance cameras were reportedly
not working.

The accountability infrastructure -- the cameras, the RTCC, the
systems sold to the community as public safety tools -- was still
dark. The community's ability to see what happened to one of its own
was offline.

Reports indicate that during the same period, aerial surveillance
platforms -- including DRT boxes (dirtboxes), aircraft-mounted IMSI
catchers that mimic cell towers to intercept cell phone data from
every device in range -- were operating over Gary. If confirmed, this
is the inversion the headgate exists to prevent: the surveillance
that serves community accountability was down, while the surveillance
that serves state power was up. The cameras that would have recorded
what happened to Kenneth Williams were not working. The systems that
intercepted every resident's cell phone data during a crisis -- without
warrant, without community authorization, without audit -- were working
fine.

This is not a resilience problem. This is a governance inversion. The
infrastructure the community paid for and was told would protect them
failed. The infrastructure the community never authorized and cannot
audit continued operating. The headgate was absent from both.

Gary's situation is not exceptional. It is the baseline. Every city
with vendor-controlled, grid-dependent public safety data infrastructure
faces the same single point of failure. The derecho revealed the
fragility. The Williams killing revealed what fills the gap when the
community's tools go dark and the state's tools do not.

---

### The Failure the Existing Spec Does Not Cover

The Acequia Protocol's existing specifications govern:

- **Who accesses data** (Sovereignty Gate -- authorization scope, not
  identity)
- **How the community decides** (Community Decision -- proposal, pruning,
  voting, degradation tiers)
- **Where data lives** (Founding Document -- civic custody, the library,
  appurtenance)

None of them address **what happens when the infrastructure fails**.

The Founding Document says the data lives at the library, not the
vendor's cloud. The Sovereignty Gate says every access is authorized and
audited. But neither specifies what happens when the building has no
power, the network is down, and the sensors are dark.

The Gary case proves this is not an edge case. It is the most important
case. A headgate that cannot operate during a crisis is a headgate that
fails precisely when the community needs governance most.

The resilience gate fills this gap: infrastructure continuity
requirements for any conforming Acequia Protocol deployment.

---

### Five Layers Where the Headgate Must Hold

#### Layer 1: Collection Continuity

The headgate sits between collection infrastructure (cameras, sensors,
shot detection) and the data pipeline. If the headgate is cloud-dependent,
it fails when the cloud is unreachable. If it is grid-dependent, it fails
when the grid is down.

**Conforming requirement:** A conforming headgate deployment must be
capable of reduced-scope operation for a minimum of 72 hours without
external power or network connectivity.

This means:

- **Local-first storage.** The civic custody node (library server, civic
  data center) must have battery or solar backup sufficient to continue
  recording to local storage. It does not need to run the full analytics
  stack. It needs to continue writing the append-only audit ledger and
  accepting sensor data that reaches it.

- **Graceful degradation, not binary failure.** A grid outage should
  reduce capability, not eliminate it. Priority sensors (those covering
  critical infrastructure, emergency routes, hospital zones) should have
  independent power. Non-priority sensors go dark first. The community
  decides the priority map in advance -- not during the crisis.

- **No silent failure.** When a sensor goes dark, the headgate records
  the gap. An append-only ledger that shows "no data from camera 14
  between 2026-08-11T14:23 and 2026-08-25T09:41" is more honest than
  a system that simply has no record for that period. The gap itself
  is data. Missingness is measured, not assumed.

#### Layer 2: Custody During Crisis

When vendor cloud goes dark, where does the data go?

In the Gary model (the vendor model): nowhere. The RTCC's cloud
dependencies mean that data collection, storage, query, and audit all
stop simultaneously. The data that existed before the outage is on the
vendor's servers, inaccessible to the community. The data that should
have been collected during the crisis does not exist.

In the Acequia model: civic custody means local-first. The civic node
continues to operate at reduced capacity. Data that was collected before
the outage remains physically present in the community. Data collected
during the outage -- even at reduced scope -- is recorded locally and
syncs upstream when connectivity returns.

**Conforming requirement:** A conforming deployment must never have a
state where community data exists only on vendor infrastructure. The
civic custody node is the primary store. Vendor cloud, if used, is a
replica -- never the sole copy.

This inverts the current architecture. In the vendor model, the
community's data is a copy of what the vendor holds. In the Acequia
model, the vendor's data is a copy of what the community holds. The
difference is not technical -- it is custodial. Who has the original
determines who has the authority.

#### Layer 3: Governed Restoration Priority

Who decides which public safety infrastructure gets restored first?

In Gary, NIPSCO made that call. A private utility with shareholders
and service territory obligations, not a public safety mission. The
community had no mechanism to say "the RTCC before the strip mall"
or "the hospital zone cameras before the commercial corridor."

**Conforming requirement:** A conforming deployment must include a
pre-negotiated restoration priority agreement between the community,
the utility, and any relevant emergency management authority.

The Community Decision Protocol already handles this. Before the crisis:

1. The community votes on a **priority map** -- which public safety
   infrastructure gets restored first. This is an action-type proposal
   with real consequences.
2. The result is a tiered list: Tier 1 (restore within 4 hours of any
   crew availability), Tier 2 (restore within 24 hours), Tier 3 (restore
   with general grid).
3. The priority map is a public record, negotiated with the utility as
   part of the community's franchise agreement or emergency management
   plan.

This does not give the community operational control of the utility. It
gives the community a documented, voted-on, pre-negotiated position on
what matters most. When the crisis comes, the priority map is already
decided -- not improvised.

**The equity dimension.** Gary's restoration timeline raised documented
concerns about disproportionate impact on a majority-Black community.
The Sovereignty Gate principle -- default protects the person with least
leverage -- applies here directly. A community with less political power
to pressure the utility needs the priority map more, not less. The
protocol makes the restoration priority a pre-decided community choice
rather than a post-crisis political negotiation where leverage
determines who gets power back first.

#### Layer 4: Vendor Dependency as Single Point of Failure

Gary's RTCC integrates Flock (vendor), Raven (vendor), and CAD
(vendor-hosted). Each of these is a separate vendor relationship with
separate terms, separate cloud infrastructure, and separate failure
modes. When the grid fails, the community discovers that it does not
own its public safety infrastructure -- it rents it.

The vendor has no contractual obligation to maintain service during a
grid failure. The vendor's cloud may be up (it is in another state),
but the community's access point is down. The vendor has no obligation
to provide local failover. The vendor's business model depends on the
community's data flowing through the vendor's infrastructure -- local
failover undermines that dependency.

**Conforming requirement:** A conforming Acequia deployment must not
have any single vendor whose failure eliminates more than one public
safety capability.

This means:

- **No vendor lock across capabilities.** If one vendor provides cameras
  AND shot detection AND LPR AND dispatch, that vendor is a single point
  of failure for the entire public safety data stack. A conforming
  deployment separates vendors across capabilities, or requires that the
  civic node can independently operate any capability whose vendor is
  unreachable.

- **Open interface at the headgate.** The headgate's ingest interface
  must accept data from any conforming sensor, not only from a specific
  vendor's hardware. This is the interoperability requirement that
  prevents vendor lock-in from becoming infrastructure fragility.

- **Vendor replaceability without data loss.** Per the Founding Document:
  mayordomo operators are auditable, fireable, and replaceable. If firing
  the vendor means losing the data, the community is captive. Civic
  custody ensures the data survives vendor change.

#### Layer 5: Crisis Governance Mode

Normal governance (Community Decision Protocol) assumes infrastructure
is functioning. Proposals, pruning, voting, and degradation tiers
require a working system. What governs when the system itself is down?

**Conforming requirement:** A conforming deployment must define a crisis
governance mode that operates without digital infrastructure.

Crisis governance mode:

- **Pre-decided authority delegation.** The community votes (before the
  crisis) on who holds emergency authority over the headgate when the
  system is down. This is the mayordomo's crisis role: maintain the
  ditch during the flood.

- **Paper fallback for audit.** When the digital audit ledger is
  unavailable, access to community data (if any systems are functioning
  on backup power) is recorded on paper. The paper record is ingested
  into the append-only ledger when the system comes back. The gap in the
  digital record is bridged, not ignored.

- **Automatic scope reduction.** In crisis mode, the headgate
  automatically narrows authorized access to emergency-only queries.
  Bulk access, analytics, and federation are suspended. This is the
  data equivalent of water rationing during drought -- the repartimiento.
  Everyone's allocation shrinks proportionally. No one gets bulk access
  during a crisis just because the oversight systems are down.

- **Community debrief after restoration.** When the system comes back
  online, a mandatory debrief proposal is generated. What happened?
  What data was collected during the crisis? What access was granted
  under emergency authority? The community sees the full record and
  votes on whether the emergency governance was appropriate. This is
  not a rubber stamp -- it is accountability for crisis decisions.

#### Layer 6: The Inverted Headgate -- Ungoverned Surveillance During Governed Silence

This is the layer the Gary case makes unavoidable.

When the derecho knocked out Gary's grid, the community's accountability
infrastructure went dark: cameras offline, RTCC offline, audit logs
offline. But aerial surveillance -- DRT boxes (dirtboxes), IMSI catchers
mounted on aircraft that mimic cell towers to intercept cell phone
communications from every device in range -- does not depend on the
municipal grid. It depends on an aircraft, a generator, and a federal or
state agency with no obligation to tell the community it is operating.

The result is a governance inversion:

| Infrastructure | Grid-dependent? | Community-authorized? | Auditable by community? | Operational during outage? |
| --- | --- | --- | --- | --- |
| RTCC cameras | Yes | Yes (council approved) | Partially (vendor-controlled logs) | No |
| LPR / Flock | Yes | Yes (council approved) | No (vendor-controlled) | No |
| Shot detection | Yes | Yes (council approved) | No (vendor-controlled) | No |
| Body cameras | Yes (charging) | Yes (policy-mandated) | Partially (department-controlled) | Degraded |
| Dirtbox / IMSI catcher | No (aircraft-powered) | No (no community vote) | No (classified program) | Yes |

Everything the community authorized and paid for went offline.
Everything the community never authorized and cannot audit stayed
operational. The headgate was absent from both directions: the
community could not keep its own tools running, and it could not
close the gate on tools it never opened.

Kenneth Williams was killed on August 28. The metro station cameras
were not working. If aerial IMSI catchers were operating, every
cell phone at the scene -- every witness, every bystander, every
family member -- was intercepted. The community has no audit log
for either system: the cameras that should have recorded the killing
were dark, and the cell-site simulators that may have intercepted the
witnesses operate without community knowledge or consent.

**Conforming requirement:** A conforming Acequia Protocol deployment
must address ungoverned surveillance operating in the community's
airspace, not only governed surveillance operating on the community's
infrastructure.

This means:

- **The headgate governs ingress, not only egress.** The existing spec
  treats the headgate as a gate on outbound data flow: who accesses
  community data, under what authorization. The inverted headgate
  problem shows that the community also needs governance over inbound
  surveillance -- data being collected FROM the community by systems
  the community did not authorize.

- **Transparency ordinance as a protocol requirement.** A conforming
  deployment should include (or advocate for) a local ordinance
  requiring disclosure of any surveillance technology operating within
  the municipality's jurisdiction, including federal and state
  deployments. This is modeled on the Community Control Over Police
  Surveillance (CCOPS) ordinances already enacted in cities including
  Oakland, Nashville, and Cambridge. The protocol does not enforce the
  ordinance -- it makes the ordinance a conformance condition.

- **Airspace surveillance disclosure in the audit ledger.** When the
  community becomes aware of aerial surveillance operations (via ADS-B
  tracking, FAA records, FOIA, whistleblower, or disclosure ordinance),
  the event is recorded in the community's audit ledger. The community
  may not be able to prevent the surveillance, but it can document that
  it occurred, that it was not authorized, and that the community's
  position is on the record.

- **Crisis-period surveillance accounting.** The post-crisis debrief
  (Layer 5) must include a question: was any surveillance technology
  operated in the community during the outage that was not part of the
  community's governed infrastructure? If yes, the community records
  the gap between what it authorized and what was deployed. This is
  the data equivalent of discovering that someone else's pipe is
  tapping the ditch upstream -- you cannot always stop it immediately,
  but you measure it and you put it on the record.

**The Williams test.** A conforming deployment must be able to answer,
after any use-of-force incident:

1. Was community-authorized surveillance operational at the scene?
   If not, why not, and when was the community notified of the gap?
2. Was any non-community-authorized surveillance operational at the
   scene? If so, what data was collected, by whom, under what
   authority, and was the community notified?
3. Is there an unbroken audit trail from the incident to the
   community's review?

If the answer to all three is "we don't know" -- as it currently is
in the Williams case -- the headgate was absent. Not broken. Absent.
The community had no gate to open or close because no gate existed.

---

### The Derecho Test

A conforming Acequia Protocol deployment must pass the **Derecho Test**:

> A sustained grid outage of 14 days, affecting 100% of municipal
> infrastructure, with no advance warning and no guaranteed restoration
> timeline.

Passing means:

1. **The civic custody node operates** (at reduced capacity) for at
   least 72 hours on backup power.
2. **Community data remains in civic custody** throughout the outage.
   No data exists only on vendor infrastructure.
3. **The audit ledger has no undocumented gaps.** Gaps are recorded as
   gaps. Missingness is measured.
4. **Emergency access is scoped and recorded.** Any data access during
   the outage is logged (paper if necessary) and ingested into the
   permanent record.
5. **Restoration priority was pre-decided** by community vote, not
   improvised by the utility or emergency management.
6. **No single vendor failure eliminated more than one capability.**
7. **Ungoverned surveillance is documented.** Any non-community-
   authorized surveillance that operated during the outage is recorded
   in the audit ledger, with whatever detail is available.
8. **A community debrief occurred** within 30 days of restoration,
   including the Williams test for any use-of-force incidents during
   the outage period.

A deployment that fails the Derecho Test is not conforming, regardless
of how well it governs data flow under normal conditions. The headgate
that works on sunny days and fails in storms is not a headgate.

---

### Relation to Existing Specs

| Spec | Resilience Gate extension |
| --- | --- |
| Sovereignty Gate | Default-closed applies in crisis: scope narrows to emergency-only. Override remains with rights-holder (the community), not the vendor or the utility. Ingress governance (Layer 6) extends the gate in both directions. |
| Community Decision | Crisis governance authority is a pre-decided community vote. Post-crisis debrief is a mandatory proposal. Priority maps and transparency ordinances use the standard protocol. |
| Founding Document | Civic custody is not just where data lives -- it is where data survives. The library (or civic node) must have backup power. The mayordomo has a crisis role. |
| Headgate Papers | Gary is the case study. The three questions (who owns, can we audit, can we close) extend to five: **can we survive?** and **what watches when we can't?** |

---

### The Fourth and Fifth Questions

The Headgate Papers propose three questions for any city council
considering a surveillance vendor contract:

1. Who owns the data after collection?
2. Can the community audit access?
3. Can the community close the headgate?

The Resilience Gate adds two more:

**4. Does the system survive when the grid doesn't?**

If the answer is no -- if a two-week power outage eliminates 100% of
the community's public safety data infrastructure -- the system is not
resilient enough to be trusted with the community's safety. The
community did not invest in public safety infrastructure. It invested in
fair-weather infrastructure that fails when safety matters most.

Gary's Real Time Crime Center cost over a million dollars in federal
funding. It survived zero days of the derecho. The cameras became
expensive decorations. The shot detection became silence. The license
plate readers became blind. The dispatch system became a phone and a
prayer.

**5. What surveillance operates when yours doesn't?**

This is the question Gary forces. When the community's cameras went
dark, what kept watching? When the community's audit logs stopped
recording, what kept collecting? The headgate governs what the community
authorized. But when the community's infrastructure fails, the systems
that operate in its absence are the ones with no headgate at all.

A dirtbox flying over a blacked-out city is the purest form of
ungoverned surveillance: no community authorization, no warrant, no
audit trail, no retention policy, no federation agreement, no oversight
mechanism of any kind. It collects from every cell phone in range --
not a targeted query against a specific suspect, but a bulk intercept
of an entire population during a crisis.

If a city council cannot answer question five, the council does not
know what is happening in its own airspace. The headgate cannot govern
what the community cannot see. Making it visible is the first step.
The Acequia Protocol does not claim the community can close every gate.
It claims the community deserves to know every gate exists.

---

### Implementation Notes

**This spec does not require every sensor to have backup power.** It
requires that the civic custody node -- the place where data lives and
the headgate operates -- can survive a grid outage. Sensors will go dark.
That is expected. What is not acceptable is that the headgate itself goes
dark, losing custody of existing data and the ability to record the gap.

**72 hours is a minimum, not a target.** Gary's outage lasted 14 days.
A conforming deployment should plan for longer. The 72-hour floor exists
because any shorter interval fails the most common disaster scenarios
(major storms, earthquakes, wildfire-related shutoffs). Communities in
high-risk areas should set their own floors higher.

**Battery/solar for a server room is not expensive relative to the
surveillance infrastructure it protects.** A municipal RTCC costs
hundreds of thousands to millions in hardware, software, and federal
grants. A UPS system with solar supplementation for a library server
room costs a fraction of that. The resilience gap is not a funding gap.
It is a priorities gap. The vendor sells cameras. Nobody sells
continuity. The protocol makes continuity a requirement.

**The priority map is the most actionable item.** A community can adopt
a priority map today, before adopting the full Acequia Protocol, by
negotiating with its utility during franchise renewal or emergency
management planning. This is the thin end of the wedge: a community
that starts by governing its own restoration priority has already begun
governing its own infrastructure.

---

*Ditch AI specs. Draft 2026-09-13. Not ratified.*
*The headgate must outlast the storm.*
