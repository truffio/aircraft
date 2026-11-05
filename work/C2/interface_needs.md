# C2 — Interface needs (FU)

What the FU requirements (`work/C2/L2_FU.md`) need from EF (C3), DYN and MS-DYN (C1) and the TST, and what FU gives to DYN, EF, FC, AF, FCP and TM. Interface IDs I-nn are those of FUNCTIONAL_ANALYSIS §3.2. "Boundary ICD" is the vehicle-model boundary ICD, whose home I1 decides (IN-B1-01, TT-720).

## 1. Summary of the FU interfaces

| Interface | Direction | Data (SI) | Rate | Defined in | FU record |
| --- | --- | --- | --- | --- | --- |
| I-01 | EF → FU | Effector outputs of the step | Each simulation step | MS-DYN | L2-AER-FU-070 |
| I-03 | FU → EF | Fuel availability (available / not available) | Each simulation step | MS-DYN | L2-AER-FU-200 |
| I-04 | FU → DYN | Vehicle mass (kg), centre-of-gravity position (m, body frame), inertia tensor (kg·m², body axes, diagonal) | Each simulation step | MS-DYN | L2-AER-FU-120 |
| I-05 | FU → FC | Mass properties (as I-04) | Each step; read at the first step of each control frame | Boundary ICD | L2-AER-FU-130, -140 |
| I-06 | FU → AF, FCP | Fuel state: remaining fuel mass (kg), low-fuel indication, fuel-exhaustion indication | Each step; read at the first step of each control frame | Boundary ICD; ICD-FCP refers to it | L2-AER-FU-130, -210 to -240 |
| I-21 | TST → FU | Fuel mass of the initial condition (kg); vehicle parameter set | Start of run | ICD-AER-TST | L2-AER-FU-010, -020, -030 |
| (new) | FU → TST | Initial-condition error naming the fuel mass | Start of run | ICD-AER-TST | L2-AER-FU-030 |
| I-31 | FU → TM | Fuel mass flow (kg/s), vehicle mass (kg), remaining fuel mass (kg) | Each step; sampled at each output sample | ICD-AER-TST | L2-AER-FU-250, -260 |

FU takes nothing from the flight software and nothing from the flight control panel.

## 2. Needs from C1 (DYN, MS-DYN)

