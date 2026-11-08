# C2 — Proposed MS-DYN content: mass-properties model (§6) and fuel model (§7.2)

**Status:** proposal by task C2 for merge into `specs/MS-DYN.md` at I1. C1 owns MS-DYN; C2 does not edit it (plan §5, §7). This file fills the two C2 content slots, "§6 C2 content slot" and "§7.2 C2 content slot", and proposes the C2 wording of check C-8 and of the FU rows of §12 and §13. It replaces the equations that `interface_needs.md` IN-C2-10 to -16 gave in the first C2 draft.

**Basis:** DD-110, DD-120, DD-130, DD-140 (accepted, D65); D66, D68, D69, D72, D73; DD-190 (EF computes the resultant once); DD-260 to DD-280 (`issues.md` §4). **Requirements:** L2-AER-FU-040, -050, -080, -110, -150 to -200, -300 to -340 (`L2_FU.md`).

**Structure (G2-F16).** One subsection per model listed in L2-AER-FU-280, so that the MS-DYN slots and that record match: §6.1 vehicle mass and centre of gravity, §6.2 and §6.3 inertia (with the mass distributions it rests on), §7.2.1 consumption relationships, §7.2.2 fuel accounting, §7.2.3 fuel availability. §6.4, §6.5 and §7.2.4 are supporting text.

**Notation.** Step index `k`, step `Δt = [P-SYS-300]`. `m_f(k)`: remaining fuel mass at the start of step `k` (CV-840). `F_c^B(k)`, `M_c^B(k)`: the control force and the control moment about the centre of gravity, in body axes, that EF gives for step `k` (§7.1, DD-190). `‖·‖`: Euclidean norm. `fl(·)`: the floating-point result of an expression.

---

## 6. Mass-properties model (content for the C2 slot)

Replace the paragraph "What DYN needs from FU, at each step `k` (IN-C1-01, IN-C1-02)" and its three bullets with §6.0 below, keep the "Reference derivation" paragraph as §6.3's derivation, and replace the "C2 content slot" sentence with §6.1 to §6.5.

### 6.0 What crosses the FU-to-DYN interface (I-04)

At each step `k`, FU gives DYN (L2-AER-FU-120):

- the vehicle mass `m(k)` (§6.1);
- the inertia tensor `J(k)`, given as its three principal moments `I_xx(k)`, `I_yy(k)`, `I_zz(k)` about the centre of gravity in the body axes, with zero products of inertia (§6.3, D61, CV-350). DYN calls these the principal moments of inertia (L2-AER-DYN-040, -210); they are the same item.

The centre-of-gravity position does not cross I-04 (G2-F05). It is the body-frame origin at every fuel state (§6.1), which DYN uses by definition (CV-160, L2-AER-DYN-200). FU gives it, as the zero vector, only as a mass-properties item at the vehicle-model boundary to flight control (L2-AER-FU-130, -150; FUNCTIONAL_ANALYSIS I-04 and I-05 as aligned by CR-B3-39).

FU also gives DYN the fuel availability `φ(k)` over interface I-03, for the ground contact model (§7.2.3, §9).

### 6.1 Vehicle mass and centre of gravity

```
m(k)   = [P-FU-030] + m_f(k)                              (L2-AER-FU-110)
r_CG   = (0, 0, 0)  in body axes, for every m_f(k)         (L2-AER-FU-150)
```

Both distributions of §6.2 have their centre of mass at `O_B`, so the centre of gravity of the vehicle stays at `O_B` as the fuel is consumed (L0-CON-130, L1-AER-210). The maximum vehicle mass is `m_max = [P-FU-030] + [P-FU-010]`; the vehicle mass at fuel exhaustion is `[P-FU-030]`.

### 6.2 Mass distributions (DD-120, DD-280)

