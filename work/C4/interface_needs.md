# C4 — Interface needs (FC)

What the flight control subsystem (FC, `work/C4/L2_FC.md`, `work/C4/L3_FC.md`) needs from, and gives to, DYN, FU, EF, AF, NAV, TM and the TST, and the answers to the needs that C1, C2, C3, C6 and C7 addressed to C4. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2 as changed by CR-B3-39 (D73). "Boundary ICD" is the vehicle-model boundary ICD, whose home I1 decides (IN-B1-01, TT-720). C4 did not coordinate with the other agents directly (C5 drafts in parallel); I1 resolves these needs. New needs are IN-C4-nn: 01–09 DYN, 10–19 FU, 20–29 EF, 30–39 TM, TST and I1, 40–49 AF, 50–59 NAV.

## 1. Summary of the FC interfaces

| Interface | Direction | Data (SI) | Rate | Defined in | FC record |
| --- | --- | --- | --- | --- | --- |
| I-13 | AF → FC | Six axis references (reference value, rate and acceleration; the regulated quantity of each translational axis) or the off value | Each control frame | ICD-FC-AF (new file `icd/ICD-FC-AF.md`) | L2-AER-FC-020 |
| I-09 | DYN → FC | Vehicle state of the frame-start step: position, velocity, attitude (quaternion, Euler angles), body rates, vehicle acceleration | Each control frame | Boundary ICD | -030, -040 |
| I-45 (extended) | DYN → FC | Gear state: gear position (extended, retracted, in transit) and on the ground or not (CR-C4-02) | Each control frame | Boundary ICD | -030, -210 |
| I-05 | FU → FC | Mass properties: vehicle mass and the three principal moments of inertia (no centre-of-gravity item, IN-C2-19) | Each control frame (the frame-start step) | Boundary ICD | -030; L3-TR-090, -RO-060 |
| I-22 | TST → FC | Flight-control-law design selection | Start of run | ICD-AER-TST | -050 |
| I-21 | TST → FC | Vehicle parameter set: P-EF-100 to -130 (number, directions, points of application, output limits) | Start of run | ICD-AER-TST | -060 |
| I-11 | TR, RO → AL | Six axis demands: a force along and a moment about each body axis (N, N·m) | Each control frame | Internal to FC (L3) | L3-AL-010 |
| I-12 | FC → EF | Effector commands (one per effector, N, along its direction of action) and the effector activation state (on, off) | Each control frame, held for the frame | Boundary ICD | -070, -080, -160, -190, -200 |
| I-33 | FC → TM | Axis references as received, axis demands, effector commands, effector activation state | Each control frame | ICD-AER-TST | -250 |

FC gives nothing to AF, NAV, FCP or the vehicle model other than I-12. FC takes no mode information from AF, no fuel state, no wind and no navigation quantity.

## 2. Answers to the needs addressed to C4

