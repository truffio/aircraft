# B3 — Impact list: C1/C2 rework and tasks not yet written (D69)

Input to the C1/C2 rework that follows the owner's approval of the B3 change requests (TT-840), and to tasks C3 to C8 and I1. The list merges the "D69 impact" of `reviews/G2/inspection_C1_C2.md` §6 (marked **G2 §6**) with what B3 found (marked **B3**). The G2 findings ruled by D72 are cross-referenced where the D69 rework touches the same text. G2 recommends doing the C1/C2 rework together with those findings, "with the gear in view", and re-inspecting it in one delta inspection of DYN, FU and EF.

The CRs are in `change_requests.md`, the new L1 records in `L1_new_records.md` (L1-AER-900 to -970), the terms in `glossary_proposals.md` and the parameters in `param_proposals.md`.

## 1. DYN (C1) — L2 records

| Record | Change | Origin |
| --- | --- | --- |
| Section intro and coverage table | Add the new L1 parents L1-AER-900, -910, -920 and -950 and their DYN children. Revise rows L1-AER-050 (ground reaction), -260, -270, -280 (gear, fuel, the run goes on) and -290 ("contact adds no shock": the arrest on the ideal gear). Add L1-AER-640 (gear state) and -660 (gear position). Add DYN to F-AER-15. Refresh the G2-F23 metadata. | B3 |
| L2-AER-DYN-020 | Reword as the "integrated state" (G2-F15). The gear state is a separate DYN state item and not part of the vehicle state (new record below). | G2-F15, B3 |
| L2-AER-DYN-100 | Statement: total force = gravity force + drag force + control force + ground reaction while on the ground, "with no other contribution". | G2 §6 |
| L2-AER-DYN-110 | Statement: total moment = control moment + moment of the ground reaction while on the ground; no moment from gravity or drag. | G2 §6 |
| L2-AER-DYN-120, -180 | No change to the statements. -180 rationale: zero control force on the ground with the effectors off. | B3 |
| L2-AER-DYN-220 | Statement or a new sibling record: the vehicle geometry includes the landing gear. Contact points of the extended gear [P-DYN-040] below the lowest point of the body at level attitude, and the retracted gear inside the body (child of L1-AER-900). State the lowest point of the body used by CV-400. | G2 §6, B3 |
| L2-AER-DYN-300 | Statement: sensed acceleration = (control force + drag force + ground reaction) / vehicle mass. Criterion (2) gains a case at rest on the ground with the effectors off, where the magnitude is [P-DYN-010]. Rationale: "the state is held at the contact step, so contact adds no acceleration" → the arrest at a landing is not a computed acceleration; define what is reported at the contact step. | G2 §6, B3 |
| L2-AER-DYN-310 | Vehicle acceleration on the ground (zero) and at the contact step of a landing (report the propagated value, not the arrest: a DD-080 addition). Step-0 accelerations of a ground start with the effectors off (IN-C1-12). | G2 §6, B3 |
| L2-AER-DYN-320, -340 | -340: "limit the data it passes to the flight software to the vehicle state" → "to the vehicle state and the gear state" (L1-AER-430 v2). -320: add the gear state. New input record: take the landing gear command from AF across the vehicle-model boundary. | B3 |
| L2-AER-DYN-350 | Add the gear state, and the height above the ground if DYN supplies it to TM (otherwise NAV does, L1-AER-640). | B3 |
| L2-AER-DYN-430 | Ground start: from a ground initial condition (gear extended), set the rest state, with the CG altitude [P-DYN-030]/2 + [P-DYN-040], zero velocity and rates, level attitude at the given heading, and the on-ground state (child of L1-AER-950). An airborne start keeps the current text, subject to B3-Q1. Reject an inconsistent ground initial condition. Drop "every run starts airborne" in IN-C1-21. | G2 §6, B3 |
| L2-AER-DYN-500 | Detection: "When the altitude reaches zero" → while airborne, when the lowest point of the vehicle (the extended gear contact points, or the body; CV-400) reaches the datum plane. No detection while on the ground; detection is re-armed at liftoff. | G2 §6 |
| L2-AER-DYN-510 | Landing condition: gear extended, fuel available (FU fuel availability, I-03) and the two speed limits. Rationale: "Ideal landing (D37…)" → ideal gear (D69). | G2 §6, B3 |
| L2-AER-DYN-520 | Crash: the complement (outside the envelope, or the gear not extended, or fuel not available, D68). Rationale: the reference mission ends this way (D68). | G2 §6, B3 |
| L2-AER-DYN-530 | Event record unchanged. Rationale: the TST ends the run on a crash only (I-41). | G2 §6 |
| L2-AER-DYN-540 (Derived, DD-070) | Revise DD-070 and the record. At the contact step of a landing, report the rest state: the CG at the rest altitude, the propagated horizontal position, zero velocity, level attitude. At a crash, report the propagated state with the lowest point of the vehicle on the datum plane. In both cases the classification uses the propagated velocity. "altitude of zero" no longer holds: the CG is never at altitude zero. | G2 §6, B3 |
| L2-AER-DYN-550 | "keep the vehicle state of the contact step" → only after a crash. After a landing, the on-ground records below apply. | G2 §6 |
| L2-AER-DYN-600, -610 | "down to the contact step", "to the contact step": unchanged in meaning (the first contact after release). These checks run from an airborne check configuration, so B3-Q1 must allow airborne initial conditions at least for credibility checks. G2-F02 fix for -610. | G2 §6, G2-F02 |
| L2-AER-DYN-620, -640 | Gravity-free check configuration over [P-DYN-270] = 600 s (D72, G2-F01). No ground contact can occur there, so no gear interaction. Absolute angle bound for -640 (G2-F14). | G2 §6, D72 |
| L2-AER-DYN-700 | Section list: add "the landing gear" (or rename "the landing gear and ground contact model", L1-AER-720 v2). | G2 §6 |
| **New DYN records** (IDs from L2-AER-DYN-250 and -560 to -590, in steps of 10) | (a) Gear movement: on a change of the landing gear command while airborne, the gear reaches the commanded position within [P-DYN-050], in transit until then (L1-AER-910). (b) The gear stays extended on the ground. (c) Gear state output (gear position, on the ground). (d) At the contact step of a landing, come to rest at level attitude (L1-AER-920). (e) While on the ground, ground reaction = minus the sum of the gravity force, drag and control force and moment, with zero velocity and rates (L1-AER-920). (f) Liftoff at the first step at which the upward component of the control force exceeds the weight. (g) The gear has no mass, inertia or drag effect (L1-AER-900; with FU). (h) A new credibility check on the ground: rest with the effectors off (sensed acceleration [P-DYN-010], velocity zero, position constant in the strongest wind) and liftoff at the force threshold. | B3 |

