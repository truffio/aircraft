# Aeronef Project — Aircraft Requirements Definition Plan

**Status:** Draft plan, not started
**Date:** 2026-10-24
**Branch:** `aircraftDef`

## 1. Purpose and scope

This plan organises the work of defining the requirements of the **Aeronef** (element `AER`), starting from [AIRCRAFT_CHARACTERISTICS.md](AIRCRAFT_CHARACTERISTICS.md) and following [METHODOLOGY.md](METHODOLOGY.md). It describes the phases, the parallel sub-agents that carry them out, the model and effort each one uses, and the gates between phases. It does not start the definition itself.

**In scope**

- The L0 statements the Aeronef traces to (objectives, constraints, success criteria), plus the ConOps scenarios and conventions the vehicle requirements need.
- The L1 Aeronef System Requirements Specification.
- L2 subsystem requirements: dynamics, effectors, fuel and mass properties, flight control, autoflight, navigation, and operational data output.
- Lower levels wherever a branch needs them, down to the last layer that is still a requirement (Section 9, D4).
- The autoflight mode catalogue in Section 9, D3.
- The model specification (MS-DYN), the parameter database, and the Aeronef side of the interface control documents.
- Verification planning: a method, a procedure ID and success criteria for every requirement.

**Out of scope for this plan**

- Hazard and failure analysis, which is deferred per the tailoring note in METHODOLOGY.md. Criticality is set to "Not assessed", and no Safety-type requirements or fault-injection requirements are written.
- Implementation: design descriptions, algorithms, software low-level requirements and code structure. Decomposition stops at the layer above them.
- Requirements for the Simulation and Testing Platform (STP) and the Reverse-Engineering Effort (REE), except the Aeronef side of shared interfaces.
- Operational manuals. They come after the requirements baseline. This plan only keeps the requirements in a state that manuals can trace to.
- Test procedure implementation. This plan names procedures and success criteria; the STP writes and runs them later.
- Manual control. It is recorded as an optional feature (EARS "Where" pattern) and is not developed.

## 2. Inputs

| Input | Used for |
| --- | --- |
| OBJECTIVES.md | L0 objectives and success criteria |
| AIRCRAFT_CHARACTERISTICS.md | Vehicle concept, modelling boundaries, constraints |
| TESTING_ENVIRONMENT.md | Interface needs toward the STP, data-collection needs |
| REVERSE_ENGINEERING.md | Constraints on operational data output (observable, but must not leak protected design) |
| METHODOLOGY.md | Process, writing rules, attributes, ID scheme, checklists, templates |

## 3. Output layout

All requirements live in one folder, `requirements/`, with **one file per level**. Inside each level file, there is one section per element or subsystem, in a fixed order: DYN, FU, EF, FC, AF, NAV, TM.

