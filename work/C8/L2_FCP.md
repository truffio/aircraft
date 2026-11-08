## FCP — Flight control panel

The flight control panel requirements (task C8). The subject of each statement is the flight control panel (FCP), the eighth Aeronef subsystem (D55). It is part of the flight software and runs once per control frame `[P-SYS-310]`, first in the frame, before navigation, autoflight and flight control (DD-010, FUNCTIONAL_ANALYSIS §4.2). FCP implements function F-AER-10 (accept the crew selections), F-AER-13 (present the annunciations and indications) and its part of F-AER-14 (the initial selector values) (FUNCTIONAL_ANALYSIS §6.1). It owns the crew side of the crew interface and the conversion between crew-facing units and SI, so that only SI values cross into the rest of the Aeronef (CV-760, L1-AER-870, -880).

**The panel content (#79, D71).** The panel is data, not a device. These two lists are what L2-AER-FCP-020 and -040 close; they are the content of the panel.

| Side | Items | Unit (CV-740) | Records |
| --- | --- | --- | --- |
| Crew selections | Eight mode selections: Stationary, Heading, Altitude hold, Go to altitude, Vertical speed, Go to hover, Takeoff, Land (the engage commands of CONOPS §4.3) | — | -020, -080, -090 |
| | Four selectors, each holding one selected value: heading, horizontal speed, altitude (the target altitude), vertical speed (signed, positive when climbing) | deg, kt, ft, ft/min | -100 to -150 |
| Crew interface output | Annunciations: the mode state, the targets, the landing gear position, the fuel alert (LOW FUEL, FUEL EXHAUSTED); the readout of each selector | crew unit of each target and readout | -320 to -350, -390 to -410 |
| | Indications: altitude, vertical speed, horizontal speed, heading, track, remaining fuel | ft, ft/min, kt, deg, deg, lb | -360 to -380 |

There is no Hover selection (Hover is armed by Go to hover and by Takeoff), no autoflight disengage selection and no manual control (L0-CON-180, L1-AER-520; C8-Q04). The selector readouts are annunciations: they show the targets the crew has selected (glossary *Annunciation*, CONOPS §4.3; CR-C8-02).

**What the panel decides, and what it does not.** FCP takes each crew selection, checks each selected value against its selectable range and selection resolution, converts it to its SI target by the exact CV-750 factor, and gives the selections to autoflight (AF) through ICD-FCP. It does not decide whether a mode selection arms, becomes active or is refused: that is the mode logic of AF (C5, AF_MODE_LOGIC), and FCP passes each mode selection on whatever the mode state. On the output side, AF decides the annunciation content (which modes, which targets, the gear position), navigation (NAV) gives the indicated quantities with their validity, and the FU subsystem gives the fuel state; FCP converts them to crew-facing units, rounds them to their display resolution (CV-780) and outputs them at each output sample. The mode labels are AF's (L1-AER-470: the labels are C5's); the fuel alert labels and the gear-position labels are FCP's (IN-C2-43; C8-Q03).

**The horizontal speed selector is a ground speed** (D72 Q1). Its target is a horizontal speed (CV-480), measured over the ground, which Heading flies; it is not an airspeed, and nothing on the panel calls it one (CV-960).

**No device, no format.** L1-AER-510 (no physical control device, no display format) and L1-AER-520 (no direct manual flight control) are leaves at L1, checked directly over the branch; they have no FCP child. The records here state data items, their units, resolutions and rounding, which L1-AER-510 and CV-780 place outside the display format. No record states a layout, a symbol, a colour or a screen. Nothing here is operator-facing text.

**Verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would be the implementation of the panel software (D4), so each record is verified directly by its own method, and the L1 parents by roll-up (D40, D58). Procedure IDs follow the record number (IN-, AN-, TP-, DM-FCP-nnn); Phase 5 (V3) writes the procedures. Most tests drive the panel through the crew interface with a selection script and read the crew interface output and the operational data. The tests of the output mapping (-210, -220, -320 to -410) can also run the panel alone, with a test source of annunciation content, navigation quantities and fuel state at the ICD-FCP boundary (IN-C8-40), as EF does with a test command source (IN-C3-33).

**Coverage of the L1 parents.** Every L1 record allocated to FCP (18, FUNCTIONAL_ANALYSIS §6.2) has at least one FCP child. L1-AER-310, -320 and -330 (the envelope) are allocated to FCP since CR-C8-01 (D76): their rationales make the panel the place where the selectable range ends, and the selector records trace to them.

| L1 parent | What FCP guarantees, in the parent's terms | FCP children |
| --- | --- | --- |
| L1-AER-310 | The selectable horizontal speed runs from zero to [P-SYS-230], and the selectable altitude up to [P-SYS-200] | -110, -120 |
| L1-AER-320 | The selectable climb vertical speed runs up to [P-SYS-240] | -130 |
| L1-AER-330 | The selectable descent vertical speed runs down to minus [P-SYS-250], and the selectable altitude down to the altitude at which the height above the ground is [P-SYS-210] at level attitude | -120, -130 |
| L1-AER-430 | FCP exchanges with the vehicle model only the fuel state, by its boundary definition | -070 |
| L1-AER-470 | A change of mode state, target or gear position that AF gives, and a change of a selected value, reaches the crew interface output within the FCP share [P-TM-010]; the mode state, targets, gear position and selector readouts are annunciated | -040, -300, -310, -320, -330, -340, -350 |
| L1-AER-480 | Each crew selection is a time-stamped data item of the crew interface, from a closed list, taken at the next control frame, checked and held | -010, -020, -080, -090, -100 to -150 |
| L1-AER-490 | The annunciations, readouts and indications are crew-interface data items, from a closed list, at each output sample, with their validity | -030, -040, -300, -320, -350, -360, -370 |
| L1-AER-500 | Each selected value, readout, annunciated target and indication is in its CV-740 unit | -100 to -130, -210, -220, -230, -350, -380 |
| L1-AER-560 | The remaining fuel mass is indicated in lb at each output sample | -380 |
| L1-AER-570 | LOW FUEL is annunciated while the fuel state indicates low fuel, within the FCP share of [P-SYS-470] | -310, -390, -410 |
| L1-AER-580 | FUEL EXHAUSTED is annunciated while the fuel state indicates fuel exhaustion, within the FCP share of [P-SYS-470] | -310, -400, -410 |
| L1-AER-610 | Each crew selection taken, accepted or not, goes to the operational data with its timestamp, its selected value and its target | -500 |
| L1-AER-620 | The annunciations presented go to the operational data at each output sample | -510 |
| L1-AER-660 | The initial selected values of the initial condition set the selectors; an invalid one is an initial-condition error | -520, -530 |
| L1-AER-680 | The selections are taken once per control frame and given to AF in that frame | -080 |
| L1-AER-690 | The panel outputs depend only on the run's selections, initial values and inputs, in a defined order | -090, -150, -540 |
| L1-AER-870 | Selected values convert to SI by the exact CV-750 factor without rounding; shown values convert from SI by the same factor, then round once | -200, -210, -220 |
| L1-AER-880 | FCP gives AF only the crew selections in SI, and takes only the annunciation content, the navigation quantities and the fuel state | -050, -060 |

No record is Derived. The design choices inside the records (the intake order of one frame, the rejection of an invalid selected value, the rounding rule, the single fuel alert, the initial selected values in crew units) are DD-520 to DD-560 of the register.

### L2-AER-FCP-010

