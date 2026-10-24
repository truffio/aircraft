# Aeronef Project — Aircraft Requirements Definition Plan

**Status:** Draft plan, not started
**Date:** 2026-10-24
**Branch:** `aircraftDef`

## 1. Purpose and scope

This plan organises the work of defining the requirements of the **Aeronef** (element `AER`), starting from [AIRCRAFT_CHARACTERISTICS.md](AIRCRAFT_CHARACTERISTICS.md) and following [METHODOLOGY.md](METHODOLOGY.md). It describes the phases, the parallel sub-agents that carry them out, the model and effort each one uses, and the gates between phases. It does not start the definition itself.

**In scope**

- The L0 statements the Aeronef traces to (objectives, constraints, success criteria), plus the ConOps scenarios and conventions the vehicle requirements need.
- The L1 Aeronef System Requirements Specification.
- L2 subsystem requirements: dynamics, effectors, fuel and mass properties, flight control, autoflight, and operational data output.
- L3 and L4 where a branch needs them, mainly flight control and autoflight.
- The model specification (MS-DYN), the parameter database, and the Aeronef side of the interface control documents.
- Verification planning: a method, a procedure ID and success criteria for every requirement.

**Out of scope for this plan**

- Hazard and failure analysis, which is deferred per the tailoring note in METHODOLOGY.md. Criticality is set to "Not assessed", and no Safety-type requirements or fault-injection requirements are written.
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

## 3. Proposed output layout

Each sub-agent writes only the files it owns. Shared files are owned by the orchestrator (Section 5).

```
requirements/
  L0/L0_REQUIREMENTS.md            L0-OBJ / L0-CON / L0-SUC statements + assumptions register
  L1/AER_SRS.md                    Aeronef L1 system requirements
  L2/AER_DYN.md                    Dynamics model
  L2/AER_EF.md                     Effectors
  L2/AER_FU.md                     Fuel and mass properties
  L2/AER_FC.md                     Flight control (with L3 TR, RO, AL sections or files)
  L2/AER_AF.md                     Autoflight (mode catalogue, mode logic)
  L3/AER_AF_<MODE>.md              One file per autoflight mode
  L2/AER_TM.md                     Operational data output (telemetry)
specs/
  CONOPS.md                        Stakeholders, needs, scenarios (Aeronef-relevant)
  CONVENTIONS.md                   Frames, axes, signs, units, time base
  GLOSSARY.md                      Defined terms
  MS-DYN.md                        Model specification: equations of motion, gravity, drag, mass, inertia
  FUNCTIONAL_ANALYSIS.md           Function list, N² matrix, control-loop flow
  AF_MODE_LOGIC.md                 State-transition diagram and decision tables
icd/
  ICD-AER-STP.md                   Aeronef ↔ STP (Aeronef side)
  ICD-FC-AF.md                     Flight control ↔ autoflight
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
tools/
  (lint, trace-check and matrix scripts)
work/<agent-id>/                   Staging: proposals, interface needs, issues (not baselined)
```

Requirement records use the Markdown template in METHODOLOGY 13.3, one block per requirement. The parameter database is YAML so scripts can read it.

## 4. Model and effort policy

| Model | Use it for | Default effort |
| --- | --- | --- |
| **Opus** | Primary authoring of requirement sets and specifications; the highest-leverage judgement (L1 architecture and allocation, the autoflight mode concept); independent gate reviews. | high; xhigh for the L1 architecture, the autoflight core, and mathematical or control-heavy work (MS-DYN, flight control) |
| **Sonnet** | Pattern-following authoring once a reference exists, verification planning, tooling scripts, integration bookkeeping. | medium–high |
| **Haiku** | Mechanical checks against the METHODOLOGY 13.1 checklist: one "shall", vague terms, missing attributes, ID format. | low–medium |

Two rules apply throughout:

1. **Independence.** A reviewer is never the agent that authored the artifact. Each gate review uses a fresh Opus / high instance that receives only the artifacts, their inputs and the checklists, never the author's working notes or conversation.
2. **Escalation.** If a Sonnet or Haiku agent reports low confidence or finds a design question, the item goes back to the orchestrator. It is not resolved at the lower tier.

## 5. Roles

| Role | Who | Responsibilities |
| --- | --- | --- |
| **Project owner** | Martin | Decides open questions, approves each gate, owns the baselines. |
| **Orchestrator** | Main Claude Code session | Launches agents, owns the shared files (parameter database, glossary, ICDs, registers), merges staging proposals, runs scripts, commits, prepares gate packages. |
| **Author agents** | Sub-agents, Sections 6–7 | Write the requirement sets they are assigned. They do not edit shared files; they propose changes in `work/<agent-id>/`. |
| **Reviewer agents** | Sub-agents, Section 8 | Lint and inspect. They raise findings and do not fix artifacts. |

