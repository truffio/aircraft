# C2 rework — dispositions of the G2 findings and of the D69 impact (FU)

**Task:** C2 rework (TT-840), after the owner's rulings on the partial G2 (D72) and the approval of the B3 package (D73). **Inputs:** `reviews/G2/inspection_C1_C2.md` (findings G2-F01 to -F25, §6 "D69 impact"); `work/B3/change_requests.md`, `L1_new_records.md` (L1-AER-900 to -970), `impact_list.md` §2; `work/C3/L2_EF.md` and DD-C3-05. **Outputs:** `work/C2/L2_FU.md` (reworked), `ms_dyn_s6_s7_fu.md` (new, MS-DYN content for merge at I1), `issues.md`, `interface_needs.md`, `param_proposals.md`, `glossary_proposals.md`.

**Record counts:** 34 records. 26 changed (version 1 → 2), 3 unchanged (L2-AER-FU-210, -240, -260), 5 new (L2-AER-FU-300 to -340), 0 deleted.

## 1. G2 findings that concern FU

The owner accepted the Minor and Editorial findings as recommended (D72); Q4 ruled G2-F18.

| Finding | Severity | Disposition | Change made | Status |
| --- | --- | --- | --- | --- |
| G2-F05 | Minor | **Accepted as recommended:** the centre of gravity does not cross I-04; it stays a mass-properties item at the vehicle-model boundary; one name for the inertia item. FU provides the centre of gravity, as the body-frame origin, to FC across the boundary (I-05), not to DYN. | L2-AER-FU-120: statement and criterion drop the centre of gravity; inertia given "as its three principal moments" = DYN's "principal moments of inertia"; parent L1-AER-210 removed (covered by -150, -160, -310). L2-AER-FU-150: rationale and criterion, the item is given at the boundary only. Agreed with C1 through IN-C2-19 (C1's L2-AER-DYN-210 already says the CG does not cross). FA I-04 already aligned by CR-B3-39. MS-DYN §6.0 text proposed. | Closed on the FU side; IN-C2-19 open for C1's wording |
| G2-F10 | Minor | **Accepted as recommended:** the exhaustion step sets the remaining fuel to zero. | New L2-AER-FU-340 (set to zero at the end of each exhaustion step). L2-AER-FU-050 statement reworded around the *exhaustion step* (new glossary term), identified by comparing `fl(q·Δt)` with the fuel left, the same product the accounting subtracts, so no other step can go below zero. DD-C2-06 revises DD-130; MS-DYN §7.2.2 text. -090, -200, -230 rationales point to -340. Checked by script: no negative and no residual positive value in 10⁵ random exhaustion steps. | Closed |
| G2-F11 | Minor | **Accepted as recommended.** | L2-AER-FU-030 criterion: one initial-condition error naming the fuel mass and its value, and FU produces no output for the run; "no output sample" moved to ICD-AER-TST and the TST (IN-C2-31). Glossary *Initial-condition error*: "The run does not start" → "The Aeronef produces no output for that run" (CR-C2-05). | Closed |
| G2-F13 | Minor | **Accepted:** #59 is answered by D68. | L2-AER-FU-230: TBD/TBR field "—"; rationale cites D68 and TT-580 (C5 annunciations). The inspector suggested the field carry `[P-SYS-470]` TBR instead, but `[P-SYS-470]` is used in the rationale only (FU's latency share is zero), so under the G2-F20 rule the Parameters field is "—" and so is TBD/TBR. TT-580 rewrite as B3 proposes. | Closed |
| G2-F16 | Minor | **Accepted as recommended:** the derivation is C2's; the fuel volume is the capsule; one MS-DYN subsection per FU model. | `ms_dyn_s6_s7_fu.md`: §6.1 to §6.3 (mass, CG, distributions, inertia with values), §7.2.1 to §7.2.3 (consumption, accounting, availability), mapping to the five models of L2-AER-FU-280. DD-C2-07 (fuel volume = body shape, no new parameter). P-FU-070, -080 values proposed, TBD → TBR (TT-770). L2-AER-FU-160, -190, -280 rationales and criteria. | Closed on the FU side; merge at I1 (IN-C2-52) |
| G2-F17 | Minor | **Accepted, first option:** apply the L2-AER-FU-190 equality to each vehicle parameter set as a run-start check. | New L2-AER-FU-330 (reject a parameter set whose `[P-FU-070]` or `[P-FU-080]` does not match the value derived from its own dimensions and masses). DD-C2-05 (check, not derive). L2-AER-FU-010, -170, -190 rationales. `[P-FU-090]` description. Initial-condition error extended (CR-C2-05, IN-C2-31). | Closed |
| G2-F18 | Minor | **Owner ruling Q4 (D72):** `[P-SYS-290]` is the anchor only. Link the chain. | L2-AER-FU-290 rationale states the chain and the re-derivation order. MS-DYN §7.2.4 proposal states the derivation formula (asinh form, recomputed: 2.3467 × 10⁻⁷) and when to re-run it. Register rows TT-110, TT-750, TT-800 linked (`param_proposals.md` §2). P-FU-040, -050 notes and the P-SYS-290 description (PARAM-UNUSED expected). No requirement cites `[P-SYS-290]`, as the ruling asks. | Closed (register edits at I1) |
| G2-F19 | Editorial | **Accepted** (FU parts). | L2-AER-FU-040 and -160: "C2 proposes … DD-110 / DD-120" → "Under DD-110 / DD-120 (accepted, D65)". L2-AER-FU-100: "ranges in work/C2/param_proposals.md" → "the PARAMETERS.yaml notes". | Closed |
| G2-F20 | Editorial | **Accepted** (FU parts): each Parameters field lists exactly the parameters its statement and criteria use, and each TBD/TBR field the open ones among them. | Applied to all 34 records; for example -050 drops P-FU-060, -080 drops P-TM-010 and adds the TBRs of P-FU-010 and P-SYS-300, -090 and -140 become "—", -110 drops P-FU-010, -220 drops P-SYS-470, -250 drops P-TM-010; -060, -160, -170, -180 add missing TBR rows. Stated in the section introduction. | Closed |
| G2-F21 | Editorial | **Accepted as recommended.** | L2-AER-FU-290 statement: "… the exponential of the product of [P-FU-040], [P-DYN-010], [P-SYS-280] and the sum of one and [P-FU-100]"; symbols in the rationale match. | Closed |
| G2-F22 | Editorial | **Accepted** (C-8 is the FU check; MS-DYN §11 is C1's). | C-8 wording proposed in `ms_dyn_s6_s7_fu.md` §7.2.5 (the FU fuel mass flow of each simulation step; SC-110 to the crash, rest on the ground included). IN-C2-51 to C1. L2-AER-FU-080 rationale cites C-8. | Closed on the FU side; C1 applies |
| G2-F24 | Editorial | **Accepted:** correct the bound. | IN-C2-41 rewritten: bound from the effector authority (C3 reference layout), at most 9.4 × 10⁻⁶ of the mass per control frame at dry mass; the inspector's 7.7 × 10⁻⁷ case quoted; conclusion unchanged. L2-AER-FU-140 rationale updated. | Closed |
| G2-F09, -F23 | Minor, Editorial | Not FU's: `[P-DYN-270]` is C1's (D72 set it to 600 s); the L1-AER-200 leg number goes through CR-B3-11. FU's rationales already cite SC-110 leg 11. | None | Not applicable |
| G2 §4 (EF note) | — | I1 should fix who computes the resultant. C3 answered: EF, once (DD-C3-05, D73). | L2-AER-FU-070 statement: FU takes the control force and moment that EF computes from its outputs; FU uses no per-effector output. L2-AER-FU-040 and -270 statements follow. IN-C2-11, -21 closed; IN-C3-10 answered. | Closed |

## 2. D69 impact on FU (B3 impact list §2 and G2 §6)

| Item | Source | Change made | Records |
| --- | --- | --- | --- |
| Section introduction: zero flow on the ground | B3 | New paragraphs "Ground operations (D69)" and the exhaustion paragraph (D68: in flight, the contact is a crash; a zero-fuel run stays on the ground). | intro |
| Runs start on the ground; initial fuel at a ground start | G2 §6, B3 | L2-AER-FU-020 rationale and criteria (ground starts at zero, half and full fuel, plus one airborne test start, D73 B3-1); L2-AER-FU-030 rationale (same check for both starts). | -020, -030 |
| Zero flow with the effectors off, no new term | G2 §6, B3, L1-AER-940 | New L2-AER-FU-300 (child of L1-AER-940): zero flow at each step with zero control force and moment; test over SC-130, SC-110 leg 7a and a ground start held on the ground. L2-AER-FU-040 and -060 gain L1-AER-940 as a parent (the relationships give zero; no idle term). L2-AER-FU-040 rationale: "each airborne condition; zero with the effectors off". | -040, -060, -300 |
| A run no longer ends at the first ground contact | G2 §6 | L2-AER-FU-080 criterion: "from a ground start at [P-FU-010] to the end of the run at the crash after fuel exhaustion", rest on the ground included. L2-AER-FU-110 criterion: "including the rest on the ground and the samples from fuel exhaustion to the crash". | -080, -110 |
| Zero-fuel runs stay on the ground | G2 §6 | L2-AER-FU-090, -200, -230 keep their zero-fuel cases, now a ground start (with a takeoff engaged for -200); rationales say the vehicle stays on the ground (SC-130 zero-fuel variation). | -090, -200, -230 |
| Fuel exhaustion in flight is a crash (D68) | D68, B3 | L2-AER-FU-200 and -230 rationales. New L2-AER-FU-320: the same fuel availability goes to the DYN ground contact model (I-03 → F-AER-12, CR-B3-39), for the "fuel remaining" of a landing and the crash at exhaustion (D73 B3-3). IN-C2-50 to C1. | -200, -230, -320 |
| Hover endurance from a takeoff at full fuel (L1-AER-360 v2) | G2 §6, CR-B3-17 | L2-AER-FU-290 rationale: the takeoff counts from its engagement; before liftoff the flow is below the hover flow; the climb's upward acceleration costs about 1.1 × 10⁻⁴ kg (0.03 s of hover flow) against a margin worth a twentieth of [P-SYS-280] of hover (8280 s); the gear transit is part of the hold; the gear adds no mass or drag. The inequality is unchanged and still met with the database values (490.35 kg needed, 500 kg held; recomputed). Criterion 2: from a ground start, takeoff engaged at the start, then Hover, exhaustion no earlier than [P-SYS-280] from the engagement. | -290 |
| Gear and mass properties | B3 | New L2-AER-FU-310: mass properties with no dependence on the gear position (parents L1-AER-900, -210, -220). L2-AER-FU-110, -150, -160, -270 rationales: the gear has no mass; FU takes no gear state. IN-C2-53 to C1. | -110, -150, -160, -270, -310 |
| L2-AER-FU-120: CG off I-04; fuel availability to DYN | B3, G2-F05 | See G2-F05; the fuel availability to DYN is a separate record, L2-AER-FU-320, because it crosses I-03, not I-04. | -120, -320 |
| L2-AER-FU-230 TBD field | G2-F13 | See G2-F13. | -230 |
| L1-AER-430 v2 (gear command in, gear state out) | CR-B3-19 | L2-AER-FU-130 rationale: neither the effector commands nor the landing gear command reaches FU; the gear state is DYN's. FU's share is unchanged. | -130 |
| L1-AER-640 v2, -660 v2, -720 v2, -880 v2, -160 v2, -200 v2, -580 v2 | CR-B3-10, -11, -18, -24 to -27 | FU's share unchanged; rationales touched where they quoted the old text (-020: gear position is DYN's item of the initial condition; -040: "airborne"; -280: gear model is DYN's). | -020, -040, -280 |
| New L1 records allocated to FU | L1-AER-940 | L2-AER-FU-300 (with -040, -060). L1-AER-900 (allocated to DYN, but its "children must show" names the FU requirements): L2-AER-FU-310, with CR-C2-04 adding FU to its allocation. L1-AER-260 v2, -270 v2 (fuel remaining, crash at exhaustion): L2-AER-FU-320, with CR-C2-04. L1-AER-910, -920, -930, -950 to -970 have no FU share. | -300, -310, -320 |
| C3: EF computes the resultant once (DD-C3-05) | Brief, C3 | L2-AER-FU-070 v2 (interface need to C3 updated). | -070 |

## 3. Numerical checks (recomputed, script in the session scratchpad)

| Quantity | Value |
| --- | --- |
| Drag at 300 kt, sea level, 5 m² | 72 945 N |
| `k_t` for exactly 8 h at that speed (asinh form) | 2.3467 × 10⁻⁷ kg/(N·s); with 2.34 × 10⁻⁷: 8.02 h |
| Largest `[P-SYS-280]` meeting L2-AER-FU-290 | 168 278 s (46.74 h); database 165 600 s |
| Capacity needed for 165 600 s | 490.35 kg ≤ 500 kg |
| Hover flow at maximum mass | 3.44 × 10⁻³ kg/s |
| Takeoff: upward acceleration phase (0.1 g to 60 ft/min) | 0.31 s; extra fuel 1.07 × 10⁻⁴ kg (0.031 s of hover) |
| Takeoff climb (1.4 m gear to 5 ft hover height) | 0.124 m |
| Inertia, 12 m × 4 m capsule: dry 1000 kg / fuel 500 kg / full | (1900, 10650) / (950, 5325) / (2850, 15975) kg·m² (I_xx, I_yy = I_zz) |
| Mass fall per control frame, authority bound, dry mass | ≤ 9.4 × 10⁻⁶ |
| Exhaustion step with the DD-C2-06 rule, 10⁵ random cases | 0 negative, 0 residual positive |

## 4. Checks run

- `python tools/lint.py --file work/C2/L2_FU.md`: 0 errors, 18 COMPOUND warnings (D30: closed lists, one relationship with its operands, or one constraint; none forms a tree of cases).
- Trial assembly (`assemble.py L2`, reverted afterwards): `trace_check` reports NO-PARENT only for L1-AER-900 and -940, which the parallel application of the B3 CRs adds (D73); no other FU error. `param_check`: no FU error; PARAM-UNUSED on P-SYS-290 is expected (anchor only, D72 Q4).
