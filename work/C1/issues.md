# C1 — Issues, owner questions, change requests and design decisions (DYN)

Task C1 (plan §6, Phase 3): the DYN section of L2 (`work/C1/L2_DYN.md`) and the model specification `specs/MS-DYN.md`. Questions are at L2 level: the dynamics model and its physics. Local IDs C1-Qnn need GitHub issue numbers; C1-Q01 is the existing sub-question **#81.1**, and C1-Q02 closes **#81**. Cite the others by issue number once they are filed (they are never reused).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 DYN records | 45: Model fidelity 18, Constraint 10, Interface 10, Functional 6, Documentation 1 |
| L1 parents covered | 23 of 23 live L1 records allocated to DYN (L1-AER-230 is Deleted, D54, and has no child) |
| Derived records | 1: L2-AER-DYN-540 (DD-C1-03) |
| L3 records | None: each DYN record is a leaf; the next layer is the implementation (D4) |
| MS-DYN | Written: §0 to §14 (C2 and C3 content slots in §6 and §7) |
| Parameters | 11 new (P-DYN-020, -030, -100, -200 to -270); 3 existing updated (P-DYN-010 status, P-DYN-400 value, P-SYS-570 value) |
| Owner questions | 6 (§2) |
| Change requests | 2 (§3), both editorial, one conditional on #81 |
| Design decisions proposed | 6 (§4) |
| Lint | 0 errors, 24 COMPOUND warnings (judged in §6) |

## 2. Questions for the project owner

Each question has a recommended answer. The requirements are written so that they are correct under either answer: they point to the MS-DYN section that records the answer and carry the item in their TBD/TBR field.

### C1-Q01 (#81.1) — The rotation-during-translation term

**Question.** When the vehicle rotates while it translates, does its velocity stay fixed in the local reference frame (Newton), or does it turn with the body? In body axes this is the term `ω × v` of the translational equation (MS-DYN §4.2, §4.5 term K-2). D18 says "seen from the aircraft's body frame", which can be read either way.

| | Option T1 — retain the term (Newtonian) | Option T2 — remove the term |
| --- | --- | --- |
| Model | `m·dv/dt = F` in the inertial frame L | `m·dv^B/dt = F^B`: with no force, the body-axis velocity is constant |
| Turn at speed with no lateral force | The vehicle keeps moving in the same direction; the nose turns away from the velocity | The velocity turns with the nose: the vehicle changes direction with no force |
| Physics | Conserves linear momentum; standard rigid-body model | Not Newtonian: a fictitious acceleration `ω × v` with no force behind it |
| Credibility checks | Free fall, terminal velocity, torque-free rotation: closed forms hold | Same closed forms hold for those (no rotation during translation in them); check C-5 has its own expected result |
| Sensed acceleration | Equals vehicle acceleration minus gravity (the relation the crew budget of FUNCTIONAL_ANALYSIS §7.2 uses) | Differs from it by `ω × v`; the budget relation of §7.2 and the L1-AER-290 rationale would need restating (a change request) |
| Effect on FC and AF | In Heading at speed, a heading change needs a lateral force (vehicle mass × horizontal speed × heading rate) to keep moving nose-first; that acceleration enters `[P-SYS-440]`, `[P-AF-200]`, `[P-SYS-120]` and `[P-SYS-410]`, and FC must hold the body-axis velocities within `[P-SYS-540]` during the turn (L1-AER-380) | A heading change at speed turns the path for free; no budget share |
| Effect in normal operation | Only in Heading at non-zero speed during a heading change. Stationary, Hover, vertical motion and turns in place are unaffected (the term has no vertical component with pitch and roll at zero) | Same scope |

**Recommended answer: T1, retain the term.** It is the physics a credible model must reproduce (METHODOLOGY §7, §10.3); a reverse-engineering team and any later sensor model would assume it; and D18's purpose, no aerodynamic or effector coupling between axes, is met by the drag, effector and inertia requirements, not by changing Newton's law. The cost is that turning at speed takes force, and the budgets must count it (IN-C1-32). The rest of D18 holds: with T1 the term is listed in MS-DYN as a retained rigid-body kinematic term, which is exactly the exception L1-AER-020 makes.

