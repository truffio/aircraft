# Aeronef Project — Aircraft Requirements Definition Plan

**Status:** Draft plan, not started
**Date:** 2026-10-24
**Branch:** `aircraftDef`

## 1. Purpose and scope

This plan organises the work of defining the requirements of the **Aeronef** (element `AER`), starting from [AIRCRAFT_CHARACTERISTICS.md](AIRCRAFT_CHARACTERISTICS.md) and following [METHODOLOGY.md](METHODOLOGY.md). It describes the phases, the parallel sub-agents that carry them out, the model and effort each one uses, and the gates between phases. It does not start the definition itself.

**In scope**

- The L0 statements the Aeronef traces to (objectives, constraints, success criteria), plus the ConOps scenarios and conventions the vehicle requirements need.
- The L1 Aeronef System Requirements Specification.
- L2 subsystem requirements: dynamics, effectors, fuel and mass properties, flight control, autoflight, flight control panel (D55), navigation, and operational data output.
- Lower levels wherever a branch needs them, down to the last layer that is still a requirement (Section 9, D4).
- The autoflight mode catalogue in Section 9, D56 (which replaced D3).
- The model specification (MS-DYN), the parameter database, and the Aeronef side of the interface control documents.
- Verification planning: a method, a procedure ID and success criteria for every requirement.

**Out of scope for this plan**

- Hazard and failure analysis, which is deferred per the tailoring note in METHODOLOGY.md. Criticality is set to "Not assessed", and no Safety-type requirements or fault-injection requirements are written.
- Implementation: design descriptions, algorithms, software low-level requirements and code structure. Decomposition stops at the layer above them.
- Requirements for the Simulation and Testing Platform (TST) and the Reverse-Engineering Effort (RVS), except the Aeronef side of shared interfaces.
- Operational manuals. They come after the requirements baseline. This plan only keeps the requirements in a state that manuals can trace to.
- Test procedure implementation. This plan names procedures and success criteria; the TST writes and runs them later.
- Manual control. There is none: no stick or yoke, and no requirement is written for it at L1 (D49, D55).

## 2. Inputs

| Input | Used for |
| --- | --- |
| OBJECTIVES.md | L0 objectives and success criteria |
| AIRCRAFT_CHARACTERISTICS.md | Vehicle concept, modelling boundaries, constraints |
| TESTING_ENVIRONMENT.md | Interface needs toward the TST, data-collection needs |
| REVERSE_ENGINEERING.md | Constraints on operational data output (observable, but must not leak protected design) |
| METHODOLOGY.md | Process, writing rules, attributes, ID scheme, checklists, templates |

## 3. Output layout

All requirements live in one folder, `requirements/`, with **one file per level**. Inside each level file, there is one section per element or subsystem, in a fixed order: DYN, FU, EF, FC, AF, FCP, NAV, TM.

```
requirements/
  L0.md                            L0-OBJ / L0-CON / L0-SUC statements + assumptions register
  L1.md                            Aeronef system requirements
  L2.md                            Subsystems: DYN, FU, EF, FC, AF, FCP, NAV, TM
  L3.md                            Sub-functions: FC axis controllers and allocation, one section per autoflight mode, ...
  L4.md …                          Only if a branch still needs a requirement layer (D4)
specs/
  CONOPS.md                        Stakeholders, needs, scenarios (Aeronef-relevant)
  CONVENTIONS.md                   Frames, axes, signs, units (SI and crew-facing units), time base
  GLOSSARY.md                      Defined terms
  MS-DYN.md                        Model specification: equations of motion, gravity, drag, mass, inertia
  FUNCTIONAL_ANALYSIS.md           Function list, N² matrix, control-loop flow
  AF_MODE_LOGIC.md                 Mode groups, compatible combinations, state-transition diagram, decision tables
icd/
  ICD-AER-TST.md                   Aeronef ↔ TST (Aeronef side)
  ICD-FC-AF.md                     Flight control ↔ autoflight
  ICD-NAV-AF.md                    Navigation ↔ autoflight
  ICD-FCP.md                       Flight control panel ↔ autoflight, navigation, fuel (D55; L1-AER-880)
parameters/
  PARAMETERS.yaml                  Parameter database (ID, name, unit, value, status, source)
registers/
  TBD_TBR.md                       Open items with owner and closure date
  DECISIONS.md                     Design decisions (DD-nnn) behind derived requirements
  CHANGE_REQUESTS.md               Upward change requests raised by child levels
verification/
  VERIFICATION_PLAN.md             Method, procedure ID and success criteria per requirement
  VCRM.md                          Generated verification matrix
reviews/
  <artifact>_<gate>.md             Peer-review records (METHODOLOGY 13.4)
templates/
  REQUIREMENT.md                   Requirement and assumption record format (parsed by the scripts)
  REVIEW_RECORD.md                 Peer-review record (METHODOLOGY 13.4)
tools/
  (lint, trace-check and matrix scripts)
work/<agent-id>/                   Staging: draft sections, proposals, interface needs, issues (not baselined)
```

Requirement records use the Markdown template in METHODOLOGY 13.3, one block per requirement. The parameter database is YAML so scripts can read it.

**Shared level files are written in two steps.** Several agents contribute to the same level file at once. Each agent writes its section as a draft, `work/<agent-id>/<level>_<SUBSYSTEM>.md`, and the orchestrator assembles the drafts into the level file in the fixed section order. No two agents ever edit the same file.

## 4. Model and effort policy

| Model | Use it for | Default effort |
| --- | --- | --- |
| **Opus** | Primary authoring of requirement sets and specifications; the highest-leverage judgement (L1 architecture and allocation, the autoflight mode logic); independent gate reviews. | high; xhigh for the L1 architecture, the autoflight core, and mathematical or control-heavy work (MS-DYN, flight control) |
| **Sonnet** | Pattern-following authoring once a reference exists, verification planning, tooling scripts, integration bookkeeping. | medium–high |
| **Haiku** | Mechanical checks against the METHODOLOGY 13.1 checklist: one "shall", vague terms, missing attributes, ID format. | low–medium |

