# C8 — Issues, owner questions, change requests and design decisions (FCP)

Task C8 (plan §6, Phase 3): the FCP section of L2 (`work/C8/L2_FCP.md`), the flight control panel: the crew interface as data. Written at branch c1_c2, commit 55c6c29 (D1–D74). Questions are at L2 level: the panel as a subsystem; mode logic is C5's and is only named here where the panel meets it. Local IDs C8-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused).

## 1. Summary

| Item | Count |
| --- | --- |
| L2 FCP records | 36: Functional 23, Interface 10, Constraint 2, Performance 1 |
| Verification methods | Test 30, Inspection 6 |
| L1 parents covered | 15 of 15 L1 records allocated to FCP, plus L1-AER-310, -320, -330 with CR-C8-01 |
| Derived records | 0 |
| L3 records | None: each FCP record is a leaf; the next layer is the panel software (D4) |
| Parameters | 2 new (P-FCP-010 fuel display resolution, P-FCP-020 conversion tolerance); 1 stored value corrected (P-SYS-230); descriptions of P-AF-010 to -040, P-TM-050 refined |
| Owner questions | 8 (§2) |
| Change requests | 3 (§3): FCP allocation of L1-AER-310 to -330; glossary refinements; CONOPS §4.3 editorial |
| Design decisions proposed | 5 (§4), each a choice inside a record |
| Lint | 0 errors, 24 COMPOUND warnings in 21 records (judged in §6) |