**Affects.** MS-DYN §4.2, §4.5, §8, check C-5; L2-AER-DYN-030, -050, -300, -640 (written for either answer); FC (C4) and AF (C5) through IN-C1-32; FUNCTIONAL_ANALYSIS §7.1, §7.2 at I1.

### C1-Q02 (#81) — Confirm the other retained kinematic terms, and close #81

**Question.** Confirm that MS-DYN retains (a) the gyroscopic term `ω × (J·ω)` of the rotational equation (K-1) and (b) the resolution of gravity, drag and the body-fixed control force through the attitude (K-3), so that #81 closes with the MS-DYN kinematic terms list (with the C1-Q01 answer for K-2).

**Recommended answer: confirm both.** K-1 is zero in normal operation: with principal axes (D61) and pitch and roll held at zero (D57), every gyroscopic product contains a pitch or a roll rate. It acts only during small pitch and roll transients and after fuel exhaustion, when it is what makes a torque-free rotation conserve its angular momentum (check C-3, required by METHODOLOGY §10.3). Removing it would make check C-3 fail by design. K-3 is not a term one can remove: it is the change of frame between the body, where the effectors act, and the local frame, where gravity acts.

**Affects.** MS-DYN §4.5; L2-AER-DYN-050; closes TT-230 (L0-CON-030) and TT-330 (L1-AER-020) through CR-C1-01.

### C1-Q03 — Drag form and aerodynamic moment

**Question.** Which drag form does MS-DYN use (§5.5), and is there an aerodynamic moment? L1-AER-070 leaves "whether drag depends on attitude (elongated body)" to MS-DYN, bounded by L1-AER-020 (no cross-axis coupling) and L1-AER-030 (no lift).

- **D1 (recommended):** isotropic quadratic drag, `D = −½·ρ·[P-DYN-100]·|v_a|·v_a`, opposite to the air-relative velocity, independent of attitude, acting at the centre of gravity.
- **D2:** per-axis quadratic drag in body axes with three coefficients and the capsule's reference areas; the drag along each body axis depends only on the flow along that axis, but for an oblique flow the force is not opposite to the flow, so it has a cross-flow component.
- **Aerodynamic moment:** none (recommended, DD-C1-01), or a rotational damping moment per body axis.

**Recommended answer: D1, and no aerodynamic moment.** D1 has no lift by construction (L1-AER-030 is shown by one line), it keeps translation and attitude independent through the aerodynamics in every frame (L0-CON-020), a motion along one body axis gives drag along that axis only (D18, L2-AER-DYN-190), and it gives the single drag function `D(V)` with which the L1 authority budgets are already written (FUNCTIONAL_ANALYSIS §7.1). AIRCRAFT_CHARACTERISTICS §1 says the shape matters only through the mass properties. No aerodynamic moment matches the L1 rationales and the reference mission ("keeps the angular rate it had" at fuel exhaustion, L1-AER-200, -390, CONOPS SC-110), keeps check C-3 valid with drag on, and makes the drag-moment lines of the moment budget zero (L1-AER-140). D2 is kept in MS-DYN as the documented alternative.

**Affects.** MS-DYN §5.5; L2-AER-DYN-110, -130, -160; P-DYN-100; FUNCTIONAL_ANALYSIS §7.1 at I1 (IN-C1-33).

### C1-Q04 — Gust shape and minimum rise time (D62)

**Question.** D62 leaves the gust rise time `[P-SYS-570]` TBD, to be set at G2 with MS-DYN, and the `[P-SYS-560]` entry says the rest of the gust shape is defined in MS-DYN. Approve the MS-DYN wind model (§5.4) and the value?

- Steady wind: horizontal, constant over a run, at most `[P-SYS-430]`.
- Gust events (gusts and bursts alike): non-overlapping; amplitude at most `[P-SYS-560]` along a fixed horizontal direction; one-minus-cosine rise over at least `[P-SYS-570]`, a hold, and a one-minus-cosine decay over at least `[P-SYS-570]`.
- `[P-SYS-570]` = 2.0 s (TBR).

