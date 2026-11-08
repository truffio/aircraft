# C6 — Interface needs (NAV)

What the navigation subsystem (NAV, `work/C6/L2_NAV.md`) needs from, and gives to, DYN, AF, FC, FCP, TM and the TST, the proposed content of ICD-NAV-AF, and the answers to the needs that C1 addressed to C6. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2. C4, C5, C7 and C8 draft in parallel; C6 did not coordinate with them, and the integration step (I1) resolves these needs. Written at branch c1_c2, commit 55c6c29 (D1–D74).

## 1. Summary of the NAV interfaces

| Interface | Direction | Data (SI) | Rate | Defined in | NAV record |
| --- | --- | --- | --- | --- | --- |
| I-10 | DYN → NAV | Vehicle state of the frame-start step (position, velocity in L, attitude quaternion with the derived Euler angles, body rates, vehicle acceleration) | Start of each control frame | Vehicle-model boundary ICD (IN-B1-01, TT-720) | -200, -210 |
| I-21 | TST → NAV | Run's vehicle parameter set: P-DYN-020, P-DYN-030, P-NAV-010, P-NAV-030 | Start of run | ICD-AER-TST | -330 |
| I-17 | NAV → AF | Altitude, height above the ground, horizontal position (north, east), horizontal speed, vertical speed, heading, track, each with its validity | Each control frame, before AF executes | ICD-NAV-AF (§2) | -220, -230, -260, -270, -310, -400 |
| I-18 | NAV → FCP | Altitude, height above the ground, horizontal speed, vertical speed, heading, track, each with its validity | Each control frame | ICD-FCP | -240, -260, -270 |
| I-35 | NAV → TM | The six navigation quantities with their validity and the frame-start timestamp | Each control frame; sampled at each output sample | ICD-AER-TST (operational data) | -250, -260 |

NAV gives nothing to the vehicle model and nothing to FC (L2-AER-NAV-210; FUNCTIONAL_ANALYSIS §3.3).

## 2. Proposed content of ICD-NAV-AF (for I1, TT-680)

One item per quantity, each with a validity flag (true = valid). Computed from the frame-start state of the frame; timestamp = step index of the frame-start step (CV-840).

| Item | Symbol | Unit | Frame / reference | Range | Definition | Validity rule | Value while invalid | NAV record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Altitude | h | m | Datum plane, positive up, at the CG | ≥ 0 in a run (CV-420) | CV-430: h = −z_D | Valid at each frame | — | -010, -150 |
| Height above the ground | h_G | m | Datum plane, positive up, at the lowest point of the body shape (gear excluded) | ≥ 0 in a run | CV-400: h − P-DYN-030/2 − ((P-DYN-020 − P-DYN-030)/2)·\|sin θ\| | Valid at each frame | — | -020, -150 |
| Horizontal position, north | x_N | m | L, north | Real | CV-410 | Valid at each frame | — | -030, -150 |
| Horizontal position, east | y_E | m | L, east | Real | CV-410 | Valid at each frame | — | -030, -150 |
| Horizontal speed | V_H | m/s | Ground-referenced (L) | ≥ 0 | CV-480: √(v_N² + v_E²) | Valid at each frame | — | -040, -150 |
| Vertical speed | VS | m/s | Positive up | Real | CV-490: −v_D | Valid at each frame | — | -050, -150 |
| Heading | ψ | rad | From true north, clockwise (CV-510, CV-520) | [0, 2π) | CV-530 by CV-260 from the quaternion | Valid while \|θ\| ≤ P-NAV-030 | The CV-260 yaw angle (defined at every attitude) | -060, -120, -130 |
| Track | χ | rad | From true north, clockwise, ground-referenced | [0, 2π) | CV-540: wrap360(atan2(v_E, v_N)) | Valid while V_H ≥ P-NAV-010 | 0 | -070, -100, -110, -140 |

The ICD-FCP items from NAV are the same rows without the horizontal position (L2-AER-NAV-240), with the same values and validity (-260).

## 3. Needs addressed to other agents

