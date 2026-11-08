## AF — Autoflight

The autoflight requirements (task C5). The subject of each statement is the autoflight subsystem (AF), one of the four flight-software subsystems with FCP, NAV and FC (D55). AF implements F-AER-07 and F-AER-08 and part of F-AER-14 (FUNCTIONAL_ANALYSIS §6.1): it decides which modes are armed and active, turns the crew's selections into references for the six degrees of freedom (guidance), commands the landing gear and gives the annunciation content. It runs once per control frame, after NAV and before FC (DD-010). Inputs: the mode selections, the selector targets and the accepted selectors from FCP; the navigation quantities from NAV; the gear state from DYN and the fuel state from FU; the initial mode state. Outputs: the axis references to FC, the landing gear command to DYN, the annunciation content to FCP, and the mode state, targets and gear command to TM.

**The mode logic is a specification of its own.** The state, the decisions on the eight mode selections in each state, the arming and the captures, the handovers, the target rules, the heading behaviour in each mode, the gear rules, the fuel exhaustion and the valid initial states are in `specs/AF_MODE_LOGIC.md`, as tables with row IDs (DT, TR, TG, PR, HD, GR, IC). METHODOLOGY §8.3 prescribes this for mode logic: a short requirement that references a decision table. These records point to it by name, because a statement cannot carry a section number, and L2-AER-AF-010 makes it binding on every autoflight implementation (D15). The catalogue is D56 extended by D69: Stationary, Heading, Altitude hold, Go to altitude, Vertical speed, Go to hover, Hover, Takeoff and Land; one horizontal and one vertical mode are active at a time, and the last four govern both axes. Pitch and roll stay at zero (D57).

**What AF guarantees and what FC guarantees.** AF shapes the references (position and velocity, altitude and vertical speed, heading and heading rate, level pitch and roll) within the acceleration limits, and FC tracks them (L2-AER-AF-090; the L1 budgets split this way: [P-AF-160] and [P-FC-010]). The records of AF's own outputs are therefore about the references and the mode state. The tolerances of the vehicle in each mode ([P-AF-090] to [P-AF-130], [P-AF-170]) are vehicle-level statements with `Allocated to: FC, EF`; the split of each between the AF reference and the FC tracking is for Phase 4.

**Allocation and Phase 4.** A mode record with `Allocated to: AF` has its children in the per-mode L3 sections of Phase 4 (M0 Stationary as the pattern, then M2, M3, M5, M8), which refine the engagement, capture shape, stopping profile, tolerances and flow-down inside the rows of AF_MODE_LOGIC. Until those sections exist the trace check shows these records as childless, as it does for L1 parents before L2. A record with `Allocated to: —` is a leaf at L2 and is verified directly by its own method.

**Verification.** Procedure IDs follow the record number (TP-, AN-, IN-, DM-AF-nnn); Phase 5 (V1) writes them. Most are tests on the TST with a scripted selection sequence and the operational data (mode state, targets, axis references, gear command), the four things L0-OBJ-140 relates. Two tests read the interface itself (ICD-FCP, ICD-FC-AF) and need the TST to record the flight-software interfaces (IN-C7-40, IN-C8-40). The decisions and transitions of AF_MODE_LOGIC are covered by TP-AF-010, -120 and -300 row by row.

**Ground operations, fuel exhaustion and the panel.** On the ground no mode is active and only Takeoff is accepted (L2-AER-AF-140, -750); Land ends in that state (L2-AER-AF-270). At fuel exhaustion autoflight disengages and refuses every selection (L2-AER-AF-860, -870, D68). The panel has no Hover selection and no disengage selection (D71): Hover is left by a selection of a group mode (L2-AER-AF-190), and there is no crew disengage, since with no manual control a disengaged airborne vehicle would have nothing flying it.

**Coverage of the L1 parents.** Every live L1 record allocated to AF has at least one AF child. L1-AER-340 is Deleted (D56) and has none. L1-AER-360 (endurance) is allocated to FU and EF only; the AF share of its premise is the constant references of Hover (L2-AER-AF-640).

| L1 parent | What AF guarantees, in the parent's terms | AF children |
| --- | --- | --- |
| L1-AER-290 | The reference acceleration is bounded by the manoeuvre limit, the AF share of the crew budget; FC bounds its transients, FU supplies the mass, DYN the sensed acceleration | -420 |
| L1-AER-300 | The manoeuvre acceleration of the translational reference (horizontal, turning and vertical) is at most the AF share, with the heading-rate bound closing the turn case (D72 Q1) | -420, -430, -440 |
| L1-AER-310 | Heading commands each horizontal speed from zero up to the maximum and holds it within the speed tolerance; FC and EF sustain it | -530, -610 |
| L1-AER-320 | Go to altitude and Vertical speed command each climb speed up to the maximum, by a bounded ramp, and hold it within the vertical speed tolerance | -320, -430, -600, -620 |
| L1-AER-330 | The same for each descent speed up to the maximum; the level-off at the selected altitude is the capture | -320, -430, -600, -620 |
| L1-AER-350 | Heading commands each heading rate up to the maximum where the speed allows, by the shorter way, and the bound keeps the lateral acceleration in budget | -440, -520 |
| L1-AER-390 | AF gives zero pitch and roll references in every mode while engaged; FC holds the angles within the tolerance | -400 |
| L1-AER-410 | The implementation is the one the configuration names | -020 |
| L1-AER-420 | Only the axis references and the off value cross to FC, each reference with a value, a rate and a regulation indication | -030, -090, -410 |
| L1-AER-430 | AF gives the gear command and takes the gear state and the fuel state, and nothing else crosses | -060 |
| L1-AER-450 | Every mode of the catalogue (nine) has a mode record; the mode state, the exclusivity, the decisions on selections, the arming, the capture, the handovers, the targets and the heading behaviour are stated; the logic is in AF_MODE_LOGIC | -010, -100, -110, -120, -130, -170, -180, -190, -220, -230, -240, -260, -300, -310, -350, -360, -450, -500, -520, -530, -540, -560, -580, -590, -620, -630, -640 |
| L1-AER-460 | The reference position is acquired (stopping position) or carried over, and held within the AF share; FC and EF give the other share | -330, -340, -500, -510, -640 |
| L1-AER-470 | AF gives the mode state, the targets and the gear position each frame and within its latency share; FCP presents them | -800, -810 |
| L1-AER-610 | AF gives the target it takes from each selector and the decision on each mode selection | -830, -840 |
| L1-AER-620 | AF gives the mode state, the targets and the gear command each frame; TM records them | -820 |
| L1-AER-660 | The initial mode state is taken or rejected; the gear command and the first references follow from the initial condition | -740, -750, -900, -910, -920 |
| L1-AER-680 | AF executes once per frame in the order of the frame | -070 |
| L1-AER-690 | AF outputs depend only on the run's inputs | -080 |
| L1-AER-880 | AF takes only the selections, targets and accepted selectors and gives only the annunciation content | -050, -800 |
| L1-AER-890 | AF takes the navigation quantities only through ICD-NAV-AF | -040 |
| L1-AER-910 | AF commands extend in Land and retract in Takeoff at the hover height, never retracts on the ground and descends only with the gear extended; DYN moves the gear | -700, -710, -720, -730 |
| L1-AER-930 | AF gives the off value whenever it is not engaged and ends it at the engagement of Takeoff; FC commands zero and EF produces zero | -140, -270, -410, -760 |
| L1-AER-950 | A ground start has no mode active, the off value and the gear command extended; only Takeoff is accepted | -140, -410, -750 |
| L1-AER-960 | Takeoff is selected on the ground with fuel, climbs at the takeoff speed to the hover height holding the position, retracts the gear and hands over to Hover | -150, -200, -250, -510, -660, -720, -760 |
| L1-AER-970 | Land is selected from Hover, extends the gear, descends only when it is extended at the landing speed over the Hover position, with the horizontal speed within the Hover tolerance, and ends at the contact | -160, -210, -260, -270, -650, -670, -700, -710 |

Two records are Derived: L2-AER-AF-860 and -870 (DD-400, the fuel exhaustion rule of D68). The design decisions proposed for AF are DD-360 to DD-420 (`work/C5/issues.md` §5). The records in this draft: 73 (Constraint 5, Functional 46, Interface 10, Performance 12); verification: Analysis 3, Demonstration 1, Inspection 5, Test 64.

### L2-AER-AF-010

```req
ID:            L2-AER-AF-010
Level:         L2
Type:          Constraint
Statement:     The autoflight subsystem shall realise the mode state, the decisions on mode
  selections, the automatic transitions, the target rules and the annunciation content that
  AF_MODE_LOGIC specifies.
Rationale:     Modes and controllers are decoupled (D15, D33): every autoflight implementation meets
  the same mode logic, so any implementation pairs with any control law. AF_MODE_LOGIC is that one
  place, and the per-mode sections of Phase 4 refine inside it. L1-AER-450 asks that the mode logic
  be specified in AF_MODE_LOGIC and that each mode of the catalogue be covered by an AF
  requirement; this record gives the specification its binding force, and the mode records below
  cover the catalogue.
  Sufficiency (L1-AER-450): with the selection, transition and mode records, this record covers
  the nine modes of D56 and D69, their arming, their transitions and their annunciation.
Parent(s):     L1-AER-450
Source:        D15, D33, D56, D69; AF_MODE_LOGIC
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-010; success criteria: a scripted sequence that covers each row of the
  tables DT, TR, TG, PR, HD, GR and IC of AF_MODE_LOGIC gives, at the control frame that follows the
  selection, the mode state, the targets and the landing gear command that the row states, in the
  operational data.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-020

```req
ID:            L2-AER-AF-020
Level:         L2
Type:          Constraint
Statement:     The autoflight subsystem shall be the autoflight implementation that the autoflight
  implementation identifier of the run's configuration names.
Rationale:     Replacing the autoflight implementation must change no vehicle model file (L0-CON-210).
  There is one implementation (D24, D42); the configuration still names it, so that a test variant
  can be named in its place. The variant must meet AF_MODE_LOGIC (L2-AER-AF-010).
  Sufficiency (L1-AER-410): L1-AER-410 is allocated to AF alone; this record is its AF child, and
  the run's use of the named implementation with unchanged vehicle model files is the whole of it.
Parent(s):     L1-AER-410
Source:        N-220; D15, D24
Allocated to:  —
Criticality:   Not assessed
Verification:  Demonstration — DM-AF-020; success criteria: a test variant of the autoflight
  implementation that realises AF_MODE_LOGIC is selected through the configuration, the run uses it
  (its identifier is in the configuration record of the operational data), and the checksums of the
  vehicle model files are unchanged.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-030

```req
ID:            L2-AER-AF-030
Level:         L2
Type:          Interface
Statement:     The autoflight subsystem shall give flight control only the axis references, with
  their off value, through the interface that ICD-FC-AF defines.
Rationale:     The single autoflight to flight-control interface (L1-AER-420, I-13). No mode state,
  target or selection crosses it (G1-F04), so no control law can depend on the mode logic. The off
  value is how autoflight tells flight control that the effectors are to be off, without naming a
  mode (L1-AER-930). The composition of an axis reference is L2-AER-AF-090.
  Sufficiency (L1-AER-420): FC has the matching record; together they give the one interface for
  every law and every implementation.
Parent(s):     L1-AER-420
Source:        D15; FUNCTIONAL_ANALYSIS I-13
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-AF-030; success criteria: ICD-FC-AF lists the axis references and the
  off value as the only items from AF to FC, and the AF implementation writes no other data to FC.
Parameters:    —
TBD/TBR:       ICD-FC-AF content, Martin, G2 (I1 with C4)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-040

```req
ID:            L2-AER-AF-040
Level:         L2
Type:          Interface
Statement:     The autoflight subsystem shall take the navigation quantities, with their validity,
  from navigation only through the interface that ICD-NAV-AF defines.
