# B3 — Issues: owner questions, notes and self-check

Task B3 (plan §6), 2026-11-05. Inputs read at branch c1_c2, commit 63499b8. The worktree was created at efe226e and was moved to 63499b8 before work started, since the brief names that commit.

## 1. Questions for the owner

D69 and D70 settle almost everything. Three choices remain open, and each has a recommended answer that the CRs already assume.

| Q | Question | Recommended answer | Where it matters |
| --- | --- | --- | --- |
| B3-Q1 | **May a run still start airborne?** D69 says "runs start on the ground". The credibility checks (C-1, C-2 from a release at altitude; C-3, C-5 gravity-free, D72) and tests at altitude (for example SC-020 at 30 000 ft) need an airborne start. Without one, each test begins with a takeoff and a climb of up to 25 min of simulation time at 6000 ft/min. | **Yes, for test runs only.** The operational start, the reference mission SC-110 and SC-130 start on the ground. A test procedure may set an airborne initial condition (gear retracted, effectors on, the modes of the scenario active), and each test that does so says why. | L1-AER-660 v2 (CR-B3-26), L1-AER-950, CONOPS §5 (CR-B3-33), MS-DYN §10.3, §11, L2-AER-DYN-430, -600 to -640, ICD-AER-TST |
| B3-Q2 | **What wind applies at a takeoff?** On the ground the ground reaction holds the vehicle against the drag. The flight software does not know the wind (L1-AER-670), so at liftoff the drag acts as a step. In the largest wind of the envelope (150 kt) the step is 18.2 kN, 1.86 g at dry mass. That breaks L1-AER-300 ([P-SYS-440] = 1.5 g), and a liftoff is not a gust that builds up over [P-SYS-570]. | **A takeoff wind limit, [P-SYS-580] = 75 kt (TBR), part of the wind envelope at liftoff.** It is sized so that the drag step at dry mass stays within the FC transient allowance [P-FC-020] (the bound is 77.8 kt). Landing needs no limit: Hover holds the position against any envelope wind, and after the contact the ground takes the drag. Alternatives: no limit, with the liftoff step excluded from L1-AER-300 (weakens the crew-protection chain), or a smaller [P-DYN-100]. | L1-AER-960, glossary *Wind envelope*, P-SYS-580, FA §7.2, C4 |
| B3-Q3 | **Which contacts are crashes, whatever the speeds?** D68 says the ground contact after fuel exhaustion is a crash. D69 does not say what a contact with the gear retracted (or in transit) is. | **Both are crashes.** A landing is a contact of the extended gear, within the speed envelope, with fuel remaining. There is no belly-landing model, and a free fall of under 2 ft after exhaustion is still a crash (D68 read literally). Under autoflight neither case occurs in nominal operation: Land extends the gear first, and Land has fuel. | L0-CON-290 v4, L0-ASM-110, L1-AER-260 v2, -270 v2, glossary *Landing*, *Crash*, MS-DYN §9, L2-AER-DYN-510, -520 |

**Not asked, decided in the CRs as recommendations (reject any one alone if unwanted):**

