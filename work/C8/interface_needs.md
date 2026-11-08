# C8 — Interface needs (FCP)

What the flight control panel (FCP, `work/C8/L2_FCP.md`) needs from, and gives to, AF (C5), NAV (C6), TM (C7), FU (C2), DYN (C1) and the TST, and the answers to the needs that earlier agents addressed to C8. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2. C4 to C7 draft in parallel; C8 did not coordinate with them, and I1 resolves these needs. Written at branch c1_c2, commit 55c6c29.

## 1. Summary of the FCP interfaces

| Interface | Direction | Data | Unit side | Rate | Defined in | FCP record |
| --- | --- | --- | --- | --- | --- | --- |
| I-26 | TST → FCP | Crew selections: eight mode selections, four selected values, each with its timestamp (CV-840) | Crew units (CV-760 group 1) | As made; taken at each control frame | ICD-AER-TST (crew interface) | -010, -020, -080 |
| I-28 | TST → FCP | Initial selected value of each of the four selectors | Crew units | Run start | ICD-AER-TST (initial condition) | -520, -530 |
| — | FCP → TST | Initial-condition error naming a selector and its value | Crew units | Run start | ICD-AER-TST | -530 |
| I-19 | FCP → AF | Ordered mode selections of the frame; SI target of each selector; set of selectors accepted in the frame | SI | Each control frame | ICD-FCP | -050, -080, -090 |
| I-16 | AF → FCP | Annunciation content: mode state, targets in use (each with its quantity), landing gear position | SI | Each control frame | ICD-FCP | -060, -320 to -340 |
| I-18 | NAV → FCP | Altitude, vertical speed, horizontal speed, heading, track, each with its validity | SI | Each control frame | ICD-FCP, by reference to ICD-NAV-AF | -060, -360, -370 |
| I-06 | FU → FCP | Fuel state: remaining fuel mass, low-fuel indication, fuel-exhaustion indication | SI | Read at each control frame start | ICD-FCP, by reference to the boundary ICD | -060, -070, -380 to -410 |
| I-42 | FCP → TST | Crew interface output: four annunciation items, four selector readouts, six indications (with validity) | Crew units (CV-760 group 2) | Each output sample | ICD-AER-TST (crew interface) | -030, -040, -300 |
| I-36 | FCP → TM | Each crew selection taken: timestamp, item, selected value and unit, accepted or not, SI target | Both (CV-760 group 4) | Each selection | ICD-AER-TST (operational data) | -500 |
| I-38 | FCP → TM | The annunciations and selector readouts presented | Crew units, as shown | Each output sample | ICD-AER-TST (operational data) | -510 |

FCP gives the vehicle model nothing and takes from it only the fuel state (L2-AER-FCP-070).

## 2. Answers to the needs addressed to C8

| Need | Answer | FCP record |
| --- | --- | --- |
| IN-C2-43 (fuel state to FCP; which alert at exhaustion; the alert labels) | FCP converts the remaining fuel mass to lb by the CV-750 factor, rounds it to [P-FCP-010] and indicates it. The fuel alert is one annunciation item: LOW FUEL while the low-fuel indication is set without exhaustion, FUEL EXHAUSTED while the exhaustion indication is set (it replaces LOW FUEL, as C2 suggested), no label otherwise (DD-C8-04). Labels as in CONOPS §4.5. FU's share of [P-SYS-470] stays zero; FCP's is [P-SYS-310] + [P-TM-010] from the step at which the indication sets. | -380, -390, -400, -410, -310 |
| B1 IN-B1-08 (ICD-FCP closed list) | Confirmed and refined: FCP → AF as §1 I-19; AF, NAV, FU → FCP as §1. Crew units stay inside FCP. | -050, -060 |
| B1 C8 row (crew interface, units, resolutions, initial values, frame, panel content) | Each item is covered: see the coverage table of `L2_FCP.md`. | — |
| B3 impact list, C8 (TAKEOFF and LAND buttons; gear labels; lowest selectable altitude; what the panel shows on the ground) | TAKEOFF and LAND are mode selections (-020). Gear labels GEAR DOWN, GEAR UP, GEAR TRANSIT (-340, C8-Q03). The lowest selectable altitude is the lowest multiple of [P-AF-010] at or above [P-SYS-210] + [P-DYN-030]/2: 20 ft, with no rounding rule or parameter of its own (-120). On the ground the panel shows the selector readouts of the initial condition, the altitude indication of the centre of gravity (11 ft with P-DYN-040 = 1.4 m; 3.4 m / 0.3048 = 11.15 ft), zero vertical and horizontal speed, track not valid, the heading, the fuel, GEAR DOWN and an empty mode state if no mode is active. | -020, -120, -340, -360, -370 |
| CONOPS SC-130 TBR "the gear labels (C5, C8)" | FCP proposes to own them (the gear position is not a mode); C5 to confirm (IN-C8-07). | -340 |
| CV-580 / CR-B1-13 (behaviour when a quantity is invalid: NAV, AF, FCP) | FCP shows the indication as not valid, with no shown value, using NAV's validity; no FCP threshold. | -370 |
| CV-780 (display resolution and rounding) | Shown value = SI value ÷ CV-750 factor, rounded half away from zero to the display resolution; heading and track wrapped so that a full turn shows as zero; selector readouts unconverted (DD-C8-03). | -210, -220, -350 |