Two rules apply throughout:

1. **Independence.** A reviewer is never the agent that authored the artifact. Each gate review uses a fresh Opus / high instance that receives only the artifacts, their inputs and the checklists, never the author's working notes or conversation.
2. **Escalation.** If a Sonnet or Haiku agent reports low confidence or finds a design question, the item goes back to the orchestrator. It is not resolved at the lower tier.

## 5. Roles

| Role | Who | Responsibilities |
| --- | --- | --- |
| **Project owner** | Martin | Decides open questions, approves each gate, owns the baselines, and is the Owner attribute of every requirement this cycle. |
| **Orchestrator** | Main Claude Code session | Launches agents, assembles the level files, owns the shared files (parameter database, glossary, ICDs, registers), merges staging proposals, runs scripts, commits, prepares gate packages. |
| **Author agents** | Sub-agents, Sections 6–7 | Write the requirement sections they are assigned. They do not edit shared files; they propose changes in `work/<agent-id>/`. |
| **Reviewer agents** | Sub-agents, Section 8 | Lint and inspect. They raise findings and do not fix artifacts. |

Each author agent runs with `isolation: "worktree"` and returns:

- its draft sections, and any spec file it owns;
- `work/<agent-id>/param_proposals.md`, with new parameters and their units, values or TBD;
- `work/<agent-id>/interface_needs.md`, with data it needs from, or provides to, other subsystems;
- `work/<agent-id>/glossary_proposals.md`;
- `work/<agent-id>/issues.md`, with change requests to the parent level, conflicts and questions for the project owner.

## 6. Phases

Phases run in sequence. Agents within a phase run in parallel unless marked otherwise.

### Phase 0 — Setup

| ID | Task | Model / effort | Depends on |
| --- | --- | --- | --- |
| T0 | Orchestrator creates the folder layout, the level files with their empty sections, empty registers, the parameter-database skeleton and the requirement template. | Orchestrator | — |
| T1 | Tooling agent writes the Python scripts: requirement parser (reads all level files), METHODOLOGY 13.1 lint (vague terms, escape clauses, multiple "shall", missing attributes), trace check (orphans, childless parents, requirements without a verification method), VCRM generator, parameter-reference check, and the assembler that builds level files from draft sections. | Sonnet / medium | T0 |

T1 runs in parallel with Phase 1.

### Phase 1 — L0 and foundations

| ID | Task | Outputs | Model / effort |
| --- | --- | --- | --- |
| A1 | Write the L0 requirements from OBJECTIVES.md and the modelling boundaries in AIRCRAFT_CHARACTERISTICS.md §7. Cover objectives (L0-OBJ), constraints as Constraint-type requirements (L0-CON: no lift or control surfaces, fixed CG, no electrical system, fictional effectors), success criteria (L0-SUC), and an assumptions register with owners (perfect state knowledge, for example). | Draft `L0` section → `requirements/L0.md` | Opus / high |
| A2 | Identify stakeholders and needs (METHODOLOGY 4.1) and write the Aeronef-relevant ConOps scenarios. They cover the catalogue in D3, for example: climb on angle to an altitude capture, then hold; descend on vertical speed; fly a constant heading at a set horizontal speed; intercept and track a VOR radial; hold a position; hover at an altitude; and a reference mission to fuel exhaustion. No failure scenarios. | `specs/CONOPS.md` | Opus / high |
| A3 | Propose the conventions per AIAA R-004: body frame, local reference frame, Euler-angle sequence, altitude datum, north reference for heading, track and VOR radials, and the time base. Define SI units for requirements and the crew-facing units (D7), with conversions. Seed the glossary, including the distinct definitions of heading (where the nose points) and track (the direction of horizontal motion), which are independent on the Aeronef. Present the alternatives that matter (for example NED versus ENU) with a recommendation. | `specs/CONVENTIONS.md`, `specs/GLOSSARY.md` | Opus / high |

**Gate G0 — L0 mission and concept review**

- Haiku / low lints A1 against the checklist.
- Opus / high inspects A1–A3 together for consistency, coverage of the objectives and conflicts.
- The project owner decides the conventions and approves the baseline.
- Exit: no open major findings, conventions fixed, L0 baselined and tagged `L0-baseline-1`.

### Phase 2 — Aeronef functional analysis, L1 and allocation

This phase is one agent, because L1 coherence matters more than speed here.

| ID | Task | Outputs | Model / effort |
| --- | --- | --- | --- |
| B1 | Refine the Aeronef function list (F-AER-01 to 08, plus functions for navigation and for producing operational data). Build the N² interface matrix and the control-loop flow. Write the L1 Aeronef SRS: functional, performance, interface, constraint, model-fidelity and documentation types. Choose the logical architecture and allocate every L1 requirement to an L2 subsystem (DYN, FU, EF, FC, AF, NAV, TM). Set the top-level budgets (fuel, effector authority, position error, timing). Take the D3 catalogue as given. At L1, state only the aircraft-level guidance capability, treating the aircraft as a whole. Leave the mode definitions, groups, combinations and logic to C5 at L2 (D33). Propose an answer to Q5 for the project owner. | `specs/FUNCTIONAL_ANALYSIS.md`, draft `L1` section → `requirements/L1.md`, staging files | Opus / xhigh |
| B2 | Runs after B1. Seed the parameter database from B1's proposals: assign P-xx-nnn IDs, units and TBD/TBR status. Open the TBD/TBR register entries. | `parameters/PARAMETERS.yaml`, `registers/TBD_TBR.md` | Sonnet / medium |
| B3 | Runs after D69 (2026-11-05). Landing gear and ground operations change: draft the change requests against L0, L1, CONOPS, CONVENTIONS, GLOSSARY and FUNCTIONAL_ANALYSIS (runs start on the ground; ground contact on the gear is a landing, not the end of the run; effectors off and no fuel use on the ground; Takeoff and Land modes; the gear as a function and its allocation; the altitude reference of the hover height, TT-820), and list the C1/C2 L2 records to rework. Owner approval, then C1/C2 rework before G2. | `work/B3/` (CRs, impact list) | Opus / high |

