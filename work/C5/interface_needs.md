# C5 — Interface needs (AF)

What the autoflight subsystem (AF, `work/C5/L2_AF.md`, with `work/C5/AF_MODE_LOGIC.md`) needs from, and gives to, FCP, NAV, FC, DYN, FU, TM and the TST, the proposed AF side of ICD-FC-AF, and the answers to the needs that C1, C2, C3, C6, C7, C8 and B3 addressed to C5. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2 as changed by CR-B3-39 (D73). "Boundary ICD" is the vehicle-model boundary ICD, whose home I1 decides (IN-B1-01, TT-720). C4 drafts in parallel and C5 did not coordinate with it or with C6 to C8; I1 resolves these. Written at branch c1_c2, commit 0b19af0 (D1 to D75).

## 1. Summary of the AF interfaces

| Interface | Direction | Data | Rate | Defined in | AF record |
| --- | --- | --- | --- | --- | --- |
| I-19 | FCP → AF | The ordered mode selections of the frame; the SI target of each of the four selectors; the selectors accepted in the frame | Each control frame | ICD-FCP | -050, -120, -310, -320 |
| I-16 | AF → FCP | Annunciation content: mode state, each target in use with its quantity (SI), gear position | Each control frame | ICD-FCP | -050, -800, -810 |
| I-17 | NAV → AF | Altitude, height above the ground, horizontal position (north, east), horizontal velocity (north, east), horizontal speed, vertical speed, heading, each with its validity. Not used: the track | Each control frame, before AF executes | ICD-NAV-AF | -040, -070, -920 |
| I-13 | AF → FC | Six axis references, each a value, its rate and a regulation indication; the off value | Each control frame | ICD-FC-AF (§2 below) | -030, -090, -410 |
| I-43 | AF → DYN | Landing gear command (extend, retract) | Each control frame | Boundary ICD | -060, -700 to -740 |
| I-45 | DYN → AF | Gear state: gear position, on the ground | Frame-start step | Boundary ICD | -060, -270, -710 |
| I-06 | FU → AF | Fuel state: the fuel exhaustion indication (the remaining mass and the low-fuel indication are not used) | Frame-start step | Boundary ICD | -060, -860 |
| I-23 | TST → AF | Initial mode state | Run start | ICD-AER-TST | -900, -910 |
| I-34 | AF → TM | Mode state (with the decision on each mode selection), the target of each armed and active mode (SI), the SI target taken from each selector, the landing gear command | Each control frame | ICD-AER-TST (operational data) | -820 to -840 |

AF gives the vehicle model only the landing gear command and reads no vehicle state (L1-AER-440). I-14 (active and armed modes to guidance) is internal to AF.

## 2. Proposed AF side of ICD-FC-AF (for I1 with C4, DD-C5-01, C5-Q12)

Six axis references, one per degree of freedom, in the local frame L (north-east-down); the rotation to the body axes is flight control's, which reads the vehicle state anyway. Each reference is a **value**, its **rate** (the time derivative the guidance intends) and a **regulated** indication (true: flight control regulates the value; false: it regulates only the rate). One **off** indication replaces all six. No mode information, no target and no selection crosses (G1-F04).

| Degree of freedom | Value (unit) | Rate (unit) | Regulated |
| --- | --- | --- | --- |
| North | Reference position x_N (m) | Velocity reference v_N (m/s) | True in a hold; false while Heading moves at a non-zero speed |
| East | Reference position y_E (m) | Velocity reference v_E (m/s) | As north |
| Vertical | Altitude reference, CG altitude (m) | Vertical speed reference, positive up (m/s) | True in Altitude hold, Hover and the holds inside Go to hover and Takeoff; false while climbing or descending at a rate (Go to altitude, Vertical speed, the climb of Takeoff, the descent of Land) |
| Heading | Heading reference (rad, [0, 2π)) | Heading rate reference (rad/s) | True |
| Pitch | Zero (rad) | Zero (rad/s) | True |
| Roll | Zero (rad) | Zero (rad/s) | True |

