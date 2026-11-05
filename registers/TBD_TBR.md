# TBD / TBR register

Open items in requirements and parameters. Every item has an owner and a closure date.

Opened by task B2 (2026-11-04). Rows TT-010 to TT-220 group the TBD and TBR parameters of `parameters/PARAMETERS.yaml`; the later rows copy the TBD/TBR field of each live L0 and L1 requirement, whose closure is stated in the field itself. IDs are never reused. G1 rework (2026-11-04): field copies refreshed from the records; TT-650 to TT-730 added (`reviews/G1/dispositions.md`).

| ID | Item | Type (TBD/TBR) | Location (requirement or parameter ID) | Owner | Closure date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TT-010 | Performance envelope values (B1-Q07, D47) | TBD | P-SYS-200, P-SYS-210, P-SYS-220, P-SYS-230, P-SYS-240, P-SYS-250, P-SYS-270, P-SYS-280 | Martin | G2 (I1) | Open |
| TT-020 | Effector authority values | TBD | P-SYS-400, P-SYS-410, P-SYS-420 | Martin | G2 (I1 budget closure) | Open |
| TT-030 | Wind: steady 100 kt, gusts 50 kt (D51) | TBR | P-SYS-430, P-SYS-560 | Martin | G2 | Open |
| TT-040 | Vehicle acceleration limit 1.5 g and its split (D48) | TBR | P-SYS-440, P-AF-200, P-FC-020 | Martin | G2 | Open |
| TT-050 | Position-holding budget 1 m and its split (D48) | TBR | P-SYS-450, P-AF-160, P-FC-010 | Martin | G2 | Open |
| TT-060 | Position-hold settling time | TBD | P-SYS-460 | Martin | G2 (C5) | Open |
| TT-070 | Timing budget (D48) | TBR | P-SYS-300, P-SYS-310, P-SYS-470, P-SYS-480, P-TM-010, P-AF-060 | Martin | G2 (I1) | Open |
| TT-080 | Effector command response time | TBD | P-EF-010 | Martin | G2 (C3) | Open |
| TT-090 | Landing envelope: 2 ft fall, 0.5 m/s (D53) | TBR | P-SYS-500, P-SYS-510 | Martin | G2 | Open |
| TT-100 | Cross-axis tolerances | TBD | P-SYS-540, P-SYS-550 | Martin | G2 (C4) | Open |
| TT-110 | Dry mass, consumption parameters, accounting tolerance | TBD | P-FU-030, P-FU-040, P-FU-050, P-FU-060 | Martin | G2 (C2) | Open |
| TT-120 | Usable fuel mass at full capacity | TBD | P-FU-010 | Martin | G2 (C2) | Open |
| TT-130 | Low-fuel threshold 0.1 of capacity (D48) | TBR | P-FU-020 | Martin | G2 | Open |
| TT-140 | Crew station position | TBD | P-DYN-400 | Martin | G2 (C1) | Open |
| TT-150 | Gravity = standard gravity (D48) | TBR | P-DYN-010 | Martin | G2 (C1) | Open |
| TT-160 | Hover height and standard vertical speed (D56) | TBD | P-AF-210, P-AF-220 | Martin | G2 (C5) | Open |
| TT-170 | Selection resolutions (crew units) | TBD | P-AF-010, P-AF-020, P-AF-030, P-AF-040 | Martin | G2 (C8) | Open |
| TT-180 | Autoflight tolerances and settling time (placeholders, split per mode in Phase 4) | TBD | P-AF-090, P-AF-100, P-AF-110, P-AF-120, P-AF-130, P-AF-140, P-AF-170, P-AF-190 | Martin | G3 (M0 to M8) | Open |
| TT-190 | Pitch and roll tolerance | TBR | P-AF-180 | Martin | G2 (C5) | Open |
| TT-200 | Navigation validity thresholds | TBD | P-NAV-010, P-NAV-030 | Martin | G2 (C6) | Open |
| TT-210 | Display resolutions (crew units) | TBD | P-TM-020, P-TM-030, P-TM-040, P-TM-050 | Martin | G2 (C8) | Open |
| TT-220 | Parallel efficiency and instance count | TBR | P-SYS-060, P-SYS-070 | Martin | When parallel execution is picked up (#86) | Open |
| TT-230 | Treatment of rigid-body kinematic terms (#81, deferred to L2), Martin, closes at G2 (C1) | TBD/TBR field | L0-CON-030 | Martin | as stated | Open |
| TT-240 | Elongated body shape provisional, TBR, Martin, 2026-11-30 | TBD/TBR field | L0-CON-140 | Martin | as stated | Open |
| TT-250 | Landing envelope limits TBD (lower level), Martin, closes at G2 | TBD/TBR field | L0-CON-290 | Martin | as stated | Open |
| TT-260 | Per-effector maximum force values TBD (EF level), Martin, closes at G2 (C3) | TBD/TBR field | L0-CON-300 | Martin | as stated | Open |
| TT-270 | — (3 g confirmed by the owner, D45, CR-B1-06) | TBD/TBR field | L0-CON-310 | Martin | as stated | Closed (D45; nothing open in the field) |
| TT-280 | P-SYS-060 value TBR (proposed 0.8), Martin, 2026-12-31; P-SYS-070 value TBR (proposed 8, the physical core count of the execution host), Martin, 2026-12-31 | TBD/TBR field | L0-SUC-060 | Martin | as stated | Open |
| TT-290 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-100 | Martin | as stated | Open |
| TT-300 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-110 | Martin | as stated | Open |
| TT-310 | Definition of a correct prediction TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-120 | Martin | as stated | Open |
| TT-320 | Scoring rule TBD in the reverse-engineering requirements (#69), Martin, closes when the plan is extended to RVS (D44) | TBD/TBR field | L0-SUC-130 | Martin | as stated | Open |
| TT-330 | Treatment of rigid-body kinematic and gyroscopic terms (#81), Martin, G2 (C1) | TBD/TBR field | L1-AER-020 | Martin | as stated | Open |
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
| TT-490 | P-SYS-250, P-SYS-210 values TBD (D47, TT-010), Martin, G2 (I1) | TBD/TBR field | L1-AER-330 | Martin | as stated | Open |
| TT-500 | P-SYS-270 value TBD (D47, TT-010), Martin, G2 (I1) | TBD/TBR field | L1-AER-350 | Martin | as stated | Open |
| TT-510 | P-SYS-280 value TBD (D47, TT-010), Martin, G2 (I1); P-FU-010, P-FU-030, P-FU-040 values TBD (TT-110, TT-120), Martin, G2 (C2) | TBD/TBR field | L1-AER-360 | Martin | as stated | Open |
| TT-520 | P-SYS-540, P-SYS-550 values TBD (TT-100), Martin, G2 (C4) | TBD/TBR field | L1-AER-380 | Martin | as stated | Open |
| TT-530 | P-AF-180 value TBR (TT-190), Martin, G2 (C5) | TBD/TBR field | L1-AER-390 | Martin | as stated | Open |
| TT-540 | P-SYS-450, P-AF-160, P-FC-010 values TBR (D48, TT-050), Martin, G2; P-SYS-460 value TBD (TT-060), Martin, G2 (C5); P-SYS-430, P-SYS-560 values TBR (D51, TT-030), Martin, G2; P-SYS-570 value TBD (D62, TT-650), Martin, G2 | TBD/TBR field | L1-AER-460 | Martin | as stated | Open |
| TT-550 | P-SYS-470, P-SYS-310, P-TM-010 values TBR (D48, TT-070), P-AF-060 value TBD (TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-470 | Martin | as stated | Open |
| TT-560 | Flight control panel content (#79), Martin, G2 (C8) | TBD/TBR field | L1-AER-480 | Martin | as stated | Open |
| TT-570 | P-FU-020 value TBR (D48, TT-130), Martin, G2 | TBD/TBR field | L1-AER-570 | Martin | as stated | Open |
| TT-580 | Autoflight state after fuel exhaustion (#59), Martin, G2 (C2, C5) | TBD/TBR field | L1-AER-580 | Martin | as stated | Open |
| TT-590 | P-TM-010 value TBR (D48, TT-070), Martin, G2 (C7) | TBD/TBR field | L1-AER-600 | Martin | as stated | Open |
| TT-600 | Releasable or protected classification of each signal (#69), Martin, closes when the plan is extended to the RVS (D44) | TBD/TBR field | L1-AER-630 | Martin | as stated | Open |
| TT-610 | Valid initial mode states (#60), Martin, G2 (C5) | TBD/TBR field | L1-AER-660 | Martin | as stated | Open |
| TT-620 | P-SYS-300 value TBR (D48, TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-670 | Martin | as stated | Open |
| TT-630 | P-SYS-310 value TBR (D48, TT-070), Martin, G2 (I1) | TBD/TBR field | L1-AER-680 | Martin | as stated | Open |
| TT-640 | P-SYS-480 value TBR (D48, TT-070), P-EF-010 value TBD (TT-080), Martin, G2 (C3, C4) | TBD/TBR field | L1-AER-710 | Martin | as stated | Open |
| TT-650 | Minimum gust rise time (D62) | TBD | P-SYS-570 | Martin | G2 (C1, with the TST wind model) | Open |
| TT-660 | Model specification MS-DYN not yet written (cited by L1-AER-010 to -070, -160, -220, -720) | TBD | specs/MS-DYN.md | Martin | G2 (C1) | Open |
| TT-670 | Autoflight mode logic AF_MODE_LOGIC not yet written (cited by L1-AER-450) | TBD | specs/AF_MODE_LOGIC.md | Martin | G2 (C5) | Open |
| TT-680 | Interface control documents not yet written: ICD-AER-TST, ICD-FC-AF, ICD-NAV-AF, ICD-FCP (new, D55) and the home of the vehicle-model boundary definitions (IN-B1-01) | TBD | icd/; L1-AER-420, -430, -480, -490, -590, -630, -640, -880, -890 | Martin | G2 (I1) | Open |
| TT-690 | Verification procedure IDs ("Inspection — TBD") of the L1 records, roll-up and leaf | TBD | requirements/L1.md, every live record | Martin | G4 (Phase 5, V4) | Open |
| TT-700 | Reading of L0-CON-100 (initial fuel quantity: capacity parameter plus the initial fuel of each run's initial condition; N-B1-08) | TBR | L0-CON-100; L1-AER-150 | Martin | G1 (owner question Q3, `reviews/G1/dispositions.md`) | Closed (D63) |
| TT-710 | P-DYN-010 value TBR (TT-150), P-SYS-440 value TBR (TT-040), P-SYS-570 value TBD (TT-650), Martin, G2 | TBD/TBR field | L1-AER-290 | Martin | as stated | Open |
| TT-720 | Vehicle-model boundary ICD home (IN-B1-01), Martin, G2 (I1) | TBD/TBR field | L1-AER-430 | Martin | as stated | Open |
| TT-730 | Abnormal and emergency procedures deferred with the hazard analysis, Martin, closes when failures are introduced (#85) | TBD/TBR field | L1-AER-840 | Martin | as stated | Open |