| ID | To | Need | ICD / interface | Records | Status |
| --- | --- | --- | --- | --- | --- |
| IN-C6-10 | AF (C5) | Autoflight reads each navigation quantity from ICD-NAV-AF with its validity, and uses the track only while it is valid (its value is zero while invalid, DD-430). In Heading at a horizontal speed below [P-NAV-010] (proposed 1 kt), the track is invalid; the track tolerance [P-AF-140] applies only at non-zero speed (its description already says so). | ICD-NAV-AF | L2-AER-NAV-100, -110, -140 | Open (C5) |
| IN-C6-11 | AF (C5) | The horizontal position (north, east) is offered across ICD-NAV-AF for Stationary, Hover, Takeoff and Land (reference position, [P-AF-160]); autoflight receives no vehicle state (L1-AER-440). Confirm that AF needs it (it does unless the ICD-FC-AF horizontal references are "hold the current position" commands that FC resolves; C4/C5, IN-B1-03). CR-C6-01. | ICD-NAV-AF | L2-AER-NAV-030, -230 | Open (C5, I1) |
| IN-C6-12 | AF (C5) | NAV gives no horizontal velocity components, no heading rate, no vehicle acceleration and no gear clearance. If AF needs the direction of a residual horizontal motion below [P-NAV-010] (to stop it in Stationary or Go to hover) or the heading rate (to bound V_H times the heading rate by [P-AF-200], D72 Q1), state it at I1: NAV can add the north and east components of the horizontal velocity, always valid, with the CR-C6-01 extension (C6-Q07). The gear clearance at the hover height is [P-AF-210] − [P-DYN-040] at level attitude, an AF computation (C6-Q08). | ICD-NAV-AF | — | Open (C5, I1) |
| IN-C6-13 | AF (C5) | The heading is valid in each mode (pitch within [P-AF-180] of zero, D57). After fuel exhaustion or in an airborne test start at a large pitch angle it can be invalid; what the modes do then is C5's (with TT-580, annunciations after fuel exhaustion). | ICD-NAV-AF | L2-AER-NAV-120, -130 | Open (C5) |
| IN-C6-14 | AF (C5) | The navigation quantities of frame k are ready before AF executes in frame k and carry the frame-start timestamp (DD-010 order). | Frame order | L2-AER-NAV-310 | Open (C5) |
| IN-C6-20 | FC (C4) | None. FC reads the vehicle state directly (L1-AER-440) and receives nothing from NAV (FUNCTIONAL_ANALYSIS §5.3). If C4 chooses to read navigation quantities, it uses the ICD-NAV-AF definitions rather than a second derivation. | — | — | Note |
| IN-C6-30 | FCP (C8) | NAV gives the panel the six navigation quantities with their validity, in SI, at each control frame (ICD-FCP). The panel converts and rounds them (CV-750, CV-780) and decides how an invalid track or heading is presented (recommended: not shown as a number), and whether the height above the ground is indicated (CONOPS §4.3 lists altitude, vertical speed, horizontal speed, heading and track). On the ground the altitude indication is the CG rest altitude [P-DYN-030]/2 + [P-DYN-040] (about 11 ft), not zero (B3 impact list, C8). | ICD-FCP | L2-AER-NAV-240, -260, -270 | Open (C8) |
| IN-C6-40 | TM (C7) | NAV gives the operational data output the six navigation quantities, their validity and the frame-start timestamp at each control frame. TM records them at each output sample from the latest frame starting at or before the sample (L1-AER-640). Recording the validity too is proposed (CR-C6-02). The horizontal position is in the recorded vehicle state. Releasable or protected classification: #69, deferred (D44). | ICD-AER-TST | L2-AER-NAV-250 | Open (C7) |
| IN-C6-50 | TST, TM (C7), I1 | **Records at the frame-start steps for the NAV analyses.** AN-NAV-010 to -070 and TP-NAV-100 to -330 compare the NAV outputs of each control frame with the recorded vehicle state of its frame-start step. Either the output samples fall on the frame-start steps (proposed: [P-TM-010] = [P-SYS-310], FUNCTIONAL_ANALYSIS §7.5, with aligned phase) or the TST records the NAV outputs and the frame-start state at each frame for those runs (as IN-C1-26, IN-C2-30, IN-C3-31 do per step). | ICD-AER-TST | L2-AER-NAV-010 to -330 | Open (I1) |
| IN-C6-51 | TST | **Test runs NAV needs:** the tumbling test run (airborne test start well above the ground, zero fuel, level attitude, a pitch rate; B3-1 allows airborne test starts), a run of SC-060 with a steady crosswind, a run accelerating from Stationary through [P-NAV-010] in Heading and back, and runs with modified vehicle parameter sets (P-DYN-030, P-DYN-040, P-NAV-010). The ability to evaluate NAV off-line on a recorded frame-start state (TP-NAV-320 b) and to observe the values AF, FCP and TM receive in one frame (TP-NAV-260, -310). | ICD-AER-TST; test harness | L2-AER-NAV-020, -040, -070, -100 to -130, -260, -310, -320, -330 | Open (TST, V3) |
| IN-C6-60 | I1 | Merge the P-NAV values and the three agreement tolerances (`param_proposals.md`); TT-200 TBD → TBR; open a TT row for P-NAV-060 to -080. | PARAMETERS, TBD_TBR | — | Open (I1) |
| IN-C6-61 | I1 | Write ICD-NAV-AF from §2 and the NAV rows of ICD-FCP and ICD-AER-TST (TT-680). | ICD-NAV-AF, ICD-FCP, ICD-AER-TST | L2-AER-NAV-220 to -270, -400 | Open (I1) |
| IN-C6-62 | I1 | Decide where P-NAV-010 and P-NAV-030 sit in the run configuration (C6-Q06; recommended: the vehicle parameter set). | ICD-AER-TST; glossary | L2-AER-NAV-330 | Open (I1) |

## 4. Answers to the needs addressed to C6

| Need | Answer | NAV record |
| --- | --- | --- |
| IN-C1-30 (vehicle state of the frame-start step to NAV and FC) | Accepted: NAV takes the frame-start state at the vehicle-model boundary and uses it unmodified. | -200, -320 |
| IN-C1-31 (Euler angles by CV-260; NAV's heading equals the yaw angle of the state) | Yes: NAV's heading is the CV-260 yaw angle of the frame-start quaternion, the derivation of L2-AER-DYN-070, so it equals the recorded heading. NAV also uses the CV-260 pitch angle for the height above the ground and the heading validity. | -020, -060, -120, -130 |
| IN-C1-45 (height above the ground by the body geometry of MS-DYN §2.6, the expression DYN uses for the contact) | Yes: NAV uses h − R − a·\|sin θ\| (CV-400) with P-DYN-020 and P-DYN-030 taken from the run's vehicle parameter set, the same values DYN uses. On the ground it equals P-DYN-040. | -020, -330 |
| B1 C6 row and IN-B1-04 (altitude, horizontal speed, vertical speed, heading and track at each control frame with CV-580 validity, to AF and FCP) | Covered, with the height above the ground (B3, L1-AER-530 v2, -890 v2) and the horizontal position (CR-C6-01). | -010 to -150, -220, -240 |
| B3 impact list §C6 (height above the ground with validity to AF and TM; track validity on the ground) | Covered: the height above the ground is always valid; the track is invalid on the ground (zero horizontal speed). | -020, -110, -150, -220, -250 |