Rationale:     L1-AER-890 and I-17. AF uses the altitude, the height above the ground, the horizontal
  position, the horizontal velocity, the horizontal speed, the vertical speed and the heading; it
  does not use the track (IN-C6-10). It receives no vehicle state (L1-AER-440). The horizontal
  position and velocity are not yet in L1-AER-530 and -890 (CR-C5-01, extending CR-C6-01).
  Sufficiency (L1-AER-890): NAV has the matching record; this record is the AF side of the one
  interface.
Parent(s):     L1-AER-890
Source:        D55; FUNCTIONAL_ANALYSIS I-17
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-AF-040; success criteria: each navigation quantity that the AF
  implementation reads is an item of ICD-NAV-AF, and the AF implementation reads no other source of
  vehicle motion.
Parameters:    —
TBD/TBR:       ICD-NAV-AF content (CR-C5-01), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-050

```req
ID:            L2-AER-AF-050
Level:         L2
Type:          Interface
Statement:     The autoflight subsystem shall take from the flight control panel only the mode
  selections, the target of each selector in SI and the selectors accepted at the control frame, and
  give it only the annunciation content, through ICD-FCP.
Rationale:     L1-AER-880, I-16 and I-19. The list is closed: AF writes no selector (no heading
  synchronisation, no reset of the vertical speed selector, IN-C8-06), and a target that AF sets for
  itself reaches the crew as a target in the annunciation content. Crew units stay in FCP.
  Sufficiency (L1-AER-880): FCP, NAV and FU have the matching records; this record is the AF side.
Parent(s):     L1-AER-880
Source:        D55; FUNCTIONAL_ANALYSIS I-16, I-19
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-AF-050; success criteria: ICD-FCP lists the mode selections, the
  selector targets and the accepted selectors as the items from FCP to AF, and the annunciation
  content as the only item from AF to FCP; the AF implementation reads and writes no other.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-060

```req
ID:            L2-AER-AF-060
Level:         L2
Type:          Interface
Statement:     The autoflight subsystem shall exchange with the vehicle model only the landing gear
  command, given out, and the gear state and the fuel state, taken in, as the vehicle-model boundary
  ICD defines them.
Rationale:     L1-AER-430: the boundary is closed. AF commands the gear (I-43), reads the gear
  position and whether the vehicle is on the ground (I-45) and reads the fuel exhaustion indication
  (I-06). AF gives no effector command and reads no vehicle state. L2-AER-FU-240 gives the fuel
  state to FCP only; the AF leg of I-06 is a need on FU (IN-C5-30).
  Sufficiency (L1-AER-430): DYN, FU, EF, FC, FCP and NAV have the matching records; this is the AF
  side of the closed list.
Parent(s):     L1-AER-430
Source:        D15; FUNCTIONAL_ANALYSIS I-06, I-43, I-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-AF-060; success criteria: the boundary ICD lists the landing gear
  command as the only item from AF into the vehicle model, and the gear state and the fuel state as
  the only items from the vehicle model to AF.
Parameters:    —
TBD/TBR:       Vehicle-model boundary ICD home (IN-B1-01), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-070

```req
ID:            L2-AER-AF-070
Level:         L2
Type:          Performance
Statement:     The autoflight subsystem shall execute once at each control frame, after navigation
  and before flight control, and keep its outputs unchanged until the next control frame.
Rationale:     The flight software runs at a fixed rate in the order FCP, NAV, AF, FC (DD-010,
  L1-AER-680). The navigation quantities that AF reads carry the frame-start timestamp, so the
  quantities of frame k are ready before AF executes in frame k (IN-C6-14).
  Sufficiency (L1-AER-680): NAV, FC and FCP have the matching records; this one fixes the AF share.
Parent(s):     L1-AER-680
Source:        DD-010; FUNCTIONAL_ANALYSIS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-070; success criteria: in every test run the axis references, the mode
  state, the annunciation content and the landing gear command change only at control-frame
  boundaries, and each is computed from the navigation quantities of the same frame.
Parameters:    P-SYS-310
TBD/TBR:       P-SYS-310 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-080

```req
ID:            L2-AER-AF-080
Level:         L2
Type:          Constraint
Statement:     The autoflight subsystem shall compute each output of a control frame only from the
  run's configuration, the initial condition, the inputs of that frame and the state it held at the
  end of the previous frame.
Rationale:     Reproducible runs (L0-OBJ-110, L1-AER-690, D59): repeated runs of the same
  configuration, initial condition and selection script give the same pass or fail verdicts. AF adds
  no wall-clock time, no random number and no input other than those listed, so the only variation
  is that of the other subsystems.
  Sufficiency (L1-AER-690): each subsystem has a reproducibility child; this is the AF one.
Parent(s):     L1-AER-690
Source:        D25, D59
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-080; success criteria: two executions of the same scripted run give the
  same sequence of mode states, the same decisions on mode selections and axis references that agree
  within the tolerance of each success criterion assessed on the run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-090

```req
ID:            L2-AER-AF-090
Level:         L2
Type:          Constraint
Statement:     The autoflight subsystem shall give flight control, for each of the six degrees of
  freedom, one axis reference made of a reference value, the rate of that value and an indication of
  whether flight control regulates the value.
Rationale:     The glossary leaves "which quantity each reference is" to C4 and C5. Autoflight shapes
  the reference (position and velocity for the horizontal and vertical axes, heading and heading
  rate, and level pitch and roll) within the acceleration limits, and flight control tracks it; this
  is why the position-holding budget splits into an AF share [P-AF-160] and an FC share [P-FC-010]
  (FUNCTIONAL_ANALYSIS §7.4). The indication separates a hold (the value is regulated) from a motion
  at a rate (only the rate is regulated, as in a climb at a selected vertical speed). The frame and
  the exact items are for ICD-FC-AF (DD-360, C5-Q12).
  Sufficiency (L1-AER-420): with L2-AER-AF-030 this defines what crosses the one interface.
Parent(s):     L1-AER-420
Source:        D15, D56; FUNCTIONAL_ANALYSIS §7.4; DD-360
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-AF-090; success criteria: ICD-FC-AF defines, for each of the six
  degrees of freedom, a reference value, its rate and the regulation indication, and the AF
  implementation gives each of the three at each control frame.
Parameters:    P-AF-160, P-FC-010
TBD/TBR:       ICD-FC-AF content (C5-Q12), Martin, G2 (I1 with C4)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-100

```req
ID:            L2-AER-AF-100
Level:         L2
Type:          Functional
Statement:     The autoflight subsystem shall keep, at each control frame, a mode state made of the
  engaged indication, the active horizontal mode, the active vertical mode, the active both-axes mode
  and the armed mode, with the values and invariants that AF_MODE_LOGIC lists.
Rationale:     The mode state is one data item with a fixed set of values, the same for every
  implementation (IN-C7-31, D15). Its fields follow the mode groups of D56 and the both-axes modes
  of D69; the armed mode is one field because Altitude hold and Hover cannot be armed together
  (invariant MS-4). The state is what FCP annunciates (L1-AER-470) and what TM records
  (L1-AER-620).
  Sufficiency (L1-AER-450): the item states the "which modes are active and armed" of the
  catalogue; the rows of AF_MODE_LOGIC and the records below say how it changes.
Parent(s):     L1-AER-450
Source:        D56, D69; AF_MODE_LOGIC §3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-100; success criteria: in every test run, at every output sample, the
  recorded mode state has only the values of AF_MODE_LOGIC §3 and meets the invariants MS-1 to MS-5.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-110

```req
ID:            L2-AER-AF-110
Level:         L2
Type:          Functional
Statement:     While autoflight is engaged, the autoflight subsystem shall have either one active
  mode in each of the horizontal group and the vertical group, or one active both-axes mode and no
  active mode in either group.
Rationale:     Owner decision D56 (Q5, #6): one horizontal and one vertical mode are active at a time,
  independently, and Go to hover, Hover, Takeoff and Land are the only modes that govern both axes
  (extended by D69). Each group always has a mode while engaged (A2-Q05): a hold mode covers a
  group the crew has not chosen (rules DT-12 to DT-16).
  Sufficiency (L1-AER-450): the exclusivity rule is the "mode combination" content of the
  catalogue.
Parent(s):     L1-AER-450
Source:        D56, D69; A2-Q05
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-110; success criteria: in every test run, at every output sample while
  engaged, either both the active horizontal mode and the active vertical mode are not none and the
  active both-axes mode is none, or the active both-axes mode is not none and both groups are none.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-120

```req
ID:            L2-AER-AF-120
Level:         L2
Type:          Functional
Statement:     At each control frame, the autoflight subsystem shall decide each mode selection that
  the flight control panel gives it, in the order given, as accepted or refused according to the
  decisions of AF_MODE_LOGIC.
Rationale:     FCP filters nothing (IN-C8-01): AF decides for each of the eight mode selections in each
  mode state, so the mode logic is in one place. The order is the order of the timestamps, and of
  receipt for equal timestamps (L2-AER-FCP-090); each decision sees the state that the previous one
  left, so a script that selects two modes in one frame has one defined result.
  Sufficiency (L1-AER-450): the decision table covers every pair of mode state class and mode
  selection (25 rows for 8 selections).
Parent(s):     L1-AER-450
Source:        D15, D16; IN-C8-01, -04
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-120; success criteria: a scripted selection for each row DT-01 to DT-25
  of AF_MODE_LOGIC, from the state class of the row, is accepted or refused as the row states; two
  selections of one frame give the state of the rows applied in order.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-130

```req
ID:            L2-AER-AF-130
Level:         L2
Type:          Functional
Statement:     If the autoflight subsystem refuses a mode selection, then the autoflight subsystem
  shall leave the mode state, the axis references and the landing gear command as they would be
  without that selection.
Rationale:     A refused selection must be harmless: the panel offers every mode selection in every
  state, and a selection that does not fit the state (Land in flight, Takeoff in the air) is not an
  error (CONOPS SC-130). The crew is told nothing extra: a refusal shows as an unchanged mode state.
  The decision is recorded for the tests (L2-AER-AF-840).
  Sufficiency (L1-AER-450): with the decision table, a refusal has one defined result.
Parent(s):     L1-AER-450
Source:        D71; IN-C8-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-130; success criteria: after each refused selection of TP-AF-120 the
  mode state, the axis references and the landing gear command equal those of a run without that
  selection.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-140

```req
ID:            L2-AER-AF-140
Level:         L2
Type:          Functional
Statement:     While the vehicle is on the ground and Takeoff is not active, the autoflight subsystem
  shall refuse each mode selection other than Takeoff.
Rationale:     On the ground the effectors are off and no mode is active (D69, L1-AER-930, -950): the
  seven other modes need a vehicle that is flying. The alternative, arming them for after the
  takeoff, would let a stale selection act at a later time (C5-Q03). Land is refused because it is
  engaged only from Hover.
  Sufficiency (L1-AER-950): with L2-AER-AF-750 the ground state is "no mode active, only Takeoff
  accepted".
