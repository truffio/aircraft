# C1 — Interface needs (DYN)

What the dynamics model (DYN) needs from, and provides to, the other subsystems and the TST, and which ICD holds each item. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2 as changed by CR-B3-39 (D73). "MS-DYN internal" means the item stays inside the vehicle model and is defined in MS-DYN (§6, §7, §9, §10.2), not in an ICD. C1 does not coordinate with the other agents directly; the integration step (I1) resolves these. Version 2 (G2 rework and D69): IDs are never reused; answered needs keep their ID with a status; new needs are IN-C1-26, -27 and -41 to -47.

## 1. Needed by DYN

| ID | From | Need | Interface, home | Driven by | Status |
| --- | --- | --- | --- | --- | --- |
| IN-C1-01 | FU (C2) | At each simulation step: the vehicle mass and the inertia tensor about the CG in body axes (three principal moments, zero products). One value per step, held over the step (MS-DYN §10.2). One name, "inertia tensor", on both sides (G2-F05). | I-04; MS-DYN internal (§6) | L1-AER-180, -220; L2-AER-DYN-030, -040, -210 | Agreed with C2 (IN-C2-19) |
| IN-C1-02 | FU (C2) | The CG at the body origin at every fuel state; **the CG position does not cross I-04** (G2-F05, FA I-04 as aligned by CR-B3-39). Mass distribution symmetric in each body coordinate plane (D61). | MS-DYN §6 | L1-AER-210, -220; L2-AER-DYN-200, -210 | Agreed with C2 (IN-C2-19) |
| IN-C1-03 | FU (C2) | Text for the MS-DYN **mass-properties model** (§6). | MS-DYN §6 (C2 slot) | L1-AER-220, -720 | Delivered: `work/C2/ms_dyn_s6_s7_fu.md`; merge at I1 (IN-C2-52). C1 left the slot unfilled in this rework. |
| IN-C1-04 | FU (C2) | Text for the MS-DYN **fuel model** (§7.2), with the five FU models of L2-AER-FU-280 (G2-F16). | MS-DYN §7.2 (C2 slot) | L1-AER-160, -720 | Delivered as IN-C1-03; merge at I1 |
| IN-C1-05 | FU (C2) | No `J̇·ω` term (MS-DYN §4.1 assumption 4). | MS-DYN §4.1 | L0-ASM-090 | Confirmed (IN-C2-14) |
| IN-C1-10 | EF (C3) | Control force and moment per step, held, zero at exhaustion and with the effectors off. | I-02; MS-DYN §7.1 | L2-AER-DYN-180 | Answered (C3, DD-C3-05) |
| IN-C1-11 | EF (C3) | Text for the MS-DYN **effector model** (§7.1). | MS-DYN §7.1 (C3 slot) | L1-AER-100, -720 | Delivered: `work/C3/ms_dyn_s7_effectors.md`; merge at I1 (IN-C3-01) |
| IN-C1-12 | EF (C3) | Effector outputs at step 0. | MS-DYN §3.4, §7.1 | L2-AER-DYN-300, -310 | Answered (C3): zero before the first commands; zero in a ground start |
| IN-C1-20 | TST, I1 | The wind velocity with each step command (north, east; down zero), the wind at `t_k`. | I-25; ICD-AER-TST | L2-AER-DYN-140, -410 | Open (I1) |
| IN-C1-21 | TST, I1 | **Initial condition (revised for D69):** position and velocity in L, attitude as a unit quaternion (CV-250), body rates in B, and the **landing gear position**, extended or retracted only. Gear extended = start on the ground (DD-C1-09): DYN sets the rest state from the horizontal position and the heading and replaces the altitude by the rest altitude `[P-DYN-030]/2 + [P-DYN-040]`; I1 decides whether the ICD carries the altitude for a ground start (recommended: it may be omitted). Non-zero velocity, body rates, pitch or roll in a ground start, or a body at or below the ground in an airborne start, give an initial-condition error (L2-AER-DYN-460, -470). Gear retracted = airborne start, for test runs and credibility checks only (D73, B3-1). "Every run starts airborne" is withdrawn. | I-21, I-27; ICD-AER-TST | L1-AER-660, -950; L2-AER-DYN-430, -450 to -470 | Open (I1) |
| IN-C1-22 | TST, I1 | The vehicle parameter set of the run, with each DYN parameter (P-DYN-010 to -400), identified by a version (N-350). The gravity-free check configuration sets P-DYN-010 to zero (D72). | I-21; ICD-AER-TST | L2-AER-DYN-440 | Open (I1) |
| IN-C1-23 | TST, I1 | The TST ends the run on a **crash** event only; a landing does not end the run (I-41 as revised). A step commanded after a crash leaves the state unchanged (L2-AER-DYN-550). | ICD-AER-TST | L2-AER-DYN-530, -550 | Open (I1) |
| IN-C1-24 | TST (test harness) | A prescribed-input harness that drives DYN with a prescribed control force and vehicle mass in place of the EF and FU outputs: checks C-4, C-9 (b) and the hover case of L2-AER-DYN-300. Zero fuel, `[P-DYN-100] = 0` and `[P-DYN-010] = 0` parameter sets for C-1 to C-5. | Test procedures (V1); TST branch (D44) | L2-AER-DYN-300, -590, -600 to -640 | Open |
| IN-C1-25 | TST | The TST applies only winds inside the wind envelope of the MS-DYN wind model, including the liftoff limit [P-SYS-580] (D73, B3-2). | ICD-AER-TST; TST branch | D51, D62, D73 | Open |
| IN-C1-26 | TST, I1 | **Per-step recording for analysis runs (G2-F12):** the vehicle-model interfaces at each simulation step (control force and moment, vehicle mass, wind, ground reaction, gear state), without changing the Aeronef configuration, as FU (IN-C2-30) and EF (IN-C3-31) need. AN-DYN-300, -310 use the inputs of the previous step, which the operational data do not hold. | TST branch; ICD-AER-TST | L2-AER-DYN-140, -300, -310, -580 | Open |
| IN-C1-27 | FU (C2) | **Fuel availability of each step to the ground contact model** (D68, D73 B3-3): the same FU item EF takes, over I-03. | I-03; MS-DYN §7.2, §9.4 | L1-AER-260, -270; L2-AER-DYN-370, -510, -520 | Agreed with C2 (IN-C2-50) |
| IN-C1-41 | AF (C5) | **Landing gear command** (extend or retract), once per control frame, across the vehicle-model boundary. Before the first command the commanded position is the initial gear position. A retraction commanded on the ground takes effect at the first airborne step. | I-43; vehicle-model boundary ICD | L1-AER-430, -910; L2-AER-DYN-270, -360 | Open (C5, I1) |

