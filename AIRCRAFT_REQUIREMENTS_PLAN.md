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
| B1 | Refine the Aeronef function list (F-AER-01 to 08, plus functions for navigation and for producing operational data). Build the N² interface matrix and the control-loop flow. Write the L1 Aeronef SRS: functional, performance, interface, constraint, model-fidelity and documentation types. Choose the logical architecture and allocate every L1 requirement to an L2 subsystem (DYN, FU, EF, FC, AF, NAV, TM). Set the top-level budgets (fuel, effector authority, position error, timing). Take the D3 catalogue as given: write one L1 requirement per mode, and organise the modes into groups (vertical, lateral, speed, hold) that can be active together. Propose answers to questions Q2–Q5 for the project owner. | `specs/FUNCTIONAL_ANALYSIS.md`, draft `L1` section → `requirements/L1.md`, staging files | Opus / xhigh |
| B2 | Runs after B1. Seed the parameter database from B1's proposals: assign P-xx-nnn IDs, units and TBD/TBR status. Open the TBD/TBR register entries. | `parameters/PARAMETERS.yaml`, `registers/TBD_TBR.md` | Sonnet / medium |

**Gate G1 — System Requirements Review (Aeronef)**

- Haiku / low runs the lint and the trace check (every L1 requirement has an L0 parent or is flagged Derived).
- Opus / high, as a fresh instance and not B1, inspects sufficiency against L0, the allocation, the budgets and the mode grouping.
- The project owner answers Q2–Q5 and approves the L1 baseline.
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
| C5 | **AF** — autoflight core | Writes the L2 autoflight section and `specs/AF_MODE_LOGIC.md`. The mode logic covers mode groups and compatible combinations, armed versus active states (altitude capture, VOR radial capture), engagement, automatic transitions (for example climb → altitude capture → altitude hold), disengagement, annunciation, target selection, and what the attitude axes do in each mode (Q2). Per-mode details are left to Phase 4. | Opus / xhigh |
| C6 | **NAV** — navigation | Navigation references used by autoflight: position, altitude, heading, track, horizontal and vertical speed, flight path angle, and the simulated VOR function (station definition, radial and deviation computation, reception limits per Q4). | Opus / high |
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
- The trace checks must pass: no orphans, no childless parents, no requirement without a verification method.
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

### Decided (2026-10-24)

| ID | Decision | Outcome |
| --- | --- | --- |
| D1 | Requirement storage format | Markdown blocks per METHODOLOGY 13.3; parameter database in YAML |
| D2 | Requirement layout | One file per requirement level, all in `requirements/` (Section 3) |
| D3 | Autoflight mode catalogue | Climb on flight path angle; climb on vertical speed (ft/min); horizontal speed; altitude capture, then altitude hold; descent on flight path angle or vertical speed, similar to climb; heading hold; track hold; VOR radial tracking; position hold; hover at altitude |
| D4 | Depth | No fixed depth. Each branch is decomposed until the next layer would be the implementation. |
| D5 | Scripting language for tools | Python |
| D6 | Owner attribute | Martin for all requirements in this cycle |
| D7 | Crew-facing units | North American aviation units for everything the crew selects or sees: ft (altitude), ft/min (vertical speed), kt (speed), NM (distance), degrees (heading, track, flight path angle, radials). Requirements and the model stay in SI; conversions are fixed in CONVENTIONS. |

### Open questions

| ID | Question | When | Proposal |
| --- | --- | --- | --- |
| Q2 | **Attitude during the guidance modes.** The modes set heading and the flight path, but the Aeronef's pitch and roll are independent of its motion. What do pitch and roll do while these modes are active? | G1 | Pitch and roll are held level by default in every mode, with heading set by the lateral mode or held |
| Q3 | **Hover at altitude versus position hold.** How do they differ? | G1 | Position hold keeps a 3-D position. Hover at altitude keeps altitude and zero horizontal velocity, without holding a horizontal position, so the vehicle may drift. |
| Q4 | **VOR model.** What fidelity is wanted? | G1 | Ground stations at fixed positions in the local frame, radials referenced to true north, no magnetic variation, an ideal signal within a reception range, and no noise in v1 |
| Q5 | **Mode combinations.** Which modes can be active together? | G1 | Airliner-style groups: one vertical mode, one lateral mode and one speed mode at a time. Position hold and hover replace the vertical and lateral groups while active. |

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