Parent(s):     L1-AER-950, L1-AER-930
Source:        D69; B3 impact list (C5)
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-140; success criteria: from a ground start and from the end of a
  landing, each mode selection other than Takeoff is refused and the mode state stays empty with the
  off value of the axis references.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-150

```req
ID:            L2-AER-AF-150
Level:         L2
Type:          Functional
Statement:     When Takeoff is selected while the vehicle is on the ground with fuel remaining, the
  autoflight subsystem shall make Takeoff the active both-axes mode and Hover the armed mode.
Rationale:     Takeoff (D69) is engaged on the ground and hands over to Hover (CONOPS §4.4). With no
  fuel the effectors cannot lift the vehicle, so the selection is refused rather than annunciated
  and never completed (C5-Q03, SC-130 zero-fuel variation). A low-fuel state does not refuse it:
  LOW FUEL is the crew's alert.
  Sufficiency (L1-AER-960): with L2-AER-AF-250, -660 and -720, the takeoff is selected, flown and
  handed over.
Parent(s):     L1-AER-960
Source:        D69; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-150; success criteria: in a ground start with fuel, TAKEOFF gives the
  mode state Takeoff active and Hover armed at the next control frame; with fuel exhausted it is
  refused.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-160

```req
ID:            L2-AER-AF-160
Level:         L2
Type:          Functional
Statement:     When Land is selected while Hover is active, the autoflight subsystem shall make Land
  the active both-axes mode.
Rationale:     Land is engaged only from Hover (D69): the vehicle is then stationary at the hover
  height over a known reference position, so the descent is short and vertical. In any other state
  the selection is refused (rows DT-03, DT-04, DT-06, DT-18, DT-25), and the crew reaches Hover by
  Go to hover.
  Sufficiency (L1-AER-970): with L2-AER-AF-670, -700 and -710, the landing is selected from Hover,
  flown and made on the extended gear.
Parent(s):     L1-AER-970
Source:        D69
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-160; success criteria: LAND while Hover is active gives Land active at
  the next control frame; LAND in each other state class is refused.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-170

```req
ID:            L2-AER-AF-170
Level:         L2
Type:          Functional
Statement:     When Go to hover is selected while the vehicle is airborne and Takeoff is not active,
  the autoflight subsystem shall make Go to hover the active both-axes mode and Hover the armed mode.
Rationale:     Go to hover takes the craft from whatever it is flying (D56) and arms Hover. It is also
  the go-around from Land (D70, SC-100 from below): the vehicle climbs back to the hover height. It
  is refused in Takeoff, which already ends in Hover (C5-Q02), and on the ground (rule DT-03).
  Sufficiency (L1-AER-450): the selection side of Go to hover; the manoeuvre is L2-AER-AF-630 and
  the handover L2-AER-AF-240.
Parent(s):     L1-AER-450
Source:        D56, D70; CONOPS SC-100
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-170; success criteria: GO HOVER in each airborne state class other than
  Takeoff gives Go to hover active and Hover armed at the next control frame, including during
  Land.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-180

```req
ID:            L2-AER-AF-180
Level:         L2
Type:          Functional
Statement:     When a horizontal mode or a vertical mode is selected while a mode of each group is
  active, the autoflight subsystem shall replace only the active mode of the group of the selected
  mode.
Rationale:     The two groups are independent (D56): changing one does not change the other
  (CONOPS §4.4, SC-050). A horizontal selection leaves the vertical mode, its target and its armed
  Altitude hold as they were, and the reverse.
  Sufficiency (L1-AER-450): with L2-AER-AF-190, the replacement rules cover every selection of a
  group mode.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-050
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-180; success criteria: for each pair of an airborne state with a mode in
  each group and a selection of a group mode, only the mode of the selected group changes (rows
  DT-20 to DT-22 and DT-24).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-190

```req
ID:            L2-AER-AF-190
Level:         L2
Type:          Functional
Statement:     When a horizontal mode or a vertical mode is selected while Hover or Go to hover is
  active, the autoflight subsystem shall make the selected mode active in its group and make Altitude
  hold, for a horizontal mode, or Stationary, for a vertical mode, active in the other group.
Rationale:     The crew leaves Hover by selecting a mode of one group, because the panel has no Hover
  selection (D71, IN-C8-09). The other group then needs a mode, and the one that continues what
  Hover was doing is its hold mode: Altitude hold at the altitude the vehicle has, Stationary at the
  reference position it was holding (rules TG-5, TG-6, PR-1). This reproduces SC-110 legs 2 and 8.
  The alternative, refusing the selection until both groups are chosen, makes a one-step scripted
  departure impossible (C5-Q01).
  Sufficiency (L1-AER-450): with L2-AER-AF-180, every selection of a group mode has a defined
  result in every airborne state.
Parent(s):     L1-AER-450
Source:        D56, D71; CONOPS SC-110 legs 2 and 8; C5-Q01
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-190; success criteria: from Hover and from Go to hover, each of STAT,
  HDG, ALT, GO ALT and V/S gives the state of rows DT-12 to DT-16, and the horizontal position and
  the altitude have no step at the transition.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-200

```req
ID:            L2-AER-AF-200
Level:         L2
Type:          Functional
Statement:     While Takeoff is active, the autoflight subsystem shall refuse each mode selection
  other than Takeoff.
Rationale:     The vehicle is on the ground or below the operating volume with the gear extended or in
  transit, and Takeoff already ends in Hover (CONOPS §4.4). Letting the crew redirect it there could
  leave it at a low height in a mode that holds a height only at a tolerance that the gear
  clearance does not allow (C5-Q02). The crew can leave Hover once the handover is made.
  Sufficiency (L1-AER-960): the takeoff runs to its handover without interruption.
Parent(s):     L1-AER-960
Source:        D69; C5-Q02
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-200; success criteria: each mode selection other than TAKEOFF during
  Takeoff is refused (rows DT-05, DT-06) and the takeoff reaches Hover.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-210

```req
ID:            L2-AER-AF-210
Level:         L2
Type:          Functional
Statement:     While Land is active, the autoflight subsystem shall refuse each mode selection other
  than Go to hover and Land.
Rationale:     Land flies below the hover height with the gear extended or in transit, where a contact
  is a landing or a crash (L1-AER-260, -270). The only way out is the go-around (D70): Go to hover
  climbs back to the hover height over the reference position (rows DT-07 to DT-09). Land selected
  again changes nothing (DT-08).
  Sufficiency (L1-AER-970): a landing is flown to the contact or abandoned by a defined go-around.
Parent(s):     L1-AER-970
Source:        D69, D70; C5-Q02
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-210; success criteria: during Land, each of STAT, HDG, ALT, GO ALT, V/S
  and TAKEOFF is refused and Land stays active; GO HOVER gives Go to hover active.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-220

```req
ID:            L2-AER-AF-220
Level:         L2
Type:          Functional
Statement:     When Go to altitude or Vertical speed becomes the active vertical mode, the autoflight
  subsystem shall make Altitude hold the armed mode.
Rationale:     Go to altitude and Vertical speed arm Altitude hold, so that they level off at the
  selected altitude (D56, owner 2026-11-04). The armed Altitude hold is not selected on its own; it
  is the next state of the vertical group (D16: arm first, engage when the condition is met).
  Sufficiency (L1-AER-450): with L2-AER-AF-230 and -360, the arming and the capture give the
  "then hold" of both vertical modes.
Parent(s):     L1-AER-450
Source:        D16, D56; CONOPS §4.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-220; success criteria: GO ALT and V/S each give Altitude hold armed at
  the next control frame, in every state where they are accepted.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-230

```req
ID:            L2-AER-AF-230
Level:         L2
Type:          Functional
Statement:     When the capture condition of AF_MODE_LOGIC for the armed Altitude hold is met, the
  autoflight subsystem shall make Altitude hold the active vertical mode, with its target, and clear
  the armed mode.
Rationale:     The capture is the engagement of the armed Altitude hold (glossary: capture). The
  condition is that the altitude still to go is within the tolerance [P-AF-110], or is at most the
  distance in which the vertical speed reference stops at the vertical acceleration [P-AF-230]
  (AF_MODE_LOGIC §5; DD-380); the onset of the level-off then needs no separate selection. The
  target is the selected altitude at the frame of the capture (L2-AER-AF-350 for the other cases).
  Sufficiency (L1-AER-450): the capture is the automatic transition Go to altitude to Altitude hold
  and Vertical speed to Altitude hold of the catalogue.
Parent(s):     L1-AER-450
Source:        D16, D56; DD-380; CONOPS SC-020, SC-040
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-230; success criteria: in SC-020 and SC-040 and their variations, the
  mode state changes from Go to altitude or Vertical speed with Altitude hold armed to Altitude hold
  active with nothing armed at the frame where the condition of AF_MODE_LOGIC first holds, and not
  before.
Parameters:    P-AF-110, P-AF-230
TBD/TBR:       P-AF-110 value TBR (TT-180), P-AF-230 value TBR (TT-830), Martin, G2/G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-240

```req
ID:            L2-AER-AF-240
Level:         L2
Type:          Functional
Statement:     When the vehicle is stationary at the hover height while Go to hover is active, the
  autoflight subsystem shall make Hover the active both-axes mode and clear the armed mode.
Rationale:     Hover engages once the craft is stationary at the hover height (D56). The gear is not
  a condition here: after a go-around it is extended (rule TR-04), and Hover with the gear extended is
  allowed, with the altitude tolerance [P-AF-110] inside the gear clearance (L2-AER-AF-580).
  Sufficiency (L1-AER-450): the automatic transition Go to hover to Hover of the catalogue.
Parent(s):     L1-AER-450
Source:        D56, D70; CONOPS SC-100
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-240; success criteria: in SC-100 and its variations, Hover becomes
  active with nothing armed at the first control frame at which the vehicle is stationary at the
  hover height (L2-AER-AF-260), not before.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-250

```req
ID:            L2-AER-AF-250
Level:         L2
Type:          Functional
Statement:     When the vehicle is stationary at the hover height with the landing gear retracted
  while Takeoff is active, the autoflight subsystem shall make Hover the active both-axes mode and
  clear the armed mode.
Rationale:     Takeoff hands over to Hover once the gear is retracted (CONOPS §4.4, "C5 confirms"): the
  retraction is commanded at the hover height (L2-AER-AF-720) and takes the gear transit time
  [P-DYN-050]; Hover starts when it is done, so the vehicle never holds with the gear in transit
  without Takeoff still being annunciated.
  Sufficiency (L1-AER-960): the last step of the takeoff, with L2-AER-AF-660 and -720.
Parent(s):     L1-AER-960
Source:        D69; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-250; success criteria: in SC-130, Hover becomes active at the first
  control frame at which the vehicle is stationary at the hover height and the gear state shows the
  gear retracted, and the horizontal position is within [P-SYS-450] of the ground position.
Parameters:    P-DYN-050, P-SYS-450
TBD/TBR:       P-DYN-050 value TBR (TT-850), P-SYS-450 value TBR (TT-050), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-260

```req
ID:            L2-AER-AF-260
Level:         L2
Type:          Functional
Statement:     The autoflight subsystem shall judge the vehicle stationary at the hover height only
  while the height above the ground is within [P-AF-110] of [P-AF-210], the horizontal speed is at
  most [P-AF-170] and the magnitude of the vertical speed is at most [P-AF-090].
