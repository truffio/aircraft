# Requirements Engineering Methodology for a Simple Aircraft

Oct 24, 2026 · @Martin

> **Project tailoring (current phase): failures and hazards deferred.**
> The project adopts this methodology except for hazard and failure analysis, which is set aside for now. Until it is reinstated:
>
> - **Section 3, step 3 (Analyse hazards)** is skipped; the cycle runs steps 1, 2, 4–8.
> - **Section 6 (Hazard and failure analysis)** is not applied. No severity classes are assigned, and rigour is not scaled by criticality.
> - **Section 9.2:** the *Criticality* attribute is left as "Not assessed", and the *Safety (failure handling)* requirement type is not used.
> - **Section 10.2:** robustness and injected-failure test cases tied to Hazardous or Catastrophic items are not required.
> - **Section 10.4:** the requirement → hazard-analysis row trace link is not used.
> - **Failure-related content elsewhere** (effector-failure scenarios and annunciations, failure injection in F-STP-02, fault-injection requirements, the hazard-related checklist items in 13.1 and 13.2) is deferred.
>
> Embedded diagrams from the source document were not carried over; their placeholders are kept below.

## 1. Purpose and scope

This document defines how the team will capture, write, decompose, validate and verify the requirements of the **Aeronef**, a fictitious six-degree-of-freedom vehicle built as a platform for flight-control laws, autoflight, simulation, automated testing and reverse engineering. It combines the development process of SAE ARP4754B and the requirements-based approach of DO-178C with the writing rules of INCOSE, EARS and ISO/IEC/IEEE 29148, scaled down for a small team whose product is a simulated vehicle and its control software.

Use it in two ways. Sections 3 to 7, 10 and 11 describe the **process**: what to do, in what order, and what each step produces. Sections 8 and 9 describe the **craft**: how to write a single requirement that is clear, verifiable and traceable. Sections 12 and 13 give a worked example and checklists the team can copy.

**What makes the Aeronef different.** It will not be certified and it does not physically fly: the deliverables are models, control software and tests. Its requirements therefore cover three things: the **physics** the simulation must reproduce (6-DOF rigid body, gravity, drag, mass that decreases as fuel burns), the **vehicle functions** (fixed-direction force effectors, fuel, flight control, autoflight), and the **test and simulation infrastructure** that proves them. Many values are still open (axis conventions, drag model, inertias, effector limits, autoflight modes); the method records them as TBD or TBR placeholders instead of letting them block the work.

**Out of scope.** Airworthiness certification, realistic force-emitter physics, electrical and ancillary systems, and detailed pilot controls and displays, as excluded by the concept summary. Certification-oriented standards are borrowed for their process discipline only, not as a compliance target.

## 2. Foundations

The method borrows from ten public frameworks; none is imposed whole. ARP4754B supplies the lifecycle skeleton, INCOSE and EARS supply the writing rules, DO-178C supplies requirements-based testing, and NASA-STD-7009 covers what is special about a simulated vehicle.

