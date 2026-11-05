# C2 — Parameter proposals (FU)

Parameters referenced by `work/C2/L2_FU.md`. The field layout follows `parameters/PARAMETERS.yaml`. A value is `null` while TBD; a proposed value is marked TBR. Owner Martin for each. Units are SI (CV-720); no FU parameter is crew-facing.

**IDs.** P-FU-010 to -060 exist and are reused with the same meaning (§1). P-FU-070 to -100 are new (§2). No FU ID has been withdrawn, so none is reused. The register rows TT-110, TT-120 and TT-130 cover P-FU-010 to -060; §3 proposes rows for the new IDs.

**Ranges.** The parameter database has no range field, so each range is in the `note`. FU relies on these ranges: L2-AER-FU-040 and -100 (the consumption rate is at least zero), L2-AER-FU-170 (the ratio to [P-FU-010]) and L2-AER-FU-190 (the tensors are physical). A future `param_check.py` range check could read them (suggestion for the orchestrator, not a request).

## 1. Existing parameters: proposed updates

The changes are to the description, the value, the status, the source and the note. The ID, name and unit are unchanged, except that the unit of P-FU-040 and P-FU-050 is confirmed as that of one linear coefficient each (DD-C2-01).

**Proposed value set (TBR).** B1 left P-FU-010, -030, -040, -050 and -060 TBD for C2 to set at G2 (TT-110, TT-120). C2 proposes one coherent set that closes the fuel budget of L2-AER-FU-290 for an assumed hover endurance [P-SYS-280] of 3600 s, which is the owner's to set (D47). With [P-FU-030] = 1000 kg, [P-FU-010] = 500 kg, [P-FU-100] = 0.05 and [P-DYN-010] = 9.80665 m/s², the budget needs [P-FU-040] ≤ ln(1.5) / (1.05 × 9.80665 × 3600) = 1.0938e-5 kg/(N·s). With [P-FU-040] = 1.09e-5 kg/(N·s), the capacity needed is 1000 × (exp(1.05 × 1.09e-5 × 9.80665 × 3600) − 1) = 497.9 kg ≤ 500 kg, and the closed-form still-air endurance is ln(1.5) / (1.09e-5 × 9.80665) = 3793 s. The hover fuel mass flow at maximum mass is then 0.160 kg/s. The masses are a placeholder scale for a small fictional craft; I1 rescales them with the effector authority budget (P-SYS-400 to -420) if needed. If the owner sets another [P-SYS-280], keep [P-FU-030] and [P-FU-010] and recompute [P-FU-040] from the same inequality (owner question C2-Q6).

```yaml
parameters:
  # --- FU (existing IDs, updated) ---
  - id: P-FU-010
    name: Usable fuel mass at full capacity
    description: Mass of usable fuel when the tank is full (fuel capacity). The largest valid initial fuel mass of a run (L1-AER-150, L2-AER-FU-030) and the initial fuel of the reference mission. The maximum vehicle mass is P-FU-030 + P-FU-010. Sized by the fuel budget of L2-AER-FU-290.
    unit: kg
    value: 500
    tolerance: null
    note: 'Range: greater than zero. Proposed with P-FU-030 and P-FU-040 as one set that meets L2-AER-FU-290 for P-SYS-280 = 3600 s (assumed; D47).'
    status: TBR
    source: CONOPS §4.5, SC-110; L1-AER-150, -360; L2-AER-FU-290; C2 proposal
    owner: Martin
  - id: P-FU-020
    name: Low-fuel threshold
    description: Fraction of the fuel capacity P-FU-010 below which the fuel state indicates low fuel and the low-fuel alert is annunciated (L1-AER-570, L2-AER-FU-220).
    unit: '1'
    value: 0.1
    tolerance: null
    note: 'Range: greater than zero and less than one.'
    status: TBR
    source: CONOPS §4.5; L1-AER-570; B1 proposal (D48)
    owner: Martin
  - id: P-FU-030
    name: Dry mass
    description: Vehicle mass with no fuel. The maximum vehicle mass is P-FU-030 + P-FU-010; the vehicle mass at fuel exhaustion is P-FU-030.
    unit: kg
    value: 1000
    tolerance: null
    note: 'Range: greater than zero. Placeholder scale; see the proposed value set in work/C2/param_proposals.md §1.'
    status: TBR
    source: L1-AER-180, -360; FUNCTIONAL_ANALYSIS §7.3; L2-AER-FU-110; C2 proposal
    owner: Martin
  - id: P-FU-040
    name: Translational fuel consumption coefficient
    description: Coefficient k_t of the translational consumption relationship of MS-DYN (DD-C2-01) - fuel mass flow per newton of the magnitude of the resultant control force. One coefficient, common to the effector set.
    unit: kg/(N*s)
    value: 1.09e-5
    tolerance: null
    note: 'Range: zero or more (zero switches off translational consumption, for model checks). Value from the fuel budget of L2-AER-FU-290 with P-SYS-280 = 3600 s (assumed). If the owner chooses per-effector consumption (C2-Q2), this becomes one coefficient per effector.'
    status: TBR
    source: L1-AER-170, -360; L0-CON-120; L2-AER-FU-040, -290; C2 proposal
    owner: Martin
  - id: P-FU-050
    name: Rotational fuel consumption coefficient
    description: Coefficient k_r of the rotational consumption relationship of MS-DYN (DD-C2-01) - fuel mass flow per newton metre of the magnitude of the resultant control moment about the centre of gravity. One coefficient, common to the effector set.
    unit: kg/(N*m*s)
    value: 1.09e-5
    tolerance: null
    note: 'Range: zero or more. Proposed equal in number to P-FU-040, so that a control moment of 1 N*m costs as much fuel as a control force of 1 N; rotation is then a small share of the reference-mission fuel. If the owner chooses per-effector consumption (C2-Q2), this becomes one coefficient per effector.'
    status: TBR
    source: L1-AER-170; L0-CON-120; L2-AER-FU-040; C2 proposal
    owner: Martin
  - id: P-FU-060
    name: Fuel mass accounting tolerance
    description: Largest difference between the remaining fuel mass of a simulation step and the initial fuel mass minus the sum, over the preceding steps, of the fuel mass flow times P-SYS-300 (L2-AER-FU-080). Covers the floating-point arithmetic of the model and of the independent check only. Also the tolerance on equal fuel and mass values in the FU tests.
    unit: kg
    value: 1.0e-6
    tolerance: null
    note: 'Range: greater than zero. About 2e-9 of P-FU-010, ample for double-precision sums over a reference mission of a few hours at P-SYS-300 = 0.01 s. Valid only if the check uses the flow of each simulation step (C2-Q3, IN-C2-30); an integration of output samples at P-TM-010 needs a larger value, set from a prototype run.'
    status: TBR
    source: L1-AER-190; METHODOLOGY §10.3; L2-AER-FU-080; C2 proposal
    owner: Martin
```

