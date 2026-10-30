# A1 — Issues, notes and questions for the project owner

## 1. Questions for the project owner

Each has a proposed answer. The L0 drafts are written to the proposed answer unless stated.

| ID | Question | Proposed answer | Affects |
| --- | --- | --- | --- |
| Q-A1-01 | "Avoid coupling between axes" (OBJECTIVES §2): does it exclude only aerodynamic coupling, or also rigid-body inertial (gyroscopic) coupling and the attitude dependence of body-fixed effector forces seen in the local frame? | Exclude aerodynamic coupling only (L0-CON-030). Keep the full rigid-body equations; inertial coupling is physics, and handling it is a flight-control task. MS-DYN (C1) may choose a diagonal inertia tensor to reduce it. | L0-CON-030 (TBR), MS-DYN, FC |
| Q-A1-02 | "Each emitter acts in a fixed direction": fixed relative to the vehicle body, or fixed in the local (Earth) frame? | Fixed relative to the body (no gimballing). | L0-CON-070 (TBR), EF, FC allocation |
| Q-A1-03 | Is there a ground? What happens when the vehicle reaches the altitude datum, for example after fuel exhaustion? | No ground contact model; the vehicle is airborne in every scenario and a run ends when altitude reaches the datum (L0-ASM-110). | L0-ASM-110, MS-DYN, TST termination, ConOps fuel-exhaustion mission |
| Q-A1-04 | How many flight-control-law designs and autoflight implementations must be compared? | 2 each (P-SYS-010, P-SYS-020, TBR). | L0-OBJ-040, -050, L0-SUC-080, -090 |
| Q-A1-05 | Reproducibility: bit-identical on the same host and build, or within a tolerance across different hosts? | Bit-identical on the same execution host and build (P-SYS-040 = 0); cross-host reproduction not required. | L0-SUC-040, L0-ASM-020 |
| Q-A1-06 | Required verification pass fraction for the reference configuration? | 1.0 (each baselined requirement passes in the reference configuration); alternative configurations are not held to it. | L0-SUC-020 (P-SYS-030) |
| Q-A1-07 | Scale of the parallel campaigns and the execution host: one multi-core workstation, or a cluster? | One host (L0-ASM-130); campaign of 10 000 runs (P-SYS-050); parallel efficiency 0.8 (P-SYS-060) at the host's physical core count, 8 TBR (P-SYS-070). | L0-OBJ-090, L0-SUC-050, -060 |
| Q-A1-08 | Set the reverse-engineering success thresholds (P-SYS-080 to P-SYS-110) now, or when the RVS requirements and scoring rules are written? | Defer to the RVS L1 baseline; keep TBD with closure 2027-01-31. Setting them before the scoring rules exist would be arbitrary. | L0-SUC-100 to -130 |
| Q-A1-09 | Air density: constant, or a function of altitude? | Function of altitude only, time-invariant (L0-ASM-060); constant versus standard atmosphere chosen in MS-DYN (C1). | L0-ASM-060, MS-DYN drag model |
| Q-A1-10 | The plan has no calendar. What closure dates should TBD/TBR items carry? | Proposed: G1 items 2026-11-30; TST-scale items 2026-12-31; RVS thresholds 2027-01-31. Replace with gate dates when the owner sets them. | All TBD/TBR fields |
| Q-A1-11 | Must any autoflight implementation run with any flight-control-law design (a full cross-product), or are they paired? | Any-with-any, through ICD-FC-AF; this is what makes L0-SUC-080 and L0-SUC-090 independent comparisons. Not written as an L0 requirement; proposed for B1 at L1. | L0-CON-200, -210, ICD-FC-AF |
| Q-A1-12 | The plan's ICD list has no interface for the evidence package (AER/TST → RVS), which METHODOLOGY §7 lists as needed early. Add one? | Yes: `icd/ICD-EVIDENCE.md` (or as part of the RVS L1), owned by the orchestrator, defining released items and release records. | L0-CON-220, -230, -240 |
| Q-A1-13 | L0 has 66 requirements plus 14 assumptions; METHODOLOGY §4 says 10–20 statements is typical. Accept, or move some constraints to L1? | Accept. The count comes from the one-thought rule applied to the concept boundaries; each constraint is separately traceable and challengeable. Candidates to move to L1 if wanted: L0-CON-260, -270, -280 (units, conventions) and L0-CON-170 (crew interface). | Whole L0 |
| Q-A1-14 | No L1 element owns project-level deliverables: the method assessment (L0-OBJ-210) and the final report (L0-SUC-170). Who owns them? | Allocate to AER, TST and RVS, each contributing its section; the orchestrator compiles the report. | L0-OBJ-210, L0-SUC-170 |
| Q-A1-15 | METHODOLOGY §4.4: assumptions must be confirmed or turned into requirements before L1 is baselined. Confirm L0-ASM-010 to L0-ASM-140 at G0/G1? | Confirm all 14 at G1; L0-ASM-010 (perfect state knowledge) and L0-ASM-070 (no failures) stay assumptions for this cycle by design. | L0-ASM register |

