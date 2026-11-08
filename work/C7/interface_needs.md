# C7 — Interface needs (TM)

What the operational data output (TM, `work/C7/L2_TM.md`) needs from the subsystems whose signals it records, and from the TST and I1 for ICD-AER-TST. It also gives the answers to the needs that C1, C2 and C3 addressed to C7. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2 as changed by CR-B3-39 (D73). "Boundary ICD" is the vehicle-model boundary ICD, whose home I1 decides (IN-B1-01, TT-720). C7 did not coordinate with C4, C5, C6 or C8, which draft in parallel; I1 resolves these needs.

TM is an observer: every item below flows **into** TM, and TM gives the TST only its operational data (L2-AER-TM-010, -810).

## 1. Signal catalogue (content for ICD-AER-TST)

"Per step" means the value its source gives for the sample's step. "Per frame" means the value of the control frame that contains the sample's step, which is the frame starting at that step (DD-C7-01, DD-C7-02). The proposed class is from C7-Q01. It is not settled, and I1 enters it in a "proposed class" column only.

| ID | Signal | Unit or values | Source, record | Timing | TM record | Proposed class |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 | Timestamp: step index, simulation time | integer; s | TM (CV-840) | Each record | -100, -110, -120 | Releasable |
| S-02 | Configuration: identifier and version of the vehicle parameter set, the flight-control-law design and the autoflight implementation | strings | Run set-up (F-AER-14, I-39) | Once per run, before the first sample | -700 | Releasable if opaque |
| S-03 | Crew selection as received: mode engage command, or selector with its selected value | command set of D71; ft, ft/min, kt, deg (CV-740) | FCP (I-36) | Each selection, at its own timestamp | -200 | Releasable |
| S-04 | SI target passed to autoflight from the selection, or none | m, m/s, rad; or "none" | FCP (I-19, I-36) | With S-03 | -210 | Releasable |
| S-05 | Mode state: armed and active mode of each mode group, autoflight engaged | mode sets of AF_MODE_LOGIC (C5) | AF (I-34) | Per frame | -300 | Protected |
| S-06 | Annunciations presented | crew interface items (C5, C8) | FCP (I-38) | Each output sample | -310 | Releasable |
| S-07 | Target of each armed and active mode (CR-C7-01) | m, m/s, rad (SI) | AF (I-34) | Per frame | -320 | Protected |
| S-08 | Indications presented (CR-C7-01) | crew interface items, crew units | FCP (I-38) | Each output sample | -330 | Releasable |
| S-09 | Axis references (six) | as ICD-FC-AF defines them, with the off value | FC, as received from AF (I-13, I-33) | Per frame | -400 | Protected |
| S-10 | Axis demands: three forces, three moments, body frame | N, N·m | FC (I-11, I-33) | Per frame | -410 | Protected |
| S-11 | Effector commands: one per effector, and the effector activation state | N; on/off | FC (I-12, I-33) | Per frame | -420 | Protected |
| S-12 | Effector output of each effector | N | EF, L2-AER-EF-410 (I-30) | Per step | -430 | Releasable |
| S-13 | Fuel mass flow | kg/s | FU, L2-AER-FU-250 (I-31) | Per step | -440 | Releasable |
| S-14 | Landing gear command (CR-C7-02) | extend/retract | AF (I-34, I-43) | Per frame | -450 | Protected |
| S-15 | Vehicle state: position, velocity, attitude quaternion, heading, pitch and roll angles, body rates, vehicle acceleration | m, m/s, 1, rad, rad/s, m/s² | DYN, L2-AER-DYN-350 (I-32) | Per step | -500 | Releasable |
| S-16 | Navigation quantities: altitude, height above the ground, horizontal speed, vertical speed, heading, track, each with its validity | m, m/s, rad; valid/not valid | NAV (I-35) | Per frame | -510 | Values releasable, validity protected |
| S-17 | Sensed acceleration at the centre of gravity, body frame | m/s² | DYN, L2-AER-DYN-350 (I-32) | Per step | -520 | Releasable |
| S-18 | Vehicle mass; remaining fuel mass | kg | FU, L2-AER-FU-260 (I-31) | Per step | -530 | Mass protected unless the manual states the empty mass; fuel releasable |
| S-19 | Gear state: gear position, on the ground | extended/retracted/in transit; true/false | DYN, L2-AER-DYN-290, -350 (I-45) | Per step | -540 | Releasable |
| S-20 | Event: classification | landing/crash | DYN, L2-AER-DYN-530 (I-37) | Each contact, at the contact step | -600, -120 | Releasable |
| S-21 | Event: classification speeds (vertical, horizontal), reported vehicle state and gear state of the contact step | m/s; as S-15, S-19 | DYN (IN-C7-01) | With S-20 | -610 | Releasable |

