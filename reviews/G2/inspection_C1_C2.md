# Gate G2 inspection (partial) — C1 and C2 (DYN and FU L2 sections, MS-DYN)

```markdown
Artifact / version:   requirements/L2.md, sections DYN (45 records, from work/C1/L2_DYN.md) and FU (29 records,
                      from work/C2/L2_FU.md), all Draft v1; specs/MS-DYN.md (Draft, task C1, 2026-11-05),
                      at branch c1_c2, commit 68553fc
                      (read with them: requirements/L1.md (AER-L1-baseline-1 plus CR-C1-01, CR-C2-01),
                      requirements/L0.md, specs/CONVENTIONS.md, specs/GLOSSARY.md, specs/FUNCTIONAL_ANALYSIS.md,
                      specs/CONOPS.md, parameters/PARAMETERS.yaml, registers/*; staging work/C1/*, work/C2/*
                      read as supporting material only)
Review type:          Inspection (IEEE 1028; METHODOLOGY §11.3, checklists §13.1–13.2), physics consistency
                      (plan §6 Gate G2: "DYN, FU and EF plus MS-DYN"; EF not yet written)
Moderator / author / reader / recorder / reviewers:
                      moderator: orchestrator / authors: task C1 (DYN, MS-DYN) and task C2 (FU), owner Martin /
                      reader, recorder, reviewer: independent Opus inspector (did not author any of the material)
Date:                 2026-11-05
Entry criteria met:   yes, with notes:
                      - assemble.py L2 --dry-run: "L2: sections DYN, FU already up to date".
                      - lint: 0 errors, 104 warnings, all COMPOUND (D30): 17 on L0, 49 on L1, 38 on L2.
                        None of the L2 warnings hides a genuinely compound requirement (section 5).
                      - trace_check: 33 errors, all CHILDLESS, all on L1 records allocated only to subsystems
                        not yet written (EF, FC, AF, NAV, TM, FCP). Accepted as known. No DERIVED error
                        (DD-070 is registered), no orphan, no unknown or deleted parent; every live L1 record
                        allocated to DYN or FU has at least one DYN or FU child.
                      - param_check: 0 errors, 23 PARAM-UNUSED warnings. Two are relevant here: P-SYS-290
                        (the D66 anchor, cited by no requirement; G2-F18) and P-DYN-040 (gear length, D69).
                      - pytest tools/tests: 39 passed.
                      - MS-DYN §6 and §7 content slots are empty, pending to I1 (TT-780); known and not
                        raised as a defect.
                      - Working tree clean at 68553fc before this record was written.
Findings:             table below (25: 4 Major, 14 Minor, 7 Editorial)
TBD/TBR list checked: yes (see section 7)
Exit decision:        Rework and re-review (recommended; see section 9)
```

**Inputs read in full:** MS-DYN; the DYN and FU sections of L2; the 36 L1 records allocated to DYN or FU, plus L1-AER-120 to -140, -300, -310, -350 and -390 for the budgets; the L0 records they trace to; CONVENTIONS CV-110 to CV-490 and CV-810 to CV-940; the GLOSSARY terms used in DYN and FU statements; FUNCTIONAL_ANALYSIS §3.2 and §7; CONOPS SC-110; PARAMETERS.yaml (SYS, DYN and FU, plus the AF, FC, EF and TM entries used in the budgets); the registers; METHODOLOGY §7, §10, §13; and plan §6 and §9 (D1 to D71).

**Also read:** reviews/G1/inspection_B1.md, for the format. The staging files work/C1 and work/C2 (issues.md, interface_needs.md) were read as support only.

**Decisions are taken as settled.** A finding flags a place where an artifact contradicts a decision or fails to implement one.

**Numerical checks.** Every number quoted below was recomputed by the inspector, with scripts kept in the session scratchpad:

- the D66 arithmetic;
- a fall with drag through the MS-DYN atmosphere, integrated with RK4 at 0.01 s and at 0.002 s;
- the run time available to the free-fall checks;
- the density difference between geopotential and geometric altitude;
- the floating-point residual of the exhaustion-step flow.

## 1. Findings

Severity:

- **Major:** a real conflict or contradiction, a criterion that a correct model can fail or that cannot be executed, or something that would mislead I1 or the C3 to C5 work.
- **Minor:** a local defect, an inconsistency or an ambiguity with a clear fix.
- **Editorial:** wording, stale text or metadata.

The "Owner?" column marks the findings that need an owner decision. The questions themselves are in section 8.