- the gear position is annunciated (CR-B3-21, optional);
- the hover endurance runs from a takeoff at full fuel (CR-B3-17);
- the effectors are switched off through an off value of the axis references (CR-B3-18);
- the gear transit time is 3 s (P-DYN-050);
- on the ground no mode is active (for C5, #60).

## 2. Notes

- **N-01 — Altitude reference (TT-820).** The altitude stays the CG altitude (CV-430), so MS-DYN, the atmosphere, the selected altitude, Altitude hold and the altitude indication do not change. A new defined quantity, the *height above the ground* (CV-400), is the clearance of the lowest point of the body, gear excluded. These quantities use it: the hover height [P-AF-210], the minimum operating height [P-SYS-210], the targets of Go to hover, Hover and Takeoff, and the Land descent. Ground contact is detected at the lowest point of the vehicle: the extended gear contact points, or the body. With the database values the CG is at 3.4 m on the ground and at 3.524 m in the hover, and the extended gear clears the ground by 0.124 m at the hover height. P-SYS-210 was described as an altitude; as a CG altitude, 1.524 m would put the body 0.48 m into the ground. It becomes a height (same value, D67 and D70).
- **N-02 — Gear clearance at the hover.** With the gear extended at the hover height (Land before its descent, Takeoff before its retraction), the clearance is only 0.124 m. [P-AF-110] (TBD) must stay below it in that phase, or the gear touches the ground. A touch would be a landing within the envelope, and the Takeoff logic would then have to handle a landing during a takeoff (C5). The wind is horizontal (D51), so the vertical disturbance is small, but C5 should state the bound. The owner may prefer a longer gear clearance (a shorter [P-DYN-040]); D69 wants the descent "short", and 0.124 m is about 0.4 s at [P-AF-240].
- **N-03 — L1 ID space.** L1-AER-900 to -970 use the next free IDs. Only L1-AER-980 and -990 remain in steps of 10 within the three digits the lint allows (`tools/lint.py`: `^L1-AER-\d{3}$`). A later L1 addition will need either an intermediate number, which breaks "steps of 10", or a lint change to four digits. The owner should decide this before the next L1 change.
- **N-04 — L0 statements unchanged.** Every L0 change is to a rationale, the roll-up guidance, a Source or the assumption. The L0 statements ("ground contact … as a landing … and as a crash", "ground contact" as an external effect) already hold with the gear, so the aircraft stays a black box at L0 (D33). The new L1 records trace to L0-CON-090, -100, -120, -130, -290, L0-OBJ-010 and -030.
- **N-05 — Liftoff in wind (B3-Q2).** If the owner rejects a takeoff wind limit, L1-AER-960's wind clause becomes "within the wind envelope", and C4 must show the liftoff step within [P-SYS-440]. With the current values that cannot hold at dry mass in the strongest gust. One of [P-SYS-440], [P-DYN-100] or the gust amplitude [P-SYS-560] would then have to change, or L1-AER-300 would need a liftoff exception.
- **N-06 — Effectors off mechanism.** L1-AER-420 lets only axis references cross from AF to FC, with no mode information (D15). The CRs propose an off value of the axis references. The alternative, FC reading the gear state and switching off on its own, would put ground logic in FC and leave Takeoff (powered on the ground) to a second rule. Either keeps L1-AER-930 as written.
- **N-07 — Fuel exhaustion on the ground.** A run started with zero fuel stays on the ground, annunciates FUEL EXHAUSTED and cannot take off. No crash occurs, because no contact happens while airborne. C5 decides whether TAKEOFF is accepted at zero fuel (SC-130 variation).
- **N-08 — Plan text.** AIRCRAFT_REQUIREMENTS_PLAN.md §6 (C1, C5, M8) still describes the catalogue of D56 alone. The orchestrator edits it (`impact_list.md` §5); B3 does not.
- **N-09 — Minor findings outside D69 included.** These were folded in because they touch the same text: G2-F23 (SC-110 leg number in L1-AER-200), G2-F13 (#59 in L1-AER-580), G2-F05 (I-04 CG item in FA) and D72 (*Accuracy horizon*). D71 closes #79 in L1-AER-480.

## 3. Self-check (METHODOLOGY §13.1, new and changed statements)

| Check | Result |
| --- | --- |
| One "shall", subject is the Aeronef (L1) | Yes for L1-AER-900 to -970 and for each changed L1 statement (-050, -260, -270, -360, -430, -470, -530, -640, -660, -720, -890). |
| EARS pattern | Ubiquitous: -900, -940, -050, -430, -530, -640, -660, -720, -890. State-driven: -920. State plus timing: -930. Complex (while … when …): -910. Event-driven: -950, -960, -970, -260, -270, -360, -470. |
| No numbers in statements; parameters by ID | Yes. All values are in `param_proposals.md`; the derived values (3.4 m, 0.124 m) appear in rationales and notes only. |
| Glossary terms | New terms in `glossary_proposals.md` §1; changed ones in §2. "Autoflight takes off / lands / is taking off" is defined through *Takeoff* and *Land (mode)*. |
| Compound statements | -270 is "or" over the three crash conditions, the complement of -260 (D30). -430, -640 and -660 are closed lists. -470 covers three annunciated kinds with one latency. None forms a tree of cases. |
| Rationale with sufficiency, parent, source | Yes for each new record. Parents are existing L0 records; no record is Derived. |
| Verification | Each new record is allocated, so it is verified by roll-up (D40, D58) with "Children must show" guidance, Test or Analysis. |
| TBD/TBR with owner and closure | Yes. The new rows TT-850 and TT-860 are proposed; the existing TT rows are cited. |
| Criticality | "Not assessed" for each; hazards deferred. |
| Solution-free | The gear layout, the transit mechanism and the way FC commands zero are left to MS-DYN, C3, C4 and C5. The off value of the axis references is stated as a recommendation in rationales only. |

## 4. Summary

- **CRs:** 41 (L0 7, L1 21, CONOPS 7, CONVENTIONS 1, GLOSSARY 1, FUNCTIONAL_ANALYSIS 4).
- **L1 changes:** 24 records changed, 8 new (L1-AER-900 to -970, all Functional, Performance, Constraint or Model fidelity; none Derived).
- **Parameters:** 2 new (P-DYN-050 TBR, P-SYS-580 TBR) and 7 changed descriptions.
- **Glossary:** 11 new terms and 26 changed definitions.
- **Conventions:** 1 new (CV-400) and 3 changed (CV-160, CV-420, CV-440).
- **Scenarios:** 1 new (SC-130) and 3 changed (SC-100, SC-110, SC-200).
- **Need:** 1 new (N-450).
- **Owner questions:** 3.