```req
ID:            L2-AER-FCP-010
Level:         L2
Type:          Interface
Statement:     The flight control panel shall take each crew selection from the crew interface
  defined in ICD-AER-TST, as one time-stamped crew-selection data item.
Rationale:     The crew interface is data, with no model of physical controls (L0-CON-170,
  L1-AER-510). A human through the TST, a test procedure and an RVS agent use the same data item
  (L0-ASM-120, N-320, N-400, SC-230), so a scripted selection at a given time is handled exactly
  as an interactive one. The timestamp is the CV-840 step index with its simulation time; it
  places the selection in a control frame (L2-AER-FCP-080). The panel is the only crew input
  (L1-AER-520, D55): no other path takes a crew selection into the Aeronef.
  Sufficiency (L1-AER-480): this record takes each crew selection as a time-stamped data item of
  the crew interface; L2-AER-FCP-020 closes the list of selections; -080 and -090 take them at the
  next control frame, in a defined order, and give them to autoflight; -100 to -150 check and hold
  the selected values. Together they accept each crew selection of a mode or a target as
  L1-AER-480 requires, and a scripted selection behaves as an interactive one because both arrive
  as this same item.
Parent(s):     L1-AER-480
Source:        N-300, N-320, N-360, N-400; L0-ASM-120; CONOPS §4.3, SC-230
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-010; success criteria: a run driven by a selection script, and the same
  run with the same selections entered through the TST interactive interface at the same
  simulation times, give identical crew-selection records in the operational data (timestamp,
  item, selected value, acceptance, target) and the same verdict on each success criterion of
  SC-050 (D59).
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-020

```req
ID:            L2-AER-FCP-020
Level:         L2
Type:          Interface
Statement:     The flight control panel shall accept as crew selections only a mode selection of
  Stationary, Heading, Altitude hold, Go to altitude, Vertical speed, Go to hover, Takeoff or Land,
  and a selected value of the heading, horizontal speed, altitude or vertical speed selector.