- **Dry mass.** `[P-FU-030]` distributed with uniform density over the solid capsule of §2.1 (length `[P-DYN-020]`, diameter `[P-DYN-030]`).
- **Fuel.** The remaining fuel `m_f` distributed with uniform density over the same capsule, a fixed fuel volume equal to the body shape. The density is `m_f` divided by the capsule volume, so the fuel depletes uniformly (DD-120) and its centre of mass stays at `O_B`. There is no slosh (L0-ASM-080).
- **Symmetry.** Both distributions are symmetric under reflection in each body coordinate plane and axisymmetric about `x_B`, so the tensor is diagonal and `I_yy = I_zz`.
- **Landing gear.** The landing gear has no mass and no inertia (L1-AER-900, glossary *Landing gear*). It is in neither distribution, and the gear position enters no mass property (L2-AER-FU-310).

The choice of the capsule as the fuel volume (DD-280) needs no fuel-volume parameter (G2-F16). Any other fuel volume centred on `O_B` and symmetric about the body axes would also meet L2-AER-FU-160; it would add dimension parameters and change `[P-FU-080]` only.

### 6.3 Inertia model

**Derivation.** For mass `m` with uniform density over the capsule (radius `R = [P-DYN-030]/2`, cylinder length `H = [P-DYN-020] − [P-DYN-030]`), the reference derivation above gives `I_xx(m)` and `I_yy(m) = I_zz(m)`, both proportional to `m`. Then (L2-AER-FU-190):

```
[P-FU-070] = ( I_xx([P-FU-030]), I_yy([P-FU-030]), I_zz([P-FU-030]) )     dry mass
[P-FU-080] = ( I_xx([P-FU-010]), I_yy([P-FU-010]), I_zz([P-FU-010]) )     fuel at full capacity
           = [P-FU-070] · [P-FU-010] / [P-FU-030]                         (same shape, DD-280)
```

**Values** (12 m × 4 m capsule, TBR with the shape, TT-740; dry mass 1000 kg, capacity 500 kg, TBR): `R = 2 m`, `H = 8 m`; the cylinder holds `H/(H + 4R/3) = 0.75` of the mass and each hemisphere `0.125`.

| Tensor | I_xx (kg·m²) | I_yy = I_zz (kg·m²) |
| --- | --- | --- |
| `[P-FU-070]`, dry mass 1000 kg | 1 900 | 10 650 |
| `[P-FU-080]`, fuel 500 kg at full capacity | 950 | 5 325 |
| Full fuel, `[P-FU-070] + [P-FU-080]` (maximum, for `[P-SYS-420]`) | 2 850 | 15 975 |

The G2 inspector rederived the dry values (G2 §3.1), and C3 uses the full-fuel values for the moment budget (`work/C3/ms_dyn_s7_effectors.md`). Each principal moment is at most the sum of the other two (2 850 ≤ 31 950; 15 975 ≤ 18 825), as a physical body requires.

**Inertia at each step** (L2-AER-FU-170):

```
J(k) = diag([P-FU-070]) + diag([P-FU-080]) · m_f(k) / [P-FU-010]
```

It runs linearly from `[P-FU-070]` at fuel exhaustion to `[P-FU-070] + [P-FU-080]` at full capacity. The equations of motion use `m(k)` and `J(k)` with no thrust term and no `J̇·ω` term (§4.1 assumption 4, L0-ASM-090). The fuel leaves with the local body velocity from a centroid at `O_B`, so this is exact (G2 §3.1).

### 6.4 Consistency of each parameter set (L2-AER-FU-330, DD-260)

At the start of each run, FU recomputes the two tensors of §6.3 from `[P-DYN-020]`, `[P-DYN-030]`, `[P-FU-030]` and `[P-FU-010]` of the run's vehicle parameter set. If any principal moment of the set's `[P-FU-070]` or `[P-FU-080]` differs from its recomputed value by more than the relative tolerance `[P-FU-090]`, FU rejects the parameter set with an initial-condition error (ICD-AER-TST) and produces no output. FU checks; it does not substitute the recomputed values, so the run uses only what its parameter set states (L1-AER-650).

### 6.5 Initial fuel (L2-AER-FU-020, -030; DD-140)

`m_f(0)` is the fuel mass of the initial condition, for a ground start and for an airborne test start alike (D69, D73 B3-1). A value outside `[0, [P-FU-010]]` is rejected with an initial-condition error; it is not clamped.

---

## 7.2 Fuel model (content for the C2 slot)

