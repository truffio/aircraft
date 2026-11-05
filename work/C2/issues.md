# C2 — Issues, change requests, design decisions and questions for the project owner

Task C2 (plan §6, Phase 3): the L2 FU section, fuel and mass properties (`work/C2/L2_FU.md`, 29 records). The questions are L2 questions about the FU subsystem and its interfaces. The local IDs C2-Qn need GitHub issues; once they are filed, cite them by issue number (sub-questions as #N.k).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 FU records | 29: Functional 8, Constraint 7, Interface 7, Model fidelity 5, Performance 1, Documentation 1 |
| Verification methods | Test 12, Inspection 10, Analysis 6, Demonstration 1 |
| L1 parents covered | 22 of 22 records allocated to FU (L1-AER-230 is Deleted, D54, so it needs no child) |
| Derived records | 0 (each record has an L1 parent; the design choices inside them are DD proposals, §4) |
| Parameters | 6 reused and updated (P-FU-010 to -060), 4 new (P-FU-070 to -100) |
| Owner questions | 6 (§2) |
| Change requests against L1 | 1 editorial, 1 conditional (§3.1); 1 editorial against the glossary (§3.2) |
| Interface needs | `interface_needs.md` IN-C2-10 to -34 |

**Coverage, L1 parent → FU children.**

| L1 record | FU children |
| --- | --- |
| L1-AER-020 | L2-AER-FU-180 |
| L1-AER-100 | L2-AER-FU-060 |
| L1-AER-150 | L2-AER-FU-010, -020, -030 |
| L1-AER-160 | L2-AER-FU-040, -050, -070 |
| L1-AER-170 | L2-AER-FU-010 |
| L1-AER-180 | L2-AER-FU-090, -100, -110, -120 |
| L1-AER-190 | L2-AER-FU-050, -080, -090 |
| L1-AER-200 | L2-AER-FU-200 |
| L1-AER-210 | L2-AER-FU-120, -150, -160 |
| L1-AER-220 | L2-AER-FU-120, -170, -180, -190 |
| L1-AER-290 | L2-AER-FU-140 |
| L1-AER-360 | L2-AER-FU-290 |
| L1-AER-430 | L2-AER-FU-130 |
| L1-AER-560 | L2-AER-FU-210, -240 |
| L1-AER-570 | L2-AER-FU-220, -240 |
| L1-AER-580 | L2-AER-FU-230, -240 |
| L1-AER-630 | L2-AER-FU-250 |
| L1-AER-640 | L2-AER-FU-260 |
| L1-AER-660 | L2-AER-FU-020, -030 |
| L1-AER-690 | L2-AER-FU-270 |
| L1-AER-720 | L2-AER-FU-280 |
| L1-AER-880 | L2-AER-FU-240 |

## 2. Questions for the project owner

Each FU record is written so that it is correct under either answer, or the open point is in its TBD/TBR field.

| ID | Question | Recommended answer | Affects |
| --- | --- | --- | --- |
| C2-Q1 | **Does the inertia change with the fuel?** L1-AER-220 leaves this to C2. C2 decided that it does: the fuel depletes uniformly over a fixed volume centred on the centre of gravity, so the inertia runs linearly from the dry-mass tensor [P-FU-070] at exhaustion to [P-FU-070] + [P-FU-080] at full capacity (DD-C2-02). The other option is a constant inertia, for example the fuel as a point mass at the centre of gravity. Confirm? | **Confirm the varying inertia.** The mass already changes with fuel (L1-AER-180), and a fixed full-fuel inertia would contradict it. The control laws then meet a varying inertia as well as a varying mass, which is what comparing laws needs, and the boundary carries the inertia for that reason (L1-AER-430 rationale). The centre of gravity stays fixed and the axes stay principal, so L0-CON-130 and D61 still hold. A constant inertia needs no rewrite: set [P-FU-080] to zero. | L2-AER-FU-160, -170, -180, -190; P-FU-070, -080; MS-DYN (C1); the moment budget P-SYS-420 (I1) |
| C2-Q2 | **Consumption form.** L1-AER-160 makes the form a C2 decision. C2 proposes (DD-C2-01): fuel mass flow = [P-FU-040] × the magnitude of the resultant control force + [P-FU-050] × the magnitude of the resultant control moment about the centre of gravity. The other option is to charge each effector on its own output, with one pair of coefficients per effector. Accept the resultant form? | **Accept the resultant form.** (1) It does not depend on the effector layout, which stays an EF design decision (D4, L1-AER-090 rationale). (2) Both terms apply whatever the layout; with per-effector charging, a layout that makes moments from offset forces would never use the rotational term, and L0-CON-120 asks for both. (3) The hover endurance keeps the closed form B1 assumed (L1-AER-360, FUNCTIONAL_ANALYSIS §7.3). (4) It is zero at zero output, so the free-fall and torque-free checks stay exact. **Cost:** effectors that oppose each other use no fuel, so an allocation that wastes authority is not penalised in fuel. FC already has to produce pure forces with the other components at zero (L1-AER-120 to -140), so this is acceptable for this cycle. If the owner prefers per-effector charging, only MS-DYN and the values of P-FU-040 and -050 change; L2-AER-FU-290 changes its formula. | L2-AER-FU-040, -060, -290; P-FU-040, -050; MS-DYN (C1); EF (C3) |
| C2-Q3 | **Data rate of the fuel-integral check.** The fuel mass flow is constant over each simulation step, so the integral is exact when the check uses each step's flow. The operational data are sampled every [P-TM-010] (two steps, proposed), so an integration of the output samples misses one step in two, and the error is not "numerical integration only" (L1-AER-190 rationale). Which data does the check use? | **The FU outputs at each simulation step, recorded by the TST for the analysis run** (IN-C2-30), with no change to the Aeronef configuration. [P-FU-060] then covers only the arithmetic (proposed 1e-6 kg). The same recording serves the tests that read outputs the operational data do not carry (inertia, fuel availability). The other option, integrating the output samples, needs a larger [P-FU-060] set from a prototype run, and the editorial change CR-C2-02. | L2-AER-FU-050, -080; P-FU-060; TST; L1-AER-190 rationale |
| C2-Q4 | **Initial fuel outside the range zero to [P-FU-010].** Reject the initial condition, or clamp the value? | **Reject**, with an initial-condition error to the TST (L2-AER-FU-030; new ICD-AER-TST item, IN-C2-31). Clamping would run a different case from the one the test procedure set, and the run could then pass against a fuel state it did not have. Zero and [P-FU-010] are valid. | L2-AER-FU-030; ICD-AER-TST (I1) |
| C2-Q5 | **#59, autoflight after fuel exhaustion (C2 share).** L1-AER-580 leaves the mode state at exhaustion to C2 and C5. What does FU give, and what should C5 do? | **FU gives the fuel-exhaustion indication in the fuel state from the first step with zero fuel to the end of the run** (L2-AER-FU-230), and nothing else changes on the FU side; this closes the C2 part of #59. For C5, C2 suggests that autoflight disengage at the first control frame in which it reads the indication, and that it annunciate no active mode, so that the crew interface and the operational data do not show a hold that the vehicle is not doing while it falls. The decision is C5's. | L2-AER-FU-230; TT-580; AF (C5) |
| C2-Q6 | **Proposed FU values.** B1 left the FU values for C2 to set at G2. C2 proposes one set that closes the fuel budget for an assumed hover endurance [P-SYS-280] of 3600 s: dry mass 1000 kg, capacity 500 kg, [P-FU-040] = [P-FU-050] = 1.09e-5 (kg/(N·s), kg/(N·m·s)), margin [P-FU-100] = 0.05, accounting tolerance [P-FU-060] = 1e-6 kg (`param_proposals.md` §1). Accept as TBR, and set [P-SYS-280]? | **Accept as TBR.** The owner sets [P-SYS-280] (D47); if it is not 3600 s, keep the masses and recompute [P-FU-040] from the inequality of L2-AER-FU-290. I1 may rescale the masses with the effector authority budget. | P-FU-010 to -060, -100; P-SYS-280; TT-110, TT-120 |

## 3. Change requests

### 3.1 Against L1 (baselined; proposed, not applied)

Every L1 record allocated to FU can be satisfied as written. The requests below are editorial.

| ID | Against | Requested change | Reason | Recommendation |
| --- | --- | --- | --- | --- |
| CR-C2-01 | L1-AER-100 rationale | After "The consumption parameters belong to FU (L1-AER-160, -170)", add: "They may be common to the effector set rather than one set per effector (L2-AER-FU-060)." | The statement says "each effector … its fuel consumption parameters", which suggests one set per effector. Under the resultant form (C2-Q2) the two coefficients are shared by the effector set. The statement still holds, because "only by" closes the list and does not require each kind to be present, but a G4 reviewer could read it otherwise. | Apply with the answer to C2-Q2 if the owner accepts the resultant form; withdraw if the owner chooses per-effector charging. Editorial: no requirement changes meaning. |
| CR-C2-02 | L1-AER-190 rationale (conditional) | "The tolerance covers the numerical integration only" → "The tolerance covers the numerical integration and the sampling of the independent check." | Needed only if the owner chooses integration of the output samples in C2-Q3. | Not needed under the recommended answer to C2-Q3. |

### 3.2 Against a fixed specification

| ID | Against | Requested change | Reason | Recommendation |
| --- | --- | --- | --- | --- |
| CR-C2-03 | GLOSSARY *Fuel state* | "below the low-fuel threshold `[P-FU-020]`" → "below the fraction `[P-FU-020]` of `[P-FU-010]`". | [P-FU-020] is a fraction, not a mass (L1-AER-570, CV-720). | Editorial; apply at the next glossary merge. |

### 3.3 Notes on L1 and the functional analysis (no change request)

| ID | Note | Proposed action |
| --- | --- | --- |
| N-C2-01 | L1-AER-360 rationale: "C2 confirms the form." Confirmed (L2-AER-FU-290), and the attitude-holding and regulation consumption that FUNCTIONAL_ANALYSIS §7.3 asked C2 to add is the margin [P-FU-100]. | I1 adds [P-FU-100] to the FUNCTIONAL_ANALYSIS §7.3 rule: [P-FU-010] ≥ [P-FU-030] · (exp((1 + [P-FU-100]) · [P-FU-040] · [P-DYN-010] · [P-SYS-280]) − 1). |
| N-C2-02 | L1-AER-210 rationale says FU defines the mass distribution; L1-AER-220 says MS-DYN states the shape and the distribution, with the dimensions as DYN parameters (C1). C2 reads them together: FU requires the distributions (centred, symmetric, uniform fuel depletion: L2-AER-FU-160, -190) and C1 states them in MS-DYN (IN-C2-13). | Integration (I1) confirms with C1. |
| N-C2-03 | L1-AER-580 TBD/TBR "#59, G2 (C2, C5)": the C2 share is closed by L2-AER-FU-230 (C2-Q5). | Update TT-580 to "C5 only" once the owner agrees. |
| N-C2-04 | The subject of the FU statements is "the FU subsystem", not "the fuel and mass-properties subsystem": the full name contains "and", and the lint raises COMPOUND on every record. *FU subsystem* is proposed for the glossary. Other agents may meet the same issue with their subsystem names. | Orchestrator: keep, or allow the full name and accept the warning. |
| N-C2-05 | Expected check results after assembly. lint: 0 errors, 14 COMPOUND warnings on the FU section (judged in §5). Trace: each of the 22 FU-allocated L1 records has at least one child (checked on a trial assembly in a scratch copy). param_check: PARAM-MISSING for P-FU-070, -080, -090, -100 until they are merged, then four PARAM-TBD warnings until the register rows of `param_proposals.md` §3 are added. | Orchestrator merges the parameters and the register rows. |
| N-C2-06 | Several FU tests read outputs that the operational data do not carry, because L1-AER-640 closes its list: the centre of gravity, the inertia tensor and the fuel availability. C2 did not ask to add them to the operational data; the tests read them through the TST recording of IN-C2-30. | TST plan extension; or a CR against L1-AER-640 if the owner wants them in the operational data. |

## 4. Proposed design decisions (for `registers/DECISIONS.md`)

These are choices inside parented records, as B1 recorded DD-030 and DD-040; no FU record is Derived. Provisional IDs DD-C2-0n; the orchestrator assigns the DD-nnn numbers.

| ID | Decision | Alternatives considered | Rationale | Requirements |
| --- | --- | --- | --- | --- |
| DD-C2-01 | The consumption rate is [P-FU-040] times the magnitude of the resultant control force plus [P-FU-050] times the magnitude of the resultant control moment about the centre of gravity (Euclidean norms). | (a) Charge each effector on its own output, with per-effector coefficients. (b) Per-body-axis absolute values of the resultant components. (c) Add an idle flow at zero output. | Independent of the effector layout; both terms apply whatever the layout; the hover endurance has a closed form; zero at zero output, which keeps the free-fall and torque-free checks exact; frame-invariant, unlike (b). (c) would add a sixth parameter kind (L1-AER-100) and break the zero-flow checks. Cost: opposing effectors use no fuel (C2-Q2). | L2-AER-FU-040, -060, -290 |
| DD-C2-02 | The fuel depletes uniformly over a fixed fuel volume centred on the centre of gravity and symmetric about the body axes, so the inertia tensor is the dry-mass tensor plus the full-fuel tensor scaled by the ratio of remaining fuel to capacity. | (a) A constant inertia, the fuel as a point mass at the centre of gravity. (b) A tank that drains from one side, which moves the centre of gravity (excluded by L0-CON-130). (c) A non-linear depletion law. | Keeps the centre of gravity fixed and the axes principal at each fuel state (L0-CON-130, D61) while the inertia follows the mass; linear, so it is simple to verify and to budget; (a) is its special case [P-FU-080] = 0 (C2-Q1). | L2-AER-FU-160, -170, -180, -190 |
| DD-C2-03 | The fuel availability of a step follows the remaining fuel at the start of the step, and in the step that ends at fuel exhaustion the fuel mass flow is limited to the remaining fuel divided by the step. | (a) Scale down the effector outputs in the last step so that they use exactly the fuel left. (b) Let the fuel go negative within one step and clamp it at the next. | Keeps the remaining fuel at or above zero, makes the fuel-mass integral exact and keeps the effector model free of fuel bookkeeping. (a) moves fuel logic into EF; (b) breaks L2-AER-FU-090 and the L1-AER-190 check. The cost, one step in which the effectors produce slightly more output than the fuel used pays for, is at most one step of output, below any test tolerance. | L2-AER-FU-050, -200 |
| DD-C2-04 | An initial fuel mass outside the range zero to [P-FU-010] is rejected with an initial-condition error; it is not clamped. | Clamp to the range; accept any value. | The run stays what the test procedure asked for (D59); clamping would hide an error in the procedure (C2-Q4). | L2-AER-FU-030 |

## 5. Self-check (METHODOLOGY §13.1 and §13.2)

**§13.1, per record.**

- One "shall" each, subject the FU subsystem, EARS patterns: ubiquitous (most records), event-driven (L2-AER-FU-010, -020: "When a run starts"), unwanted behaviour (L2-AER-FU-030: "If … then"). The lint reports 0 errors on 29 records.
- No number in a statement; each quantity is a parameter ID listed under Parameters. "Zero" and "one" appear only as definitional constants (zero fuel, zero products of inertia, "minus one" in the exponential budget of L2-AER-FU-290).
- No vague terms, escape clauses, open lists or absolutes (lint clean). No TIMING or KEYWORD warning.
- COMPOUND warnings (14), each judged one thought (D30):
  - closed lists of one object (4): L2-AER-FU-010 (the FU parameters), -120 (the three mass properties), -260 (two signals), -280 (the five MS-DYN models);
  - one relationship with two operands (6): L2-AER-FU-040 (the two terms of one sum), -050 ("the smaller of" two values), -060 (the two consumption sets), -170 (the two tensors of one sum), -190 (the shape and the distributions behind one derivation), -290 (one inequality);
  - a pair that is one constraint (4): L2-AER-FU-130 (the two kinds of boundary output), -160 (both distributions centred), -200 (the two values of one signal), -270 (the inputs of one function).
  None forms a tree of cases.
- Solution-free: no algorithm, data structure or code. The consumption form, the depletion model and the exhaustion-step limit are model physics (METHODOLOGY §7: for a simulation the physics is the requirement), recorded as DD proposals with alternatives. The equations are in MS-DYN through IN-C2-10 to -16, not in the statements.
- Terms: glossary terms, or proposals in `glossary_proposals.md` (FU subsystem, Dynamics subsystem, Vehicle-model boundary, Consumption relationship, Consumption rate, Fuel availability, Fuel capacity, Initial-condition error, Inertia tensor, Dry-mass and fuel-mass distribution). Axes and signs per CONVENTIONS (CV-160, CV-340, CV-350).
- Rationale with a "Sufficiency" argument per L1 parent on each record; parent, source, verification method, procedure ID and success criteria on each record.
- Criticality Not assessed; each TBD or TBR names an owner and a closure point.

**§13.2, the set.**

- Each L1 record allocated to FU has at least one FU child, with the sufficiency argument in the first child and "see …" in the others (coverage table, §1).
- Types considered: functional, interface, constraint, model fidelity, performance and documentation are present; failure handling is deferred (tailoring), and fuel exhaustion is treated as nominal behaviour throughout.
- Interfaces: each FU interface has an FU interface record and a home (MS-DYN, the boundary ICD, ICD-FCP, ICD-AER-TST); the other side is in `interface_needs.md`.
- No derived records. The DD proposals are reviewed with the set.
- No conflict found with L1. Possible overlaps with C1 (who states the mass distributions, N-C2-02; the DYN glossary term, IN-C2-18), C3 (consumption parameters stay FU's, IN-C2-22) and C8 (alert priority at exhaustion, IN-C2-43) are listed for I1.
- Manual sections affected: the Vehicle Operating Manual fuel limitations and the LOW FUEL and FUEL EXHAUSTED procedures (written after the requirements baseline, L1-AER-840).