**Recommended answer: approve.** The one-minus-cosine shape is the standard discrete-gust form; it is continuous with a continuous rate, which bounds the rate of change of the drag that FC must follow (rate at most `(π/2)·[P-SYS-560]/[P-SYS-570]`). 2.0 s is about the passage time of the longest FAR 25.341 gust gradient (350 ft) at the 100 kt steady wind, and 20 times the control-loop latency `[P-SYS-480]`. C4 confirms at I1 that the transient allowance `[P-FC-020]` and the position share `[P-FC-010]` cover it; if they do not, the value goes up, not the budgets. A gust that overlaps another, or a steady wind that changes during a run, is outside the envelope and stays with the refined wind model (#84).

**Affects.** MS-DYN §5.4; L2-AER-DYN-410; P-SYS-570 (TT-650); the TST wind model (IN-C1-25).

### C1-Q05 — Body shape and dimensions (L0-CON-140, TBR 2026-11-30)

**Question.** L0-CON-140 keeps the elongated "Tic Tac" shape provisional until 2026-11-30. Accept the capsule (a cylinder with hemispherical ends, MS-DYN §2.1), 12 m long and 4 m in diameter (TBR)?

**Recommended answer: accept the capsule now; keep the dimensions TBR until FU sets the masses.** The capsule is the "Tic Tac" of the concept, it is symmetric in each body plane (so a symmetric mass distribution gives the principal axes of D61 and a centre of gravity at its centre), and its inertia has a closed form (MS-DYN §6). Under drag option D1 the dimensions affect only the inertia and the crew station; their values follow from the mass properties C2 chooses, so they close with C2 at I1.

**Affects.** MS-DYN §2, §6; L2-AER-DYN-220, -240; P-DYN-020, -030, -400; closes TT-240 and TT-430.

### C1-Q06 — Gravity value

**Question.** `[P-DYN-010]` = 9.806 65 m/s² is TBR (TT-150, D48). Set it?

**Recommended answer: set it (status Set) at G2.** Standard gravity is a definition, not an estimate; the crew limit then reads exactly 1 g in a hover (G0-F25), and nothing at L2 argues for another value. The standard atmosphere uses its own `g_0` constant, so the two stay independent (MS-DYN §5.3).

**Affects.** P-DYN-010; TT-150, TT-340, TT-710.

## 3. Change requests

No baselined L1 record is unsatisfiable as written: each L1 record allocated to DYN has a DYN child that meets the DYN share in the parent's terms (coverage table in `work/C1/L2_DYN.md`). The requests below are editorial.

| ID | Against | Requested change | Reason | When |
| --- | --- | --- | --- | --- |
| CR-C1-01 | L1-AER-020 (statement, TBD/TBR field); L0-CON-030 (TBD/TBR field) | In L1-AER-020, replace "other than the rigid-body kinematic terms that MS-DYN retains" by "other than the rigid-body kinematic terms of the MS-DYN kinematic terms list", and close its TBD/TBR field (TT-330). Close the L0-CON-030 TBD/TBR field (TT-230). | The G1 checklist (L1-AER-020, Minor, deferred to #81) asked for the retained terms to be listed or the MS-DYN section cited once #81 closes. MS-DYN §4.5 now holds the list. | When the owner answers C1-Q01 (#81.1) and C1-Q02 (#81) |
| CR-C1-02 | GLOSSARY fixed terms *Standard atmosphere*, *Vehicle state*, *Landing envelope*, *Sensed acceleration* | As in `work/C1/glossary_proposals.md` §2. | MS-DYN names the atmosphere; the vehicle-state acceleration needs a defined evaluation instant (DD-C1-04); "contact sample" becomes the defined *contact step*; the sensed acceleration gets its formula. | At I1 |

**Conditional on C1-Q01.** If the owner chooses option T2, two further change requests are needed: the L1-AER-290 rationale and FUNCTIONAL_ANALYSIS §7.2, which state the sensed acceleration as the vehicle acceleration minus gravity, must allow for the `ω × v` term. Under the recommended T1 nothing changes.

## 4. Design decisions proposed (for `registers/DECISIONS.md`)

Local IDs; the orchestrator assigns register numbers. Only DD-C1-03 has a derived requirement; the others are choices inside parented records, recorded so the choice can be reviewed (as B1 did with DD-030 and DD-040).

| ID | Decision | Alternatives considered | Rationale | Requirements |
| --- | --- | --- | --- | --- |
| DD-C1-01 | Drag acts at the centre of gravity; there is no aerodynamic moment (no rotational damping, no centre-of-pressure offset). | Rotational damping moment per body axis; drag at a centre of pressure off the centre of gravity. | An offset centre of pressure couples translation into rotation (D18). Damping would contradict "keeps the angular rate it had" at fuel exhaustion (L1-AER-200, -390, SC-110) and break check C-3 with drag on. Simplest model consistent with L1. | L2-AER-DYN-110 (C1-Q03) |
| DD-C1-02 | Isotropic quadratic drag with one drag area `[P-DYN-100]` (MS-DYN §5.5, option D1). | Per-axis quadratic drag (D2); linear drag. | No lift by construction; attitude-independent; meets D18 for single-axis motion; matches the `D(V)` of the L1 budgets. Linear drag is not the air resistance of the concept. | L2-AER-DYN-130, -160, -190 (C1-Q03) |
| DD-C1-03 | At the contact step the reported altitude is zero; the horizontal position and the velocity are those propagated; the classification uses that velocity; there is no interpolation to the crossing instant. | Report the propagated (slightly negative) altitude; interpolate the state to the crossing instant. | CV-420 says the altitude is never negative in a run. Interpolation puts a state off the CV-820 time grid and changes the classification instant away from a step. The velocity changes by at most one step's acceleration, which is negligible against the envelope limits. | L2-AER-DYN-540 (Derived) |
| DD-C1-04 | The acceleration quantities (vehicle acceleration, sensed acceleration) of step k ≥ 1 are evaluated at the end of the step that produced the state; those of step 0 with the inputs of the first step (MS-DYN §3.3). | Evaluate at the start of the step, with that step's inputs (not available when the frame-start state is passed to NAV and FC); omit the acceleration from the vehicle state. | Keeps the acceleration part of the frame-start state (L1-AER-440) and available to TM at every sample, with one defined value per step. | L2-AER-DYN-300, -310 |
| DD-C1-05 | The standard atmosphere is the U.S. Standard Atmosphere, 1976, from altitude zero to 47 000 m, with the geopotential altitude taken equal to the altitude. | ICAO ISA (identical to 32 km); an exponential atmosphere. | D20 asks for the standard atmosphere and the glossary asks MS-DYN to name it. The 1976 standard is published with a density table for check C-7. An exponential atmosphere is not the standard. | L2-AER-DYN-150 |
| DD-C1-06 | Over each simulation step the control force and moment, the mass properties and the wind are held at their step values (MS-DYN §10.2). | Interpolate the inputs within the step; let EF and FU vary them within the step. | Gives each step a defined input, so the step is reproducible (L1-AER-690) and the independent solutions of the checks have a known input. EF outputs and FU mass are per step by their glossary definitions. | L2-AER-DYN-400, -410, -420 |

## 5. Notes for the orchestrator

| ID | Note | Proposed action |
| --- | --- | --- |
| N-C1-01 | No L3 is needed for DYN (D4): each record can be implemented and verified by one owner without further interpretation; the integration method is a design choice bounded by the credibility checks. | None. |
| N-C1-02 | Expected check results after assembly (checked in a scratch copy with the proposals merged): lint 0 errors and 24 COMPOUND warnings on the DYN section; trace check: DERIVED error for L2-AER-DYN-540 until DD-C1-03 is in the register, and no DYN-allocated L1 record childless; param check: 0 errors, PARAM-TBD warnings for P-DYN-020 to -270 until the TBD/TBR rows of `param_proposals.md` §3 are added. | Register DD-C1-03; add the TBD/TBR rows. |
| N-C1-03 | MS-DYN §6 and §7 hold content slots for C2 (mass properties, fuel model) and C3 (effector model), as L1-AER-160, -220 and -720 require. | Merge the C2 and C3 text at I1; their L2 children cite those sections. |
| N-C1-04 | FUNCTIONAL_ANALYSIS I-07 lists the sensed acceleration inside the vehicle state; the glossary and L1-AER-640 keep them separate. MS-DYN keeps them separate (IN-C1-35). | Align I-07 at I1. |
| N-C1-05 | FUNCTIONAL_ANALYSIS §7.1: under DD-C1-01 the drag-moment lines of `[P-SYS-420]` are zero; under DD-C1-02 `D(V) = ½·ρ·[P-DYN-100]·V²` at the density of `[P-SYS-210]`. Under C1-Q01 T1, the turn-at-speed acceleration is a new share of §7.1 and §7.2 (IN-C1-32). | I1 budget closure. |
| N-C1-06 | `[P-SYS-200]` must lie within the atmosphere model's range, 47 000 m (IN-C1-39). | I1, when P-SYS-200 is set. |
| N-C1-07 | TBD/TBR register: TT-660 (MS-DYN) is now drafted; TT-140 (P-DYN-400) and TT-650 (P-SYS-570) move from TBD to TBR with proposed values; TT-150 closes if C1-Q06 is accepted. | Update at I1. |
| N-C1-08 | The TST will need requirements for the wind envelope it applies and for a prescribed-input harness for checks C-4 and the hover case of L2-AER-DYN-300 (IN-C1-24, -25). The TST branch is not written yet (D44). | Record for the TST plan extension. |
| N-C1-09 | Procedure IDs are proposed as IN-, AN-, TP- and DM-DYN-nnn, matching the record number (METHODOLOGY §10.4 example AN-DYN-020). | V1 confirms in Phase 5. |
| N-C1-10 | The DYN subject "the dynamics model" is a new glossary term (*Dynamics model*). | Merge from `glossary_proposals.md`. |

## 6. Self-check (METHODOLOGY §13.1 and §13.2)

**§13.1, per record.**

- One "shall", subject the dynamics model, EARS pattern (ubiquitous, event-driven "When", state-driven "While"): lint 0 errors over 45 records.
- No numbers in statements: every quantity is a parameter reference listed under Parameters (checked by script: no statement or verification parameter missing from its Parameters field). MS-DYN sections are cited by name because section numbers would be digits.
- No vague terms, escape clauses, open lists or absolutes (lint clean). No TIMING or KEYWORD warning.
- COMPOUND warnings (24 on 23 records), each judged one thought (D30):
  - closed lists of one object (8): L2-AER-DYN-020 (the state), -070 (the three angles), -100 (the three forces), -430 (the initial-condition elements), -530 (the content of one record), -620 (the two conserved quantities of one check), -700 (the MS-DYN sections), -350 (the two DYN outputs to TM);
  - inputs or qualifiers of one computation or one interface item (10): -030, -040, -130, -180, -210, -220, -240, -300, -330, -420;
  - one prohibition or one exclusion (2): -110 ("from gravity or from drag"), -170 (surface and what it produces, two warnings);
  - one envelope and its complement (2): -510, -520 (D30, as L1-AER-280);
  - one check under two wind conditions with the same expected value (1): -610.
  None forms a tree of cases.
- Solution-free: no integration method, code structure or data layout. The model choices (drag form, no aerodynamic moment, contact-step altitude, acceleration instant, atmosphere standard, input hold) are recorded as DD-C1-01 to -06.
- Terms: glossary terms, or new terms in `glossary_proposals.md`. Axes and signs per CONVENTIONS.
- Rationale, parent or Derived, source, and a sufficiency argument per L1 parent: present on each record (the full argument in one child per parent, "see …" in its siblings).
- Verification: a direct method on each record (Inspection 20, Test 13, Analysis 11, Demonstration 1), a procedure ID and success criteria.
- Criticality Not assessed; each TBD/TBR item has an owner and a closure point.

**§13.2, the set.**

- Each L1 parent allocated to DYN is covered, with what DYN guarantees stated in the parent's terms (coverage table at the head of the section).
- No duplicates or conflicts found between the records; units SI; frames per CONVENTIONS.
- Types considered: model fidelity (the physics and its accuracy), constraint, interface, functional and documentation are present. Failure handling is deferred (tailoring); fuel exhaustion and ground contact are nominal behaviour.
- Each DYN interface has a home: the vehicle-model boundary ICD, ICD-AER-TST, or MS-DYN internal (`interface_needs.md` §3).
- The derived record (L2-AER-DYN-540) is flagged with DD-C1-03 for review at G2.
- The physics-as-requirement rule is met: the equations live in MS-DYN; the records point to its named sections; the credibility checks of METHODOLOGY §10.3 are records L2-AER-DYN-600 to -640 with tolerances, plus the fuel-mass integral, which is FU's (C-8, L1-AER-190).
- Manual sections affected: none directly (DYN behaviour reaches the operator only through the ground-contact outcome and fuel exhaustion, described by the operational manuals after the baseline).