| ID | Need | Why | FU records |
| --- | --- | --- | --- |
| IN-C2-10 | **Consumption relationships (please put in MS-DYN, fuel section).** For simulation step k, with `F_c(k)` the resultant control force and `M_c(k)` the resultant control moment about the centre of gravity, both from the effector outputs of step k: consumption rate `q(k) = k_t · ‖F_c(k)‖ + k_r · ‖M_c(k)‖`, with `k_t = [P-FU-040]` (kg/(N·s)) and `k_r = [P-FU-050]` (kg/(N·m·s)), Euclidean norms. Name the two terms "translational consumption term" and "rotational consumption term". | The form is C2's decision, recorded in MS-DYN (L1-AER-160; DD-110). Linear terms give the closed-form hover endurance; zero output gives zero flow. | L2-AER-FU-040, -060, -290 |
| IN-C2-11 | **One mapping from effector outputs to control force and moment.** MS-DYN states once how the effector outputs of a step give `F_c` and `M_c` (through the EF control effectiveness, about the centre of gravity), and both the equations of motion and the consumption relationships use it. | The fuel used and the motion must come from the same forces (L2-AER-FU-070). | L2-AER-FU-070 |
| IN-C2-12 | **Fuel accounting.** `ṁ_f(k) = min(q(k), m_f(k) / Δt)` with `Δt = [P-SYS-300]`; `m_f(k+1) = m_f(k) − ṁ_f(k) · Δt`; `m_f(0)` = fuel mass of the initial condition. This assumes the effector output is one value per step (glossary *Effector output*); if C1 or C3 let it vary within a step, tell C2, because the accounting then needs the integral over the step. | Exact fuel integral; fuel exactly zero at exhaustion (DD-130). | L2-AER-FU-050, -080, -090 |
| IN-C2-13 | **Mass distributions and inertia derivation.** State the dry-mass distribution and the fuel-mass distribution, each symmetric about the three body axes with its centre of mass at the body-frame origin. C2 recommends: the dry mass as a uniform solid of the body shape; the fuel as a uniform fill of a fixed fuel volume centred on the centre of gravity and coaxial with the body, whose density falls in proportion to the remaining fuel mass (uniform depletion, no slosh, L0-ASM-080). The simplest choice is a fuel volume equal to the body shape, which gives `[P-FU-080] = [P-FU-070] · [P-FU-010] / [P-FU-030]`. Derive the three principal moments of `[P-FU-070]` (dry) and `[P-FU-080]` (fuel at full capacity) from the shape dimensions (DYN parameters). | L1-AER-220 asks MS-DYN to derive the inertia from the shape and the distribution; FU needs the two tensors (DD-120). | L2-AER-FU-160, -170, -180, -190 |
| IN-C2-14 | **Mass properties in the equations of motion.** Vehicle mass `m(k) = [P-FU-030] + m_f(k)`; inertia `J(k) = [P-FU-070] + [P-FU-080] · m_f(k) / [P-FU-010]`, diagonal; centre of gravity at the body-frame origin. The equations of motion use `m(k)` and `J(k)` with no thrust term and no `dJ/dt · ω` term: consumed fuel leaves with no force or moment and carries its own momentum (L0-ASM-090). That is, `m · dv/dt = F` and `J · dω/dt + ω × (J · ω) = M`. | Variable-mass equations consistent with L0-ASM-090. | L2-AER-FU-110, -120, -170 |
| IN-C2-15 | **Fuel availability to EF.** Available at step k when `m_f(k) > 0`, not available when `m_f(k) = 0`. | L1-AER-200 (zero output at exhaustion). | L2-AER-FU-200 |
| IN-C2-16 | **Credibility checks (METHODOLOGY §10.3).** (a) Fuel-mass integral: the independent summation of AN-FU-080. (b) Steady hover in still air: `m(t) = m_0 · exp(−k_t · g · t)` and the endurance `ln(m_0 / [P-FU-030]) / (k_t · g)`, an independent solution for N-290 (AN-FU-290). (c) Torque-free rotation: with zero control moment and force the fuel mass flow is zero, so `J` is constant and the angular momentum is conserved as the check expects. (d) Free fall from exhaustion: the vehicle mass is `[P-FU-030]` and constant. | Lets the MS-DYN checks cover the fuel model. | L2-AER-FU-040, -080, -290 |
| IN-C2-17 | MS-DYN sections for the five FU models of L2-AER-FU-280: consumption relationships, fuel accounting, fuel availability, vehicle mass and centre of gravity, inertia. | L1-AER-720. | L2-AER-FU-280 |
| IN-C2-18 | Glossary: C1 may also propose a term for the DYN subsystem. C2 proposes *Dynamics subsystem* (`glossary_proposals.md`); the orchestrator merges one. | Avoid two names. | L2-AER-FU-070, -120 |

## 3. Needs from C3 (EF)

| ID | Need | Why | FU records |
| --- | --- | --- | --- |
| IN-C2-20 | EF produces zero control force and zero control moment while the fuel availability is not available, from the first simulation step at which FU gives not available (the EF child of L1-AER-200). In a step that starts with fuel available, EF produces its commanded output for the whole step; FU limits the fuel used in that step (L2-AER-FU-050). | Closes L1-AER-200 between EF and FU. | L2-AER-FU-200 |
| IN-C2-21 | EF gives FU its effector outputs at each simulation step (I-01), one value per effector per step. | Input of the consumption rate. | L2-AER-FU-070 |
| IN-C2-22 | EF defines no consumption parameter of its own: the fifth kind of L1-AER-100 is FU's (`[P-FU-040]`, `[P-FU-050]`). | L1-AER-100 closed list. | L2-AER-FU-060 |
| IN-C2-23 | EF's child of L1-AER-360 shows that, in a still-air hold at level attitude, the resultant control force is the weight and the resultant control moment is zero, within the margin `[P-FU-100]`. With the C2 consumption form, effector waste (opposing effectors) costs no fuel, so EF's share is only the resultant. | The fuel budget closes only with both shares (L2-AER-FU-290). | L2-AER-FU-290 |

## 4. Needs from the TST and from I1 (ICD-AER-TST, boundary ICD)