## 2. New parameters

```yaml
parameters:
  # --- FU (new) ---
  - id: P-FU-070
    name: Dry-mass principal moments of inertia
    description: Principal moments of inertia (Ixx, Iyy, Izz) of the dry mass about the centre of gravity, in the body axes, three components. Products of inertia are zero (D61; CV-350 sign convention). The inertia tensor at fuel exhaustion (L2-AER-FU-170). Derived in MS-DYN from the body shape and the dry-mass distribution with P-FU-030 (L2-AER-FU-190); not set independently.
    unit: kg*m^2
    value: null
    tolerance: null
    note: 'Range: each component greater than zero, and each at most the sum of the other two (triangle inequality of a physical body). Value TBD until C1 states the body shape and the distributions in MS-DYN.'
    status: TBD
    source: L1-AER-220; L0-CON-140; L2-AER-FU-170, -180, -190; MS-DYN (C1)
    owner: Martin
  - id: P-FU-080
    name: Full-fuel principal moments of inertia
    description: Principal moments of inertia (Ixx, Iyy, Izz) of the fuel at full capacity P-FU-010 about the centre of gravity, in the body axes, three components. Products of inertia are zero. The fuel share of the inertia tensor is this value times the ratio of the remaining fuel mass to P-FU-010 (L2-AER-FU-170; uniform depletion, DD-C2-02). Derived in MS-DYN from the fuel-mass distribution with P-FU-010 (L2-AER-FU-190); not set independently.
    unit: kg*m^2
    value: null
    tolerance: null
    note: 'Range: each component zero or more; all three zero gives an inertia that does not change with fuel (the alternative of C2-Q1). If MS-DYN gives the fuel the same uniform distribution as the dry mass (IN-C2-13), P-FU-080 = P-FU-070 x P-FU-010 / P-FU-030.'
    status: TBD
    source: L1-AER-220; L0-CON-140; L2-AER-FU-170, -180, -190; MS-DYN (C1, C2)
    owner: Martin
  - id: P-FU-090
    name: FU computation agreement tolerance
    description: Largest relative difference between an FU output (fuel mass flow, principal moment of inertia) and its independent computation from the recorded inputs, in the FU analyses and tests (AN-FU-040, -050, -170; DM-FU-010). Floating-point agreement only.
    unit: '1'
    value: 1.0e-9
    tolerance: null
    note: 'Range: greater than zero. A verification tolerance, kept in the database like P-FU-060 because the requirements cite it.'
    status: TBR
    source: L2-AER-FU-010, -040, -050, -170; C2 proposal
    owner: Martin
  - id: P-FU-100
    name: Hover endurance consumption margin
    description: Fraction by which the fuel mass flow in a still-air hold may exceed the translational term that balances the weight, used to size the fuel capacity P-FU-010 (L2-AER-FU-290). Covers the regulation of the hold, the attitude-holding moments and the transient at the start of the hold (FUNCTIONAL_ANALYSIS §7.3).
    unit: '1'
    value: 0.05
    tolerance: null
    note: 'Range: zero or more. Confirmed or resized at G2 from a prototype hover run (FC and EF).'
    status: TBR
    source: L1-AER-360; FUNCTIONAL_ANALYSIS §7.3; L2-AER-FU-290; C2 proposal
    owner: Martin
```

## 3. Register rows proposed for `registers/TBD_TBR.md`

| ID (orchestrator assigns) | Item | Type | Location | Owner | Closure date |
| --- | --- | --- | --- | --- | --- |
| TT-new-1 | Dry-mass and full-fuel principal moments of inertia, derived in MS-DYN | TBD | P-FU-070, P-FU-080 | Martin | G2 (C1, C2) |
| TT-new-2 | FU computation agreement tolerance 1e-9 and hover consumption margin 0.05 | TBR | P-FU-090, P-FU-100 | Martin | G2 (C2) |
| TT-110, TT-120 (update) | Status TBD → TBR with the C2 value set: dry mass 1000 kg, capacity 500 kg, k_t = k_r = 1.09e-5, accounting tolerance 1e-6 kg | TBR | P-FU-010, P-FU-030, P-FU-040, P-FU-050, P-FU-060 | Martin | G2 (I1, with P-SYS-280) |

## 4. Parameters cited but not owned by FU

P-SYS-300 (simulation step), P-SYS-120 (crew limit), P-SYS-280 (hover endurance), P-SYS-440 (vehicle acceleration), P-SYS-470 (annunciation latency), P-TM-010 (output sample period) and P-DYN-010 (gravity) are cited by ID only; no change is proposed.