**The panel content (#79, D71) in one line.** Eight mode selections (Stationary, Heading, Altitude hold, Go to altitude, Vertical speed, Go to hover, Takeoff, Land); four selectors (heading in degrees from 0 to 359, horizontal speed in knots from 0 to 300, altitude in feet from 20 to 150 000, vertical speed in feet per minute from −6000 to +6000, at the D71 resolutions); an output of four annunciation items (mode state, targets, gear position, fuel alert), four selector readouts and six indications (altitude, vertical speed, horizontal speed, heading, track, fuel), in crew units, at each output sample.

**Open TBD/TBR carried by the FCP records.** All existing register rows except the new one: TT-010 (envelope limits), TT-070 (timing), TT-120, TT-130 (fuel threshold), TT-170 (selection resolutions), TT-200 (NAV validity), TT-210 (display resolutions), TT-600 (#69), TT-670 (AF_MODE_LOGIC), TT-680 (ICDs), TT-720 (boundary ICD home), TT-740 and TT-830 (body and gear dimensions); new: P-FCP-010 and -020 (TBR, proposed row); and C8-Q01 to -Q08 below.

## 2. Questions for the project owner

Each question has a recommended answer. The records are written for the recommended answer; where another answer changes a record, the question says which.

### C8-Q01 — A selected value the panel does not accept

**Question.** A crew selection gives a selector a value outside its selectable range (for example 400 kt) or off its resolution (for example 10 005 ft). What does the panel do?

| | Option A — refuse, keep the previous value (recommended) | Option B — clamp to the range, round to the resolution | Option C — accept any value |
| --- | --- | --- | --- |
| Conversion | Exact, no rounding before conversion (CV-770, L1-AER-870) | Rounds the value before conversion, which L1-AER-870's guidance forbids | Exact |
| Envelope | Targets always inside the envelope | Inside | Targets outside the envelope reach AF |
| Tests | A script error shows as a refused selection in the operational data | A script error is hidden: the run is not what the procedure asked (D59) | AF must police the envelope |
| Crew | The readout does not change | The readout shows the clamped value | — |

**Recommended answer: A**, the same choice as DD-140 for the initial fuel. The refusal is recorded in the operational data as "not accepted" (L2-AER-FCP-500) and is visible to a human because the readout stays where it was; no separate "selection refused" annunciation is added. Under B, L2-AER-FCP-140 becomes a clamp-and-round rule and L1-AER-870 needs a change request; under C, L2-AER-FCP-100 to -140 are withdrawn and AF takes the range checks.

**Affects.** L2-AER-FCP-140, -500; DD-C8-02.

### C8-Q02 — North on the heading selector and in the shown values

**Question.** CV-520 leaves "how the crew-facing value of north is shown (for example 360 or 000)" to a display requirement. Is north selected and shown as 0, or as 360?

**Recommended answer: 0.** The selectable heading range is then the CV-520 range [0°, 360°), each heading has exactly one selected value and one shown value, and the selector, the target and the shown value use the same range with no special case; a heading that rounds to 360° is shown as 0. Alternative: the airliner habit, 360 for north (range (0°, 360°]); then 0 is refused and 360 converts to a target of zero by wrapping, which is a second special case in the conversion. The digit layout ("0" or "000") is a display format, outside the Aeronef either way.

**Affects.** L2-AER-FCP-100, -220; P-AF-040, P-TM-050 descriptions.

### C8-Q03 — Gear-position labels and who owns them

**Question.** The gear position is annunciated (L1-AER-470 v2). CONOPS SC-130 leaves "the gear labels" to C5 and C8. Which labels, and whose?

**Recommended answer: the panel's labels GEAR DOWN (extended), GEAR UP (retracted), GEAR TRANSIT (in transit).** The gear position is not a mode, so its labels sit with the other non-mode annunciations, the fuel alerts, at the panel; C5 owns only the mode labels. The three labels map one to one onto the three gear positions of the glossary. Alternatives: GEAR EXT / GEAR RET / GEAR MOVING; or C5 defines them in AF_MODE_LOGIC and passes them, in which case L2-AER-FCP-340 says "with the label that AF_MODE_LOGIC assigns" as -320 does.

**Affects.** L2-AER-FCP-340; IN-C8-07.

### C8-Q04 — No Hover selection and no autoflight disengage selection

**Question.** D71 says the panel has "the buttons that engage each mode". CONOPS §4.3 (CR-B3-32, approved D73) lists eight engage commands, without Hover. Confirm that the panel has no Hover selection and no autoflight disengage selection?

**Recommended answer: confirm both.** Hover is reached only through Go to hover or Takeoff, which arm it, and it engages when the vehicle is stationary at the hover height (D56, D69); a Hover button would only duplicate Go to hover. A disengage selection would leave a vehicle with no manual control (L0-CON-180) and no mode, so the crew leaves a mode by selecting another one; autoflight disengages only where AF_MODE_LOGIC says (for example at fuel exhaustion, D68). If the owner wants either, L2-AER-FCP-020 gains an item and C5 its logic.

**Affects.** L2-AER-FCP-020; IN-C8-09.

### C8-Q05 — Initial selected values in crew units

**Question.** L1-AER-660 gives "targets" in the initial condition, and the panel holds them as the initial selector values (FUNCTIONAL_ANALYSIS I-28). Are they given in crew units, as selected values, or in SI, as targets?

**Recommended answer: in crew units, as selected values, checked like a crew selection; an invalid one is an initial-condition error (DD-C8-05).** The readouts then start exact (an SI target converted back to ft or kt is not, in general, a multiple of its resolution), the same range and resolution checks apply, and the run is what the procedure asked for (DD-140, D59). The targets that AF sets for itself (an airborne test start in Altitude hold, for example) stay AF's item of the initial condition. Alternative: SI targets converted back and rounded to the selection resolution, which is a rounding the panel otherwise never does.

**Affects.** L2-AER-FCP-520, -530; IN-C8-08, IN-C8-33.

### C8-Q06 — Fuel display resolution and the rounding rule

**Question.** No parameter exists for the resolution of the fuel indication, and CV-780 leaves the rounding rule to FCP. Which?

**Recommended answer: [P-FCP-010] = 1 lb (TBR), and one rule for every shown value: the SI value divided by the exact CV-750 factor, rounded half away from zero to its display resolution (DD-C8-03).** Half away from zero is symmetric for a signed vertical speed and is the CV-780 example. With it, less than 0.5 lb of fuel shows as 0 lb while fuel remains; the FUEL EXHAUSTED alert, not the shown zero, marks exhaustion. Alternative: round the fuel down (the shown fuel is never more than the fuel on board), at the cost of a second rule.

**Affects.** L2-AER-FCP-210, -380; P-FCP-010.

### C8-Q07 — 300 kt must be selectable: the stored value of P-SYS-230

**Question.** [P-SYS-230] is stored as 154.333 m/s, which is 299.9994 kt. The selectable horizontal speed is bounded by it (L1-AER-310, L2-AER-FCP-110), so 300 kt, the owner's maximum (D66), would be refused. Change the stored value?

**Recommended answer: store 154.33333333333334, the nearest double to 300 kt (463/3 m/s), which lies just above it.** It is the same value in intent; only the digits change (`param_proposals.md` §2). The range check uses the exact conversion of the selected value (L2-AER-FCP-110 to -130), which is also needed at the other limits: in floating point 6000 × 0.3048 / 60 exceeds the stored 30.48, so a check on the floating-point target would refuse 6000 ft/min. Alternative: a crew-facing limit parameter of 300 kt beside P-SYS-230, which duplicates one value in two places.

**Affects.** P-SYS-230; L2-AER-FCP-110.

### C8-Q08 — Is zero a selectable vertical speed?

**Question.** The vertical speed selector runs from −[P-SYS-250] to +[P-SYS-240]. Is zero inside the range?

**Recommended answer: yes.** It is a multiple of the resolution, it keeps the range one interval, and a crew can set it to hold level flight in Vertical speed. What Vertical speed does with a zero selected vertical speed, or with one whose sign leads away from the selected altitude, is mode logic for C5 (SC-040 TBR, IN-C8-03). If the owner says no, L2-AER-FCP-130 excludes zero.

**Affects.** L2-AER-FCP-130.

## 3. Change requests

| ID | Against | Requested change | Reason | Status |
| --- | --- | --- | --- | --- |
| CR-C8-01 | L1-AER-310, L1-AER-320, L1-AER-330 (Allocated to); FUNCTIONAL_ANALYSIS §6.2 rows and count row | Allocated to "AF, FC, EF" → "AF, FC, EF, FCP" in each; the rationale adds "FCP bounds the selectable value (L2, C8)". §6.2 ticks FCP in the three rows; the FCP count becomes 18. | Each rationale makes the panel the top (or bottom) of the selectable value: "[P-SYS-230] is the top of the selectable horizontal speed", "[P-SYS-240] is the top of the selectable climb vertical speed", "the selectable altitude is bounded below by … (L2, C8)". The capability can be flown only if it can be selected, so FCP has a share, and L2-AER-FCP-110, -120 and -130 trace to these records. The same kind of change as CR-C2-04 (D74). | Proposed |
| CR-C8-02 | GLOSSARY *Annunciation*, *Flight control panel*, *Crew selection*, *Low-fuel alert*, *Selected value*, *Horizontal speed* (Fixed, D43) | As in `work/C8/glossary_proposals.md` §2. | The selector readouts are annunciations of the selected targets (CONOPS §4.3, D71), the fuel alert is one item, the panel content is now defined (#79), and the selected horizontal speed is a ground speed (D72). | Proposed |
| CR-C8-03 | CONOPS §4.3 (editorial) | "**Indications** show … the remaining fuel (lb, D9), and the LOW FUEL and FUEL EXHAUSTED alerts." → move the alerts to the annunciation sentence: "**Annunciations** show the active horizontal and vertical modes, the armed mode, the selected targets, the landing gear position … and the fuel alert (LOW FUEL, FUEL EXHAUSTED)." | The glossary classes the alerts as annunciations (*Indication*: "Distinct from an annunciation, which shows the autoflight state or an alert"); L2-AER-FCP-040 follows the glossary. | Proposed (editorial) |

No L1 record is unsatisfiable, and no record conflicts with the finished DYN, FU and EF sections.

## 4. Design decisions proposed

Each is a choice inside a record (no Derived record). Local IDs DD-C8-01 to -05; the orchestrator assigns DD numbers.

| ID | Decision | Alternatives considered | Rationale | Derived requirements |
| --- | --- | --- | --- | --- |
| DD-C8-01 | One intake per control frame: the panel takes each selection timestamped after the previous frame start and at or before this one; within the frame it applies each selected value first, then gives autoflight the mode selections in timestamp order (receipt order for equal timestamps) with the selector targets of the end of the intake. | Interleave strictly, giving AF a target per mode selection; take selections at each simulation step. | One AF evaluation per frame (DD-010); deterministic (L1-AER-690); a target set and a mode engaged in the same frame act together, whatever their order within 20 ms, which no crew can tell apart. | — (choice inside L2-AER-FCP-080, -090) |
| DD-C8-02 | A selected value outside its selectable range or off its selection resolution is refused; the selector keeps its value; the refusal is recorded. Range checks use the exact CV-750 conversion. | Clamp and round; accept anything; check the floating-point target. | CV-770 (no rounding before conversion); D59 and DD-140 (no hidden script errors); the exact check keeps exact crew limits (150 000 ft, 6000 ft/min, 300 kt) selectable. | — (choice inside L2-AER-FCP-100 to -140) |
| DD-C8-03 | Shown value = SI value ÷ exact CV-750 factor, rounded once, half away from zero, to the display resolution; heading and track that round to a full turn are shown as zero; selector readouts are the selected value, unconverted. | Truncation; round half to even; north as 360; readouts converted back from the target. | One rule, symmetric for signed values, the CV-780 example; one shown value per direction; exact read-back of what the crew set. | — (choice inside L2-AER-FCP-210, -220, -350) |
| DD-C8-04 | The fuel alert is one annunciation item: FUEL EXHAUSTED while the exhaustion indication is set, LOW FUEL while only the low-fuel indication is set, no label otherwise. | Two independent alerts, both shown at exhaustion. | The crew sees the more severe state; one item, one label (IN-C2-43, C2's suggestion). | — (choice inside L2-AER-FCP-390 to -410) |
| DD-C8-05 | The initial condition gives each selector's initial selected value in its crew unit; the panel checks it as a selection, and an invalid one gives an initial-condition error naming the selector and the value. | SI targets converted back; panel defaults. | Exact readouts from the start; the same checks; the run is what the procedure asked (DD-140, D59). | — (choice inside L2-AER-FCP-520, -530) |

## 5. Other findings and notes for I1

1. **Lowest selectable altitude.** The B3 impact list asked whether the bound (11.56 ft as a CG altitude) rounds up to 20 ft. The record states the bound as [P-SYS-210] + [P-DYN-030]/2 on the exact conversion, so the lowest multiple of 10 ft at or above it, 20 ft, is selectable and 10 ft is not, with no rounding rule and no parameter of its own; it follows any change of the body diameter (TT-740, 2026-11-30).
2. **Floating point at the limits.** 150 000 ft × 0.3048 is exactly 45 720 in double precision, but 6000 × 0.3048 / 60 is 30.480000000000004 > 30.48, and 300 kt is 154.33333333333334 m/s > 154.333. Hence the exact-conversion rule (DD-C8-02) and C8-Q07.
3. **Resolution consistency.** Each selection resolution is a multiple of its display resolution (10/1 ft, 100/10 ft/min, 1/1 kt, 1/1°), so a target from a selected value is annunciated as the selected value. The P-AF descriptions should say so (`param_proposals.md` §2), so that a later change keeps it.
4. **Timing.** FCP share of [P-SYS-470] is [P-TM-010] for AF content and selections (FUNCTIONAL_ANALYSIS §7.5). For the fuel alerts the panel also carries the wait to the next frame start: [P-SYS-310] + [P-TM-010] = 0.04 s with the proposed values, inside 0.5 s.
5. **Altitude on the ground.** The altitude indication at rest on the gear is the CG altitude, [P-DYN-030]/2 + [P-DYN-040] = 3.4 m = 11 ft, not zero (CV-430). A reader expecting 0 ft on the ground should be told so in the operating manual (after the baseline; not written here).
6. **No conflict with DYN, FU, EF.** FU-210 to -240 give exactly the fuel state FCP needs; DYN has no FCP interface; EF none.
7. **Annunciation labels in statements.** L2-AER-FCP-340 and -390, -400 carry their labels in the statement (as METHODOLOGY §8.5 does for LOW FUEL); if the owner changes a label, only the statement changes.

## 6. Self-check (METHODOLOGY 13.1, 13.2)

**13.1, each record:**

- [x] One "shall", one subject (the flight control panel), one thought. The 24 COMPOUND warnings (21 records) are: closed enumerations of the panel content or of an interface (-020, -030, -040, -050, -060, -230, -360, -500, -510, -540); one range with its two limits (-120, -130); one window with its two ends or one order with its tie-break (-080, -090, -300); one computation with its steps (-210: divide and round; -220: range and wrap); a three-way label map (-340); one alert condition with its exclusion (-390); one error item with its content (-530); "an input or a selected value" as one trigger (-310). None is a tree of cases (D30).
- [x] Subject is the element at this level, never the crew.
- [x] EARS: ubiquitous (most), state-driven (-370, -390, -400, -410), event-driven (-080, -090, -200, -310, -520), unwanted behaviour (-140, -530).
- [x] Every quantity is a parameter ID or a CV reference; no number in a statement (lint). Crew units appear only in selection and presentation records (CV-760 groups 1, 2, 4).
- [x] No vague terms, escape clauses, open lists or absolutes (lint).
- [x] Solution-free: no device, layout or format (L1-AER-510); the intake order, refusal, rounding and alert rules are behaviour visible at the interface, with their choices in DD-C8-01 to -05.
- [x] Terms in the glossary or proposed (`glossary_proposals.md`); quantities per CONVENTIONS (CV-430, CV-480, CV-490, CV-520 to CV-540).
- [x] Rationale, parent and source on each record; a sufficiency argument for each parent.
- [x] Verification method, procedure ID and success criteria on each record.
- [x] Criticality "Not assessed"; each TBD/TBR item has an owner and a closure.

**13.2, the set:**

- [x] Each of the 15 allocated L1 parents is covered, with a sufficiency argument (coverage table at the head of the section), plus L1-AER-310 to -330 with CR-C8-01.
- [x] No duplicates or conflicts. The readout (-350, what the crew set) and the target annunciation (-330, what the modes use) are different items for different purposes. -140 (refused crew selection) and -530 (refused initial value) differ because there is no previous value at the start.
- [x] Types considered: functional, performance, interface, constraint. No model-fidelity item (the panel has no physics); no documentation item (the ICDs are written at I1). Failure handling deferred (tailoring).
- [n/a] Hazard rows and fault injection: deferred (tailoring).
- [x] Interfaces: each FCP interface has an FCP record and a counterpart or a need (FU-240 exists; AF, NAV, TM needs in `interface_needs.md`; ICD items IN-C8-31 to -34).
- [x] No Derived record.
- [x] Trace checks: §7.
- [n/a] Manual sections: none yet (after the baseline).

## 7. Check results (scratch copy of the repository, outside the worktree)

Run with the draft assembled into a copy of `requirements/L2.md` (`tools/assemble.py L2 --root <copy>`); the worktree files were not changed.

| Check | Result | Meaning |
| --- | --- | --- |
| `lint.py --file work/C8/L2_FCP.md` | 0 errors, 24 warnings (COMPOUND) | Judged in §6 |
| `trace_check.py` | 14 errors, all CHILDLESS (22 before FCP) | The 8 cleared are L1-AER-470, -480, -490, -500, -610, -620, -680, -870. The 14 left are allocated only to FC, AF, NAV or TM (C4 to C7). No ORPHAN, NO-PARENT or DERIVED error from FCP. |
| `param_check.py` | 3 PARAM-MISSING (P-FCP-010 in -210 and -380, P-FCP-020 in -200); PARAM-UNUSED warnings on AF parameters and P-SYS-290 are pre-existing | Clears when I1 merges `param_proposals.md` §1 |
