# I1 — Integration record, owner questions and notes

Task I1 (plan §6, Phase 3b), run on branch `worktree-agent-a41641cdac88adfea` from the `c1_c2` tip (41505b5, D76). Local IDs I1-Qnn need GitHub issue numbers; cite them by issue number once filed (never reused).

## 1. What was done

| Step | Result |
| --- | --- |
| 1. Change requests | CR-C4-01 to -05, CR-C5-01 to -03, CR-C6-01 to -03, CR-C7-01 to -04, CR-C8-01 to -03 applied and logged "Applied", approved by the owner (D76), 2026-11-08. CR-C3-01 and -02 were already applied (D73). L1 records changed (versions bumped): L1-AER-310 v3, -320 v2, -330 v3, -360 v4, -370 v2, -380 v2, -530 v3, -620 v2, -630 v2, -640 v3, -890 v3. GLOSSARY, CONOPS, FUNCTIONAL_ANALYSIS, CONVENTIONS CV-830 and the P-SYS-540 description changed. L0 needed no change. |
| 2. Staging merge | Parameters (P-FC-030 to -120, P-NAV-060 to -080, P-FCP-010, -020; values for the C4 to C8 proposals; P-SYS-230 stored as 154.33333333333334 m/s). TBD/TBR rows TT-940 to TT-960 and status updates (TT-100, -200 TBD to TBR; TT-580, -590, -610, -670, -680, -720 closed). 41 glossary terms. Design decisions DD-210 to DD-560 (C1 rework DD-C1-07 to -11 = DD-210 to DD-250; C2 rework DD-C2-05 to -07 = DD-260 to DD-280; C4 = DD-290 to DD-350; C5 = DD-360 to DD-420; C6 = DD-430 to DD-460; C7 = DD-470 to DD-510; C8 = DD-520 to DD-560), then DD-570 and DD-580 (I1). All local `DD-Cx-nn` references in the drafts, MS-DYN and the specifications were replaced. `work/C5/AF_MODE_LOGIC.md` moved to `specs/AF_MODE_LOGIC.md`. L2 and L3 reassembled with `assemble.py L2` and `L3` only. |
| 3. ICDs | `icd/ICD-AER-TST.md`, `ICD-FC-AF.md`, `ICD-NAV-AF.md`, `ICD-FCP.md` and, for the vehicle-model boundary, `ICD-VM-FS.md`. **Home decision (IN-B1-01, TT-720): its own file, DD-570**; ICD-AER-TST keeps to the TST interface. C7's classification is the "proposed class" column of ICD-AER-TST §6.2 (D76). |
| 4. Conflicts | Section 2. |
| 5. Checks | Section 4. |

## 2. Conflicts resolved