Each author agent runs with `isolation: "worktree"` and returns:

- its owned files;
- `work/<agent-id>/param_proposals.md`, with new parameters and their units, values or TBD;
- `work/<agent-id>/interface_needs.md`, with data it needs from, or provides to, other subsystems;
- `work/<agent-id>/glossary_proposals.md`;
- `work/<agent-id>/issues.md`, with change requests to the parent level, conflicts and questions for the project owner.

## 6. Phases

Phases run in sequence. Agents within a phase run in parallel unless marked otherwise.

### Phase 0 — Setup

| ID | Task | Model / effort | Depends on |
| --- | --- | --- | --- |
| T0 | Orchestrator creates the folder layout, empty registers, the parameter-database skeleton and the requirement template. | Orchestrator | Open decisions D1–D2 (Section 9) |
| T1 | Tooling agent writes the scripts: requirement parser, METHODOLOGY 13.1 lint (vague terms, escape clauses, multiple "shall", missing attributes), trace check (orphans, childless parents, requirements without a verification method), VCRM generator, parameter-reference check. | Sonnet / medium | T0 |

T1 runs in parallel with Phase 1.

### Phase 1 — L0 and foundations

| ID | Task | Outputs | Model / effort |
| --- | --- | --- | --- |
| A1 | Write the L0 requirements from OBJECTIVES.md and the modelling boundaries in AIRCRAFT_CHARACTERISTICS.md §7. Cover objectives (L0-OBJ), constraints as Constraint-type requirements (L0-CON: no lift or control surfaces, fixed CG, no electrical system, fictional effectors), success criteria (L0-SUC), and an assumptions register with owners (perfect state knowledge, for example). | `requirements/L0/L0_REQUIREMENTS.md` | Opus / high |
| A2 | Identify stakeholders and needs (METHODOLOGY 4.1) and write the Aeronef-relevant ConOps scenarios: hold position and attitude, translate at constant attitude, rotate in place, reference mission to fuel exhaustion. No failure scenarios. | `specs/CONOPS.md` | Opus / high |
| A3 | Propose axis and sign conventions per AIAA R-004 (body frame, local reference frame, Euler-angle sequence, units, time base) and seed the glossary. Present the alternatives that matter (for example NED versus ENU) with a recommendation. | `specs/CONVENTIONS.md`, `specs/GLOSSARY.md` | Opus / high |

**Gate G0 — L0 mission and concept review**

- Haiku / low lints A1 against the checklist.
- Opus / high inspects A1–A3 together for consistency, coverage of the objectives and conflicts.
- The project owner decides the conventions and approves the baseline.
- Exit: no open major findings, conventions fixed, L0 baselined and tagged `L0-baseline-1`.

### Phase 2 — Aeronef functional analysis, L1 and allocation

This phase is one agent, because L1 coherence matters more than speed here.

| ID | Task | Outputs | Model / effort |
| --- | --- | --- | --- |
| B1 | Refine the Aeronef function list (F-AER-01 to 08, plus a function for producing operational data). Build the N² interface matrix and the control-loop flow. Write the L1 Aeronef SRS: functional, performance, interface, constraint, model-fidelity and documentation types. Choose the logical architecture and allocate every L1 requirement to an L2 subsystem (DYN, EF, FU, FC, AF, TM). Set the top-level budgets (fuel, effector authority, position error, timing) and propose the initial autoflight mode catalogue for v1, with a short rationale per mode, adapting airliner modes to independent 6-DOF control. | `specs/FUNCTIONAL_ANALYSIS.md`, `requirements/L1/AER_SRS.md`, staging files | Opus / xhigh |
| B2 | Runs after B1. Seed the parameter database from B1's proposals: assign P-xx-nnn IDs, units and TBD/TBR status. Open the TBD/TBR register entries. | `parameters/PARAMETERS.yaml`, `registers/TBD_TBR.md` | Sonnet / medium |

**Gate G1 — System Requirements Review (Aeronef)**

- Haiku / low runs the lint and the trace check (every L1 requirement has an L0 parent or is flagged Derived).
- Opus / high, as a fresh instance and not B1, inspects sufficiency against L0, the allocation and the budgets.
- The project owner approves the mode catalogue and the L1 baseline.
- Exit: L1 baselined and tagged `AER-L1-baseline-1`, mode catalogue frozen for this cycle.