Replace the paragraph "What DYN needs: nothing directly …" and the "C2 content slot" sentence with the following. The first sentence of the current text stays true: the fuel mass flow does not enter the equations of motion, because consumed fuel gives no force and no moment (L0-ASM-090).

### 7.2.1 Consumption relationships (L1-AER-160, -170, -940; DD-110)

EF gives FU, over interface I-01, the control force and the control moment it computed once for step `k` from its effector outputs, the same values it gives DYN (§7.1, DD-190, L2-AER-FU-070). FU uses no per-effector output. The **consumption rate** of step `k` is

```
q(k) = [P-FU-040] · ‖F_c^B(k)‖ + [P-FU-050] · ‖M_c^B(k)‖
```

The first term is the **translational consumption term** and the second the **rotational consumption term**. `[P-FU-040]` (kg/(N·s)) and `[P-FU-050]` (kg/(N·m·s)) are one coefficient each, common to the effector set, and no other parameter enters (L2-AER-FU-060).

Properties used by the requirements:

- `q(k) ≥ 0` for non-negative coefficients, so the remaining fuel never increases (L2-AER-FU-100).
- `q(k) = 0` exactly when `F_c^B(k) = 0` and `M_c^B(k) = 0` (L1-AER-940, L2-AER-FU-300). No fuel is used with the effectors off on the ground (L1-AER-930, D69), in the free fall after exhaustion, or in the credibility checks that run with no effector output (C-1 to C-5).
- `q` is frame-invariant and does not depend on the effector layout.

### 7.2.2 Fuel accounting (L1-AER-190; DD-130 as revised by DD-270)

Let `c(k) = fl(q(k) · Δt)`: the fuel that step `k` would use at its consumption rate. Step `k` is an **exhaustion step** when `m_f(k) > 0` and `c(k) ≥ m_f(k)`. Then:

```
not an exhaustion step:   ṁ_f(k) = q(k)            m_f(k+1) = m_f(k) − c(k)
exhaustion step:          ṁ_f(k) = m_f(k) / Δt     m_f(k+1) = 0
```

- The flow is held over the step, as the control force and moment are (§10.2, DD-100), so the fuel consumed in a step is the flow times `Δt`, and the remaining fuel is the initial fuel minus the sum of the flows times `Δt`, to rounding (L2-AER-FU-080).
- In a step that is not an exhaustion step, `c(k) < m_f(k)`, so `m_f(k) − c(k) > 0` in IEEE arithmetic: the remaining fuel stays above zero. The comparison and the subtraction use the same `c(k)`.
- At the end of the exhaustion step the remaining fuel is set to zero exactly (L2-AER-FU-340, G2-F10), and not computed as `m_f(k) − ṁ_f(k)·Δt`, whose rounding residual can be positive or negative. The difference from the summed flow is at most a few units of rounding of `m_f(k)`, far inside `[P-FU-060]`.
- From the step after the exhaustion step, `m_f = 0`, fuel is not available (§7.2.3), the effectors give zero force and moment (§7.1), `q = 0` and `ṁ_f = 0` to the end of the run (L2-AER-FU-090, -200).

### 7.2.3 Fuel availability (L1-AER-200, -260, -270; L2-AER-FU-200, -320)

```
φ(k) = available       if m_f(k) > 0
φ(k) = not available   if m_f(k) = 0
```

FU gives `φ(k)` over interface I-03 to the effector model (§7.1: zero output while not available) and to the ground contact model (§9: a ground contact with fuel not available is a crash, whatever the speed; D68, D73 B3-3). Both read the same value for the same step. A run that starts with `m_f(0) = 0` has fuel not available from step 0; a takeoff then produces no output and the vehicle stays on the ground. Fuel exhaustion is nominal behaviour (L0-ASM-070): `φ` is a model state, not a failure flag.

### 7.2.4 Derivation of the consumption coefficients and of the hover endurance (D66, D72 Q4)

`[P-SYS-290]` is the anchor of the chain, not a requirement (D72 Q4). In still air at sea level (ρ₀ = 1.225 kg/m³), at the maximum horizontal speed `V = [P-SYS-230]` with level attitude, the control force balances the drag `D = ½·ρ₀·[P-DYN-100]·V²` and the weight, and the control moment is zero. So `ṁ = −[P-FU-040]·√(D² + (m·g)²)` with `g = [P-DYN-010]`, and the time from `m_max` to `[P-FU-030]` is