Rationale:     "Stationary at the hover height" is the engagement condition of Hover (D56) and needs a
  definition (glossary proposal). The three tolerances are the altitude hold tolerance, the hover
  horizontal speed tolerance and the vertical speed tolerance already in the database; no new
  parameter. [P-AF-170] is at most the landing envelope horizontal speed [P-SYS-510], so that Land
  from Hover meets the envelope (L1-AER-970).
  Sufficiency (L1-AER-450, -970): the one definition used by L2-AER-AF-240 and -250.
Parent(s):     L1-AER-450, L1-AER-970
Source:        D56, D70
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-AF-260; success criteria: replaying the recorded height above the
  ground, horizontal speed and vertical speed of the SC-100 and SC-130 runs through the condition
  gives the frames at which the Hover handover occurred, and none earlier.
Parameters:    P-AF-110, P-AF-210, P-AF-170, P-AF-090, P-SYS-510
TBD/TBR:       P-AF-110, P-AF-090 values TBR and P-AF-170 value TBR (TT-180), Martin, G2/G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-270

```req
ID:            L2-AER-AF-270
Level:         L2
Type:          Functional
Statement:     When the gear state shows the vehicle on the ground while Land is active, the
  autoflight subsystem shall end Land and leave no mode active and no mode armed in the same control
  frame.
Rationale:     A landing ends the descent (D69): the contact is detected from the gear state, the
  effectors are switched off through the off value (L2-AER-AF-410), and the mode state is empty, so
  that nothing is annunciated but the gear (SC-130 step 5, C5-Q04). The same control frame as the
  detection keeps the AF share of the effectors-off latency [P-SYS-480] at one frame.
  Sufficiency (L1-AER-970, -930): with L2-AER-AF-410, the landing ends in the on-ground state of
  D69.
Parent(s):     L1-AER-970, L1-AER-930
Source:        D69; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-270; success criteria: in SC-130 and SC-110 leg 7a, the mode state is
  empty and the axis references take the off value at the first control frame whose gear state shows
  the vehicle on the ground.
Parameters:    P-SYS-480
TBD/TBR:       P-SYS-480 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-300

```req
ID:            L2-AER-AF-300
Level:         L2
Type:          Functional
Statement:     The autoflight subsystem shall evaluate the automatic transitions of AF_MODE_LOGIC once
  at each control frame, after it has decided the mode selections of that frame.
Rationale:     A fixed order makes a selection and a capture in one frame give one result (for
  example GO ALT with a selected altitude equal to the present one captures at once) and keeps the
  runs reproducible (L2-AER-AF-080). The transitions do not chain (AF_MODE_LOGIC §4), so one
  evaluation is complete. The fuel exhaustion and the end of Land are evaluated before the
  selections (TR-01, TR-02).
  Sufficiency (L1-AER-450): ties the selection rows and the transition rows into one frame
  sequence.
Parent(s):     L1-AER-450
Source:        D16; AF_MODE_LOGIC §4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-300; success criteria: GO ALT selected at the present altitude gives
  Altitude hold active at the frame of the selection; a selection and a capture in one frame give the
  state of the rows applied in the order of AF_MODE_LOGIC §4.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-310

```req
ID:            L2-AER-AF-310
Level:         L2
Type:          Functional
Statement:     When the target of a selector changes, the autoflight subsystem shall guide toward the
  new target only in a mode that uses that selector, without changing the mode state.
Rationale:     "Changing a target does not change the mode. The vehicle goes to the new target"
  (CONOPS §4.4, SC-020 step 3, SC-050 steps 1 and 2). A selector that no active or armed mode uses has
  no effect: in particular a new selected altitude does not move an Altitude hold that is already
  active, whose target is its own (rules TG-1, TG-4 of AF_MODE_LOGIC). The selectors and the modes
  that use them are the table of AF_MODE_LOGIC §9.
  Sufficiency (L1-AER-450): with L2-AER-AF-320, -350 and -520 to -530, each selected quantity is
  followed by the mode that uses it.
Parent(s):     L1-AER-450
Source:        D56; CONOPS §4.4, SC-020, SC-050
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-310; success criteria: a change of the selected speed, heading, altitude
  or vertical speed during a mode that uses it changes the corresponding reference and not the mode
  state; a change of the selected altitude during Altitude hold changes neither.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-320

```req
ID:            L2-AER-AF-320
Level:         L2
Type:          Functional
Statement:     While Go to altitude is active, the autoflight subsystem shall command a vertical
  speed toward the selected altitude whose magnitude is [P-AF-220], or that of the selected vertical
  speed once the panel has accepted one since Go to altitude was selected.
Rationale:     Go to altitude climbs or descends at the standard vertical speed, "which the crew can
  change" (D56, D70). The standard speed is not a selector value, so the panel holds whatever the
  crew last selected and AF decides which speed to fly from the accepted set of the frame
  (IN-C8-03). Go to altitude always starts at the standard speed; a selected vertical speed accepted
  in the frame of the selection, or later, replaces it. The direction is always toward the selected
  altitude, so only the magnitude of the selected vertical speed is used, and a selected vertical
  speed of zero is ignored (C5-Q08). The speeds up to [P-SYS-240] and [P-SYS-250] that the panel
  accepts (L2-AER-FCP-130) are the climb and descent capability of L1-AER-320 and -330.
  Sufficiency (L1-AER-320, -330): with L2-AER-AF-600 (the vertical speed is held), L2-AER-AF-620 and
  -430 (vertical speed in Vertical speed mode and the ramp), the climb and descent speeds up to the
  limits are commanded in both vertical modes that climb or descend.
Parent(s):     L1-AER-320, L1-AER-330
Source:        D56, D70; IN-C8-03; CONOPS SC-020
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-320; success criteria: in SC-020 and its climb variation, the vertical
  speed reference has the magnitude [P-AF-220] until a selected vertical speed is accepted and the
  magnitude of that selection from then on, toward the selected altitude, and a re-selection of GO
  ALT restarts at [P-AF-220].