## 2. FU (C2) — L2 records

| Record | Change | Origin |
| --- | --- | --- |
| Section intro | "keeps doing so to the end of the run": unchanged. Add: on the ground with the effectors off, the flow is zero (L1-AER-940). | B3 |
| L2-AER-FU-020, -030 | Rationale: a ground start takes its fuel from the initial condition as before. A zero-fuel run now stays on the ground. The criteria are unchanged. G2-F11 for -030. | G2 §6, G2-F11 |
| L2-AER-FU-040 | Rationale: "fuel is consumed in each flight condition, hover included" → "in each airborne condition; zero with the effectors off (L1-AER-940, D69)". DD-110 already gives zero at zero output, so no new term is needed (G2 §6). | G2 §6 |
| **New FU record** (child of L1-AER-940) | The FU subsystem shall give a zero fuel mass flow for each simulation step in which the effector outputs are zero. Test: remaining fuel mass constant over a rest on the ground (SC-130). Analysis: DD-110 form. | B3 |
| L2-AER-FU-050 | G2-F10: set the remaining fuel to zero at the exhaustion step. No D69 change. | G2-F10 |
| L2-AER-FU-080 | Criterion "from [P-FU-010] to ground contact" → "from [P-FU-010] to the end of the run (the crash after exhaustion)". The reference mission now includes a rest on the ground (leg 7a), where the summed flow is zero. | G2 §6 |
| L2-AER-FU-090, -200 | The "run started with zero fuel" cases are now a run that stays on the ground: keep the cases and say so in the rationale. | G2 §6 |
| L2-AER-FU-110 | Criterion "from fuel exhaustion to ground contact" → "from fuel exhaustion to the crash". | G2 §6 |
| L2-AER-FU-120 | G2-F05 (the CG position does not cross I-04), aligned with FA I-04 in CR-B3-39. Add the fuel availability for DYN's contact classification (I-03, D68). | G2-F05, B3 |
| L2-AER-FU-230 | TBD/TBR field: G2-F13; #59 answered by D68 (L1-AER-580 v2). | G2-F13 |
| L2-AER-FU-290 | Rationale and criterion follow L1-AER-360 v2. The simulated endurance runs from the Takeoff engagement at full fuel, then Hover (SC-110 variation). The takeoff consumption is inside [P-FU-100]. The inequality is unchanged. G2-F21 rewording. | G2 §6, G2-F21 |
| Gear and mass properties | Add to L2-AER-FU-160 (or a sibling): the landing gear has no mass and does not move the mass distribution (L1-AER-900). | B3 |