**Gate G1 — System Requirements Review (Aeronef)**

- Haiku / low runs the lint and the trace check (every L1 requirement has an L0 parent or is flagged Derived).
- Opus / high, as a fresh instance and not B1, inspects sufficiency against L0, the allocation, the budgets and the mode grouping.
- The project owner answers Q5 and approves the L1 baseline.
- Exit: L1 baselined and tagged `AER-L1-baseline-1`.

### Phase 3 — L2 subsystem requirements (main parallel fan-out)

Eight agents run in parallel. Each agent:

- reads L0, L1, CONVENTIONS, GLOSSARY, PARAMETERS and the relevant parts of METHODOLOGY;
- writes its subsystem's L2 section, with the full attributes of METHODOLOGY 9.2 and a sufficiency argument per L1 parent;
- states the verification method;
- references parameters by ID and never writes numbers in sentences;
- flags derived requirements and records their design decisions as DD proposals;
- stops where the next layer would be implementation (D4).

| ID | Subsystem | Notes | Model / effort |
| --- | --- | --- | --- |
| C1 | **DYN** — dynamics model | Also writes `specs/MS-DYN.md`: 6-DOF rigid-body equations, gravity model, drag model, integration requirements, and the independent analytical checks for credibility (free fall, terminal velocity, torque-free rotation, fuel-mass integral; METHODOLOGY 10.3). | Opus / xhigh |
| C2 | **FU** — fuel and mass properties | Fuel quantity, consumption for linear and rotational actuation (configurable), mass decrease, fixed CG, inertia assignment and how it changes with fuel. Fuel exhaustion is nominal behaviour, not a failure. | Opus / high |
| C3 | **EF** — effectors | Fixed-direction emitters: authority per axis, limits, command response, consumption interface to FU. Stays solution-free: the emitter layout is a design decision, not a requirement. | Opus / high |
| C4 | **FC** — flight control | L2, plus the L3 sections for translational control (TR), rotational control (RO) and control allocation (AL). Includes independent per-axis regulation, saturation handling as nominal behaviour, and the constraint that control laws are swappable without changing the vehicle model (objective: compare control laws). | Opus / xhigh |
| C5 | **AF** — autoflight core | Writes the L2 autoflight section and `specs/AF_MODE_LOGIC.md`. The mode logic covers the catalogue of D56 (one horizontal and one vertical mode, plus Go to hover and Hover), armed versus active states (Go to hover arming Hover), engagement, automatic transitions (for example Go to altitude → Altitude hold, Go to hover → Hover), disengagement, annunciation, target selection, and the heading behaviour in each mode; pitch and roll stay at zero (D57). Per-mode details are left to Phase 4. | Opus / xhigh |
| C6 | **NAV** — navigation | Navigation references used by autoflight and the panel: position, altitude, height above the ground, heading, track, horizontal and vertical speed. No VOR and no flight path angle (D56). | Opus / high |
| C7 | **TM** — operational data output | Signals the Aeronef exposes so inputs, mode changes, control activity and responses can be correlated (REVERSE_ENGINEERING §3C, TESTING_ENVIRONMENT §8). Includes the selected targets, armed and active modes, and annunciations. Whether each signal is *releasable* or *protected* is decided with the RVS (#69, D44), so that telemetry does not leak protected design. | Opus / high |
| C8 | **FCP** — flight control panel (D55) | The crew interface as data: the mode selections and the heading, horizontal speed, target altitude and vertical speed selectors (D56), the annunciations and indications, and the conversion to and from crew units (CV-740 to CV-770). Defines the panel content (#79). No physical device or display format (L1-AER-510). | Opus / high |

C1–C3 are closely coupled (mass, inertia, effector forces, consumption), as are C5, C6 and C8 (navigation data used by the modes, selections and annunciations crossing the panel). Coupled agents do not coordinate directly; they record needs in `interface_needs.md` and the integration step resolves them.

### Phase 3b — Integration (sequential)

| ID | Task | Model / effort |
| --- | --- | --- |
| I1 | Assemble `requirements/L2.md` from the drafts. Merge all staging proposals: the parameter database, glossary and DD register. Write `icd/ICD-AER-TST.md` (Aeronef side: state vector, effector commands, operational data, frame rate, units), `icd/ICD-FC-AF.md`, `icd/ICD-NAV-AF.md` and `icd/ICD-FCP.md`, and decide the home of the vehicle-model boundary definitions (IN-B1-01). Resolve cross-subsystem conflicts, check that the budgets close, and turn unresolved conflicts into change requests at L1 or questions for the project owner. | Opus / xhigh |
| I2 | Re-run the parameter-reference check and the trace check. | Orchestrator (scripts) |

**Gate G2 — Subsystem requirements review**

- Eight Haiku / low lint agents run in parallel, one per L2 section.
- Two Opus / high inspectors run in parallel: one for DYN, FU and EF plus MS-DYN (physics consistency), and one for FC, AF, FCP, NAV and TM plus the ICDs (control, guidance, crew interface and data consistency).
- The project owner approves.
- Exit: L2 baselined and tagged `AER-L2-baseline-1`.

### Phase 4 — Lower-level requirements (second fan-out)

There is one L3 section per autoflight mode, plus the flight-control deepening. Each agent decomposes its branch until the next layer would be implementation (D4). If that point is not reached at L3, the agent continues into the next level file.

| ID | Mode or branch | Model / effort |
| --- | --- | --- |
| M0 | **Stationary** (position hold over the ground, D56), the reference mode and the METHODOLOGY §12 worked example: engagement and position capture, hold accuracy, annunciation, disengagement, and the flow-down to FC and EF. This sets the pattern for the other modes. | Opus / high |

These run in parallel after M0:

| ID | Mode or branch | Model / effort |
| --- | --- | --- |
| M1 | Withdrawn: no flight path angle mode (D56) | — |
| M2 | **Vertical speed**: climb or descent at the selected rate (feet per minute), then capture and hold of the selected altitude | Sonnet / high |
| M3 | **Go to altitude and Altitude hold**: climb or descent at the standard or selected vertical speed, capture of the selected altitude, then hold | Opus / high |
| M4 | Withdrawn: horizontal speed is a selector of Heading, not a mode (D56) | — |
| M5 | **Heading** at the selected horizontal speed, including a heading change in place at zero speed | Sonnet / high |
| M6 | Withdrawn: no track hold mode (D56) | — |
| M7 | Withdrawn: no VOR (D56) | — |
| M8 | **Go to hover and Hover**: from any mode, stop on all axes at the hover height, arm Hover, engage it when stationary, then hold height and position against the wind | Opus / high |
| FC1 | **Flight-control deepening**: TR, RO and AL to the last requirement layer, including the allocation priority rule as a derived requirement with its DD entry | Opus / high |

M3 and M8 use Opus because arming, capture and transition logic is the subtlest part of the catalogue. Any Sonnet mode that departs significantly from the M0 pattern is escalated to Opus / high. The orchestrator then assembles `requirements/L3.md`, and any lower level file.

**Gate G3 — Lower-level requirements review**

- Haiku / low lints each section.
- Opus / high runs one inspection across all modes. It checks that the mode sections agree with AF_MODE_LOGIC and with each other: the transitions, compatible combinations and annunciations match, and there are no gaps between climb or descent, capture and hold.
- The project owner approves.

### Phase 5 — Verification planning (third fan-out)

There is one agent per group of sections, run in parallel. For every requirement, the agent writes:

- the method (Inspection, Analysis, Demonstration or Test);
- the procedure ID (TP-, AN-, DM- or IN-nnn);
- success criteria stated before the work, per METHODOLOGY 9.3 and 10.2.

Physics requirements are verified by analysis against independent solutions, and functional and performance requirements by automated TST tests. The agents add nominal and boundary cases; robustness cases tied to failures are deferred.

| ID | Scope | Model / effort |
| --- | --- | --- |
| V1 | DYN, FU, EF and MS-DYN | Sonnet / high |
| V2 | FC (all levels) | Sonnet / high |
| V3 | AF, FCP and NAV (all levels, all modes) | Sonnet / high |
| V4 | TM, ICDs, L1 and L0 | Sonnet / high |
| V5 | Runs after V1–V4. Generate `verification/VCRM.md` with the script and check that no requirement lacks a method. | Orchestrator (scripts) |

**Gate G4 — Verification plan inspection and requirements baseline**

- Opus / high runs the inspection, which checks that the success criteria are measurable and that the procedures are written from the requirement and not from a design.
- The trace checks must pass: no orphans, no childless parents, no requirement without a verification method. L0 requirements allocated only to TST or RVS are not counted as childless (D44).
- The project owner approves the complete Aeronef requirements baseline, tagged `AER-REQ-baseline-1`.

## 7. Standard brief for every author agent

Each agent prompt contains the following:

1. **Role, the sections it drafts and any spec file it owns.** It must not edit any other file.
2. **Inputs to read**, with paths, including the relevant METHODOLOGY sections (8 writing rules, 9 attributes, 13 checklists and template).
3. **Tailoring reminders.** Hazards are deferred, Criticality is "Not assessed", and the Safety type is not used.
4. **Depth rule (D4).** Stop decomposing when the next layer would describe the implementation: design, algorithms, gains or code structure. Record such content as a DD proposal, not as a requirement.
5. **Writing rules.**
   - Use EARS patterns, one "shall" per requirement.
   - Use parameter IDs instead of numbers, SI units, and terms from the glossary only. Crew-facing units appear only in requirements about crew selection or annunciation, per CONVENTIONS.
   - Write the rationale at the same time as each requirement, with a sufficiency argument per parent.
6. **ID scheme** (METHODOLOGY 9.1). Number in steps of 10, and never reuse an ID.
7. **Information separation.** All design artifacts are protected. Nothing in the outputs is written as operator-facing manual text. Whether each signal is releasable or protected is decided with the RVS (#69, D44).
8. **Hand-back.** The agent returns its draft sections, its staging files (Section 5), a self-check against METHODOLOGY 13.1, and a short summary: counts per type, open TBD/TBR, derived requirements, and questions for the project owner.

## 8. Reviews

| Check | Tool | When |
| --- | --- | --- |
| Lint (METHODOLOGY 13.1 mechanical items) | Script plus Haiku / low | Every gate, per section |
| Trace and parameter-reference checks | Scripts | Every gate, and after each integration |
| Inspection (METHODOLOGY 13.2, sufficiency, consistency) | Opus / high, fresh instance, never the author | G0–G4 |
| Approval | Project owner | Every gate |

Findings are recorded with the METHODOLOGY 13.4 template in `reviews/`. Authors rework, and the orchestrator confirms closure before the baseline tag.

## 9. Decisions

### Decided (2026-10-24; D8–D40 on 2026-10-25)

| ID | Decision | Outcome |
| --- | --- | --- |
| D1 | Requirement storage format | Markdown blocks per METHODOLOGY 13.3; parameter database in YAML |
| D2 | Requirement layout | One file per requirement level, all in `requirements/` (Section 3) |
| D3 | Autoflight mode catalogue (**replaced by D56**) | Climb on flight path angle; climb on vertical speed (ft/min); horizontal speed; altitude capture, then altitude hold; descent on flight path angle or vertical speed, similar to climb; heading hold; track hold; VOR radial tracking; position hold; hover at altitude |
| D4 | Depth | No fixed depth. Each branch is decomposed until the next layer would be the implementation. |
| D5 | Scripting language for tools | Python |
| D6 | Owner attribute | Martin for all requirements in this cycle |
| D7 | Crew-facing units | North American aviation units for everything the crew selects or sees: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track, flight path angle, radials). Requirements and the model stay in SI; conversions are fixed in CONVENTIONS. |
| D8 | Ground (#50; refined by D37) | The Earth is flat with no terrain, and altitude zero is ground level. Contact with the ground outside the landing envelope is a crash (D37). |
| D9 | Crew-facing fuel unit (#51) | Pounds (lb) |
| D10 | Attitude during guidance modes (#3, Q2; **revised by D57**) | Pitch and roll stay level. The Aeronef doesn't need to pitch or roll to move. Those manoeuvres are possible but serve no purpose, because the axes are uncoupled. |
| D11 | Hover versus position hold (#4, Q3; **replaced by D56**) | Position hold is a lateral mode. The vehicle stops moving on all axes (zero velocity, zero acceleration) and holds its position at any altitude, compensating for wind. Hover is a vertical mode. When it engages, the vehicle descends from its current altitude to the altitude set on the flight control panel, then holds position. Hover therefore needs position hold. Whether position is held from the moment hover engages, or only after the velocity has come down to zero, is still open (#78). |
| D12 | VOR model (#5, Q4; **withdrawn by D56**: no VOR) | Ideal VOR: the simplest model. Ground stations are at fixed positions in the local frame, radials refer to true north, there is no magnetic variation or noise, and the signal is ideal within the reception range. |
| D13 | Mode compatibility (#61; **replaced by D56**) | A flight-path-angle vertical mode needs horizontal velocity, so it can't be combined with position hold. Detailed design (#6) will produce a compatibility matrix of lateral modes, vertical modes and speed selection. |
| D14 | VOR tracking (#53; **withdrawn by D56**: no VOR) | The crew flies a course. Tracking a radial is a track over the ground, and flying TO or FROM the station changes the course flown. |
| D15 | Mode logic versus controllers (#72) | The modes say how the aircraft flies; the controllers implement them, so the two are decoupled. Every control-law version and autoflight implementation must meet the same mode logic, so any implementation pairs with any law. |
| D16 | Mode engagement rule (#78) | When the crew selects a mode, it normally arms first and engages once its engagement conditions are met. While the mode is armed, the active mode manoeuvres the craft into those conditions. Manoeuvres are g-limited: maximum acceleration and deceleration are design parameters. This covers, for example, climb or descent sequencing to altitude hold, and motion sequencing to position hold. |
| D17 | Wind (#49) | Wind exists and can be configured in the test environment. Position hold compensates for wind. Refined by D51 (gusts). |
| D18 | No coupling between axes (#63) | A motion along one of the six degrees of freedom does not induce acceleration on another axis, seen from the aircraft's body frame. A translation along one axis does not cause translation along another. This is unlike winged aircraft, where roll and yaw are coupled. How this treats the rigid-body kinematic terms is open (#81). |
| D19 | Effectors (#64) | Effectors are fixed in the body frame and nothing swivels. There are enough of them to give control in all 6 degrees of freedom. |
| D20 | Air density (#70) | Standard atmosphere |
| D21 | Local frame (#46) | North-east-down (NED) |
| D22 | Attitude representation (#47) | The quaternion is the authoritative attitude; Euler angles are derived from it. |
| D23 | Angle units (#48) | Radians in calculations, requirements and parameters; degrees only at the crew interface. |
| D24 | Number of designs compared (#65) | One autoflight definition and implementation; two or three control-law designs (TBR). Refined by D42: one control-law design for now. |
| D25 | Reproducibility (#66) | Runs are not checked for bit-identical results, which is out of scope and too costly. A repeated run must give the same expected result. |
| D26 | Pass fraction, reference configuration (#67) | 100%. A failed test means either a badly written procedure or software that doesn't meet its intended function. |
| D27 | L0 size (#74) | Start with the 66 L0 requirements. The owner audits them during review and decides which ones are too detailed for L0. |
| D28 | Method assessment and final report (#75) | Each element contributes its section and the orchestrator compiles them; the human owner audits all of it. |
| D29 | Assumption review (#76) | The owner reviews every assumption before the gate (G0), not at G1, so that a broken assumption is found before work is built on it. |
| D30 | "and" / "or" in statements (#44) | Allowed, provided the requirement meets the quality criteria (clear, complete, testable, implementable). If the conjunctions form a tree of possibilities, split the requirement. The lint reports COMPOUND as a warning only. |
| D31 | Requirement identifiers (#45) | One syntax at every level, starting with the level: `L0-OBJ\|CON\|SUC\|ASM-nnn`, `L1-AER-nnn`, `L<n>-AER-<SUB>[-<ITEM>]-<NNN>`. The prefix must match the Level field, and the lint enforces it. A requirement that moves to another level gets a new ID. |
| D32 | Scenario values (#62) | Test procedures set the defaults and constants for test scenarios. They are not design parameters and stay out of `PARAMETERS.yaml`. |
| D33 | Levels and where modes are defined (#80) | L0 is the project, and the aircraft is a black box at L0. L1 is the project's components: the aircraft (AER), the test environment (TST) and the reverse-engineering effort (RVS). This plan writes only the AER branch of L1. L2 divides a component into its subsystems. Modes, guidance, mode logic and control-law implementation are defined at L2 (AF, FC), not at L0 or L1. |
| D34 | Crew units (#52, refines D7) | What the crew sees and sets is in crew units: feet, knots and degrees. Time is in whatever unit makes sense, so vertical rates are in ft/min and flight duration in hours or minutes. Internal calculations use SI or whatever is most convenient. Crew-facing parameters are stored in their crew unit and flagged in the schema. |
| D35 | Remaining G0 conventions (#58) | Approved as recommended in CONVENTIONS §11: G0-02, -04, -07, -08, -11, -13, -14, -15. |
| D36 | R-004 basis (#57) | No copy of the R-004 text is held. The conventions were checked against public sources (Wikipedia; NASA NESC simulation output spec citing R-004 §1.1.7) and match. CONVENTIONS describes them as "consistent with R-004 practice". |
| D37 | Landing (G0 review of L0-ASM-110) | Landing is modelled as an ideal landing. Contact with the ground within a velocity and acceleration envelope is a successful landing; contact outside it is a crash. There is no gear, bounce or friction model. |
| D38 | Crew-protection limit (#87) | The limit is on the acceleration the crew senses (g load), not on force. As fuel is used up and the mass falls, the resultant effector force is reduced to keep within the limit (L0-CON-310, P-SYS-120). The limit is ±3 g for now: the magnitude of the sensed acceleration is at most 3 g in any direction. |
| D39 | Coverage is 100% (G0 review of SUC) | Every coverage criterion is 100%, never a fraction. Every requirement is verified by the method chosen for it (test, demonstration, analysis or inspection), and every verification passes (L0-SUC-020, -100 to -130). |
| D40 | Verification roll-up (G0 review of SUC) | The lowest-level requirements are verified directly by their method, by test wherever a test applies. A higher-level requirement (L0, L1, …) is verified when all its children have passed and the decomposition has been reviewed. |
| D41 | L0 verification (#90, G0-F01) | Every L0 requirement is verified by roll-up (D40): method Inspection, success criteria "each child requirement has passed its verification and the decomposition has been reviewed". What the children must show stays in the rationale as guidance. |
| D42 | Configurations (#91, G0-F03; refines D24) | One set of flight-control laws for now, so there is one Aeronef configuration: the autoflight implementation with that control-law design. It must pass every requirement (D26). The term "reference configuration" is dropped. Control laws stay replaceable (L0-CON-200) so that more designs can be added later. |
| D43 | Conventions fixed (#92, G0-F10) | All remaining conventions in CONVENTIONS are fixed as written, apart from the items parked for L2 (CV-650, CV-660, #54). The conventions and glossary become Fixed at the L0 baseline; later changes go through a change request. |
| D44 | TST and RVS branches (#93, G0-F12) | This plan covers the Aeronef branch only. The plan will be extended later to the simulation and testing platform (TST) and the reverse-engineering effort (RVS). Until then, L0 requirements allocated only to TST or RVS have no children by design: the trace check and the G1–G4 trace exits do not count them as childless, and they are verified by roll-up once their branch exists. |
| D45 | Crew g-limit (#97, B1-Q03) | The crew acceleration limit (L0-CON-310) is evaluated at the centre of gravity, to keep it simple. The limit of 3 g ([P-SYS-120]) is confirmed. |
| D46 | Effector authority shape (#98, B1-Q04) | The weight is carried along the negative body z axis (up at level attitude) only, with a smaller authority in the other five force directions. **Revised by D72:** the authority in the other five directions is set by the drag at maximum speed and may exceed the upward authority. |
| D47 | Performance envelope (#101, B1-Q07) | The performance envelope values (P-SYS-200 to -280) stay TBD for now. |
| D48 | L1 budgets (#102, B1-Q08) | The B1 budget values are accepted as TBR (FUNCTIONAL_ANALYSIS §7); each closes at G2. |
| D49 | Manual control (#103, B1-Q09) | No manual-control requirement is written at L1. Manual control is a lower-level matter. |
| D50 | AER share of reproducibility and headless running (#104, B1-Q10) | L0-OBJ-110 and L0-CON-190 are also allocated to the Aeronef (CR-B1-01, CR-B1-02). |
| D51 | Wind and gusts (#99, B1-Q05; revises D17) | The wind is horizontal only, with no vertical component. It is a steady wind of 0 to 100 kt ([P-SYS-430]) plus gusts and bursts of up to 50 kt ([P-SYS-560]); the two add up, so the largest instantaneous wind is 150 kt. This replaces the earlier "no gusts" assumption (L0-ASM-050, CR-B1-03). A wind that varies across the operating volume stays with the refined wind model (#84). |
| D52 | Element codes (owner, 2026-10-28) | The test environment element is coded **TST** (was STP) and the reverse-engineering element **RVS** (was REE), in IDs, allocations and text. Review records in `reviews/` and earlier GitHub issues keep the old codes. |
| D53 | Landing envelope (#100, B1-Q06, #100.1) | The landing envelope is two limits at the contact sample: a vertical speed magnitude of at most [P-SYS-500] = 3.458 m/s (a free fall from 2 ft) and a horizontal speed of at most [P-SYS-510] = 0.5 m/s, both TBR. There is no acceleration limit: the ideal landing (D37) has no gear model, so no touchdown shock is computed, and the vertical speed limit stands in for the impact. P-SYS-520 is withdrawn. |
| D54 | Absent systems (owner, 2026-11-04) | No requirement is written for a system the Aeronef does not have; the design simply does not include it. L1-AER-230 (no electrical power) is deleted. L0-CON-160 stays as a scope statement, made a leaf checked directly by inspection over the Aeronef branch (CR-B1-04). |
| D55 | Logical architecture and the flight control panel (#95, B1-Q01; answers #80.3) | The three-layer cascade of FUNCTIONAL_ANALYSIS §5 is approved: the crew sets up the manoeuvre on the flight control panel, autoflight (AF) turns the selections into axis targets (guidance), flight control (FC) turns the targets into effector commands, and the effectors (EF) produce the forces, around a vehicle model (DYN, FU, EF) behind one fixed boundary. NAV derives the guidance quantities from the true state; TM observes and feeds nothing back. The **flight control panel (FCP) is its own L2 subsystem**, the eighth: it owns the crew selections and their presentation on the panel. There is no manual control (no stick or yoke, L0-CON-180); the panel only sets up autoflight. |
| D56 | Autoflight mode catalogue (owner, 2026-11-04; replaces D3, D11, D13; withdraws D12, D14; answers Q5 #6 and #78) | The horizontal and vertical modes are independent: one of each is active at a time. **Horizontal:** *Stationary* holds the horizontal position over the ground, the effectors fighting the wind; *Heading* flies the selected heading at the selected horizontal speed, and with no horizontal velocity a heading change turns the craft in place about the vertical axis. **Vertical:** *Altitude hold* holds the current altitude; *Go to altitude* climbs or descends to the selected altitude at a standard vertical speed, which the crew can change; *Vertical speed* climbs or descends at the selected constant rate and, like Go to altitude, arms Altitude hold, so it levels off at the selected altitude (owner, 2026-11-04). **Both axes:** *Go to hover* takes the craft from whatever it is flying, brings it to zero velocity at the hover height above the ground (a project constant) and arms *Hover*; *Hover* engages once the craft is stationary at that height, and then holds the height and the position over the ground against the wind. These two are the only modes that govern both axes. **Panel selectors:** heading, horizontal speed (from zero to the vehicle's maximum), target altitude and vertical speed. **Dropped:** flight path angle, track hold, VOR radial tracking (and the VOR function), and a separate speed mode. Whether Go to hover climbs to the hover height when engaged below it stays open (#88). Flying with the nose one way and the motion another (need N-110) is dropped (owner, 2026-11-04). |
| D57 | Attitude (owner, 2026-11-04; revises D10) | The dynamics keep all six degrees of freedom, but pitch and roll are not used for now: they are held at zero at all times. The craft translates along three axes and rotates about the vertical axis only. |
| D58 | How L1 is verified (#96, B1-Q02) | D40 applies to L1 as D41 does to L0: each L1 record allocated to subsystems is verified by roll-up (Inspection: each child requirement has passed its verification and the decomposition has been reviewed), and its rationale says what the children must show. The L1 leaves (`Allocated to: —`) keep their own direct method. |
| D59 | Reproducible runs (G1-F09; confirms D25) | Repeat runs of the same configuration, initial condition and selection script must give the same pass/fail verdicts and agree within stated tolerances. They are not required to be bit-identical. |
| D60 | Position-holding accuracy (G1-F06) | The position-holding budget ([P-SYS-450], 1 m TBR) is a horizontal position error, in Stationary and in Hover. Altitude error is covered separately by the altitude-hold tolerance. |
| D61 | Principal axes (G1-F12) | The body axes are the principal axes of inertia: the products of inertia are zero, so a rotation about one body axis produces no torque about another. |
| D62 | Gust shape (G1-F08) | A gust or burst builds up over a minimum rise time (a new parameter, value TBD, set at G2 with the dynamics model and the TST wind model); instantaneous steps are not allowed. The budgets close against it. |
| D63 | G1 owner questions (reviews/G1/dispositions.md Q1–Q4, 2026-11-04) | **Q1:** the process and document records L1-AER-750 to -860 stay at L1 as leaves with the Aeronef as subject. **Q2:** the envelope records require each value from zero up to the maximum to be sustainable; tracking tolerances stay at L2. **Q3:** L0-CON-100's "initial fuel quantity as a parameter" is the capacity [P-FU-010] plus the initial fuel of each run's initial condition; no change request. **Q4:** the tolerances of D59 are those of each success criterion; no run-to-run tolerance parameter. Also: the flight control panel boundaries get their own ICD-FCP. |
| D64 | Dynamics model (C1 questions, owner 2026-11-05; closes #81 and #81.1) | **Kinematic terms:** the rotation-during-translation term ω × v is retained (option T1, Newtonian); the gyroscopic term and the resolution of forces through the attitude are retained too (MS-DYN §4.5). **Drag:** isotropic quadratic drag, the same in every direction, with one drag area [P-DYN-100] (option D1); no aerodynamic moment. **Body:** a capsule 12 m long and 4 m in diameter, crew station at (4, 0, −1) m in body axes, all TBR. **Gusts:** one-minus-cosine rise and decay over at least [P-SYS-570] = 2 s (TBR). **Gravity:** [P-DYN-010] is standard gravity, Set. The other C1 proposals are accepted: DD-050 to DD-100 (from DD-C1-01 to -06), the credibility-check tolerances P-DYN-200 to -270 (TBR) and change requests CR-C1-01, CR-C1-02. |
| D65 | Fuel and mass properties (C2 questions, owner 2026-11-05) | **Inertia** changes linearly with the fuel (uniform depletion, DD-120). **Consumption** is charged on the magnitude of the resultant control force and of the resultant control moment, one coefficient each, common to the effector set (DD-110). **Fuel-integral check** uses the FU outputs of every simulation step. **Initial fuel** outside zero to [P-FU-010] is rejected, not clamped (DD-140). **#59:** the FU share is closed (the fuel-exhaustion indication); the autoflight behaviour stays with C5. **Masses:** dry mass 1000 kg, fuel capacity 500 kg, both TBR. The other C2 proposals are accepted: DD-130, P-FU-060 to -100 (TBR), CR-C2-01, CR-C2-03. |
| D66 | Maximum speed and endurance (owner 2026-11-05; sets part of D47) | The craft's horizontal speed saturates at **300 kt true airspeed** ([P-SYS-230] = 154.333 m/s, Set); an earlier Mach 50 figure is withdrawn, because the turn rate at that speed would be negligible. **At that speed the craft flies 8 hours** from full fuel ([P-SYS-290], Set), anchored at sea level in still air, the densest air of the operating volume, so the endurance at speed is at least that everywhere. With the drag area [P-DYN-100] and the C2 masses this gives the consumption coefficients [P-FU-040] = [P-FU-050] = 2.34 × 10⁻⁷ (kg/(N·s), kg/(N·m·s)), TBR, and, through the fuel budget of L2-AER-FU-290 with its 5 % margin, a hover endurance [P-SYS-280] of 46 h (TBR; 46.7 h computed). Consequences: at 300 kt a 1 g lateral acceleration gives a heading rate of about 3.6 °/s, so retaining ω × v (D64) does not limit turns; the range at maximum speed, about 4400 km, scales the operating radius [P-SYS-220] (still TBD). |
| D67 | Performance envelope (owner 2026-11-05; closes the rest of D47, #101) | Maximum operating altitude [P-SYS-200] 150 000 ft (45 720 m), inside the 47 km atmosphere model with margin; minimum operating altitude [P-SYS-210] the hover height (5 ft); horizontal operating radius [P-SYS-220] 2400 NM (the range at 300 kt for 8 h); maximum climb and descent vertical speeds [P-SYS-240], [P-SYS-250] 6000 ft/min; maximum heading rate [P-SYS-270] 3.6 °/s (a 1 g lateral acceleration at 300 kt). All TBR. |
| D68 | Fuel exhaustion (owner 2026-11-05; answers #59) | When the fuel runs out the effectors stop, the vehicle falls and its ground contact is a crash. There is no recovery: running out of fuel is the crew's to avoid, with the LOW FUEL alert. What the mode annunciations show after exhaustion is C5's (C2 suggests that autoflight disengages and shows no active mode). |
| D69 | Landing gear and ground operations (owner 2026-11-05; answers #60; revises D37, D53, D54 for the gear) | The Aeronef gets an extendable **landing gear**, so it can rest on the ground, stable and stationary, with the effectors off and **no fuel consumption**. **Runs start on the ground**, on the extended gear, effectors off. Two new modes, both axes: **Takeoff**, engaged on the ground, powers up, climbs at [P-AF-240] to the hover height over the current position, retracts the gear and hands over to **Hover**; **Land**, engaged only from Hover, extends the gear, descends at [P-AF-240], touches down within the landing envelope, then switches the effectors off so that fuel consumption stops. Gear length [P-DYN-040] a little less than the hover height (TBR). This changes baselined L0 and L1 records (ground contact, initial conditions, mode catalogue, fuel, absent systems) and the C1/C2 drafts; task B3 drafts the change requests. |
| D70 | Hover, vertical-speed and settling values (owner 2026-11-05; answers #88) | **Go to hover** engaged below the hover height climbs to it, as it descends to it from above. **Hover height** [P-AF-210] 5 ft (Set), measured below the body (see TT-820). **Standard vertical speed** [P-AF-220] 2000 ft/min (Set), the default of Go to altitude and of Vertical speed, climbing and descending. Vertical speed changes ramp at a **vertical acceleration** [P-AF-230] of 0.1 g (TBR): about 10 s to reach 2000 ft/min and a level-off over about 170 ft. **Land and Takeoff vertical speed** [P-AF-240] 60 ft/min (TBR), well inside the landing envelope. **Position-hold settling** [P-SYS-460] 30 s (TBR), set by the deceleration from maximum speed at the 1 g manoeuvre limit (about 16 s) plus the capture. |
| D71 | Flight control panel (owner 2026-11-05; answers #79) | The panel has the buttons that engage each mode (now including Takeoff and Land) and readouts of the values the crew sets: horizontal speed (kt), vertical speed (ft/min), target altitude (ft) and, for Heading, the selected heading (deg, D56). Everything in crew units. Selection resolutions [P-AF-010] to [P-AF-040]: 10 ft, 100 ft/min, 1 kt, 1° (TBR); display resolutions [P-TM-020] to [P-TM-050]: 1 ft, 10 ft/min, 1 kt, 1° (TBR). #69 (reverse engineering), #85 (failures) and #86 (parallel runs) stay deferred. |
| D72 | G2 (partial) owner rulings on C1/C2 (reviews/G2/inspection_C1_C2.md Q1–Q4, G2-F01; owner 2026-11-05) | **No long checks (G2-F01):** no credibility check runs for the 48 h hover duration; the torque-free rotation check C-3 and the rotation-during-translation check C-5 run in a check configuration with no ground contact (gravity zero) over a short accuracy horizon [P-DYN-270] of 600 s (TBR). The terminal-speed check C-2 states its release height and checked altitude band (G2-F02). **Q1 (G2-F03):** [P-SYS-230] is a **ground speed** (CV-480, L1-AER-310, the panel selector); D66's 300 kt is the still-air anchor of [P-SYS-290], where ground speed and true airspeed coincide; C5 bounds the commanded heading rate so that horizontal speed times heading rate stays within [P-AF-200]. Owner said 'true airspeed' in D66; this ruling follows the inspector's recommendation, which the owner accepted, and needs no CR on L1. **Q2 (G2-F04):** D46 is revised: the weight is carried along −z_B only; the authority in the other five force directions is set by the drag at maximum speed and may exceed the upward authority. [P-DYN-100] = 5 m² and D66 stand. **Q3 (G2-F06):** isotropic drag meets D18: motion along one axis gives drag along that axis only; the shared airspeed magnitude in oblique flow is accepted (recorded in D64 and MS-DYN §4.5). **Q4 (G2-F18):** [P-SYS-290] is the anchor of [P-FU-040], [P-FU-050] and [P-SYS-280] only, not a requirement; a change of [P-DYN-100] at I1 re-derives them (TT-110, TT-750, TT-800). The Minor and Editorial findings are accepted as recommended; C1 and C2 apply them with the D69 rework after B3. |

### Open questions

All open and deferred questions are tracked as GitHub issues labelled `questions` (`deferred` marks those the owner has parked). The issue number is the permanent ID.

| ID | Question | When | Proposal |
| --- | --- | --- | --- |
| Q5 (#6) | **Mode combinations.** Which modes can be active together? | G1 | **Answered (D56):** one horizontal and one vertical mode at a time, independent; Go to hover and Hover govern both. |

## 10. Summary of agents

| Phase | Parallel agents | Models |
| --- | --- | --- |
| 0 | 1 | Sonnet |
| 1 | 3, then a gate | Opus ×3, Haiku, Opus (review) |
| 2 | 1, then 1, then a gate | Opus (xhigh), Sonnet, Haiku, Opus (review) |
| 3 | 8 | Opus ×8 (three at xhigh) |
| 3b | 1, then a gate | Opus (xhigh), Haiku ×8, Opus ×2 (review) |
| 4 | 1, then 5, then a gate | Opus (M0), then Opus ×3 (M3, M8, FC1) and Sonnet ×2 (M2, M5), Haiku, Opus (review) |
| 5 | 4, then a gate | Sonnet ×4, Opus (review) |

The critical path runs G0 → B1 → G1 → C5 → I1 → G2 → M0 → M3/M8 → G3 → G4. The largest time savings come from the parallel fan-outs in Phases 3, 4 and 5.
