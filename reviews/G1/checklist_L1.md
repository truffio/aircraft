# G1 checklist review: requirements/L1.md

- **Artifact:** requirements/L1.md (84 `req` records; 4 Deleted skipped: L1-AER-230, -340, -540, -550; 80 checked, all Draft)
- **Checklist:** METHODOLOGY §13.1 (single requirement), judgement items only; §13.2 not in scope here. Decisions D1 to D58 (AIRCRAFT_REQUIREMENTS_PLAN §9) and specs/GLOSSARY.md applied.
- **Date:** 2026-11-04
- **Reviewer:** Haiku checklist pass
- **Tool results:**
  - `python tools/lint.py`: 0 errors, 62 warnings. 17 warnings are on L0 (already decided in reviews/G0/checklist_L0.md); 45 warnings are on L1 (43 records), decided in section 2.
  - `python tools/trace_check.py`: 67 errors, all accepted at G1: 65 CHILDLESS (all L1 records allocated to subsystems, no L2 yet) and 2 DERIVED (L1-AER-680 for DD-010, L1-AER-710 for DD-020).
- **Accepted without finding:** statements contain no literal numbers (quantities are parameter IDs); all Allocated-to records use the roll-up method and all `Allocated to: —` leaves use their own direct method (D58); all records are Owner Martin (D6). Criticality "Not assessed" is the documented METHODOLOGY §6 and §13.1 hazard deferral, so it is not a finding.

Skipped (Deleted): L1-AER-230, L1-AER-340, L1-AER-540, L1-AER-550.

## 1. Findings