### Phase 3 — L2 subsystem requirements (main parallel fan-out)

Six agents run in parallel. Each agent:

- reads L0, L1, CONVENTIONS, GLOSSARY, PARAMETERS and the relevant parts of METHODOLOGY;
- writes the L2 requirements for its subsystem, with the full attributes of METHODOLOGY 9.2 and a sufficiency argument per L1 parent;
- states the verification method;
- references parameters by ID and never writes numbers in sentences;
- flags derived requirements and records their design decisions as DD proposals.

| ID | Subsystem | Notes | Model / effort |
| --- | --- | --- | --- |
| C1 | **DYN** — dynamics model | Also writes `specs/MS-DYN.md`: 6-DOF rigid-body equations, gravity model, drag model, integration requirements, and the independent analytical checks for credibility (free fall, terminal velocity, torque-free rotation, fuel-mass integral; METHODOLOGY 10.3). | Opus / xhigh |
| C2 | **FU** — fuel and mass properties | Fuel quantity, consumption for linear and rotational actuation (configurable), mass decrease, fixed CG, inertia assignment and how it changes with fuel. Fuel exhaustion is nominal behaviour, not a failure. | Opus / high |
| C3 | **EF** — effectors | Fixed-direction emitters: authority per axis, limits, command response, consumption interface to FU. Stays solution-free: the emitter layout is a design decision, not a requirement. | Opus / high |
| C4 | **FC** — flight control | L2, plus L3 sections for translational control (TR), rotational control (RO) and control allocation (AL). Includes independent per-axis regulation, saturation handling as nominal behaviour, and the constraint that control laws are swappable without changing the vehicle model (objective: compare control laws). | Opus / xhigh |
| C5 | **AF** — autoflight core | Writes the L2 autoflight requirements and `specs/AF_MODE_LOGIC.md` (state-transition diagram and decision tables for engagement, transitions and annunciation), the guidance framework and annunciation principles. Per-mode details are left to Phase 4. | Opus / xhigh |
| C6 | **TM** — operational data output | Signals the Aeronef exposes so inputs, mode changes, control activity and responses can be correlated (REVERSE_ENGINEERING §3C, TESTING_ENVIRONMENT §8). Each signal is classified as *releasable* or *protected*, so telemetry does not leak protected design. | Opus / high |

C1–C3 are closely coupled (mass, inertia, effector forces, consumption). They do not coordinate directly; they record needs in `interface_needs.md` and the integration step resolves them.

### Phase 3b — Integration (sequential)

| ID | Task | Model / effort |
| --- | --- | --- |
| I1 | Merge all staging proposals: the parameter database, glossary and DD register. Write `icd/ICD-AER-STP.md` (Aeronef side: state vector, effector commands, operational data, frame rate, units) and `icd/ICD-FC-AF.md`. Resolve cross-subsystem conflicts, check that the budgets close, and turn unresolved conflicts into change requests at L1 or questions for the project owner. | Opus / xhigh |
| I2 | Re-run the parameter-reference check and the trace check. | Orchestrator (scripts) |

**Gate G2 — Subsystem requirements review**

- Six Haiku / low lint agents run in parallel, one per file.
- Two Opus / high inspectors run in parallel: one for DYN, FU and EF plus MS-DYN (physics consistency), and one for FC, AF and TM plus the ICDs (control and data consistency).
- The project owner approves.
- Exit: L2 baselined and tagged `AER-L2-baseline-1`.

### Phase 4 — L3/L4 deepening (second fan-out)

The number of agents depends on the mode catalogue frozen at G1.

| ID | Task | Model / effort |
| --- | --- | --- |
| D0 | Write the **reference mode**, Position Hold (the METHODOLOGY §12 worked example): L3 requirements for capture, hold and annunciation, the derived L4 software high-level requirements where needed, and the flow-down to FC and EF. This sets the pattern for the other modes. | Opus / high |
| D1…Dn | Runs after D0. One agent per remaining mode (for example attitude hold, translate to waypoint, rotate to attitude), following D0's pattern and the mode logic in AF_MODE_LOGIC. Any mode that departs significantly from the pattern is escalated to Opus / high. | Sonnet / high |
| D-FC | Deepen FC L3 (TR, RO, AL) to L4 where a single owner cannot yet implement and verify without interpretation. This includes the allocation priority rule as a derived requirement with its DD entry. Runs in parallel with D1…Dn. | Opus / high |

**Gate G3 — Low-level requirements review**

- Haiku / low lints each file.
- Opus / high runs one inspection across all modes, checking that the mode files agree with the mode logic and with each other.
- The project owner approves.

### Phase 5 — Verification planning (third fan-out)

