# A1 — Parameter proposals (P-SYS)

New system-level parameters referenced by the L0 requirements. Field layout follows `parameters/PARAMETERS.yaml`. Proposed values are marked TBR; `value: null` where no proposal is made (TBD). Closure dates are proposals (see issues.md, Q-A1-10).


**Withdrawn at the G0 owner review (2026-10-25)**, because no live requirement uses them any more: P-SYS-010, -020 (design counts; OBJ-040/-050 and SUC-080/-090 deleted), P-SYS-030 (pass fraction; every requirement must pass), P-SYS-040 (reproduction tolerance; D25), P-SYS-050 (campaign size; #68), P-SYS-080, -090, -100, -110 (replaced by 100% coverage, D39). B2 must not seed them.

```yaml
- id: P-SYS-010
  name: Minimum number of flight-control-law designs
  description: Minimum number of distinct flight-control-law designs developed and compared on the Aeronef.
  unit: "1"
  value: 2
  tolerance: null
  status: TBR
  source: L0-OBJ-040, L0-SUC-080 (OBJECTIVES.md §2, §6)
  owner: Martin

- id: P-SYS-020
  name: Minimum number of autoflight implementations
  description: Minimum number of distinct autoflight implementations developed and compared on the Aeronef.
  unit: "1"
  value: 2
  tolerance: null
  status: TBR
  source: L0-OBJ-050, L0-SUC-090 (OBJECTIVES.md §2, §6)
  owner: Martin

- id: P-SYS-030
  name: Required verification pass fraction, reference configuration
  description: Minimum fraction of baselined Aeronef requirements with a passing last verification result in the reference configuration.
  unit: "1"
  value: 1.0
  tolerance: null
  status: TBR
  source: L0-SUC-020 (OBJECTIVES.md §6)
  owner: Martin

- id: P-SYS-040
  name: Run reproduction tolerance
  description: Maximum relative difference between each output of a re-executed test run and the recorded output, given the recorded configuration, software version and inputs. 0 means bit-identical on the same execution host.
  unit: "1"
  value: 0
  tolerance: null
  status: TBR
  source: L0-SUC-040 (OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §5)
  owner: Martin

- id: P-SYS-050
  name: Minimum campaign size
  description: Minimum number of simulation runs in one automated test campaign executed as a single batch without operator action.
  unit: "1"
  value: 10000
  tolerance: null
  status: TBR
  source: L0-SUC-050 (OBJECTIVES.md §3, §6)
  owner: Martin

- id: P-SYS-060
  name: Minimum parallel efficiency
  description: Minimum parallel efficiency (single-instance campaign duration divided by the product of the parallel campaign duration and the number of instances) at P-SYS-070 instances.
  unit: "1"
  value: 0.8
  tolerance: null
  status: TBR
  source: L0-SUC-060 (OBJECTIVES.md §3; TESTING_ENVIRONMENT.md §5)
  owner: Martin

- id: P-SYS-070
  name: Parallel instances for efficiency demonstration
  description: Number of parallel simulation instances at which the parallel efficiency is measured. Proposed equal to the physical core count of the execution host (L0-ASM-130).
  unit: "1"
  value: 8
  tolerance: null
  status: TBR
  source: L0-SUC-060
  owner: Martin

- id: P-SYS-080
  name: Required mode identification fraction
  description: Minimum fraction of the autoflight modes in the baselined mode catalogue that the reconstructed model identifies. Scoring rule set in the REE requirements.
  unit: "1"
  value: null
  tolerance: null
  status: TBD
  source: L0-SUC-100 (REVERSE_ENGINEERING.md §6)
  owner: Martin

- id: P-SYS-090
  name: Required mode transition reproduction fraction
  description: Minimum fraction of the autoflight mode transitions in the protected mode logic that the reconstructed model reproduces (source mode, destination mode and triggering condition match).
  unit: "1"
  value: null
  tolerance: null
  status: TBD
  source: L0-SUC-110 (REVERSE_ENGINEERING.md §6)
  owner: Martin

- id: P-SYS-100
  name: Required prediction fraction on withheld scenarios
  description: Minimum fraction of withheld assessment scenarios whose observed outcome the reconstructed model predicts correctly. Correctness criterion set in the REE requirements.
  unit: "1"
  value: null
  tolerance: null
  status: TBD
  source: L0-SUC-120 (REVERSE_ENGINEERING.md §6)
  owner: Martin

- id: P-SYS-110
  name: Required requirement coverage fraction
  description: Minimum fraction of the baselined Aeronef system (L1) requirements that the reconstructed model covers, scored against the manual trace register.
  unit: "1"
  value: null
  tolerance: null
  status: TBD
  source: L0-SUC-130 (REVERSE_ENGINEERING.md §6; METHODOLOGY.md §11.2)
  owner: Martin

- id: P-SYS-120
  name: Maximum crew-sensed acceleration magnitude
  description: Maximum magnitude of the acceleration sensed by the crew (specific force; non-gravitational forces divided by current mass), set to protect the crew from excessive g load (D38).
  unit: m/s^2
  value: 29.41995
  tolerance: null
  note: 3 g (3 x 9.80665 m/s^2), owner value 'for now' (2026-10-25); applies in any direction
  status: TBR
  source: L0-CON-310 (owner review at G0, 2026-10-25)
  owner: Martin
```

## TBD/TBR register entries to open (for B2 / orchestrator)

| Item | Type | Location | Owner | Proposed closure |
| --- | --- | --- | --- | --- |
| Count of flight-control-law designs | TBR | P-SYS-010 (L0-OBJ-040, L0-SUC-080) | Martin | 2026-11-30 (G1) |
| Count of autoflight implementations | TBR | P-SYS-020 (L0-OBJ-050, L0-SUC-090) | Martin | 2026-11-30 (G1) |
| Verification pass fraction | TBR | P-SYS-030 (L0-SUC-020) | Martin | 2026-11-30 (G1) |
| Reproduction tolerance | TBR | P-SYS-040 (L0-SUC-040) | Martin | 2026-11-30 (G1) |
| Campaign size | TBR | P-SYS-050 (L0-SUC-050) | Martin | 2026-12-31 (STP L1) |
| Parallel efficiency | TBR | P-SYS-060 (L0-SUC-060) | Martin | 2026-12-31 (STP L1) |
| Parallel instance count | TBR | P-SYS-070 (L0-SUC-060) | Martin | 2026-12-31 (STP L1) |
| Mode identification fraction | TBD | P-SYS-080 (L0-SUC-100) | Martin | 2027-01-31 (REE L1) |
| Transition reproduction fraction | TBD | P-SYS-090 (L0-SUC-110) | Martin | 2027-01-31 (REE L1) |
| Prediction fraction | TBD | P-SYS-100 (L0-SUC-120) | Martin | 2027-01-31 (REE L1) |
| Coverage fraction | TBD | P-SYS-110 (L0-SUC-130) | Martin | 2027-01-31 (REE L1) |
| Scope of excluded coupling | TBR | L0-CON-030 | Martin | 2026-11-30 (G1) |
| Body-fixed effector direction | TBR | L0-CON-070 | Martin | 2026-11-30 (G1) |
| Elongated body shape | TBR | L0-CON-140 | Martin | 2026-11-30 (G1) |