## 2. Notes for the orchestrator and the tooling (T1)

- **Verification procedure IDs.** Every L0 record has `Verification: <method> — TBD; success criteria: ...`. The method and criteria are set; procedure IDs (IN-/AN-/DM-/TP-nnn) are left to V4 (Phase 5). These TBDs are not listed in the TBD/TBR field, which holds only technical open items. The lint should not treat a TBD procedure ID as a missing TBD/TBR entry.
- **Sufficiency line.** L0 records have no parent, so the `Sufficiency:` continuation line of the template is omitted.
- **Digits in statements.** Statements contain no numbers except inside identifiers: level names (L0, L1 in L0-OBJ-180, -190, L0-SUC-170) and the standard number AIAA R-004-1992 (L0-CON-280). Spelled-out counts that define the concept ("six degrees of freedom") are kept as words. The lint should allow identifiers.
- **Subject.** Every L0 statement has "The Aeronef project" as subject (METHODOLOGY §4.3).
- **Allocated to** uses the L1 element codes AER, TST, RVS.
- **Statements with "and".** The remaining "and"/"or" in statements are closed enumerations of a single object (for example the external effects in L0-CON-090, the test categories in L0-SUC-070), not two requirements.
- **Spelling.** British spelling, as in METHODOLOGY (centre, behaviour, modelled). AIRCRAFT_CHARACTERISTICS uses "center"; see glossary_proposals.md.
- **Worktree base.** This worktree was created at commit ff9d1a4, before T0. It was fast-forwarded to b58cbe3 (T0) before work started, so the commit sits on top of T0.

## 3. Design content kept out of L0 (for B1, C1–C3)

- **Inertial coupling.** With a non-spherical inertia tensor, the rigid-body term ω × Iω couples the rotational axes even without aerodynamics; for an axisymmetric "Tic Tac" it vanishes only when the rotation is about the symmetry axis or there is no spin. C1/C4 decision (see Q-A1-01).
- **Body-fixed effectors and attitude.** A body-fixed force seen in the local frame depends on attitude, so translation commands in the local frame need attitude-dependent allocation. This is a flight-control allocation design item, not an L0 constraint.
- **Inertia versus fuel state.** Whether the moments of inertia change as fuel burns (with a fixed centre of gravity) is left to C2.
- **Drag model.** Whether drag depends on attitude relative to the velocity (elongated body) or is defined per axis is an MS-DYN choice, bounded by L0-CON-030.
- **Closed list of onboard functions.** A constraint limiting the Aeronef's modelled functions to force generation, fuel supply, flight control, autoflight, navigation and operational data output was considered and left out: it is L1 architecture (B1).
- **Effector layout** is a design decision (plan §6, C3), not an L0 constraint.

## 4. Change requests to the parent level

None. L0 is the top level.

## 5. Derived requirements

None. All L0 records trace to the project input documents.
