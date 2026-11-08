# TBD / TBR register

Open items in requirements and parameters. Every item has an owner and a closure date.

Opened by task B2 (2026-11-04). Rows TT-010 to TT-220 group the TBD and TBR parameters of `parameters/PARAMETERS.yaml`; the later rows copy the TBD/TBR field of each live L0 and L1 requirement, whose closure is stated in the field itself. IDs are never reused. G1 rework (2026-11-04): field copies refreshed from the records; TT-650 to TT-730 added (`reviews/G1/dispositions.md`). C1/C2 merge (2026-11-05): TT-740 to TT-800 added; rows updated for D64 to D66. B3 applied (2026-11-05, D73): TT-810, TT-820 and TT-560 closed; TT-850 to TT-920 added; field copies refreshed. C3 merged (D73): TT-020, TT-080 valued, TT-260 closed, TT-930 added. I1 merge (2026-11-08, D76): C4 to C8 parameters merged; TT-940 to TT-960 added; TT-100 and TT-200 TBD to TBR; TT-580, TT-590, TT-610, TT-670, TT-680 and TT-720 closed; TT-650 and TT-860 checked (FUNCTIONAL_ANALYSIS §7.6).

| ID | Item | Type (TBD/TBR) | Location (requirement or parameter ID) | Owner | Closure date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TT-010 | Performance envelope values (D47, D66, D67); P-SYS-230 is stored as 154.33333333333334 m/s, the nearest double to 300 kt, so that 300 kt is selectable (C8-Q07, D76) | TBR | P-SYS-200, P-SYS-210, P-SYS-220, P-SYS-240, P-SYS-250, P-SYS-270, P-SYS-230 | Martin | G2 (I1) | Open |
| TT-020 | Effector authority values 60 kN up, 190 kN in the other five force directions, 2000 N·m per axis (C3, D73) | TBR | P-SYS-400, P-SYS-410, P-SYS-420 | Martin | G2 (I1 budget closure) | Open |
| TT-030 | Wind: steady 100 kt, gusts 50 kt (D51) | TBR | P-SYS-430, P-SYS-560 | Martin | G2 | Open |
| TT-040 | Vehicle acceleration limit 1.5 g and its split (D48) | TBR | P-SYS-440, P-AF-200, P-FC-020 | Martin | G2 | Open |
| TT-050 | Position-holding budget 1 m and its split (D48) | TBR | P-SYS-450, P-AF-160, P-FC-010 | Martin | G2 | Open |
| TT-060 | Position-hold settling time 30 s (D70); the hold starts as rule PR-4 of AF_MODE_LOGIC defines it (C5) | TBR | P-SYS-460 | Martin | G2 (C5) | Open |
| TT-070 | Timing budget (D48); P-TM-010 equals P-SYS-310 (C7-Q03, D76) and P-AF-060 is 0.04 s TBR (C5); TT-590 merged | TBR | P-SYS-300, P-SYS-310, P-SYS-470, P-SYS-480, P-TM-010, P-AF-060 | Martin | G2 (I1) | Open |
| TT-080 | Effector command response time 0.06 s to the band P-EF-030 (C3, D73) | TBR | P-EF-010 | Martin | G2 (C3) | Open |
| TT-090 | Landing envelope at the contact step of a gear contact: 2 ft fall, 0.5 m/s (D53) | TBR | P-SYS-500, P-SYS-510 | Martin | G2 | Open |
| TT-100 | Cross-axis tolerances 0.1 m/s and 0.005 rad/s (C4, D76) | TBR | P-SYS-540, P-SYS-550 | Martin | G2 (C4) | Open |
| TT-110 | Dry mass 1000 kg, consumption coefficients 2.34e-7, accounting tolerance 1e-6 kg (D65, D66) | TBR | P-FU-030, P-FU-040, P-FU-050, P-FU-060 | Martin | G2 (I1) | Open |
| TT-120 | Usable fuel mass at full capacity 500 kg (D65) | TBR | P-FU-010 | Martin | G2 (I1) | Open |
| TT-130 | Low-fuel threshold 0.1 of capacity (D48) | TBR | P-FU-020 | Martin | G2 | Open |
| TT-140 | Crew station position (4, 0, −1) m (D64) | TBR | P-DYN-400 | Martin | G2 | Open |
| TT-150 | Gravity = standard gravity (D48) | TBR | P-DYN-010 | Martin | G2 (C1) | Closed 2026-11-05: Set by the owner (D64) |
| TT-160 | Hover height and standard vertical speed (D56) | TBD | P-AF-210, P-AF-220 | Martin | G2 (C5) | Closed 2026-11-05: Set by the owner (D70) |
| TT-170 | Selection resolutions 10 ft, 100 ft/min, 1 kt, 1° (D71). Checked by C8 against the selector ranges (20 ft to 150 000 ft, ±6000 ft/min, 0 to 300 kt, 0 to 359°): no conflict. The owner confirms at G2 | TBR | P-AF-010, P-AF-020, P-AF-030, P-AF-040 | Martin | G2 (C8) | Open |
| TT-180 | Autoflight tolerances and settling time (placeholders, split per mode in Phase 4). P-AF-090, -100, -120, -130, -190 as C5 proposed; P-AF-110 0.07 m and P-AF-170 0.4 m/s closed with the FC shares at I1; P-AF-140 stays TBD for M5 | TBR (P-AF-140 TBD) | P-AF-090, P-AF-100, P-AF-110, P-AF-120, P-AF-130, P-AF-140, P-AF-170, P-AF-190 | Martin | G3 (M0 to M8) | Open |
| TT-190 | Pitch and roll tolerance | TBR | P-AF-180 | Martin | G2 (C5) | Open |
| TT-200 | Navigation validity thresholds 1 kt and 80° (C6) | TBR | P-NAV-010, P-NAV-030 | Martin | G2 (C6) | Open |
| TT-210 | Display resolutions 1 ft, 10 ft/min, 1 kt, 1° (D71). Checked by C8: each selection resolution is a multiple of its display resolution. The owner confirms at G2 | TBR | P-TM-020, P-TM-030, P-TM-040, P-TM-050 | Martin | G2 (C8) | Open |
| TT-220 | Parallel efficiency and instance count | TBR | P-SYS-060, P-SYS-070 | Martin | When parallel execution is picked up (#86) | Open |
| TT-230 | Treatment of rigid-body kinematic terms (#81, deferred to L2), Martin, closes at G2 (C1) | TBD/TBR field | L0-CON-030 | Martin | as stated | Closed 2026-11-05: D64, CR-C1-01 |
| TT-240 | Elongated body shape provisional, TBR, Martin, 2026-11-30 | TBD/TBR field | L0-CON-140 | Martin | as stated | Open |
| TT-250 | Landing envelope limits TBR (P-SYS-500, P-SYS-510, TT-090), Martin, G2 | TBD/TBR field | L0-CON-290 | Martin | as stated | Open |
| TT-260 | Per-effector maximum force values TBD (EF level), Martin, closes at G2 (C3) | TBD/TBR field | L0-CON-300 | Martin | as stated | Closed 2026-11-05: per-effector maximum force values set as P-EF-120 (C3, D73; TBR under TT-930). The L0-CON-300 field still reads TBD until its next change |
| TT-270 | — (3 g confirmed by the owner, D45, CR-B1-06) | TBD/TBR field | L0-CON-310 | Martin | as stated | Closed (D45; nothing open in the field) |
| TT-280 | P-SYS-060 value TBR (proposed 0.8), Martin, 2026-12-31; P-SYS-070 value TBR (proposed 8, the physical core count of the execution host), Martin, 2026-12-31 | TBD/TBR field | L0-SUC-060 | Martin | as stated | Open |
| TT-290 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-100 | Martin | as stated | Open |
| TT-300 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-110 | Martin | as stated | Open |
| TT-310 | Definition of a correct prediction TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-120 | Martin | as stated | Open |
| TT-320 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-130 | Martin | as stated | Open |
| TT-330 | Treatment of rigid-body kinematic and gyroscopic terms (#81), Martin, G2 (C1) | TBD/TBR field | L1-AER-020 | Martin | as stated | Closed 2026-11-05: D64, CR-C1-01 |
| TT-340 | P-DYN-010 value TBR (D48, TT-150), Martin, G2 (C1) | TBD/TBR field | L1-AER-060 | Martin | as stated | Open |
| TT-350 | Per-effector maximum force values TBD, Martin, G2 (C3) | TBD/TBR field | L1-AER-110 | Martin | as stated | Open |
| TT-360 | P-SYS-400 value TBD (computed when the maximum vehicle mass is known), Martin, G2 (I1); P-SYS-440 value TBR (TT-040), P-SYS-240 value TBD (TT-010) | TBD/TBR field | L1-AER-120 | Martin | as stated | Open |
| TT-370 | P-SYS-410 value TBD (computed when the maximum vehicle mass is known), Martin, G2 (I1) | TBD/TBR field | L1-AER-130 | Martin | as stated | Open |
| TT-380 | P-SYS-420 value TBD (computed when the inertia is known), Martin, G2 (I1) | TBD/TBR field | L1-AER-140 | Martin | as stated | Open |
| TT-390 | P-FU-010 value TBD, Martin, G2 (C2, fuel budget §7.3) | TBD/TBR field | L1-AER-150 | Martin | as stated | Open |
| TT-400 | P-FU-040, P-FU-050 values TBD, Martin, G2 (C2) | TBD/TBR field | L1-AER-170 | Martin | as stated | Open |
| TT-410 | P-FU-030 value TBD, Martin, G2 (C2) | TBD/TBR field | L1-AER-180 | Martin | as stated | Open |
| TT-420 | P-FU-060 value TBD, Martin, G2 (C2) | TBD/TBR field | L1-AER-190 | Martin | as stated | Open |
| TT-430 | Body shape provisional (L0-CON-140), Martin, 2026-11-30 | TBD/TBR field | L1-AER-220 | Martin | as stated | Open |
| TT-440 | P-DYN-400 value TBD, Martin, G2 (C1) | TBD/TBR field | L1-AER-250 | Martin | as stated | Open |
| TT-450 | P-SYS-500, P-SYS-510 values TBR (owner, #100), Martin, G2 | TBD/TBR field | L1-AER-280 | Martin | as stated | Open |
| TT-460 | P-SYS-440, P-AF-200, P-FC-020 values TBR (D48, TT-040); P-SYS-570 value TBD (D62, TT-650), Martin, G2 | TBD/TBR field | L1-AER-300 | Martin | as stated | Open |
| TT-470 | P-SYS-200, P-SYS-210, P-SYS-220, P-SYS-230 values TBD (D47, TT-010), Martin, G2 (I1); P-SYS-430, P-SYS-560 values TBR (D51, TT-030), Martin, G2; P-SYS-570 value TBD (D62, TT-650), Martin, G2 | TBD/TBR field | L1-AER-310 | Martin | as stated | Open |
| TT-480 | P-SYS-240 value TBD (D47, TT-010), Martin, G2 (I1) | TBD/TBR field | L1-AER-320 | Martin | as stated | Open |
| TT-490 | P-SYS-250, P-SYS-210 values TBD (D47, TT-010), Martin, G2 (I1); P-DYN-030 value TBR (TT-740) | TBD/TBR field | L1-AER-330 | Martin | as stated | Open |
| TT-500 | P-SYS-270 value TBD (D47, TT-010), Martin, G2 (I1) | TBD/TBR field | L1-AER-350 | Martin | as stated | Open |
| TT-510 | P-SYS-280 value TBR (TT-800), P-FU-010, P-FU-030, P-FU-040, P-FU-100 values TBR (TT-110, TT-120, TT-790), Martin, G2 (I1) | TBD/TBR field | L1-AER-360 | Martin | as stated | Open |
| TT-520 | P-SYS-540, P-SYS-550 values TBR (TT-100), Martin, G2 (C4) | TBD/TBR field | L1-AER-380 | Martin | as stated | Open |
| TT-530 | P-AF-180 value TBR (TT-190), Martin, G2 (C5) | TBD/TBR field | L1-AER-390 | Martin | as stated | Open |
| TT-540 | P-SYS-450, P-AF-160, P-FC-010 values TBR (D48, TT-050), Martin, G2; P-SYS-460 value TBD (TT-060), Martin, G2 (C5); P-SYS-430, P-SYS-560 values TBR (D51, TT-030), Martin, G2; P-SYS-570 value TBD (D62, TT-650), Martin, G2 | TBD/TBR field | L1-AER-460 | Martin | as stated | Open |
| TT-550 | P-SYS-470, P-SYS-310, P-TM-010 values TBR (D48, TT-070), P-AF-060 value TBD (TT-070), Martin, G2 (I1) (P-AF-060 is TBR since the I1 merge; the L1 field reads TBD until its next change) | TBD/TBR field | L1-AER-470 | Martin | as stated | Open |
| TT-560 | Flight control panel content (#79), Martin, G2 (C8) | TBD/TBR field | L1-AER-480 | Martin | as stated | Closed 2026-11-05: D71, CR-B3-22 (L1-AER-480 field —) |
| TT-570 | P-FU-020 value TBR (D48, TT-130), Martin, G2 | TBD/TBR field | L1-AER-570 | Martin | as stated | Open |
| TT-580 | Annunciations after fuel exhaustion (D68); #59 answered by D68, so the L1-AER-580 field is closed (CR-B3-24) | TBD | AF (C5); L1-AER-580 | Martin | G2 (C5) | Closed 2026-11-08: L2-AER-AF-860 and -870 (DD-400, C5-Q04 accepted, D76) |
| TT-590 | P-TM-010 value TBR (D48, TT-070), Martin, G2 (C7) | TBD/TBR field | L1-AER-600 | Martin | as stated | Closed 2026-11-08: merged into TT-070 (C7-Q03, D76); the L1-AER-600 field keeps its text until its next change |
| TT-600 | Releasable or protected classification of each signal (#69), Martin, closes when the plan is extended to the RVS (D44) | TBD/TBR field | L1-AER-630 | Martin | as stated | Open |
| TT-610 | Valid initial mode states (#60), Martin, G2 (C5). On the ground, no mode active, recommended (B3); airborne starts only for test runs and credibility checks (D73) | TBD/TBR field | L1-AER-660 | Martin | as stated | Closed 2026-11-08: AF_MODE_LOGIC §14, rows IC-1 to IC-7 (C5-Q10, D76); the L1-AER-660 field keeps its text until its next change |
| TT-620 | P-SYS-300 value TBR (D48, TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-670 | Martin | as stated | Open |
| TT-630 | P-SYS-310 value TBR (D48, TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-680 | Martin | as stated | Open |
| TT-640 | P-SYS-480 value TBR (D48, TT-070), P-EF-010 value TBD (TT-080), Martin, G2 (C3, C4) | TBD/TBR field | L1-AER-710 | Martin | as stated | Open |
| TT-650 | Minimum gust rise time 2 s (D62, D64). I1 check (FUNCTIONAL_ANALYSIS §7.6): the transient allowance holds at 2 s with an effective compensation delay of at most 0.18 s; the owner confirms the value at G2 | TBR | P-SYS-570 | Martin | G2 (C4 budget check at I1) | Open |
| TT-660 | Model specification MS-DYN not yet written (cited by L1-AER-010 to -070, -160, -220, -720) | TBD | specs/MS-DYN.md | Martin | G2 (C1) | Closed 2026-11-05: drafted by C1; §6, §7 content and baseline at I1/G2 (TT-780) |
| TT-670 | Autoflight mode logic AF_MODE_LOGIC not yet written (cited by L1-AER-450) | TBD | specs/AF_MODE_LOGIC.md | Martin | G2 (C5) | Closed 2026-11-08: specs/AF_MODE_LOGIC.md written by C5 and moved from work/C5 at I1 |
| TT-680 | Interface control documents not yet written: ICD-AER-TST, ICD-FC-AF, ICD-NAV-AF, ICD-FCP (new, D55) and the home of the vehicle-model boundary definitions (IN-B1-01) | TBD | icd/; L1-AER-420, -430, -480, -490, -590, -630, -640, -880, -890 | Martin | G2 (I1) | Closed 2026-11-08: icd/ICD-AER-TST.md, ICD-FC-AF.md, ICD-NAV-AF.md and ICD-FCP.md written, and the vehicle-model boundary in icd/ICD-VM-FS.md (I1, DD-570) |
| TT-690 | Verification procedure IDs ("Inspection — TBD") of the L1 records, roll-up and leaf | TBD | requirements/L1.md, every live record | Martin | G4 (Phase 5, V4) | Open |
| TT-700 | Reading of L0-CON-100 (initial fuel quantity: capacity parameter plus the initial fuel of each run's initial condition; N-B1-08) | TBR | L0-CON-100; L1-AER-150 | Martin | G1 (owner question Q3, `reviews/G1/dispositions.md`) | Closed (D63) |
| TT-710 | P-DYN-010 value TBR (TT-150), P-SYS-440 value TBR (TT-040), P-SYS-570 value TBD (TT-650), Martin, G2 | TBD/TBR field | L1-AER-290 | Martin | as stated | Open |
| TT-720 | Vehicle-model boundary ICD home (IN-B1-01), Martin, G2 (I1) | TBD/TBR field | L1-AER-430 | Martin | as stated | Closed 2026-11-08: the vehicle-model boundary has its own ICD, icd/ICD-VM-FS.md (I1, DD-570) |
| TT-730 | Abnormal and emergency procedures deferred with the hazard analysis, Martin, closes when failures are introduced (#85) | TBD/TBR field | L1-AER-840 | Martin | as stated | Open |
| TT-740 | Body dimensions 12 m × 4 m with the provisional shape (L0-CON-140, D64) | TBR | P-DYN-020, P-DYN-030 | Martin | 2026-11-30 | Open |
| TT-750 | Drag area 5 m² (D64) | TBR | P-DYN-100 | Martin | G2 (I1 budget closure) | Open |
| TT-760 | Model accuracy tolerances and horizon (D64) | TBR | P-DYN-200, P-DYN-210, P-DYN-220, P-DYN-230, P-DYN-240, P-DYN-250, P-DYN-260, P-DYN-270 | Martin | G2 | Open |
| TT-770 | Dry-mass and full-fuel principal moments of inertia, derived in MS-DYN | TBD | P-FU-070, P-FU-080 | Martin | G2 (I1, C1 and C2) | Open |
| TT-780 | MS-DYN §6 (mass properties) and §7 (effector and fuel models) content, and the MS-DYN baseline | TBD | specs/MS-DYN.md | Martin | G2 (I1, C2 and C3) | Open |
| TT-790 | FU computation agreement tolerance 1e-9 and hover consumption margin 0.05 (D65) | TBR | P-FU-090, P-FU-100 | Martin | G2 | Open |
| TT-800 | Hover endurance 46 h, derived from the endurance at maximum speed (D66) | TBR | P-SYS-280 | Martin | G2 (I1) | Open |
| TT-810 | Landing gear and ground operations: change requests against L0, L1 and the specifications, and the C1/C2 rework (D69) | TBD | task B3; L0-CON-160, -290, -310; L1-AER-280, -580, -660 and the mode records | Martin | Before G2 (B3, owner approval) | Closed 2026-11-05: B3 approved and applied (D73, CR-B3-01 to -41); the C1/C2 rework continues under TT-840 |
| TT-820 | Altitude reference with the gear: CV-430 measures the CG, while the hover height and the gear length are measured below the body (capsule radius 2 m) | TBD | P-AF-210, P-SYS-210, P-DYN-040; CV-430 | Martin | B3 | Closed 2026-11-05: CV-400, the height above the ground at the lowest point of the body (CR-B3-36, D73) |
| TT-830 | Vertical acceleration 0.1 g, takeoff and landing vertical speed 60 ft/min, gear length 1.4 m (D69, D70) | TBR | P-AF-230, P-AF-240, P-DYN-040; L1-AER-900, -950, -960, -970 | Martin | G2 (C1, C5) | Open |
| TT-840 | G2 (partial) rework of C1/C2: G2-F01, -F02, the Minor and Editorial findings, with the D69 rework (D72; scope `work/B3/impact_list.md` §1 to §3) | TBD | work/C1, work/C2, specs/MS-DYN.md | Martin | B3 approved (D73); delta re-inspection with EF | Open |
| TT-850 | Landing gear transit time 3 s (D69, B3, D73) | TBR | P-DYN-050 | Martin | G2 (C1) | Open |
| TT-860 | Maximum wind speed at liftoff 75 kt (D69, D73, B3-Q2). I1 check (FUNCTIONAL_ANALYSIS §7.6): the drag at the liftoff wind uses 93 % of P-FC-020 at dry mass; the budget closes with 7 % margin | TBR | P-SYS-580 | Martin | G2 (I1, C4 check against P-FC-020) | Open |
| TT-870 | P-DYN-040 value TBR (TT-830), P-DYN-030 value TBR (TT-740), Martin, G2 (C1) | TBD/TBR field | L1-AER-900 | Martin | as stated | Open |
| TT-880 | P-DYN-050 value TBR (TT-850), Martin, G2 (C1) | TBD/TBR field | L1-AER-910 | Martin | as stated | Open |
| TT-890 | P-SYS-480 value TBR (TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-930 | Martin | as stated | Open |
| TT-900 | P-DYN-030 value TBR (TT-740), P-DYN-040 value TBR (TT-830), Martin, G2 (C1); valid initial mode states (#60), Martin, G2 (C5) | TBD/TBR field | L1-AER-950 | Martin | as stated | Open |
| TT-910 | P-SYS-580 value TBR (TT-860), P-SYS-450 value TBR (TT-050), P-AF-240 value TBR (TT-830), Martin, G2 | TBD/TBR field | L1-AER-960 | Martin | as stated | Open |
| TT-920 | P-SYS-500, P-SYS-510 values TBR (TT-090), P-AF-240 value TBR (TT-830), Martin, G2; P-AF-170 value TBR 0.4 m/s (TT-180; the L1 field reads TBD until its next change), Martin, G2 (C5) | TBD/TBR field | L1-AER-970 | Martin | as stated | Open |
| TT-930 | Effector model values and reference layout: time constant 0.015 s, response band 5 %, six effectors of 100 kN (DD-160, DD-200; C3, D73) | TBR | P-EF-020, P-EF-030, P-EF-100, P-EF-110, P-EF-120, P-EF-130 | Martin | G2 (I1) | Open |
| TT-940 | FC tracking tolerances, settling times, allocation accuracy and ground-force margin (C4 first estimates, to be confirmed by a prototype run of the reference law) | TBR | P-FC-030, P-FC-040, P-FC-050, P-FC-060, P-FC-070, P-FC-080, P-FC-090, P-FC-100, P-FC-110, P-FC-120 | Martin | G2 (I1) | Open |
| TT-950 | NAV agreement tolerances 1e-6 m, 1e-9 m/s, 1e-9 rad (C6) | TBR | P-NAV-060, P-NAV-070, P-NAV-080 | Martin | G2 (I1) | Open |
| TT-960 | Fuel display resolution 1 lb and crew-unit conversion tolerance 1e-12 (C8) | TBR | P-FCP-010, P-FCP-020 | Martin | G2 (I1) | Open |