The magnitude of the acceleration of (v_N, v_E, vertical speed reference) is at most [P-AF-200] (L2-AER-AF-420); the vertical speed reference changes at most at [P-AF-230] (-430); the heading rate reference is bounded by [P-SYS-270] and by [P-AF-200] over the horizontal speed reference (-440). If C4 prefers body-axis references (L1-AER-370, -380 speak of "each body axis"), AF converts the horizontal pair with the heading reference, a rotation about the vertical axis only (pitch and roll are zero, D57); the change is confined to this interface.

## 3. Answers to the needs addressed to C5

| Need | Answer | AF record |
| --- | --- | --- |
| **IN-C8-01** (mode selections, outcome in each state) | Accepted: AF decides each of the eight in each state; the outcome of every pair is the decision table DT-01 to DT-25 of AF_MODE_LOGIC §6, including Land when Hover is not active (refused), Takeoff in the air or with no fuel (refused), and each selection on the ground (refused but Takeoff). | -120, -130, -140 to -210 |
| **IN-C8-02** (selector targets) | Accepted as C8 states them: heading in [0, 2π), horizontal speed ≥ 0 (ground speed), altitude (CG), vertical speed signed; AF uses them as the table of AF_MODE_LOGIC §9 says and treats an unaccepted selector as unchanged. | -050, -310 |
| **IN-C8-03** (standard versus selected vertical speed) | AF decides: Go to altitude starts at [P-AF-220]; a selected vertical speed accepted in the frame of the GO ALT selection or later replaces it, as a magnitude toward the selected altitude; zero is ignored; a re-selection of GO ALT restarts at the standard speed (C5-Q08). Vertical speed with a zero selected rate, or with the selected altitude behind, ends at once in Altitude hold (C5-Q06). | -320, -360 |
| **IN-C8-04** (same-frame order) | Accepted: AF decides the selections in the order given, each against the state the previous one left, with the selector targets of the end of the frame's intake. | -120 |
| **IN-C8-05** (annunciation content, labels) | AF gives: ENG, the active horizontal, vertical and both-axes modes, the armed mode (identifiers of AF_MODE_LOGIC §3), the targets in use with their quantity (§9 table), the gear position. Labels: STAT, HDG, ALT, GO ALT, V/S, GO HOVER, HOVER, TAKEOFF, LAND for the active modes; ALT and HOVER for the armed mode; none for a field with the value none (AF_MODE_LOGIC §2). The empty mode state is valid content. | -100, -800 |
| **IN-C8-06** (no data path into the selectors) | Accepted: AF writes no selector. The held altitude, the hover altitude and the standard vertical speed in use go in the annunciation content as targets; the reference position is not annunciated (it is not one of the four quantities). No new AF → FCP item, so no change to L1-AER-880. | -050, -800 |
| **IN-C8-07** (labels owned by FCP) | Confirmed: the gear labels GEAR DOWN, GEAR UP, GEAR TRANSIT and the fuel alert labels are FCP's; C5 owns the mode labels. | -800 |
| **IN-C8-08** (initial condition) | Accepted: the initial selected values are FCP's, the initial mode state is AF's (valid states IC-1 to IC-7). At the first frame AF takes the SI targets of the initial selector values and the first navigation quantities; Altitude hold and Stationary take their targets from the true state (level-off altitude, stopping position). | -900, -910, -920 |
| **IN-C8-09** (no Hover and no disengage selection) | Hover is left by a selection of a group mode, the other group taking its hold mode (DT-12 to DT-16, C5-Q01). There is no crew disengage; autoflight ceases to be engaged only at the end of Land and at fuel exhaustion (C5-Q04). | -190, -270, -860 |
| **IN-C6-10** (track and the horizontal speed below [P-NAV-010]) | AF does not use the track. The track tolerance [P-AF-140] is a test measure on NAV's track and applies only at a speed of at least [P-NAV-010] (`param_proposals.md`). | -040 |
| **IN-C6-11** (horizontal position) | Needed: AF needs the horizontal position (and the velocity components, IN-C5-10) to acquire the stopping position and to initialise the references. CR-C5-01 extends CR-C6-01. | -040, -330, -920 |
| **IN-C6-12** (velocity components, heading rate, gear clearance) | Velocity components: needed, always valid (IN-C5-10). Heading rate: not needed (the heading rate bound acts on the reference, not on the measured rate). Gear clearance: AF computes it where it needs it ([P-AF-210] minus [P-DYN-040]); it is not an input. | -330, -440 |
| **IN-C6-13** (heading validity) | The mode logic does not depend on the heading validity. The heading reference is initialised from NAV's heading (the CV-260 yaw angle) valid or not; the heading reference then moves only in Heading by its own rate. | -450, -920 |
| **IN-C6-14** (navigation quantities of frame k before AF executes) | Accepted: AF executes after NAV in the frame (DD-010) and reads the quantities of that frame. | -070 |
| **IN-C7-30** (mode state, targets, gear command to TM) | Accepted, with the decision on each mode selection added to the mode state record (IN-C5-40) and the selector targets AF takes (-830). | -820, -830, -840 |
| **IN-C7-31** (fixed set of mode state values) | Accepted: AF_MODE_LOGIC §3 fixes the five fields and their values for every implementation. | -100 |
| **IN-C7-32** (first frame at step zero) | Accepted: AF executes at the first control frame, at step zero, and gives the initial mode state in that frame (a ground start gives the empty mode state and the off value). | -900 |
| **IN-C1-32** (heading rate bound, D72 Q1) | Done: the heading rate reference is at most [P-SYS-270] and at most [P-AF-200] over the horizontal speed reference; the resultant horizontal acceleration is at most the horizontal limit (DD-C5-07). With a tailwind the actual ground speed can exceed the reference; that excess is FC's transient allowance. | -420, -440 |
| **IN-C1-41** (landing gear command) | Accepted: one command per control frame, extend or retract, held between changes; the first command equals the initial gear position; AF commands retraction only airborne at the hover height, and extension throughout the on-ground state. | -700 to -740 |
| **IN-C1-42** (gear state) | Accepted: AF reads the gear position and the on-ground state at the frame-start step; it descends below the hover height only with the gear extended and ends Land at "on the ground". | -270, -710 |
| **IN-C1-43** (liftoff rule) | Land keeps the downward vertical speed reference until the off value is given, so that FC's upward force stays at most the weight at the contact (a request to C4: the reference is a rate, "not regulated" altitude). | -670 |
| **IN-C1-44** (gear clearance at the hover height) | [P-AF-110] plus the tilt term of [P-AF-180] stays inside [P-AF-210] minus [P-DYN-040]: 0.05 m + 0.035 m < 0.124 m (`param_proposals.md`). | -580 |
| **C2 note** (fuel state to AF, annunciations after exhaustion, Takeoff with no fuel) | Fuel state: needed (IN-C5-30). After exhaustion: disengage, empty mode state, every selection refused; Takeoff with no fuel refused (C5-Q03, C5-Q04). | -150, -860, -870 |
| **IN-C3-26, IN-C3-30** (effectors on and off) | AF decides by the off value of the axis references: the effectors are on exactly while autoflight is engaged, from the frame of the Takeoff selection to the frame of the contact of Land (or exhaustion). FC derives the effector activation state from it (a request to C4: the activation state is on exactly while the references are not off). | -410, -760 |
| **IN-B1-03** (ICD-FC-AF: which quantity each reference is) | Proposed: §2 above. | -090 |
| **B3 impact list, C5** | Covered: Takeoff and Land (-150, -160, -660, -670), gear command (-700 to -740), the mode state on the ground (-140, -750), airborne initial states (-900, -910), Go to hover from below and during Land (-170, -210, -630), heading held in Takeoff and Land (-450), annunciations (-800), fuel exhaustion (-860), the tolerances in Hover with the gear extended (-580), the lowest selectable altitude (FCP's; AF uses the selector target as given). | — |

## 4. Needs addressed to others

| ID | To | Need | Why | AF records |
| --- | --- | --- | --- | --- |
| **IN-C5-10** | NAV (C6), I1 | The horizontal velocity components (north, east) among the navigation quantities, always valid, beside the horizontal position (CR-C6-01 extended; **CR-C5-01** on L1-AER-530 and -890). AF uses the horizontal speed, the vertical speed, the altitude, the height above the ground and the heading as NAV defines them. | The stopping position and the initial references need the velocity vector at any speed; the track is invalid below [P-NAV-010], and a speed with no direction would leave the stopping position wrong by up to the distance travelled at that speed (C5-Q13). | -040, -330, -920 |
| **IN-C5-20** | FC (C4), I1 | (a) The axis references of §2, or C4's counter-proposal (C5-Q12). (b) The effector activation state is on exactly while the references are not off (IN-C3-26). (c) FC tracks the reference position and altitude reference only where the regulated indication is true, and the rate alone otherwise. (d) FC keeps the upward force at most the weight while the vertical speed reference is downward on the ground (IN-C1-43). (e) FC receives no mode information and needs none. | One interface for every law (L1-AER-420); the split of the budgets [P-AF-160] and [P-FC-010]; the activation state. | -030, -090, -410, -670 |
| **IN-C5-30** | FU (C2), I1 | Give the fuel state to AF as well as to FCP (L2-AER-FU-240 names FCP only; FUNCTIONAL_ANALYSIS I-06 and §3.3 have FU → AF). AF needs only the fuel exhaustion indication, at the frame-start step. | D68 behaviour; TT-580. Conflict C5-C02. | -060, -860, -870 |
| **IN-C5-40** | TM (C7), I1 | Add to the mode state signal (S-05) the decision on each mode selection of the frame, accepted or refused, with the timestamp; and the SI target AF takes from each selector (a signal beside S-04). Both are AF's children of L1-AER-610 and -620; classes with the RVS (#69). | A refused selection and a selection of the active mode both leave the mode state unchanged; the tests need to tell them apart. | -830, -840 |
| **IN-C5-50** | FCP (C8) | Confirm that FCP's accepted-selector set includes a selector accepted in the frame of the mode selection that uses it (GO ALT with its vertical speed in one frame), and that the targets AF reads are the end-of-intake targets (DD-C8-01). No change to FCP otherwise. | TG-2 of AF_MODE_LOGIC. | -320 |
| **IN-C5-60** | DYN (C1) | Gear state at the start of each control frame, including "on the ground" at the contact step of a landing. A retraction commanded on the ground takes effect at the first airborne step (IN-C1-41): AF never commands it (-730), so the rule is a safeguard. | The end of Land is detected in the frame after the contact; the effectors-off latency [P-SYS-480] counts from the contact (one frame for AF). | -270, -730 |
| **IN-C5-70** | TST, I1 | (a) ICD-AER-TST, initial condition: the initial mode state (the five fields), validated by AF against the rows IC-1 to IC-7, with an initial-condition error naming it (-910). (b) Recording of the ICD-FCP and ICD-FC-AF interfaces for test runs (as IN-C7-40, IN-C8-40). (c) Test scripts for the 25 decisions DT, run from each state class; a test flight-control-law design for the autoflight implementation variant (IN-C3-33, DM-AF-020). (d) The TST applies a wind within [P-SYS-580] at liftoff (IN-C1-25). | The decisions and the transitions are verified by scripted sequences; TP-AF-010, -120, -810. | -010, -020, -120, -810, -910 |

## 5. ICDs touched

| ICD | AF items |
| --- | --- |
| ICD-FC-AF | The six axis references and the off value (§2, IN-C5-20) |
| ICD-NAV-AF | The navigation quantities AF reads, with the horizontal position and velocity (IN-C5-10) |
| ICD-FCP | Mode selections, selector targets, accepted selectors in; annunciation content out (IN-C8-01 to -09) |
| Vehicle-model boundary ICD | Landing gear command out; gear state, fuel state in (IN-C5-30, -60) |
| ICD-AER-TST | Initial mode state, initial-condition error (IN-C5-70); operational data: mode state with decision, targets, selector targets, gear command (IN-C5-40) |
