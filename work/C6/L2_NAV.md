## NAV — Navigation

The navigation requirements (task C6). The subject of each statement is the navigation subsystem (NAV), one of the four flight software subsystems with flight control (FC), autoflight (AF) and the flight control panel (FCP) (glossary *Flight software*, D55). NAV implements function F-AER-09 (FUNCTIONAL_ANALYSIS §6.1). It runs once per control frame `[P-SYS-310]`, after the flight control panel and before autoflight (DD-010). Its only input is the **frame-start state**, the vehicle state of the first simulation step of the control frame, which the dynamics model gives it exactly (L1-AER-440, L2-AER-DYN-330). Its outputs are the navigation quantities of the frame, each with its validity, to autoflight (ICD-NAV-AF), to the flight control panel (ICD-FCP) and to the operational data output.

**What NAV computes.** Eight quantities, each by its CONVENTIONS definition and nothing else: the altitude (CV-430), the height above the ground (CV-400), the horizontal position (CV-410), the north and east components of the horizontal velocity (CV-460), the horizontal speed (CV-480), the vertical speed (CV-490), the heading (CV-530, by CV-260) and the track (CV-540). They are the navigation quantities of L1-AER-530 and -890. The horizontal position and the horizontal velocity components are there because the modes that hold a position over the ground (Stationary, Hover, Takeoff, Land) need them and autoflight receives no vehicle state (L1-AER-440 gives the state to NAV and FC only); the owner approved them with CR-C6-01 and CR-C5-01 (D76). Each quantity is in SI (CV-720, CV-730); the crew-facing units stay in the panel (CV-760, L1-AER-870).