| Source | What it contributes | How the Aeronef project uses it |
| --- | --- | --- |
| [SAE ARP4754B](https://saemobilus.sae.org/content/ARP4754B) (Dec 2023) | Development lifecycle for aircraft and systems: requirement capture, validation, verification, derived requirements, link to safety | Lifecycle skeleton and level-by-level flow; no development assurance levels |
| [SAE ARP4761A](https://saemobilus.sae.org/content/ARP4761A) (Dec 2023) | Safety assessment: functional hazard assessment, preliminary and final system safety assessments | Lightweight hazard analysis that produces failure-handling requirements and fault-injection tests |
| [ISO/IEC/IEEE 29148:2018](https://store.sfs.fi/en/ieee-29148-2018) | Requirements processes, the construct of a good requirement, attributes, required documents | Document set and the needs-to-requirements transformation |
| [INCOSE Guide to Writing Requirements v4](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf) (Jun 2023) | 15 characteristics, 42 writing rules and a catalogue of attributes | The project's writing standard and review checklist |
| [EARS](https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax) (Mavin, Rolls-Royce, 2009) | Five sentence patterns keyed on While, When, Where and If/Then | Default syntax, especially for autoflight mode logic and failure handling |
| [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) (SP-2016-6105 Rev 2) | Requirement flow-down, shall/will/should conventions, rationale, TBD/TBR handling, verification matrix, ConOps outline | Process details, checklists and templates |
| DO-178C with DO-331 (model-based supplement) | High-level and low-level software requirements, derived requirements, requirements-based testing and coverage analysis | Control-law and autoflight software; automated tests generated from requirements |
| [NASA-STD-7009B](https://standards.nasa.gov/node/263) (Mar 2024) | Credibility of models and simulations: verification, validation, input pedigree, uncertainty | Requirements and evidence for the simulation and the dynamics model |
| AIAA R-004-1992 and SAWE STD A-6 (2023) | Standard flight-vehicle coordinate systems and mass-properties reporting | Axis and sign conventions fixed before any dynamics requirement is written |
| IEEE 1028 | Review types: walkthrough, technical review, inspection, audit | Peer-review process for every artifact |

The certification standards are used for **process discipline**, not compliance: the Aeronef has no certification authority, so the team decides how much rigour each requirement deserves (Section 6).

## 3. The process: a recursive, level-by-level flow

Requirements are developed top-down through a hierarchy whose depth varies by element, and verified bottom-up against the same hierarchy. The same eight-step cycle is applied at every level; each level's validated, baselined output becomes the parent input of the level below.

| Level | Scope | Typical artifact | Subject of the requirements |
| --- | --- | --- | --- |
| L0 | Mission and project objectives, constraints, success criteria | Concept of Operations; L0 Requirements Document | The Aeronef project |
| L1 | Major system elements and their responsibilities: the **Aeronef**, the **Simulation and Testing Platform** (STP) and the **Reverse-Engineering Effort** (REE) | One System Requirements Specification per element; interface control documents between elements | Each element |
| L2 | Subsystems of each element, for example the Aeronef's dynamics model, effectors, fuel and mass, flight control and autoflight | Subsystem specifications; model specification | Each subsystem |
| L3 to Ln | Subfunctions and items: axis controllers, control allocation, mode logic, guidance laws, test harness components; software high- and low-level requirements | Item specifications; software requirements | Each item or software component |

**Depth is decided per branch.** Stop decomposing a branch when a requirement can be implemented and verified by a single owner without further interpretation. Autoflight will likely need four or five levels; the REE may need only two.

&#91;embedded content: Aeronef requirement hierarchy · L0 to L4, depth varies by element\]

The Aeronef branch runs to L4 through autoflight software, while the reverse-engineering branch is complete at L2.

**The cycle at each level**

1. **Understand the parent.** Read the parent requirements, the ConOps and the open TBDs; confirm the boundary of the element.
2. **Analyse functions.** List what the element must do and how functions exchange data (Section 5).
3. **Analyse hazards.** Identify failure conditions and the behaviour required when they occur (Section 6).
4. **Architect and allocate.** Choose a logical architecture, allocate functions and budgets to children, define interfaces (Section 7).
5. **Write the child requirements** with the rules in Section 8 and the attributes in Section 9.
6. **Validate.** Check that the children are necessary and together sufficient to satisfy each parent (Section 10).
7. **Plan verification.** Assign a method and a procedure to every requirement before it is baselined (Section 10).
8. **Peer review and baseline.** Review, resolve findings, place under configuration control (Section 11).

The cycle is iterative, not a waterfall. Design work at L3 often exposes a missing or infeasible L2 requirement; it is fixed at L2 through a change request, never silently in the child.

## 4. Step 1 — L0: stakeholders, mission and concept of operations

L0 turns the project's purpose into a small, agreed set of objectives, constraints and success criteria; every other requirement must trace back to one of them. Write L0 before any vehicle requirement, and keep it short: ten to twenty statements is typical.

**4.1 Identify stakeholders and their needs.** List everyone who will use, build, test, review or consume the project's outputs, then record each one's needs in their own words before translating them.

| Stakeholder | Interest | Example need (stakeholder's words) |
| --- | --- | --- |
| Control-law designers | Develop and compare several control-law designs | "We need to swap controllers without touching the vehicle model." |
| Autoflight designers | Airliner-inspired modes adapted to 6-DOF | "We need modes that a crew can understand from annunciations alone." |
| Simulation and test engineers | Repeatable, automated verification | "Every requirement should have a test that runs unattended." |
| Reverse-engineering team | Evidence to reconstruct design and requirements | "We need manuals and logs written for people, not for us." |
| Crew (simulated or human-in-the-loop) | Monitor and command the vehicle | "I need to know which mode is active and what it will do next." |
| Peer reviewers | Judge each artifact | "Each requirement must say why it exists." |

**4.2 Write the concept of operations (ConOps).** The ConOps describes how the Aeronef and its platform are used, from the operator's point of view, through scenarios. Use the NASA Appendix S outline, trimmed. Useful first scenarios: hold position and attitude; translate to a waypoint at constant attitude; rotate in place; fly a reference mission until fuel exhaustion; handle an effector failure; run a regression test campaign overnight; hand a document package to the reverse-engineering team. Operational statements such as "the crew selects Position Hold" belong in the ConOps and the manuals, not in product requirements.

**4.3 Transform needs into L0 requirements.** Each L0 statement names the project as subject and states an objective, a constraint or a success criterion. Illustrative examples:

- **L0-OBJ-001** — The Aeronef project shall provide a simulated six-degree-of-freedom vehicle on which multiple flight-control-law designs can be implemented and compared.
- **L0-OBJ-002** — The Aeronef project shall develop autoflight functions, derived from airliner autoflight concepts, as the primary method of operating the vehicle.
- **L0-OBJ-003** — The Aeronef project shall verify each baselined requirement through automated, repeatable procedures where the verification method is test.
- **L0-OBJ-004** — The Aeronef project shall produce human-oriented operational manuals and procedures sufficient for a separate team to reconstruct the vehicle's functions and requirements.
- **L0-CON-001** — The Aeronef project shall exclude aerodynamic lift and aerodynamic control surfaces from the vehicle model.
- **L0-CON-002** — The Aeronef project shall treat the vehicle centre of gravity as fixed in the body frame.

**4.4 Record constraints, assumptions and success criteria.** The simplifications in the concept summary (no lift, fixed centre of gravity, no electrical system, fictional effectors) are **constraints**, written as requirements with type Constraint so they can be traced and challenged. Assumptions (for example, perfect knowledge of vehicle state in the first version) are listed separately with an owner, and confirmed or turned into requirements before L1 is baselined. Success criteria state what "done" means for each objective, so L0 itself can be validated at the end.

## 5. Step 2 — Functional analysis

Before writing L1 and L2 requirements, list the functions each element must perform and the data each function exchanges; requirements are then written against functions, not against an imagined design. Functions are verbs ("propagate motion"), not boxes ("the physics engine").

**Techniques.** A function list with inputs and outputs is enough at L1. Add a functional flow diagram for the control loop, an N-squared (N²) matrix for interfaces between functions, and a state-transition diagram for autoflight modes (NASA Handbook Appendix F covers functional, timing and state analysis).

| ID | Element | Function | Main inputs → outputs |
| --- | --- | --- | --- |
| F-AER-01 | Aeronef | Generate commanded forces and moments with the fixed-direction effectors | Effector commands → body forces, body moments |
| F-AER-02 | Aeronef | Consume fuel and update vehicle mass | Effector output → fuel flow, mass, inertia |
| F-AER-03 | Aeronef | Propagate six-degree-of-freedom rigid-body motion under effector forces, gravity and drag | Forces, moments, mass, inertia → position, velocity, attitude, angular rate |
| F-AER-04 | Aeronef | Provide vehicle state to the control functions | Simulated state → state vector (perfect knowledge assumed, TBR) |
| F-AER-05 | Aeronef | Regulate each translational and rotational axis independently | Axis references, state → axis force and moment demands |
| F-AER-06 | Aeronef | Allocate axis demands to individual effectors | Axis demands, effector limits → effector commands |
| F-AER-07 | Aeronef | Guide the vehicle according to the active autoflight mode | Mode, targets, state → axis references |
| F-AER-08 | Aeronef | Manage autoflight mode engagement, transitions and annunciation | Crew selections, state, failures → active mode, annunciations |
| F-STP-01 | Simulation and Testing Platform | Execute the simulation at a fixed step, in real time or faster | Initial conditions, parameters → time histories |
| F-STP-02 | Simulation and Testing Platform | Inject scenarios, disturbances and failures | Test script → injected events |
| F-STP-03 | Simulation and Testing Platform | Run requirement-tagged tests unattended and report pass or fail | Test procedures → results, coverage report |
| F-STP-04 | Simulation and Testing Platform | Record and archive data | Simulation outputs → logs |
| F-REE-01 | Reverse-Engineering Effort | Collect evidence: manuals, procedures, logs, observed behaviour | Released evidence package → evidence register |
| F-REE-02 | Reverse-Engineering Effort | Reconstruct functions, requirements and models | Evidence → reconstructed specification |
| F-REE-03 | Reverse-Engineering Effort | Compare the reconstruction with the baseline and report gaps | Reconstruction, baseline → gap report |

The flight-control and autoflight functions (F-AER-05 to F-AER-08) are where most requirements will live; the diagram below shows how they close the loop around the vehicle physics.

&#91;embedded content: Aeronef control loop · 7 functions, 1 feedback path\]

Every arrow is an interface that needs an ICD entry and interface requirements on both sides; the dynamics box is where the physics requirements and the model specification live.

## 6. Step 3 — Hazard and failure analysis

Even a simulated vehicle needs a hazard analysis, because failure handling is a large share of real control-law and autoflight requirements. Use a lightweight version of the ARP4761A functional hazard assessment: for each function, ask how it can fail, what happens to the vehicle, and what the system must do about it.

**Severity classes (adapted).** In a simulation, "catastrophic" means loss of control or the vehicle leaving its defined operating volume. The classes keep the ARP4761A names so the method transfers to real projects: Catastrophic, Hazardous, Major, Minor, No safety effect.

| Function | Failure condition | Effect on the vehicle | Severity | Requirement it generates |
| --- | --- | --- | --- | --- |
| F-AER-01 Effectors | One effector produces zero output | Loss of authority on one or more axes | Hazardous | Detection, annunciation and reconfigured allocation (If/Then) |
| F-AER-01 Effectors | Commanded force exceeds the effector limit | Saturation, axis coupling, overshoot | Major | Saturation handling in control allocation |
| F-AER-02 Fuel | Fuel reaches zero | All effectors stop; vehicle falls under gravity | Catastrophic | Low-fuel alert and zero-thrust behaviour |
| F-AER-08 Mode logic | Uncommanded mode change | Crew confusion, unexpected trajectory | Hazardous | Mode-transition requirements and annunciation |
| F-AER-04 State | State data invalid (later versions) | Controller acts on wrong information | Catastrophic | Validity monitoring and safe-mode behaviour |
| F-STP-01 Simulation | Numerical integration diverges | False test results | Major | Integration accuracy and divergence detection |

**What the analysis produces.** Three kinds of requirements: unwanted-behaviour requirements in the EARS If/Then pattern; monitoring and annunciation requirements; and fault-injection requirements on the STP so each failure condition can be tested.

**Rigour by criticality instead of development assurance levels.** Record a Criticality attribute on each requirement from the worst severity it protects against. Use it to scale effort: requirements linked to Catastrophic or Hazardous conditions get an independent reviewer, robustness tests at limits and out of range, and full trace to a failure scenario; Minor ones need only a nominal test.

## 7. Step 4 — Decompose, allocate and derive

Each parent requirement is satisfied by a set of child requirements allocated to the next level's elements; children that come from design decisions rather than from a parent are marked as derived and sent back up for review.

**Allocated versus derived.**

- An **allocated** requirement flows from a parent: "hold position within 1 m" splits into a guidance requirement, a translational-control accuracy requirement and an effector authority requirement.
- A **derived** requirement arises from an architecture or design choice and has no direct parent, for example the priority rule used by control allocation when effectors saturate. DO-178C and ARP4754B both require derived requirements to be visible: record the design decision that created them in the rationale and have them reviewed at the parent level and by the hazard analysis.

**Rules for a sound decomposition.**

1. Every child traces to at least one parent, or is flagged Derived with its rationale.
2. Every parent is fully covered: the rationale states why satisfying all children satisfies the parent. This sufficiency argument is the core of requirement validation.
3. Children are written at the right level: a child restates the parent's intent for its own element, with more detail, never a copy of the parent.
4. Quantities are split with **budgets**. Allocate fuel, effector authority, position error and timing (simulation frame time, controller latency) between children, and track margins.

**Interfaces.** Write interface requirements wherever two elements exchange data, and detail the data in an interface control document (ICD). Three ICDs are needed early: Aeronef model ↔ STP (state vector, effector commands, frame rate, units); flight control ↔ autoflight (axis references, mode status); and Aeronef and STP ↔ REE (the evidence package: which manuals, logs and behaviours are released).

**Parameters belong in a controlled table, not in sentences.** The concept summary leaves inertias, drag coefficients, effector limits and fuel-consumption rates configurable. Keep them in a version-controlled parameter database with IDs, units, values and status, and let requirements reference them, for example "within \[P-AF-012\] metres". A parameter change then becomes a reviewed change, with every affected requirement found through the reference.

**For a simulation, the physics is the requirement.** The equations of motion, axis conventions, gravity model and drag model are what the Aeronef must reproduce. Write them in a model specification (INCOSE rule R23: refer to a supporting model) and let short requirements point to it, so the equations are verified by analysis and test like any other requirement.

**Unknowns.** Use TBD when no value exists and TBR when a best estimate exists but needs confirmation. Each carries an owner and a closure date, and the list is reviewed at every baseline.

## 8. How to write a good requirement

A good requirement is one sentence, with one responsible subject, one "shall", one measurable result and any condition stated explicitly; it says **what** is needed and leaves **how** to the design.

**8.1 Anatomy.** `[Condition] the <subject> shall <action> <object> <performance with tolerance>.` The subject is the element at the current level (the Aeronef, the autoflight system, the STP), never a person: "the crew shall..." is an operating procedure and belongs in a manual.

**8.2 Keywords.** Following the NASA convention: **shall** states a requirement (verified); **will** states a fact or declaration of purpose (not verified); **should** states a goal (not verified). Avoid "must" and "may" in requirement statements.

**8.3 Use the EARS patterns.** Every requirement fits one of five patterns or a combination. The examples are illustrative; bracketed IDs refer to the parameter table.

| Pattern | Template | Aeronef example |
| --- | --- | --- |
| Ubiquitous (always active) | The \<system> shall \<response> | The dynamics model shall compute vehicle mass as dry mass plus remaining fuel mass. |
| Event-driven | When \<trigger>, the \<system> shall \<response> | When Position Hold is engaged, the autoflight system shall capture the current vehicle position as the reference position. |
| State-driven | While \<state>, the \<system> shall \<response> | While Attitude Hold is active, the flight control system shall hold each attitude angle within \[P-FC-004\] degrees of its reference. |
| Optional feature | Where \<feature is included>, the \<system> shall \<response> | Where the manual control option is installed, the flight control system shall accept six-axis rate commands from the crew input device. |
| Unwanted behaviour | If \<undesired event>, then the \<system> shall \<response> | If remaining fuel mass reaches zero, then the effector system shall produce zero force and zero moment. |
| Complex | While \<state>, when \<trigger>, the \<system> shall \<response> | While the autoflight system is engaged, when an effector failure is detected, the autoflight system shall annunciate the failure within \[P-AF-030\] seconds. |

EARS is weak for requirements with many conditions; express those as a decision table or a state-transition diagram, and write a short requirement that references it. Autoflight mode logic is a typical case.

**8.4 The rules that matter most.** The INCOSE guide has 42 rules; these twelve catch most defects.

1. **Singular:** one thought per statement; avoid "and", "or", "as well as", "unless".
2. **Active voice,** with the responsible element as subject.
3. **Measurable:** a number, a unit and a tolerance or range for every quantity.
4. **No vague terms:** quickly, adequate, appropriate, user-friendly, robust, efficient, sufficient, minimize, maximize, approximately.
5. **No escape clauses:** as far as possible, if necessary, where practicable, as required.
6. **No open-ended lists:** etc., including but not limited to. Enumerate the set.
7. **No unachievable absolutes:** always, never, all, 100 %. Use "each" for universal quantification.
8. **Explicit conditions:** state when the requirement applies (mode, state, phase, fuel state).
9. **Explicit timing:** replace "after", "once", "eventually", "instantaneous" with a stated time or event.
10. **Solution-free:** no design unless constrained on purpose, with the reason in the rationale.
11. **Positive statements:** prefer "shall hold" to "shall not drift"; reserve "shall not" for true prohibitions.
12. **Defined terms only:** every noun is in the project glossary, every unit in SI, every axis per the coordinate-system standard.

**8.5 From bad to good.**

| Weak requirement | Defect | Better requirement |
| --- | --- | --- |
| The flight control system shall respond quickly to commands. | Vague, not measurable | The flight control system shall reach 90 % of a commanded body roll-rate step within \[P-FC-010\] seconds. |
| The vehicle shall be stable and controllable in all modes. | Two thoughts, absolute, vague | Split into one stability-margin requirement and one tracking requirement per mode, each with a measure. |
| The autoflight should hold altitude and heading. | "Should" is a goal; two thoughts; airliner terms that may not apply in 6-DOF | Two "shall" statements, using defined terms such as vertical position and yaw angle. |
| The pitch controller shall be a PID. | Design, not requirement | State the required tracking and margin performance; record PID as a design choice. If comparing control laws is the purpose, write it as a constraint with rationale. |
| Drag shall be modelled appropriately. | Vague, unverifiable | The dynamics model shall compute aerodynamic drag in accordance with model specification MS-DYN, section on drag. |
| Fuel shall not run out during a mission. | Negative, untestable, belongs to operations | When remaining fuel falls below \[P-FU-005\] % of initial fuel, the Aeronef shall annunciate LOW FUEL. |

**8.6 Write the rationale at the same time.** One or two sentences on why the requirement exists, what assumption it rests on and which parent or analysis it comes from. Rationale is what lets a reviewer, a later engineer or the reverse-engineering team judge a requirement without asking its author.

## 9. Requirement attributes, identifiers and verification methods

A requirement is the statement plus its attributes; without rationale, trace and verification method it cannot be reviewed, verified or reverse-engineered. The minimum set below follows the INCOSE starred attributes, trimmed for a small team.

**9.1 Identifiers.** One identifier syntax is used at every level, and the identifier starts with the level, so the level of a requirement can be read from its ID alone (decision D31): `L<n>-<ELEMENT>[-<SUBSYSTEM>[-<ITEM>]]-<NNN>`. For example, `L1-AER-010` is the Aeronef at L1, and `L2-AER-AF-PH-010` is Aeronef, autoflight, Position Hold, number 010, at L2. L0 uses `L0-OBJ-nnn`, `L0-CON-nnn`, `L0-SUC-nnn` and `L0-ASM-nnn`. Because depth varies by branch, the element path after the level prefix shows where the requirement sits in the architecture. Number in steps of 10 to leave room, and never reuse a deleted identifier. A requirement that moves to another level gets a new identifier, and the old one is deleted with a pointer to the new one. The Level attribute must match the prefix.

**9.2 Minimum attributes.**

| Attribute | Content |
| --- | --- |
| ID | Unique, permanent identifier (9.1) |
| Statement | The single "shall" sentence |
| Rationale | Why it exists, assumptions, design decision if derived |
| Level | L0, L1, L2 … Ln |
| Type | Functional, Performance, Interface, Constraint, Safety (failure handling), Model fidelity, Documentation |
| Parent(s) | IDs of parent requirements, or "Derived" |
| Source | ConOps scenario, hazard analysis row, stakeholder need, trade study |
| Allocated to | Child element(s) that implement it |
| Criticality | Worst severity it protects against (Section 6) |
| Verification method | Inspection, Analysis, Demonstration or Test |
| Verification reference | Test procedure or analysis ID and its success criteria |
| Status | Draft, Reviewed, Baselined, Verified, Deleted |
| Owner | Person accountable for the requirement |
| TBD/TBR | Open items with owner and closure date |
| Version | Incremented on each approved change |

**9.3 Verification methods.** Choose the cheapest method that gives adequate confidence, and state success criteria before the work is done.

| Method | Definition | Aeronef example |
| --- | --- | --- |
| Inspection | Examination of an artifact, code or data against the requirement, without running it | Check that every parameter in the model has an SI unit in the parameter table |
| Analysis | Calculation, model or comparison with an independent solution | Compare simulated free fall with drag against the closed-form terminal velocity; check mass decrease against the integral of fuel flow |
| Demonstration | Operating the system to show a qualitative capability, without detailed measurement | Show that a controller can be swapped through configuration without rebuilding the vehicle model |
| Test | Operating the system under controlled conditions and measuring the result against the criteria | Automated STP scenario: engage Position Hold, inject a 0.5 m offset, measure the position error after \[P-AF-014\] seconds |

For the Aeronef, most functional and performance requirements are verified by **automated test** on the STP, and the physics by **analysis against independent solutions**; Inspection covers documentation and coding-standard requirements.

## 10. Validation, verification, traceability and change control

Validation asks "are these the right requirements?" and happens before a baseline; verification asks "does the product meet them?" and happens after implementation. Traceability links both into one auditable chain.

**10.1 Validate requirements before baselining.** ARP4754B keeps traceability and engineering review as the primary validation methods, with analysis, modelling and test added when those are not enough. Apply the NASA six questions to each set: written correctly? technically correct? satisfies the stakeholders? feasible? verifiable? free of redundancy and over-specification? For the Aeronef, early prototype simulations are a cheap way to validate performance numbers before they are baselined.

**10.2 Verify requirements-based, not code-based.** Write each test procedure from the requirement alone, not from the implementation, as DO-178C requires. Include nominal cases, boundaries and robustness cases (out-of-range inputs, injected failures) for Hazardous and Catastrophic items. Run the same tests with code coverage measured: code that no requirement-based test exercises means either a missing requirement or unintended behaviour.

**10.3 Establish simulation credibility.** The STP's results are only evidence if the simulation itself is credible. Following NASA-STD-7009B, verify the model against independent solutions (free fall, terminal velocity, torque-free rotation conserving angular momentum, fuel-mass integral), document input pedigree for every parameter, and quantify sensitivity of key results to uncertain parameters.

**10.4 Maintain bidirectional traceability.** Four link types are mandatory:

- child requirement → parent requirement (or "Derived" with rationale);
- requirement → hazard-analysis row or ConOps scenario that produced it;
- requirement → verification procedure → verification result;
- operational manual section or procedure → requirements it describes (Section 11).

Run automated checks on each build: requirements without a parent, parents without children, requirements without a verification procedure, procedures without a requirement, and requirements whose last result is failed or missing. Tagging each automated test with the IDs it verifies (for example `@verifies L2-AER-AF-PH-010`) lets a script regenerate the requirements verification matrix every night.

| Req ID | Statement (short) | Method | Procedure | Level verified | Result | Status |
| --- | --- | --- | --- | --- | --- | --- |
| L2-AER-AF-PH-010 | Hold position within \[P-AF-012\] m | Test | TP-AF-PH-010 | Aeronef in STP | Pass (example) | Verified |
| L2-AER-DYN-020 | Mass equals dry mass plus fuel | Analysis | AN-DYN-020 | Dynamics model | Pending | Baselined |

**10.5 Baseline and control changes.** Hold a review at each level before baselining: an L0 mission and concept review, a System Requirements Review per L1 element, then design and test-readiness reviews as branches mature. After a baseline, changes go through a change request that lists the affected requirements (found through trace links), tests, parameters and manuals, and is approved by a small change board.

**10.6 Tools.** A small team can keep requirements as structured text (for example YAML or Markdown with one requirement per block) in the same version-control repository as the models, code and tests, with scripts for trace checks and matrix generation; this suits automated testing well. Dedicated tools (DOORS, Jama Connect, Polarion, Capella for model-based work) become worthwhile when the requirement count or team size grows.

## 11. Engineering artifacts, operational manuals and peer review

Every step produces a documented artifact, every artifact is peer reviewed before it is baselined, and the operational manuals are written as a deliberate second view of the vehicle that the reverse-engineering team can work from.

**11.1 Artifact set.**

| Artifact | Level | Content | Review type |
| --- | --- | --- | --- |
| Project plan (lightweight SEMP) | L0 | Organisation, levels, process tailoring, review schedule | Technical review |
| Concept of operations | L0 | Stakeholders, scenarios, operating concept | Technical review with stakeholders |
| L0 requirements document | L0 | Objectives, constraints, success criteria | Inspection |
| System requirements specification, one per L1 element | L1 | Aeronef, STP and REE requirements | Inspection |
| Interface control documents | L1–L2 | Data, units, rates, frames between elements | Inspection |
| Model specification | L2 | Axis conventions, equations of motion, gravity, drag, mass and inertia model | Technical review plus inspection |
| Parameter database | L2–Ln | Every configurable value, with unit, source and status | Inspection |
| Hazard analysis | L1–L2 | Failure conditions, severities, resulting requirements | Technical review |
| Subsystem and software requirements | L2–Ln | Flight control, allocation, autoflight, STP components | Inspection |
| Design descriptions | L2–Ln | Architecture, control-law designs, trade studies | Technical review |
| Verification plan and procedures | All | Methods, scenarios, success criteria | Inspection |
| Verification matrix and results | All | Generated status per requirement | Audit at each milestone |
| Simulation credibility report | STP | Model verification, validation and uncertainty | Technical review |
| Operational manuals and procedures | L1 | See 11.2 | Walkthrough plus inspection |

**11.2 Operational manuals as reverse-engineering evidence.** Produce manuals modelled on airline documentation, written for an operator rather than for an engineer:

- **Vehicle Operating Manual:** vehicle description, limitations (fuel, effector authority, operating volume), autoflight mode descriptions with what each mode holds, captures and annunciates, and the conditions for each mode transition.
- **Normal, abnormal and emergency procedures:** step-by-step, for example engaging Position Hold, responding to LOW FUEL, responding to an effector-failure annunciation.
- **Quick reference checklists:** the short form of the procedures.
- **STP user guide:** how to configure, run and read a simulation and a test campaign.

Four rules make the manuals useful as evidence:

1. Describe observable behaviour and operator actions; never paste requirement text.
2. Trace each manual section and procedure to the requirements it describes, in a register kept outside the released manual. This register is the answer key for scoring the reconstruction.
3. Version manuals with the requirement baseline they describe, and update them through the same change process.
4. Decide, in the REE's L1 requirements, exactly which artifacts the reverse-engineering team receives (manuals, logs, executable simulation) and which it does not (requirements, design, source code).

**11.3 Peer-review process.** Use the IEEE 1028 review types according to the artifact (table in 11.1): a **walkthrough** led by the author to explain and gather feedback; a **technical review** focused on technical soundness and design choices; an **inspection**, the most formal, for requirement sets and procedures.

1. **Plan:** the moderator confirms entry criteria (artifact complete, self-checked against Section 13, trace links present), picks reviewers including one outside the author's team for critical items, and sets the date.
2. **Prepare:** each reviewer reads the artifact alone using the checklist, and logs findings with location and severity.
3. **Meet:** the moderator leads; a reader paraphrases the artifact; a recorder logs findings and decisions. The meeting finds defects; it does not fix them.
4. **Rework:** the author resolves each finding or records why it was rejected.
5. **Close:** the moderator verifies the rework against exit criteria (no open major findings, TBDs listed) and the artifact is baselined. The review record is kept as evidence.

## 12. Worked example: one thread from L0 to verification

The example follows the autoflight Position Hold mode from a project objective down to a test procedure and a manual procedure, showing allocation, a derived requirement, an interface and the STP's supporting requirement. All values are placeholders held in the parameter table.

| ID | Level | Statement | Parent | Verification |
| --- | --- | --- | --- | --- |
| L0-OBJ-002 | L0 | The Aeronef project shall develop autoflight functions, derived from airliner autoflight concepts, as the primary method of operating the vehicle. | — | Inspection of L1 coverage |
| L1-AER-001 | L1 | The Aeronef shall provide a Position Hold autoflight mode. | L0-OBJ-002 | Demonstration |
| L2-AER-AF-PH-010 | L2 | When Position Hold is engaged, the autoflight system shall capture the current vehicle position as the reference position. | L1-AER-001 | Test TP-AF-PH-010 |
| L2-AER-AF-PH-020 | L2 | While Position Hold is active, the autoflight system shall hold the vehicle position within \[P-AF-012\] m of the reference position. | L1-AER-001 | Test TP-AF-PH-020 |
| L2-AER-AF-PH-030 | L2 | While Position Hold is active, the autoflight system shall annunciate POS HOLD. | L1-AER-001 | Test TP-AF-PH-030 |
| L3-AER-FC-TR-040 | L3 | The translational controller shall track each commanded velocity component with a steady-state error of at most \[P-FC-021\] m/s at maximum and minimum vehicle mass. | L2-AER-AF-PH-020 | Test TP-FC-TR-040 |
| L3-AER-EF-010 | L3 | The effector system shall deliver a force of at least \[P-EF-001\] N along each body axis. | L2-AER-AF-PH-020 | Analysis AN-EF-010 |
| L4-AER-FC-AL-050 | L4 | If a commanded body force exceeds the effector limit on any axis, then the control allocation shall scale all translational force commands by the same factor. | Derived (design decision DD-012: preserve direction of translation) | Test TP-FC-AL-050 |
| ICD-AER-STP-005 | L2 | The Aeronef model shall output the vehicle position in the local reference frame defined in model specification MS-DYN, in metres, at each simulation step. | L2-AER-AF-PH-020 | Inspection |
| STP-TA-030 | L2 | The STP shall execute each test procedure tagged with a requirement ID without operator action and record pass or fail against its success criteria. | L0-OBJ-003 | Demonstration |

**Reading the thread.** L0-OBJ-002 is satisfied when the autoflight modes, including Position Hold, are delivered; L1-AER-001 is satisfied when capture (PH-010), hold accuracy (PH-020) and annunciation (PH-030) are all met; PH-020 is in turn satisfied by translational tracking accuracy and enough effector authority, which is a budget split recorded in its rationale. L4-AER-FC-AL-050 has no parent: it comes from a design decision, so it is marked Derived and reviewed against the hazard analysis (saturation, Section 6).

**Downstream links.** TP-AF-PH-020 lives in the STP test suite, tagged with L2-AER-AF-PH-020, and runs every night. The Vehicle Operating Manual section on Position Hold tells the crew what the mode holds, what POS HOLD looks like and how to disengage it; the manual trace register links that section to PH-010, PH-020 and PH-030, so a reconstruction by the REE can be scored against them.

## 13. Checklists and templates

Authors run the single-requirement checklist before submitting; reviewers use both checklists during inspection.

**13.1 Single requirement.**

- [ ] One "shall", one subject, one thought; no "and", "or", "unless"
- [ ] Subject is the element at this level, not a person
- [ ] Fits an EARS pattern; conditions and timing are explicit
- [ ] Every quantity has a number or parameter ID, an SI unit and a tolerance
- [ ] No vague terms, escape clauses, open lists or absolutes
- [ ] States what, not how, or the constraint is justified in the rationale
- [ ] All terms are in the glossary; axes follow the coordinate-system standard
- [ ] Rationale written; parent or "Derived" recorded; source recorded
- [ ] Verification method and success criteria stated
- [ ] Criticality assigned; TBD or TBR items have an owner and a date

**13.2 Requirement set.**

- [ ] Each parent is fully covered by its children, with a sufficiency argument
- [ ] No duplicates or conflicts; consistent terms and units across the set
- [ ] Functional, performance, interface, failure-handling, model-fidelity and documentation requirements all considered
- [ ] Each hazard-analysis row has at least one requirement and one fault-injection test
- [ ] Each interface is covered by an ICD and interface requirements on both sides
- [ ] Derived requirements reviewed at the parent level and against the hazard analysis
- [ ] Trace checks pass: no orphans, no childless parents, no untested requirements
- [ ] Affected manual sections identified

**13.3 Requirement record template.**

```markdown
ID:            L<n>-AER-<SUBSYSTEM>[-<ITEM>]-<NNN>
Level:         L2
Type:          Functional | Performance | Interface | Constraint | Safety | Model fidelity | Documentation
Statement:     [While <state>,] [when <trigger>,] the <element> shall <response> <performance>.
Rationale:     Why it exists; assumptions; design decision if derived.
Parent(s):     <IDs> | Derived (<design decision ID>)
Source:        <ConOps scenario | hazard row | stakeholder need | trade study>
Allocated to:  <child elements>
Criticality:   Catastrophic | Hazardous | Major | Minor | No safety effect
Verification:  Inspection | Analysis | Demonstration | Test — <procedure ID>; success criteria: <...>
Parameters:    <P-xx-nnn, ...>
TBD/TBR:       <item, owner, date>
Owner:         <name>
Status:        Draft | Reviewed | Baselined | Verified | Deleted
Version:       <n>
```

**13.4 Peer-review record template.**

```markdown
Artifact / version:   <name, version, baseline>
Review type:          Walkthrough | Technical review | Inspection
Moderator / author / reader / recorder / reviewers: <names>
Entry criteria met:   yes | no (<why>)
Findings:             <ID> | <location> | <description> | Major/Minor | <disposition> | <closed by, date>
TBD/TBR list checked: yes | no
Exit decision:        Baseline | Rework and re-review | Rework, moderator closes
```

## 14. References

- Aeronef Project — Aircraft Characteristics, initial concept summary, 2026-10-24 (project input).
- [SAE ARP4754B, Guidelines for Development of Civil Aircraft and Systems](https://saemobilus.sae.org/content/ARP4754B), December 2023.
- [SAE ARP4761A, Guidelines for Conducting the Safety Assessment Process on Civil Aircraft, Systems, and Equipment](https://saemobilus.sae.org/content/ARP4761A), December 2023.
- [Release of ARP4754B: exploring the updates](https://dmd.solutions/blog/arp4754b-updates) — validation methods and independence.
- [ISO/IEC/IEEE 29148:2018, Requirements engineering](https://store.sfs.fi/en/ieee-29148-2018).
- [INCOSE Guide to Writing Requirements v4, Summary Sheet](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf), INCOSE-TP-2010-006-04, June 2023.
- [Easy Approach to Requirements Syntax (EARS)](https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax); Mavin et al., RE'09, 2009.
- [NASA Systems Engineering Handbook, Appendix C: How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/), SP-2016-6105 Rev 2.
- [NASA Systems Engineering Handbook, 4.2 Technical Requirements Definition](https://www.nasa.gov/seh/4-2-technical-requirements-definition).
- [NASA Systems Engineering Handbook, Appendix D: Requirements Verification Matrix](https://www.nasa.gov/seh/appendix-d_requirements-verification-matrix).
- [NASA-STD-7009B, Standard for Models and Simulations](https://standards.nasa.gov/node/263), March 2024.
- RTCA DO-178C and DO-331 — see [George Romanski on DO-178C requirements-based testing](https://www.electronicdesign.com/technologies/embedded/article/21800099/george-romanski-of-verocel-explains-do-178c-certification-for-airborne-equipment).
- [AIAA R-004-1992, Recommended Practice for Atmospheric and Space Flight Vehicle Coordinate Systems](https://webstore.ansi.org/standards/aiaa/0041992); [SAWE STD A-6 (2023)](https://sawe.org/?p=5768).
- IEEE 1028, Standard for Software Reviews and Audits — see [software walkthrough overview](https://en.wikipedia.org/wiki/Software_walkthrough).