| Need | Answer | FC record |
| --- | --- | --- |
| IN-C1-30 (the vehicle state of the frame-start step to FC) | Accepted: FC uses it as given and holds no estimate of it. | -040 |
| IN-C1-32 (turn at speed needs a lateral force m·v·ω; AF bounds the heading rate; the acceleration enters P-SYS-410, P-AF-200, P-SYS-120, P-SYS-540) | Accepted. With the translational references in frame V (DD-290) a heading change at constant velocity is a rotation of FC's force resolution and not a manoeuvre of the translational axes (DD-300), and a velocity vector that turns with the heading (Heading mode) is AF's reference acceleration, which FC follows by feed-forward. The cross-axis tolerance P-SYS-540 is stated along the reference axes (CR-C4-03). | -120, -140 |
| IN-C1-33 (drag for the budgets, isotropic, sea-level density) | Used for the checks in `issues.md` §5; no change. | L3-TR-080, -100 |
| IN-C1-34 (gust bounds: wind rate at most (π/2) P-SYS-560 / P-SYS-570) | Used: the transient allowance check of `issues.md` §5 and L3-AER-FC-TR-080. | L3-TR-080 |
| IN-C1-35 (the sensed acceleration is not part of the boundary state) | Accepted: FC does not read it; FC limits the vehicle acceleration it demands instead (DD-320). | -030, -130 |
| IN-C1-43 (liftoff rule: the upward control force must stay at most the weight from the frame in which a contact can occur) | Accepted and met by L2-AER-FC-210 (the cap while the gear is extended and the vertical reference rate is below zero). The contact itself is not seen by FC (the gear state reaches it at the next frame start), which is why the cap rests on the gear position and on the reference and not on the on-ground flag. Needs AF's Land references (IN-C4-43). | -210 |
| IN-C2-41 (mass properties at the frame start; the mass falls by a negligible fraction within a frame) | Accepted: FC reads the vehicle mass and the principal moments of inertia of the frame-start step. | L3-TR-090, -RO-060 |
| IN-C3-20 (effector command = a force in N along the direction of action, one per effector, plus the activation state; the layout comes from the parameter set) | Accepted. | -060, -070 |
| IN-C3-21 (FC does not rely on output beyond the limits; its priority rule acts beyond the box) | Accepted: FC never commands beyond the limits and limits a demand beyond the box component by component. | -160, -170; L3-AL-020 |
| IN-C3-22 (the lag is in the loop: P-SYS-310 + P-EF-010 ≤ P-SYS-480 with 0.02 s of margin) | Accepted: the baseline law is designed with the lag and the frame delay (DD-350); the gust allowance needs an effective compensation delay of at most about 0.18 s (`issues.md` §5). | L3-TR-080 |
| IN-C3-23 (inside the box each component can be allocated and saturated on its own) | Accepted and used: the priority rule is independent limiting per component (DD-310). | L3-AL-020 |
| IN-C3-24 (FC's child of L1-AER-360: the hold commands the weight within P-FU-100) | Accepted as L2-AER-FC-240; needs CR-C4-01 (L1-AER-360 is not allocated to FC). | -240 |
| IN-C3-25 (confirm a heading-rate onset of at least 0.5 s, which P-SYS-420 = 2000 N·m allows) | **Confirmed.** FC asks for no onset faster than 0.5 s: the rotational settling time P-FC-090 is 4 s, the heading rate tolerance is 0.005 rad/s, and RO never demands more than P-SYS-420 (the box). | L3-RO-030, -050 |
| IN-C3-26 (who sets the effector activation state) | FC sets it from the off value alone: off while the axis references carry the off value, on while they do not (DD-340). AF supplies the off value and nothing else. | -190, -200 |
| IN-C3-30 (Takeoff and Land state when the effectors switch on and off) | Through the off value: Takeoff replaces it by axis references in the engagement frame; Land restores it in the frame that shows the gear on the ground (IN-C4-42, IN-C4-43). After fuel exhaustion EF gives zero whatever FC commands (D68). | -190, -200 |
| IN-C6-11 and IN-B1-03 (does AF need the horizontal position, or are the ICD-FC-AF horizontal references "hold the present position" commands that FC resolves?) | **AF needs it.** The references are absolute; FC resolves no "hold" command and latches nothing, because a latched state in FC would be mode information (L1-AER-420). AF takes the reference position from NAV (ICD-NAV-AF) and sends it. | -020 |
| IN-C6-20 (FC receives nothing from NAV) | Confirmed. | -030 |
| IN-C7-20 (give TM the axis references as received, the six axis demands, the effector commands and the activation state) | Accepted. | -250 |
| IN-C7-32 (the first control frame starts at step zero; each output sample step is a frame start) | Confirmed: the effector commands of the frame that starts at step zero are present at step zero. | -070 |

## 3. Needs on DYN (C1)

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-01 | The vehicle state of the frame-start step (I-09) carries, in SI and in the frames of CONVENTIONS: the position (north, east, altitude), the velocity in frame V, the attitude quaternion with the Euler angles derived by CV-260, the body rates (p, q, r) and the vehicle acceleration in frame V (glossary *Vehicle state*). | FC resolves forces with the attitude and uses the measured acceleration for the disturbance compensation of the gust allowance (DD-350). | -040; L3-TR-080 |
| IN-C4-02 | **Gear state to FC (I-45 extended to F-05, F-06; CR-C4-02):** the gear position (extended, retracted, in transit) and whether the vehicle is on the ground, at the start of each control frame, in the boundary ICD. L2-AER-DYN-340 limits the data to the flight software to the vehicle state and the gear state and L1-AER-430 lists the gear state, so only the FA §3.2 destination list changes. FC uses only "extended" (L2-AER-FC-210). | The descent cap. | -030, -210 |
| IN-C4-03 | MS-DYN §9.6 (the liftoff rule) stays as written: the first step at which the upward component of the control force exceeds the weight. | L2-AER-FC-210 rests on it; the margin P-FC-120 covers the rounding. | -210 |
| IN-C4-04 | The vehicle acceleration and the sensed acceleration of each step are in the TST recording of every run (the sensed acceleration already goes to TM, IN-C1-36). | The tests of L3-TR-070, -080, -100 read them. | L3-TR-070 |

## 4. Needs on FU (C2)

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-10 | The mass properties of I-05 give, at the frame-start step, the vehicle mass (the one DYN integrates, L2-AER-FU-140) and the three principal moments of inertia (zero products, D61); no centre-of-gravity item (IN-C2-19). | Force and moment demands scale with the mass and the inertia (D38, D65). | L3-TR-090, -RO-060 |
| IN-C4-11 | The consumption relationship of MS-DYN (DD-110) in a form an analysis can call on recorded commands (control force and moment in, fuel mass flow out), for AN-FC-240. | The analysis of the FC share of P-FU-100. | -240 |
| IN-C4-12 | FC takes no fuel state; the exhaustion indication stays with AF and FCP. | D68: nothing to do in FC. | -030 |

## 5. Needs on EF (C3)

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-20 | The number of effector commands, their order and their sign are those of P-EF-100 to -130; a positive command acts along +d_i (CV-330); the commands are held for the control frame (L2-AER-EF-150). The authority box is stated in the body frame: the force along x_B and y_B within P-SYS-410, along z_B from minus P-SYS-400 to P-SYS-410 (z_B points down), the moment about each axis within P-SYS-420. | AL needs the sign and the asymmetry of the box (the upward bound is P-SYS-400). | L3-AL-010, -020 |
| IN-C4-21 | Confirm that L2-AER-EF-210 gives each effector output exactly zero from the first step of the control frame that carries the activation state off (no lag in the off direction), and that on from off starts the lag from zero. | The timing of L2-AER-FC-190 (zero within P-SYS-310 of the contact). | -190, -200 |
| IN-C4-22 | The authority box (L2-AER-EF-330) is the guarantee that AL's limiting rule uses. A different layout (DM-FC-060, AN-FC-AL-010) has to meet it too: the second layout is checked by AN-EF-330 before FC uses it. | L3-AL-020. | -060; L3-AL-010, -020 |

## 6. Needs on AF (C5)

C5 drafts in parallel and could not be consulted; these are C4's needs and proposals for ICD-FC-AF, to be reconciled by I1.

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-40 | **ICD-FC-AF content (DD-290).** At the start of each control frame, either the off value or six axis references: for the north, east and vertical axes of frame V, a reference value (position, altitude), a reference rate (velocity, vertical speed, positive up) and a reference acceleration, with the regulated quantity of each axis (position or velocity); for roll, pitch and heading, a reference angle (rad; heading as a direction angle, CV-520), the reference body rate about the axis and the reference acceleration. SI, one set per frame, absolute (no "hold" command). | The one interface between AF and FC (D15, L1-AER-420). | -020 |
| IN-C4-41 | **Continuity.** The three parts of a reference are consistent (the rate is the derivative of the value, the acceleration of the rate); AF shapes them so that the translational reference acceleration stays within P-AF-200, the vertical acceleration within P-AF-230 and the heading rate within P-SYS-270; steps happen only at a mode change or a new selection, and at a change of the regulated quantity of an axis the new reference value is where the vehicle will be (no step beyond the tolerance). A velocity vector that turns with the heading (Heading mode) is a reference acceleration of v·ω in the reference. | The premises of L2-AER-FC-140 and of the tracking tolerances. | -100, -110, -140 |
| IN-C4-42 | **Takeoff.** In the engagement frame AF replaces the off value by axis references: the reference position is exactly the position on the ground (the guidance share of L1-AER-960 is zero, L2-AER-FC-220), the vertical regulated quantity is the velocity at the climb rate P-AF-240, the heading is the present heading, pitch and roll are zero. FC switches the effectors on in that frame. | L2-AER-FC-200, -220. | -200, -220 |
| IN-C4-43 | **Land.** AF extends the gear before the descent, holds the vertical reference rate at zero in the Hover that precedes it (a negative rate with the gear extended caps the upward force), sends a vertical reference rate of minus P-AF-240 for the descent, and sends the off value in the control frame whose gear state shows the vehicle on the ground (AF runs before FC in the frame, FUNCTIONAL_ANALYSIS §4.2). | L2-AER-FC-190, -210. | -190, -210 |
| IN-C4-44 | **Ground start.** The first control frame of a run on the ground carries the off value (the recommendation for #60: no mode is active on the ground at the start). An airborne test start (D73, B3-1) carries axis references from step zero. | L2-AER-FC-190, -200. | -190, -200 |
| IN-C4-45 | **Tolerance closure.** The AF tolerances include the FC shares: P-AF-110 ≥ P-FC-030 plus the AF share; P-AF-090 ≥ P-FC-050 plus the AF share; P-AF-130 ≥ P-FC-070 plus the AF share; P-AF-170 ≥ P-FC-040 and P-AF-170 ≤ P-SYS-510; P-AF-160 + P-FC-010 ≤ P-SYS-450; P-AF-200 + P-FC-020 ≤ P-SYS-440; P-AF-180 is used by FC as it stands. | The budgets of FUNCTIONAL_ANALYSIS §7. | -100, -110, -130, -140 |
| IN-C4-46 | **Horizontal position from NAV** (answer to IN-C6-11): AF takes the horizontal position from ICD-NAV-AF to build the reference position; FC does not use NAV. | L2-AER-FC-020. | -020 |

## 7. Needs on NAV (C6)

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-50 | None. FC reads the vehicle state directly (FUNCTIONAL_ANALYSIS §5.3, IN-C6-20). Altitude and vertical speed on the vertical axis are the CV-430 and CV-490 quantities, the same as NAV's definitions. | One definition of each quantity. | -030 |

## 8. Needs on TM (C7), the TST and I1

| ID | Need | Why | FC records |
| --- | --- | --- | --- |
| IN-C4-30 | **Test reference source:** a test autoflight variant, selected through the configuration, that sends scripted axis references and the off value through ICD-FC-AF in place of the mode logic (no mode information). It is the open-loop source for TP-FC-070 to -260 and for the L1-AER-370 and -380 tests; it is also the demonstration variant of L1-AER-410. TST requirement for when the plan covers the TST (D44). | FC tests need reference steps without a mode. | -050, -100 to -260 |
| IN-C4-31 | **TST recording for analysis runs:** at each control frame the axis references as received, the axis demands, the effector commands and the activation state; at each simulation step the effector commands (as IN-C3-31); and the vehicle state with its acceleration and the sensed acceleration, without changing the Aeronef configuration. (If P-TM-010 equals P-SYS-310 the operational data already hold the frame values, L2-AER-FC-250.) | AN-FC-240, AN-FC-AL-010, TP-FC-080, L3-TR-070, -080, -100. | -080, -240, -250 |
| IN-C4-32 | **ICD-AER-TST:** operational data signals "axis references (as received)", "axis demands" (three forces in N, three moments in N·m, body frame), "effector commands" (one per effector, N) and "effector activation state" (IN-C7-20). | L1-AER-630. | -250 |
| IN-C4-33 | **Boundary ICD:** the FC items (I-09, I-45 extended, I-05, I-12): vehicle state elements, gear state, mass properties, effector commands array of n forces in N (n from the parameter set) and the activation state. | L1-AER-430. | -030 |
| IN-C4-34 | **ICD-FC-AF:** a new file `icd/ICD-FC-AF.md` written at integration from IN-C4-40 to -44 and the AF counterpart. | L1-AER-420. | -020 |
| IN-C4-35 | **ICD-AER-TST configuration:** the flight-control-law design selection with identifier and version (I-22), carried to the configuration identity of the operational data (L1-AER-650). | L2-AER-FC-050. | -050 |
| IN-C4-36 | **Second compliant layout:** a vehicle parameter set with another effector layout that meets L2-AER-EF-330 (for example twelve one-way effectors in opposed pairs), as a fixture for DM-FC-060, AN-FC-AL-010 and TP-FC-AL-020. Written at V1 and checked by AN-EF-330. | Shows that FC is layout-independent. | -060 |
| IN-C4-37 | **Budget closure at I1:** the closure rules in `issues.md` §5 and IN-C4-45, with the TBR values of `param_proposals.md`; TT-650, TT-860 checks (done in `issues.md` §5). | FUNCTIONAL_ANALYSIS §7. | -100, -140, -220 |

## 9. ICDs touched

| ICD | FC items |
| --- | --- |
| ICD-FC-AF (new, `icd/ICD-FC-AF.md`) | The six axis references and the off value (IN-C4-40 to -44) |
| Vehicle-model boundary ICD (IN-B1-01, TT-720) | Vehicle state, gear state (I-45 extended), mass properties in; effector commands and the activation state out (IN-C4-33) |
| ICD-AER-TST | Control-law design selection; the FC operational data signals; the vehicle parameter set (IN-C4-32, -35) |
