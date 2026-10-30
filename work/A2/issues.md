# A2 — Issues

## Questions for the project owner

Each question has a proposed answer, which `specs/CONOPS.md` already uses. The scenario parts that depend on them are marked in CONOPS §7.

| ID | Question | Proposed answer | Affects |
| --- | --- | --- | --- |
| A2-Q01 | Is the air still (no wind) in this cycle? | Yes. Drag is relative to still air; horizontal speed is the same relative to air and ground. Wind can be added later as an TST-injected condition. | CONOPS §4.2; drag model (C1); horizontal speed definition (A3) |
| A2-Q02 | Are take-off, landing and ground contact in scope? | No. Runs start airborne; reaching the ground plane ends the run; no ground-contact model. | CONOPS §4.2, §4.6; SC-110 leg 10 |
| A2-Q03 | Refinement of Q2: in HDG, does the track follow the heading? In TRK and VOR, what does the heading do? | HDG sets the heading, and the track follows it (the vehicle flies nose first). TRK and VOR hold the heading at its value when the mode became active, so heading and track can differ. Alternative: a separate heading group, so the crew can select heading and track at the same time. | CONOPS §4.4; SC-060, SC-070, SC-080 |
| A2-Q04 | After fuel exhaustion, do the autoflight modes stay engaged? | Yes. Modes stay engaged and annunciated; FUEL EXHAUSTED is annunciated; no automatic disengagement. | CONOPS §4.5; SC-110 leg 10 |
| A2-Q05 | Can a mode group have no active mode? | No. Each group always has one active mode, or a hold mode covers it. The run's initial condition sets the starting modes. | CONOPS §4.4; all scenarios |
| A2-Q06 | What happens when FPA is selected with horizontal speed near zero? | FPA does not engage below P-AF-070; the active vertical mode stays as it was. | SC-040 variation |
| A2-Q07 | Refinement of Q5: do Position Hold and Hover also replace the speed group? | Yes, because both hold zero horizontal speed. | CONOPS §4.4; SC-090, SC-100 |
| A2-Q08 | Refinement of Q4: what happens when the vehicle passes over a VOR station? | Out of this cycle's scenarios. C6 and C5 define the behaviour; until then scenarios end before station passage. | SC-080, SC-110 leg 3 |
| A2-Q09 | In what crew-facing unit is fuel shown? D7 does not cover fuel. | Percent of full fuel capacity. | CONOPS §4.3; TM (C7) |
| A2-Q10 | How does the crew leave Position Hold or Hover? | By engaging a mode in any group. The groups not selected start in their hold mode at current values: ALT (current altitude), HDG (current heading), SPD (current horizontal speed). | SC-090 variation; SC-110 legs 2 and 8 |
| A2-Q11 | Which altitude does Hover hold? | The altitude at engagement, as Position Hold does. | SC-100 |
| A2-Q12 | Do scenario values (initial altitude, selected targets, leg durations) belong in the parameter database? | No. They are scenario variables set by the test procedures; the database holds system values only. | CONOPS §1.1; parameter database (B2) |

## Notes for the orchestrator

- **Worktree base.** This worktree's branch was created at `ff9d1a4`, before the plan, METHODOLOGY and the T0 skeleton existed. I fast-forwarded it to `b58cbe3` (T0) before starting, so the commit sits on top of T0. No conflict is expected; only `specs/CONOPS.md` and `work/A2/` are added.
- **Provisional annunciation labels.** CONOPS uses airliner-style short labels (FPA, V/S, ALT, ALT*, SPD, HDG, TRK, VOR, VOR*, POS HOLD, HOVER, LOW FUEL, FUEL EXHAUSTED) so the sequence tables are readable. C5 owns the final labels.
- **Position Hold numbering.** METHODOLOGY §12 uses `P-AF-012` for the position hold tolerance as an illustration. A2 proposes `P-AF-160` (steps of 10). M0 should use whatever B2 assigns.
- **Platform scenarios.** SC-200 to SC-240 describe how the TST and RVS use the Aeronef. They are included because several Aeronef needs (reproducibility, configuration, data output, release) are only visible in those uses. The TST and RVS requirements themselves are out of scope.
- **Information separation.** CONOPS is protected design material. It is not written as manual text; the manual authors (SH-09) will write their own operator-facing descriptions from the baselined requirements.
- **No conflicts with D1 to D7** found.
