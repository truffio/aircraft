## TM — Operational data output

The operational data output requirements (task C7). The subject of each statement is the operational data output, the TM subsystem of the Aeronef (glossary proposal *Operational data output*, `work/C7/glossary_proposals.md`). TM implements function F-AER-11 (FUNCTIONAL_ANALYSIS §6.1). Its inputs are the signals that the other subsystems give it (I-30 to I-39, I-45: FUNCTIONAL_ANALYSIS §3.2) and the identity of the run's configuration (I-39, from F-AER-14). Its output is the operational data, given to the TST (I-40) as ICD-AER-TST defines it.

**What TM does, and what it does not do.** TM records; it computes no quantity of its own. Each signal is the value its source gives, defined once by the source's requirement: the dynamics model (L2-AER-DYN-350, -530), FU (L2-AER-FU-250, -260), the effector subsystem (L2-AER-EF-410), and the FC, AF, FCP and NAV children that C4, C5, C8 and C6 write (`work/C7/interface_needs.md`). TM observes and feeds nothing back (FUNCTIONAL_ANALYSIS §5.2 item 4; L2-AER-TM-810), so recording cannot change the run it records.

**Releasable or protected (#69, D44).** TM does not decide, and does not enforce, which signals reach the Reverse-Engineering Effort (RVS). The owner deleted L0-CON-220 at G0: the system itself protects nothing, and the owner chooses what is released when the reverse-engineering work starts. The classification of each signal is decided with the RVS, once the plan covers that branch (D44, TT-600). TM's share is to keep each signal a separate, named data item, so that a release can contain any subset of the signals without a change to the Aeronef (L2-AER-TM-020, derived, DD-C7-04). A proposed classification of each signal, with its reasons, is in `work/C7/issues.md` (C7-Q01, C7-Q02). It is a proposal for the owner, not a requirement, and nothing in this section depends on it.

**Record kinds.** The operational data are four kinds of record (L2-AER-TM-010): the **output sample**, one every `[P-TM-010]`, which holds each sampled signal; the **crew selection record**, one per crew selection received; the **event record**, one per ground contact, a landing or a crash; and the **configuration record**, one per run. Crew selections and events keep their own step: they are not delayed to the next output sample.

**Sampling (DD-C7-01, DD-C7-02).** Output samples start at step zero and fall on a fixed grid of the step index (L2-AER-TM-140). `[P-TM-010]` is an integer multiple of the control frame period `[P-SYS-310]` (L2-AER-TM-150, derived), and the first control frame starts at step zero (FUNCTIONAL_ANALYSIS §4.2), so each output sample is taken at the first step of a control frame. A sample of step k holds, for each signal, the value that its source gives for step k, and, for a flight software signal, the value of the control frame that starts at step k (L2-AER-TM-130). One output sample therefore relates a cause to its response on one record: the vehicle state at `t_k`, what the flight software decided from it in that frame, and what the effectors and the fuel did over the step from `t_k` (MS-DYN §3.4, §10.2).

**Signals beyond the L1 closed lists.** Three TM records depend on change requests to L1 (`work/C7/issues.md` §3): the targets of the armed and active modes and the indications (L2-AER-TM-320, -330; CR-C7-01 against L1-AER-620, C7-Q04) and the landing gear command (L2-AER-TM-450; CR-C7-02 against L1-AER-630, C7-Q05). They are written for the recommended answers. If a change request is rejected, the record it supports is deleted.

**Verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would describe the implementation (the record format, buffering and encoding), which ICD-AER-TST and the design fix (D4). Each record is verified directly by its own method, and the L1 parents by roll-up (D40, D58). Procedure IDs follow the record number (IN-, AN-, TP-, DM-TM-nnn); Phase 5 (V4) writes the procedures. A test of a TM record compares the operational data with the source value. For the vehicle-model signals the source values come from the per-step recording of the vehicle-model interfaces that the TST makes for test runs (IN-C1-26, IN-C2-30, IN-C3-31). For the flight software signals they come from a recording of the flight software interfaces of the same kind (IN-C7-40), and for the crew interface from the crew interface output that the TST receives itself (I-42). The `Parameters` field of each record lists the parameters its statement and success criteria use.

**Coverage of the L1 parents.** Every L1 record allocated to TM (FUNCTIONAL_ANALYSIS §6.2: ten records) has at least one TM child.

| L1 parent | What TM guarantees, in the parent's terms | TM children |
| --- | --- | --- |
| L1-AER-260 | Each landing that DYN classifies is reported in the operational data as one event record, at the contact step, with no crash event | -600, -120 (with the Derived -610) |
| L1-AER-270 | Each crash that DYN classifies is reported as one event record, at the contact step, even when the run ends before the next output sample | -600, -120 (with the Derived -610) |
| L1-AER-590 | Output samples, crew selection records and event records are the timestamped record kinds; each carries the CV-840 timestamp of its step; every signal of a sample stands for the instant of that timestamp | -010, -100, -110, -120, -130 |
| L1-AER-600 | One output sample at step zero and one every [P-TM-010] on the step grid, to the end of the run | -140 (with the Derived -150) |
| L1-AER-610 | Each crew selection received gives one record, with its selected value in the crew-facing unit, its timestamp and the SI target passed to autoflight, or none | -110, -200, -210 |
| L1-AER-620 | Each sample holds the mode state of its control frame and the annunciations presented; with CR-C7-01, also the targets of the armed and active modes and the indications | -300, -310, -320, -330 |
| L1-AER-630 | Each sample holds the axis references, axis demands and effector commands of its control frame, and the effector outputs and fuel mass flow of its step, each defined in ICD-AER-TST, the same for each design; with CR-C7-02, also the landing gear command | -030, -400, -410, -420, -430, -440, -450 |
| L1-AER-640 | Each sample holds the vehicle state, navigation quantities, sensed acceleration, vehicle mass, remaining fuel mass and gear state of its step, each defined in ICD-AER-TST, the same for each design; each landing and crash is an event record | -030, -500, -510, -520, -530, -540, -600 |
| L1-AER-650 | One configuration record per run names the vehicle parameter set, the flight-control-law design and the autoflight implementation, with their versions | -010, -700 |
| L1-AER-690 | TM's records depend only on the run, and the run does not depend on TM | -800, -810 |

Three records are Derived: L2-AER-TM-020 (DD-C7-04, each signal a separate data item), -150 (DD-C7-02, samples on control-frame starts) and -610 (DD-C7-03, the contact values in each event record). The design decisions are proposed in `work/C7/issues.md` §4.

### L2-AER-TM-010

```req
ID:            L2-AER-TM-010
Level:         L2
Type:          Interface
Statement:     The operational data output shall give the TST its operational data only as output
  samples, crew selection records, event records and one configuration record per run, as
  ICD-AER-TST defines these record kinds.
Rationale:     L1-AER-590 names the three time-stamped record kinds (glossary *Output sample*,
  *Crew selection*, *Event record*), and L1-AER-650 adds the identity of the run's configuration.
  The list is closed, one enumeration of the kinds (D30). Each kind has its own timing: output
  samples at a fixed period (L2-AER-TM-140), crew selections and events at their own step
  (L2-AER-TM-110, -120), and the configuration record at the start of the run (L2-AER-TM-700). A
  selection or an event therefore keeps its exact step whatever [P-TM-010] is, and two selections in
  one control frame, or a landing between two output samples, are each recorded. The TST also
  receives the events directly from the dynamics model, to end the run on a crash (I-41); the event
  record of the operational data is the record of it.
  Sufficiency (L1-AER-590): L1-AER-590 asks for the CV-840 timestamp on each output sample, crew
  selection record and event record. This record makes these, with the configuration record, the
  only kinds of record; L2-AER-TM-100, -110 and -120 give each kind its timestamp, and -130 fixes the
  instant that the timestamp of a sample stands for. The configuration record belongs to the run as
  a whole, so it needs no timestamp.
  Sufficiency (L1-AER-650): see L2-AER-TM-700.
Parent(s):     L1-AER-590, L1-AER-650
Source:        N-340, N-350, N-390; CV-830, CV-840; FUNCTIONAL_ANALYSIS §3.2 I-40, I-41
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-TM-010; success criteria: ICD-AER-TST defines the output sample, the
  crew selection record, the event record and the configuration record, and the TM implementation
  gives the TST no other kind of record.
Parameters:    P-TM-010
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); P-TM-010 value TBR (TT-070),
  Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-020

```req
ID:            L2-AER-TM-020
Level:         L2
Type:          Constraint
Statement:     The operational data output shall output each signal of its operational data as a
  separate data item, named in ICD-AER-TST, that can be read without any other signal of the same
  record.
Rationale:     Derived from a design decision: DD-C7-04 (proposed). Whether each signal is releasable
  or protected is decided with the RVS (#69, D44, TT-600). The system itself protects nothing
  (L0-CON-220 deleted at the G0 owner review), so a release is assembled outside the Aeronef, from
  the operational data of a run (recommended answer to C7-Q02). For any classification to be
  applicable without a change to the Aeronef, a release must be a subset of the signals: no signal
  packs another into it, and no signal needs another to be read, for example a value whose unit,
  scale or frame is given by a second signal. The timestamp is a signal of each record, so a subset
  keeps the common time base (L1-AER-590). The proposed classification of each signal is in
  `work/C7/issues.md` (C7-Q01); it is not settled and this record does not depend on it.
Parent(s):     Derived (DD-C7-04)
Source:        N-030, N-400; REVERSE_ENGINEERING.md §3C, §7; CONOPS SC-240; L0-CON-220 (deleted)
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-TM-020; success criteria: ICD-AER-TST defines each signal as its own
  named data item with its unit or its set of values, and none by reference to the value of another
  signal; from the operational data of a run of SC-130, a copy that keeps the timestamps and only
  the signals proposed releasable in C7-Q01 is read, by a reader written from ICD-AER-TST, with no
  error, and each kept signal has the value it has in the full operational data.
Parameters:    —
TBD/TBR:       DD-C7-04 proposed, Martin, G2; releasable or protected classification of each signal
  (#69, TT-600), Martin, closes when the plan is extended to the RVS (D44); ICD-AER-TST not yet
  written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-030

```req
ID:            L2-AER-TM-030
Level:         L2
Type:          Constraint
Statement:     The operational data output shall output the same signals, with the same ICD-AER-TST
  definitions, for each flight-control-law design and each autoflight implementation that a
  configuration selects.
Rationale:     The flight-control law and the autoflight implementation are replaceable through the
  configuration (L1-AER-400, -410; L0-CON-200, -210). The operational data verify each requirement
  against whichever design runs (L1-AER-790) and, later, compare designs under the same procedures
  (CONOPS SC-220: the operational data format stays the same for both versions; N-220). The content
  lists of L1-AER-630 and -640 are closed and stated in terms that do not depend on the design: axis
  references through ICD-FC-AF, six axis demands (glossary), the effector commands of the
  vehicle-model boundary. A design that has other internal signals keeps them out of the
  operational data. The number of effector signals follows the vehicle parameter set (DD-200), not
  the control law. With L2-AER-TM-700, the configuration record is then what tells two runs of
  different designs apart.
  Sufficiency (L1-AER-630, L1-AER-640): both parents ask their children to show that each listed
  signal is defined in ICD-AER-TST. The signal records (L2-AER-TM-400 to -450, -500 to -540) each
  record their signal as ICD-AER-TST defines it; this record makes that definition independent of
  the design loaded, so the same verification, and later the same release, apply to each
  configuration.
Parent(s):     L1-AER-630, L1-AER-640
Source:        N-220, N-230, N-350; CONOPS SC-220; L0-CON-200, L0-CON-210
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-TM-030; success criteria: two runs of SC-130 from the same initial
  condition and selection script, one with the configured flight-control-law design and one with the
  test flight-control-law design of IN-C3-33, give operational data with the same record kinds and
  the same signal names, units and sets of values, and each configuration record names the design
  of its run.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); test flight-control-law design
  (IN-C3-33), Martin, when the plan is extended to the TST (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-100

```req
ID:            L2-AER-TM-100
Level:         L2
Type:          Interface
Statement:     The operational data output shall attach to each output sample the timestamp, by
  CONVENTIONS CV-840, of the simulation step whose values the sample holds.
Rationale:     CV-840: each output sample carries the step index k and the simulation time t_k of its
  step; the step index is authoritative and t_k = k times [P-SYS-300], computed as a product
  (CV-820). One time base for every record kind is what lets crew inputs, mode changes, control
  activity and responses be related (N-390, L0-OBJ-140). The simulation time is that of the model,
  not the wall clock (CV-810, CV-870).
  Sufficiency (L1-AER-590): see L2-AER-TM-010.
Parent(s):     L1-AER-590
Source:        N-390; CV-820, CV-840
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-100; success criteria: at each output sample of a run of the reference
  mission (SC-110), the step index equals that of the vehicle state the sample holds, and the
  simulation time equals the step index times [P-SYS-300] computed as a product.
Parameters:    P-SYS-300
TBD/TBR:       P-SYS-300 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-110

```req
ID:            L2-AER-TM-110
Level:         L2
Type:          Interface
Statement:     The operational data output shall attach to each crew selection record the timestamp,
  by CONVENTIONS CV-840, that the crew selection carries in the crew interface.
Rationale:     Each crew selection reaches the Aeronef as a time-stamped data item (L1-AER-480); the
  TST sets the timestamp from the selection script or from the time of an interactive selection
  (N-320, CONOPS §4.6). Keeping that timestamp lets a test measure each response from the
  selection that caused it (CV-860) and lets the RVS tie its own action to the effect (N-390).
  Whether a selection timestamped k first affects step k or step k + 1 is fixed in ICD-AER-TST
  (CV-840); TM does not move the timestamp to the control frame that takes the selection.
  Sufficiency (L1-AER-590): see L2-AER-TM-010. Sufficiency (L1-AER-610): see L2-AER-TM-200.
Parent(s):     L1-AER-590, L1-AER-610
Source:        N-320, N-390; CV-840, CV-860
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-110; success criteria: in a run with a selection script that has a
  selection of each mode engage command and of each selector, two selections at the same step and a
  selection at a step that is not the first step of a control frame, each crew selection record
  carries the step index and the simulation time of its scripted selection.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-120

```req
ID:            L2-AER-TM-120
Level:         L2
Type:          Interface
Statement:     The operational data output shall attach to each event record the timestamp of the
  contact step that the dynamics model gives with the ground-contact event.
Rationale:     The dynamics model outputs each ground-contact event with the timestamp of its contact
  step (L2-AER-DYN-530, CV-840). The contact step is the "contact sample" of L1-AER-280 (glossary
  *Contact step*) and usually falls between two output samples. TM keeps the timestamp, so the
  landing or the crash is recorded at the exact step at which it happened; the children of
  L1-AER-260 and -270 must show the event "at the contact sample".
  Sufficiency (L1-AER-590): see L2-AER-TM-010. Sufficiency (L1-AER-260, L1-AER-270): see
  L2-AER-TM-600.
Parent(s):     L1-AER-590, L1-AER-260, L1-AER-270
Source:        I-37; CV-840; L2-AER-DYN-530
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-120; success criteria: in each contact test of L2-AER-DYN-510 and -520,
  and in a run of SC-130 with two landings, including contacts at steps that are not output sample
  steps, each event record carries the step index and the simulation time of the contact step that
  the dynamics model gives.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-130

```req
ID:            L2-AER-TM-130
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample, for each signal, the
  value that the source of the signal gives for the simulation step of the sample, or, for a signal
  of the flight software, for the control frame that contains that step.
Rationale:     CV-840: a value timestamped k is the value at t_k. For quantities that are held over a
  step or computed once per frame, the source defines its value of step k: the vehicle state of step
  k, with its acceleration quantities evaluated as MS-DYN §3.4 states (DD-080); the effector outputs
  and the fuel mass flow of step k, held over the step from t_k to t_(k+1) (MS-DYN §10.2, DD-100); the
  masses of step k; and the flight software values, computed once per control frame and held over
  its steps (L1-AER-680). TM takes each value as its source defines it and does not interpolate,
  filter or re-sample (DD-C7-01, proposed). With L2-AER-TM-150 the sample step is the first step of
  its control frame, so a sample holds the state from which the flight software computed that
  frame's values, and the effector and fuel response to them over the step. The values of step k
  are complete when the TST commands the step from step k (IN-C1-38), which is when TM can output
  the sample.
  Sufficiency (L1-AER-590): the timestamp must stand for the same instant for each signal of a
  record, or the correlation that L0-OBJ-140 asks for would mix steps; this record fixes that
  instant.
Parent(s):     L1-AER-590
Source:        CV-840; MS-DYN §3.4, §10.2; FUNCTIONAL_ANALYSIS §4.2; DD-080, DD-100
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-130; success criteria: in a run of SC-130, at each output sample, the
  vehicle state, gear state, sensed acceleration, vehicle mass, remaining fuel mass, fuel mass flow
  and effector outputs equal the values of the sample's step in the per-step recording of the
  vehicle-model interfaces (IN-C1-26, IN-C2-30, IN-C3-31), and each flight software signal equals
  its value for the control frame that contains that step in the recording of the flight software
  interfaces (IN-C7-40), with no difference other than floating-point representation.
Parameters:    —
TBD/TBR:       DD-C7-01 proposed, Martin, G2; TST recording of the vehicle-model and flight software
  interfaces (IN-C1-26, IN-C7-40), Martin, when the plan is extended to the TST (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-140

```req
ID:            L2-AER-TM-140
Level:         L2
Type:          Performance
Statement:     The operational data output shall produce one output sample for step zero and for each
  later simulation step whose simulation time is a whole multiple of [P-TM-010], up to the last step
  from which the TST commands a step.
Rationale:     L1-AER-600: one output sample every [P-TM-010] of simulation time. Counting from step
  zero puts the samples on a fixed grid of the step index (CV-820): the step indices of the samples are the whole
  multiples of [P-TM-010] divided by [P-SYS-300], a whole number because [P-TM-010] is a whole
  multiple of [P-SYS-310] (L2-AER-TM-150) and [P-SYS-310] of [P-SYS-300] (L1-AER-680). Step zero is
  a sample, so the first sample reports the initial condition (L1-AER-660, -950 children). A step's
  values are complete when the TST commands the step from it (L2-AER-TM-130), so the last sample is
  the last sample step from which the TST commanded a step. A crash ends the run, often between two
  samples; its event record carries the contact values (L2-AER-TM-610), so no extra sample is
  needed, and the spacing of L1-AER-600 holds.
  Sufficiency (L1-AER-600): exactly one sample per [P-TM-010] on the step grid, from the start of the
  run to its last commanded step, is the rate L1-AER-600 states.
Parent(s):     L1-AER-600
Source:        N-340; CV-820, CV-830
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-140; success criteria: in a run of SC-110 and in a run of SC-130, the
  first output sample has step index zero, the step indices of consecutive samples differ by
  [P-TM-010] divided by [P-SYS-300], no step index appears in two samples, and the last sample is
  that of the last sample step from which the TST commanded a step.
Parameters:    P-TM-010, P-SYS-300, P-SYS-310
TBD/TBR:       P-TM-010, P-SYS-300, P-SYS-310 values TBR (TT-070, TT-590), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-150

```req
ID:            L2-AER-TM-150
Level:         L2
Type:          Constraint
Statement:     The operational data output shall use an output sample period [P-TM-010] that is an
  integer multiple of the control frame period [P-SYS-310].
Rationale:     Derived from a design decision: DD-C7-02 (proposed). The first control frame starts at
  step zero (FUNCTIONAL_ANALYSIS §4.2) and the frame period is a whole number of steps (L1-AER-680),
  so each sample step is then the first step of a control frame. The sample holds the state that the
  flight software used in that frame and the values it computed from it (L2-AER-TM-130). A period
  that is not a multiple of the frame would put some samples in the middle of a frame, holding
  flight software values computed from an earlier state, and the mode changes, which happen only at
  frames, would be recorded with an offset that varies from sample to sample. L1-AER-600 asks for an
  integer multiple of the simulation step only; this record is stronger. Proposed equal to the frame
  period, so that each control frame is recorded (C7-Q03); the per-step data that the analyses need
  come from the TST recording of the vehicle-model interfaces, not from the operational data
  (IN-C2-30, IN-C3-31).
Parent(s):     Derived (DD-C7-02)
Source:        FUNCTIONAL_ANALYSIS §4.2, §7.5; CV-830; L1-AER-680
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-TM-150; success criteria: in the parameter database, [P-TM-010] divided
  by [P-SYS-310] is a whole number of at least one, and the step index of each output sample of a
  run of SC-130 is that of the first step of a control frame.
Parameters:    P-TM-010, P-SYS-310
TBD/TBR:       DD-C7-02 proposed, Martin, G2; P-TM-010, P-SYS-310 values TBR (TT-070, TT-590), Martin,
  G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-200

```req
ID:            L2-AER-TM-200
Level:         L2
Type:          Functional
Statement:     When the flight control panel receives a crew selection, the operational data output
  shall output one crew selection record that holds the selection as received, with its selected
  value in the crew-facing unit of CONVENTIONS CV-740.
Rationale:     Crew inputs are the first of the four things L0-OBJ-140 relates (L1-AER-610;
  REVERSE_ENGINEERING §3C, §5). A crew selection is a mode engage command or a selector with its
  selected value (D71, glossary *Crew selection*). Each selection received is recorded, whether the
  panel passes it on or not (L2-AER-TM-210): a selection that has no effect is behaviour too, which
  the TST assesses and the RVS reconstructs. The selected value is recorded as the crew entered it,
  in its crew-facing unit, which CV-760 group 4 allows in the operational data. The flight control
  panel gives TM the selection as received (C8, IN-C7-10).
  Sufficiency (L1-AER-610): this record gives "each crew selection it receives", L2-AER-TM-210
  "each target that results from it", and L2-AER-TM-110 the timestamp, so each scripted selection
  appears once in the operational data with its timestamp and its target, as the children of
  L1-AER-610 must show.
Parent(s):     L1-AER-610
Source:        N-320, N-340, N-390; CV-760; D71
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-200; success criteria: in a run whose selection script has each mode engage
  command of D71 and a selection of each selector (heading, horizontal speed, target altitude,
  vertical speed), including a selected value outside its selectable range, the operational data
  hold exactly one crew selection record per scripted selection, with the command or the selector
  and the selected value, in its crew-facing unit, as scripted.
Parameters:    —
TBD/TBR:       Releasable or protected classification (#69, TT-600; proposal C7-Q01), Martin, closes
  when the plan is extended to the RVS (D44); ICD-AER-TST not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-210

```req
ID:            L2-AER-TM-210
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each crew selection record the target, in
  SI, that the flight control panel passes to autoflight from that selection, or that the flight
  control panel passes none.
Rationale:     L1-AER-610: each target that results from a crew selection. The target is the selected
  value converted by the exact CV-750 factor without rounding (CV-770), within the selectable range
  and resolution that C8 sets. What the panel passes across ICD-FCP is what autoflight flies, so TM
  records the passed value, not a recomputation of it (DD-C7-05, proposed). "None" covers a mode
  engage command, which carries no selected value, and a selection that the panel does not pass. The
  pair of the selected value (L2-AER-TM-200) and the target shows the conversion and the acceptance
  of each selection.
  Sufficiency (L1-AER-610): see L2-AER-TM-200.
Parent(s):     L1-AER-610
Source:        N-390; CV-770; D55, D71; FUNCTIONAL_ANALYSIS §3.2 I-19
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-210; success criteria: in the run of TP-TM-200, each record of a selected
  value inside its range and on its selection resolution holds the SI target equal to the selected
  value times its CV-750 factor; each record of a mode engage command, and of a selection that the
  panel does not pass, holds the indication that none was passed; each SI target equals the target
  that crosses ICD-FCP to autoflight in the recording of the flight software interfaces (IN-C7-40).
Parameters:    —
TBD/TBR:       DD-C7-05 proposed, Martin, G2; ICD-FCP not yet written (TT-680), Martin, G2 (I1);
  releasable or protected classification (#69, TT-600; proposal C7-Q01), Martin, closes when the
  plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-300

```req
ID:            L2-AER-TM-300
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the mode state that
  autoflight gives for the control frame that contains the sample's step, as ICD-AER-TST defines
  the signal.
Rationale:     Mode changes are the second thing L0-OBJ-140 relates (L1-AER-620); the RVS reconstructs
  them (L0-SUC-100, -110) and the mode-transition tests assess them. The mode state is the armed and
  active modes of each mode group and whether autoflight is engaged (glossary *Mode state*, TBR,
  C5), so one signal covers the horizontal and vertical modes and the modes that govern both axes
  (D56, D69). Mode changes happen only at control frames; with the sample period equal to the frame
  period (C7-Q03), each change appears at the sample of the frame in which it occurs, as the children
  of L1-AER-620 must show. Autoflight gives TM the mode state of each frame (C5, IN-C7-30). The
  signal carries the mode names of the design (glossary note on mode names); the annunciations carry
  the same state as the crew sees it, which is why C7-Q01 proposes the two different classes.
  Sufficiency (L1-AER-620): this record gives the armed and active modes, L2-AER-TM-310 the
  annunciations presented, which are the two items of L1-AER-620; L2-AER-TM-320 and -330 add the
  targets and the indications of CR-C7-01.
Parent(s):     L1-AER-620
Source:        N-060, N-210, N-340, N-390; D16, D56, D69
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-300; success criteria: in the mode-transition tests of each transition of
  AF_MODE_LOGIC and in a run of SC-110, the mode state of each output sample equals the mode state
  that autoflight gives for the control frame of that sample in the recording of the flight software
  interfaces (IN-C7-40), and each change of mode state appears first at the sample of the control
  frame in which it occurs.
Parameters:    P-TM-010, P-SYS-310
TBD/TBR:       Mode state definition TBR and AF_MODE_LOGIC not yet written (TT-670), Martin, G2 (C5);
  P-TM-010, P-SYS-310 values TBR (TT-070), Martin, G2 (I1); releasable or protected classification
  (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-310

```req
ID:            L2-AER-TM-310
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the annunciations that
  the flight control panel presents at that output sample, as the crew interface data items of
  ICD-AER-TST define them.
Rationale:     L1-AER-620: the annunciations presented to the crew. The flight control panel presents
  them at each output sample, in crew-facing units (L1-AER-490, -500), with the labels and the gear
  position that C5 and C8 set (L1-AER-470). TM records them as presented, unchanged, which CV-760
  group 4 allows. That lets the TST measure the annunciation latency [P-SYS-470] from the operational
  data (L1-AER-470, CV-860) and gives the RVS what the crew saw (N-210, N-380). The fuel alerts
  (LOW FUEL, FUEL EXHAUSTED) are annunciations, so they are recorded here at each sample, not as
  event records (C7-Q06).
  Sufficiency (L1-AER-620): see L2-AER-TM-300.
Parent(s):     L1-AER-620
Source:        N-060, N-210, N-380, N-390; CV-760; CONOPS §4.3, §4.6
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-310; success criteria: in the mode-transition tests, in a run of SC-130 and
  in a run of SC-110 through the low-fuel alert and fuel exhaustion, at each output sample, the
  recorded annunciations equal, item by item, the crew interface annunciations that the flight
  control panel outputs to the TST at the same sample (I-42).
Parameters:    P-SYS-470
TBD/TBR:       P-SYS-470 value TBR (TT-070), Martin, G2 (I1); annunciation labels (C5, C8, TT-670),
  Martin, G2; releasable or protected classification (#69, TT-600; proposal C7-Q01), Martin, closes
  when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-320

```req
ID:            L2-AER-TM-320
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample, in SI, the target of
  each armed mode and of each active mode that autoflight gives for the control frame that contains
  the sample's step.
Rationale:     The TST assesses captures and holds against the target that autoflight flies, in SI:
  the altitude that Altitude hold captures, the position that Stationary and Hover hold (the
  reference position of L1-AER-460), the heading held. The annunciations show the selected targets
  in crew-facing units at the display resolutions [P-TM-020] to [P-TM-050], too coarse for tolerances
  such as [P-SYS-450], and a target that autoflight sets is not a crew selection, so L1-AER-610 does
  not record it. CR-C7-01 adds the targets to L1-AER-620 (C7-Q04); this record is written for that
  change and is deleted if it is rejected. Autoflight gives TM the targets of each frame (C5,
  IN-C7-30).
  Sufficiency (L1-AER-620): see L2-AER-TM-300.
Parent(s):     L1-AER-620
Source:        N-060, N-340; CONOPS §4.4; L1-AER-460; CR-C7-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-320; success criteria: in the mode-transition tests and in a run of SC-110,
  at each output sample, the recorded target of each armed and active mode equals, in its SI unit,
  the target that autoflight gives for the control frame of that sample in the recording of the
  flight software interfaces (IN-C7-40); at the sample of each capture of Altitude hold and of each
  engagement of Stationary and of Hover, the recorded target is the captured altitude or the held
  position.
Parameters:    P-TM-020, P-TM-030, P-TM-040, P-TM-050, P-SYS-450
TBD/TBR:       CR-C7-01 proposed (C7-Q04), Martin, G2; P-TM-020 to P-TM-050 values TBR (TT-210),
  Martin, G2 (C8); P-SYS-450 value TBR (TT-050), Martin, G2; releasable or protected classification
  (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-330

```req
ID:            L2-AER-TM-330
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the indications that
  the flight control panel presents at that output sample, as the crew interface data items of
  ICD-AER-TST define them.
Rationale:     The indications are the vehicle quantities the crew sees, in crew-facing units:
  altitude, vertical speed, horizontal speed, heading, track and remaining fuel (glossary
  *Indication*, L1-AER-490). CONOPS §4.6 lists the indications in the operational data, and
  FUNCTIONAL_ANALYSIS I-38 carries the presentation to TM, but L1-AER-620 names the annunciations
  only; CR-C7-01 adds the indications (C7-Q04), and this record is deleted if it is rejected. The SI
  quantities are recorded already (L2-AER-TM-510, -530); the indications add what the crew actually
  saw: the display rounding [P-TM-020] to [P-TM-050] and what the panel shows while a quantity is
  not valid (CV-580). TM records them as presented (CV-760 group 4).
  Sufficiency (L1-AER-620): see L2-AER-TM-300.
Parent(s):     L1-AER-620
Source:        N-150, N-380, N-390; CONOPS §4.3, §4.6; CV-580, CV-760; CR-C7-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-330; success criteria: in a run of SC-130 and in a run of SC-110, at each
  output sample, the recorded indications equal, item by item, the crew interface indications that
  the flight control panel outputs to the TST at the same sample (I-42).
Parameters:    P-TM-020, P-TM-030, P-TM-040, P-TM-050
TBD/TBR:       CR-C7-01 proposed (C7-Q04), Martin, G2; P-TM-020 to P-TM-050 values TBR (TT-210),
  Martin, G2 (C8); releasable or protected classification (#69, TT-600; proposal C7-Q01), Martin,
  closes when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-400

```req
ID:            L2-AER-TM-400
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the axis references
  that flight control receives from autoflight for the control frame that contains the sample's
  step, as ICD-FC-AF defines them.
Rationale:     Control activity is the third thing L0-OBJ-140 relates (L1-AER-630,
  TESTING_ENVIRONMENT §8). The axis references are the only data autoflight passes to flight
  control (D15, L1-AER-420), with the off value on the ground (glossary *Axis reference*, D69), so
  recording them shows the boundary between guidance and regulation. Which quantity each reference
  is, is set by C4 and C5 in ICD-FC-AF; TM records them as defined there. L1-AER-630 is allocated to
  FC, not AF, so flight control gives TM the references it receives (C4, IN-C7-20).
  Sufficiency (L1-AER-630): L1-AER-630 closes the list to the axis references, the axis demands, the
  effector commands, the effector outputs and the fuel mass flow. L2-AER-TM-400 to -440 record each,
  from flight control (references, demands, commands), the effector subsystem (outputs,
  L2-AER-EF-410) and FU (fuel mass flow, L2-AER-FU-250), at each output sample; L2-AER-TM-030 keeps
  their ICD-AER-TST definitions the same for each design. L2-AER-TM-450 adds the landing gear command
  of CR-C7-02.
Parent(s):     L1-AER-630
Source:        N-250, N-340; TESTING_ENVIRONMENT.md §8; FUNCTIONAL_ANALYSIS §3.2 I-13, I-33
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-400; success criteria: in a run of SC-130 (start on the ground, takeoff,
  hover, landing), each output sample holds the axis references of ICD-FC-AF equal to those of the
  control frame of that sample in the recording of the flight software interfaces (IN-C7-40), and
  holds the off value at each sample on the ground before the takeoff and after the landing.
Parameters:    —
TBD/TBR:       ICD-FC-AF and ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or
  protected classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended
  to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-410

```req
ID:            L2-AER-TM-410
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the six axis demands
  that flight control computes for the control frame that contains the sample's step, as
  ICD-AER-TST defines the signal.
Rationale:     The axis demands are the force along, and the moment about, each body axis that the
  regulation function asks the allocation function to produce, six per control frame (glossary
  *Axis demand*, F-AER-05, F-AER-06), in N and N·m in the body frame (CV-310, CV-320). They are
  internal to flight control (I-11), so flight control gives them to TM (C4, IN-C7-20). With the
  references and the effector commands they show regulation and allocation separately (N-240,
  N-260).
  Sufficiency (L1-AER-630): see L2-AER-TM-400.
Parent(s):     L1-AER-630
Source:        N-240, N-250, N-260, N-340; FUNCTIONAL_ANALYSIS §3.2 I-11, I-33
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-410; success criteria: in a run of SC-130, each output sample holds three
  force demands in N and three moment demands in N·m equal to those of the control frame of that
  sample in the recording of the flight software interfaces (IN-C7-40).
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-420

```req
ID:            L2-AER-TM-420
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the effector commands
  that flight control gives the effector subsystem for the control frame that contains the sample's
  step, as the vehicle-model boundary ICD defines them.
Rationale:     The effector commands are one effector command per effector, a force in N along its
  direction of action, and the effector activation state, on or off (glossary *Effector command*,
  DD-180). They cross the vehicle-model boundary once per control frame (L1-AER-430,
  L2-AER-EF-400). The activation state shows the effectors switched off on the ground and on again
  for a takeoff (D69), so no other signal is needed for it (B3 impact list, C7). The number of
  commands follows the vehicle parameter set (DD-200).
  Sufficiency (L1-AER-630): see L2-AER-TM-400.
Parent(s):     L1-AER-630
Source:        N-250, N-340; D69; FUNCTIONAL_ANALYSIS §3.2 I-12, I-33
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-420; success criteria: in a run of SC-130, each output sample holds one
  effector command in N per effector of the vehicle parameter set and the effector activation
  state, equal to those of the control frame of that sample in the per-step recording of the
  vehicle-model interfaces (IN-C3-31), with the activation state off at each sample on the ground
  before the takeoff.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1); releasable or
  protected classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended
  to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-430

```req
ID:            L2-AER-TM-430
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the effector output of
  each effector that the effector subsystem gives for the simulation step of the sample, as
  ICD-AER-TST defines the signal.
Rationale:     The effector outputs are the effector subsystem's item of the closed list of
  L1-AER-630; it gives TM the output of each effector at each step (L2-AER-EF-410), and TM samples
  them. An effector output is a force in N along the effector's direction of action, held over the
  step (glossary *Effector output*). With the effector commands of the same sample it shows the
  command response and the saturation (N-260).
  Sufficiency (L1-AER-630): see L2-AER-TM-400.
Parent(s):     L1-AER-630
Source:        N-250, N-260, N-340; L2-AER-EF-410; FUNCTIONAL_ANALYSIS §3.2 I-30
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-430; success criteria: in a run of the reference mission (SC-110), each
  output sample holds one effector output in N per effector, equal to the output of the sample's
  step in the per-step recording of the vehicle-model interfaces (IN-C3-31).
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-440

```req
ID:            L2-AER-TM-440
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the fuel mass flow that
  the FU subsystem gives for the simulation step of the sample, as ICD-AER-TST defines the signal.
Rationale:     The fuel mass flow is FU's item of the closed list of L1-AER-630; FU gives TM the flow
  of each step (L2-AER-FU-250), in kg/s (CV-720), and TM samples it. It ties the control activity to
  the fuel used (N-250, N-280). The fuel-mass integral check uses the flow of every step, from the
  TST recording, not the sampled flow (D65, IN-C2-30).
  Sufficiency (L1-AER-630): see L2-AER-TM-400.
Parent(s):     L1-AER-630
Source:        N-250, N-280, N-340; L2-AER-FU-250; FUNCTIONAL_ANALYSIS §3.2 I-31
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-440; success criteria: in a run of the reference mission (SC-110), each
  output sample holds the fuel mass flow in kg/s equal to that of the sample's step in the per-step
  recording of the FU outputs (IN-C2-30), and zero at each sample on the ground with the effectors
  off.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-450

```req
ID:            L2-AER-TM-450
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the landing gear
  command that autoflight gives the vehicle model for the control frame that contains the sample's
  step, as the vehicle-model boundary ICD defines it.
Rationale:     The children of L1-AER-910 must show that after each change of the gear command in
  flight the gear state shows the gear in transit and then in the commanded position within
  [P-DYN-050]. The gear state is recorded (L2-AER-TM-540), but the command is not in the closed lists
  of L1-AER-620 to -640, so the operational data would show the effect without its cause. The
  command is control activity across the vehicle-model boundary (L1-AER-430, I-43), extend or
  retract, once per control frame (L2-AER-DYN-360). CR-C7-02 adds it to L1-AER-630 and adds AF to
  that record's allocation (C7-Q05); this record is deleted if it is rejected. Autoflight gives TM
  the command of each frame (C5, IN-C7-30).
  Sufficiency (L1-AER-630): see L2-AER-TM-400.
Parent(s):     L1-AER-630
Source:        N-450; D69; L1-AER-910; FUNCTIONAL_ANALYSIS §3.2 I-34, I-43; CR-C7-02
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-450; success criteria: in a run of SC-130, each output sample holds the
  landing gear command of the control frame of that sample, equal to the command in the per-step
  recording of the vehicle-model interfaces (IN-C1-26), and the first sample with each new command
  is that of the control frame in which autoflight first issues it.
Parameters:    P-DYN-050
TBD/TBR:       CR-C7-02 proposed (C7-Q05), Martin, G2; P-DYN-050 value TBR (TT-850), Martin, G2 (C1);
  vehicle-model boundary ICD home (IN-B1-01, TT-720), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-500

```req
ID:            L2-AER-TM-500
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the vehicle state that
  the dynamics model gives for the simulation step of the sample, as ICD-AER-TST defines the
  signal.
Rationale:     Vehicle responses are the fourth thing L0-OBJ-140 relates (L1-AER-640). The vehicle
  state is the position, the velocity, the attitude quaternion with the Euler angles derived from it
  (L2-AER-DYN-070) and the body rates and vehicle acceleration (glossary *Vehicle state*), which the
  dynamics model gives TM at each step (L2-AER-DYN-350). The vehicle acceleration of the sample's
  step is evaluated as MS-DYN §3.4 states, so that of step zero is known when the first step is
  commanded (IN-C1-38). The TST assesses the performance records from these values (L1-AER-300,
  -460).
  Sufficiency (L1-AER-640): L1-AER-640 closes the list to the vehicle state, the altitude, height
  above the ground, horizontal speed, vertical speed, heading and track, the sensed acceleration,
  the vehicle mass, the remaining fuel mass, the gear state and each landing and crash event.
  L2-AER-TM-500 to -540 record the first nine items at each output sample, from the dynamics model,
  NAV and FU, and L2-AER-TM-600 records each event; L2-AER-TM-030 keeps their ICD-AER-TST
  definitions the same for each design. Together they cover the list.
Parent(s):     L1-AER-640
Source:        N-250, N-340, N-390; L2-AER-DYN-350; FUNCTIONAL_ANALYSIS §3.2 I-32
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-500; success criteria: in a run of the reference mission (SC-110) and in a
  run of SC-130, each output sample holds the position in m, the velocity in m/s, the attitude
  quaternion, the heading, pitch and roll angles in rad, the body rates in rad/s and the vehicle
  acceleration in m/s², each equal to that of the sample's step in the per-step recording of the
  vehicle-model interfaces (IN-C1-26).
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-510

```req
ID:            L2-AER-TM-510
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the navigation
  quantities, each with its validity, that NAV gives for the control frame that contains the
  sample's step, as ICD-AER-TST defines the signals.
Rationale:     L1-AER-640 lists the altitude, the height above the ground, the horizontal speed, the
  vertical speed, the heading and the track; these are the navigation quantities, each with its
  validity (glossary *Navigation quantities*, CV-580), which NAV computes once per control frame
  (L1-AER-530). The validity is part of each quantity: the track has no meaning at zero horizontal
  speed, so a recorded track without it could not be assessed. The height above the ground lets the
  TST assess takeoffs, landings and rests on the ground (L1-AER-920 to -970). NAV gives TM the
  quantities of each frame (C6, IN-C7-50).
  Sufficiency (L1-AER-640): see L2-AER-TM-500.
Parent(s):     L1-AER-640
Source:        N-340, N-390; CV-400 to CV-580; FUNCTIONAL_ANALYSIS §3.2 I-35
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-510; success criteria: in a run of SC-130 and in a run of the turn in place
  of SC-120, each output sample holds the altitude and the height above the ground in m, the
  horizontal and vertical speeds in m/s, the heading and the track in rad, and the validity of each,
  equal to those NAV gives for the control frame of that sample in the recording of the flight
  software interfaces (IN-C7-40), with the track not valid at each sample at zero horizontal speed.
Parameters:    —
TBD/TBR:       Navigation validity thresholds (TT-200), Martin, G2 (C6); ICD-AER-TST not yet written
  (TT-680), Martin, G2 (I1); releasable or protected classification (#69, TT-600; proposal C7-Q01),
  Martin, closes when the plan is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-520

```req
ID:            L2-AER-TM-520
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the sensed acceleration
  at the centre of gravity that the dynamics model gives for the simulation step of the sample, as
  ICD-AER-TST defines the signal.
Rationale:     The crew limit is on the sensed acceleration at the centre of gravity (D38, D45,
  L1-AER-290), which is not part of the vehicle state (glossary). The dynamics model computes it at
  each step in the body frame (L2-AER-DYN-300) and gives it to TM (L2-AER-DYN-350), so the TST can
  assess the limit in each run.
  Sufficiency (L1-AER-640): see L2-AER-TM-500.
Parent(s):     L1-AER-640
Source:        N-170, N-340; D38, D45; L2-AER-DYN-300, -350
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-520; success criteria: in a run of SC-130, each output sample holds the
  sensed acceleration in m/s² along the three body axes, equal to that of the sample's step in the
  per-step recording of the vehicle-model interfaces (IN-C1-26), of magnitude [P-DYN-010] at each
  sample on the ground.
Parameters:    P-DYN-010
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-530

```req
ID:            L2-AER-TM-530
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the vehicle mass and
  the remaining fuel mass that the FU subsystem gives for the simulation step of the sample, as
  ICD-AER-TST defines the signals.
Rationale:     The vehicle responses include the masses (L1-AER-640): the TST needs them for the fuel
  used per leg of the reference mission (N-250) and for the crew-limit check (L1-AER-290). FU gives
  both at each step in kg (L2-AER-FU-260). The two are one pair of FU outputs of the same step
  (D30); the remaining fuel mass is recorded in SI here, and in pounds as the fuel indication
  (L2-AER-TM-330).
  Sufficiency (L1-AER-640): see L2-AER-TM-500.
Parent(s):     L1-AER-640
Source:        N-150, N-250, N-340; L2-AER-FU-260; FUNCTIONAL_ANALYSIS §3.2 I-31
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-530; success criteria: in a run of the reference mission (SC-110), each
  output sample holds the vehicle mass and the remaining fuel mass in kg, each equal to that of the
  sample's step in the per-step recording of the FU outputs (IN-C2-30).
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-540

```req
ID:            L2-AER-TM-540
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each output sample the gear state that the
  dynamics model gives for the simulation step of the sample, as ICD-AER-TST defines the signal.
Rationale:     The gear state is the gear position, extended, retracted or in transit, and whether the
  vehicle is on the ground (glossary *Gear state*, L2-AER-DYN-290). The dynamics model gives it to
  TM at each step (L2-AER-DYN-350). With the height above the ground (L2-AER-TM-510) it lets the TST
  assess the takeoffs, landings and rests on the ground (L1-AER-640 rationale, L1-AER-920 to -970),
  and with the landing gear command (L2-AER-TM-450) the gear movement of L1-AER-910.
  Sufficiency (L1-AER-640): see L2-AER-TM-500.
Parent(s):     L1-AER-640
Source:        N-450; D69; L2-AER-DYN-290, -350; FUNCTIONAL_ANALYSIS §3.2 I-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-540; success criteria: in a run of SC-130, each output sample holds the gear
  position and the on-the-ground state, equal to those of the sample's step in the per-step
  recording of the vehicle-model interfaces (IN-C1-26), with the gear in transit at the samples
  between the retraction command and the gear retracted.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-600

```req
ID:            L2-AER-TM-600
Level:         L2
Type:          Functional
Statement:     When the dynamics model outputs a ground-contact event, the operational data output
  shall output one event record with the classification, landing or crash, that the dynamics model
  gives.
Rationale:     L1-AER-260 and -270: report a landing or a crash in the operational data; L1-AER-640:
  each landing and crash event. The dynamics model detects each contact, classifies it with the fuel
  availability of FU and outputs one event per contact (L2-AER-DYN-370, -500 to -530). TM records
  each event once and creates none of its own, so a landing gives one landing event and no crash
  event. A run can hold several landings and at most one crash (IN-C1-37). The TST also receives the
  event directly, to end the run on a crash (I-41). The fuel alerts are not event records: they are
  annunciations, recorded at each output sample (L2-AER-TM-310; C7-Q06, CR-C7-03).
  Sufficiency (L1-AER-260, L1-AER-270): the dynamics model detects and classifies each contact and
  outputs one event (its children), FU gives it the fuel availability (its children, CR-C2-04), and
  TM reports the event in the operational data (this record) at the contact step (L2-AER-TM-120),
  with the values of the contact (L2-AER-TM-610). Together they give one correctly classified
  landing or crash event in the operational data at the contact step, which is what the two parents
  ask the children to show.
  Sufficiency (L1-AER-640): see L2-AER-TM-500.
Parent(s):     L1-AER-260, L1-AER-270, L1-AER-640
Source:        N-370, N-450; D37, D68, D69, D73; L2-AER-DYN-530; FUNCTIONAL_ANALYSIS §3.2 I-37
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-600; success criteria: in each contact test of L2-AER-DYN-510 and -520 (a
  landing within the envelope with fuel remaining, a contact just outside each speed limit, a
  contact with the gear retracted, a free fall from fuel exhaustion) and in a run of SC-130 with two
  takeoffs and landings, the operational data hold exactly one event record per contact, with the
  classification that the dynamics model gives, and no other event record.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-610

```req
ID:            L2-AER-TM-610
Level:         L2
Type:          Functional
Statement:     The operational data output shall record in each event record the vertical speed and
  the horizontal speed by which the dynamics model classified the contact, and the vehicle state
  and the gear state that the dynamics model reports for the contact step.
Rationale:     Derived from a design decision: DD-C7-03 (proposed). The contact step usually falls
  between two output samples, and a crash ends the run, often before the next sample
  (L2-AER-TM-140), so without these values the operational data would not show the contact itself.
  The speeds are those of the propagated state, by which the contact is classified against the
  envelope [P-SYS-500], [P-SYS-510] (L1-AER-280, MS-DYN §9.4). The reported state differs from them:
  a landing reports the rest state, with zero velocity (L2-AER-DYN-560), and a crash the state raised
  onto the datum plane (L2-AER-DYN-540). Both are needed to read an event. An extra output sample at
  the contact step would break the fixed spacing of L1-AER-600, so the values go in the event record
  instead. The dynamics model gives the classification speeds with the event (C1, IN-C7-01); the
  record kind is one closed list of the contact values (D30).
Parent(s):     Derived (DD-C7-03)
Source:        N-370, N-390; MS-DYN §9.4, §9.5, §9.8; L2-AER-DYN-530, -540, -560
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-610; success criteria: in each contact test of L2-AER-DYN-510 and -520 and
  at each landing of a run of SC-130, each event record holds the vertical speed and the horizontal
  speed of the propagated state of the contact step, in m/s, equal to those in the per-step
  recording of the vehicle-model interfaces (IN-C1-26), and the vehicle state and gear state that
  the dynamics model reports for the contact step.
Parameters:    P-SYS-500, P-SYS-510
TBD/TBR:       DD-C7-03 proposed (C7-Q07), Martin, G2; classification speeds with the DYN event
  (IN-C7-01), Martin, G2 (I1); P-SYS-500, P-SYS-510 values TBR (TT-090), Martin, G2; releasable or
  protected classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended
  to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-700

```req
ID:            L2-AER-TM-700
Level:         L2
Type:          Interface
Statement:     When a run starts, the operational data output shall output, before the first output
  sample, one configuration record with the identifier and the version of the vehicle parameter
  set, of the flight-control-law design and of the autoflight implementation of the run's
  configuration.
Rationale:     A result is evidence only if the configuration that produced it is known (N-350,
  L1-AER-650; CONOPS SC-200 step 6). TM takes the three identities from the configuration that the
  TST starts the run with (F-AER-14, I-39; glossary *Configuration (run)*) and outputs them before
  any sample, so each record of the run is tied to them. The TST adds its own run metadata, such as
  the software version and the wall-clock start time (CV-870). The record is one closed list of
  three identities (D30). C7-Q01 proposes the identifiers as releasable if they carry no design
  content; that is an ICD-AER-TST matter.
  Sufficiency (L1-AER-650): L1-AER-650 asks for the identifier and version of the vehicle parameter
  set, the flight-control-law design and the autoflight implementation, for each run; this record
  gives them once per run, and L2-AER-TM-030 keeps the signals the same for each design, so the
  configuration record is what tells the runs of different designs apart.
Parent(s):     L1-AER-650
Source:        N-350; CV-870; CONOPS §4.6, SC-200; FUNCTIONAL_ANALYSIS §3.2 I-39
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-700; success criteria: two runs started with different configurations,
  the configured one and a test variant with another vehicle parameter set version and the test
  flight-control-law design of IN-C3-33, each give exactly one configuration record, before their
  first output sample, whose identifiers and versions match those that the TST started that run
  with.
Parameters:    —
TBD/TBR:       ICD-AER-TST not yet written (TT-680), Martin, G2 (I1); releasable or protected
  classification (#69, TT-600; proposal C7-Q01), Martin, closes when the plan is extended to the
  RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-800

```req
ID:            L2-AER-TM-800
Level:         L2
Type:          Constraint
Statement:     The operational data output shall compute each record of a run only from the signals,
  the timestamps and the configuration identity that the functions of the Aeronef give it in that
  run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59). TM adds no
  variation if its records depend on nothing but the run: no wall-clock time, no random source, no
  state carried over from another run or another simulation instance, and no dependence on how fast
  the run executes (CV-810, CV-870; CONOPS SC-200, SC-210). TM copies values without computing new
  ones (L2-AER-TM-130), so its records repeat whenever their sources repeat. Bit-identical results
  are not required (D25, D59); the tolerances are those of each success criterion (D63 Q4).
  Sufficiency (L1-AER-690): see L2-AER-TM-810.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59; CV-810, CV-870
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-TM-800; success criteria: two executions of SC-110 and of SC-130 with the same
  configuration, initial condition, selection script and TST step and wind inputs, in two simulation
  instances, one faster than real time and one in real time, give the same verdict on each success
  criterion of TP-TM-100 to TP-TM-700, and the same record kinds with the same step indices.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-TM-810

```req
ID:            L2-AER-TM-810
Level:         L2
Type:          Constraint
Statement:     The operational data output shall give no data to the vehicle model or to the flight
  software.
Rationale:     TM observes every interface and feeds nothing back (FUNCTIONAL_ANALYSIS §3.1, §5.2 item
  4), so recording cannot change the behaviour it records: a run's verdicts do not depend on what TM
  records, nor on which signals a release later keeps (CONOPS SC-240: the released Aeronef behaves
  the same as the protected one). For the same reason TM is not a party to the vehicle-model
  boundary (L1-AER-430) or to the panel boundary (L1-AER-880). The prohibition is one thought, two
  receivers (D30).
  Sufficiency (L1-AER-690): every subsystem contributes to the operational data (L1-AER-690
  rationale). TM's share is that its records depend only on the run (L2-AER-TM-800) and that the run
  does not depend on TM (this record), so a repeated run gives the same operational data and the
  same verdicts.
Parent(s):     L1-AER-690
Source:        FUNCTIONAL_ANALYSIS §3.1, §5.2; CONOPS SC-240; N-330, N-400
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-TM-810; success criteria: in the interface definitions (ICD-AER-TST, the
  vehicle-model boundary ICD, ICD-FC-AF, ICD-NAV-AF, ICD-FCP) and in the implementation, no function
  of the vehicle model or of the flight software reads an output of the operational data output.
Parameters:    —
TBD/TBR:       Interface control documents not yet written (TT-680), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```
