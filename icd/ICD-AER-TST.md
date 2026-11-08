# ICD-AER-TST — Aeronef to the test environment (Aeronef side)

**Status:** Draft, written at integration (I1, 2026-11-08) from the interface needs of A2, A3, B1 and C1 to C8. Baselined with L2 at G2. This is the Aeronef side of the interface. The TST side is written when the plan covers the TST (D44).
**Parties:** the Aeronef (all subsystems) and the TST. The crew acts through the TST, which supplies the crew selections and receives the crew interface output (L0-ASM-120). The RVS never uses this interface; it sees only the releasable subset of the operational data (D44, D76).
**Classification:** Protected design material. The releasable data dictionary for the RVS is written outside the Aeronef from this document and is not part of it (IN-C7-43).
**Related:** [CONVENTIONS](../specs/CONVENTIONS.md) CV-720 to CV-780, CV-820 to CV-860, [FUNCTIONAL_ANALYSIS](../specs/FUNCTIONAL_ANALYSIS.md) I-21 to I-28 and I-30 to I-45, L1-AER-590 to -690.

## 1. Scope

Everything that crosses between the Aeronef and the TST: the run set-up (configuration, initial condition), the per-step inputs (simulation step command, wind), the crew interface (input and output), the operational data and the events. The Aeronef side only: frame rate, units, state vector, effector commands and operational data. The vehicle-model boundary inside the Aeronef is ICD-VM-FS, and the other internal interfaces are ICD-FC-AF, ICD-NAV-AF and ICD-FCP.

## 2. Conventions

| Item | Rule |
| --- | --- |
| Units | SI inside the Aeronef and in every signal of §5 and §6, with the angles in rad (CV-720). Crew units (CV-740: ft, ft/min, kt, deg, lb) appear in the crew interface (§4), in the initial selected values (§3.3) and in signals S-03, S-06 and S-08 only (CV-760 group 4). |
| Frames, signs | CONVENTIONS CV-120 to CV-350. The state vector is position in L, velocity in V (north, east, down), attitude as a unit quaternion with Euler angles derived (CV-250, CV-260), body rates in B. |
| Time base | The vehicle model advances in fixed simulation steps of `[P-SYS-300]`. The step index k is an integer from 0 (CV-820); the simulation time is `t_k = k · [P-SYS-300]`. There is no calendar time in the model (CV-870). |
| Control frame | The flight software executes once per control frame of period `[P-SYS-310]`, an integer multiple of the simulation step (L1-AER-680, DD-010). The first control frame starts at step 0. |
| Output sample | One record every `[P-TM-010]`: an integer multiple of `[P-SYS-310]`, so of `[P-SYS-300]`, with the first sample at step 0. Each sample step is therefore the first step of a control frame (DD-480, L2-AER-TM-140, -150). |
| Timestamp | Step index and simulation time (CV-840), on every output sample, crew selection record and event record. The step index is authoritative. |
| **Input timing** | An input timestamped k first affects the computation of step k: the wind of step k acts over step k (DD-060), and a crew selection timestamped k is taken at the first control frame that starts at or after step k (FUNCTIONAL_ANALYSIS §4.2, L2-AER-FCP-080), so that it can change the effector commands from that frame's first step. This fixes the open point of CV-840. |
| Determinism | The same configuration, initial condition and selection script give the same pass or fail verdicts and agree within the tolerances of each success criterion; they need not be bit-identical (D59, L1-AER-690). Runs of one instance do not depend on another (SC-210). |
| Identifiers | Configuration identifiers (versions) carry no design content, so that they can be released (IN-C7-41, L2-AER-TM-700). |

## 3. Run set-up (TST to Aeronef)

### 3.1 Configuration (I-27)

| Item | Content | Records |
| --- | --- | --- |
| Vehicle parameter set | The values of the vehicle model parameters and of the navigation parameters, identified by a version: P-DYN-010 to -400 (the gravity-free check configuration sets P-DYN-010 to zero, D72), P-FU-010 to -100, P-EF-020 and P-EF-100 to -130 (number, directions, points of application, output limits of the effectors), P-NAV-010 and P-NAV-030 | L2-AER-DYN-440; L2-AER-FU-010, -330; L2-AER-EF-050; L2-AER-NAV-330 |
| Flight-control-law design | One selection, with identifier and version (I-22) | L2-AER-FC-050 |
| Autoflight implementation | One selection, with identifier and version | L2-AER-AF-010 |