```
requirements/
  L0.md                            L0-OBJ / L0-CON / L0-SUC statements + assumptions register
  L1.md                            Aeronef system requirements
  L2.md                            Subsystems: DYN, FU, EF, FC, AF, NAV, TM
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
  ICD-AER-STP.md                   Aeronef ↔ STP (Aeronef side)
  ICD-FC-AF.md                     Flight control ↔ autoflight
  ICD-NAV-AF.md                    Navigation ↔ autoflight
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

**Gate G1 — System Requirements Review (Aeronef)**

- Haiku / low runs the lint and the trace check (every L1 requirement has an L0 parent or is flagged Derived).
- Opus / high, as a fresh instance and not B1, inspects sufficiency against L0, the allocation, the budgets and the mode grouping.
- The project owner answers Q5 and approves the L1 baseline.
- Exit: L1 baselined and tagged `AER-L1-baseline-1`.

### Phase 3 — L2 subsystem requirements (main parallel fan-out)

Seven agents run in parallel. Each agent:

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
| C5 | **AF** — autoflight core | Writes the L2 autoflight section and `specs/AF_MODE_LOGIC.md`. The mode logic covers mode groups and compatible combinations, armed versus active states (altitude capture, VOR radial capture), engagement, automatic transitions (for example climb → altitude capture → altitude hold), disengagement, annunciation, target selection, and what the attitude axes do in each mode (D10). Per-mode details are left to Phase 4. | Opus / xhigh |
| C6 | **NAV** — navigation | Navigation references used by autoflight: position, altitude, heading, track, horizontal and vertical speed, flight path angle, and the simulated VOR function (station definition, radial and deviation computation, reception limits per D12). | Opus / high |
| C7 | **TM** — operational data output | Signals the Aeronef exposes so inputs, mode changes, control activity and responses can be correlated (REVERSE_ENGINEERING §3C, TESTING_ENVIRONMENT §8). Includes the selected targets, armed and active modes, and annunciations. Each signal is classified as *releasable* or *protected*, so telemetry does not leak protected design. | Opus / high |

C1–C3 are closely coupled (mass, inertia, effector forces, consumption), as are C5 and C6 (navigation data used by the modes). Coupled agents do not coordinate directly; they record needs in `interface_needs.md` and the integration step resolves them.

### Phase 3b — Integration (sequential)

| ID | Task | Model / effort |
| --- | --- | --- |
| I1 | Assemble `requirements/L2.md` from the drafts. Merge all staging proposals: the parameter database, glossary and DD register. Write `icd/ICD-AER-STP.md` (Aeronef side: state vector, effector commands, operational data, frame rate, units), `icd/ICD-FC-AF.md` and `icd/ICD-NAV-AF.md`. Resolve cross-subsystem conflicts, check that the budgets close, and turn unresolved conflicts into change requests at L1 or questions for the project owner. | Opus / xhigh |
| I2 | Re-run the parameter-reference check and the trace check. | Orchestrator (scripts) |

**Gate G2 — Subsystem requirements review**

- Seven Haiku / low lint agents run in parallel, one per L2 section.
- Two Opus / high inspectors run in parallel: one for DYN, FU and EF plus MS-DYN (physics consistency), and one for FC, AF, NAV and TM plus the ICDs (control, guidance and data consistency).
- The project owner approves.
- Exit: L2 baselined and tagged `AER-L2-baseline-1`.

### Phase 4 — Lower-level requirements (second fan-out)

There is one L3 section per autoflight mode, plus the flight-control deepening. Each agent decomposes its branch until the next layer would be implementation (D4). If that point is not reached at L3, the agent continues into the next level file.

| ID | Mode or branch | Model / effort |
| --- | --- | --- |
| M0 | **Position Hold**, the reference mode and the METHODOLOGY §12 worked example: engagement and position capture, hold accuracy, annunciation, disengagement, and the flow-down to FC and EF. This sets the pattern for the other modes. | Opus / high |

These run in parallel after M0:

| ID | Mode or branch | Model / effort |
| --- | --- | --- |
| M1 | **Climb and descent on flight path angle** | Sonnet / high |
| M2 | **Climb and descent on vertical speed** (selected in feet per minute) | Sonnet / high |
| M3 | **Altitude capture and altitude hold**: arming, capture onset and transition from the climb or descent modes, then hold | Opus / high |
| M4 | **Horizontal speed** | Sonnet / high |
| M5 | **Heading hold** (constant heading) | Sonnet / high |
| M6 | **Track hold** (constant track) | Sonnet / high |
| M7 | **VOR radial tracking**: arming, intercept, capture and tracking | Opus / high |
| M8 | **Hover at altitude** | Sonnet / high |
| FC1 | **Flight-control deepening**: TR, RO and AL to the last requirement layer, including the allocation priority rule as a derived requirement with its DD entry | Opus / high |

M3 and M7 use Opus because arming, capture and transition logic is the subtlest part of the catalogue. Any Sonnet mode that departs significantly from the M0 pattern is escalated to Opus / high. The orchestrator then assembles `requirements/L3.md`, and any lower level file.

**Gate G3 — Lower-level requirements review**

- Haiku / low lints each section.
- Opus / high runs one inspection across all modes. It checks that the mode sections agree with AF_MODE_LOGIC and with each other: the transitions, compatible combinations and annunciations match, and there are no gaps between climb or descent, capture and hold.
- The project owner approves.

### Phase 5 — Verification planning (third fan-out)

There is one agent per group of sections, run in parallel. For every requirement, the agent writes:

- the method (Inspection, Analysis, Demonstration or Test);
- the procedure ID (TP-, AN-, DM- or IN-nnn);
- success criteria stated before the work, per METHODOLOGY 9.3 and 10.2.

Physics requirements are verified by analysis against independent solutions, and functional and performance requirements by automated STP tests. The agents add nominal and boundary cases; robustness cases tied to failures are deferred.

| ID | Scope | Model / effort |
| --- | --- | --- |
| V1 | DYN, FU, EF and MS-DYN | Sonnet / high |
| V2 | FC (all levels) | Sonnet / high |
| V3 | AF and NAV (all levels, all modes) | Sonnet / high |
| V4 | TM, ICDs, L1 and L0 | Sonnet / high |
| V5 | Runs after V1–V4. Generate `verification/VCRM.md` with the script and check that no requirement lacks a method. | Orchestrator (scripts) |

**Gate G4 — Verification plan inspection and requirements baseline**

- Opus / high runs the inspection, which checks that the success criteria are measurable and that the procedures are written from the requirement and not from a design.
- The trace checks must pass: no orphans, no childless parents, no requirement without a verification method. L0 requirements allocated only to STP or REE are not counted as childless (D44).
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
7. **Information separation.** All design artifacts are protected. Nothing in the outputs is written as operator-facing manual text, and the TM agent marks each signal releasable or protected.
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
| D3 | Autoflight mode catalogue | Climb on flight path angle; climb on vertical speed (ft/min); horizontal speed; altitude capture, then altitude hold; descent on flight path angle or vertical speed, similar to climb; heading hold; track hold; VOR radial tracking; position hold; hover at altitude |
| D4 | Depth | No fixed depth. Each branch is decomposed until the next layer would be the implementation. |
| D5 | Scripting language for tools | Python |
| D6 | Owner attribute | Martin for all requirements in this cycle |
| D7 | Crew-facing units | North American aviation units for everything the crew selects or sees: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track, flight path angle, radials). Requirements and the model stay in SI; conversions are fixed in CONVENTIONS. |
| D8 | Ground (#50; refined by D37) | The Earth is flat with no terrain, and altitude zero is ground level. Contact with the ground outside the landing envelope is a crash (D37). |
| D9 | Crew-facing fuel unit (#51) | Pounds (lb) |
| D10 | Attitude during guidance modes (#3, Q2) | Pitch and roll stay level. The Aeronef doesn't need to pitch or roll to move. Those manoeuvres are possible but serve no purpose, because the axes are uncoupled. |
| D11 | Hover versus position hold (#4, Q3) | Position hold is a lateral mode. The vehicle stops moving on all axes (zero velocity, zero acceleration) and holds its position at any altitude, compensating for wind. Hover is a vertical mode. When it engages, the vehicle descends from its current altitude to the altitude set on the flight control panel, then holds position. Hover therefore needs position hold. Whether position is held from the moment hover engages, or only after the velocity has come down to zero, is still open (#78). |
| D12 | VOR model (#5, Q4) | Ideal VOR: the simplest model. Ground stations are at fixed positions in the local frame, radials refer to true north, there is no magnetic variation or noise, and the signal is ideal within the reception range. |
| D13 | Mode compatibility (#61) | A flight-path-angle vertical mode needs horizontal velocity, so it can't be combined with position hold. Detailed design (#6) will produce a compatibility matrix of lateral modes, vertical modes and speed selection. |
| D14 | VOR tracking (#53) | The crew flies a course. Tracking a radial is a track over the ground, and flying TO or FROM the station changes the course flown. |
| D15 | Mode logic versus controllers (#72) | The modes say how the aircraft flies; the controllers implement them, so the two are decoupled. Every control-law version and autoflight implementation must meet the same mode logic, so any implementation pairs with any law. |
| D16 | Mode engagement rule (#78) | When the crew selects a mode, it normally arms first and engages once its engagement conditions are met. While the mode is armed, the active mode manoeuvres the craft into those conditions. Manoeuvres are g-limited: maximum acceleration and deceleration are design parameters. This covers, for example, climb or descent sequencing to altitude hold, and motion sequencing to position hold. |
| D17 | Wind (#49) | Wind exists and can be configured in the test environment. Position hold compensates for wind. |
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
| D33 | Levels and where modes are defined (#80) | L0 is the project, and the aircraft is a black box at L0. L1 is the project's components: the aircraft (AER), the test environment (STP) and the reverse-engineering effort (REE). This plan writes only the AER branch of L1. L2 divides a component into its subsystems. Modes, guidance, mode logic and control-law implementation are defined at L2 (AF, FC), not at L0 or L1. |
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
| D44 | STP and REE branches (#93, G0-F12) | This plan covers the Aeronef branch only. The plan will be extended later to the simulation and testing platform (STP) and the reverse-engineering effort (REE). Until then, L0 requirements allocated only to STP or REE have no children by design: the trace check and the G1–G4 trace exits do not count them as childless, and they are verified by roll-up once their branch exists. |

### Open questions

All open and deferred questions are tracked as GitHub issues labelled `questions` (`deferred` marks those the owner has parked). The issue number is the permanent ID.

| ID | Question | When | Proposal |
| --- | --- | --- | --- |
| Q5 (#6) | **Mode combinations.** Which modes can be active together? | G1 | Airliner-style groups: one vertical mode, one lateral mode and one speed mode at a time. Position hold and hover replace the vertical and lateral groups while active. |

## 10. Summary of agents

| Phase | Parallel agents | Models |
| --- | --- | --- |
| 0 | 1 | Sonnet |
| 1 | 3, then a gate | Opus ×3, Haiku, Opus (review) |
| 2 | 1, then 1, then a gate | Opus (xhigh), Sonnet, Haiku, Opus (review) |
| 3 | 7 | Opus ×7 (three at xhigh) |
| 3b | 1, then a gate | Opus (xhigh), Haiku ×7, Opus ×2 (review) |
| 4 | 1, then 9, then a gate | Opus (M0), then Opus ×3 (M3, M7, FC1) and Sonnet ×6, Haiku, Opus (review) |
| 5 | 4, then a gate | Sonnet ×4, Opus (review) |

The critical path runs G0 → B1 → G1 → C5 → I1 → G2 → M0 → M3/M7 → G3 → G4. The largest time savings come from the parallel fan-outs in Phases 3, 4 and 5.