```
T(k_t) = ( asinh(m_max·g/D) − asinh([P-FU-030]·g/D) ) / (k_t · g)
```

Setting `T = [P-SYS-290]` gives `k_t = 2.3467 × 10⁻⁷ kg/(N·s)` with the current database (D = 72 945 N); `[P-FU-040]` is that value rounded down to 2.34 × 10⁻⁷, so the endurance at speed is 8.02 h, at least `[P-SYS-290]`. `[P-FU-050]` is equal in number (D66). Then `[P-SYS-280]` is the largest value, rounded down, that meets L2-AER-FU-290:

```
[P-SYS-280] ≤ ln(m_max / [P-FU-030]) / ( (1 + [P-FU-100]) · [P-FU-040] · g )   = 168 278 s (46.7 h); set to 165 600 s (46 h)
```

**When an input changes** (TT-110, TT-750, TT-800, linked; G2-F18): a change of `[P-DYN-100]`, `[P-SYS-230]`, `[P-FU-010]`, `[P-FU-030]` or `[P-FU-100]` at I1 re-derives `[P-FU-040]` and `[P-FU-050]` from this subsection, then `[P-SYS-280]` from the inequality, and re-checks L2-AER-FU-290 (criterion 1). The inequality stays valid by construction.

### 7.2.5 Fuel in the credibility checks

- **C-8 (proposed wording, G2-F22).** Configuration: the reference mission SC-110, from the ground start at full fuel to the crash after fuel exhaustion, rest on the ground (leg 7a) included, with the FU outputs of each simulation step recorded (IN-C2-30). Independent solution: the initial fuel mass minus an independent summation of the FU fuel mass flow of each simulation step times `Δt`. Tolerance: at most `[P-FU-060]` at each step. Owner: FU (L1-AER-190; C2).
- **C-1 to C-5** run with zero fuel or with the effectors off (§7.1). Then `q = 0`, `m` and `J` are constant and equal to their initial values, as the closed forms assume (IN-C2-16 c, d).
- **No long fuel check.** No credibility check runs over the hover endurance (D72). The hover endurance is verified as a performance test of L1-AER-360 v2 (L2-AER-FU-290 criterion 2), not as a credibility check.

---

## §12 and §13 rows (proposed)

**§12 Parameters and input pedigree, FU rows:**

| Parameter | Value | Status | Pedigree |
| --- | --- | --- | --- |
| `[P-FU-010]` | 500 kg | TBR | Owner (D65); meets L2-AER-FU-290 |
| `[P-FU-030]` | 1000 kg | TBR | Owner (D65) |
| `[P-FU-040]`, `[P-FU-050]` | 2.34 × 10⁻⁷ | TBR | Derived from `[P-SYS-290]` (§7.2.4, D66) |
| `[P-FU-060]` | 1 × 10⁻⁶ kg | TBR | Rounding of per-step sums (D65) |
| `[P-FU-070]` | (1 900, 10 650, 10 650) kg·m² | TBR | Derived, §6.3 (DD-280) |
| `[P-FU-080]` | (950, 5 325, 5 325) kg·m² | TBR | Derived, §6.3 (DD-280) |
| `[P-FU-090]` | 1 × 10⁻⁹ | TBR | Floating-point agreement |
| `[P-FU-100]` | 0.05 | TBR | Regulation, attitude moments and takeoff (L2-AER-FU-290) |
| `[P-SYS-280]` | 165 600 s | TBR | Derived, §7.2.4 |
| `[P-SYS-290]` | 28 800 s | Set | Owner anchor (D66, D72 Q4) |

**§13 Open items, FU rows:** TT-770 (`[P-FU-070]`, `[P-FU-080]`): TBD → TBR with the values of §6.3, closure with the body shape (TT-740, 2026-11-30). TT-780: the C2 part closes when §6 and §7.2 are merged from this file.

**§14 Trace, additions:** §6 adds L1-AER-900 (no gear mass); §7.2 adds L1-AER-940 (zero flow at zero output) and L1-AER-260, -270 (fuel availability to the ground contact model).