## 3. Needs on AF (C5) and AF_MODE_LOGIC

| ID | Need | Why | FCP records |
| --- | --- | --- | --- |
| IN-C8-01 | **Mode selections.** AF receives at each control frame the ordered list of mode selections that FCP took (any of the eight, whatever the mode state) and decides for each whether it arms, becomes active or is refused. FCP filters nothing. AF_MODE_LOGIC states the outcome of each mode selection in each mode state, including Land when Hover is not active, Takeoff when airborne or with no fuel, and any mode selection on the ground. | One place for the mode logic (D15, D33). | -050, -080 |
| IN-C8-02 | **Selector targets.** AF receives at each control frame the SI target of each of the four selectors (heading in [0, 2π) rad; horizontal speed ≥ 0 m/s, a ground speed; altitude in m, CG altitude, at least [P-SYS-210] + [P-DYN-030]/2; vertical speed in m/s, signed, positive up, from −[P-SYS-250] to [P-SYS-240], zero possible) and the set of selectors accepted in that frame. A refused selection is not reported as accepted, and the target is unchanged. | AF needs the value to fly and needs to know when the crew set it (N-090). | -050, -100 to -140 |
| IN-C8-03 | **Standard versus selected vertical speed.** The standard vertical speed [P-AF-220] is not a selector value; FCP holds whatever the crew last selected (or the initial selected value). AF decides when Go to altitude uses [P-AF-220] and when the selected vertical speed ("until the crew selects another", D56), from the "accepted in this frame" set. AF also decides what Vertical speed does with a zero, or a wrong-signed, selected vertical speed (SC-040 TBR; C8-Q08). | D56, D70; SC-020, SC-110 legs 4 and 6. | -050, -130 |
| IN-C8-04 | **Same-frame order.** Within one frame, AF evaluates the mode selections in the order given, each with the selector targets of the end of the frame's intake (DD-C8-01). A target set and a mode engaged in the same frame therefore act together. | Reproducibility; SC-060 step 1. | -090 |
| IN-C8-05 | **Annunciation content.** At each control frame AF gives FCP: the mode state (the active horizontal and vertical modes, or the both-axes mode; the armed modes; whether autoflight is engaged), each target in use with its quantity (altitude, vertical speed, horizontal speed or heading) in SI, and the landing gear position (extended, retracted, in transit) from the gear state. AF_MODE_LOGIC assigns one label to each mode in each state (armed, active); FCP shows these labels unchanged. An empty mode state (no mode active, for example on the ground) is a valid content. | L1-AER-470 (labels are C5's), L1-AER-880. | -320, -330, -340 |
| IN-C8-06 | **No data path into the selectors.** AF does not reset or synchronise a selector (no "heading sync" on a mode change, no reset of the vertical speed selector to the standard). A target AF sets for itself (the altitude held by Altitude hold engaged directly, the reference position, the hover height, the standard vertical speed) goes in the annunciation content as a target. If C5 needs a selector reset, that is a new AF → FCP item and needs a change to L1-AER-880. | L1-AER-880 closes AF → FCP to annunciation content. | -150, -330 |
| IN-C8-07 | **Labels owned by FCP.** FCP proposes to own the gear-position labels (GEAR DOWN, GEAR UP, GEAR TRANSIT) and the fuel alert labels (LOW FUEL, FUEL EXHAUSTED); C5 owns the mode labels. C5 confirms or takes the gear labels into AF_MODE_LOGIC (C8-Q03). | CONOPS SC-130 TBR; IN-C2-43. | -340, -390, -400 |
| IN-C8-08 | **Initial condition.** The four initial selected values are FCP's item of the initial condition (crew units, checked as selections, C8-Q05). The initial mode state and any target AF sets for itself (for an airborne test start) are AF's. At the first frame FCP gives AF the SI targets of the initial values, with no accepted selection. | L1-AER-660; TT-610. | -520, -530 |
| IN-C8-09 | **No Hover and no disengage selection.** The panel has no Hover selection and no autoflight disengage selection (C8-Q04). AF_MODE_LOGIC states how the crew leaves Hover (by another mode selection) and how autoflight disengages, if ever (fuel exhaustion, D68). | D71; CONOPS §4.3; SC-100 TBR. | -020 |

## 4. Needs on NAV (C6)

| ID | Need | Why | FCP records |
| --- | --- | --- | --- |
| IN-C8-10 | At each control frame, the altitude, vertical speed, horizontal speed, heading and track, each with its validity (CV-580, thresholds [P-NAV-010], [P-NAV-030]), in SI, to FCP through ICD-FCP: the same values and validity that NAV gives AF through ICD-NAV-AF, defined once and referenced by ICD-FCP. FCP does not need the height above the ground (it is not an indication). | One definition of each quantity (FUNCTIONAL_ANALYSIS §5.2); L1-AER-880. | -060, -360, -370 |
| IN-C8-11 | Heading in [0, 2π) and track in [0, 2π) (wrap360, CV-920). FCP wraps after rounding only. | CV-520. | -220 |

## 5. Needs on TM (C7)

| ID | Need | Why | FCP records |
| --- | --- | --- | --- |
| IN-C8-20 | Record each crew selection the panel takes, once: its timestamp, the control frame at which FCP took it, its item, its selected value and unit (for a selected value), whether FCP accepted it, and its SI target (for an accepted selected value). | L1-AER-610; CV-760 group 4. | -500 |
| IN-C8-21 | Record at each output sample the four annunciation items and the four selector readouts as presented. | L1-AER-620. | -510 |
| IN-C8-22 | Releasable or protected classification of the FCP signals is with the RVS (#69). The crew interface output is what an RVS agent sees when it operates the released Aeronef (N-400), so it is a natural candidate for releasable. | #69, D44. | -500, -510 |

## 6. Needs on FU (C2) and DYN (C1)

| ID | Need | Why | FCP records |
| --- | --- | --- | --- |
| IN-C8-30 | FU: no change. The fuel state of L2-AER-FU-210 to -240 is what FCP needs; FCP reads it at each control frame start. | IN-C2-43 answered (§2). | -060, -380 to -410 |
| — | DYN: no direct interface. The gear position reaches FCP through AF (L1-AER-470 v2). | L1-AER-430, -880. | -070 |

## 7. Needs on the ICDs (I1) and the TST

| ID | Need | Why | FCP records |
| --- | --- | --- | --- |
| IN-C8-31 | **ICD-AER-TST, crew interface (input).** The twelve crew-selection items of L2-AER-FCP-020, each with its timestamp; a selected value in its crew unit (deg, kt, ft, ft/min signed). A data item naming no listed selection, or with a malformed value, is refused at the crew interface. Two selections with equal timestamps are ordered by their order of receipt (in a script, their order in the script). Fix whether an input timestamped k first affects step k or k + 1 (CV-840); FCP takes it at the first control frame starting at or after k (FUNCTIONAL_ANALYSIS §4.2). | L1-AER-480; DD-C8-01. | -010, -020, -080, -090 |
| IN-C8-32 | **ICD-AER-TST, crew interface (output).** Four annunciation items (mode state, targets with quantity, gear position, fuel alert), four selector readouts, six indications with a validity flag each; each with its crew unit. No layout, graphics or symbology (L1-AER-510). | L1-AER-490. | -030, -040 |
| IN-C8-33 | **ICD-AER-TST, initial condition.** The initial selected value of each of the four selectors, in its crew unit (C8-Q05); the initial-condition error from FCP naming the selector and its value. | L1-AER-660; DD-C8-05. | -520, -530 |
| IN-C8-34 | **ICD-FCP.** As §1: FCP → AF (I-19), AF → FCP (I-16), NAV → FCP (I-18, by reference to ICD-NAV-AF), FU → FCP (I-06, by reference to the boundary ICD). All SI. | L1-AER-880. | -050, -060, -070 |
| IN-C8-40 | **TST test source at ICD-FCP.** For the FCP output-mapping tests, a way to run the panel with scripted annunciation content, navigation quantities and fuel state at the ICD-FCP boundary, and to record the ICD-FCP data of each control frame, as for EF (IN-C3-33). | TP-FCP-080, -090, -210 to -370. | — |
| IN-C8-41 | **TST interactive interface.** The TST shows the crew interface output to a human and takes the crew's selections into the same data items as a script (N-360, SC-230). How it is drawn is the TST's (L1-AER-510). | L1-AER-480, -490. | -010, -030 |

## 8. Offered, not required

| ID | Offer | Why |
| --- | --- | --- |
| IN-C8-50 | FCP can give TM the six indications as shown (with validity) at each output sample, beside the SI navigation quantities NAV gives TM. L1-AER-620 asks only for the annunciations; C7 decides. | Lets the RVS and the evaluators see exactly what the crew saw (CV-760 group 4). |