### 3.2 Initial condition (I-21, I-23, I-27)

| Item | Content | Rule | Records |
| --- | --- | --- | --- |
| Position, velocity | North, east, altitude (m); velocity in V (m/s) | A ground start may omit the altitude: the rest altitude `[P-DYN-030]/2 + [P-DYN-040]` replaces it | L2-AER-DYN-430, -450 to -470 |
| Attitude, body rates | Unit quaternion; (p, q, r) in rad/s | | L2-AER-DYN-430 |
| Landing gear position | `extended` or `retracted` only | `extended` is a start on the ground (DD-230): the rest state is taken from the horizontal position and the heading; a non-zero velocity, body rate, pitch or roll is an initial-condition error. `retracted` is an **airborne test start**, for test runs and credibility checks only (D73, B3-1); a body at or below the ground is an error | L2-AER-DYN-460, -470 |
| Fuel mass | kg, from zero to `[P-FU-010]` | A value outside the range is rejected, not clamped (DD-140) | L2-AER-FU-010, -020, -030 |
| Initial mode state | The five fields of AF_MODE_LOGIC §3, one of the valid initial states IC-1 to IC-7 | A ground start carries the empty mode state | L2-AER-AF-900, -910 |
| Initial selected values | The four selectors' values, in crew units (deg, kt, ft, ft/min signed) | Checked as selections (DD-560) | L2-AER-FCP-520, -530 |

### 3.3 Initial-condition error (Aeronef to TST)

An item that fails its check gives an initial-condition error that names the item and its value. It can come from DYN, FU, AF, FCP or the vehicle parameter set (an inertia item that does not match its derived value, L2-AER-FU-330). The run does not start and no output sample follows (G2-F11). Records: L2-AER-DYN-460, -470; L2-AER-FU-030, -330; L2-AER-AF-910; L2-AER-FCP-530.

## 4. Crew interface (I-26, I-28, I-42)

The same interface serves a script and a human (N-320, SC-230). How it is drawn is the TST's (L1-AER-510).

### 4.1 Input: crew selections (TST to FCP)

Twelve items, each with its timestamp (CV-840); a value is in its crew unit.

| Item | Value | Records |
| --- | --- | --- |
| Mode selection: STAT, HDG, ALT, GO ALT, V/S, GO HOVER, TAKEOFF, LAND | None | L2-AER-FCP-020 |
| Heading selector | deg, [0, 360), north as 0 | L2-AER-FCP-100 |
| Horizontal speed selector | kt, from 0 to the maximum speed, a ground speed | L2-AER-FCP-110 |
| Altitude selector | ft | L2-AER-FCP-120 |
| Vertical speed selector | ft/min, signed, positive up | L2-AER-FCP-130 |

A data item that names no listed selection, or with a malformed value, is refused at the crew interface. Two selections with equal timestamps are ordered by their order of receipt (in a script, their order in the script). There is no Hover selection and no autoflight disengage selection (D71, D76).

### 4.2 Output: crew interface output (FCP to TST), at each output sample

| Item | Content | Records |
| --- | --- | --- |
| Annunciations (four) | Mode state (the mode labels of AF_MODE_LOGIC §2), targets with their quantity, gear position (GEAR DOWN, GEAR UP, GEAR TRANSIT), fuel alert (LOW FUEL, FUEL EXHAUSTED, or none) | L2-AER-FCP-030, -040, -300 to -340, -390 to -410 |
| Selector readouts (four) | The value each selector holds, as selected, in its crew unit | L2-AER-FCP-350 |
| Indications (six) | Altitude (ft), vertical speed (ft/min), horizontal speed (kt), heading (deg), track (deg), remaining fuel (lb); each with a validity flag, the track and heading not shown as a number when invalid | L2-AER-FCP-210, -220, -360 to -380 |

No layout, graphics or symbology (L1-AER-510). The values are rounded as CV-780 states, to `[P-TM-020]` to `[P-TM-050]` and `[P-FCP-010]`.

## 5. Per-step inputs and the run

