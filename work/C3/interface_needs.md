# C3 — Interface needs (EF)

What the effector subsystem (EF, `work/C3/L2_EF.md`) needs from, and gives to, DYN, FU, FC, AF, TM and the TST, and the answers to the needs that C1 and C2 addressed to C3. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2. "MS-DYN internal" means the item stays inside the vehicle model and is defined in the MS-DYN effector model (`work/C3/ms_dyn_s7_effectors.md`), not in an ICD. "Boundary ICD" is the vehicle-model boundary ICD, whose home I1 decides (IN-B1-01, TT-720). C3 did not coordinate with the other agents directly; I1 resolves these.

## 1. Summary of the EF interfaces

| Interface | Direction | Data (SI) | Rate | Defined in | EF record |
| --- | --- | --- | --- | --- | --- |
| I-12 | FC → EF | Effector commands: one command per effector (N, along its direction of action) and the effector activation state (on/off) | Each control frame, used at each step of the frame | Boundary ICD | L2-AER-EF-150, -400 |
| I-03 | FU → EF | Fuel availability (available / not available) | Each simulation step | MS-DYN internal | L2-AER-EF-200 |
| I-02 | EF → DYN | Control force `F_c^B` (N, body frame) and control moment `M_c^B` (N·m, about the CG) | Each step, held over the step | MS-DYN internal | L2-AER-EF-130 |
| I-01 | EF → FU | Effector outputs (N) and the same `F_c^B`, `M_c^B` as I-02 | Each step, held over the step | MS-DYN internal | L2-AER-EF-140 |
| I-30 | EF → TM | Effector output of each effector (N) | Each step; sampled at each output sample | ICD-AER-TST | L2-AER-EF-410 |
| I-21 | TST → EF | Vehicle parameter set with P-EF-020, -100 to -130 | Start of run | ICD-AER-TST | L2-AER-EF-050 |

EF gives nothing to the flight software (L2-AER-EF-400).

## 2. Answers to the needs addressed to C3

| Need | Answer | EF record |
| --- | --- | --- |
| IN-C1-10 (control force and moment per step, held, zero at exhaustion) | Yes: EF computes `F_c^B`, `M_c^B` once per step from the outputs (MS-DYN §7.1.5), one value per step held over it, and zero while fuel is not available or the effectors are off. | -120, -130, -200, -210 |
| IN-C1-11 (text for the effector model) | `work/C3/ms_dyn_s7_effectors.md`, to merge as MS-DYN §7.1. | -430 |
| IN-C1-12 (effector outputs at step 0) | Zero before the first effector commands of a run (activation state off). If the first frame's commands at step 0 set the effectors on, `u_i(0) = β·ĉ_i(0)`; under the D69 ground start they are off, so the outputs and the step-0 accelerations (DD-080) see zero control force. | -100, -210 |
| IN-C2-11 (one mapping from outputs to force and moment) | Yes, and EF computes it once and gives the same value to DYN and FU (DD-C3-05). Recommended for I1: L2-AER-FU-070 reads "the effector outputs of each simulation step, with the control force and control moment computed from them" (editorial; FU-040 is unchanged). | -120, -140 |
| IN-C2-20 (zero output while not available; full output in a step that starts available) | Yes, both. Zero at once, without the lag; the lag restarts from zero. | -200 |
| IN-C2-21 (effector outputs per step to FU) | Yes, one value per effector per step (I-01). | -140 |
| IN-C2-22 (no EF consumption parameter) | Confirmed: no EF parameter enters a consumption relationship (IN-EF-010 checks it). | -010 |
| IN-C2-23 (EF child of L1-AER-360: hold at no more than the weight within [P-FU-100]) | EF's share of the margin is zero: the lag has unit steady-state gain and no overshoot, and the resultant is exactly the sum of the outputs, so the fuel used in a hold is that of the resultant flight control commands. Holding that resultant at the weight within [P-FU-100] is FC's share (IN-C3-24). | -100, -120 |
| Inspection G2 §4 note to EF | Who computes the resultant: EF, once (DD-C3-05). Step-0 outputs: above. L1-AER-360 child: above. Zero from the first step not available: -200. | — |

## 3. Needs on DYN (C1) and MS-DYN

| ID | Need | Why | EF records |
| --- | --- | --- | --- |
| IN-C3-01 | Merge `work/C3/ms_dyn_s7_effectors.md` as MS-DYN §7.1 (the **effector model**), and add P-EF-020, -030, -100 to -130 and the authority values to the MS-DYN §12 pedigree table. | L1-AER-720; TT-780. | -430 |
| IN-C3-02 | MS-DYN §5.1, §10.2 and L2-AER-DYN-180 already take the control force and moment from EF, one value per step held over the step: no change. The rationale of L2-AER-DYN-180 ("EF sums its effector outputs") matches DD-C3-05. | Consistency. | -130 |
| IN-C3-03 | MS-DYN §11 common conditions ("zero fuel means … the effectors produce no force and no moment"): add "or the effectors off" once D69 is applied; the effector model gives exactly zero in both cases. | D69 rework of the check configurations (G2 §6). | -200, -210 |

## 4. Needs on FU (C2)