**Validity (CV-580).** The track is valid while the horizontal speed is at least `[P-NAV-010]`, and its value is zero while it is invalid (DD-430). The heading is valid while the magnitude of the pitch angle is at most `[P-NAV-030]`; its value stays the CV-260 yaw angle, which is defined at every attitude. The other five quantities are defined at every state and the state is exact, so they are valid at each frame; they carry a validity all the same, so that each quantity crosses the interfaces in one form and a later sensor model (#83) changes values and flags, not the interfaces. Pitch and roll are held at zero in every mode (D57, L1-AER-390), so the heading is valid in nominal flight; the threshold matters for airborne test starts and after fuel exhaustion, when the vehicle keeps its angular rate and can tumble. On the ground, and in Stationary, Hover, Takeoff and Land, the horizontal speed is below `[P-NAV-010]` and the track is invalid.

**Altitude and height above the ground (TT-820, D69, D70, D73).** The altitude is that of the centre of gravity above the datum plane (CV-430): the selected altitude, Altitude hold, the operating ceiling and the atmosphere use it. The height above the ground is that of the lowest point of the body shape, the capsule of MS-DYN §2.6, with the landing gear not part of it (CV-400, CR-B3-36, which closed TT-820): the hover height `[P-AF-210]` and the minimum operating height `[P-SYS-210]` are heights above the ground (D67, D70), and Go to hover, Hover, Takeoff and Land guide on it. NAV uses the expression of MS-DYN §2.6 with the body dimensions `[P-DYN-020]` and `[P-DYN-030]` of the run's vehicle parameter set, the same expression the dynamics model uses for the ground contact (IN-C1-45). At rest on the extended gear the height above the ground is the gear length `[P-DYN-040]`; at the hover height the extended gear clears the ground by `[P-AF-210]` − `[P-DYN-040]`, which is an autoflight matter (MS-DYN §2.5). NAV gives no height of the gear itself (C6-Q08).

**Horizontal speed is a ground speed (D72 Q1).** The horizontal speed is the magnitude of the horizontal vehicle velocity relative to the ground (CV-480), which is what the panel selector, Heading and the envelope limit `[P-SYS-230]` refer to. The flight software receives no wind (L1-AER-670, L2-AER-DYN-340), so NAV computes no airspeed and none is required of it. The frame L is inertial (CV-140), so the horizontal speed times the heading rate is the lateral acceleration that autoflight bounds by `[P-AF-200]` when the vehicle moves along its heading (D72 Q1).

**No VOR and no flight path angle (D56).** L1-AER-340, -540 and -550 are Deleted and have no NAV children; P-NAV-020, -040 and -050 are withdrawn; CV-560 and CV-610 to CV-670 are deleted.

**Depth and verification.** Each record is a leaf at L2 (`Allocated to: —`): the next layer would be the implementation (D4). NAV computes each quantity in closed form from the exact state; there is no estimator, filter or predictor, and any estimation algorithm introduced with a sensor model (#83) is a design decision, not a requirement (DD-450). The L1 parents are verified by roll-up (D40, D58). Procedure IDs follow the record number (IN-, AN-, TP-NAV-nnn); Phase 5 (V3) writes the procedures. The analyses compare the NAV outputs of each control frame with an independent computation from the recorded frame-start state, within the agreement tolerances `[P-NAV-060]` (lengths), `[P-NAV-070]` (speeds) and `[P-NAV-080]` (angles, differenced by CV-930); they need the operational data, or a per-frame record, at the frame-start steps (IN-C6-50). The **tumbling test run** used by several records is an airborne test start (D73, B3-1) at an altitude well above the ground, with zero fuel, level attitude and a pitch rate, so that the vehicle falls while its pitch angle passes through its whole CV-230 range.

**Coverage of the L1 parents.** Every live L1 record allocated to NAV has at least one NAV child.

| L1 parent | What NAV guarantees, in the parent's terms | NAV children |
| --- | --- | --- |
| L1-AER-430 | NAV takes only the vehicle state from the vehicle model, at the boundary as its ICD defines it, and gives the vehicle model nothing | -200, -210 |
| L1-AER-440 | NAV receives the exact frame-start state and computes the frame's quantities from it, unmodified, before autoflight runs in that frame | -200, -310, -320 |
| L1-AER-450 | NAV gives autoflight each quantity the mode catalogue guides on, the horizontal position and velocity of the position-holding modes included | -030, -080, -220, -230, -280 |
| L1-AER-530 | At each control frame NAV computes the altitude, the height above the ground, the horizontal position, the horizontal velocity components, the horizontal speed, the vertical speed, the heading and the track by CV-400 to CV-550, with the CV-580 validity, from the frame-start state and the run's parameter values | -010, -020, -030, -040, -050, -060, -070, -080, -100, -110, -120, -130, -330 |
| L1-AER-640 | NAV gives the operational data output the navigation quantities of each frame, with their validity and the timestamp of the frame-start step | -250 |
| L1-AER-680 | NAV computes one set of quantities per control frame, ready before autoflight executes in that frame | -300, -310 |
| L1-AER-690 | NAV's outputs depend only on the frame-start state and the run's parameter values, and an invalid track has a fixed value, so NAV adds no variation between repeated runs | -140, -320, -330 |
| L1-AER-880 | NAV gives the panel the navigation quantities with their validity, in SI, the same values autoflight receives, as ICD-FCP defines them | -240, -260, -270 |
| L1-AER-890 | NAV passes the eight quantities with their validity to autoflight through ICD-NAV-AF, in SI, with a defined value and validity rule for each, and ICD-NAV-AF defines each item | -100 to -150, -220, -230, -260, -270, -280, -400 |

No record is Derived. The choices inside the records are DD-430 to DD-460 (accepted, D76).

### L2-AER-NAV-010

```req
ID:            L2-AER-NAV-010
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the altitude of
  CONVENTIONS CV-430 from the vehicle position of the frame-start state.
Rationale:     The altitude is the guidance quantity of Altitude hold, Go to altitude and the
  level-off of Vertical speed (D56), and it is indicated to the crew (CONOPS §4.3). It is the
  geometric altitude of the centre of gravity above the datum plane, h = −z_D (CV-430); there is
  no pressure altitude. On the ground at rest it is the rest altitude of MS-DYN §2.5, the body
  radius plus [P-DYN-040], not zero: requirements on the clearance of the body above the ground
  use the height above the ground (L2-AER-NAV-020, CV-400).
  Sufficiency (L1-AER-530): -010, -020, -040, -050, -060 and -070 compute each of the six listed
  quantities by its CONVENTIONS definition, from the frame-start state (-320) and the run's
  parameter values (-330); -100 to -130 give the CV-580 validity of the two direction quantities.
  Together they are the whole of what L1-AER-530 asks, inside the validity range of CV-580.
Parent(s):     L1-AER-530
Source:        N-080, N-190; CV-410, CV-430
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-010; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of the tumbling test run, the altitude NAV outputs differs by at
  most [P-NAV-060] from minus the down component of the recorded position of the frame-start step.
Parameters:    P-NAV-060, P-DYN-040
TBD/TBR:       P-NAV-060 value TBR (TT-950), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-020

```req
ID:            L2-AER-NAV-020
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the height above the
  ground of CONVENTIONS CV-400 from the altitude and the pitch angle of the frame-start state,
  with the body length [P-DYN-020] and the body diameter [P-DYN-030].
Rationale:     The height above the ground is the guidance quantity of Go to hover, Hover, Takeoff
  and Land (L1-AER-530 rationale, D69, D70). The hover height [P-AF-210] and the minimum operating
  height [P-SYS-210] are heights above the ground, measured below the body (D67, D70): TT-820 was
  closed by defining the height above the ground at the lowest point of the body shape, not at the
  centre of gravity (CV-400, CR-B3-36, D73). The landing gear is not part of the body shape, so
  this is the height of the body, not of the gear. NAV uses h − P-DYN-030/2 −
  ((P-DYN-020 − P-DYN-030)/2)·|sin θ|, the expression of MS-DYN §2.6 that the dynamics model uses
  for the ground contact (IN-C1-45), so NAV and DYN agree on where the body is. It does not depend
  on the roll angle (the capsule is axisymmetric about the body x axis) and is defined at every
  attitude, so it has no validity condition (-150). At level attitude, which every mode holds
  (D57), it is h − P-DYN-030/2. At rest on the extended gear it equals the gear length
  [P-DYN-040] (CV-400, MS-DYN §2.5); at the hover height the extended gear clears the ground by
  [P-AF-210] − [P-DYN-040], an autoflight matter (C6-Q08).
  Sufficiency (L1-AER-530): see L2-AER-NAV-010.
Parent(s):     L1-AER-530
Source:        D69, D70, D73; TT-820; CV-400; MS-DYN §2.5, §2.6; IN-C1-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-020; success criteria: (a) at each control frame of a run of the
  reference mission (SC-110) and of the tumbling test run, the height above the ground NAV outputs
  differs by at most [P-NAV-060] from the CV-400 expression evaluated independently from the
  recorded altitude and pitch angle of the frame-start step and the run's [P-DYN-020] and
  [P-DYN-030]; (b) at each control frame in which the vehicle is on the ground, it is within
  [P-NAV-060] of [P-DYN-040].
Parameters:    P-DYN-020, P-DYN-030, P-DYN-040, P-AF-210, P-SYS-210, P-NAV-060
TBD/TBR:       P-DYN-020, P-DYN-030 values TBR (TT-740), P-DYN-040 value TBR (TT-830), Martin,
  2026-11-30 and G2 (C1); P-NAV-060 value TBR (TT-950), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-030

```req
ID:            L2-AER-NAV-030
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the horizontal
  position of CONVENTIONS CV-410 from the vehicle position of the frame-start state.
Rationale:     Stationary and Hover hold the horizontal position over the ground against the wind
  (D56, D60), Takeoff climbs over its ground position and Land descends over the Hover reference
  position (D69, CONOPS §4.4). The reference position is a horizontal position (glossary), and the
  autoflight share of the position-holding budget [P-AF-160] is measured on it (FUNCTIONAL_ANALYSIS
  §7.4). Autoflight receives no vehicle state (L1-AER-440 gives the state to NAV and FC only), and
  NAV derives every guidance quantity from the true state (FUNCTIONAL_ANALYSIS §5.1), so the
  horizontal position reaches autoflight through NAV. The north and east components are in the local
  reference frame, in m (CV-120, CV-410). L1-AER-530 and -890 list the horizontal position since
  CR-C6-01 (D76). The NAV share of the position budget is zero, because the state is exact
  (L1-AER-440). Sufficiency (L1-AER-450): NAV's share of the guidance capability is to give
  autoflight each quantity the mode catalogue guides on: the altitude (Altitude hold, Go to
  altitude, Vertical speed), the vertical speed (Vertical speed, Go to altitude, Takeoff, Land), the
  horizontal speed and the heading (Heading), the track (Heading in a wind, [P-AF-140]), the height
  above the ground (Go to hover, Hover, Takeoff, Land) and the horizontal position (Stationary,
  Hover, Takeoff, Land). This record and -230 compute and pass the horizontal position; -220 passes
  the other six. Together they give autoflight what it needs to guide through each mode of the
  catalogue.
Parent(s):     L1-AER-530, L1-AER-450
Source:        N-130, N-140; D56, D60, D69; CV-410; glossary *Navigation*, *Reference position*
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-030; success criteria: at each control frame of a run of the
  reference mission (SC-110), the north and east components of the horizontal position NAV
  outputs each differ by at most [P-NAV-060] from the north and east components of the recorded
  position of the frame-start step.
Parameters:    P-AF-160, P-AF-140, P-NAV-060
TBD/TBR:       P-NAV-060 value TBR (TT-950), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-040

```req
ID:            L2-AER-NAV-040
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the horizontal speed
  of CONVENTIONS CV-480 from the north and east components of the vehicle velocity of the
  frame-start state.
Rationale:     The horizontal speed is the guidance quantity that Heading flies at the selected
  horizontal speed (D56), and it is indicated to the crew. It is relative to the ground: [P-SYS-230]
  is a ground speed, and so is the panel's horizontal speed selector (D72 Q1, G2-F03). The flight
  software receives no wind (L1-AER-670, L2-AER-DYN-340), so NAV computes no airspeed. The frame L
  is inertial (CV-140), so the horizontal speed times the heading rate is the lateral acceleration
  autoflight bounds by [P-AF-200] when moving along the heading (D72 Q1). It does not depend on the
  attitude. On the ground it is zero.
  Sufficiency (L1-AER-530): see L2-AER-NAV-010.
Parent(s):     L1-AER-530
Source:        D56, D72; CV-480; N-170
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-040; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of a run of SC-060 with a steady wind across the heading, the
  horizontal speed NAV outputs differs by at most [P-NAV-070] from the square root of the sum of
  the squares of the north and east components of the recorded velocity of the frame-start step.
Parameters:    P-SYS-230, P-AF-200, P-NAV-070
TBD/TBR:       P-NAV-070 value TBR (TT-950), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-050

```req
ID:            L2-AER-NAV-050
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the vertical speed of
  CONVENTIONS CV-490 from the down component of the vehicle velocity of the frame-start state.
Rationale:     The vertical speed is the guidance quantity of Vertical speed, of Go to altitude at the
  standard vertical speed [P-AF-220], and of Takeoff and Land at [P-AF-240] (D56, D69, D70), and
  it is indicated to the crew. It is VS = −v_D, positive when climbing, and does not depend on the
  attitude. The landing envelope is assessed by the dynamics model on its own state at the contact
  step (MS-DYN §9.4), not on this quantity.
  Sufficiency (L1-AER-530): see L2-AER-NAV-010.
Parent(s):     L1-AER-530
Source:        D56, D69, D70; CV-490
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-050; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of the tumbling test run, the vertical speed NAV outputs differs
  by at most [P-NAV-070] from minus the down component of the recorded velocity of the frame-start
  step.
Parameters:    P-AF-220, P-AF-240, P-NAV-070
TBD/TBR:       P-AF-240 value TBR (TT-830), Martin, G2 (C5); P-NAV-070 value TBR (TT-950), Martin,
  G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-060

```req
ID:            L2-AER-NAV-060
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the heading of
  CONVENTIONS CV-530 as the yaw angle that CONVENTIONS CV-260 derives from the attitude
  quaternion of the frame-start state.
Rationale:     The heading is the guidance quantity of Heading and the quantity held in Stationary,
  Go to hover, Hover, Takeoff and Land (CONOPS §4.4), and it is indicated to the crew. It is where
  the nose points, defined by the attitude only (CV-530). It equals the Euler yaw angle for each
  pitch angle other than plus or minus a right angle, and CV-260 gives it a value in that singular
  case too, so the heading has a value at every attitude; whether it is meaningful is its validity
  (-120, -130). This is the derivation the dynamics model uses for the recorded Euler angles
  (L2-AER-DYN-070), so NAV's heading equals the heading of the recorded state (IN-C1-31). The
  value is a direction angle in [0, 2π) rad (CV-520, CV-920).
  Sufficiency (L1-AER-530): see L2-AER-NAV-010.
Parent(s):     L1-AER-530
Source:        D56, D57; CV-250, CV-260, CV-530; IN-C1-31
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-060; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of the tumbling test run, the heading NAV outputs lies in
  [0, 2π) rad; at each such frame at which the magnitude of the recorded pitch angle is at most
  [P-NAV-030], it differs, by the CV-930 difference, by at most [P-NAV-080] from the CV-260 yaw
  angle computed independently from the recorded quaternion of the frame-start step. (Beyond
  [P-NAV-030] the yaw angle is ill-conditioned, so two correct computations may differ by more
  than rounding; there the value is only checked for its range.)
Parameters:    P-NAV-080, P-NAV-030
TBD/TBR:       P-NAV-080 value TBR (TT-950), Martin, G2 (I1); P-NAV-030 value TBR (TT-200), Martin,
  G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-070

```req
ID:            L2-AER-NAV-070
Level:         L2
Type:          Functional
Statement:     While the horizontal speed of the frame-start state is at least [P-NAV-010], the
  navigation subsystem shall compute, at each control frame, the track of CONVENTIONS CV-540 from
  the north and east components of the vehicle velocity of the frame-start state.
Rationale:     The track is the direction of horizontal motion over the ground, defined by the
  velocity only (CV-540, CV-550). Autoflight uses it in Heading, where the vehicle moves along its
  heading and the track tolerance [P-AF-140] applies, including in a wind (CONOPS SC-060 / wind),
  and it is indicated to the crew. It is undefined at zero horizontal speed and ill-conditioned
  near it, hence the condition, which is the CV-580 threshold; below it the track is invalid and
  its value is fixed (-110, -140). The value is a direction angle in [0, 2π) rad (CV-520).
  Sufficiency (L1-AER-530): see L2-AER-NAV-010.
Parent(s):     L1-AER-530
Source:        CV-540, CV-550, CV-580; CONOPS SC-060
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-070; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of a run of SC-060 with a steady wind across the heading in which
  the recorded horizontal speed of the frame-start step is at least [P-NAV-010], the track NAV
  outputs lies in [0, 2π) rad and differs, by the CV-930 difference, by at most [P-NAV-080] from
  wrap360(atan2(v_E, v_N)) computed independently from the recorded velocity of that step.
Parameters:    P-NAV-010, P-AF-140, P-NAV-080
TBD/TBR:       P-NAV-010 value TBR (TT-200), Martin, G2 (C6); P-NAV-080 value TBR (TT-950), Martin,
  G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-080

```req
ID:            L2-AER-NAV-080
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall compute, at each control frame, the north and east
  components of the horizontal velocity of CONVENTIONS CV-460 from the vehicle velocity of the
  frame-start state.
Rationale:     The stopping position of a hold entered with the vehicle moving, and the initial
  references of Stationary, Go to hover and Heading at a low speed, need the velocity vector at any
  speed, including below the validity speed of the track, where the direction of a residual motion
  is not available from the horizontal speed and the track (C5-Q13, DD-390). Autoflight receives no
  vehicle state (L1-AER-440), so the components reach it through NAV. They are the components of
  the ground-referenced vehicle velocity in the local reference frame, in m/s (CV-120, CV-460,
  CV-480), always valid, and they do not depend on the attitude. L1-AER-530 and -890 list them
  since CR-C5-01 (D76).
  Sufficiency (L1-AER-530): the velocity components are among the quantities of the parent; this
  record computes them from the frame-start state, as the other NAV records compute the others.
  Sufficiency (L1-AER-450): see L2-AER-NAV-030.
Parent(s):     L1-AER-530, L1-AER-450
Source:        N-130, N-140; D56, D60, D69; CV-460, CV-480; CR-C5-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Analysis — AN-NAV-080; success criteria: at each control frame of a run of the
  reference mission (SC-110) and of a run of SC-060 with a steady wind across the heading, the north
  and east components of the horizontal velocity NAV outputs each differ by at most [P-NAV-070]
  from the north and east components of the recorded velocity of the frame-start step.
Parameters:    P-NAV-070
TBD/TBR:       P-NAV-070 value TBR (TT-950), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-100

```req
ID:            L2-AER-NAV-100
Level:         L2
Type:          Functional
Statement:     While the horizontal speed of the frame-start state is at least [P-NAV-010], the
  navigation subsystem shall mark the track valid.
Rationale:     CV-580 bounds the validity of the track by the minimum horizontal speed [P-NAV-010],
  inclusive ("minimum horizontal speed for which track is valid"). Autoflight, the panel and the
  operational data read the validity with the value (L1-AER-890 "with their validity"). The
  threshold has no hysteresis (DD-440): with an exact state the validity is a function of the
  frame-start state alone, and a speed that stays near the threshold is a hold, in which the track
  is not used. The proposed value, one knot (C6-Q02), is the horizontal speed selection resolution
  [P-AF-030], and it is above the landing envelope speed [P-SYS-510], so the track is invalid in a
  hold and at each landing.
  Sufficiency (L1-AER-890): the six quantities cross to autoflight through ICD-NAV-AF (-220), each
  with a validity: the track by -100 and -110, the heading by -120 and -130, the other four by
  -150; the value of an invalid track is fixed (-140); each is in SI (-270), with the same value
  and validity as the panel and the operational data receive (-260), and each item is defined in
  ICD-NAV-AF with its unit, frame, range and validity rule (-400). Together they deliver every
  quantity the catalogue guides on with its validity across one defined boundary.
Parent(s):     L1-AER-890, L1-AER-530
Source:        CV-540, CV-580; D55
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-100; success criteria: in a run that accelerates from Stationary
  through [P-NAV-010] to a selected horizontal speed in Heading and then returns to Stationary,
  and in a run of the reference mission (SC-110), the track is marked valid at each control frame
  whose recorded frame-start horizontal speed is at least [P-NAV-010].
Parameters:    P-NAV-010, P-AF-030, P-SYS-510
TBD/TBR:       P-NAV-010 value TBR (TT-200), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-110

```req
ID:            L2-AER-NAV-110
Level:         L2
Type:          Functional
Statement:     While the horizontal speed of the frame-start state is less than [P-NAV-010], the
  navigation subsystem shall mark the track invalid.
Rationale:     The complement of -100 (CV-580). The track is invalid on the ground, where the
  horizontal speed is zero, and in Stationary, Hover, Takeoff and Land once the horizontal motion
  has stopped. Autoflight and the panel do not use an invalid track (IN-C6-10, IN-C6-30).
  Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-890, L1-AER-530
Source:        CV-540, CV-580
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-110; success criteria: in the runs of TP-NAV-100, the track is marked
  invalid at each control frame whose recorded frame-start horizontal speed is less than
  [P-NAV-010], including each frame on the ground.
Parameters:    P-NAV-010
TBD/TBR:       P-NAV-010 value TBR (TT-200), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-120

```req
ID:            L2-AER-NAV-120
Level:         L2
Type:          Functional
Statement:     While the magnitude of the pitch angle of the frame-start state is at most
  [P-NAV-030], the navigation subsystem shall mark the heading valid.
Rationale:     At and near a pitch angle of plus or minus a right angle the heading and the roll
  angle are not separately meaningful (CV-260): a small change of attitude moves the heading by a
  large angle. CV-580 bounds the validity of the heading by the maximum magnitude of the pitch
  angle [P-NAV-030], inclusive. Pitch is held within [P-AF-180] of zero in every mode (D57,
  L1-AER-390), far inside the threshold, so the heading is valid in nominal flight. The threshold
  matters in an airborne test start at a large pitch angle and after fuel exhaustion, when the
  vehicle keeps the angular rate it had and can tumble (L1-AER-200). No hysteresis (DD-440).
  Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-890, L1-AER-530
Source:        CV-260, CV-580; D57
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-120; success criteria: in the tumbling test run and in a run of the
  reference mission (SC-110), the heading is marked valid at each control frame whose recorded
  frame-start pitch angle has a magnitude of at most [P-NAV-030].
Parameters:    P-NAV-030, P-AF-180
TBD/TBR:       P-NAV-030 value TBR (TT-200), Martin, G2 (C6); P-AF-180 value TBR (TT-190), Martin,
  G2 (C5)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-130

```req
ID:            L2-AER-NAV-130
Level:         L2
Type:          Functional
Statement:     While the magnitude of the pitch angle of the frame-start state exceeds [P-NAV-030],
  the navigation subsystem shall mark the heading invalid.
Rationale:     The complement of -120 (CV-580). The heading value keeps the CV-260 yaw angle while
  it is invalid (-060): CV-260 defines it at every attitude, so no substitute value is needed, and
  the value stays a function of the frame-start state.
  Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-890, L1-AER-530
Source:        CV-260, CV-580
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-130; success criteria: in the tumbling test run, the heading is marked
  invalid at each control frame whose recorded frame-start pitch angle has a magnitude greater than
  [P-NAV-030], and at least one such frame occurs.
Parameters:    P-NAV-030
TBD/TBR:       P-NAV-030 value TBR (TT-200), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-140

```req
ID:            L2-AER-NAV-140
Level:         L2
Type:          Functional
Statement:     While the track is invalid, the navigation subsystem shall set the track value to
  zero.
Rationale:     At zero horizontal speed the track has no defined value (CV-540), and the arc tangent
  of a zero vector depends on the signs of the zero components in floating point. A fixed value
  makes the output a function of the frame-start state alone, so repeated runs agree (L1-AER-690,
  D59), and keeps NAV without memory: it has no state to initialise (FUNCTIONAL_ANALYSIS F-AER-14).
  Holding the last valid track would carry state across frames and make the value depend on the
  history of the run (DD-430, C6-Q04). Consumers read the validity before the value (IN-C6-10,
  IN-C6-30, IN-C6-40). The heading needs no counterpart, because CV-260 defines it at every
  attitude (-130).
  Sufficiency (L1-AER-890): see L2-AER-NAV-100. Sufficiency (L1-AER-690): see L2-AER-NAV-320.
Parent(s):     L1-AER-890, L1-AER-690
Source:        CV-540, CV-580; D59; FUNCTIONAL_ANALYSIS F-AER-14
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-140; success criteria: in the runs of TP-NAV-100, the track value is
  zero at each control frame at which the track is marked invalid, including each frame on the
  ground and in Stationary and Hover.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-150

```req
ID:            L2-AER-NAV-150
Level:         L2
Type:          Functional
Statement:     The navigation subsystem shall mark the altitude, the height above the ground, the
  horizontal position, the horizontal speed and the vertical speed valid at each control frame.
Rationale:     These quantities are defined at every state (CV-400 to CV-490), and the state is
  exact (L1-AER-440), so no validity condition applies to them. L1-AER-890 passes each quantity
  "with its validity"; giving each a validity keeps one form for each quantity across the
  interfaces, so a later sensor model (#83) changes values and flags, not the interfaces.
  Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-890
Source:        CV-400 to CV-490, CV-580; #83
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-150; success criteria: in a run of the reference mission (SC-110) and
  in the tumbling test run, each of the five quantities is marked valid at each control frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-200

```req
ID:            L2-AER-NAV-200
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall take, at the start of each control frame, the
  frame-start state from the vehicle model at the vehicle-model boundary, as the vehicle-model
  boundary ICD defines it.
Rationale:     NAV is flight software, and the vehicle state reaches it only across the
  vehicle-model boundary (L1-AER-430). The dynamics model provides the state of the first
  simulation step of each frame, equal to the state it records (L2-AER-DYN-330, IN-C1-30); this
  record is the NAV side of that exchange. The state carries the quaternion attitude, with the
  Euler angles derived by CV-260 (L2-AER-DYN-070), the frames and units of CONVENTIONS, and the
  vehicle acceleration (MS-DYN §3); NAV uses the position, the velocity and the attitude.
  Sufficiency (L1-AER-430): NAV's part of the boundary is the vehicle state in (this record) and
  nothing else either way (-210). With the DYN, FU, EF, FC, AF and FCP children, every item
  crossing the boundary is one of the listed kinds.
  Sufficiency (L1-AER-440): DYN gives the exact frame-start state (L2-AER-DYN-330); NAV receives it
  (this record), computes the frame's quantities from it without modification (-320) and has
  them ready before autoflight runs in the frame (-310). Together NAV's quantities are those of the
  exact simulated state of the frame-start step, as L1-AER-440 requires.
Parent(s):     L1-AER-430, L1-AER-440
Source:        L0-ASM-010; IN-B1-01, IN-C1-30; FUNCTIONAL_ANALYSIS I-10
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-200; success criteria: at each control frame of a run of the
  reference mission (SC-110), the vehicle state NAV receives equals, element by element, the
  recorded vehicle state of the frame-start step.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-210

```req
ID:            L2-AER-NAV-210
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall limit its data exchange with the vehicle model to
  receiving the vehicle state.
Rationale:     The boundary list of L1-AER-430 is closed. NAV needs neither the gear state
  (autoflight reads it from the vehicle model directly), nor the mass properties, nor the fuel
  state (the panel takes it from FU), and it commands nothing in the vehicle model. The wind is
  not part of the vehicle state and does not reach the flight software (L2-AER-DYN-340).
  Sufficiency (L1-AER-430): see L2-AER-NAV-200.
Parent(s):     L1-AER-430
Source:        IN-B1-01; FUNCTIONAL_ANALYSIS §3.3, §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-210; success criteria: the NAV implementation reads no item of
  the vehicle-model boundary ICD other than the vehicle state, and writes no item of it.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-220

```req
ID:            L2-AER-NAV-220
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall provide autoflight, at each control frame, with the
  altitude, the height above the ground, the horizontal speed, the vertical speed, the heading and
  the track of that frame, each with its validity, through the one interface defined in
  ICD-NAV-AF.
Rationale:     The navigation → autoflight boundary of the architecture (FUNCTIONAL_ANALYSIS §5.1,
  I-17; L1-AER-890). One definition of each quantity is used by autoflight, the crew indications
  and the operational data (-260). The content of ICD-NAV-AF is in `icd/ICD-NAV-AF.md`.
  Sufficiency (L1-AER-890): see L2-AER-NAV-100. Sufficiency (L1-AER-450): see L2-AER-NAV-030.
Parent(s):     L1-AER-890, L1-AER-450
Source:        N-190; FUNCTIONAL_ANALYSIS I-17, §5.1; IN-B1-04
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-220; success criteria: the NAV implementation provides each of
  the six quantities and its validity to autoflight only as items of ICD-NAV-AF, at each control
  frame, and each item is defined in ICD-NAV-AF.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-230

```req
ID:            L2-AER-NAV-230
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall provide autoflight, at each control frame, with the
  horizontal position of that frame, with its validity, through ICD-NAV-AF.
Rationale:     The position-holding modes need the horizontal position (L2-AER-NAV-030), and
  autoflight receives it only from NAV. It crosses the same interface as the other navigation
  quantities, so ICD-NAV-AF stays the one navigation → autoflight interface (L1-AER-890). L1-AER-890
  lists it since CR-C6-01 (D76); the record stays apart from -220 so that each item of ICD-NAV-AF
  has its own record. Sufficiency (L1-AER-450): see L2-AER-NAV-030.
Parent(s):     L1-AER-890, L1-AER-450
Source:        D56, D60, D69; FUNCTIONAL_ANALYSIS §5.1
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-230; success criteria: the NAV implementation provides the north
  and east components of the horizontal position and their validity to autoflight only as items
  of ICD-NAV-AF, at each control frame, and the items are defined in ICD-NAV-AF in m in the local
  reference frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-240

```req
ID:            L2-AER-NAV-240
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall provide the flight control panel, at each control
  frame, with the altitude, the height above the ground, the horizontal speed, the vertical speed,
  the heading and the track of that frame, each with its validity, as defined in ICD-FCP.
Rationale:     L1-AER-880 passes the navigation quantities into the panel, which presents the
  indications: the altitude, vertical speed, horizontal speed, heading and track (CONOPS §4.3,
  glossary *Indication*). NAV gives them in SI; the panel converts them to crew units and rounds
  them (L1-AER-870, CV-760, CV-780). The height above the ground is given too, as one of the
  navigation quantities; whether the panel indicates it is for the panel (IN-C6-30). The
  horizontal position is not an indication and is not given. How the panel presents an invalid
  track or heading is for the panel (IN-C6-30).
  Sufficiency (L1-AER-880): NAV's part of the panel boundary is the navigation quantities into the
  panel (this record), in SI (-270), with the values and validity autoflight receives (-260). With
  the FCP, AF and FU children, every item crossing the panel boundary is one of the listed kinds
  and is defined in ICD-FCP.
Parent(s):     L1-AER-880
Source:        D55; CONOPS §4.3; FUNCTIONAL_ANALYSIS I-18; IN-B1-08
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-240; success criteria: the NAV implementation provides each of
  the six quantities and its validity to the flight control panel only as items of ICD-FCP, at
  each control frame, and each item is defined in ICD-FCP.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-250

```req
ID:            L2-AER-NAV-250
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall provide the operational data output, at each control
  frame, with the navigation quantities of that frame, each with its validity, and the timestamp
  of the frame-start step.
Rationale:     L1-AER-640 records the altitude, the height above the ground, the horizontal speed,
  the vertical speed, the heading and the track at each output sample; the TST assesses the
  takeoffs, hovers and landings from the height above the ground (L1-AER-920 to -970). NAV gives
  them at each control frame and the operational data output samples them every [P-TM-010]. The
  timestamp (CV-840) ties each value to the state it was computed from, so a test can compare them
  with the recorded state. The validity is given so that the data show what autoflight and the panel
  saw (L1-AER-640 asks for it since CR-C6-02, D76). The horizontal position is part of the recorded
  vehicle state already. Sufficiency (L1-AER-640): NAV's share of the list is the navigation
  quantities (this record); DYN gives the vehicle state, the gear state, the sensed acceleration and
  the events (L2-AER-DYN-350), FU the masses, and TM records them.
Parent(s):     L1-AER-640
Source:        N-250, N-340, N-390; FUNCTIONAL_ANALYSIS I-35
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-250; success criteria: at each output sample of a run of the reference
  mission (SC-110), the operational data hold the six navigation quantities, their validity and
  the frame-start timestamp that NAV provided for the latest control frame starting at or before
  the step of that sample.
Parameters:    P-TM-010
TBD/TBR:       P-TM-010 value TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-260

```req
ID:            L2-AER-NAV-260
Level:         L2
Type:          Constraint
Statement:     The navigation subsystem shall provide autoflight, the flight control panel and the
  operational data output with the same value and the same validity of each navigation quantity
  in each control frame.
Rationale:     One definition of each navigation quantity, used by autoflight, the crew indications
  and the operational data, is the reason NAV is a subsystem of its own (FUNCTIONAL_ANALYSIS §5.2
  item 3, §5.3). The crew then sees what autoflight guides on, and the operational data record
  what both used, so a test or the RVS can tie a mode behaviour to an indication (N-390).
  Sufficiency (L1-AER-880): see L2-AER-NAV-240. Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-880, L1-AER-890
Source:        FUNCTIONAL_ANALYSIS §5.2, §5.3; N-390
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-260; success criteria: at each control frame of a run of the reference
  mission (SC-110), the value and the validity of each navigation quantity received by autoflight,
  by the flight control panel and by the operational data output are identical.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-270

```req
ID:            L2-AER-NAV-270
Level:         L2
Type:          Constraint
Statement:     The navigation subsystem shall provide each quantity in its SI unit of CONVENTIONS
  CV-720, with each angle in radians and each direction angle in the range of CONVENTIONS CV-520.
Rationale:     Interface signals are in SI (CV-710, L1-AER-730); the crew-facing units appear only in
  the panel (CV-760, L1-AER-500, -870), so no unit conversion takes place in NAV and none crosses
  into autoflight. Lengths and positions in m, speeds in m/s, the heading and the track in rad in
  [0, 2π) (CV-730, CV-520, CV-920).
  Sufficiency (L1-AER-880): see L2-AER-NAV-240. Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-880, L1-AER-890
Source:        CV-520, CV-710 to CV-760
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-270; success criteria: each item that NAV provides in ICD-NAV-AF,
  ICD-FCP and ICD-AER-TST has the SI unit of CV-720 for its quantity, angles are in rad, the
  heading and the track are defined in [0, 2π) rad, and the NAV implementation applies no crew-unit
  conversion factor of CV-750.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-280

```req
ID:            L2-AER-NAV-280
Level:         L2
Type:          Interface
Statement:     The navigation subsystem shall provide autoflight, at each control frame, with the
  north and east components of the horizontal velocity of that frame, with their validity, through
  ICD-NAV-AF.
Rationale:     The holds of the horizontal position need the velocity vector (L2-AER-NAV-080), and
  autoflight receives it only from NAV. It crosses the same interface as the other navigation
  quantities, so ICD-NAV-AF stays the one navigation to autoflight interface (L1-AER-890).
  Sufficiency (L1-AER-890): see L2-AER-NAV-220.
  Sufficiency (L1-AER-450): see L2-AER-NAV-030.
Parent(s):     L1-AER-890, L1-AER-450
Source:        D56, D60, D69; FUNCTIONAL_ANALYSIS §5.1, I-17; CR-C5-01
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-280; success criteria: the NAV implementation provides the north
  and east components of the horizontal velocity and their validity to autoflight only as items of
  ICD-NAV-AF, at each control frame, and the items are defined in ICD-NAV-AF in m/s in the local
  reference frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-300

```req
ID:            L2-AER-NAV-300
Level:         L2
Type:          Performance
Statement:     The navigation subsystem shall compute one set of navigation quantities in each
  control frame of period [P-SYS-310].
Rationale:     The flight software runs at the control frame period, an integer multiple of the
  simulation step [P-SYS-300] (L1-AER-680, DD-010). One set per frame, from that frame's
  frame-start state, keeps the navigation quantities on the CV-840 time base and gives autoflight
  a new set at each of its executions.
  Sufficiency (L1-AER-680): NAV executes at the control frame period (this record) and in its
  place in the frame order, before autoflight (-310); the AF, FC and FCP children cover theirs.
Parent(s):     L1-AER-680
Source:        DD-010; CV-830; FUNCTIONAL_ANALYSIS §4.2
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-300; success criteria: in a run of the reference mission (SC-110), NAV
  provides exactly one set of navigation quantities per control frame, each timestamped with the
  frame-start step of its frame, and the timestamps of successive sets differ by [P-SYS-310].
Parameters:    P-SYS-310, P-SYS-300
TBD/TBR:       P-SYS-300, P-SYS-310 values TBR (TT-070), Martin, G2 (I1)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-310

```req
ID:            L2-AER-NAV-310
Level:         L2
Type:          Performance
Statement:     The navigation subsystem shall complete the navigation quantities of each control
  frame before autoflight executes in that frame.
Rationale:     The frame order is FCP, NAV, AF, FC (DD-010, FUNCTIONAL_ANALYSIS §4.2). Autoflight
  then guides on the quantities of the current frame-start state, so the only delay between the
  state and the axis references is the frame sampling that the timing budget counts (L1-AER-440,
  FUNCTIONAL_ANALYSIS §7.5); a quantity one frame old would add a frame of latency to every mode.
  Sufficiency (L1-AER-680): see L2-AER-NAV-300. Sufficiency (L1-AER-440): see L2-AER-NAV-200.
Parent(s):     L1-AER-680, L1-AER-440
Source:        DD-010; FUNCTIONAL_ANALYSIS §4.2, §7.5
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-310; success criteria: at each control frame of a run of the
  reference mission (SC-110), the navigation quantities that autoflight uses carry the timestamp of
  the frame-start step of that same frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-320

```req
ID:            L2-AER-NAV-320
Level:         L2
Type:          Constraint
Statement:     The navigation subsystem shall compute the navigation quantities of each control
  frame from no data other than the frame-start state of that frame and the parameter values of
  the run.
Rationale:     Perfect state knowledge (L0-ASM-010, L1-AER-440): NAV uses the exact state as it is,
  with no filter, estimate or prediction, and carries nothing from one frame to the next. Each
  quantity is then the closed form of its CONVENTIONS definition (DD-450); an estimator is a
  design matter that a later sensor model would bring (#83, D4). Without memory, NAV has no state
  to initialise (FUNCTIONAL_ANALYSIS F-AER-14), and its outputs repeat exactly when the state
  repeats.
  Sufficiency (L1-AER-690): NAV adds no variation of its own between repeated runs: its outputs
  are a function of the frame-start state and the run's parameter values (this record, with
  -330), and the value of an invalid track is fixed (-140). So, given the same vehicle states, NAV
  gives the same quantities, and it cannot change a verdict.
  Sufficiency (L1-AER-440): see L2-AER-NAV-200.
Parent(s):     L1-AER-440, L1-AER-690
Source:        L0-ASM-010; D59; FUNCTIONAL_ANALYSIS F-AER-14; #83
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-320; success criteria: (a) two runs of the reference mission (SC-110)
  with the same configuration, initial condition, selection script and TST inputs give identical
  navigation quantities and validity at each control frame; (b) NAV evaluated off-line on the
  recorded frame-start state of each frame of one of these runs, in any order of the frames,
  reproduces the navigation quantities and validity of that frame.
Parameters:    —
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-330

```req
ID:            L2-AER-NAV-330
Level:         L2
Type:          Constraint
Statement:     The navigation subsystem shall take the values of [P-DYN-020], [P-DYN-030],
  [P-NAV-010] and [P-NAV-030] from the vehicle parameter set of the run.
Rationale:     The height above the ground must use the body dimensions the dynamics model uses for
  the ground contact (MS-DYN §2.6, IN-C1-45); taking them from the run's parameter set rather
  than from a copy keeps the two equal when the body dimensions change (TT-740). The validity
  thresholds are parameters, not conventions (CV-580), so they come from the run's parameters
  too, and the identifier and version of the parameter set identify them (L1-AER-650). Where the
  NAV thresholds sit in the run configuration is C6-Q06 (recommended: the vehicle parameter set).
  Sufficiency (L1-AER-530): see L2-AER-NAV-010. Sufficiency (L1-AER-690): see L2-AER-NAV-320.
Parent(s):     L1-AER-530, L1-AER-690
Source:        MS-DYN §2.6; CV-400, CV-580; IN-C1-45
Allocated to:  —
Criticality:   Not assessed
Verification:  Test — TP-NAV-330; success criteria: in two runs started on the ground with vehicle
  parameter sets that differ in [P-DYN-030] and [P-DYN-040], the height above the ground NAV
  outputs at rest is within [P-NAV-060] of the [P-DYN-040] of each run's set; and in two runs of
  TP-NAV-100 with sets that differ in [P-NAV-010], the track validity changes at the [P-NAV-010]
  of each run's set.
Parameters:    P-DYN-020, P-DYN-030, P-DYN-040, P-NAV-010, P-NAV-030, P-NAV-060
TBD/TBR:       P-NAV-010, P-NAV-030 values TBR (TT-200), Martin, G2 (C6)
Owner:         Martin
Status:        Draft
Version:       1
```

### L2-AER-NAV-400

```req
ID:            L2-AER-NAV-400
Level:         L2
Type:          Documentation
Statement:     The navigation subsystem shall have each quantity it provides to autoflight defined
  in ICD-NAV-AF with its SI unit, its frame, its range of values and its validity rule.
Rationale:     L1-AER-890 asks its children to show that each quantity is defined in ICD-NAV-AF with
  its unit, frame and validity. The range of values (for example [0, 2π) rad for the heading and
  the track) and the value of an invalid track (-140) complete the definition, so that autoflight
  implementations read the items in one way (L0-CON-210). The content is in `icd/ICD-NAV-AF.md`.
  Sufficiency (L1-AER-890): see L2-AER-NAV-100.
Parent(s):     L1-AER-890
Source:        FUNCTIONAL_ANALYSIS §5.1; IN-B1-04; TT-680
Allocated to:  —
Criticality:   Not assessed
Verification:  Inspection — IN-NAV-400; success criteria: ICD-NAV-AF defines each item NAV provides
  to autoflight with its SI unit, its frame (or none for a scalar), its range of values, its
  validity rule with the CV-580 parameter it uses, and the value it carries while invalid.
Parameters:    P-NAV-010, P-NAV-030
TBD/TBR:       —
Owner:         Martin
Status:        Draft
Version:       1
```