| Item | Content | Records |
| --- | --- | --- |
| Simulation step command (I-25) | Advance the vehicle model by one step of `[P-SYS-300]`, with the wind velocity at `t_k` (north, east; the down component is zero) | L1-AER-670; L2-AER-DYN-140, -410 |
| Wind | The TST applies only winds inside the wind envelope: the steady wind up to `[P-SYS-430]`, gusts up to `[P-SYS-560]` built up over at least `[P-SYS-570]`, and at a liftoff at most `[P-SYS-580]` (D51, D62, D73) | MS-DYN §5.4 |
| Run end | The TST ends the run on a **crash** event, on the scenario's end condition, or at a maximum run time. A landing does not end the run (D69). A step commanded after a crash leaves the state unchanged | L2-AER-DYN-530, -550 |
| End of data | A sample of step k is complete when the TST commands the step from k. When a crash ends the run, the data end with the event record and the last complete sample before it | L2-AER-TM-140, -610 |

## 6. Operational data (Aeronef to TST), I-30 to I-40

### 6.1 Record kinds

| Kind | When | Content | Records |
| --- | --- | --- | --- |
| Configuration record | Once per run, before the first output sample | Identifier and version of the vehicle parameter set, the flight-control-law design and the autoflight implementation | L2-AER-TM-700 |
| Output sample | Each sample step | The sampled signals of §6.2 | L2-AER-TM-100, -130, -140 |
| Crew selection record | Each crew selection, at its own timestamp | The selection as received, with its selected value and crew unit, whether the panel accepted it, and the SI target passed to autoflight, or `none`; for a selected value, the SI target that autoflight takes; for a mode selection, autoflight's decision, `accepted` or `refused` (IN-C5-40) | L2-AER-TM-110, -200, -210, -220, -230 |
| Event record | Each ground contact, at the contact step | The classification (`landing` or `crash`), the vertical and horizontal speed of the propagated state by which it was classified, and the vehicle state and gear state reported for the contact step (DD-490). A run can hold several landing events and at most one crash | L2-AER-TM-120, -600, -610; L2-AER-DYN-530 |

### 6.2 Signal catalogue

Each signal is a separate, named data item, readable without any other signal of its record (DD-500, L2-AER-TM-020). "Per step" is the value its source gives for the sample's step. "Per frame" is the value of the control frame that starts at the sample step (DD-470). There is no interpolation, filtering or re-sampling. The **proposed class** column is the working proposal of C7-Q01 (D76). It is not settled: the classification is decided with the RVS when the plan covers it (#69, D44, TT-600). The two conditional entries (S-12, S-18a) depend on what the operating manuals will say.

| ID | Signal | Unit or values | Source | Timing | TM record | Proposed class |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 | Timestamp: step index, simulation time | integer; s | TM (CV-840) | Each record | L2-AER-TM-100 to -120 | Releasable |
| S-02 | Configuration: identifier and version of the vehicle parameter set, flight-control-law design and autoflight implementation | strings, opaque | Run set-up (I-39) | Once per run | -700 | Releasable if opaque |
| S-03 | Crew selection as received: mode engage command, or selector with its selected value | command set of §4.1; ft, ft/min, kt, deg | FCP (I-36) | Each selection | -200 | Releasable |
| S-04 | SI target passed to autoflight from the selection, or `none` | m, m/s, rad; or none | FCP (I-19, I-36) | With S-03 | -210 | Releasable |
| S-04b | SI target that autoflight takes from the selector, with the control frame that takes it (IN-C5-40) | m, m/s, rad | AF (I-34), L2-AER-AF-830 | With S-03 | -230 | Releasable |
| S-05 | Mode state: the five fields | AF_MODE_LOGIC §3 | AF (I-34) | Per frame | -300 | Protected |
| S-06 | Annunciations presented | §4.2 | FCP (I-38) | Each output sample | -310 | Releasable |
| S-07 | Target of each armed and active mode (CR-C7-01) | m, m/s, rad | AF (I-34) | Per frame | -320 | Protected |
| S-08 | Indications presented (CR-C7-01) | §4.2, crew units | FCP (I-38) | Each output sample | -330 | Releasable |
| S-09 | Axis references (six), or the off value | as ICD-FC-AF | FC, as received from AF (I-13, I-33) | Per frame | -400 | Protected |
| S-10 | Axis demands: three forces, three moments, body frame | N, N·m | FC (I-11, I-33) | Per frame | -410 | Protected |
| S-11 | Effector commands (one per effector) and the effector activation state | N; on / off | FC (I-12, I-33) | Per frame | -420 | Protected |
| S-12 | Effector output of each effector | N | EF, L2-AER-EF-410 (I-30) | Per step | -430 | Releasable (conditional) |
| S-13 | Fuel mass flow | kg/s | FU, L2-AER-FU-250 (I-31) | Per step | -440 | Releasable |
| S-14 | Landing gear command (CR-C7-02) | extend / retract | AF (I-34, I-43) | Per frame | -450 | Protected |
| S-15 | Vehicle state: position, velocity, attitude quaternion, heading, pitch and roll angles, body rates, vehicle acceleration | m, m/s, 1, rad, rad/s, m/s² | DYN, L2-AER-DYN-350 (I-32) | Per step | -500 | Releasable |
| S-16 | Navigation quantities with their validity: altitude, height above the ground, horizontal speed, vertical speed, heading, track (the position and velocity components are in S-15) | m, m/s, rad; valid / not valid | NAV (I-35) | Per frame | -510 | Values releasable, validity protected |
| S-17 | Sensed acceleration at the centre of gravity, body frame | m/s² | DYN, L2-AER-DYN-350 (I-32) | Per step | -520 | Releasable |
| S-18a | Vehicle mass | kg | FU, L2-AER-FU-260 (I-31) | Per step | -530 | Protected unless the manual states the empty mass (conditional) |
| S-18b | Remaining fuel mass | kg | FU, L2-AER-FU-260 (I-31) | Per step | -530 | Releasable |
| S-19 | Gear state: gear position, on the ground | extended / retracted / in transit; true / false | DYN, L2-AER-DYN-290, -350 (I-45) | Per step | -540 | Releasable |
| S-20 | Event: classification | landing / crash | DYN, L2-AER-DYN-530 (I-37) | Each contact | -600, -120 | Releasable |
| S-21 | Event: classification speeds (vertical, horizontal), reported vehicle state and gear state of the contact step | m/s; as S-15, S-19 | DYN | With S-20 | -610 | Releasable |