| Conflict | Resolution |
| --- | --- |
| ICD-FC-AF: C4 (value, rate, acceleration in frame V) against C5 (value, rate, regulated flag in frame L) | One axis reference of reference value, reference rate, reference acceleration and the regulated quantity (`value` or `rate`); the axes are those of frame V, which is parallel to frame L (CV-150), so velocity and acceleration are the same in both; a position is absolute, in L. DD-580. Changed: L2-AER-AF-090 (statement, rationale, verification), AF_MODE_LOGIC §12, L2-AER-FC-020 rationale, glossary *Axis reference*. AF now owes the reference acceleration (it is the derivative of the rate it already shapes). |
| C5-C02: L2-AER-FU-240 gave the fuel state to FCP only | FU-240 gives the one fuel-state item to the panel and to AF (parent L1-AER-430 added). |
| C5-C04: AF-820 gear command against L1-AER-630 | AF-820 has parents L1-AER-620 and L1-AER-630 (CR-C7-02 allocates AF). |
| C5-Q13 / CR-C5-01: NAV gave no horizontal velocity components | L2-AER-NAV-080 (compute) and -280 (interface) written; NAV-030 and -230 trace to L1-AER-530 and -890. |
| IN-C5-40: decision on each mode selection and the target AF takes were recorded by nobody | L2-AER-TM-220 (decision) and -230 (selector target) written; ICD-AER-TST §6. |
| IN-C7-01: the event record needs the classification speeds | L2-AER-DYN-530 now outputs them and the reported state (DD-490). |
| Allocation against children (FA §6.2) | L1-AER-960 and -970 had no EF child: L2-AER-EF-340 (parent L1-AER-960) and L2-AER-EF-210 (parent L1-AER-970) take them, with a sufficiency argument each. A script check in both directions (each allocated subsystem has a child; each child's subsystem is allocated) now finds no gap. |
| C2 against C4: FU gives a centre-of-gravity item, FC says there is none | ICD-VM-FS §4.3 carries the zero vector for L1-AER-430 and says FC does not use it; FC reads the mass and the three principal moments. |
| Budgets (C4 §5, C5) | FUNCTIONAL_ANALYSIS §7.6 closes every budget. Two values changed: P-AF-110 0.05 m to 0.07 m (FC share 0.05 m plus AF share 0.02 m, inside the gear clearance with the tilt term) and P-AF-170 0.25 m/s to 0.4 m/s (at least P-FC-040, at most P-SYS-510, below P-NAV-010). |
| Input timing (CV-840 left it to the ICD) | An input timestamped k first affects step k; a crew selection is taken at the first control frame starting at or after k (ICD-AER-TST §2). |

## 3. Owner questions

| ID | Question | Recommended answer |
| --- | --- | --- |
| I1-Q01 | The C1 and C2 rework design decisions DD-210 to DD-280 (C1: the atmosphere to 84 852 m, the gear geometry and movement, the ground start, the contact-step state, the ground hold; C2: the run-start inertia check, the exhaustion step, the fuel volume) are registered as "Accepted (rework under D72, D73; delta inspection at G2)". The owner ruled on the G2 findings (D72) and on the gear package (D73) but not on these decisions one by one. Accept them? | Yes, confirmed at the G2 delta inspection of C1 and C2. |
| I1-Q02 | Accept the two tolerance values that I1 changed to close the C4 and C5 shares: P-AF-110 = 0.07 m and P-AF-170 = 0.4 m/s (TBR, with P-FC-030 = 0.05 m and P-FC-040 = 0.3 m/s)? | Yes. The margin to the gear clearance is 0.019 m. The alternative of a smaller tilt tolerance P-AF-180 buys margin but tightens the attitude hold. |
| I1-Q03 | Three budgets close with little margin: the liftoff wind (P-SYS-580 = 75 kt uses 93 % of P-FC-020 at dry mass), the gust compensation delay (0.13 s against 0.18 s) and the altitude hold against the gear clearance (0.019 m). Keep the values until the prototype run of the reference law? | Yes. If the prototype shows less margin, lower P-SYS-580 to 70 kt first (drag 3.97 m/s², 19 % margin). A gust rise time below about 1.5 s would break the delay budget. |
| I1-Q04 | The TBD/TBR fields of some baselined L1 records still read as before the merge: L1-AER-430 (ICD home, TT-720), L1-AER-470 (P-AF-060 TBD), L1-AER-600 (G2 (C7)), L1-AER-660 and L1-AER-950 (valid initial mode states, TT-610), L1-AER-970 (P-AF-170 TBD). The register rows say so. Refresh them as an editorial change? | Yes, one editorial change request, with version bumps and no change to a statement, before the L1 re-baseline at G2. |

No question concerns an L1 statement, an allocation or a requirement value that the owner has already set.

## 4. Check results (task I2)

| Check | Result |
| --- | --- |
| `lint.py` | 0 errors, 273 warnings (COMPOUND and TIMING, judged by the authors) |
| `trace_check.py` | 16 errors, all CHILDLESS: the AF mode and tolerance records L2-AER-AF-320, -500, -520, -530, -540, -560, -580, -590, -600, -610, -620, -630, -640, -650, -660 and -670, which Phase 4 decomposes (M0 to M8, FC1) |
| `param_check.py` | 0 errors; one warning, P-SYS-290 not referenced (it anchors P-FU-040, P-FU-050 and P-SYS-280 only, D72 Q4) |
| `vcrm.py --check` | 0 errors; `verification/VCRM.md` regenerated (483 requirements) |
| Reference scripts | Every record ID, DD and parameter ID cited in the ICDs, the specifications and the registers exists (a script check; two withdrawn IDs are cited in the change request log only) |

## 5. Notes for the orchestrator

1. **Plan.** The plan has no D77 yet. Suggested content: the vehicle-model boundary has its own ICD (DD-570); ICD-FC-AF carries the reference acceleration and the regulated quantity (DD-580); the design decisions DD-210 to DD-580 are registered; P-AF-110 and P-AF-170 changed (I1-Q02). C5's note: the §6 C5 row reads "the catalogue of D56 and D69", and M8 covers Takeoff and Land with Go to hover and Hover.
2. **Staging files.** `work/C1` to `work/C8` and `work/I1` stay as the record of the merge. Their DD tables keep the local `DD-Cx-nn` IDs; the mapping is in `registers/DECISIONS.md` (the decision text) and in section 1 above.
3. **Work still outside the Aeronef requirements.** The TST side of ICD-AER-TST and the TST recordings of ICD-AER-TST §7 (D44); the classification of the signals with the RVS (TT-600, D44).
4. **G2.** Gate G2 reviews the L2 sections and the ICDs; the delta inspection of C1 and C2 covers DD-210 to DD-280 and the L2-AER-EF-210 and -340 parents added here.