## 3. MS-DYN (C1, with C2 and C3 slots)

| Section | Change | Origin |
| --- | --- | --- |
| Header, §0 | Related: D1–D72; status words (G2-F19). | G2-F19 |
| §1 | Notation: the height above the ground `h_G` (CV-400), the ground reaction `R^L`, the gear position and the on-ground flag. | B3 |
| §2 | New §2.5 "landing gear": contact points of the extended gear, retracted gear inside the body, no mass or drag, transit time [P-DYN-050]. Also state the lowest point of the body for CV-400. P-DYN-040 is missing from §12 and §13 (G2 §6). | G2 §6 |
| §3 | Add the gear state (gear position, transit progress, on-ground flag) to the model state and to the §3.4 outputs (AF across the vehicle-model boundary; TM). §3.3 (DD-080): the acceleration reported at the contact step and on the ground. | G2 §6, B3 |
| §4 | The equations hold airborne. On the ground the state is held at rest by the ground reaction (§9); say so in §4.1. | B3 |
| §5.1 | Delete "Ground contact is not a force: it ends the run as a landing or a crash". Add the ground reaction to F and M while on the ground. Also a note that the gear gives no drag (§5.5). | G2 §6 |
| §5.3 | G2-F08. With the gear, the propagated CG at a contact step stays well above zero unless the vehicle tumbles after exhaustion; still extend layer 0 below zero. | G2-F08 |
| §8 | f = (F_c + D + R)/m; 1 g at rest on the ground. Delete "the vehicle is no longer airborne at the contact step, so no sensed acceleration is defined for the contact itself" or restate it for the arrest. | G2 §6 |
| §9 | Rewrite: (1) detection at the lowest point of the vehicle while airborne; (2) classification: landing = gear extended, fuel available and both speed limits; otherwise a crash; (3) landing: arrest to the rest state at the contact step (revised DD-070); (4) on the ground: ground reaction, held at rest, no sliding or tipping, the gear held extended; (5) liftoff condition; (6) crash: hold the state, the TST ends the run; (7) gear movement and a contact in transit; (8) event records: landing and crash (the TST ends the run only on a crash). Delete "no gear … or ground reaction force". | G2 §6 |
| §10.3 | Initial state: a ground start (rest state from the horizontal position and heading) and, per B3-Q1, an airborne start. | G2 §6 |
| §11 | C-1, C-2: release from an airborne check configuration, to the first contact. C-3, C-5: gravity-free, 600 s (D72). New C-9: rest on the ground and liftoff (static equilibrium, exact to rounding). C-8: the reference mission now includes a rest with zero flow (G2-F22: per-step data). | G2 §6, D72, B3 |
| §12, §13 | Add P-DYN-040, P-DYN-050, P-AF-210 (used for the hover-height clearance) and P-SYS-580 (pedigree only). | G2 §6 |
| §14 | Trace: add L1-AER-900, -910, -920, -950 to §2, §3, §9 and §10. | B3 |