## 2. Provided by DYN

| ID | To | What DYN provides | Interface, home | Driven by | Status |
| --- | --- | --- | --- | --- | --- |
| IN-C1-30 | NAV (C6), FC (C4) | At the start of each control frame, the vehicle state of the frame-start step (MS-DYN §3.1, §3.2, §3.4). | I-09, I-10; vehicle-model boundary ICD | L1-AER-430, -440; L2-AER-DYN-320, -330 | Open (I1) |
| IN-C1-31 | NAV (C6) | Euler angles derived by CV-260 (L2-AER-DYN-070); NAV's heading equals the yaw angle of the state. | Vehicle-model boundary ICD | L1-AER-530 | Open (C6) |
| IN-C1-32 | FC (C4), AF (C5), I1 | Under option T1 (D64) a heading change at a non-zero horizontal speed needs a lateral force of the vehicle mass times the horizontal speed times the heading rate. [P-SYS-230] is a **ground speed** (D72), and the turn acceleration depends on the ground velocity, so C5 bounds the commanded heading rate so that the horizontal speed times the heading rate stays within [P-AF-200] (D72); with a tailwind the ground speed can exceed [P-SYS-230] only if AF allows it. The acceleration enters [P-SYS-440], [P-AF-200], [P-SYS-120], [P-SYS-410] and the cross-axis tolerance [P-SYS-540]. | ICD-FC-AF; FUNCTIONAL_ANALYSIS §7.1, §7.2 | L1-AER-130, -290, -300, -350, -380 | Open (C4, C5) |
| IN-C1-33 | FC (C4), I1 | Drag for the budgets (MS-DYN §5.5): `D(V) = ½·ρ·[P-DYN-100]·V²`, at most `D(V)` along any body axis, at the sea-level density 1.225 kg/m³ (the operating volume is now bounded below by a height above the ground and Takeoff and Land reach the ground). Largest airspeed [P-SYS-230] + [P-SYS-430] + [P-SYS-560] (D72). No aerodynamic moment; no gear drag. | FUNCTIONAL_ANALYSIS §7.1 | L1-AER-120 to -140 | Open (I1) |
| IN-C1-34 | FC (C4), I1 | Gust bounds: wind rate at most `(π/2)·[P-SYS-560]/[P-SYS-570]` (MS-DYN §5.4). | FUNCTIONAL_ANALYSIS §7.2, §7.4 | L1-AER-300, -460 | Open (C4) |
| IN-C1-35 | FC (C4) | The sensed acceleration is not part of the boundary state; it goes to TM. | Vehicle-model boundary ICD | L1-AER-290, -430 | Open (I1) |
| IN-C1-36 | TM (C7) | At each step: vehicle state, **gear state**, sensed acceleration. | I-32, I-45; ICD-AER-TST | L1-AER-640; L2-AER-DYN-350 | Open (C7) |
| IN-C1-37 | TM (C7), TST | One event record per contact step: landing or crash, with the timestamp of the contact step. **A run can hold several landing events** and at most one crash; the TST ends the run on a crash. | I-37, I-41; ICD-AER-TST | L1-AER-260, -270; L2-AER-DYN-530 | Open (C7, I1) |
| IN-C1-38 | TM (C7) | Step-0 acceleration quantities are known once the first step runs (MS-DYN §3.4); in a ground start they are the rest values (zero, and [P-DYN-010] upward). | ICD-AER-TST | L1-AER-640 | Open (C7) |
| IN-C1-39 | I1 | [P-SYS-200] inside the atmosphere model. | PARAMETERS | L1-AER-070 | Closed: 45 720 m is in layer 3, and the model now reaches 84 852 m (DD-C1-07) |
| IN-C1-40 | I1 | Maximum mass and inertia from FU for [P-SYS-400] to [P-SYS-420]. | FUNCTIONAL_ANALYSIS §7.1 | L1-AER-120 to -140 | Open (I1) |
| IN-C1-42 | AF (C5) | **Gear state** at the start of each control frame: gear position (extended, retracted, in transit) and on the ground. Autoflight descends below the hover height only with the gear extended (a contact in transit or retracted is a crash), and detects the landing from "on the ground". | I-45; vehicle-model boundary ICD | L1-AER-430, -910; L2-AER-DYN-290, -320 | Open (C5, I1) |
| IN-C1-43 | FC (C4), AF (C5) | **Liftoff rule** (MS-DYN §9.6): the vehicle leaves the ground at the first step at which the upward control force exceeds the vehicle mass times [P-DYN-010]; the condition is evaluated at the contact step of a landing too. So during the Land descent and until the effectors are off, the upward control force must stay at most the weight from the frame in which a contact can occur, or the vehicle lifts off again and makes a second landing. At liftoff in wind the drag of the wind acts at once (the [P-SYS-580] limit). | ICD-FC-AF; FUNCTIONAL_ANALYSIS §7.2 | L1-AER-920, -930, -960, -970 | Open (C4, C5) |
| IN-C1-44 | AF (C5) | **Gear clearance at the hover height** with the gear extended is [P-AF-210] − [P-DYN-040] (0.124 m): a touch at that height within the envelope is a landing (MS-DYN §2.5, §9.4). | P-AF-110 | L1-AER-960, -970 | Open (C5) |
| IN-C1-45 | NAV (C6) | The height above the ground (CV-400) uses the body geometry of MS-DYN §2.6 (`h − R − a·|sin θ|`); DYN uses the same expression for the contact. | ICD-NAV-AF; MS-DYN §2.6 | L1-AER-530, -890 | Open (C6) |
| IN-C1-46 | FU (C2) | Answers to C2: IN-C2-19 done (L2-AER-DYN-210 keeps the CG out of I-04 and uses "inertia tensor"; MS-DYN §6 third bullet says the CG does not cross I-04 — the §6.0 text of `ms_dyn_s6_s7_fu.md` replaces it at the I1 merge); IN-C2-50 done (L2-AER-DYN-370, -510, -520, MS-DYN §9.4 name the FU fuel availability); IN-C2-51 done (C-8 per-step wording, "zero fuel or effectors off" in the common conditions, no hover-endurance check); IN-C2-53 done (MS-DYN §2.5: the gear has no mass or inertia). | — | G2-F05, G2-F22, D68, L1-AER-900 | Closed (C1 side) |
| IN-C1-47 | TST, I1 | Credibility checks C-1 to C-5 start airborne with the gear retracted (D73, B3-1); each such procedure says why. | ICD-AER-TST; test procedures | L2-AER-DYN-600 to -640 | Open (V1) |

## 3. ICDs touched

| ICD | DYN items |
| --- | --- |
| Vehicle-model boundary ICD (IN-B1-01; home decided at I1, TT-720) | IN-C1-30, -31, -35, -41, -42 |
| ICD-AER-TST | IN-C1-20 to -23, -25, -26, -36 to -38, -47 |
| ICD-FC-AF | IN-C1-32, -43 |
| ICD-NAV-AF | IN-C1-45 |
| MS-DYN internal (I-01 to I-04, I-08, I-44, I-46; not an ICD) | IN-C1-01 to -05, -10 to -12, -27 |