| ID | Need | Why | FU records |
| --- | --- | --- | --- |
| IN-C2-31 | **ICD-AER-TST:** an initial-condition error item from the Aeronef to the TST, naming the item and its value; the TST does not start the run. | Range check of the initial fuel mass. | L2-AER-FU-030 |
| IN-C2-32 | **ICD-AER-TST:** the initial fuel mass in kg (I-21), and the vehicle parameter set carrying P-FU-010 to -100. | Initialisation. | L2-AER-FU-010, -020 |
| IN-C2-33 | **ICD-AER-TST:** operational data signals "fuel mass flow" (kg/s), "vehicle mass" (kg), "remaining fuel mass" (kg). Fuel alerts as event records, if TM chooses (glossary *Event record*): the low-fuel and exhaustion indications of the fuel state change once each per run, at most. | L1-AER-630, -640. | L2-AER-FU-250, -260 |
| IN-C2-34 | **Boundary ICD:** the mass-properties items (vehicle mass, centre-of-gravity position as a body-frame vector, inertia tensor with three principal moments and zero products) and the fuel-state item (remaining fuel mass in kg, low-fuel indication, fuel-exhaustion indication), defined once; ICD-FCP refers to the fuel-state definition. | L1-AER-430, -880. | L2-AER-FU-130, -240 |
| IN-C2-30 | **TST recording for analysis runs:** the FU analyses AN-FU-050 and AN-FU-080, and the tests that read outputs not in the operational data (centre of gravity, inertia tensor, fuel availability: IN-FU-150 is by inspection, but TP-FU-140, AN-FU-170 and TP-FU-200 read them), need the FU outputs at each simulation step or at the boundary. Recommended: the TST records the vehicle-model interfaces at each simulation step for these runs, without changing the Aeronef configuration (owner question C2-Q3). | The fuel integral is exact only at the step; the operational data hold neither the inertia nor the availability (L1-AER-640 closed list). | L2-AER-FU-050, -080, -140, -170, -200 |

## 5. Given by FU to the other subsystems

| To | What FU gives | Where | Note |
| --- | --- | --- | --- |
| DYN (C1) | Vehicle mass, centre of gravity (body-frame origin), diagonal inertia tensor, each simulation step | MS-DYN (I-04) | The inertia changes with fuel (C2-Q1). |
| EF (C3) | Fuel availability, each simulation step | MS-DYN (I-03) | Not available from the first step with zero fuel to the end of the run. |
| FC (C4) | Mass properties of each step, the same vehicle mass that DYN uses (L2-AER-FU-140) | Boundary ICD (I-05) | **IN-C2-41 (bound for the crew limit).** FC reads the mass at the frame start; within one control frame the mass falls by the fuel used in that frame. The relative fall is at most `(k_t · ‖F_c‖ + k_r · ‖M_c‖) · [P-SYS-310] / m`. With `‖F_c‖ / m` bounded by the crew limit, the translational part is at most `[P-FU-040] · [P-SYS-120] · [P-SYS-310]`, about 6.4e-6 with the proposed values, so the sensed acceleration can exceed the frame-start value by that fraction. FC covers it inside the margin of FUNCTIONAL_ANALYSIS §7.2. The maximum inertia for the moment budget is `[P-FU-070] + [P-FU-080]` (full fuel), the minimum `[P-FU-070]` (exhaustion). |
| AF (C5) | Fuel state (remaining fuel mass, low-fuel and fuel-exhaustion indications) | Boundary ICD (I-06) | For #59 (modes after exhaustion), see C2-Q5. The exhaustion indication is set from the first step with zero fuel. |
| FCP (C8) | Fuel state, in SI | ICD-FCP, by reference to the boundary ICD (I-06) | **IN-C2-43.** FCP converts the remaining fuel mass to lb (CV-750) and presents the indication; it annunciates the low-fuel alert and the fuel exhaustion. Both indications are set at exhaustion; FCP decides which annunciation it shows then (C2 suggests that fuel exhaustion replaces the low-fuel alert). FU's share of `[P-SYS-470]` is zero: FU sets each indication in the step in which its condition first holds. |
| TM (C7) | Fuel mass flow, vehicle mass, remaining fuel mass of each step | ICD-AER-TST (I-31) | Releasable or protected classification with the RVS (#69). |
| I1 | Maximum vehicle mass `[P-FU-030] + [P-FU-010]` = 1500 kg (proposed) for `[P-SYS-400]`, `[P-SYS-410]`; maximum inertia `[P-FU-070] + [P-FU-080]` for `[P-SYS-420]`, once C1 derives it; the fuel budget of FUNCTIONAL_ANALYSIS §7.3 confirmed, with the margin `[P-FU-100]` added (L2-AER-FU-290). | FUNCTIONAL_ANALYSIS §7.1, §7.3 | Budget closure. |