## 4. Tasks not yet written

### C3 — EF (effectors)

- Zero output whenever the effector commands are zero (the effectors off, L1-AER-930). Step-0 outputs of a ground start are zero (IN-C1-12).
- No idle or standby output: with DD-110, zero output means zero fuel (L1-AER-940).
- Power-up response at a Takeoff from the effectors off: the command response [P-EF-010] counts in the [P-SYS-480] of L1-AER-930 and in the liftoff transient.
- EF children of L1-AER-930, -960, -970, and of L1-AER-360 v2: a hold at no more than the weight after the takeoff, within [P-FU-100] (IN-C2-23).
- P-SYS-400 (upward authority) is unchanged: a takeoff from rest needs m_max·(g + [P-AF-230]), far below the budget.

### C4 — FC (flight control)

- The off value of the axis references: command zero to every effector. No integrator wind-up on the ground. Resume cleanly at a Takeoff (L1-AER-420 v2, -930).
- Takeoff: ramp the vertical force from zero until liftoff without a jump in the sensed acceleration. Liftoff drag step in wind: show that it stays within [P-FC-020] up to [P-SYS-580] at dry mass (B3-Q2; L1-AER-960).
- Landing: after the contact step, do not lift off again while the effectors are switching off (vertical force at most the weight), within [P-SYS-480] (L1-AER-930).
- Horizontal position held through the Takeoff and the Land descent within [P-SYS-450] (L1-AER-960, -970).

### C5 — AF (autoflight) and AF_MODE_LOGIC