| ID | Checklist item | Finding | Severity | Suggested fix |
| --- | --- | --- | --- | --- |
| L1-AER-330 | Verification criteria match statement; decisions consistent (D56) | Criterion adds an obligation the statement does not have: "and levels off above the minimum operating altitude". "minimum operating altitude" is not in the glossary. D56 says Vertical speed "arms Altitude hold, so it levels off at the selected altitude", which is not the same. (escalate: design question on where descent levels off.) | Major | Confirm with the owner where a descent levels off. Then either state the levelling in the statement or remove it from the criterion, and align with D56. Define the term if it stays. |
| L1-AER-690 | Statement is testable; decisions consistent (D25) | Statement: "produce identical operational data from an identical configuration, initial condition, crew selection sequence and execution host". D25: "Runs are not checked for bit-identical results ... A repeated run must give the same expected result." The criterion requires identical data on one host, which is bit-identical. (escalate: the owner must decide between bit-identical and verdict-identical.) | Major | Owner decision. If verdicts are the test, use the L0-OBJ-090 fix: "produce the same pass or fail verdicts". If bit-identical data on one host is wanted, say so in D25 and in the statement. |
| L1-AER-360, L1-AER-460 | Terms in glossary; EARS condition explicit | "While holding a fixed position" (-360) and "While autoflight holds a fixed position" (-460). "fixed position" is not in the glossary. The glossary defines the two modes that hold position, *Stationary* (horizontal) and *Hover* (both axes), and the statement's scope depends on which one applies. | Major | Name the modes with glossary terms, for example "While Stationary or Hover is active with ...". Or add "fixed position" to the glossary with a definition. |
| L1-AER-460 | Verification criteria match statement | Statement: "at each output sample that follows the start of the hold by at least [P-SYS-460]". Criterion: "holds in zero wind ... stay within [P-SYS-450]". The criterion has no time gate, so it does not test P-SYS-460. | Minor | "... stay within [P-SYS-450] at each output sample after the start of the hold plus [P-SYS-460]". |
| L1-AER-370 | Verification criteria measurable; no vague terms | Criterion: "a step in the reference of each degree of freedom is followed by that degree of freedom". "followed" has no measure, tolerance or time, and the statement ("regulate ... toward a separate reference") has none either. | Minor | Give a measure: the degree of freedom reaches its reference within a tolerance and time, held as parameters, or cite the L1-AER-380 values. |
| L1-AER-220 | No vague terms; states what, not how | Statement: "from the elongated body shape and the simplified mass distribution stated in MS-DYN". "elongated" and "simplified" are not quantities. This is the same issue as L0-CON-140 (G0 Minor). | Minor | Name the shape parameters with their IDs (for example a length-to-diameter parameter) and name the mass model in MS-DYN. |
| L1-AER-020 | No escape clauses | Statement: "other than the rigid-body kinematic terms that MS-DYN retains". This exception leaves the set open until #81 closes (TBR, Martin, G2). (escalate: design question, #81.) | Minor | Keep the TBR. When #81 closes, list the retained terms in the statement, or cite the MS-DYN section that lists them. |
| L1-AER-450 | Terms in glossary; no unsupported status | "through the autoflight modes of the baselined mode catalogue". The record is Draft and D56 is a plan decision, not a baseline. The glossary says "The baselined list" for *Mode catalogue*. | Minor | Remove "baselined": "through the autoflight modes of the mode catalogue (D56)". |
| L1-AER-640 | No open lists | Statement: "its navigation quantities". The rationale says "The list is closed", but "navigation quantities" is an undefined category. | Minor | List the quantities, as L1-AER-530 does: altitude, horizontal speed, vertical speed, heading, track. |
| L1-AER-530 | Verification criteria self-contained | Criterion: "inside its validity range". The range is not in this record. The rationale says validity thresholds are in CV-580. | Minor | Cite the range in the criterion: "inside the validity range of CV-580". |
| L1-AER-120, L1-AER-140 | Source and rationale accurate (decisions) | Rationale cites "At level attitude (D10)" (-120) and "Pitch and roll are held level (D10)" (-140). D10 is revised by D57, which says pitch and roll are "held at zero at all times". L1-AER-390 already cites D57. | Minor | Cite D57 (which revises D10) in both rationales. |
| L1-AER-390 | Source recorded; question references | Rationale: "(D33, A2-Q03)". Questions are cited by GitHub issue number (#N), not by the work-package code. | Minor | Replace "A2-Q03" with its GitHub issue number. |
| L1-AER-060 | Numbers only as parameter IDs | Rationale: "reads 1 g in a hover exactly". A literal value in the rationale. | Minor | Cite the glossary entry *Sensed acceleration* (1 g in a hover), or the parameter ID, and drop the literal. |
| L1-AER-140 | Vague terms; quantified rationale | Rationale: "with a margin for holding level attitude". The margin is not quantified. | Minor | Give the margin as a parameter or cite its FUNCTIONAL_ANALYSIS §7.1 value. |
| L1-AER-520 | Rationale clear | Rationale: "the flight control panel is as manual as flying the Aeronef gets". The phrase does not state a reason. | Minor | "The flight control panel is the only crew input (L0-CON-180)." |
| L1-AER-830 | Rationale written | Rationale: "(important to the owner)". This is a priority note, not a reason. | Minor | Replace with the reason, for example "OBJECTIVES §1: the assessment of the AI-assisted methods is an objective in its own right". |
| L1-AER-800 | Clear, testable statement | Statement: "down to the last requirement layer of each subsystem branch". "last" is ambiguous (the same issue as L0-SUC-010, G0 Minor). | Minor | "down to the lowest level of each branch defined in the plan (D4)". |
| L1-AER-820 | EARS: timing explicit | Statement: "contribute to the final test report". "final" has no event or time (the same issue as L0-SUC-170, G0 Minor). | Minor | "When the project completes (G4), the Aeronef shall contribute ...". |
| L1-AER-840 | TBD/TBR recorded | Rationale: "Abnormal and emergency procedures are deferred with the hazard analysis." The deferral is not in the TBD/TBR field and has no owner or closure. | Minor | Record a TBR with owner and gate, or "deferred to <issue>", as in the TBD register. |
| L1-AER-630 | TBD/TBR owner and closure | TBD/TBR: "Martin, RVS plan extension (D44)". The closure is not a date or a gate. | Minor | Name a gate or date, for example "G2 (I1)". |
| L1-AER-750 | Single thought (D30) | Statement joins two obligations (one level file per level; each record states its level and its parent or design decision) with "either ... or". The "either ... or" selects between two record forms with different checks. See section 2 (split). | Minor | Split as section 2 proposes: a file-layout requirement, a level requirement, and a parent-or-Derived requirement. |
| L1-AER-750, -760, -780, -800, -810, -820, -830 | Subject is the element at this level (escalate) | Records with `Allocated to: —` state "The Aeronef shall have its requirements ...", "shall have each of its engineering artifacts peer reviewed", "shall pass the automated trace check", "shall contribute to the final test report". These describe project process and documents, not the Aeronef. Whether they belong at L1 is a scope question (D33, D44). (escalate) | Minor | Owner decision: keep them as Aeronef-branch leaves with a subject that is the Aeronef's documents, or move them to the plan and to L0 (process). |
| Systemic: L1-AER-070, -100, -110, -150, -160, -170, -180, -190, -200, -300, -310, -320, -330, -350, -460, -530, -570, -580, -590, -630, -660, -830 | Terms in glossary (GLOSSARY.md) | Used but not defined: "operating volume" (-310, -320, -330, -350); "operating altitude range" (-310 criterion); "vehicle acceleration" (-300); "event record" (-590); "standard atmosphere" (-070); "fuel mass flow" (-160, -630); "dry mass" (-180); "reference mission" (-190, -200, -570, -580); "parameter database" (-110, -150, -170); "reference position" (-460); "control effectiveness", "command response", "output limits" and "consumption parameters" (-100); "mode state" (-660); "AI-assisted methods" (-830); "validity range" (-530). | Minor | Add the entries to specs/GLOSSARY.md, or rephrase each use with a term that is defined. |
| Systemic: L1-AER-060, -300, -450, -470, -570, -670, -680, -710 | Numbers only as parameter IDs (TBD/TBR fields) | The TBD/TBR fields repeat proposed values: "9.806 65 m/s²" (-060), "14.709 975 m/s², 1.5 g" (-300), "1 m" (-450), "0.5 s" (-470), "0.1" (-570), "0.01 s" (-670), "0.02 s" (-680), "0.1 s" (-710). These copies can drift from PARAMETERS.yaml. | Minor | Keep the values in parameters/PARAMETERS.yaml only. The TBD/TBR field should cite the parameter ID and its status. |
| Systemic: L1-AER-420, -430, -480, -490, -630, -640, -720, -760 and the ICD-based records | Documents cited exist or have a TBD | Records cite deliverables that are not in the repository: ICD-FC-AF, ICD-AER-TST (icd/ is empty), MS-DYN (only planned, task C1), AF_MODE_LOGIC. The TBD/TBR fields are "—", so no closure is recorded. | Minor | Add a TBR row per deliverable, with owner and gate, to registers/TBD_TBR.md, or note the planned gate in the record's TBD/TBR field. |

## 2. COMPOUND warnings (D30)

Verdict rule: split only where the conjunctions form a tree of separate cases. Otherwise accept as one thought. The 17 L0 warnings are decided in reviews/G0/checklist_L0.md and are not repeated here.

| ID | Statement fragment (conjunction) | Verdict | Reason |
| --- | --- | --- | --- |
| L1-AER-020 | "a force or moment" ("or") | accept (one thought) | One exclusion of coupling terms. |
| L1-AER-050 | "gravity, aerodynamic drag and the control forces and control moments" | accept (one thought) | A closed list summed into one total force and moment. |
| L1-AER-070 | "air-relative velocity ... and ... air density" | accept (one thought) | Two inputs to one drag computation. |
| L1-AER-080 | "each control force and each control moment" | accept (one thought) | A pair generated by the same effectors (as L0-CON-060). |
| L1-AER-100 | list of five effector definition kinds | accept (one thought) | A closed list in one obligation. |
| L1-AER-120 | "control force and control moment components at zero" | accept (one thought) | Condition on the other components of one authority case. |
| L1-AER-130 | "positive and negative body x axis, ... y axis and ... z axis" | accept (one thought) | A list of directions in one authority obligation. |
| L1-AER-140 | "about each body axis in each sense" | accept (one thought) | One rule applied to six moments. |
| L1-AER-160 | "translational ... and a rotational consumption relationship" | accept (one thought) | Both terms form one fuel-flow computation; no branching. |
| L1-AER-170 | "translational ... and rotational consumption parameters" | accept (one thought) | A list of two parameter sets read at one time. |
| L1-AER-200 | "zero control force and zero control moment" | accept (one thought) | The same output rule for both quantities. |
| L1-AER-220 | "elongated body shape and the simplified mass distribution" | accept (one thought) | Two inputs to one derivation. The vagueness is a separate finding. |
| L1-AER-280 | "vertical speed magnitude ... and the horizontal speed" | accept (one thought) | Two limits of one envelope, one region (see rationale, D30). |
| L1-AER-380 | "translational axis ... and the body rate about each other rotational axis" | accept (one thought) | One tolerance rule for two classes of axes. |
| L1-AER-390 | "its pitch angle and its roll angle" | accept (one thought) | One attitude-hold rule for two angles. |
| L1-AER-420 | "FC and AF ... each ... design and each ... implementation" | accept (one thought) | One interface applied to each pairing. |
| L1-AER-430 | "vehicle model and its flight software ... vehicle mass and fuel state" | accept (one thought) | One closed list of boundary data. |
| L1-AER-440 | "navigation and flight-control functions" | accept (one thought) | One state supply to two consumers. |
| L1-AER-450 | "its translation and its heading" | accept (one thought) | Two motion quantities guided by one capability. |
| L1-AER-470 | "armed or active, or when a target changes" | accept (one thought) | Alternative triggers with one identical response (annunciate). |
| L1-AER-480 | "a mode or a target" | accept (one thought) | The same handling for both selection kinds. |
| L1-AER-490 | "annunciations and indications" | accept (one thought) | Two classes of crew output under one data-item rule. |
| L1-AER-500 | "each crew selection and each annunciated or indicated quantity"; "or" | accept (one thought) | One unit rule applied to each class. |
| L1-AER-510 | "physical control device and display format" | accept (one thought) | One exclusion with a list. |
| L1-AER-520 | "through the flight control panel ... and through no direct manual flight control" | accept (one thought) | One channel rule: the panel is the only input path. |
| L1-AER-530 | "altitude, horizontal speed, vertical speed, heading and track" | accept (one thought) | A list of computed quantities from one state. |
| L1-AER-590 | "output sample, crew selection record and event record" | accept (one thought) | A list of record kinds under one timestamp rule. |
| L1-AER-610 | "each crew selection ... and each target" | accept (one thought) | Two items under one logging rule. |
| L1-AER-620 | "armed and active autoflight modes and the annunciations" | accept (one thought) | A list of logged state items. |
| L1-AER-630 | list of five signal kinds | accept (one thought) | A closed list of logged signals. |
| L1-AER-640 | list of six data kinds | accept (one thought) | A closed list. "navigation quantities" is a separate finding. |
| L1-AER-650 | "identifier and version ... design and ... implementation" | accept (one thought) | A list of configuration identifiers for one run. |
| L1-AER-660 | list of initial-condition items | accept (one thought) | A list that makes up one initial condition. |
| L1-AER-680 | "navigation, autoflight and flight-control functions" | accept (one thought) | One timing rule for three functions. |
| L1-AER-690 | "configuration, initial condition, crew selection sequence and execution host" | accept (one thought) | The inputs that define one repeatable run (as L0-SUC-040). The D25 question is a separate finding. |
| L1-AER-720 | list of MS-DYN contents | accept (one thought) | A closed content list for one specification. |
| L1-AER-730 | "requirements, models, interface signals and parameters" | accept (one thought) | One SI-unit rule over four artefact types. |
| L1-AER-740 | "requirements, models, interface signals and parameters" | accept (one thought) | One conventions rule over the same four artefact types. |
| L1-AER-750 | "one level file per level ... stating its level and either its parent requirements or the design decision it derives from" | split | Two separate obligations (file layout; record attributes) and an either-or tree: the Parent(s) field or the Derived field, each with its own check. Proposed split: (a) one level file per level; (b) each record below L0 states its level; (c) each record states its parent(s), or, when derived, its design decision. |
| L1-AER-760 | "a verification method, a verification procedure and a recorded verification result" | accept (one thought) | One link chain of verification data. |
| L1-AER-810 | "no orphan ..., no childless parent ... and no requirement without a verification method" | accept (one thought) | Three absence checks of one automated trace check (as L0-SUC-150). |
| L1-AER-830 | "the AI-assisted methods used to design and to verify the Aeronef" | accept (one thought) | One assessment covering two uses of the same methods. |
| L1-AER-840 | "a Vehicle Operating Manual, normal procedures and quick reference checklists" | accept (one thought) | Three documents in one deliverable. |

## 3. Count

Records checked: 80 (all Draft), 4 Deleted skipped. Findings: 24 in total: 3 Major (L1-AER-330, L1-AER-690, L1-AER-360/-460) and 21 Minor, of which 4 are marked (escalate) (L1-AER-330, L1-AER-690, L1-AER-020, and the subject finding for L1-AER-750 to -830). COMPOUND, L1 only (45 lint warning lines on 43 records): 42 accept, 1 split (L1-AER-750).
