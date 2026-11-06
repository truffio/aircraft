# C1 rework — disposition of the G2 findings and the D69 changes (DYN, MS-DYN)

Task C1 rework, 2026-11-06, from branch c1_c2 at ffa195f (D73). Inputs: `reviews/G2/inspection_C1_C2.md` (findings and §6 "D69 impact"), owner rulings D72 and D73, the approved B3 package (`work/B3/`: CR-B3-01 to -41, L1-AER-900 to -970, impact list, P-DYN-050, P-SYS-580), the C2 rework (a99ad88, read for coordination only) and the C3 staging files. Outputs: `work/C1/L2_DYN.md` (version 2), `specs/MS-DYN.md` (version 2), and the staging files of this folder.

## 1. G2 findings on DYN and MS-DYN

| Finding | Severity | Ruling | Change made | Where | Status |
| --- | --- | --- | --- | --- | --- |
| G2-F01 C-3, C-5 horizon cannot be reached | Major | D72: gravity-free check configuration, [P-DYN-270] = 600 s, no 48 h check | C-3 and C-5 run in the new **gravity-free check configuration** ([P-DYN-010] = 0 in the check's parameter set), zero fuel, zero initial vertical velocity, airborne start; body rates bounded by [P-SYS-270], horizontal speed by [P-SYS-230]. §10.3 states which check holds over which span; no check over a long hold. L2-AER-DYN-620, -640 statements and criteria; -440 demonstrates the configuration. | MS-DYN §5.2, §10.3, §11; L2-AER-DYN-440, -620, -640; P-DYN-270 description (param_proposals §4) | Closed by author |
| G2-F02 C-2 closed form not accurate enough | Major | D72: state release height and checked band | C-2 now: release at rest vertically at 3 000 m, horizontal velocity equal to the wind velocity; checked from 1 500 m down to the contact step (layer 0). Residual of the neglected physics recomputed by C1 (RK4 at 0.002 s, dry mass 1000 kg, 5 m²): at most 3.04·10⁻⁴ in still air and in wind (air-relative velocity vertical), against [P-DYN-210] = 10⁻³. The "tenth" claim is replaced by the achieved residual. Release at rest relative to the ground in a 100 kt wind leaves a 1.7·10⁻² horizontal error at 1 500 m, so the wind case starts at the wind velocity; L2-AER-DYN-140 criterion (1) changed accordingly (same defect class). A release at 3 000 m checked from 2 000 m gives 4.2·10⁻³ (not settled), which is why the band starts at 1 500 m. | MS-DYN §11 C-2 and notes; L2-AER-DYN-140, -610 | Closed by author |
| G2-F03 / Q1 P-SYS-230 ground or airspeed | Major | D72: ground speed | MS-DYN §4.5 note (turn acceleration from ground velocity; C5 bounds heading rate so V_H·r ≤ [P-AF-200]); §5.5 budget form: largest airspeed = [P-SYS-230] + [P-SYS-430] + [P-SYS-560]; IN-C1-32, -33. No DYN record states P-SYS-230 as an airspeed. | MS-DYN §4.5, §5.5, §12; interface_needs | Closed by author (DYN share) |
| G2-F04 / Q2 D46 vs drag | Major | D72: D46 revised, [P-DYN-100] kept | No DYN text cited D46. §12 pedigree of P-DYN-100 and its note record the ruling. | MS-DYN §12; param_proposals §4 | Closed (no DYN change needed) |
| G2-F05 CG across I-04 | Minor | As recommended (CG does not cross); FA aligned by CR-B3-39 | L2-AER-DYN-210 takes "the vehicle mass and the inertia tensor", rationale cites G2-F05 and CR-B3-39; MS-DYN §6 states that the CG does not cross I-04. Agreed with the C2 rework (IN-C2-19 asks exactly this; L2-AER-FU-120 drops the CG). Note: the C1 brief suggested "FU provides it"; C1 followed the G2 recommendation as accepted by D72 and the approved CR-B3-39, which C2 also follows. | L2-AER-DYN-210; MS-DYN §6; IN-C1-01, -02, -46 | Closed by author |
| G2-F06 / Q3 isotropic drag and D18 | Minor | D72: confirmed | Recorded in MS-DYN §4.5 (new paragraph "Drag and D18"), §5.5 table row, L2-AER-DYN-050 rationale and criteria, -190 rationale, coverage table row L1-AER-020. | MS-DYN §4.5, §5.5; L2-AER-DYN-050, -190 | Closed by author |
| G2-F07 C-7 reference altitude | Minor | As recommended | C-7 reference computed from the standard's defining equations at geopotential altitude = h (DD-090), cross-checked against the table read by geopotential altitude; L2-AER-DYN-150 criteria. | MS-DYN §11 C-7; L2-AER-DYN-150 | Closed by author |
| G2-F08 Atmosphere range | Minor | As recommended | Layer 0 continued below zero; layers 4 to 6 of the 1976 standard added up to 84 852 m (base pressures recomputed: 110.9063, 66.938 87, 3.956 420 Pa); zero density above. Proposed as DD-C1-07 (extends DD-090). L2-AER-DYN-150 criterion (2). | MS-DYN §5.3; L2-AER-DYN-150; issues §7 | Closed by author (DD-C1-07 for owner acceptance at the delta inspection) |
| G2-F09 Accuracy horizon / glossary | Minor | D72 | MS-DYN §10.3, §12; P-DYN-270 description proposal; glossary *Accuracy horizon* changed by B3 (CR-B3-37). | MS-DYN §10.3, §12; param_proposals §4 | Closed by author |
| G2-F12 Acceleration-check data | Minor | As recommended | L2-AER-DYN-300 (4) and -310 name the control force, mass and wind of the previous step and use per-step records of the vehicle-model interfaces; new IN-C1-26 to the TST. | L2-AER-DYN-300, -310; IN-C1-26 | Closed by author |
| G2-F14 Undefined tolerances | Minor | As recommended | Relative error defined in MS-DYN §11 common conditions (from step one, against the largest change so far, vector norms); C-5 pitch and roll bounded absolutely in radian, yaw rate relative to its initial magnitude. L2-AER-DYN-600, -630, -640 criteria. | MS-DYN §11; L2-AER-DYN-600, -630, -640 | Closed by author |
| G2-F15 Two meanings of vehicle state | Minor | As recommended | L2-AER-DYN-020 now holds the "integrated state" (MS-DYN §3.1 term); *Vehicle state* keeps the glossary meaning; new glossary term *Integrated state*. -010 criteria use it. | L2-AER-DYN-010, -020; MS-DYN §3.1; glossary_proposals §3 | Closed by author |
| G2-F16 MS-DYN §6, §7 ownership and slots | Minor | As recommended | MS-DYN §6 assigns the distributions and the derivation to C2; the §6 and §7.2 slot notes list the five FU models of L2-AER-FU-280; slot content not written by C1 (merge of `work/C2/ms_dyn_s6_s7_fu.md` and `work/C3/ms_dyn_s7_effectors.md` at I1). | MS-DYN §6, §7 | Closed by author (content at I1, TT-780) |
| G2-F19 Stale status words | Editorial | — | DD-050 "proposed" → accepted (-110); "TBR, TT-150" → Set (-120, MS-DYN §5.2); DD-070 "proposed" (-540) now cites the revision; MS-DYN §3.3 (now §3.4) "proposed for an update" → CR-C1-02; "glossary proposal" removed (-500, MS-DYN §9). | L2-AER-DYN-110, -120, -500, -540; MS-DYN | Closed by author |
| G2-F20 Parameters vs TBD/TBR fields | Editorial | — | Each DYN record's TBD/TBR field now lists exactly the TBR/TBD parameters its statement and criteria use, with the TT row: -060, -140, -240, -410, -440, -610, -620, -640 and the new records. | L2_DYN.md | Closed by author |
| G2-F22 C-8 per-step data | Editorial | — | C-8: "the FU fuel mass flow of each simulation step", over SC-110 with the rest on the ground. | MS-DYN §11 C-8 | Closed by author |
| G2-F23 Metadata | Editorial | — | MS-DYN header D1–D73; §13 closure of P-DYN-020, -030 = 2026-11-30 (TT-740); K-3 named "gravity, drag, the control force and the ground reaction" in MS-DYN §4.5 and L2-AER-DYN-050; coverage row L1-AER-070 adds -410. L1-AER-200 leg number and the L2.md / DECISIONS headers are B3's / the orchestrator's. | MS-DYN; L2_DYN.md | Closed by author (DYN share) |
| G2-F25 Rise-time justification | Editorial | — | MS-DYN §5.4: equivalence stated for a vehicle near rest; the rise time is a definition of the envelope. | MS-DYN §5.4 | Closed by author |
| G2 §3.2 C-3 rate bound (note) | — | — | Body rates bounded by [P-SYS-270]. | MS-DYN §11 C-3 | Closed |

Not C1's: G2-F10, -F11, -F13, -F17, -F18, -F21, -F24 (FU, registers, parameters).

## 2. D69 (landing gear) — changes from the B3 package and G2 §6

| Item (B3 impact list §1, §3; G2 §6) | Change | Records / sections |
| --- | --- | --- |
| Gear geometry (L1-AER-900) | Four contact points (±a, ±R/2, λ·(R + [P-DYN-040])); extended [P-DYN-040] below the body at level attitude; retracted inside the body; no mass, drag or moment effect (DD-C1-08) | MS-DYN §2.5; new L2-AER-DYN-250, -260 |
| Height above the ground and lowest point | `h_G = h − R − a·|sin θ|` (CV-400); lowest point of the vehicle = min over body and gear points; altitude stays the CG altitude | MS-DYN §2.6; L2-AER-DYN-500, -470 |
| Gear movement (L1-AER-910) | Constant-rate transit over [P-DYN-050] while airborne; held extended on the ground; command from AF per frame | MS-DYN §9.1; new L2-AER-DYN-270, -280, -360 |
| Gear state | Gear position and on-the-ground flag, a separate DYN item, to AF (boundary) and TM | MS-DYN §3.3, §3.5; new -290; -320, -340, -350 |
| Ground reaction (L1-AER-050 v2, -920) | `R = −(m·g + D + C_LB·F_c)`, `M_R = −M_c` while on the ground; enters the closed force list; not a control force | MS-DYN §5.1, §9.6; -100, -110, -180; new -580 |
| Rest and liftoff (L1-AER-920) | State held at the rest state; liftoff at the first step at which the upward control force exceeds m·g (DD-C1-11) | MS-DYN §9.6; new -570, -590 |
| Detection | While airborne, lowest point of the vehicle reaches the datum plane; none on the ground; resumes after liftoff | MS-DYN §9.3; -500 |
| Classification (D68, D73 B3-3) | Landing = gear extended, gear lowest, fuel available, both speed limits; otherwise crash (complement) | MS-DYN §9.4; -510, -520; new -370 (fuel availability from FU) |
| DD-070 consequences | Landing: rest state at the propagated horizontal position and heading (new -560); crash: raised so the lowest point is on the datum plane (-540, Derived, DD-070 revised by DD-C1-10); hold after a crash only (-550) | MS-DYN §9.5, §9.7 |
| Events | One record per contact; several landings per run; TST ends the run on a crash only | MS-DYN §9.8; -530 |
| Sensed and vehicle acceleration (-300, -310) | Ground reaction in f; 1 g at rest; zero vehicle acceleration on the ground; propagated values at a contact step (DD-C1-11, supplement to DD-080) | MS-DYN §3.4, §8; -300, -310 |
| Initial condition (L1-AER-660 v2, -950; B3-1) | Gear extended = start on the ground → rest state (DD-C1-09) (new -450), inconsistent items rejected (new -460); gear retracted = airborne test start (-430), body at or below ground rejected (new -470) | MS-DYN §9.9, §10.3 |
| Checks | C-1, C-2 airborne starts with the gear retracted; C-3, C-5 gravity-free; new C-9 rest and liftoff; C-8 with the rest | MS-DYN §11; -570 to -590, -600 to -640 |
| MS-DYN content list (L1-AER-720 v2) | Landing gear model and ground contact model named | MS-DYN §9; -700 |
| Pedigree and trace | P-DYN-040, -050, P-SYS-580, P-AF-210, P-SYS-200, -230, -270 in §12; open items §13; trace §14 with L1-AER-900 to -950 | MS-DYN §12 to §14 |
| Coverage | New parents L1-AER-900, -910, -920, -950 (DYN allocations of the B3 records); rows -050, -260, -270, -280, -290, -430, -640, -660, -720 revised | L2_DYN.md coverage table |

## 3. Record counts (DYN section)

- **Total:** 59 records (45 before, 14 new, 0 deleted): Model fidelity 20, Functional 14, Constraint 12, Interface 12, Documentation 1; Inspection 23, Test 21, Analysis 14, Demonstration 1.
- **Changed (version 2):** 35 — L2-AER-DYN-010, -020, -050, -060, -100, -110, -120, -140, -150, -180, -190, -210, -220, -240, -300, -310, -320, -340, -350, -410, -420, -430, -440, -500, -510, -520, -530, -540, -550, -600, -610, -620, -630, -640, -700.
- **New (version 1):** 14 — L2-AER-DYN-250, -260, -270, -280, -290, -360, -370, -450, -460, -470, -560, -570, -580, -590.
- **Unchanged:** 10 — -030, -040, -070, -130, -160, -170, -200, -230, -330, -400.
- **Deleted:** none (no ID removed or reused).

## 4. Checks run (scratch assembly, reverted; no shared file edited)

- `lint.py --file work/C1/L2_DYN.md`: 0 errors, 35 COMPOUND warnings (judged in `issues.md` §7.4).
- `assemble.py L1, L2` and `trace_check.py` on a scratch copy with the B3 records L1-AER-900 to -970 added: no DYN error (no orphan, no unknown parent, DERIVED L2-AER-DYN-540 resolves to DD-070); no L1 record allocated to DYN childless. The remaining errors are CHILDLESS records of subsystems not yet written and one EF DERIVED (DD-C3-04 not registered), not C1's.
- `param_check`: P-DYN-050 and P-SYS-580 resolve once the B3 parameters are merged (applied on c1_c2 by the parallel B3 task).