- Takeoff and Land, both axes (D69). Takeoff: engaged only on the ground (with fuel remaining?); effectors on; climb at [P-AF-240] with the [P-AF-230] ramps to [P-AF-210] (height above the ground, CV-400); retract the gear; Hover armed, engaging once the gear is retracted and the vehicle is stationary. Land: engaged only from Hover; extend the gear and wait until it is extended; descend at [P-AF-240]; detect the landing from the gear state; switch the effectors off (off reference) within [P-SYS-480].
- The gear command (L1-AER-910): never retract on the ground; never descend below the hover height with the gear not extended.
- Mode state on the ground: recommended "no mode active", with Takeoff the only mode accepted (#60, TT-610). Decide what happens to other selections made on the ground (rejected, or armed for after the Takeoff). Decide whether LAND stays annunciated after the landing.
- Valid initial mode states for an airborne test start (B3-Q1).
- Go to hover from below (D70), including during Land, as a go-around: does the gear retract? Crew selections during Takeoff and Land.
- Heading held in Takeoff and Land. Horizontal position held from the ground position (Takeoff) and from the Hover reference (Land).
- Annunciations: TAKEOFF, LAND and the gear position (L1-AER-470 v2); the annunciations after fuel exhaustion (D68, TT-580).
- Tolerances: [P-AF-110] in Hover with the gear extended below the 0.124 m clearance; [P-AF-170] at most [P-SYS-510] (L1-AER-970).
- Selectable altitude and the Go to altitude and V/S targets bounded below by [P-SYS-210] + [P-DYN-030]/2 as a CG altitude (with C8; L1-AER-330 v2).
- AF children of L1-AER-910, -930, -950, -960, -970 and of L1-AER-360 v2.

### C6 — NAV (navigation)

- Height above the ground (CV-400) from the altitude, the pitch angle and [P-DYN-020], [P-DYN-030], with its validity, to AF through ICD-NAV-AF (L1-AER-530 v2, -890 v2), and to TM (L1-AER-640 v2).
- Track validity on the ground (zero horizontal speed): already covered by CV-580.

### C7 — TM (operational data)

- Gear state at each output sample. Landing and crash events: a landing does not end the run, so several landings can occur in one run. Height above the ground (L1-AER-640 v2).
- The effectors off is visible through the effector commands and outputs (L1-AER-630); no new signal is needed.
- Releasable or protected classification of the new signals (#69, deferred).

### C8 — FCP (flight control panel)

- TAKEOFF and LAND engage buttons (D71; L1-AER-480 v2).
- Gear position annunciation: labels, and the crew units are not applicable (L1-AER-470 v2; optional, CR-B3-21).
- Selected altitude lower bound as a CG altitude (above) rounded to [P-AF-010]: 11.56 ft is not a multiple of 10 ft, so C8 decides whether the bound rounds up to 20 ft.
- What the panel shows on the ground: the readouts of the selected values and the indications (altitude 11 ft on the ground at rest).

### I1 — Integration

- ICD-AER-TST: ground-start initial condition (gear position, horizontal position, heading), airborne start (B3-Q1), initial-condition errors for inconsistent ground states, landing and crash events (the run ends on a crash), the wind envelope at liftoff (P-SYS-580).
- Vehicle-model boundary ICD (IN-B1-01): the landing gear command (in) and the gear state (out).
- ICD-FC-AF: the off value of the axis references.
- ICD-FCP: gear position as annunciation content.
- ICD-NAV-AF: height above the ground.
- Budget closure: P-SYS-580 against P-FC-020, P-FU-030 and P-DYN-100.

### TST (when the plan is extended)

- The run ends on a crash only. The ground start is the default initial condition. The TST applies winds within the wind envelope, including the liftoff limit.

## 5. Specifications and plan

- **FUNCTIONAL_ANALYSIS, CONOPS, CONVENTIONS, GLOSSARY:** CR-B3-29 to -41.
- **AIRCRAFT_REQUIREMENTS_PLAN.md:** §6 C5 row: "the catalogue of D56" → "the catalogue of D56 and D69 (Takeoff, Land)". §6 M8 row: add Takeoff and Land, or a new Phase 4 branch M9 "Takeoff and Land" (recommended: inside M8, since they hand over to and from Hover). C1 row: "landing gear and ground contact". C6 row already lists the height above the ground. §1 "In scope" mentions D56 only. These are plan edits for the orchestrator, not CRs.

## 6. Registers

| Register item | Change |
| --- | --- |
| TT-090 | Description: "Landing envelope at the contact step of a gear contact" (values unchanged). |
| TT-560 | Close (D71): L1-AER-480 TBD/TBR field "—". |
| TT-580 | Rewrite: "Annunciations after fuel exhaustion (D68), C5"; location AF (L1-AER-580 field "—"). |
| TT-610 | Note: "On the ground, no mode active, recommended (B3); airborne starts per B3-Q1". |
| TT-810 | Close when the owner approves this B3 set. |
| TT-820 | Close by CV-400 (CR-B3-36): the height above the ground at the lowest point of the body. |
| TT-830 | Keep (values TBR); add the location L1-AER-900, -960, -970. |
| TT-840 | Scope as in §1 to §3 of this list. |
| TT-850, TT-860 | New (`param_proposals.md` §1). |
| New field copies | One TT row per new L1 record with a TBD/TBR field: L1-AER-900, -910, -930, -950, -960, -970. Also L1-AER-360 v2 and L1-AER-660 v2. |
| DECISIONS.md | DD-070: revise for a landing (rest state) and a crash (lowest point on the datum plane). DD-110: now required by L1-AER-940 (Derived requirements column: add L1-AER-940 as a constraint on the choice). |