| F-ID | Location | Severity | Finding | Recommended disposition | Owner? |
| --- | --- | --- | --- | --- | --- |
| G2-F01 | MS-DYN §10.3 (accuracy), §11 C-3 and C-5; L2-AER-DYN-620, -640 (statement and criteria); P-DYN-270; glossary *Accuracy horizon* | Major | **Checks C-3 and C-5 cannot be run over their horizon.** C-3 and C-5 must hold "over [P-DYN-270]" (172 800 s, 48 h), and §10.3 claims that C-1 to C-6 hold over that horizon. Both checks run with zero fuel, so only gravity (and in C-3 optionally drag) acts. The vehicle falls, and the contact step ends the motion: MS-DYN §9 item 5 and L2-AER-DYN-550 hold the state from then on. The longest free flight available is short. In vacuum (C-5), staying below the 47 km ceiling of the atmosphere model, it is at most 2·√(2·47 000/g) = 196 s. With drag, from [P-SYS-200] = 45 720 m at rest, it is 282 s (simulated). L2-AER-DYN-620 and -640 therefore cannot be verified as written, and the sufficiency claim of L2-AER-DYN-010 for L1-AER-010 ("torque-free rotation") fails until this is fixed. | Give C-3 and C-5 a check configuration with no ground contact. For example, set [P-DYN-010] = 0 in the check's vehicle parameter set, as a check configuration like the vacuum-equivalent one (MS-DYN §5.3 already keeps the atmosphere independent of [P-DYN-010]). The 48 h horizon then applies. Alternatively, state C-3 and C-5 "to the contact step", drop [P-DYN-270] from them, and cover long-horizon accuracy with another check (C-6 in SC-110 plus an energy or momentum check in a powered hold). Correct §10.3 and the glossary entry to match. | No (author C1; the tolerances were accepted in D64, so inform the owner) |
| G2-F02 | MS-DYN §11 C-2 (configuration, tolerance column); L2-AER-DYN-610; L2-AER-DYN-440 (its demonstration relies on C-2) | Major | **The terminal-speed closed form is not accurate enough for the run's parameter set.** Take dry mass 1000 kg and [P-DYN-100] = 5 m², with an exact integration of the vertical equation. The settled \|VS\| differs from `v_exp(h)` by 2.6×10⁻⁴ at the ground and 2.9×10⁻⁴ at 500 m. The value is the same at time steps of 0.01 s and 0.002 s, so it is the neglected physics, not integration error. That is 2.6 to 2.9 times the "tenth of [P-DYN-210]" that the C-2 text says the configuration keeps. The residual grows with altitude and reaches [P-DYN-210] = 1×10⁻³ near 5.2 km. A drop from 10 km, checked after a 60 s settling interval, peaks at 1.06×10⁻³, so a correct model fails L2-AER-DYN-610. The configuration column names no altitude band, release height or settling interval. Its remark "a large drag area gives a small v_t" implies changing [P-DYN-100], which the common conditions allow only "as each check states". The first-order correction also jumps at the layer boundaries (the lapse-rate change at 11 km), so the closed form only holds inside one layer. | Either (a) state the configuration: a release height and a checked band (for example release at no more than 3 km, check below 2 km after the settling interval). Then replace the "tenth" claim with the residual actually achieved (at most 3×10⁻⁴), or keep the claim and fix a drag area and mass in the configuration that make it true. Or (b) make the independent solution a reference integration of the one-dimensional vertical equation `dV/dt = g − ρ(h)·[P-DYN-100]·V²/(2m)`, computed outside the model to a tight tolerance. That holds at every altitude and across layers. | No (author C1) |
| G2-F03 | PARAMETERS P-SYS-230 description ("as true airspeed; the effectors saturate there"), D66; vs CV-480, L1-AER-310 rationale, L1-AER-130, P-SYS-410 description, FUNCTIONAL_ANALYSIS §7.1, P-SYS-270 note | Major | **Maximum speed is defined as both a ground speed and a true airspeed.** D66 and the P-SYS-230 description define the maximum speed as a true airspeed at which the effectors saturate. CV-480, the CONOPS selector and L1-AER-310 make horizontal speed ground-referenced: "a headwind raises the airspeed and the drag the effectors must overcome; that is why the wind limit enters the authority budget". So do P-SYS-410 and §7.1, which size the drag at [P-SYS-230] + [P-SYS-430] + [P-SYS-560]. Both readings break something. (i) Ground speed: 300 kt into a 150 kt wind is a 450 kt airspeed (231.5 m/s), with a drag of 164.1 kN, so "the effectors saturate there" (at 300 kt airspeed) is false. (ii) True airspeed: L1-AER-310 cannot be met into wind, and P-SYS-410 is oversized. Also, with ω×v retained (D64), the lateral acceleration of a turn depends on the ground velocity. With a 150 kt tailwind the ground speed is 450 kt and 231.5 × 0.062832 = 14.55 m/s². That is above [P-AF-200] (9.807 m/s²) and 99 % of [P-SYS-440] (14.71 m/s²), so the P-SYS-270 note ("9.70 m/s², inside P-AF-200") holds only at a ground speed of 300 kt. | The owner rules (Q1). Recommended: keep the CV-480 ground speed for [P-SYS-230] (baselined L1, the crew selector). Treat D66's "300 kt true airspeed" as the still-air anchor of [P-SYS-290], where the two coincide. Delete "as true airspeed; the effectors saturate there" from P-SYS-230. Have C5 bound the commanded heading rate so that the horizontal speed times the heading rate stays within [P-AF-200]. If the owner prefers the true-airspeed reading, raise CRs against L1-AER-130 and -310, FUNCTIONAL_ANALYSIS §7.1 and the P-SYS-410 description. | **Yes** |
| G2-F04 | D46; L1-AER-120 Source (D46); P-DYN-100 (TBR, "confirmed at I1 with the authority budgets"); D66; P-SYS-400, P-SYS-410 budgets | Major | **The D66 speed and the D64 drag area contradict D46.** D46 says the weight is carried along −z_B "with a smaller authority in the other five force directions". With the database values: P-SYS-400 ≥ 1500 × (9.807 + 14.710) + D(30.48 m/s) = 36.8 + 2.8 = 39.6 kN. P-SYS-410 ≥ 1500 × 14.710 + D(231.5 m/s) = 22.1 + 164.1 = 186.2 kN in reading (i) of G2-F03. It is 22.1 + 72.9 = 95.0 kN in reading (ii), and the still-air drag at 300 kt alone is 72.9 kN. The five "non-weight-bearing" directions therefore need 2.4 to 4.7 times the upward authority, and 186 kN is 12.7 times the maximum weight. The drag also dominates the fuel budget: at 300 kt the flow is 0.0174 kg/s, 5.1 times the hover flow of 0.0034 kg/s. This is the I1 confirmation that the P-DYN-100 source asks for, and it fails against D46. | The owner rules (Q2). Recommended: keep D66 and [P-DYN-100] = 5 m², and revise the wording of D46. The weight is carried along −z_B only; the authority in the other five directions is set by the drag at maximum speed and may exceed the upward authority. The alternative is to cut [P-DYN-100] to about 0.53 m² in reading (i), or 1.2 m² in reading (ii), or to lower [P-SYS-230]. Either change re-derives [P-FU-040], [P-FU-050] and [P-SYS-280] (G2-F18). | **Yes** |
| G2-F05 | L2-AER-FU-120 (statement, criteria) vs L2-AER-DYN-210 (rationale: "its position does not cross this interface"); IN-C1-02 vs IN-C2 §1 row I-04; FUNCTIONAL_ANALYSIS I-04 | Minor | **The DYN and FU records disagree on what crosses interface I-04 (FU to DYN).** FU gives "the vehicle mass, the centre-of-gravity position and the inertia tensor". DYN takes "the vehicle mass and the principal moments of inertia" and says the centre of gravity does not cross. The two sides also name the inertia differently ("inertia tensor" against "principal moments"). There is no physical effect while the centre of gravity is zero, but the MS-DYN §6 slot and the inspection criteria of the two records cannot both pass. | I1 picks one definition. Recommended: the centre of gravity does not cross I-04 (L2-AER-DYN-200 and L2-AER-FU-150 already fix it at the origin), and it stays a mass-properties item at the vehicle-model boundary to FC (L1-AER-430). Change L2-AER-FU-120 and its criterion, align FA I-04, and use one name for the inertia item. | No |
| G2-F06 | L2-AER-DYN-050 rationale; DYN coverage table row L1-AER-020 ("drag couples no axis"); MS-DYN §4.5 ("there is no aerodynamic coupling"); L2-AER-DYN-190 | Minor | **The no-coupling claim for drag is overstated.** Under isotropic drag D1, the drag along body x is `−k·|v_a|·v_a,x`, which depends on the y component through the shared magnitude. Motion along y therefore changes the x acceleration whenever v_a,x ≠ 0. MS-DYN §5.5 says so ("the magnitude \|v_a\| is shared"; D2 "meets D18 in the stronger per-axis reading"). Yet §4.5, L2-AER-DYN-050 and the coverage table claim no aerodynamic cross-coupling. L2-AER-DYN-190 covers single-axis flow only. At the G4 roll-up, an inspector of L0-CON-030 ("no term by which motion along one degree of freedom produces a force … along another") could fail the decomposition. | The owner confirms the D18 reading (Q3). Then record it in MS-DYN §4.5, the L2-AER-DYN-050 rationale and the coverage table: D18 is met for motion along one axis (L2-AER-DYN-190), and the coupling of oblique flow through the shared magnitude is accepted with option D1 (D64). | Confirm |
| G2-F07 | MS-DYN §11 C-7; L2-AER-DYN-150 criteria; P-DYN-260 | Minor | **C-7 does not say which altitude the density table is read at.** The 1976 standard tabulates by geometric altitude, with the geopotential value alongside. MS-DYN takes the geopotential altitude equal to h (DD-090), but C-7 compares with "the published density table" at the base altitudes and midpoints without naming the altitude. Reading the geometric-altitude rows gives relative differences of 2.4×10⁻³ at 11 km, 9.9×10⁻³ at 20 km, 2.5×10⁻² at 32 km and 4.8×10⁻² at 47 km. That is 24 to 480 times [P-DYN-260], so a correct model would fail. | State that the reference is read at the geopotential altitude equal to h (DD-090): name the table by geopotential altitude, or compute the reference from the standard's defining equations at those points. | No |
| G2-F08 | MS-DYN §5.3 ("defined from h = 0 to … 47 000 m"); DD-090; L2-AER-DYN-150; §11 C-1 ("any initial position") | Minor | **The density is undefined outside 0 to 47 km, and the model reaches both sides.** (a) In the step that ends at contact, the integrator evaluates the drag at altitudes at or below zero: the propagated altitude at the contact step is at most zero by definition (DD-070). (b) An initial condition, a check configuration (C-1 allows any initial position) or a ballistic arc can lie above 47 km. No DYN record says what happens there. | Extend layer 0 below zero (the 1976 standard is defined down to −5 km) and state a rule above 47 km. Either reject an initial altitude above the model range, as L2-AER-FU-030 does for the fuel, or extend the layers. Record the rule in DD-090. | No |
| G2-F09 | P-DYN-270 value and description; MS-DYN §12 note; glossary *Accuracy horizon* | Minor | **The accuracy horizon is shorter than the longest run.** It is set to "at least the longest run" and sized from [P-SYS-280] (46 h). But [P-SYS-280] is a minimum endurance, not the length of a run. With the database values, a hold from full fuel with no regulation overhead lasts ln(1.5)/(k_t·g) = 176 692 s (49.1 h), followed by the fall. That is longer than [P-DYN-270] = 172 800 s. The SC-110 hover-endurance variation (the L2-AER-FU-290 criterion (2)) and SC-110 leg 10 both run to exhaustion. | Size [P-DYN-270] from ln(m_max/m_dry)/([P-FU-040]·[P-DYN-010]) plus the fall, for example 180 000 s, and fix the description ("raised to P-SYS-280" uses the wrong bound). D69 makes this unbounded (section 6). | No |
| G2-F10 | L2-AER-FU-050 (statement; criterion "the remaining fuel mass of the next step is zero"); L2-AER-FU-090 ("exactly zero"); L2-AER-FU-200 ("above zero"); DD-130 | Minor | **Exactly zero fuel at exhaustion depends on floating-point rounding.** With the flow limited to `m_f/Δt` and `m_f(k+1) = m_f(k) − flow·Δt` (IN-C2-12), the result is not exactly zero in floating point. In 10⁵ random fuel residues with Δt = 0.01 s, 7.0 % gave a positive residual and 6.6 % a negative one. A positive residual keeps the fuel availability "available" for one more step, with full effector output on about 10⁻²¹ kg of fuel. A negative residual violates L2-AER-FU-090. | State in L2-AER-FU-050 (and DD-130, MS-DYN §7.2) that the step that ends at exhaustion sets the remaining fuel mass to zero, so exactness does not depend on rounding. | No |
| G2-F11 | L2-AER-FU-030 criteria ("… and no output sample") vs its rationale ("the TST decides what to do with the run") | Minor | **The FU-030 criterion tests TST behaviour, which the record says it does not control.** "No output sample" depends on the TST, and the rationale leaves the reaction to the TST. | Criterion: one initial-condition error naming the fuel mass, and FU produces no outputs for that run. Move "no output sample" to the ICD-AER-TST and TST requirements. | No |
| G2-F12 | L2-AER-DYN-300 criterion (3); L2-AER-DYN-310 criteria; DD-080; P-TM-010 | Minor | **The data for the acceleration checks are not in the operational data.** Under DD-080, the acceleration quantities of step k use the inputs held over step k−1 to k: the control force, mass and wind of step k−1. The operational data sample every [P-TM-010] = 2 × [P-SYS-300] and record the effector outputs and mass of step k only. The step k−1 inputs that the independent computation needs are therefore not in the operational data. L2-AER-DYN-300 (3) does not say which step's force and mass it uses. With the step-k mass, the difference is ṁΔt/m (about 1.7×10⁻⁷), not "floating-point rounding". | Name the inputs of step k−1 in L2-AER-DYN-300 (3) and -310, and require per-step recording of the vehicle-model interfaces for these analyses, as FU does (IN-C2-30). | No |
| G2-F13 | L2-AER-FU-230 `TBD/TBR` ("Autoflight state after fuel exhaustion (#59, TT-580), Martin, G2 (C5)"); registers TT-580 | Minor | **The TBD field cites an answered question.** D68 answered #59, and D65 closed FU's share of it. L2-AER-FU-230 states the FU indication only and does not depend on the answer. TT-580 is still Open, citing #59. | Set the field to the record's own open item ([P-SYS-470] value TBR, TT-070). Rewrite TT-580 as the C5 annunciation item after exhaustion (D68). | No |
| G2-F14 | L2-AER-DYN-640 criteria; MS-DYN §11 C-1, C-4 and C-5 ("relative to … change since t_0"); L2-AER-DYN-600, -630 | Minor | **Two tolerances are undefined as written.** (a) L2-AER-DYN-640 asks that the pitch and roll angles "keep their initial values to within the same relative tolerance", but the configuration has level attitude, so the initial values are zero and a relative tolerance is undefined. (b) The "relative to their change since the start" errors of C-1, C-4 and L2-AER-DYN-600 are 0/0 at step 0, and also for a component that does not change. | Give an absolute bound for the angles. Define the relative errors from step 1 on, with the vector norm. | No |
| G2-F15 | L2-AER-DYN-020 statement ("a vehicle state made of …"; rationale "The list is closed") vs glossary *Vehicle state*, L2-AER-DYN-310 rationale, -320, -330, -340 | Minor | **"Vehicle state" has two meanings.** L2-AER-DYN-020 closes the vehicle state to the four integrated elements. The glossary, and L2-AER-DYN-310 ("The vehicle acceleration is part of the vehicle state (glossary)"), include the Euler angles and the vehicle acceleration. L2-AER-DYN-320 to -340 pass "the vehicle state" across the boundary, so which list applies matters. | Reword L2-AER-DYN-020 as the "integrated state" (the MS-DYN §3.1 term), and keep *Vehicle state* as the glossary defines it. | No |
| G2-F16 | MS-DYN §0, §6, §7.2 slots; P-FU-070 source and note ("Value TBD until C1 states the body shape and the distributions"), P-FU-080; L2-AER-FU-160 rationale ("with their dimensions as DYN parameters"); L2-AER-FU-280 (five FU models) | Minor | **Ownership and structure of the pending MS-DYN content are inconsistent.** MS-DYN gives the mass distributions to C2, while P-FU-070 waits for C1 to state them. No parameter exists for the fuel-volume dimensions that L2-AER-FU-160 cites. The MS-DYN §7.2 slot lists only the consumption relationships and the remaining fuel, while L2-AER-FU-280 requires sections for five FU models: fuel availability and the exhaustion limit (DD-130) have no slot. | At I1, assign the derivation to C2 (as MS-DYN §6 says). Either add the fuel-volume dimensions as parameters or choose the fuel volume equal to the capsule (IN-C2-13, which needs none). Align the MS-DYN §6 and §7.2 slots with the five models of L2-AER-FU-280. | No |
| G2-F17 | L2-AER-FU-190 criterion (database values only); L2-AER-FU-010 (P-FU-070, -080 taken from each vehicle parameter set) | Minor | **Derived inertia values can go stale in a campaign.** [P-FU-070] and [P-FU-080] are derived from [P-DYN-020], [P-DYN-030], [P-FU-030] and [P-FU-010], but each run takes them from its own parameter set. A campaign that varies [P-FU-030] or [P-FU-010] (allowed by the L2-AER-FU-010 rationale) without re-deriving them runs a body that no mass distribution gives, and L2-AER-FU-190 would not catch it. | Apply the L2-AER-FU-190 equality to each vehicle parameter set (a run-start check), or have FU derive the tensors at run start. | No |
| G2-F18 | P-SYS-290 (Set, PARAM-UNUSED); P-FU-040, -050 and P-SYS-280 notes; TT-110, TT-750, TT-800 | Minor | **The D66 derivation chain is recorded only in notes.** [P-FU-040] and [P-FU-050] are derived from [P-DYN-100], [P-FU-010], [P-FU-030], [P-SYS-230] and [P-SYS-290], and [P-SYS-280] from [P-FU-040]. The three TT rows are not linked. [P-SYS-290] is cited by no requirement, so nothing verifies the 8 h at maximum speed, and nothing triggers the re-derivation when [P-DYN-100] is confirmed at I1 (G2-F04). | Link the TT rows, or merge them into one row. The owner decides whether [P-SYS-290] is a requirement or only an anchor (Q4). Recommended: anchor only, said so in its description. | **Yes** (Q4) |
| G2-F19 | L2-AER-DYN-110 (rationale and Source "DD-050 (proposed)"); -540 ("DD-070, proposed"); -120 rationale and MS-DYN §5.2 ("TBR, TT-150"); MS-DYN §3.3 ("is proposed for an update"); MS-DYN §9 item 1 and L2-AER-DYN-500 ("glossary proposal"); L2-AER-FU-040 and -160 ("C2 proposes … DD-110 / DD-120"); L2-AER-FU-100 ("ranges in work/C2/param_proposals.md") | Editorial | **Status words are stale after the owner answers.** DD-050 to DD-140 are Accepted (D64, D65). [P-DYN-010] is Set and TT-150 is Closed; MS-DYN §12 says Set, so MS-DYN contradicts itself. CR-C1-02 is applied, and the glossary now holds *Contact step* and the DD-080 sentence. The parameter ranges are now in the PARAMETERS.yaml notes. | Refresh the wording. | No |
| G2-F20 | Parameters and `TBD/TBR` fields of L2-AER-DYN-140, -240, -410, -440, -610, -640; L2-AER-FU-040, -050, -060, -080, -090, -140, -160, -170, -190, -220, -230, -250 | Editorial | **The Parameters and TBD/TBR fields are inconsistent with each other.** Cited TBR parameters are missing from the TBD/TBR field. Examples: L2-AER-DYN-140 cites [P-DYN-210] with field "—"; L2-AER-DYN-640 omits [P-DYN-270]; L2-AER-DYN-610 omits [P-DYN-100] and [P-SYS-430]; L2-AER-FU-080 omits [P-FU-010], [P-SYS-300] and [P-TM-010]. Some listed parameters are not used in the statement or the criteria. L2-AER-FU-140 lists [P-SYS-120] and [P-SYS-440] and carries a TBR for [P-SYS-440], which it does not use. The register covers every one at parameter level (the same class of defect as G1 §5). | Make each field list exactly the TBR or TBD parameters that the statement and the criteria use. | No |
| G2-F21 | L2-AER-FU-290 statement | Editorial | **The statement can be parsed two ways.** "the exponential of the product of one plus [P-FU-100], [P-FU-040], [P-DYN-010] and [P-SYS-280]" can be read either way; only the formula in the rationale resolves it. | "… the product of [P-FU-040], [P-DYN-010], [P-SYS-280] and the sum of one and [P-FU-100]". | No |
| G2-F22 | MS-DYN §11 C-8 | Editorial | **C-8 does not require the per-step data.** C-8 integrates "the recorded fuel mass flow" without saying per simulation step (D65, L2-AER-FU-080, IN-C2-30). An integration of the output samples (every 2 steps) would not meet [P-FU-060] = 1×10⁻⁶ kg. | Say "the FU fuel mass flow of each simulation step". | No |
| G2-F23 | requirements/L2.md header ("Status: Skeleton (T0), no requirements yet"); registers/DECISIONS.md header ("D1–D66"); MS-DYN §13 (closure "G2" for P-DYN-020, -030; TT-740 closes 2026-11-30); K-3 naming (MS-DYN "gravity, drag and wind"; L2-AER-DYN-050 "gravity, drag and control force"; L1-AER-020 "forces"); DYN coverage table row L1-AER-070 (omits -410); L1-AER-200 rationale ("SC-110 leg 10"; the fall is leg 11) | Editorial | **Metadata and cross-references are stale or inconsistent.** | Refresh. Pass the L1-AER-200 leg number to B3 with its change requests. | No |
| G2-F24 | work/C2/interface_needs.md IN-C2-41 (cited by the L2-AER-FU-140 rationale) | Editorial | **The bound on the mass fall within a frame uses old numbers and a false premise.** It says "[P-FU-040]·[P-SYS-120]·[P-SYS-310], about 6.4e-6", but the database values give 1.4×10⁻⁷. The premise "‖F_c‖/m bounded by the crew limit" is false when drag is large: at 300 kt into the largest wind, ‖F_c‖/m reaches about 164 m/s² at dry mass, which gives 7.7×10⁻⁷. The conclusion, that the fall is negligible, still holds. | Correct the bound at I1. | No |
| G2-F25 | MS-DYN §5.4 rise-time note; P-SYS-570 note | Editorial | **The physical justification of the 2 s rise time covers only a vehicle near rest.** The note ties 2 s to "the passage time of the longest FAR 25.341 gust gradient at the steady wind". That equivalence holds for a vehicle at rest. At [P-SYS-230] into the wind (231.5 m/s airspeed), a frozen 107 m gradient passes in 0.46 s. The model is uniform in space and defined in time, so this is a definition, not an error. | Say that the equivalence is for a vehicle near rest. | No |