There is one agent per subsystem file group, run in parallel. For every requirement, the agent writes:

- the method (Inspection, Analysis, Demonstration or Test);
- the procedure ID (TP-, AN-, DM- or IN-nnn);
- success criteria stated before the work, per METHODOLOGY 9.3 and 10.2.

Physics requirements are verified by analysis against independent solutions, and functional and performance requirements by automated STP tests. The agents add nominal and boundary cases; robustness cases tied to failures are deferred.

| ID | Scope | Model / effort |
| --- | --- | --- |
| V1 | DYN, FU, EF and MS-DYN | Sonnet / high |
| V2 | FC (all levels) | Sonnet / high |
| V3 | AF (all levels, all modes) | Sonnet / high |
| V4 | TM, ICDs, L1 and L0 | Sonnet / high |
| V5 | Runs after V1–V4. Generate `verification/VCRM.md` with the script and check that no requirement lacks a method. | Orchestrator (scripts) |

**Gate G4 — Verification plan inspection and requirements baseline**

- Opus / high runs the inspection, which checks that the success criteria are measurable and that the procedures are written from the requirement and not from a design.
- The trace checks must pass: no orphans, no childless parents, no requirement without a verification method.
- The project owner approves the complete Aeronef requirements baseline, tagged `AER-REQ-baseline-1`.

## 7. Standard brief for every author agent

Each agent prompt contains the following:

1. **Role and the exact files it owns.** It must not edit any other file.
2. **Inputs to read**, with paths, including the relevant METHODOLOGY sections (8 writing rules, 9 attributes, 13 checklists and template).
3. **Tailoring reminders.** Hazards are deferred, Criticality is "Not assessed", and the Safety type is not used.
4. **Writing rules.**
   - Use EARS patterns, one "shall" per requirement.
   - Use parameter IDs instead of numbers, SI units, and terms from the glossary only.
   - Write the rationale at the same time as each requirement, with a sufficiency argument per parent.
5. **ID scheme** (METHODOLOGY 9.1). Number in steps of 10, and never reuse an ID.
6. **Information separation.** All design artifacts are protected. Nothing in the outputs is written as operator-facing manual text, and the TM agent marks each signal releasable or protected.
7. **Hand-back.** The agent returns its owned files, its staging files (Section 5), a self-check against METHODOLOGY 13.1, and a short summary: counts per type, open TBD/TBR, derived requirements, and questions for the project owner.

## 8. Reviews

| Check | Tool | When |
| --- | --- | --- |
| Lint (METHODOLOGY 13.1 mechanical items) | Script plus Haiku / low | Every gate, per file |
| Trace and parameter-reference checks | Scripts | Every gate, and after each integration |
| Inspection (METHODOLOGY 13.2, sufficiency, consistency) | Opus / high, fresh instance, never the author | G0–G4 |
| Approval | Project owner | Every gate |

Findings are recorded with the METHODOLOGY 13.4 template in `reviews/`. Authors rework, and the orchestrator confirms closure before the baseline tag.

## 9. Open decisions before starting

| ID | Decision | Recommendation |
| --- | --- | --- |
| D1 | Requirement storage format | Markdown blocks per METHODOLOGY 13.3, with the parameter database in YAML |
| D2 | Repository layout and separation | Layout in Section 3 in this repo for now. A separate repo for REE-released material when manuals start. |
| D3 | Size of the v1 autoflight mode catalogue | Four to six modes, proposed by B1 and decided at G1 |
| D4 | Depth for this cycle | Through L4 for AF and FC only where needed. Other branches stop at L2 or L3. |
| D5 | Scripting language for tools | Python |
| D6 | Owner attribute | Martin for all requirements in this cycle |

## 10. Summary of agents

| Phase | Parallel agents | Models |
| --- | --- | --- |
| 0 | 1 | Sonnet |
| 1 | 3, then a gate | Opus ×3, Haiku, Opus (review) |
| 2 | 1, then 1, then a gate | Opus (xhigh), Sonnet, Haiku, Opus (review) |
| 3 | 6 | Opus ×6 (three at xhigh) |
| 3b | 1, then a gate | Opus (xhigh), Haiku ×6, Opus ×2 (review) |
| 4 | 1, then n + 1, then a gate | Opus, Sonnet ×n, Opus, Haiku, Opus (review) |
| 5 | 4, then a gate | Sonnet ×4, Opus (review) |

The critical path runs G0 → B1 → G1 → C4/C5 → I1 → G2 → D0 → G3 → G4. The largest time savings come from the parallel fan-outs in Phases 3, 4 and 5.