## 2. Answers to the needs addressed to C7

| Need | Answer | TM record |
| --- | --- | --- |
| IN-C1-36 (vehicle state, gear state, sensed acceleration at each step) | Yes. TM records the values of each sample's step; it does not need every step. | -500, -520, -540, -130 |
| IN-C1-37 (one event record per contact step; several landings, at most one crash) | Yes. One event record per DYN event, at the contact step's timestamp, none of TM's own, any number per run. With C7-Q07 the record also carries the contact values (IN-C7-01). | -600, -120, -610 |
| IN-C1-38 (step-0 accelerations known once the first step runs) | Yes. A sample of step k is output when the TST commands the step from k, so sample 0 waits for the first step. In a ground start its accelerations are the rest values. | -130, -140 |
| IN-C2-33 (fuel mass flow, vehicle mass, remaining fuel mass; fuel alerts as events if TM chooses) | Signals: yes. Fuel alerts: not event records; they are annunciations recorded at each output sample (C7-Q06, CR-C7-03). | -440, -530, -310 |
| IN-C2-30, IN-C3-31, IN-C1-26 (TST per-step recording of the vehicle-model interfaces) | Not TM's. These are not operational data, which stay at [P-TM-010]. TM's tests use the same recording as their reference (IN-C7-40). | — |
| IN-C3-32 (operational data signal "effector output", one per effector, in N; effector commands are FC's) | Yes. The effector commands are FC's (IN-C7-20). | -430, -420 |
| C2 §interface table, TM row (classification with the RVS) | Proposed in C7-Q01, not settled (TT-600). | -020 |
| B3 impact list, C7 (gear state; several landings; height above the ground; effectors off via commands and outputs) | All covered; no new signal for the effectors off. | -540, -600, -510, -420, -430 |

## 3. Needs on DYN (C1)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-01 | With each ground-contact event (L2-AER-DYN-530, MS-DYN §9.8), also give the vertical speed magnitude and the horizontal speed of the propagated state of the contact step, the values the classification used (MS-DYN §9.4). This is an addition to the event content. | A landing reports the rest state, with zero velocity, at the contact step (L2-AER-DYN-560), so neither the reported state nor a sample shows the speeds that decided the classification (C7-Q07, DD-C7-03). | -610 |
| IN-C7-02 | Confirm: L2-AER-DYN-350 gives the vehicle state (with the Euler angles of -070 and the vehicle acceleration of -310), the gear state and the sensed acceleration at each step, and the event of -530 carries the timestamp of the contact step. No change. | Sources of S-15, S-17, S-19, S-20. | -500, -520, -540, -600, -120 |
| IN-C7-03 | Add the **landing gear command** to the per-step recording of IN-C1-26. | TP-DYN-270 and TP-TM-450 need the step at which the command changes; IN-C1-26 lists the control force and moment, mass, wind, ground reaction and gear state only (C7-Q05). | -450 |

## 4. Needs on FU (C2) and EF (C3)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-05 | Confirm: L2-AER-FU-250 and -260 give the fuel mass flow, the vehicle mass and the remaining fuel mass of each step, and L2-AER-EF-410 gives the effector output of each effector of each step. No change. | Sources of S-12, S-13, S-18. | -430, -440, -530 |

## 5. Needs on FCP (C8)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-10 | For each crew selection received, give TM: the selection as received (mode engage command, or selector with its selected value and its crew unit), its crew-interface timestamp, and the SI target passed to autoflight across ICD-FCP, or the indication that none was passed (a mode engage command, or a selection outside the selectable range or not accepted). This is the FCP child of L1-AER-610. | L1-AER-610 is allocated to TM, AF and FCP; TM records what the panel received and passed (DD-C7-05). | -110, -200, -210 |
| IN-C7-11 | At each output sample, give TM the annunciations and (with CR-C7-01) the indications that the panel presents, as the same crew interface data items it outputs to the TST (I-42). This is the FCP child of L1-AER-620. | The recorded presentation must equal what the crew received. | -310, -330 |
| IN-C7-12 | The annunciation labels of the fuel alerts (LOW FUEL, FUEL EXHAUSTED) are annunciations, not event records (C7-Q06). | Consistency with CR-C7-03. | -310 |

## 6. Needs on AF (C5)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-30 | At each control frame, give TM: the mode state (armed and active mode of each mode group, autoflight engaged); with CR-C7-01, the target of each armed and active mode in SI; with CR-C7-02, the landing gear command. These are the AF children of L1-AER-620 and (with CR-C7-02) L1-AER-630. AF is also allocated to L1-AER-610: its child gives the target AF takes from each selection, the same value as IN-C7-10. | Sources of S-05, S-07, S-14. | -300, -320, -450 |
| IN-C7-31 | Define the mode state in AF_MODE_LOGIC as a data item with a fixed set of values, the same for each autoflight implementation (D15). | L2-AER-TM-030: the signals must not change with the implementation. | -030, -300 |
| IN-C7-32 | Confirm, with C4 and I1: the first control frame of a run starts at step zero (FUNCTIONAL_ANALYSIS §4.2), so each output sample step is a frame start (DD-C7-02). | L2-AER-TM-130, -150. | -130, -150 |

## 7. Needs on FC (C4)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-20 | At each control frame, give TM: the axis references received from autoflight (as ICD-FC-AF defines them, the off value included), the six axis demands (N and N·m in the body frame), and the effector commands with the effector activation state, as they cross the vehicle-model boundary. These are the FC children of L1-AER-630. | L1-AER-630 is allocated to FC (not AF) for these items; the axis demands are internal to FC (I-11). | -400, -410, -420 |
| IN-C7-21 | The same signals, with the same definitions, for each flight-control-law design; a design's other internal signals stay out of the operational data. | L2-AER-TM-030; L0-CON-200. | -030 |

## 8. Needs on NAV (C6)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-50 | At each control frame, give TM the navigation quantities (altitude, height above the ground, horizontal speed, vertical speed, heading, track), each with its validity. This is the NAV child of L1-AER-640. | Source of S-16. | -510 |

## 9. Needs on the TST and I1 (ICD-AER-TST)

| ID | Need | Why | TM records |
| --- | --- | --- | --- |
| IN-C7-40 | **TST recording of the flight software interfaces for test runs:** at each control frame, the values that each flight software function gives TM (S-04, S-05, S-07, S-09 to S-11, S-14, S-16), recorded at the interface, without changing the Aeronef configuration. This is the flight software counterpart of IN-C1-26, IN-C2-30 and IN-C3-31; it is a TST requirement for when the plan covers the TST (D44). | The TM tests compare each recorded value with its source. | -130, -210, -300, -320, -400 to -420, -510 |
| IN-C7-41 | **ICD-AER-TST, operational data:** the four record kinds (output sample, crew selection record, event record, configuration record); the catalogue of §1, each signal a separate named item with its unit or set of values, none defined through another (L2-AER-TM-020); the CV-840 timestamp on the first three kinds; the units of CV-720, and the crew units of CV-740 for S-03, S-06 and S-08 only (CV-760 group 4); configuration identifiers that carry no design content; a "proposed class" column (C7-Q01). | L1-AER-590, -630, -640, -650; TT-680. | -010, -020, -030, -100 to -120, -700 |
| IN-C7-42 | **ICD-AER-TST, end of run:** a sample of step k is output when the TST commands the step from k, so when a crash ends the run the data end with the event record and the last complete sample before it; the TST ends the run on the crash event (I-41, IN-C1-23). | L2-AER-TM-140, -610. | -140 |
| IN-C7-43 | **Release package (RVS branch, D44):** the release is assembled outside the Aeronef as a subset of the signals (C7-Q02, option A). It is accompanied by a releasable data dictionary in operator terms (N-380), written from ICD-AER-TST but not part of it, because the ICD is protected. | #69; L0-CON-220 deleted; SC-240. | -020 |
| IN-C7-44 | **Test flight-control-law design** of IN-C3-33, used also by DM-TM-030 and TP-TM-700 (the same signals for another design; the configuration record names it). | L2-AER-TM-030, -700. | -030, -700 |
| IN-C7-45 | **FUNCTIONAL_ANALYSIS:** I-30 to I-39 are the TM inputs. With CR-C7-02 the gear command reaches TM over I-34. With C7-Q04, the indications reach TM over I-38. No new interface ID is needed. | Consistency of the N² matrix. | — |

## 10. ICDs touched

| ICD | TM items |
| --- | --- |
| ICD-AER-TST (operational data, I-40) | Record kinds, signal catalogue, timestamps, units, end-of-run rule, proposed class (IN-C7-41, -42) |
| ICD-AER-TST (crew interface, I-42) | Annunciations and indications, whose items TM records unchanged (IN-C7-11) |
| ICD-FC-AF | Axis references, recorded as defined there (IN-C7-20) |
| ICD-FCP | SI targets that cross to autoflight, recorded in the crew selection record (IN-C7-10) |
| Vehicle-model boundary ICD | Effector commands and landing gear command, recorded as defined there; TM is not a party (IN-C7-20, -30; L2-AER-TM-810) |
