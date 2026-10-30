# A1 — Parameter proposals (P-SYS)

New system-level parameters referenced by the live L0 requirements. Field layout follows `parameters/PARAMETERS.yaml`. Proposed values are marked TBR; `value: null` where no proposal is made (TBD). B2 seeds the parameters in the YAML block below and opens the register entries in the table, and nothing else.

```yaml
- id: P-SYS-060
  name: Minimum parallel efficiency
  description: Minimum parallel efficiency (single-instance campaign duration divided by the product of the parallel campaign duration and the number of instances) at P-SYS-070 instances.
  unit: "1"
  value: 0.8
  tolerance: null
  status: TBR
  source: L0-SUC-060 (Draft, deferred with #86; OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §5)
  owner: Martin

- id: P-SYS-070
  name: Parallel instances for efficiency demonstration
  description: Number of parallel simulation instances at which the parallel efficiency is measured. Proposed equal to the physical core count of the execution host (L0-ASM-130).
  unit: "1"
  value: 8
  tolerance: null
  status: TBR
  source: L0-SUC-060 (Draft, deferred with #86)
  owner: Martin

- id: P-SYS-120
  name: Maximum crew-sensed acceleration magnitude
  description: Maximum magnitude of the acceleration sensed by the crew while airborne (specific force; non-gravitational forces divided by current mass), set to protect the crew from excessive g load (D38).
  unit: m/s^2
  value: 29.41995
  tolerance: null
  note: 3 g (3 x 9.80665 m/s^2), owner value 'for now' (2026-10-25); applies in any direction, gravity included in the load felt
  status: TBR
  source: L0-CON-310 (owner review at G0, 2026-10-25)
  owner: Martin
```

## TBD/TBR register entries to open (for B2 / orchestrator)

Taken from the TBD/TBR fields of the live L0 records after the G0 rework (2026-10-27).

| Item | Type | Location | Owner | Proposed closure |
| --- | --- | --- | --- | --- |
| Crew acceleration limit | TBR | P-SYS-120 (L0-CON-310) | Martin | G1 |
| Treatment of rigid-body kinematic terms | TBR | L0-CON-030 (#81) | Martin | G2 (C1) |
| Elongated body shape | TBR | L0-CON-140 | Martin | 2026-11-30 (G1) |
| Landing envelope limits | TBD | L0-CON-290 | Martin | G2 |
| Per-effector maximum force | TBD | L0-CON-300 | Martin | G2 (C3) |
| Parallel efficiency | TBR | P-SYS-060 (L0-SUC-060, Draft) | Martin | When parallel execution is picked up (#86) |
| Parallel instance count | TBR | P-SYS-070 (L0-SUC-060, Draft) | Martin | When parallel execution is picked up (#86) |
| RVS scoring rules | TBD | L0-SUC-100 to -130 | Martin | When the plan is extended to RVS (D44, #69) |

## Withdrawn

Withdrawn at the G0 owner review (2026-10-25), because no live requirement uses them: P-SYS-010 and -020 (design counts; L0-OBJ-040, -050 and L0-SUC-080, -090 deleted), P-SYS-030 (pass fraction; every requirement must pass, D26), P-SYS-040 (reproduction tolerance; D25), P-SYS-050 (campaign size; #68), and P-SYS-080 to -110 (replaced by 100% coverage, D39). Their IDs are not reused. The TBRs on the coupling scope (L0-CON-030, D18) and the body-fixed effector direction (L0-CON-070, D19) are closed.