Principle of the proposal: releasable are the signals that the crew enters and sees, the motion and physical outcomes that an outside observer could record, and the opaque identity of the configuration; protected are the signals that cross an internal interface, the design's own state variables and values that give a design parameter directly (C7-Q01). The release is a subset of the signals, assembled outside the Aeronef (DD-500, D76). A released Aeronef behaves as the protected one (SC-240).

## 7. Recordings the TST owes the test procedures

These are not operational data. They are TST requirements for when the plan covers the TST (D44), listed here so that the Aeronef test procedures can rely on them.

| Need | Content | Source |
| --- | --- | --- |
| Per-step recording of the vehicle-model interfaces | Control force and moment, vehicle mass, wind, ground reaction, gear state, landing gear command, vehicle acceleration and sensed acceleration at each simulation step, without changing the configuration | IN-C1-26, IN-C2-30, IN-C3-31, IN-C4-31, IN-C7-03 |
| Recording of the flight software interfaces | At each control frame, the values on ICD-FC-AF, ICD-NAV-AF and ICD-FCP and the signals S-04, S-04b, S-05, S-07, S-09 to S-11, S-14, S-16 at their interface | IN-C7-40, IN-C5-70, IN-C8-40 |
| Test sources | A test autoflight variant sending scripted axis references; a test flight-control-law design; a way to run the panel with scripted annunciation content, navigation quantities and fuel state | IN-C4-30, IN-C3-33, IN-C7-44, IN-C8-40 |
| Test runs | Airborne test starts (tumbling run, credibility checks), a run with a crosswind, a run through the track validity speed, runs with modified vehicle parameter sets, a second effector layout | IN-C6-51, IN-C1-47, IN-C4-36 |
| Interactive interface | Shows the crew interface output to a human and takes the selections into the same data items as a script | IN-C8-41 |
| Wind limit | Only winds inside the envelope, including the liftoff limit | IN-C1-25 |

## 8. Traceability

| Aeronef side | L2-AER-DYN-430 to -470, -530, -550; L2-AER-FU-010 to -030, -250, -260, -330; L2-AER-EF-050, -410; L2-AER-FC-050, -250; L2-AER-AF-010, -820 to -840, -900 to -910; L2-AER-NAV-250, -330; L2-AER-FCP-010 to -140, -520, -530; L2-AER-TM (all) |
| --- | --- |
| L1 | L1-AER-480, -490, -590 to -690, -950 |
| Decisions | DD-010, DD-060, DD-230, DD-470 to DD-510, DD-560 |
| Open | TT-600 (classification, D44); the TST side of this ICD (D44) |