Rationale:     The panel content set by the owner (D71, answers #79): a button that engages each
  mode, Takeoff and Land included (D69), and the readouts of the values the crew sets, horizontal
  speed, vertical speed, target altitude and the heading for Heading (D56). CONOPS §4.3 (CR-B3-32,
  D73) lists eight engage commands; Hover has none, because Go to hover and Takeoff arm it and it
  engages when the vehicle is stationary at the hover height (D56, D69; C8-Q04). There is no
  autoflight disengage selection and no manual control (L0-CON-180, D49). The altitude selector
  is the target altitude selector of D56; its selected value is the selected altitude. The
  provisional engage labels of CONOPS §4.3 (STAT, HDG, ALT, GO ALT, V/S, GO HOVER, TAKEOFF, LAND)
  name the items in ICD-AER-TST. The list is closed: it is the input side of the panel content
  (#79). A data item that names no listed selection is refused by the crew interface (IN-C8-31).
  Sufficiency (L1-AER-480): see L2-AER-FCP-010; this record fixes which selections exist.
Parent(s):     L1-AER-480
Source:        D56, D69, D71; #79; CONOPS §4.3, §4.4
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-020; success criteria: ICD-AER-TST defines exactly twelve
  crew-selection items, the eight mode selections and the four selected values listed, and the
  FCP implementation defines no other crew-selection item.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-030

```req
ID:            L2-AER-FCP-030
Level:         L2
Type:          Interface
Statement:     The flight control panel shall output its annunciations, selector readouts and
  indications at each output sample as the crew-interface data items defined in ICD-AER-TST.
Rationale:     The crew receives annunciations and indications as data (L0-CON-170). The output
  sample period is [P-TM-010] (L1-AER-600), the same clock as the operational data, so what the
  crew sees and what the operational data record line up in time (N-390). Each data item carries
  its crew-facing unit in its ICD definition (CV-760 group 2) and, for an indication, its
  validity (L2-AER-FCP-370). The crew interface output goes to the TST, which shows it to a human
  or hands it to a test procedure (FUNCTIONAL_ANALYSIS I-42); how a human sees it is the TST's,
  not a display format of the Aeronef (L1-AER-510).
  Sufficiency (L1-AER-490): this record outputs the annunciations and indications as ICD-AER-TST
  data items at each output sample; -040 closes the list; -300 forms each sample from the latest
  control frame; -320, -350 and -360 to -380 give each item its content, and -370 its validity.
  Together they are the whole of L1-AER-490.
Parent(s):     L1-AER-490
Source:        N-060, N-340, N-380; CONOPS §4.3
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-030; success criteria: each output sample of the reference mission
  (SC-110) holds each crew-interface output data item of ICD-AER-TST, with its unit as defined
  there, and the samples are spaced by [P-TM-010].
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-040

```req
ID:            L2-AER-FCP-040
Level:         L2
Type:          Interface
Statement:     The flight control panel shall give in its crew interface output only the mode state,
  target, landing gear position and fuel alert annunciations, the readout of each selector and the
  altitude, vertical speed, horizontal speed, heading, track and remaining fuel indications.
Rationale:     The output side of the panel content (#79, D71). The annunciations show the autoflight
  state and the alerts: the armed and active modes and whether autoflight is engaged (the mode
  state), the targets in use, the gear position (L1-AER-470 v2) and the fuel alert (L1-AER-570,
  -580). The selector readouts are the values the crew has set (D71); they are annunciations of
  the selected targets (CONOPS §4.3; CR-C8-02). The indications are the closed list of the
  glossary (*Indication*; CONOPS §4.3; L1-AER-490). There is no flight path angle and no VOR
  quantity (D56); the height above the ground is a guidance quantity of autoflight, not an
  indication. The list is closed so that the panel content is fixed in one place.
  Sufficiency (L1-AER-490): see L2-AER-FCP-030; this record fixes which items exist.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310; this record makes the mode state, the targets and
  the gear position items of the output.
Parent(s):     L1-AER-490, L1-AER-470
Source:        D55, D56, D69, D71; #79; CONOPS §4.3; N-060, N-150
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-040; success criteria: ICD-AER-TST defines the crew interface
  output as exactly these items (four annunciation items, four selector readouts, six
  indications), each with its unit, and the FCP implementation outputs no other crew-interface
  item.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-050

```req
ID:            L2-AER-FCP-050
Level:         L2
Type:          Interface
Statement:     The flight control panel shall give autoflight, through ICD-FCP, only the mode
  selections it takes, the target of each selector in SI and the selectors whose selected value it
  accepts at that control frame.
Rationale:     The panel → autoflight half of the panel boundary (L1-AER-880, FUNCTIONAL_ANALYSIS
  I-19). Only SI values cross: the crew-facing units stay in the panel (CV-760). AF receives the
  current target of each of the four selectors at each control frame, so it always has the value
  to fly, and it learns which selectors the crew set in this frame, which it needs to tell a new
  selection from an unchanged one (for example a new selected vertical speed during Go to
  altitude, N-090, SC-020). The mode selections are given in order (L2-AER-FCP-090), with no
  judgement of the mode state: arming, activation and refusal are AF's (C5). The selected heading
  arrives as a direction angle in [0, 2π) rad, the selected horizontal speed as a horizontal speed
  in m/s, the selected altitude as an altitude in m and the selected vertical speed as a signed
  vertical speed in m/s (CV-430, CV-480, CV-490, CV-530).
  Sufficiency (L1-AER-880): this record is the panel's output across ICD-FCP and -060 its inputs;
  each is closed, so the panel exchanges with its neighbours only the listed kinds of L1-AER-880.
Parent(s):     L1-AER-880
Source:        D55; FUNCTIONAL_ANALYSIS §3.2 I-19, §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-050; success criteria: ICD-FCP defines the panel → autoflight
  data as the ordered mode selections of a control frame, the SI target of each of the four
  selectors and the set of selectors accepted in the frame, each with its SI unit, and the FCP
  implementation gives autoflight nothing else.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-060

```req
ID:            L2-AER-FCP-060
Level:         L2
Type:          Interface
Statement:     The flight control panel shall take, through ICD-FCP, only the annunciation content
  from autoflight, the navigation quantities with their validity from navigation and the fuel state
  from the FU subsystem.
Rationale:     The inputs of the panel boundary (L1-AER-880; FUNCTIONAL_ANALYSIS I-06, I-16, I-18).
  Autoflight gives the annunciation content: the mode state, the targets in use and the landing
  gear position, which AF takes from the gear state (L1-AER-470 v2). Navigation gives the
  altitude, vertical speed, horizontal speed, heading and track with their validity, the same
  values it gives autoflight (L1-AER-890), so the crew and the modes see one definition of each
  quantity (FUNCTIONAL_ANALYSIS §5.2). The FU subsystem gives the fuel state: the remaining fuel
  mass, the low-fuel indication and the fuel-exhaustion indication (L2-AER-FU-240). Each input is
  in SI. The panel reads each input once per control frame, at the frame start.
  Sufficiency (L1-AER-880): see L2-AER-FCP-050.
Parent(s):     L1-AER-880
Source:        D55; FUNCTIONAL_ANALYSIS §3.2 I-06, I-16, I-18, §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-060; success criteria: ICD-FCP defines the inputs of the panel as
  the annunciation content (mode state, targets, gear position), the five indicated navigation
  quantities with their validity and the fuel state (by reference to its vehicle-model boundary
  definition), each in SI, and the FCP implementation reads no other input during a run.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-070

```req
ID:            L2-AER-FCP-070
Level:         L2
Type:          Interface
Statement:     The flight control panel shall exchange with the vehicle model only the fuel state,
  taken as the vehicle-model boundary ICD defines it.
Rationale:     The vehicle-model boundary carries effector commands and the landing gear command in,
  and vehicle state, gear state, mass properties and fuel state out (L1-AER-430). Of these the
  panel uses the fuel state only, which ICD-FCP takes by reference to its boundary definition
  (L1-AER-880 rationale, L2-AER-FU-240). The panel gives the vehicle model nothing. The gear
  position reaches the panel through autoflight, as annunciation content, not from the gear
  state directly (L1-AER-470 v2), and the indicated quantities come from navigation, not from the
  vehicle state. Keeping the panel off the rest of the boundary keeps it replaceable with the
  flight software (L0-CON-210).
  Sufficiency (L1-AER-430): the fuel state is one of the listed kinds and is defined in the
  boundary ICD; no other panel data item crosses the boundary, which is the FCP share of
  L1-AER-430.
Parent(s):     L1-AER-430
Source:        D55; FUNCTIONAL_ANALYSIS §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-070; success criteria: the only FCP data item that crosses the
  vehicle-model boundary is the fuel state, read by its boundary ICD definition; no FCP
  requirement or implementation item reads the vehicle state, the gear state or the mass
  properties, or writes to the vehicle model.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-080

```req
ID:            L2-AER-FCP-080
Level:         L2
Type:          Functional
Statement:     At each control frame, the flight control panel shall take each crew selection whose
  timestamp is later than the start of the previous control frame and at or before the start of
  this control frame, and give it to autoflight in this control frame.
Rationale:     The flight software runs once per control frame, in the order FCP → NAV → AF → FC
  (DD-010, L1-AER-680); the panel takes the selections at step 2 of the frame (FUNCTIONAL_ANALYSIS
  §4.2), so a selection reaches autoflight in the frame that takes it. A selection timestamped
  inside a frame waits at most one control frame [P-SYS-310], which is in the annunciation budget
  (FUNCTIONAL_ANALYSIS §7.5). The first control frame starts at step zero and has no previous
  frame, so it takes each selection timestamped at step zero. Whether an input timestamped k first
  affects step k or step k + 1 is fixed in ICD-AER-TST (CV-840); this record follows the frame
  sequence of FUNCTIONAL_ANALYSIS §4.2. Mode selections are given whatever the mode state; whether
  a mode arms, becomes active or is refused is the mode logic of AF (C5). A selection made on the
  ground or during a Takeoff or a Land is taken the same way.
  Sufficiency (L1-AER-680): the panel's crew-selection function executes at each control frame and
  at no other time; with DD-010 it runs in the frame, before autoflight, which is the FCP share
  of L1-AER-680.
  Sufficiency (L1-AER-480): see L2-AER-FCP-010.
Parent(s):     L1-AER-680, L1-AER-480
Source:        FUNCTIONAL_ANALYSIS §4.2; CV-830, CV-840; DD-010
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-080; success criteria: with selections scripted at a frame-start step,
  at a step inside a control frame and at the step that follows a frame start, the ICD-FCP data
  of the control frames (IN-C8-40) show each selection given to autoflight at the first control
  frame whose start is at or later than its timestamp, and at no other frame; a mode selection
  that autoflight refuses (Land with Hover not active) is still given to autoflight.
Parameters:    P-SYS-310
TBD/TBR:       P-SYS-310 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-090

```req
ID:            L2-AER-FCP-090
Level:         L2
Type:          Functional
Statement:     When the flight control panel takes more than one crew selection at a control frame,
  the flight control panel shall give autoflight the mode selections in the order of their
  timestamps, and of their receipt for equal timestamps, with the selector targets that result
  from each selected value it accepts at that control frame.
Rationale:     Several selections can fall in one frame: a script sets a target and engages a mode
  at the same time (SC-060 step 1, SC-110 leg 2), or a human makes two quick selections. The
  order must be defined so that a repeated run gives the same result (L1-AER-690). The mode
  selections keep their order, so that two mode selections in one frame reach the mode logic as
  the crew made them. The selector targets given with them are those after each selected value of
  the frame has been checked and applied, so that a mode engaged in the same frame as its target
  uses the new target, whatever the order of the two in the frame. A frame lasts [P-SYS-310], so
  the crew cannot tell the two orders apart. Two selected values of one selector in one frame:
  the last one accepted holds. This is design decision DD-520, inside this record.
  Sufficiency (L1-AER-690): with -150 and -540, this record makes the panel output a function of
  the selections and their order only, which is the FCP share of L1-AER-690.
  Sufficiency (L1-AER-480): see L2-AER-FCP-010.
Parent(s):     L1-AER-690, L1-AER-480
Source:        N-330; CONOPS SC-060, SC-110; DD-520
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-090; success criteria: with two mode selections, and with a selected
  value and a mode selection, scripted in one control frame in each order and with equal
  timestamps, the ICD-FCP data of that frame (IN-C8-40) give the mode selections in script order
  and the targets of the selected values of the frame; with two selected values of one selector
  in one frame, the target is that of the later one.
Parameters:    P-SYS-310
TBD/TBR:       P-SYS-310 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-100

```req
ID:            L2-AER-FCP-100
Level:         L2
Type:          Functional
Statement:     The flight control panel shall accept a selected heading, in degrees, that is a
  multiple of [P-AF-040] within the direction-angle range of CV-520.
Rationale:     The heading selector of Heading mode (D56, D71). The selected heading is a heading,
  the direction in which the nose points (CV-530), not a track. The direction-angle range of
  CV-520 is from zero, north, up to but not including a full turn, so 360° is not a selectable
  value and north is selected as zero (C8-Q02); every heading has exactly one selected value. The
  selection resolution [P-AF-040] is 1° (D71, TBR). A value the selector does not accept is
  handled by L2-AER-FCP-140. The unit is the CV-740 crew-facing unit for heading (CV-760 group 1).
  Sufficiency (L1-AER-480): see L2-AER-FCP-010. Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-480, L1-AER-500
Source:        D56, D71; CONOPS §4.3, SC-060, SC-120; CV-520, CV-530, CV-740
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-100; success criteria: selected headings of zero, of [P-AF-040], of 180°
  and of the largest multiple of [P-AF-040] below a full turn are accepted (the selector readout
  shows them); 360°, a negative value and a value that is not a multiple of [P-AF-040] are not
  accepted (the readout keeps the previous value).
Parameters:    P-AF-040
TBD/TBR:       P-AF-040 value TBR (TT-170), Martin, G2 (C8)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-110

```req
ID:            L2-AER-FCP-110
Level:         L2
Type:          Functional
Statement:     The flight control panel shall accept a selected horizontal speed, in knots, that is
  a non-negative multiple of [P-AF-030] whose exact CV-750 conversion is at most [P-SYS-230].
Rationale:     The horizontal speed selector of Heading mode, from zero to the vehicle's maximum
  (D56). Zero is selectable: with no horizontal speed, a heading change turns the vehicle in
  place (SC-120). The selected horizontal speed is a ground speed: its target is a horizontal
  speed (CV-480), over the ground, and [P-SYS-230] is a ground speed (D72 Q1); with wind the
  airspeed differs. [P-SYS-230] is the top of the selectable horizontal speed (L1-AER-310
  rationale). The range check uses the exact conversion of the selected value (in rational
  arithmetic, or against the limit converted to crew units), not its floating-point target, so a
  limit that is an exact crew value is selectable whatever the order of the operations (the same
  rule in -120 and -130). [P-SYS-230] is 300 kt (D66); for 300 kt to be accepted, the database
  value of [P-SYS-230] must be at least the exact conversion of 300 kt, which its present
  three-decimal value (299.9994 kt) is not (C8-Q07, D76). The resolution
  [P-AF-030] is 1 kt (D71, TBR).
  Sufficiency (L1-AER-310): the vehicle can sustain each horizontal speed up to [P-SYS-230] under
  autoflight only if the crew can select it; this record and -120 (the altitude range of the
  operating volume) give the panel side, and AF, FC and EF fly it.
  Sufficiency (L1-AER-480): see L2-AER-FCP-010. Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-480, L1-AER-500, L1-AER-310
Source:        D56, D66, D71, D72; CONOPS §4.3, SC-060, SC-120; CV-480
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-110; success criteria: selected horizontal speeds of zero, of
  [P-AF-030] and of the largest multiple of [P-AF-030] whose exact CV-750 conversion is at most
  [P-SYS-230] (300 kt with the proposed database value) are accepted; the next multiple, a negative
  value and a value that is not a multiple of [P-AF-030] are not accepted.
Parameters:    P-AF-030, P-SYS-230
TBD/TBR:       P-AF-030 value TBR (TT-170), Martin, G2 (C8)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-120

```req
ID:            L2-AER-FCP-120
Level:         L2
Type:          Functional
Statement:     The flight control panel shall accept a selected altitude, in feet, that is a
  multiple of [P-AF-010] whose exact CV-750 conversion is at least [P-SYS-210] plus half of
  [P-DYN-030] and at most [P-SYS-200].
Rationale:     The target altitude selector of Go to altitude and Vertical speed (D56). The target
  is an altitude, of the centre of gravity (CV-430). The lower bound is the altitude at which the
  height above the ground is the minimum operating height [P-SYS-210] at level attitude (CV-400;
  L1-AER-330 v2; the P-SYS-210 description); pitch and roll are held at zero (D57), so the level
  geometry applies. With the present values it is 3.524 m (11.56 ft), so the lowest selectable
  value is 20 ft. That answers the B3 impact-list question for C8: the bound needs no rounding and
  no parameter of its own, because the rule picks the lowest multiple of [P-AF-010] at or above it,
  and it follows a change of [P-SYS-210] or [P-DYN-030]. The upper bound is the maximum operating
  altitude [P-SYS-200] (150 000 ft, a multiple of [P-AF-010]). The check uses the exact
  conversion, as in -110. The resolution [P-AF-010] is 10 ft (D71, TBR).
  Sufficiency (L1-AER-330): a descent levels off at the selected altitude (D56); this record bounds
  the selectable altitude below at the minimum operating height, as the L1-AER-330 rationale
  assigns to C8.
  Sufficiency (L1-AER-310): this record bounds the selectable altitude above at the top of the
  operating volume, so a selected altitude is inside the volume in which L1-AER-310 applies.
  Sufficiency (L1-AER-480): see L2-AER-FCP-010. Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-480, L1-AER-500, L1-AER-330, L1-AER-310
Source:        D56, D67, D70, D71; CONOPS §4.2, §4.3, SC-020; CV-400, CV-430; B3 impact list (C8)
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-120; success criteria: the lowest multiple of [P-AF-010] whose exact CV-750
  conversion is at least [P-SYS-210] plus half of [P-DYN-030] (20 ft with the present values) and
  the multiple equal to [P-SYS-200] (150 000 ft) are accepted, and a mid value is accepted; the
  multiple below the lower one, the multiple above [P-SYS-200] and a value that is not a multiple
  of [P-AF-010] are not accepted.
Parameters:    P-AF-010, P-SYS-210, P-DYN-030, P-SYS-200
TBD/TBR:       P-AF-010 value TBR (TT-170), Martin, G2 (C8); P-SYS-200, P-SYS-210 values TBR
  (TT-010), Martin, G2 (I1); P-DYN-030 value TBR (TT-740), Martin, 2026-11-30
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-130

```req
ID:            L2-AER-FCP-130
Level:         L2
Type:          Functional
Statement:     The flight control panel shall accept a selected vertical speed, in feet per minute
  and positive when climbing, that is a multiple of [P-AF-020] whose exact CV-750 conversion is at
  least minus [P-SYS-250] and at most [P-SYS-240].
Rationale:     The vertical speed selector of Vertical speed mode, and of Go to altitude, where it
  replaces the standard vertical speed [P-AF-220] (D56, D70; CONOPS §4.3). The selected value is
  signed as the vertical speed (CV-490): a climb is positive, a descent negative. [P-SYS-240] is
  the top of the selectable climb vertical speed (L1-AER-320 rationale) and [P-SYS-250] the
  largest selectable descent magnitude, both 6000 ft/min (D67). The check uses the exact
  conversion, as in -110: in floating point, 6000 × 0.3048 / 60 exceeds 30.48 by one rounding
  step, and a limit check on that target would refuse the maximum. Zero is a multiple of [P-AF-020]
  and is selectable; what Vertical speed does with a zero or a wrong-signed selected vertical
  speed is AF's (C5, SC-040 TBR; C8-Q08). The standard vertical speed is not a selected value: AF
  uses it until the crew selects another (D56), and AF knows when that happens from the selectors
  accepted in each frame (L2-AER-FCP-050). The resolution [P-AF-020] is 100 ft/min (D71, TBR).
  Sufficiency (L1-AER-320): the vehicle can climb at each vertical speed up to [P-SYS-240] under
  autoflight only if the crew can select it; this record gives the panel side.
  Sufficiency (L1-AER-330): likewise for the descent down to minus [P-SYS-250]; with -120 (the
  lowest selectable altitude) it is the FCP share of L1-AER-330.
  Sufficiency (L1-AER-480): see L2-AER-FCP-010. Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-480, L1-AER-500, L1-AER-320, L1-AER-330
Source:        D56, D67, D70, D71; CONOPS §4.3, SC-020, SC-040; CV-490
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-130; success criteria: selected vertical speeds of minus the multiple
  of [P-AF-020] equal to [P-SYS-250], of zero, of [P-AF-020] and of the multiple equal to
  [P-SYS-240] are accepted; the multiples beyond each end and a value that is not a multiple of
  [P-AF-020] are not accepted.
Parameters:    P-AF-020, P-SYS-240, P-SYS-250, P-AF-220
TBD/TBR:       P-AF-020 value TBR (TT-170), Martin, G2 (C8); P-SYS-240, P-SYS-250 values TBR
  (TT-010), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-140

```req
ID:            L2-AER-FCP-140
Level:         L2
Type:          Functional
Statement:     If the flight control panel takes a selected value that its selector does not accept,
  then the flight control panel shall keep the previous selected value of that selector.
Rationale:     A selected value outside its selectable range or not a multiple of its selection
  resolution (L2-AER-FCP-100 to -130) is refused, not clamped to the range and not rounded to the
  resolution. Rounding would change the value before conversion, which CV-770 and L1-AER-870
  exclude; clamping would hide an error in a selection script, and the run would no longer be what
  the test procedure asked for (D59; the same choice as DD-140 for the initial fuel). The refusal
  is visible: the selector readout keeps its value, autoflight is not told of a new selection
  (L2-AER-FCP-050), and the operational data record the selection as not accepted
  (L2-AER-FCP-500). This is design decision DD-530 (C8-Q01).
  Sufficiency (L1-AER-480): see L2-AER-FCP-010; this record defines the outcome of a selection the
  panel does not accept.
Parent(s):     L1-AER-480
Source:        CV-770; D59; DD-140; DD-530
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-140; success criteria: for each selector, a selected value above its
  range, below its range and off its resolution, each scripted after an accepted value, leaves the
  selector readout and the target given to autoflight at the accepted value, and the operational
  data record each refused selection as not accepted.
Parameters:    —
TBD/TBR:       Refusal rather than clamping or rounding (C8-Q01, DD-530), Martin, G2
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-150

```req
ID:            L2-AER-FCP-150
Level:         L2
Type:          Functional
Statement:     The flight control panel shall change the selected value of a selector only when it
  accepts a selected value of that selector.
Rationale:     A selected value stays until the crew changes it (N-090: the crew changes a target
  and sees the vehicle go to it). Autoflight has no data path into the selectors: across ICD-FCP
  it gives the panel annunciation content only (L1-AER-880), so no mode change resets or
  synchronises a selector. A target that autoflight sets for itself, for example the altitude
  that Altitude hold holds when engaged directly (SC-050 step 5), the reference position of
  Stationary or the standard vertical speed of Go to altitude, is AF's, and the panel annunciates
  it as a target (L2-AER-FCP-330), not as a selected value. The selected value is held in its
  crew-facing unit, as selected, so its readout and its target never pass through a round trip
  of conversions (L2-AER-FCP-200, -350).
  Sufficiency (L1-AER-690): see L2-AER-FCP-090. Sufficiency (L1-AER-480): see L2-AER-FCP-010.
Parent(s):     L1-AER-480, L1-AER-690
Source:        N-090; CONOPS §4.4 (targets); D55
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-150; success criteria: in the reference mission (SC-110), the readout
  and the SI target of each selector change only at the control frames that accept a selection of
  that selector, and are unchanged across each mode change, capture, takeoff, landing and the
  fuel exhaustion.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-200

```req
ID:            L2-AER-FCP-200
Level:         L2
Type:          Functional
Statement:     When the flight control panel accepts a selected value, the flight control panel
  shall set its target to the selected value multiplied by the exact CV-750 factor of its
  crew-facing unit, without rounding.
Rationale:     CV-770: a selected value becomes its SI target by multiplication by the exact factor,
  with no intermediate rounding (L1-AER-870). The factors are 0.3048 m per ft, 0.3048/60 m/s per
  ft/min, 1852/3600 m/s per kt (used as the fraction, CV-750) and π/180 rad per degree. A selected
  heading in the CV-520 range gives a target in [0, 2π) without wrapping, and the sign of a
  selected vertical speed is kept. "Without rounding" excludes any rounding of the value to a
  resolution or to fewer digits; the floating-point representation of the product is the only
  difference allowed, bounded in the test by the relative tolerance [P-FCP-020]. The target is
  computed once, at acceptance, from the selected value held in its crew unit (L2-AER-FCP-150).
  Sufficiency (L1-AER-870): this record converts each crew selection to SI by the exact factor
  without rounding; -210 and -220 convert each shown quantity from SI by the same factor with one
  rounding at the end, so together they are the whole of L1-AER-870.
Parent(s):     L1-AER-870
Source:        N-070; D7, D34; CV-750, CV-770
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-200; success criteria: for each selector and for selected values at
  both ends of its range and at three values inside it, the SI target that the panel gives
  autoflight equals the selected value times the CV-750 factor, computed independently, within the
  relative tolerance [P-FCP-020].
Parameters:    P-FCP-020
TBD/TBR:       P-FCP-020 value TBR (TT-960), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-210

```req
ID:            L2-AER-FCP-210
Level:         L2
Type:          Functional
Statement:     The flight control panel shall compute the shown value of each annunciated target and
  each indication by dividing its SI value by the exact CV-750 factor of its crew-facing unit and
  rounding the result half away from zero to the nearest multiple of its display resolution.
Rationale:     The display resolution and the rounding rule are FCP requirement matters (CV-780).
  The display resolutions are [P-TM-020] for altitude (1 ft), [P-TM-030] for vertical speed
  (10 ft/min), [P-TM-040] for horizontal speed (1 kt), [P-TM-050] for heading and track (1°), all
  D71, TBR, and [P-FCP-010] for the remaining fuel (1 lb, proposed). The conversion uses the
  inverse of the CV-750 factor with no intermediate rounding (CV-750, L1-AER-870), and then one
  rounding, half away from zero, which is symmetric for a signed vertical speed. A target that the
  crew selected converts back to its selected value up to floating-point error, which the rounding
  removes, because each selection resolution is a multiple of the display resolution of its
  quantity. The selector readouts are not converted (L2-AER-FCP-350). A remaining fuel mass below
  half of [P-FCP-010] shows as zero before fuel exhaustion; the fuel alert, not the shown value,
  marks the exhaustion (L2-AER-FCP-400). This is design decision DD-540 (C8-Q06).
  Sufficiency (L1-AER-870): see L2-AER-FCP-200.
  Sufficiency (L1-AER-500): see L2-AER-FCP-230; this record gives each shown value in its CV-740
  unit.
Parent(s):     L1-AER-870, L1-AER-500
Source:        N-070; D7, D9, D71; CV-750, CV-780; #55; DD-540
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-210; success criteria: with a test source at ICD-FCP (IN-C8-40), for SI
  values of each quantity at a multiple of its display resolution, just below and just above half
  a resolution step from it, and at negative vertical speeds, the shown value equals the
  independently computed quotient rounded half away from zero to the display resolution.
Parameters:    P-TM-020, P-TM-030, P-TM-040, P-TM-050, P-FCP-010
TBD/TBR:       P-TM-020 to P-TM-050 values TBR (TT-210), Martin, G2 (C8); P-FCP-010 value TBR
  (TT-960), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-220

```req
ID:            L2-AER-FCP-220
Level:         L2
Type:          Functional
Statement:     The flight control panel shall show each heading and each track in the
  direction-angle range of CV-520, with a value that rounds to a full turn shown as zero.
Rationale:     A heading or track just below a full turn (for example 359.6°) rounds to a full turn
  under L2-AER-FCP-210; north is shown as zero, so the shown value stays in the CV-520 range,
  matches the selectable heading range (L2-AER-FCP-100) and each direction has one shown value.
  CV-520 leaves the crew-facing value of north to a display requirement; this is that requirement
  (C8-Q02). How the number is laid out ("0" or "000") is a display format, outside the Aeronef
  (L1-AER-510). Annunciated heading targets follow the same rule.
  Sufficiency (L1-AER-870): see L2-AER-FCP-200.
  Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-870, L1-AER-500
Source:        CV-520, CV-920; DD-540
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-220; success criteria: with a test source at ICD-FCP (IN-C8-40),
  headings and tracks of zero, of just below a full turn by less than half of [P-TM-050], of just
  below by more than half of [P-TM-050] and of half a turn are shown as zero, zero, the largest
  multiple of [P-TM-050] below a full turn and 180°.
Parameters:    P-TM-050
TBD/TBR:       P-TM-050 value TBR (TT-210), Martin, G2 (C8)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-230

```req
ID:            L2-AER-FCP-230
Level:         L2
Type:          Constraint
Statement:     The flight control panel shall state each selected value, selector readout,
  annunciated target and indication in the crew-facing unit that CV-740 assigns to its quantity.
Rationale:     North American aviation units for everything the crew selects or sees (D7, D9, D34;
  L0-CON-270): altitude in ft, vertical speed in ft/min, horizontal speed in kt, heading and track
  in degrees, fuel in lb. A selected value and its readout are in the unit of the quantity of
  their selector; an annunciated target is in the unit of the quantity it applies to. CV-760 lets
  crew-facing units appear only in crew-selection and crew-presentation requirements (groups 1
  and 2): these FCP records are those, and every other FCP quantity, at ICD-FCP and in the
  vehicle-model boundary, is in SI (L2-AER-FCP-050, -060). The selection and display resolution
  parameters are stored in their crew units (CV-790).
  Sufficiency (L1-AER-500): this record names the CV-740 unit of every crew-facing item;
  L2-AER-FCP-100 to -130 name it for each selector, -210 and -220 compute each shown value in it,
  -350 shows each readout in it and -380 the fuel in pounds. Together each crew selection and
  each annunciated or indicated quantity is in its CV-740 unit.
Parent(s):     L1-AER-500
Source:        N-070; D7, D9, D34; CV-740, CV-760, CV-790
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-FCP-230; success criteria: each crew-selection item and each
  crew-interface output item in ICD-AER-TST, and each FCP requirement on a crew selection or a
  crew-facing output, names the CV-740 unit of its quantity; no FCP item at ICD-FCP or at the
  vehicle-model boundary is in a crew-facing unit.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-300

```req
ID:            L2-AER-FCP-300
Level:         L2
Type:          Functional
Statement:     At each output sample, the flight control panel shall form its crew interface output
  from the inputs it took and the selected values it held at the latest control frame that starts
  at or before that output sample.
Rationale:     The panel reads its inputs once per control frame (L2-AER-FCP-060) and outputs at
  each output sample [P-TM-010] (L1-AER-490). This record ties the two: a sample shows the
  frame's data, never a mix of two frames, so the annunciations, readouts and indications of a
  sample agree with each other and with the operational data of that sample. [P-TM-010] is
  proposed equal to [P-SYS-310] (FUNCTIONAL_ANALYSIS §7.5), so each frame is shown once; if it is
  a multiple, the samples skip frames, and the latency stays within [P-TM-010] (L2-AER-FCP-310).
  Sufficiency (L1-AER-490): see L2-AER-FCP-030.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310.
Parent(s):     L1-AER-490, L1-AER-470
Source:        FUNCTIONAL_ANALYSIS §4.2, §7.5; CV-830
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-300; success criteria: in the reference mission (SC-110), each output
  sample's crew interface output equals the output computed independently from the ICD-FCP inputs
  and the selected values of the latest control frame that starts at or before the sample
  (IN-C8-40).
Parameters:    P-TM-010, P-SYS-310
TBD/TBR:       P-TM-010, P-SYS-310 values TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-310

```req
ID:            L2-AER-FCP-310
Level:         L2
Type:          Performance
Statement:     When an input of the flight control panel or a selected value it holds changes at a
  control frame, the flight control panel shall present the change in its crew interface output
  within [P-TM-010] of the start of that control frame.
Rationale:     The FCP share of the annunciation latency [P-SYS-470] is one output sample period
  [P-TM-010] (L1-AER-470; FUNCTIONAL_ANALYSIS §7.5). The rest is upstream: AF decides the content
  within its share [P-AF-060] (C5), and a crew selection waits at most one control frame
  [P-SYS-310] before the panel takes it (L2-AER-FCP-080). For the fuel alerts, the FU subsystem
  sets the indication in the step at which the condition first holds (its share is zero,
  L2-AER-FU-220, -230) and the panel reads it at the next frame start, at most one control frame
  later, so the alert is shown within [P-SYS-310] plus [P-TM-010] of the condition, well inside
  [P-SYS-470] (0.04 s against 0.5 s with the proposed values). Measured as CV-860, from the start
  of the frame at which the input or selected value changes to the first output sample that shows
  it.
  Sufficiency (L1-AER-470): a change of mode state, target or gear position given by AF, or of a
  selected value, reaches the output within [P-TM-010] of its frame (this record); -320, -330,
  -340 and -350 make each of them an annunciation, and -040 and -300 place them in each sample.
  With AF's share [P-AF-060] and the frame wait of -080, the change is annunciated within
  [P-SYS-470].
  Sufficiency (L1-AER-570, L1-AER-580): with -390 and -400 (the alert content) and FU's zero share,
  this record keeps each fuel alert within [P-SYS-470] of its condition.
Parent(s):     L1-AER-470, L1-AER-570, L1-AER-580
Source:        N-060, N-150, N-210; FUNCTIONAL_ANALYSIS §7.5; CONOPS §4.4, §4.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-310; success criteria: in the mode-transition tests and the reference
  mission (SC-110), for each change of the annunciation content, of a navigation quantity, of the
  fuel state and of a selected value, the first output sample showing it is within [P-TM-010] of
  the start of the control frame at which the panel took it; each LOW FUEL and FUEL EXHAUSTED
  annunciation is within [P-SYS-310] plus [P-TM-010] of the first simulation step at which its
  fuel-state condition holds.
Parameters:    P-TM-010, P-SYS-310, P-SYS-470, P-AF-060
TBD/TBR:       P-TM-010, P-SYS-310, P-SYS-470 values TBR (TT-070), P-AF-060 value TBR (TT-070),
  Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-320

```req
ID:            L2-AER-FCP-320
Level:         L2
Type:          Functional
Statement:     The flight control panel shall annunciate each item of the mode state in the
  annunciation content with the label that AF_MODE_LOGIC assigns to that item.
Rationale:     The crew needs to know which mode is active, which is armed and what the vehicle
  will do next, from the annunciations alone (N-060, N-210). The mode state is the active
  horizontal and vertical modes (or the one mode that governs both axes), the armed modes and
  whether autoflight is engaged (glossary *Mode state*). AF decides the content and the labels
  (L1-AER-470: the labels are C5's; CONOPS §4.4 gives provisional ones), so the panel shows the
  label that AF_MODE_LOGIC gives each mode in each state and adds none of its own; the mode logic
  and its annunciation are then defined in one place. With no mode active, for example on the
  ground before a Takeoff, each item is annunciated as empty. What the mode state is after fuel
  exhaustion is AF's (D68, TT-580); the panel shows it the same way.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310.
  Sufficiency (L1-AER-490): see L2-AER-FCP-030.
Parent(s):     L1-AER-470, L1-AER-490
Source:        N-060, N-210; CONOPS §4.4; D56, D68
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-320; success criteria: in the mode-transition tests and the reference
  mission (SC-110), at each output sample, the mode-state annunciation holds, for each item of the
  annunciation content of the latest control frame, the AF_MODE_LOGIC label of that item, and no
  other mode label.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-330

```req
ID:            L2-AER-FCP-330
Level:         L2
Type:          Functional
Statement:     The flight control panel shall annunciate each target of the annunciation content as
  its shown value, with the quantity to which the target applies.
Rationale:     The crew needs to see the targets the active and armed modes are flying (N-060): for
  example the altitude that Altitude hold is armed to capture, the vertical speed Go to altitude
  is using (the standard one or the selected one), the altitude Altitude hold holds when engaged
  directly, or the hover height. AF decides which targets are in the content and gives them in SI
  (C5); the panel converts each with L2-AER-FCP-210 and -220 and names its quantity (altitude,
  vertical speed, horizontal speed or heading). A target that came from a selected value shows the
  selected value, because each selection resolution is a multiple of the display resolution
  (L2-AER-FCP-210). The selector readouts are a separate item (L2-AER-FCP-350): a readout is what
  the crew set, a target annunciation is what the modes use.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310.
Parent(s):     L1-AER-470
Source:        N-060; CONOPS §4.3, §4.4, SC-020, SC-050
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-330; success criteria: in SC-020, SC-050 and the reference mission
  (SC-110), at each output sample, the target annunciation holds each target of the annunciation
  content of the latest control frame, with its quantity, as its shown value per -210 and -220.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-340

```req
ID:            L2-AER-FCP-340
Level:         L2
Type:          Functional
Statement:     The flight control panel shall annunciate the landing gear position of the
  annunciation content as GEAR DOWN when the gear is extended, GEAR UP when it is retracted and
  GEAR TRANSIT when it is in transit.
Rationale:     The gear position is annunciated because a landing needs the gear extended and the
  crew needs to know what the vehicle will do next (L1-AER-470 v2, N-060). AF passes it from the
  gear state as annunciation content (L1-AER-880). The gear position is not a mode, so its labels
  are the panel's, like the fuel alerts; CONOPS SC-130 left them to C5 and C8, and C8 proposes
  these (C8-Q03). The three labels cover the three gear positions (glossary *Gear position*). No
  crew-facing unit applies.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310; this record makes the gear position an
  annunciation.
Parent(s):     L1-AER-470
Source:        N-060; D69; CONOPS SC-130
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-340; success criteria: in the takeoff and landing scenario (SC-130), at
  each output sample, the gear-position annunciation is GEAR DOWN, GEAR UP or GEAR TRANSIT as the
  gear position in the annunciation content of the latest control frame is extended, retracted or
  in transit, and each change of gear position appears within [P-TM-010] of its control frame.
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-350

```req
ID:            L2-AER-FCP-350
Level:         L2
Type:          Functional
Statement:     The flight control panel shall give the readout of each selector as the selected
  value that the selector holds, in the crew-facing unit in which it was selected, with no
  conversion.
Rationale:     The panel shows the values the crew sets: horizontal speed in kt, vertical speed in
  ft/min, target altitude in ft and the selected heading in degrees (D71). The readout is the
  selected value itself, as held (L2-AER-FCP-150), so the crew reads back exactly what it set,
  with no conversion round trip and no display rounding; each selected value is already a
  multiple of its selection resolution. A refused selection leaves the readout unchanged
  (L2-AER-FCP-140). Each readout is present at each output sample, whatever the mode state: the
  heading readout is the selector of Heading mode, shown in each mode.
  Sufficiency (L1-AER-470): see L2-AER-FCP-310; a change of a selected target is annunciated in
  its readout. Sufficiency (L1-AER-490): see L2-AER-FCP-030.
  Sufficiency (L1-AER-500): see L2-AER-FCP-230.
Parent(s):     L1-AER-470, L1-AER-490, L1-AER-500
Source:        D71; CONOPS §4.3; N-060, N-070
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-350; success criteria: in SC-050 and the reference mission (SC-110), at
  each output sample, each selector readout equals the last accepted selected value of that
  selector (or its initial selected value), in its CV-740 unit, digit for digit.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-360

```req
ID:            L2-AER-FCP-360
Level:         L2
Type:          Functional
Statement:     The flight control panel shall indicate the altitude, vertical speed, horizontal
  speed, heading and track of the navigation quantities as their shown values.
Rationale:     The crew sees the vehicle quantities (L1-AER-490 rationale; glossary *Indication*;
  CONOPS §4.3): altitude in ft, vertical speed in ft/min, horizontal speed in kt, heading and track
  in degrees. Navigation computes them once, for autoflight and the panel alike (L1-AER-530,
  -890), and the panel only converts and rounds them (L2-AER-FCP-210, -220). The horizontal speed
  is the ground speed (CV-480). Heading and track are shown separately because they are
  independent on the Aeronef (CV-550). On the ground at rest, the altitude indication is the
  altitude of the centre of gravity, [P-DYN-030]/2 plus [P-DYN-040] (11 ft with the present
  values), not zero, because altitude is measured at the centre of gravity (CV-430).
  Sufficiency (L1-AER-490): see L2-AER-FCP-030.
Parent(s):     L1-AER-490
Source:        N-060, N-380; CONOPS §4.3; CV-430 to CV-550
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-360; success criteria: in the reference mission (SC-110), at each output
  sample, each of the five indications equals the shown value computed independently from the
  navigation quantity of the latest control frame (IN-C8-40), including the ground rests.
Parameters:    P-DYN-030, P-DYN-040
TBD/TBR:       P-DYN-030 value TBR (TT-740), Martin, 2026-11-30; P-DYN-040 value TBR (TT-830),
  Martin, G2 (C1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-370

```req
ID:            L2-AER-FCP-370
Level:         L2
Type:          Functional
Statement:     While a navigation quantity is not valid, the flight control panel shall give its
  indication as not valid, with no shown value.
Rationale:     Track is undefined at zero horizontal speed, and heading near ±90° of pitch (CV-540,
  CV-580). Navigation gives the validity with each quantity, from the thresholds [P-NAV-010] and
  [P-NAV-030] (L1-AER-890, C6). A value shown while its quantity is undefined would mislead the
  crew; the panel shows that the indication is not valid instead. Track is not valid on the
  ground, in Hover, in Stationary and in a turn in place, which are ordinary states. Heading is
  not expected to be invalid, because pitch is held at zero (D57), but the rule covers it. The
  panel uses the validity that navigation gives and sets no threshold of its own, so the crew and
  autoflight see the same validity (CV-580 leaves the behaviour to NAV, AF and FCP, CR-B1-13).
  Sufficiency (L1-AER-490): see L2-AER-FCP-030; this record gives the indications their validity.
Parent(s):     L1-AER-490
Source:        CV-540, CV-580; CR-B1-13; CONOPS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-370; success criteria: in SC-040 and SC-120 (zero horizontal speed),
  in SC-130 on the ground and in a test source run at ICD-FCP (IN-C8-40) with each quantity
  flagged not valid, the indication of each quantity flagged not valid is given as not valid
  with no shown value at each output sample, and as a shown value at each sample at which it is
  valid.
Parameters:    P-NAV-010, P-NAV-030
TBD/TBR:       P-NAV-010, P-NAV-030 values TBR (TT-200), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-380

```req
ID:            L2-AER-FCP-380
Level:         L2
Type:          Functional
Statement:     The flight control panel shall indicate the remaining fuel mass of the fuel state in
  pounds as its shown value.
Rationale:     The crew needs to see how much fuel is left (N-150), in pounds (D9, CV-740). The FU
  subsystem gives the remaining fuel mass in kg in the fuel state (L2-AER-FU-210, -240); the panel
  converts it by the exact CV-750 factor (0.453 592 37 kg per lb) and rounds it to [P-FCP-010]
  (L2-AER-FCP-210). On the ground the fuel is constant (L1-AER-940), and so is the indication.
  Sufficiency (L1-AER-560): FU gives the remaining fuel mass at each step (L2-AER-FU-210); this
  record and -210 show it in lb, and -300 and -030 put it in each output sample, so the remaining
  fuel mass is indicated at each output sample, which is the FCP share of L1-AER-560.
Parent(s):     L1-AER-560
Source:        N-150; D9; CONOPS §4.3, §4.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-380; success criteria: at each output sample of the reference mission
  (SC-110), the fuel indication equals the remaining fuel mass of the fuel state of the latest
  control frame divided by 0.453 592 37 and rounded half away from zero to [P-FCP-010].
Parameters:    P-FCP-010
TBD/TBR:       P-FCP-010 value TBR (TT-960), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-390

```req
ID:            L2-AER-FCP-390
Level:         L2
Type:          Functional
Statement:     While the fuel state indicates low fuel and does not indicate fuel exhaustion, the
  flight control panel shall annunciate LOW FUEL as the fuel alert.
Rationale:     The crew needs a warning before the fuel runs out (N-150); running out is the crew's
  to avoid, with this alert (D68). The low-fuel indication is set by FU when the remaining fuel
  mass is below the fraction [P-FU-020] of the capacity [P-FU-010] (L2-AER-FU-220), so a run that
  starts below it shows LOW FUEL from its first sample, on the ground included. The label is the
  CONOPS one (§4.5, SC-110); the alert label is L2 and the panel's (L1-AER-570, IN-C2-43). The
  fuel alert is one annunciation item with one label at a time: at fuel exhaustion FUEL EXHAUSTED
  replaces LOW FUEL (L2-AER-FCP-400), as C2 suggested. This is design decision DD-550.
  Sufficiency (L1-AER-570): FU sets the low-fuel indication at the step at which the fuel falls
  below the threshold; this record annunciates LOW FUEL while it is set; -410 clears the alert
  while it is not; -310 bounds the delay so that the alert comes within [P-SYS-470].
Parent(s):     L1-AER-570
Source:        N-150; CONOPS §4.5, SC-110; D68; IN-C2-43; DD-550
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-390; success criteria: in the reference mission (SC-110), the fuel alert
  is LOW FUEL at each output sample whose latest control frame read a fuel state with the low-fuel
  indication set and the fuel-exhaustion indication clear, and is not LOW FUEL at any other
  sample; in a run started on the ground below the threshold, it is LOW FUEL at the first sample.
Parameters:    P-FU-020, P-FU-010
TBD/TBR:       P-FU-020 value TBR (TT-130), P-FU-010 value TBR (TT-120), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-400

```req
ID:            L2-AER-FCP-400
Level:         L2
Type:          Functional
Statement:     While the fuel state indicates fuel exhaustion, the flight control panel shall
  annunciate FUEL EXHAUSTED as the fuel alert.
Rationale:     The crew needs to know when the fuel has run out and what follows (N-150): the
  effectors stop, and the ground contact that follows in flight is a crash (D68, L1-AER-200). The
  fuel-exhaustion indication is set by FU from the first step with zero fuel to the end of the run
  (L2-AER-FU-230), so the alert holds to the end of the run; in a run that starts on the ground
  with no fuel it holds from the first sample (SC-130 zero-fuel variation). The label is the
  CONOPS one (§4.5, SC-110). It replaces LOW FUEL in the one fuel-alert item (DD-550),
  because the more severe state is the one the crew must see; the low-fuel indication stays set
  in the fuel state (L2-AER-FU-220). What the mode annunciations show after exhaustion is AF's
  (D68, TT-580).
  Sufficiency (L1-AER-580): FU sets the exhaustion indication at the first step with zero fuel;
  this record annunciates FUEL EXHAUSTED while it is set; -310 bounds the delay so that it comes
  within [P-SYS-470].
Parent(s):     L1-AER-580
Source:        N-150; CONOPS §4.5, SC-110, SC-130; D68; IN-C2-43; DD-550
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-400; success criteria: in the reference mission (SC-110) and in a run
  started on the ground with zero fuel, the fuel alert is FUEL EXHAUSTED at each output sample
  whose latest control frame read a fuel state with the fuel-exhaustion indication set, and never
  LOW FUEL at those samples.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-410

```req
ID:            L2-AER-FCP-410
Level:         L2
Type:          Functional
Statement:     While the fuel state indicates neither low fuel nor fuel exhaustion, the flight
  control panel shall give the fuel alert with no label.
Rationale:     An alert that stayed on when its condition does not hold would make the alert
  meaningless (N-150). FU never refuels the vehicle during a run (L2-AER-FU-100), so in practice
  the alert clears only at the start of a run with fuel at or above the threshold; the record
  still closes the decision table of the fuel alert: no label, LOW FUEL (-390) or FUEL EXHAUSTED
  (-400), one at a time (DD-550).
  Sufficiency (L1-AER-570, L1-AER-580): with -390 and -400 this record makes the fuel alert follow
  the fuel state in each of its three cases, so each alert appears for its condition and for no
  other.
Parent(s):     L1-AER-570, L1-AER-580
Source:        N-150; CONOPS §4.5; DD-550
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-410; success criteria: in the reference mission (SC-110), the fuel alert
  has no label at each output sample whose latest control frame read a fuel state with both
  indications clear, from the first sample to the first low-fuel sample.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-500

```req
ID:            L2-AER-FCP-500
Level:         L2
Type:          Interface
Statement:     The flight control panel shall give the operational data output, for each crew
  selection it takes, the selection with its timestamp, its selected value in its crew-facing
  unit, whether the panel accepted it and, for an accepted selected value, its target.
Rationale:     Crew inputs are the first thing the operational data relate in time (L0-OBJ-140,
  L1-AER-610; REVERSE_ENGINEERING §3C). The target is recorded in SI with, where the crew
  selected it, the crew-facing value (CV-760 group 4). A selection the panel refuses
  (L2-AER-FCP-140) is recorded too, as not accepted, so a test can tell a refused selection from
  a lost one. A mode selection is recorded as taken; whether autoflight acted on it is the mode
  state that AF gives to the operational data (L1-AER-620). The timestamp is the one the crew
  interface gave (CV-840); TM records the selection with the frame at which the panel took it.
  Whether each signal is releasable is decided with the RVS (#69).
  Sufficiency (L1-AER-610): this record gives TM each crew selection with its timestamp, its
  value and the target that results from it, which is the FCP share; TM records it and AF gives
  the mode state that results.
Parent(s):     L1-AER-610
Source:        N-340, N-390; CV-760; REVERSE_ENGINEERING.md §3C
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-500; success criteria: each scripted selection of SC-050 and of the
  refusal test TP-FCP-140 appears once in the operational data, with its timestamp, its item, its
  selected value and unit, its acceptance, and for an accepted selected value its SI target equal
  to the target given to autoflight.
Parameters:    —
TBD/TBR:       releasable or protected classification (#69, TT-600), Martin, closes when the plan is
  extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-510

```req
ID:            L2-AER-FCP-510
Level:         L2
Type:          Interface
Statement:     The flight control panel shall give the operational data output, at each output
  sample, the annunciations and selector readouts of its crew interface output.
Rationale:     The operational data record the annunciations presented to the crew
  (L1-AER-620), so a test or the RVS can tie a crew action to the mode change and to what the crew
  saw (N-390). The panel gives what it presented, as presented (CV-760 group 4: a crew-facing
  value recorded as shown), so the record is the crew's view, not a recomputation. The armed and
  active modes in SI-side form are AF's item of the same record (C5). Recording the indications as
  shown is offered to TM as well (IN-C8-50); L1-AER-620 does not ask for it.
  Sufficiency (L1-AER-620): this record gives TM the annunciations presented at each output
  sample, which is the FCP share; AF gives the armed and active modes.
Parent(s):     L1-AER-620
Source:        N-060, N-340, N-390
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-510; success criteria: in each mode-transition test and the reference
  mission (SC-110), each output sample of the operational data holds the four annunciation items
  and the four selector readouts equal to the crew interface output of that sample.
Parameters:    —
TBD/TBR:       Releasable or protected classification (#69, TT-600), Martin, closes when the plan
  is extended to the RVS (D44)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-520

```req
ID:            L2-AER-FCP-520
Level:         L2
Type:          Interface
Statement:     When a run starts, the flight control panel shall set each selector to the initial
  selected value, in its crew-facing unit, that the initial condition gives for that selector.
Rationale:     The targets of the initial condition are the initial selector values, which the
  panel holds (L1-AER-660 v2, FUNCTIONAL_ANALYSIS I-28). They are given in crew-facing units, as
  a crew selection is, so that the same checks and the same exact conversion apply and each
  readout starts exact (C8-Q05, DD-560). The four initial selected values are the FCP
  item of the initial condition; the mode state and the targets that autoflight sets for itself
  are AF's, the kinematic items DYN's and the fuel mass FU's (L2-AER-DYN-430, L2-AER-FU-020). On
  a ground start no mode is active (recommended to C5, #60), and the selectors simply hold the
  values for the first selections after the Takeoff. At the first control frame the panel gives
  autoflight the SI targets of these values (L2-AER-FCP-050), with no selection accepted.
  Sufficiency (L1-AER-660): this record and -530 take the initial selected values; with the DYN,
  FU and AF children, the initial condition of L1-AER-660 is accepted in full.
Parent(s):     L1-AER-660
Source:        N-310; CONOPS §4.6, SC-200; FUNCTIONAL_ANALYSIS I-28; DD-560
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-520; success criteria: for a ground start and an airborne start, each
  with stated initial selected values, the first output sample shows each selector readout equal
  to its initial selected value, and the first control frame gives autoflight their SI targets
  and no accepted selection.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-530

```req
ID:            L2-AER-FCP-530
Level:         L2
Type:          Functional
Statement:     If an initial selected value is one that its selector does not accept, then the
  flight control panel shall give the TST an initial-condition error that names the selector and
  the value.
Rationale:     An initial selected value outside its selectable range or off its resolution
  (L2-AER-FCP-100 to -130) is rejected, not clamped and not rounded, as an initial fuel mass is
  (DD-140): the run stays what the test procedure asked for (D59). The initial-condition error is
  the data item by which the Aeronef tells the TST that an item of the initial condition is out of
  range; the run does not start (glossary). There is no previous value to keep at the start, so
  the refusal rule of L2-AER-FCP-140 cannot apply. Part of DD-560.
  Sufficiency (L1-AER-660): see L2-AER-FCP-520.
Parent(s):     L1-AER-660
Source:        N-310; DD-140; DD-560; ICD-AER-TST (initial-condition error)
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-530; success criteria: for each selector, an initial condition with an
  initial selected value above its range, below its range and off its resolution gives an
  initial-condition error naming that selector and value, and the run does not start; an initial
  condition with each value valid starts.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-FCP-540

```req
ID:            L2-AER-FCP-540
Level:         L2
Type:          Constraint
Statement:     The flight control panel shall compute each of its outputs only from the initial
  selected values, the crew selections and the ICD-FCP inputs of the run.
Rationale:     Repeat runs must give the same pass or fail verdicts (L1-AER-690, D59). The panel
  adds no variation if its outputs depend on nothing but the run's own inputs: no wall-clock time,
  no random source, no state carried over from another run or simulation instance, and no
  dependence on how fast the run executes (CV-810). The order of the selections within a frame is
  fixed by L2-AER-FCP-090. Bit-identical results are not required (D25, D59); the tolerances are
  those of each success criterion (D63 Q4).
  Sufficiency (L1-AER-690): see L2-AER-FCP-090.
Parent(s):     L1-AER-690
Source:        N-330; D25, D59
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-FCP-540; success criteria: two executions of the reference mission (SC-110)
  and of SC-050, with the same configuration, initial condition, selection script and TST step and
  wind inputs, in two simulation instances and at two execution speeds, give the same verdict on
  each success criterion of TP-FCP-310, -350, -390 and -500.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