**Counts:** 4 Major (G2-F01 to G2-F04), 14 Minor (G2-F05 to G2-F18), 7 Editorial (G2-F19 to G2-F25). Owner decisions are needed for G2-F03, G2-F04 and G2-F18, and a confirmation for G2-F06.

## 2. Sufficiency per L1 parent

Each row is one live L1 record allocated to DYN or FU. L1-AER-230 is Deleted. "Sufficient" means the DYN and FU children cover the DYN and FU share and the argument holds. A share held by a subsystem not yet written is marked "pending" and is not a defect.

| L1 parent | Allocated to | DYN / FU children | Verdict |
| --- | --- | --- | --- |
| L1-AER-010 | DYN | DYN-010, -020, -030, -040, -060, -440, -600, -610, -620, -630, -640 | **Not sufficient as written.** The structure is sound, but the torque-free check cannot be executed over its horizon (G2-F01), and the terminal-velocity check can fail a correct model (G2-F02). |
| L1-AER-020 | DYN, EF, FU | DYN-040, -050, -110, -190, -640; FU-180 | DYN and FU shares sufficient once the D18 reading for oblique flow is recorded (G2-F06). EF pending. L2-AER-DYN-640 is affected by G2-F01. |
| L1-AER-030 | DYN | DYN-160 | Sufficient. Under option D1 the drag is antiparallel to the air-relative velocity, so there is no lift. |
| L1-AER-040 | DYN, EF | DYN-170 | DYN share sufficient; EF pending. |
| L1-AER-050 | DYN | DYN-100, -110, -180 (with -120 and -130) | Sufficient. D69 adds a ground reaction (section 6). |
| L1-AER-060 | DYN | DYN-120, -600 | Sufficient. |
| L1-AER-070 | DYN | DYN-130, -140, -150, -410, -610 | Sufficient in structure. The C-2 criterion (G2-F02) and the C-7 criterion (G2-F07) need fixing. |
| L1-AER-100 | EF, FU | FU-060 | FU share sufficient (one coefficient per kind, D65); EF pending. |
| L1-AER-150 | FU | FU-010, -020, -030 | Sufficient (D63 Q3 reading). |
| L1-AER-160 | FU, EF | FU-040, -050, -070 | FU share sufficient. The MS-DYN §7.2 content is pending (TT-780). EF pending, including the single mapping of IN-C2-11 (section 4). |
| L1-AER-170 | FU | FU-010 | Sufficient. |
| L1-AER-180 | FU, DYN | DYN-030, -210, -630; FU-090, -100, -110, -120 | Sufficient. The variable-mass form with no thrust term matches L0-ASM-090 (section 3). |
| L1-AER-190 | FU | FU-050, -080, -090 | Sufficient, with G2-F10 (exact zero) and G2-F22 (per-step data). |
| L1-AER-200 | EF, FU | FU-200 | FU share sufficient; EF pending. |
| L1-AER-210 | FU, DYN | DYN-200; FU-120, -150, -160 | Sufficient. Interface wording: G2-F05. |
| L1-AER-220 | FU, DYN | DYN-040, -210, -220; FU-120, -170, -180, -190 | Sufficient in structure. Values and text are pending (TT-770, TT-780). Ownership: G2-F16. Per-run consistency: G2-F17. |
| L1-AER-240 | DYN | DYN-230 | Sufficient. |
| L1-AER-250 | DYN | DYN-240 | Sufficient. (4, 0, −1) m lies inside the capsule: the cylinder runs from x = −4 to 4 m with radius 2 m. |
| L1-AER-260 | DYN, TM | DYN-500, -510, -530, -550 (and -540) | DYN share sufficient; TM pending. D69 rework (section 6). |
| L1-AER-270 | DYN, TM | DYN-500, -520, -530, -550 | As L1-AER-260. |
| L1-AER-280 | DYN | DYN-500, -510, -520 | Sufficient. The two records partition the contacts by CV-940 ("at most" / "exceeds"). |
| L1-AER-290 | FC, AF, FU, DYN | DYN-120, -300, -550; FU-140 | DYN and FU shares sufficient (the measurement, the gravity share, one mass). FC and AF pending. The unpowered case also passes (section 3). |
| L1-AER-360 | FU, EF | FU-290 | FU share sufficient, arithmetic verified (section 3). The EF share (a hold at no more than the weight, IN-C2-23) is pending. |
| L1-AER-430 | DYN, FU, EF, FC, AF, FCP, NAV | DYN-320, -340; FU-130 | DYN and FU shares sufficient. ICD home open (TT-720). Naming: G2-F05. |
| L1-AER-440 | DYN, NAV, FC | DYN-330 | DYN share sufficient. |
| L1-AER-560 | FU, FCP | FU-210, -240 | FU share sufficient. |
| L1-AER-570 | FU, FCP | FU-220, -240 | FU share sufficient (FU's latency share is zero). |
| L1-AER-580 | FU, FCP | FU-230, -240 | FU share sufficient. Stale TBD: G2-F13. |
| L1-AER-630 | TM, FC, EF, FU | FU-250 | FU share sufficient. |
| L1-AER-640 | TM, DYN, NAV, FU | DYN-070, -300, -310, -350, -530; FU-260 | DYN and FU shares sufficient. |
| L1-AER-660 | DYN, FU, AF, FCP | DYN-430; FU-020, -030 | DYN and FU shares sufficient. D69 rework (ground start). |
| L1-AER-670 | DYN | DYN-140, -400, -410 | Sufficient. |
| L1-AER-690 | all eight | DYN-420; FU-270 | DYN and FU shares sufficient (D59, D63 Q4). |
| L1-AER-720 | DYN, FU, EF | DYN-700; FU-280 | **Not yet.** MS-DYN §6 and §7 are pending (TT-780), and the slot list does not match L2-AER-FU-280 (G2-F16). DYN-700's own list is complete. |
| L1-AER-880 | FCP, AF, NAV, FU | FU-240 | FU share sufficient. |

## 3. Physics and budget verification

### 3.1 MS-DYN, checked correct

- **Translational equation (§4.2).** Option T1, `m·dv^L/dt = F^L`, is Newton's second law in L. Its body-axis form `dv^B/dt = C_BL·F^L/m − ω^B × v^B` follows from `dC_BL/dt = −[ω×]·C_BL`. The T2 forms are also derived correctly. ω×v is retained (D64).
- **Variable mass (§4.1 assumption 4).** There is no `ṁ·v` term and no `J̇·ω` term. This is exact, not only an approximation, under the FU model: fuel depletes uniformly over a volume centred on the centre of gravity (DD-120) and leaves with the local body velocity. The linear momentum carried away is `ṁ·v`, because the fuel centroid is at the origin. The angular momentum carried away is `−J̇_fuel·ω`, so `J·ω̇ + ω×(J·ω) = M` holds. This is consistent with L0-ASM-090.
- **Rotational equation (§4.3).** Euler's equations with a diagonal J: the signs are right. The gyroscopic term is retained, and with ω = (0, 0, r) every product term vanishes, as K-1 says.
- **Quaternion kinematics (§4.4).** CV-250 defines `q` as the passive L→B rotation, with `C_BL` equal to the transpose of the active matrix. So `v^L = q ⊗ v^B ⊗ q*`, and `q̇ = ½·q ⊗ (0, ω^B)` is the right form. All four component equations were checked against the Hamilton product.
- **Gravity (§5.2).** Uniform, `g^L = (0, 0, g)` in NED, applied at the centre of gravity, with no gradient moment.
- **Atmosphere (§5.3).** The base pressures follow from the layer equations: computed 22 632.06, 5 474.888 and 868.0187 Pa against 22 632.06, 5 474.889 and 868.0187 Pa. ρ(0) = 1.2250 kg/m³, and ρ(47 km) = 1.4275×10⁻³ kg/m³. The exponent sign and the isothermal branch are correct. The limits are G2-F07 and G2-F08.
- **Wind (§5.4).** `s(τ) = ½(1 − cos(πτ/T_r))`. Its rate is zero at both ends and peaks at `π/(2T_r)`, and its second derivative peaks at `π²/(2T_r²)`, as stated. With [P-SYS-560] = 25.722 m/s and 2 s, the wind rate is at most 20.2 m/s². Events do not overlap, so the largest wind is [P-SYS-430] + [P-SYS-560].
- **Drag (§5.5).** `D = −½ρ·[P-DYN-100]·|v_a|·v_a` gives no lift and no moment.
- **Sensed acceleration (§8).** `f = (F_c + D)/m = a − g` under T1. It is 0 in free fall and g in a hover.
- **Mass-properties reference derivation (§6).** The uniform-capsule formulas were rederived: the hemisphere about the capsule centre is `2R²/5 + H²/4 + 3HR/8`. For 12 m × 4 m and 1000 kg uniform: I_xx = 1900 and I_yy = I_zz = 10 650 kg·m².
- **Credibility checks:**
  - The C-2 quasi-steady correction `v_t·(1 − v_t²·ρ'/(4gρ))` is right to first order (its accuracy is G2-F02).
  - The C-3 precession rate is `(I_t − I_xx)·p/I_t`.
  - The C-4 closed form is `v = v_0 + (F/ṁ)·ln(m_0/m)`, and the mass hold over a step costs `ṁΔt/(2m)`, as stated.
  - The C-5 expectations under T1 are right.
- **Ground contact and step input hold (§9, §10.2).** These are consistent with DD-070, DD-080 and DD-100, and with FU's start-of-step convention (CV-840). The DYN and FU step timing agree: the mass of step k is dry plus the remaining fuel at the start of step k, held over k to k+1; the flow of step k uses the effector outputs of step k. The exception is the measurement point of G2-F12.

### 3.2 Credibility checks C-1 to C-8: configuration, tolerance and horizon

| Check | Closed form holds? | Tolerance and horizon coherent? |
| --- | --- | --- |
| C-1 | Yes. Constant acceleration, and independent of rotation under T1. | The tolerance is easy to meet. Run time is limited by the contact step (at most about 196 s in vacuum below 47 km). Relative error is undefined at step 0 (G2-F14). |
| C-2 | First order only. | **No** (G2-F02). |
| C-3 | Yes. | **No:** the horizon cannot be reached (G2-F01). The configuration's "any initial body rates" needs an upper bound for any fixed-step integrator. Recommended: bound the rates by the reachable envelope. |
| C-4 | Yes. | Yes. The hold condition `ṁ·Δt/(2m) < 10⁻⁵` is met by a wide margin for any realistic ṁ. |
| C-5 | Yes. | **No:** the horizon cannot be reached (G2-F01). Relative pitch and roll tolerance: G2-F14. |
| C-6 | Yes. | Yes in SC-110. Inherits G2-F01 through C-3 and C-5. |
| C-7 | Yes. | Ambiguous reference altitude (G2-F07). |
| C-8 | Yes. | Yes with per-step data (G2-F22). [P-FU-060] = 10⁻⁶ kg is ample against a typical rounding drift of about 5×10⁻¹⁰ kg over 1.8×10⁷ steps. |

### 3.3 D66 and fuel-budget arithmetic

All figures recomputed from the database values.

| Item | Computed | Database / record | OK |
| --- | --- | --- | --- |
| Drag at [P-SYS-230] = 154.333 m/s, ρ = 1.225 kg/m³, [P-DYN-100] = 5 m² | 72 945 N (4.96 × max weight) | — | — |
| k_t giving exactly 8 h at 300 kt (flow = k_t·√(D² + (m·g)²), mass falling from 1500 to 1000 kg) | 2.3467×10⁻⁷ kg/(N·s) | P-FU-040 note "2.347e-7, rounded down" | Yes |
| Endurance at 300 kt with k_t = 2.34×10⁻⁷ | 8.02 h | ≥ [P-SYS-290] = 8 h | Yes |
| Hover endurance with no margin, ln(1.5)/(k_t·g) | 176 692 s = 49.08 h | — | — |
| Hover endurance with [P-FU-100] = 0.05 | 168 278 s = 46.74 h | P-SYS-280 note "46.7 h", value 165 600 s = 46 h | Yes |
| L2-AER-FU-290: [P-FU-030]·(exp(1.05·k_t·g·[P-SYS-280]) − 1) | 490.35 kg (exponent 0.39901) | ≤ [P-FU-010] = 500 kg | Yes (9.6 kg margin) |
| Range at [P-SYS-230] for [P-SYS-290] | 4 444 790 m = 2400.0 NM | P-SYS-220 = 4 444 800 m | Yes |
| Lateral acceleration at 300 kt ground speed and [P-SYS-270] | 9.697 m/s² | ≤ [P-AF-200] = 9.807 | Yes, but only at a ground speed of 300 kt (G2-F03) |
| [P-SYS-270] = 3.6°/s | 0.0628319 rad/s | 0.062832 | Yes |
| P-SYS-460 note, deceleration from [P-SYS-230] at 1 g | 15.7 s | "about 16 s" | Yes |
| P-AF-230 note (0.1 g up to 2000 ft/min; level-off distance) | 10.36 s; 52.6 m | "10.4 s", "52.6 m" | Yes |
| [P-SYS-500] = √(2·g·0.6096) | 3.4578 m/s | 3.458 | Yes |
| [P-SYS-570] equivalence: 107 m / [P-SYS-430]; and 2 s / [P-SYS-480] | 2.08 s; 20 | "about", "20 times" | Yes (G2-F25) |
| Gust drag-rate transient over [P-SYS-480] at 231.5 m/s airspeed and dry mass | 28.6 kN/s, giving 2.86 m/s² | below [P-FC-020] = 4.90 m/s² | Plausible; C4 confirms at I1 |
| Peak sensed acceleration, unpowered fall from [P-SYS-200] at rest (dry, drag on) | 19.6 m/s² = 2.0 g at 21.9 km | ≤ [P-SYS-120] = 3 g | Yes: L1-AER-290 holds after exhaustion too |
| P-SYS-400 lower bound | 39.6 kN | — | G2-F04 |
| P-SYS-410 lower bound, reading (i) / (ii) | 186.2 kN / 95.0 kN | — | G2-F04 |

Two side notes, neither a defect. The exhaustion fall from high altitude is supersonic in places (349 m/s at 22 km); MS-DYN §5.5 defines the drag coefficient as Mach-independent, which is a definition of the fictional vehicle. Rotation costs little fuel at heading-rate onsets, since [P-FU-050] is equal in number to [P-FU-040] (D66).

## 4. Interfaces

**DYN ↔ FU, inside the vehicle model and defined in MS-DYN.** Units are SI throughout. Frames follow CV-340 and CV-350: mass properties about the centre of gravity in body axes. Step timing is consistent (section 3.1). The one conflict is the centre-of-gravity item and the inertia name on I-04 (G2-F05). No duplicate ownership remains between DYN and FU, apart from the authorship of the mass distributions (G2-F16).

**Vehicle-model boundary.** L2-AER-DYN-320 and -340 give the vehicle state only; L2-AER-FU-130 and -140 give the mass properties and the fuel state. Together they match L1-AER-430. The ICD home is open (TT-720). L2-AER-DYN-330 and L2-AER-FU-140 use the same frame-start sampling.

**Notes toward subsystems not yet written.** These are not defects of DYN or FU.

- **EF (C3).** L2-AER-DYN-180 expects EF to give one resultant force and moment per step ("EF sums its effector outputs", rationale). L2-AER-FU-070 expects a single MS-DYN mapping that both DYN and FU apply to the per-effector outputs (IN-C2-11). I1 should fix who computes the resultant, so that it is computed once. EF also needs to:
  - state the step-0 effector outputs (IN-C1-12), which DD-080 needs for the step-0 accelerations;
  - write a child of L1-AER-360 showing a hold at no more than the weight within [P-FU-100] (IN-C2-23);
  - give zero output from the first step at which fuel is not available (IN-C2-20).
- **FC (C4).** Under T1, a turn at speed needs a lateral force of m·V_H·r (IN-C1-32). The sensed acceleration is not part of the boundary state (IN-C1-35, N-C1-04; FA I-07 still lists it). If the crew limit is enforced in a closed loop, FC must compute it from the control force, the drag and the mass, or I1 adds it to the boundary ICD. The gust shares of [P-FC-020] and [P-FC-010] are checked against [P-SYS-570] at I1.
- **AF (C5).** The heading rate at speed, see G2-F03. The annunciations after exhaustion (D68).
- **TST, for the plan extension.** A harness that drives DYN with a prescribed force and mass for C-4 and L2-AER-DYN-300 (2) (IN-C1-24). The wind-envelope requirement (IN-C1-25). Per-step recording of the vehicle-model interfaces for analysis runs (IN-C2-30, and G2-F12). An initial-condition error item (IN-C2-31).

## 5. Requirement quality (METHODOLOGY §13.1) and confirmed OK

- **The checklist items hold on all 74 records:** one "shall", the element as subject, an EARS pattern, no numbers in statements, parameters by ID, a rationale, a source, parents or Derived, and a direct method with a procedure ID. Lint confirms most of these, and the parameter-reference sweep by script found no parameter missing from PARAMETERS.yaml. Types are Model fidelity 23, Constraint 17, Interface 17, Functional 14, Documentation 2 and Performance 1. Methods are Inspection 30, Test 25, Analysis 17 and Demonstration 2.
- **COMPOUND warnings (38 on L2).** Each was read. They are closed enumerations (state elements, forces, initial-condition items), one envelope and its complement (L2-AER-DYN-510, -520), or one computation with its inputs. None forms a tree of cases (D30).
- **Decisions implemented:** D18 with the kinematic terms list (with G2-F06), D20 (DD-090), D37 and D53 (two speed limits and no acceleration limit), D45 (centre of gravity), D51 and D62 (wind envelope), D57 (K-1 zero in normal operation), D59 and D63 Q4 (L2-AER-DYN-420, L2-AER-FU-270), D61 (L2-AER-DYN-040, L2-AER-FU-180), D64 (T1, D1, capsule, gust shape, gravity Set) and D65 (DD-110 to DD-140, the per-step integral, rejection of the initial fuel).
- **One record is Derived:** L2-AER-DYN-540, with DD-070 Accepted. All the design decisions DD-050 to DD-140 are in the register as Accepted.
- **Glossary.** The terms used in the DYN and FU statements are defined (C1 and C2 merge), apart from the two meanings of *Vehicle state* (G2-F15).

## 6. D69 impact (input to task B3; not findings)

D69 adds a landing gear, a ground start with the effectors off, and the Takeoff and Land modes. It invalidates or changes the following.

**DYN records.**

- L2-AER-DYN-100, -110 and MS-DYN §5.1 ("Ground contact is not a force"): resting on the gear needs a ground reaction or a defined resting state. This also changes the closed list of L1-AER-050 and L0-CON-090.
- L2-AER-DYN-500 to -550 and MS-DYN §9, the whole of the ground contact model:
  - contact is at the gear contact points, [P-DYN-040] below the body, not at altitude zero (TT-820: the centre of gravity rests at about R + [P-DYN-040] = 3.4 m);
  - classification at touchdown under Land;
  - L2-AER-DYN-540 ("altitude of zero");
  - L2-AER-DYN-550 ("keep the vehicle state of the contact step"), which is incompatible with a Takeoff after a rest and with a landing that does not end the run;
  - L2-AER-DYN-530, where the TST ends the run on the event.
- L2-AER-DYN-430, MS-DYN §10.3 "Initial state" and IN-C1-21 ("every run starts airborne"): the ground start.
- L2-AER-DYN-300, -310, MS-DYN §3.3 and §8: the sensed and vehicle acceleration on the ground; the step-0 accelerations with the effectors off (IN-C1-12).
- L2-AER-DYN-600, -610, -620, -640 and checks C-1 to C-5: every "until the contact step" or "to the contact step" clause. The G2-F01 fix should be made with the gear in view.
- L2-AER-DYN-220 and MS-DYN §2: the gear geometry. P-DYN-040 is missing from MS-DYN §12 and §13.
- L2-AER-DYN-700: the "ground contact model" section.
- [P-DYN-270] and the glossary *Accuracy horizon* (G2-F09): with a rest on the ground there is no longest run.
- Glossary *Airborne*, *Ground contact* ("no landing gear") and *Contact step*.

**FU records.**

- L2-AER-FU-020 and -030: the initial fuel of a ground start. A zero-fuel run now stays on the ground, which makes the zero-fuel cases of L2-AER-FU-090 and -200 trivial.
- L2-AER-FU-080 ("from [P-FU-010] to ground contact") and -110 ("from fuel exhaustion to ground contact"): a run no longer ends at the first contact.
- L2-AER-FU-290 and SC-110 (hover-endurance variation): the run now begins with a Takeoff, so its fuel and time count against L1-AER-360 "from an initial fuel mass of [P-FU-010]", while the closed form starts at the hold.
- L2-AER-FU-040 rationale ("fuel is consumed in each flight condition"). DD-110 already gives zero flow at zero effector output, so the effectors off on the ground need no new consumption term. That is consistent with D69's "no fuel consumption".

## 7. TBD/TBR list checked: yes

- **Record fields against the register.** Every TT row cited by a DYN or FU TBD/TBR field exists, is Open and lists the cited parameter: TT-040, -070, -090, -110, -120, -130, -140, -600, -650, -680, -720, -740, -750, -760, -770, -780, -790 and -800.
- **Fields that refer to answered questions:**
  - L2-AER-FU-230 cites #59 and TT-580 (G2-F13).
  - L2-AER-DYN-120 has the field "—", which is correct, but its rationale is stale (G2-F19).
  - No other field refers to an answered question.
- **Cited TBR parameters missing from record fields** (G2-F20): a consistency item only; the register covers each at parameter level.
- **Register rows out of date** (L1 field copies; to refresh with the B3 change requests):
  - TT-340 (L1-AER-060) and TT-710 (L1-AER-290) still cite P-DYN-010 TBR, although TT-150 is Closed (Set, D64).
  - TT-580 is Open on #59, which D68 answered.
  - TT-470 copies "P-SYS-230 … TBD" (now Set, D66).
  - TT-390, -400, -410, -420, -440, -480, -490, -500 and -510 copy "value TBD" for parameters that are now TBR with values (D64 to D67).
- **Missing linkage.** The D66 derivation chain spans TT-110, TT-750 and TT-800 (G2-F18).
- **MS-DYN §13.** It matches TT-650, -740, -750, -760, -780 and TT-140, apart from the closure date of TT-740 (G2-F23).
- **Known and accepted:** TT-810, -820 and -830 (D69, B3); TT-780 (§6, §7 content).

## 8. Questions for the owner

| Q | Question (finding) | Recommended answer |
| --- | --- | --- |
| Q1 | Is [P-SYS-230] a ground speed (CV-480, as L1-AER-310 and the panel selector use it) or a true airspeed at which the effectors saturate (D66 wording)? (G2-F03) | **Ground speed.** Keep D66's 300 kt as the still-air anchor of [P-SYS-290], where ground speed and true airspeed coincide. Delete "as true airspeed; the effectors saturate there" from P-SYS-230. Have C5 bound the commanded heading rate so that the horizontal speed times the heading rate stays within [P-AF-200]. This needs no CR on the baselined L1. |
| Q2 | With D66 and [P-DYN-100] = 5 m², the horizontal authority must exceed the upward authority by 2.4 to 4.7 times (95 to 186 kN against 39.6 kN). D46 says it is smaller. Which gives way? (G2-F04) | **Revise the wording of D46:** "The weight is carried along −z_B only; the authority in the other five directions is set by the drag at maximum speed." Keep [P-DYN-100] and D66. Shrinking the drag area to about 0.5 m² would re-derive [P-FU-040], [P-FU-050] and [P-SYS-280], and would leave a capsule with an implausibly low drag. |
| Q3 | Under isotropic drag (D64, option D1), oblique flow couples the axes through the shared magnitude \|v_a\|, although motion along one axis gives drag along that axis only. Is D18 met in this reading? (G2-F06) | **Yes.** Confirm, and record the reading in D64 and in the MS-DYN kinematic terms list, so that the G4 roll-up of L0-CON-030 has an explicit basis. |
| Q4 | Is the 8 h endurance at maximum speed ([P-SYS-290], Set) a requirement to be verified, or only the anchor from which [P-FU-040] and [P-FU-050] are derived? (G2-F18) | **Anchor only.** Say so in its description, and link TT-110, TT-750 and TT-800, so that a change of [P-DYN-100] at I1 re-derives [P-FU-040], [P-FU-050] and [P-SYS-280] and re-checks L2-AER-FU-290. |

## 9. Recommended exit decision

**Rework and re-review.** This early, partial G2 does not support a baseline yet.

**What is sound.** The DYN and FU decomposition is complete: every DYN or FU share of the 35 live L1 parents is covered, and the sufficiency arguments hold, apart from L1-AER-010 and L1-AER-720. The equations of motion, the variable-mass treatment, the quaternion kinematics, the atmosphere, the wind and drag models, the sensed acceleration and the fuel accounting are physically correct. The D66 arithmetic and the L2-AER-FU-290 fuel budget close with the database values.

**Rework needed in MS-DYN:**

- the credibility-check configurations: the C-3 and C-5 horizon cannot be reached (G2-F01), and the C-2 closed form fails at the stated tolerance above about 5 km (G2-F02);
- the C-7 reference altitude (G2-F07);
- the atmosphere range (G2-F08).

**Rework needed in the parameter budgets.** These need owner rulings first:

- the maximum speed defined both as a ground speed and as a true airspeed (G2-F03, Q1);
- the conflict between D46 and the drag at maximum speed (G2-F04, Q2);
- the D66 derivation chain (G2-F18, Q4);
- the D18 reading of isotropic drag (G2-F06, Q3), a confirmation only.

**Moderator closure.** The Minor and Editorial findings can be closed by the moderator once the authors have applied them.

**Re-inspection.** Re-inspect after B3 (D69) has reworked the ground-contact, initial-condition and fuel records (section 6) and C3 has written EF. Do it as one delta inspection of DYN, FU and EF with MS-DYN §5.3, §6, §7, §9, §11 and §12, so that the check configurations are fixed once, with the gear in view.