| ID | Need | Why | EF records |
| --- | --- | --- | --- |
| IN-C3-10 | L2-AER-FU-070 and MS-DYN §7.2 use the control force and moment that EF gives with the outputs (I-01), not a second computation from the outputs. | One mapping (IN-C2-11, DD-C3-05). | -140 |
| IN-C3-11 | L2-AER-FU-040 rationale "fuel is consumed in each flight condition, hover included": with D69 there is no consumption with the effectors off on the ground. DD-110 already gives it (zero resultant, zero flow). Wording for the C2 D69 rework. | D69. | -210 |

## 5. Needs on FC (C4)

| ID | Need | Why | EF records |
| --- | --- | --- | --- |
| IN-C3-20 | The effector command is a force in N along the effector's direction of action, one per effector, plus the effector activation state; FC issues them once per control frame and holds them for the frame. The layout (number, directions, points of application, limits) comes from the vehicle parameter set (P-EF-100 to -130), so FC reads it from the configuration and does not hard-code it. | Boundary ICD content; layout replaceable (DD-C3-06). | -150, -400 |
| IN-C3-21 | A command beyond an output limit is clipped by EF (nominal). FC's child of L1-AER-110 must not rely on output beyond the limits, and its priority rule (FC1) acts beyond the authority box. | L1-AER-110 FC share. | -110 |
| IN-C3-22 | The effector lag (time constant P-EF-020, reaching the band P-EF-030 within P-EF-010) is in the loop: FC's stability margins and regulation shares (P-FC-010, P-FC-020) are designed with it. P-SYS-310 + P-EF-010 ≤ P-SYS-480 holds with 0.02 s of margin. | L1-AER-460, -710. | -100, -340 |
| IN-C3-23 | Inside the authority box (L2-AER-EF-330) each force and moment component can be allocated and saturated on its own; the crew limit (L1-AER-290) caps the usable resultant force below the box at low mass. | L1-AER-290, -380; FA §7.1 upper side. | -330 |
| IN-C3-24 | FC's child of L1-AER-360 shows that in a still-air hold at level attitude the commanded resultant control force is the weight, and the commanded moment zero, within [P-FU-100]; EF adds nothing to it. | IN-C2-23; L2-AER-FU-290. | -100, -120 |
| IN-C3-25 | Confirm a heading-rate onset time of at least 0.5 s at maximum inertia, which [P-SYS-420] = 2000 N·m allows (FA §7.1 "α_req … that C4 sets"); a shorter onset needs a larger [P-SYS-420]. | L1-AER-140, -350. | -320 |
| IN-C3-26 | (D69) FC sets the effector activation state: on before Takeoff powers up, off at Land touchdown. Which function decides (FC on an AF mode signal, or AF through FC) is C4/C5 with B3. While off, FC's commands have no effect. | DD-C3-04. | -210 |

## 6. Needs on AF (C5)

| ID | Need | Why | EF records |
| --- | --- | --- | --- |
| IN-C3-30 | (D69) Takeoff and Land state when the effectors switch on and off (via FC, IN-C3-26); after fuel exhaustion the outputs are zero whatever the activation state (D68). | DD-C3-04; D68, D69. | -200, -210 |

## 7. Needs on TM (C7), the TST and I1

| ID | Need | Why | EF records |
| --- | --- | --- | --- |
| IN-C3-31 | **TST recording for analysis runs:** the effector commands, the effector activation state, the effector outputs and the control force and moment at each simulation step (as IN-C2-30 for FU), without changing the Aeronef configuration. | AN-EF-100, -120 and TP-EF-150 need per-step data; the operational data hold the outputs only at output samples. | -100, -120, -150 |
| IN-C3-32 | **ICD-AER-TST:** operational data signal "effector output", one per effector, in N, at each output sample (I-30). TM records it. The effector commands are FC's signal (L1-AER-630). | L1-AER-630. | -410 |
| IN-C3-33 | **Test command source:** a way to drive EF with scripted effector commands and activation state in place of flight control (open loop), for TP-EF-110, -210, -340 and DM-EF-050. Recommended: a test flight-control-law design selected through the configuration (L1-AER-400), so the vehicle model is unchanged. TST requirement for when the plan covers the TST (D44). | Open-loop effector tests. | -110, -210, -340, -050 |
| IN-C3-34 | **Boundary ICD:** the effector-commands item: an array of n forces in N (n from the parameter set) and the activation state (on/off). | L1-AER-430. | -400 |
| IN-C3-35 | **I1 budget closure:** FA §7.1 P-SYS-400 line to use the vertical drag of a climb at [P-SYS-240] at the largest horizontal airspeed (CR-C3-01); values P-SYS-400 = 60 kN, -410 = 190 kN, -420 = 2000 N·m (TBR); re-derive P-SYS-420 when P-FU-070, -080 are set. | TT-020. | -300 to -330 |

## 8. ICDs touched

| ICD | EF items |
| --- | --- |
| Vehicle-model boundary ICD (IN-B1-01, TT-720) | Effector commands and activation state (IN-C3-20, -34) |
| ICD-AER-TST | Effector output signal (IN-C3-32); EF parameters in the vehicle parameter set (I-21); per-step recording (IN-C3-31); test command source (IN-C3-33) |
| MS-DYN internal (I-01, I-02, I-03) | §7.1 (IN-C3-01, -10) |