Parameters:    P-AF-220, P-SYS-240, P-SYS-250
TBD/TBR:       P-SYS-240, P-SYS-250 values TBR (TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-330

```req
ID:            L2-AER-AF-330
Level:         L2
Type:          Functional
Statement:     When a mode that holds the horizontal position becomes active from a mode that does
  not, the autoflight subsystem shall set the reference position to the position at which the
  horizontal velocity reaches zero under the horizontal acceleration limit.
Rationale:     What "the position held" is when a hold is entered with the vehicle moving (SC-090 TBR,
  #78): the position at engagement cannot be held, since the vehicle is moving; the position at which
  it stops can. The modes that hold the horizontal position are Stationary, Go to hover, Hover,
  Takeoff, Land and Heading at a selected speed of zero. From the ground the velocity is zero, so the
  reference is the ground position (L1-AER-960). The limit is the part of [P-AF-200] that
  [P-AF-230] leaves (DD-420, AF_MODE_LOGIC §11); the stopping position is the horizontal position
  plus the velocity times its magnitude over twice that limit (DD-390, C5-Q05).
  Sufficiency (L1-AER-460): with L2-AER-AF-340 and -510, the reference position is defined for every
  entry to a hold, and its accuracy is the share [P-AF-160].
Parent(s):     L1-AER-460
Source:        #78, D16, D56; DD-390; CONOPS SC-090
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-AF-330; success criteria: for Stationary engaged from Heading at
  several speeds and directions, the reference position equals the position and velocity of the
  engagement frame propagated at the horizontal acceleration limit to zero velocity, within
  [P-AF-160].
Parameters:    P-AF-200, P-AF-230, P-AF-160
TBD/TBR:       P-AF-200 value TBR (TT-040), P-AF-160 value TBR (TT-050), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-340

```req
ID:            L2-AER-AF-340
Level:         L2
Type:          Functional
Statement:     When a mode that holds the horizontal position becomes active from a mode that holds
  it, the autoflight subsystem shall keep the reference position unchanged.
Rationale:     The hold modes hand over to one another without a new capture: Go to hover to Hover,
  Takeoff to Hover, Hover to Land, Hover to Stationary (DT-12, TG-6). Re-capturing at each handover
  would let the reference creep by the tracking error at every handover, and the budget [P-SYS-450]
  counts from the start of the hold, not from each handover (PR-4).
  Sufficiency (L1-AER-460): with L2-AER-AF-330, every hold has one reference position from its start.
Parent(s):     L1-AER-460
Source:        D56, D60; DD-390
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-340; success criteria: at each handover between modes that hold the
  horizontal position in SC-100, SC-130 and SC-110, the reference position is the same before and
  after, and the horizontal position stays within [P-SYS-450] of it from [P-SYS-460] after the start
  of the hold.
Parameters:    P-SYS-450, P-SYS-460
TBD/TBR:       P-SYS-450 value TBR (TT-050), P-SYS-460 value TBR (TT-060), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-350

```req
ID:            L2-AER-AF-350
Level:         L2
Type:          Functional
Statement:     When Altitude hold becomes active other than by the capture of the selected altitude,
  the autoflight subsystem shall set its target to the altitude at which the vertical speed reference
  reaches zero under [P-AF-230].
Rationale:     SC-050 step 5 TBR: with Altitude hold selected during a climb, the vehicle "holds the
  altitude reached". The target is the altitude where the vertical speed reference stops at the
  vertical acceleration (the level-off altitude, DD-380): a target at the altitude of the selection
  would need an instantaneous stop and a return (C5-Q06). It applies to ALT selected directly, to
  the group selections over Hover and Go to hover (rule TG-5) and to the start of an airborne initial
  mode state. At zero vertical speed it is the present altitude.
  Sufficiency (L1-AER-450): with L2-AER-AF-230, every Altitude hold has a defined target.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-050; DD-380
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-350; success criteria: with ALT selected during a climb and during a
  descent at several vertical speeds, the Altitude hold target recorded is the altitude of the
  selection frame plus the vertical speed reference times its magnitude over twice [P-AF-230], and
  the vertical speed reference reaches zero there.
Parameters:    P-AF-230
TBD/TBR:       P-AF-230 value TBR (TT-830), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-360

```req
ID:            L2-AER-AF-360
Level:         L2
Type:          Functional
Statement:     When Vertical speed is active and the selected altitude is not ahead in the direction
  of the selected vertical speed, the autoflight subsystem shall make Altitude hold the active
  vertical mode.
Rationale:     SC-040 TBR ("a selected altitude behind the direction of motion"). Altitude hold cannot
  capture an altitude the vehicle is moving away from, so a Vertical speed whose selected altitude is
  behind, or whose selected vertical speed is zero, ends at once in Altitude hold, by the same
  capture mechanism as the normal one (AF_MODE_LOGIC §5). Refusing the selection instead would need a
  second rule and a refusal that the crew sees only as a mode that did not engage (C5-Q06).
  Sufficiency (L1-AER-450): with L2-AER-AF-230, every Vertical speed ends in Altitude hold.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-040 TBR; C5-Q06
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-360; success criteria: V/S selected with the selected altitude below the
  vehicle and a positive selected vertical speed, with the selected altitude above it and a negative
  one, and with a zero selected vertical speed, each gives Altitude hold active at the frame of the
  selection and no Vertical speed.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-400

```req
ID:            L2-AER-AF-400
Level:         L2
Type:          Performance
Statement:     While autoflight is engaged, the autoflight subsystem shall give a pitch angle
  reference of zero and a roll angle reference of zero.
Rationale:     Pitch and roll are not used for now (D57, revising D10): the vehicle translates along
  three axes and rotates about the vertical axis only, in every mode. This is a rule for every mode
  and is stated once. AF gives the references; FC holds the angles within [P-AF-180] of them
  (L1-AER-390).
  Sufficiency (L1-AER-390): the AF child gives the level references, and the FC child holds the
  attitude to them; together they keep the angles within [P-AF-180] of zero.
Parent(s):     L1-AER-390
Source:        D57; N-160
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-400; success criteria: in every mode of every test run while engaged,
  the recorded pitch angle reference and roll angle reference are zero.
Parameters:    P-AF-180
TBD/TBR:       P-AF-180 value TBR (TT-190), Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-410

```req
ID:            L2-AER-AF-410
Level:         L2
Type:          Functional
Statement:     While autoflight is not engaged, the autoflight subsystem shall give flight control the
  off value of the axis references, from the control frame in which autoflight ceased to be engaged.
Rationale:     On the ground the effectors are off so that no fuel is used (D69, L1-AER-930); after
  fuel exhaustion they produce nothing in any case (D68). The off value replaces the six references
  and carries no mode information (L1-AER-420); FC commands zero effector output and sets the
  effector activation state off while it is given (IN-C3-26, IN-C3-30). Giving it in the frame in
  which the mode state became empty keeps the AF share of [P-SYS-480] at one control frame. The
  references leave the off value in the frame in which Takeoff or an airborne initial mode state makes
  autoflight engaged (L2-AER-AF-760).
  Sufficiency (L1-AER-930, -950): AF sets the off reference, FC commands zero and EF produces zero.
Parent(s):     L1-AER-930, L1-AER-950, L1-AER-420
Source:        D69; CONOPS SC-130; IN-C3-26
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-410; success criteria: in a ground start, after each landing and after
  fuel exhaustion, the axis references recorded take the off value at the control frame in which the
  mode state becomes empty and keep it until a mode becomes active.
Parameters:    P-SYS-480
TBD/TBR:       P-SYS-480 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-420

```req
ID:            L2-AER-AF-420
Level:         L2
Type:          Performance
Statement:     The autoflight subsystem shall keep the magnitude of the acceleration of its
  translational velocity reference at most [P-AF-200].
Rationale:     Manoeuvres are g-limited (D16): this is the autoflight share of the vehicle acceleration
  budget, [P-AF-200] plus the flight-control allowance [P-FC-020] at most [P-SYS-440]
  (FUNCTIONAL_ANALYSIS §7.2, L1-AER-300), which in turn keeps the sensed acceleration under
  [P-SYS-120] (L1-AER-290). The acceleration is that of the reference in three dimensions: the
  horizontal part, a turning velocity reference included, and the vertical part (DD-420 splits
  [P-AF-200] into a horizontal limit and the vertical one [P-AF-230]).
  Sufficiency (L1-AER-300, -290): the AF share is bounded; FC's child bounds its transients.
Parent(s):     L1-AER-300, L1-AER-290
Source:        D16, D38; FUNCTIONAL_ANALYSIS §7.2; DD-420
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-420; success criteria: in every test run, the magnitude of the change of
  the recorded translational velocity reference per control frame, divided by the frame period, is
  at most [P-AF-200], in every mode and at every transition, in winds within the wind envelope.
Parameters:    P-AF-200, P-FC-020, P-SYS-440, P-SYS-120
TBD/TBR:       P-AF-200 value TBR (TT-040), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-430

```req
ID:            L2-AER-AF-430
Level:         L2
Type:          Performance
Statement:     The autoflight subsystem shall change its vertical speed reference at a rate of at most
  [P-AF-230] in magnitude.
Rationale:     The vertical speed ramps rather than steps (D70): about ten seconds to reach the
  standard speed, and a level-off over about 170 ft. The same limit applies to an engagement, a new
  selection, a reversal and a level-off (P-AF-230 description). It is the vertical component of the
  manoeuvre acceleration, so the horizontal limit is derived from it (DD-420).
  Sufficiency (L1-AER-320, -330): the climb and descent are reached by a bounded ramp.
Parent(s):     L1-AER-320, L1-AER-330, L1-AER-300
Source:        D70
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-430; success criteria: at each transition of the vertical speed
  reference in SC-020, SC-040, SC-050, SC-130, the rate of change of the recorded vertical speed
  reference is at most [P-AF-230].
Parameters:    P-AF-230
TBD/TBR:       P-AF-230 value TBR (TT-830), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-440

```req
ID:            L2-AER-AF-440
Level:         L2
Type:          Performance
Statement:     The autoflight subsystem shall keep the magnitude of its heading rate reference at most
  [P-SYS-270] and at most the quotient of [P-AF-200] by its horizontal speed reference.
Rationale:     Owner ruling D72 Q1: [P-SYS-230] is a ground speed, and the lateral acceleration of a
  turn is the horizontal speed times the heading rate (option T1, D64). C5 bounds the commanded
  heading rate so that this product stays within [P-AF-200]. At the highest speed the quotient is a
  little above [P-SYS-270], which governs there; at lower speeds up to the stated rate is reached.
  The rate is also the heading rate capability of L1-AER-350. The bound is on the reference, so a
  tailwind or an overshoot that raises the actual ground speed is FC's transient allowance
  [P-FC-020].
  Sufficiency (L1-AER-350, -300): AF commands rates up to [P-SYS-270] where the acceleration budget
  allows, and the budget is closed by the second bound.
Parent(s):     L1-AER-350, L1-AER-300
Source:        D64, D72 (Q1); IN-C1-32; IN-C6-12; DD-420
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-440; success criteria: in heading changes at selected horizontal speeds
  from zero to [P-SYS-230], the recorded heading rate reference never exceeds [P-SYS-270], and its
  product with the recorded horizontal speed reference never exceeds [P-AF-200]; at zero speed the
  rate reaches [P-SYS-270].
Parameters:    P-SYS-270, P-AF-200, P-SYS-230, P-FC-020
TBD/TBR:       P-SYS-270 value TBR (TT-010), P-AF-200 value TBR (TT-040), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-450

```req
ID:            L2-AER-AF-450
Level:         L2
Type:          Constraint
Statement:     The autoflight subsystem shall change the heading reference only while Heading is
  active.
Rationale:     The heading behaviour of each mode (CONOPS §4.4, D57): Heading turns to the selected
  heading; in Stationary, Go to hover, Hover, Takeoff and Land the heading is held at its value when
  the first of these modes became active, and the vertical modes do not change the heading (rules
  HD-1 to HD-3). The value at the first activation is the reference in effect, or the navigation
  heading when there was none (L2-AER-AF-920).
  Sufficiency (L1-AER-450): with the Heading records, the heading behaviour in each mode is stated.
Parent(s):     L1-AER-450
Source:        D56, D57; CONOPS §4.4; A2-Q03
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-450; success criteria: in SC-110 and SC-050, the recorded heading
  reference changes only at frames where Heading is active.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-500

```req
ID:            L2-AER-AF-500
Level:         L2
Type:          Functional
Statement:     While Stationary is active, the autoflight subsystem shall give a horizontal velocity
  reference that brings the horizontal velocity to zero and a reference position that it then holds.
Rationale:     Stationary stops the horizontal motion within the acceleration limits (D16) and holds
  the position over the ground, with the effectors fighting the wind (D56, D17). The reference
  position is the stopping position (L2-AER-AF-330); the heading is held (L2-AER-AF-450); the vertical
  mode is independent. This is the reference mode; the engagement, capture shape and flow-down are
  the Phase 4 section M0.
  Sufficiency (L1-AER-450, -460): the mode record of Stationary; the accuracy of the hold is
  L2-AER-AF-510.
Parent(s):     L1-AER-450, L1-AER-460
Source:        D56; CONOPS SC-090
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-500; success criteria: in SC-090 and its wind variation, from several
  initial horizontal speeds, the horizontal velocity reference reaches zero and the reference
  position then stays fixed.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-510

```req
ID:            L2-AER-AF-510
Level:         L2
Type:          Performance
Statement:     While the horizontal position is held, the autoflight subsystem shall give a reference
  position within [P-AF-160] of the target position of the hold at each control frame that follows the
  start of the hold by at least [P-SYS-460].
Rationale:     The AF share of the position-holding budget (FUNCTIONAL_ANALYSIS §7.4, L1-AER-460): the
  reference position versus the target, through the capture and the hold, with [P-FC-010] for the
  regulation of the vehicle to the reference. The target position is the stopping position or the one
  carried over (L2-AER-AF-330, -340). The hold starts as rule PR-4 of AF_MODE_LOGIC says, and the
  time [P-SYS-460] covers the deceleration from [P-SYS-230] (about 16 s) and the capture (D70). It
  holds in Stationary, Hover, Takeoff, Land and Heading at zero speed, and, with the position error
  as a horizontal error only (D60).
  Sufficiency (L1-AER-460, -960): with the FC and EF children, [P-AF-160] plus [P-FC-010] is at most
  [P-SYS-450]; for Takeoff the target is the ground position.
Parent(s):     L1-AER-460, L1-AER-960
Source:        D60; FUNCTIONAL_ANALYSIS §7.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-AF-510; success criteria: from the recorded position and velocity of
  the first frame of each hold, and the recorded reference position, the distance between the
  reference position and the target position is at most [P-AF-160] at every frame from [P-SYS-460]
  after the start, in Stationary, Hover, Takeoff, Land and Heading at zero speed.
Parameters:    P-AF-160, P-SYS-460, P-SYS-450, P-FC-010
TBD/TBR:       P-AF-160, P-SYS-450, P-FC-010 values TBR (TT-050); P-SYS-460 value TBR (TT-060),
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-520

```req
ID:            L2-AER-AF-520
Level:         L2
Type:          Functional
Statement:     While Heading is active, the autoflight subsystem shall change the heading reference
  toward the selected heading, through the smaller angle and at the largest heading rate that the
  bound on the heading rate reference allows.
Rationale:     Heading turns the nose to the selected heading (D56), by the shorter way ("mode logic to
  confirm", SC-050 step 2; on an exact half turn clockwise, HD-1). The largest permitted rate gives
  the heading rate capability up to [P-SYS-270] (L1-AER-350) where the speed allows; at zero speed
  it turns the vehicle in place (SC-120).
  Sufficiency (L1-AER-350, -450): with L2-AER-AF-440 the heading rate is both reached and bounded.
Parent(s):     L1-AER-350, L1-AER-450
Source:        D56; CONOPS SC-050, SC-060, SC-120
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-520; success criteria: in SC-060 and SC-120, the heading reference goes
  to the selected heading through the smaller angle at the heading rate of L2-AER-AF-440, in both
  senses and across the north direction.
Parameters:    P-SYS-270
TBD/TBR:       P-SYS-270 value TBR (TT-010), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-530

```req
ID:            L2-AER-AF-530
Level:         L2
Type:          Functional
Statement:     While Heading is active with a non-zero selected horizontal speed, the autoflight
  subsystem shall give a horizontal velocity reference along the heading reference whose magnitude
  goes to the selected horizontal speed within the acceleration limit.
Rationale:     In Heading the vehicle moves along its heading at the selected horizontal speed, a
  ground speed (D56, D72): "its motion turns with" the heading (SC-050 step 2). The velocity
  direction follows the heading reference, not the final heading, so a turn bends the path. The
  selected speed runs from zero to [P-SYS-230], the capability of L1-AER-310. A speed change and a
  turn share the horizontal limit (AF_MODE_LOGIC §11, DD-420). The track follows the heading
  (CV-550 reading, SC-060); its tolerance [P-AF-140] is for the mode section M5.
  Sufficiency (L1-AER-310): the horizontal speeds up to [P-SYS-230] are commanded in Heading; the
  vehicle sustains them by the FC and EF children.
Parent(s):     L1-AER-310, L1-AER-450
Source:        D56, D72; CONOPS SC-060
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-530; success criteria: in SC-060 and its wind variation, at selected
  speeds up to and including [P-SYS-230], the horizontal velocity reference has the direction of the
  heading reference and its magnitude reaches the selected speed with the acceleration of
  L2-AER-AF-420.
Parameters:    P-SYS-230, P-AF-140
TBD/TBR:       P-AF-140 value TBD (TT-180), Martin, G3 (M5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-540

```req
ID:            L2-AER-AF-540
Level:         L2
Type:          Functional
Statement:     While Heading is active with a selected horizontal speed of zero, the autoflight
  subsystem shall hold the reference position.
Rationale:     SC-120 TBR: with no horizontal velocity a heading change turns the craft in place
  (D56). Regulating a zero velocity alone would let the vehicle drift with the integral of the
  velocity error in a wind, so that a turn in place would move it. Holding the reference position, as
  Stationary does, keeps it where it is, and Heading differs from Stationary only by the turn
  (C5-Q07). The reference position is acquired as in L2-AER-AF-330.
  Sufficiency (L1-AER-450): the zero-speed case of the Heading mode.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-120 TBR; C5-Q07
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-540; success criteria: in SC-120 with a steady wind and gusts, the
  horizontal position stays within [P-SYS-450] of its value at the start from [P-SYS-460] on, and the
  heading goes to the selected heading.
Parameters:    P-SYS-450, P-SYS-460
TBD/TBR:       P-SYS-450 value TBR (TT-050); P-SYS-460 value TBR (TT-060), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-560

```req
ID:            L2-AER-AF-560
Level:         L2
Type:          Functional
Statement:     While Altitude hold is active, the autoflight subsystem shall give an altitude
  reference equal to its target and a vertical speed reference of zero.
Rationale:     Altitude hold holds the altitude (D56): the captured selected altitude, or the level-off
  altitude of a direct selection (L2-AER-AF-230, -350). The reference approaches the target without
  passing it, within the vertical acceleration limit (L2-AER-AF-430); the vehicle overshoot is
  L2-AER-AF-590 and the hold tolerance L2-AER-AF-580. The mode section M3 refines the capture.
  Sufficiency (L1-AER-450): the mode record of Altitude hold.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-020, SC-040, SC-050
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-560; success criteria: in SC-020, SC-040 and SC-050, once Altitude hold
  is active the recorded altitude reference equals the Altitude hold target and the vertical speed
  reference is zero.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-580

```req
ID:            L2-AER-AF-580
Level:         L2
Type:          Performance
Statement:     While Altitude hold or Hover is active, the autoflight subsystem shall hold the
  altitude within [P-AF-110] of its target from [P-AF-190] after the altitude reference reaches it.
Rationale:     The altitude error is a separate tolerance from the horizontal position budget (D60,
  L1-AER-460). In Hover with the gear extended (after a go-around, or before the retraction of a
  takeoff) the error must stay inside the gear clearance, [P-AF-210] minus [P-DYN-040], with the
  tilt allowed by [P-AF-180] (IN-C1-44; the proposed values meet it, `param_proposals.md`). The
  value is shared between the AF reference and the FC regulation by the mode sections (M0, M3, M8,
  FC1). The tolerance is on the altitude of the centre of gravity; the hover target is the hover
  height above the body plus half of [P-DYN-030].
  Sufficiency (L1-AER-450): the vehicle-level tolerance of the two altitude-holding modes.
Parent(s):     L1-AER-450
Source:        D56, D60, D70; IN-C1-44
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-580; success criteria: in SC-020, SC-100, SC-110 and SC-130 with gusts
  within the wind envelope, the altitude is within [P-AF-110] of the target at every output sample
  from [P-AF-190] after the altitude reference reaches the target; in Hover with the gear extended
  the margin to the ground contact stays positive.
Parameters:    P-AF-110, P-AF-190, P-AF-210, P-DYN-040, P-AF-180
TBD/TBR:       P-AF-110, P-AF-190 values TBR (TT-180); P-AF-180 value TBR (TT-190), Martin, G2/G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-590

```req
ID:            L2-AER-AF-590
Level:         L2
Type:          Performance
Statement:     When Altitude hold captures the selected altitude, the autoflight subsystem shall keep
  the altitude from passing the selected altitude by more than [P-AF-100].
Rationale:     The level-off ends on the selected altitude "without passing it by more than
  [P-AF-100]" (CONOPS SC-020 step 4). The reference does not pass the target (L2-AER-AF-560), so the
  overshoot is the tracking overshoot of the vehicle; the tolerance is shared by the mode sections.
  Sufficiency (L1-AER-450): the capture accuracy of the two modes that capture.
Parent(s):     L1-AER-450
Source:        D56; CONOPS SC-020, SC-040
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-590; success criteria: in SC-020, SC-040 and their variations, climbing
  and descending at the standard and at the highest selectable vertical speed, the altitude does not
  pass the selected altitude by more than [P-AF-100].
Parameters:    P-AF-100
TBD/TBR:       P-AF-100 value TBR (TT-180), Martin, G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-600

```req
ID:            L2-AER-AF-600
Level:         L2
Type:          Performance
Statement:     While Vertical speed is active, or Go to altitude is active, the autoflight subsystem
  shall hold the vertical speed within [P-AF-090] of its commanded vertical speed from [P-AF-190] after
  the vertical speed reference reaches it.
Rationale:     The tracking tolerance of the selected vertical speed (L1-AER-320, -330 rationale; CONOPS
  SC-020, SC-040): "Settled" means within the tolerance, reached within a settling time after the
  reference reaches the target (the definition of [P-AF-190] proposed in
  `param_proposals.md`). The vehicle-level tolerance is shared by the AF reference and the FC regulation
  by the mode sections. Together with L2-AER-AF-320, -430 and -620, the climb and descent speeds up
  to [P-SYS-240] and [P-SYS-250] are sustained in both vertical modes.
  Sufficiency (L1-AER-320, -330): the vertical speed tolerance that the two L1 records leave to L2.
Parent(s):     L1-AER-320, L1-AER-330
Source:        D56; CONOPS SC-020, SC-040
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-600; success criteria: in SC-020 and SC-040 and their variations, at the
  standard vertical speed, at the highest climb and descent speed, and at zero and highest horizontal
  speed, the vertical speed is within [P-AF-090] of the commanded one at every output sample from
  [P-AF-190] after the reference reaches it.
Parameters:    P-AF-090, P-AF-190, P-SYS-240, P-SYS-250
TBD/TBR:       P-AF-090, P-AF-190 values TBR (TT-180), Martin, G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-610

```req
ID:            L2-AER-AF-610
Level:         L2
Type:          Performance
Statement:     While Heading is active, the autoflight subsystem shall hold the horizontal speed
  within [P-AF-120] of the selected horizontal speed from [P-AF-190] after the horizontal speed
  reference reaches it.
Rationale:     There is no separate speed mode (D56): the horizontal speed is a selector of Heading.
  The tolerance is on the ground speed (D72). It is the tracking tolerance that L1-AER-310 leaves to
  L2 ("a per-mode tolerance set at L2", P-AF-120), also at the highest speed [P-SYS-230] in the
  strongest wind.
  Sufficiency (L1-AER-310): with L2-AER-AF-530, the speeds up to [P-SYS-230] are commanded and held.
Parent(s):     L1-AER-310
Source:        D56, D72; CONOPS SC-060, SC-120
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-610; success criteria: in SC-060 and SC-120, with and without wind, at
  selected speeds up to and including [P-SYS-230], the horizontal speed is within [P-AF-120] of the
  selected speed at every output sample from [P-AF-190] after the reference reaches it.
Parameters:    P-AF-120, P-AF-190, P-SYS-230
TBD/TBR:       P-AF-120, P-AF-190 values TBR (TT-180), Martin, G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-620

```req
ID:            L2-AER-AF-620
Level:         L2
Type:          Functional
Statement:     While Vertical speed is active, the autoflight subsystem shall give a vertical speed
  reference equal to the selected vertical speed.
Rationale:     Vertical speed climbs or descends at the selected constant rate (D56); the selected rate
  is signed, positive up, and runs from minus [P-SYS-250] to [P-SYS-240] (L2-AER-FCP-130), the climb
  and descent capability of L1-AER-320 and -330. The reference reaches the rate by the ramp of
  L2-AER-AF-430. A change of the selected rate during the mode retargets the rate (L2-AER-AF-310).
  Sufficiency (L1-AER-320, -330): the mode record of Vertical speed; the end of the climb is the
  capture (L2-AER-AF-230).
Parent(s):     L1-AER-320, L1-AER-330, L1-AER-450
Source:        D56; CONOPS SC-040
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-620; success criteria: in SC-040 and its descent variation, the vertical
  speed reference equals the selected vertical speed, up to [P-SYS-240] and down to minus [P-SYS-250],
  from the end of the ramp until the capture.
Parameters:    P-SYS-240, P-SYS-250
TBD/TBR:       P-SYS-240, P-SYS-250 values TBR (TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-630

```req
ID:            L2-AER-AF-630
Level:         L2
Type:          Functional
Statement:     While Go to hover is active, the autoflight subsystem shall give references that bring
  the vehicle to zero velocity on each axis at the hover height above the ground, from above and from
  below.
Rationale:     Go to hover takes the craft from whatever it is flying, stops the horizontal motion and
  goes to the hover height, descending from above or climbing from below (D56, D70). Horizontally it
  stops as Stationary does (reference position as L2-AER-AF-330); vertically it flies to the hover
  altitude at the standard vertical speed [P-AF-220] with the ramps of L2-AER-AF-430, and the selected
  altitude and vertical speed are not used. The heading is held. Hover is armed (L2-AER-AF-170) and
  engages by L2-AER-AF-240.
  Sufficiency (L1-AER-450): the mode record of Go to hover.
Parent(s):     L1-AER-450
Source:        D56, D70; CONOPS SC-100
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-630; success criteria: in SC-100 from above at the highest horizontal
  speed, and from below as a go-around in SC-130, the horizontal and vertical velocity references go
  to zero and the vertical position reference to the hover height, with the accelerations of
  L2-AER-AF-420 and -430.
Parameters:    P-AF-210, P-AF-220
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-640

```req
ID:            L2-AER-AF-640
Level:         L2
Type:          Functional
Statement:     While Hover is active, the autoflight subsystem shall give references that hold the
  hover height above the ground and the reference position.
Rationale:     Hover holds the height and the position over the ground against the wind (D56). The
  reference position is the one carried over (L2-AER-AF-340), the heading is held, and the references
  are constant in still air, so that the fuel used in a hold is that of the weight alone (the
  premise of the endurance budget L1-AER-360 and L2-AER-FU-290).
  Sufficiency (L1-AER-450, -460): the mode record of Hover; the accuracy is L2-AER-AF-510 and -580.
Parent(s):     L1-AER-450, L1-AER-460
Source:        D56; CONOPS SC-100, SC-110 leg 1
Allocated to:  AF, FC
Criticality:   Not assessed
Verification:  Test — TP-AF-640; success criteria: while Hover is active in still air, the recorded
  position and altitude references and the heading reference are constant, and the velocity references
  are zero.
Parameters:    P-AF-210
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-650

```req
ID:            L2-AER-AF-650
Level:         L2
Type:          Performance
Statement:     While Hover is active, the autoflight subsystem shall keep the horizontal speed at most
  [P-AF-170].
Rationale:     L1-AER-970 leaves the Hover speed tolerance to C5: a Land from Hover must meet the
  landing envelope horizontal speed [P-SYS-510], so [P-AF-170] is at most [P-SYS-510]; the proposed
  value is half of it, for the gust response at the touchdown (`param_proposals.md`). The tolerance
  is on the ground speed. Land holds the Hover reference position through the contact
  (L2-AER-AF-670), so the speed at the contact is that of Hover.
  Sufficiency (L1-AER-970): with L2-AER-AF-670 and -710, the horizontal speed condition of the
  landing envelope is met.
Parent(s):     L1-AER-970
Source:        D53, D60; B3 impact list (C5)
Allocated to:  FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-650; success criteria: in SC-130 and SC-100, with and without wind
  within the wind envelope, the horizontal speed is at most [P-AF-170] at every output sample in
  Hover and at the contact of the landing, and [P-AF-170] is at most [P-SYS-510].
Parameters:    P-AF-170, P-SYS-510
TBD/TBR:       P-AF-170 value TBR (TT-920), P-SYS-510 value TBR (TT-090), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-660

```req
ID:            L2-AER-AF-660
Level:         L2
Type:          Functional
Statement:     While Takeoff is active, the autoflight subsystem shall give references that climb the
  vehicle vertically at [P-AF-240] to the hover height above the ground over its ground position,
  holding the heading.
Rationale:     Takeoff (D69) powers up, climbs at [P-AF-240] to the hover height over the current
  position, retracts the gear and hands over to Hover. The reference is a vertical speed with the
  ramp of L2-AER-AF-430 until the hover height is near, then the hover altitude (AF_MODE_LOGIC §13,
  rule TO-1); the horizontal reference holds the ground position (PR-3); the heading is held at its
  value at the engagement. Flight control keeps the vehicle on the ground until the upward force
  exceeds the weight (liftoff, IN-C1-43); the wind limit of the takeoff is [P-SYS-580].
  Sufficiency (L1-AER-960): with L2-AER-AF-150, -250, -510 and -720, the takeoff is selected, flown
  to the hover height with the gear retracted, within [P-SYS-450] of the ground position, and handed
  to Hover.
Parent(s):     L1-AER-960
Source:        D69, D70, D73; CONOPS SC-130
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-660; success criteria: in SC-130 and SC-110 leg 0, at full fuel and near
  dry mass, in still air and in a steady wind of [P-SYS-580] from several directions, the vehicle
  reaches the hover height with the gear retracted, and its horizontal position stays within
  [P-SYS-450] of the ground position.
Parameters:    P-AF-240, P-AF-210, P-SYS-580, P-SYS-450
TBD/TBR:       P-AF-240 value TBR (TT-830), P-SYS-580 value TBR (TT-860), P-SYS-450 value TBR (TT-050),
  Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-670

```req
ID:            L2-AER-AF-670
Level:         L2
Type:          Functional
Statement:     While Land is active, the autoflight subsystem shall give references that descend the
  vehicle vertically at [P-AF-240] over the reference position, holding the heading, until it gives
  the off value.
Rationale:     Land (D69) descends at [P-AF-240] from the hover height to the touchdown, well inside the
  vertical speed limit of the landing envelope [P-SYS-500]. The downward reference stays until the
  off value is given, so that flight control commands no more than the weight at the contact and the
  vehicle does not lift off again (IN-C1-43, MS-DYN liftoff rule). The descent starts only with the
  gear extended (L2-AER-AF-710). The reference position is that of Hover (PR-3), so the horizontal
  speed at the contact is that of Hover (L2-AER-AF-650).
  Sufficiency (L1-AER-970): with L2-AER-AF-160, -270, -650, -700 and -710, a landing from Hover is
  made on the extended gear within the landing envelope, at a vertical speed below [P-SYS-500].
Parent(s):     L1-AER-970
Source:        D53, D69, D70; CONOPS SC-130
Allocated to:  AF, FC, EF
Criticality:   Not assessed
Verification:  Test — TP-AF-670; success criteria: in SC-130 and SC-110 leg 7a at full fuel and near
  dry mass, in still air and in a steady wind of [P-SYS-430] with gusts of [P-SYS-560] from several
  directions, each landing from Hover gives one landing event, no crash, and the vertical speed at
  the contact is at most [P-SYS-500].
Parameters:    P-AF-240, P-SYS-500, P-SYS-430, P-SYS-560
TBD/TBR:       P-AF-240 value TBR (TT-830), P-SYS-500 value TBR (TT-090), P-SYS-430, P-SYS-560 values
  TBR (TT-030), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-700

```req
ID:            L2-AER-AF-700
Level:         L2
Type:          Functional
Statement:     When Land becomes active, the autoflight subsystem shall command the landing gear to
  extend.
Rationale:     Land extends the gear before the descent (D69, L1-AER-910). The command is issued in
  the frame in which Land becomes active, so the gear is in transit for at most the transit time
  [P-DYN-050] before the descent can start (L2-AER-AF-710). If the gear is already extended, as after
  a go-around, the command changes nothing (rule GR-3).
  Sufficiency (L1-AER-910, -970): AF commands the extension, DYN moves the gear (L2-AER-DYN-270),
  and AF descends only when it is extended.
Parent(s):     L1-AER-910, L1-AER-970
Source:        D69; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-700; success criteria: in SC-130 step 4 the recorded landing gear
  command changes to extend at the control frame in which Land becomes active.
Parameters:    P-DYN-050
TBD/TBR:       P-DYN-050 value TBR (TT-850), Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-710

```req
ID:            L2-AER-AF-710
Level:         L2
Type:          Functional
Statement:     While Land is active, the autoflight subsystem shall give a downward vertical speed
  reference only while the gear state shows the gear extended.
Rationale:     A ground contact with the gear in transit or retracted is a crash whatever the speed
  (L1-AER-270, D73 B3-3), so autoflight descends below the hover height only with the gear extended
  (L1-AER-910 rationale, IN-C1-42). Until then Land holds the hover height and the reference
  position.
  Sufficiency (L1-AER-910, -970): the other half of L2-AER-AF-700.
Parent(s):     L1-AER-910, L1-AER-970
Source:        D69, D73; IN-C1-42
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-710; success criteria: in SC-130 step 4 and with the gear starting
  retracted, the vertical speed reference is not downward until the gear state shows the gear
  extended, and the vehicle makes no ground contact with the gear in transit.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-720

```req
ID:            L2-AER-AF-720
Level:         L2
Type:          Functional
Statement:     When Takeoff has brought the vehicle to the hover height, the autoflight subsystem
  shall command the landing gear to retract.
Rationale:     Takeoff retracts the gear once the vehicle is at the hover height (D69, L1-AER-910).
  The condition is the height above the ground within [P-AF-110] of [P-AF-210] or above it while the
  vehicle is airborne (rule GR-2), so the gear is never retracted on the ground. Retracting at the
  hover height, not earlier, keeps the gear under the vehicle through the liftoff.
  Sufficiency (L1-AER-910, -960): AF commands the retraction, DYN moves the gear, and Hover starts
  when it is retracted (L2-AER-AF-250).
Parent(s):     L1-AER-910, L1-AER-960
Source:        D69; CONOPS SC-130 step 2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-720; success criteria: in SC-130 step 2 the recorded landing gear
  command changes to retract at the first control frame at which the vehicle is airborne and its
  height above the ground is within [P-AF-110] of [P-AF-210] or above it, and not before.
Parameters:    P-AF-110, P-AF-210
TBD/TBR:       P-AF-110 value TBR (TT-180), Martin, G2/G3
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-730

```req
ID:            L2-AER-AF-730
Level:         L2
Type:          Functional
Statement:     While the gear state shows the vehicle on the ground, the autoflight subsystem shall
  command the landing gear to stay extended.
Rationale:     On the ground the gear stays extended and does not respond to a retraction command,
  because a retraction there would drop the body onto the ground (L1-AER-910, L1-AER-920); a command
  to retract given on the ground would take effect at the first airborne step (IN-C1-41), which is
  after the liftoff and before the hover height. AF therefore commands extension throughout the
  on-ground state, and retracts only by L2-AER-AF-720.
  Sufficiency (L1-AER-910): the "never retract on the ground" half of the gear rules.
Parent(s):     L1-AER-910
Source:        D69; IN-C1-41
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-730; success criteria: in SC-130 from the start to the liftoff, in every
  second takeoff and after each landing, the recorded landing gear command is extend.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-740

```req
ID:            L2-AER-AF-740
Level:         L2
Type:          Functional
Statement:     When a run starts, the autoflight subsystem shall set the landing gear command to the
  gear position of the initial condition.
Rationale:     Before the first command the commanded position is the initial gear position (IN-C1-41),
  so a run does not begin with a gear movement that the crew did not ask for. A ground start has the
  gear extended (L1-AER-950); an airborne test start may have it retracted (D73).
  Sufficiency (L1-AER-660): the gear item of the initial condition reaches the command.
Parent(s):     L1-AER-660
Source:        D69, D73; IN-C1-41
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-740; success criteria: for a ground start and for an airborne start with
  the gear retracted, the landing gear command of the first control frame equals the initial gear
  position, and the gear state shows no transit.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-750

```req
ID:            L2-AER-AF-750
Level:         L2
Type:          Functional
Statement:     When a run starts on the ground, the autoflight subsystem shall start with no mode
  active, no mode armed and the off value of the axis references.
Rationale:     A run starts on the ground, on the extended gear, with the effectors off (D69,
  L1-AER-950); the recommendation to C5 was that no mode is active (A2-Q05, #60, TT-610). Takeoff is
  the mode engaged from there. A ground start with a mode in the initial condition is an
  initial-condition error (L2-AER-AF-910).
  Sufficiency (L1-AER-950): AF sets the effectors-off reference, FC commands zero and EF produces
  nothing, which is the ground start of D69.
Parent(s):     L1-AER-950, L1-AER-660
Source:        D69; CONOPS §4.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-750; success criteria: the first output sample of a ground start shows
  the empty mode state and the off value of the axis references.
Parameters:    —
TBD/TBR:       Valid initial mode states (#60, TT-610), closed here, Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-760

```req
ID:            L2-AER-AF-760
Level:         L2
Type:          Functional
Statement:     When Takeoff becomes active, the autoflight subsystem shall end the off value of the
  axis references in the same control frame.
Rationale:     "Taking off" is the interval from the engagement of Takeoff to the liftoff, the only
  time the effectors work on the ground (glossary, L1-AER-930). Flight control sets the effector
  activation state on while the references are not off (IN-C3-26), so the effectors power up in the
  frame of the selection and the liftoff follows when the upward force exceeds the weight.
  Sufficiency (L1-AER-930, -960): with L2-AER-AF-410, the off value ends exactly at the engagement
  of Takeoff and returns at the end of Land.
Parent(s):     L1-AER-930, L1-AER-960
Source:        D69; CONOPS SC-130 step 1
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-760; success criteria: in SC-130 step 1, the axis references recorded
  are not the off value from the control frame in which Takeoff becomes active.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-800

```req
ID:            L2-AER-AF-800
Level:         L2
Type:          Interface
Statement:     At each control frame, the autoflight subsystem shall give the flight control panel
  the annunciation content made of the mode state, each target in use with the quantity it applies
  to, and the landing gear position.
Rationale:     AF decides the content (which modes, which targets, the gear position); FCP presents it
  with the labels of AF_MODE_LOGIC §2 and the crew units (D55, L1-AER-470, -880, I-16). The targets in
  use are those of AF_MODE_LOGIC §9, each with its quantity (altitude, vertical speed, horizontal
  speed or heading) in SI, including a target that AF sets for itself, such as the held altitude
  (IN-C8-05, -06). The gear position is the gear state's, passed on (the gear labels are FCP's,
  IN-C8-07). An empty mode state is a valid content.
  Sufficiency (L1-AER-470): with FCP's presentation and L2-AER-AF-810, a change of the mode state, of a
  target or of the gear position reaches the crew.
Parent(s):     L1-AER-470, L1-AER-880
Source:        D55; IN-C8-05, -06
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-800; success criteria: at every control frame of SC-020, SC-050, SC-100,
  SC-130 and SC-110, the annunciation content recorded at ICD-FCP equals the mode state, the targets
  in use of AF_MODE_LOGIC §9 and the gear position of the same frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-810

```req
ID:            L2-AER-AF-810
Level:         L2
Type:          Performance
Statement:     When the autoflight subsystem receives a mode selection or a selector target, or the
  gear state changes, the autoflight subsystem shall give the annunciation content that results
  within [P-AF-060] of the change.
Rationale:     The AF share of the annunciation latency [P-SYS-470] (FUNCTIONAL_ANALYSIS §7.5):
  [P-AF-060] is at most [P-SYS-470] minus [P-TM-010], and FCP's share is one output sample period.
  A selection taken at the next control frame and processed in that frame takes two frame periods
  at most ([P-SYS-310] each), which is the proposed value of [P-AF-060]. Changes that AF causes
  itself, such as a capture or a handover, are annunciated in the content of the frame in which they
  occur (AF_MODE_LOGIC §4).
  Sufficiency (L1-AER-470): with FCP's presentation within one output sample period, a change reaches
  the crew within [P-SYS-470].
Parent(s):     L1-AER-470
Source:        FUNCTIONAL_ANALYSIS §7.5; CONOPS §4.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-810; success criteria: with the ICD-FCP interface recorded (IN-C8-40),
  for each change in the mode-transition tests the content that shows it is given within [P-AF-060]
  of the timestamp of the selection, of the target or of the gear state, and [P-AF-060] plus
  [P-TM-010] is at most [P-SYS-470].
Parameters:    P-AF-060, P-SYS-470, P-TM-010, P-SYS-310
TBD/TBR:       P-AF-060 value TBR (TT-070), P-SYS-470, P-TM-010, P-SYS-310 values TBR (TT-070),
  Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-820

```req
ID:            L2-AER-AF-820
Level:         L2
Type:          Interface
Statement:     At each control frame, the autoflight subsystem shall give the operational data output
  the mode state, the target of each active and armed mode in SI, and the landing gear command.
Rationale:     The mode changes are what the RVS reconstructs (L1-AER-620, L0-SUC-100) and what the
  mode-transition tests assess. The targets in SI and the gear command are the CR-C7-01 and CR-C7-02
  additions, and are what the tests need to compare a mode's behaviour with its target and the gear
  with its command (IN-C7-30). The mode state has the fixed set of values of AF_MODE_LOGIC §3 for
  every implementation (IN-C7-31). TM classifies each signal as releasable or protected with the RVS
  (#69, D44).
  Sufficiency (L1-AER-620): AF gives the armed and active modes, FCP the annunciations, TM records
  both at each output sample.
Parent(s):     L1-AER-620
Source:        L0-OBJ-140; IN-C7-30, -31
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-820; success criteria: each mode change in the mode-transition tests
  appears in the operational data at the output sample where it occurs, with the targets of the active
  and armed modes and the landing gear command of that sample.
Parameters:    —
TBD/TBR:       Releasable or protected class (#69, TT-600), Martin; CR-C7-01, CR-C7-02 to L1-AER-620,
  -630
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-830

```req
ID:            L2-AER-AF-830
Level:         L2
Type:          Interface
Statement:     When the autoflight subsystem takes a selector target from the flight control panel, it
  shall give the operational data output that target in SI with the timestamp of the control frame.
Rationale:     L1-AER-610 asks for each crew selection received and each target that results from it.
  FCP records what it took and passed (IN-C7-10); AF's child is the target AF takes (IN-C7-30), the
  same value, which lets the test compare the two ends of ICD-FCP and shows the frame at which a
  target reached the mode logic.
  Sufficiency (L1-AER-610): with TM's and FCP's children, the crew selection and the target that
  results are recorded once each.
Parent(s):     L1-AER-610
Source:        L0-OBJ-140; IN-C7-10, -30
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-830; success criteria: each scripted selection of a selector in a run
  appears in the operational data as an SI target of AF equal to the SI target of the panel, at the
  control frame that takes it.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-840

```req
ID:            L2-AER-AF-840
Level:         L2
Type:          Interface
Statement:     When the autoflight subsystem decides a mode selection, it shall give the operational
  data output the decision, accepted or refused.
Rationale:     A refused selection shows in the mode state only as no change, and a selection of the
  mode already active is also no change, so the two cannot be told apart in the operational data. The
  mode-transition tests and the reconstruction of the mode logic need the decision (C5-Q01 to Q03).
  It travels with the mode state record of L2-AER-AF-820 (IN-C5-40; a new field of S-05 proposed to
  C7).
  Sufficiency (L1-AER-610): the decision on each crew selection of mode kind is recorded.
Parent(s):     L1-AER-610
Source:        L0-OBJ-140; IN-C7-30
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-840; success criteria: in TP-AF-120, each scripted mode selection appears
  in the operational data with the decision of its row DT.
Parameters:    —
TBD/TBR:       Class of the decision field (#69), Martin
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-860

```req
ID:            L2-AER-AF-860
Level:         L2
Type:          Functional
Statement:     When the fuel state indicates fuel exhaustion, the autoflight subsystem shall make no
  mode active and no mode armed in the same control frame.
Rationale:     Derived from the owner ruling D68 (answer to #59): at exhaustion the effectors stop, the
  vehicle falls and its ground contact is a crash; what the annunciations show is C5's, with the
  suggestion of C2 that autoflight disengages (TT-580, C5-Q04). The alternatives are to keep the modes
  engaged and annunciated, which would show a guidance that no longer acts, and to freeze the last
  state. Disengagement shows the truth, FUEL EXHAUSTED comes from FCP (L2-AER-FCP-400), and the off
  value follows (L2-AER-AF-410). There is no recovery and no crew disengage selection. The state is
  reached in the frame in which the fuel state shows exhaustion, before the selections (TR-01).
  Sufficiency: DD-400 is the one decision; with L2-AER-AF-870 the post-exhaustion state is
  fully defined.
Parent(s):     Derived (DD-400)
Source:        D68; TT-580; CONOPS SC-110 leg 11
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-860; success criteria: in SC-110 at exhaustion, and in a ground start
  with no fuel, the mode state is empty with nothing armed at the control frame in which the fuel
  state shows exhaustion, the axis references take the off value, and the annunciation content has
  the empty mode state.
Parameters:    —
TBD/TBR:       Annunciations after fuel exhaustion (D68, TT-580), closed here, Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-870

```req
ID:            L2-AER-AF-870
Level:         L2
Type:          Functional
Statement:     While the fuel state indicates fuel exhaustion, the autoflight subsystem shall refuse
  each mode selection.
Rationale:     Derived with L2-AER-AF-860 (DD-400): after exhaustion nothing can fly the vehicle, so
  a mode that engaged would be annunciated without acting. It also answers the zero-fuel variation of
  SC-130: a ground start with no fuel refuses Takeoff and shows FUEL EXHAUSTED only.
  Sufficiency: with L2-AER-AF-860, the post-exhaustion state is empty and stays empty.
Parent(s):     Derived (DD-400)
Source:        D68; CONOPS SC-130 zero-fuel variation
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-870; success criteria: after exhaustion, each of the eight mode
  selections is refused and the mode state stays empty.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-900

```req
ID:            L2-AER-AF-900
Level:         L2
Type:          Interface
Statement:     When a run starts, the autoflight subsystem shall set its mode state to the initial
  mode state of the initial condition.
Rationale:     The TST sets the whole starting state of a run (L1-AER-660, I-23). The mode state is a
  data item here; the valid initial mode states are the rows IC-1 to IC-7 of AF_MODE_LOGIC §14:
  none on the ground, any mode combination or Go to hover or Hover in an airborne test start. The
  targets of the initial mode state come from the initial selector values (IN-C8-08) and the first
  navigation quantities.
  Sufficiency (L1-AER-660): with L2-AER-AF-740 and -920, the AF items of the initial condition (mode
  state, gear command, references) are taken.
Parent(s):     L1-AER-660
Source:        N-310; D69, D73
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-900; success criteria: the first output sample of a ground start and of
  each valid airborne start reports the mode state of the initial condition.
Parameters:    —
TBD/TBR:       Valid initial mode states (#60, TT-610), closed here, Martin, G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-910

```req
ID:            L2-AER-AF-910
Level:         L2
Type:          Interface
Statement:     If the initial mode state is not a valid initial mode state of AF_MODE_LOGIC, then the
  autoflight subsystem shall give the TST an initial-condition error that names the initial mode
  state.
Rationale:     The run is what the test procedure asked for (D59), so an initial mode state outside
  the valid set is rejected, as a fuel mass outside its range is (DD-140). Invalid are: any mode
  active at a ground start, Takeoff or Land at the start, and no mode active airborne with fuel
  remaining (rows IC-5 to IC-7). The run does not start.
  Sufficiency (L1-AER-660): with L2-AER-AF-900, every initial mode state is either taken or rejected.
Parent(s):     L1-AER-660
Source:        D59, D69, D73; DD-140
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-910; success criteria: each initial mode state of the rows IC-5 to IC-7
  gives an initial-condition error that names it, and the run does not start.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-AF-920

```req
ID:            L2-AER-AF-920
Level:         L2
Type:          Functional
Statement:     When autoflight first provides references with a mode active, the autoflight subsystem
  shall start its references from the navigation quantities of that control frame.
Rationale:     The first references of a run that starts airborne, and the references of Takeoff from
  the ground, start from the true state, so that no step is demanded of flight control: the
  horizontal position and velocity, the altitude, the vertical speed and the heading (the stopping
  position of L2-AER-AF-330, the level-off altitude of L2-AER-AF-350). The heading is the navigation
  heading even when its validity flag is false, because NAV gives the CV-260 yaw angle while invalid
  (IN-C6-13); nothing in the mode logic depends on the heading validity, and AF does not use the track
  (IN-C6-10).
  Sufficiency (L1-AER-660): the starting references of the AF initial mode state.
Parent(s):     L1-AER-660
Source:        D73; IN-C6-10, -13
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-AF-920; success criteria: in an airborne start in each valid mode state and
  in a takeoff, the references of the first frame with a mode active equal the navigation quantities
  of that frame, apart from the stopping position and the level-off altitude, and the first
  effector commands show no step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
