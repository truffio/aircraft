# Aeronef — Model Specification MS-DYN

**Status:** Draft (task C1), for Gate G2. Not baselined.
**Date:** 2026-11-05
**Owner:** Martin (author: C1)
**Classification:** Protected design material. Not for release to the Reverse-Engineering Effort (RVS).
**Related:** [L1](../requirements/L1.md) (tag `AER-L1-baseline-1`), the DYN section of L2 (draft `work/C1/L2_DYN.md`), [CONVENTIONS](CONVENTIONS.md), [GLOSSARY](GLOSSARY.md), [FUNCTIONAL_ANALYSIS](FUNCTIONAL_ANALYSIS.md), [PARAMETERS](../parameters/PARAMETERS.yaml), METHODOLOGY §7 and §10.3, plan §9 (D1–D63).

## 0. Purpose, scope and how to cite

For a simulated vehicle the physics is the requirement (METHODOLOGY §7). This document states the physics that the Aeronef vehicle model reproduces: the frames and the state, the equations of motion, the external forces, the sensed acceleration, the ground contact, the simulation step and the independent checks that make the model credible. Short requirements in L1 and L2 point to it (INCOSE R23). It states *what* the model computes. It does not choose an integration method, a code structure or a data layout, except where a requirement needs it (D4).

- **Citing.** Requirement statements cannot carry section numbers (the lint forbids digits), so they cite a section by its name in bold below, for example "the **drag model** of MS-DYN". Each named section keeps its name for the life of the document.
- **Numbers.** Numbers in this document are definitions: exact mathematical constants, the constants of a named standard (the atmosphere of §5.3) and the conventions. Every value that the design can change is a parameter `P-<SUB>-<NNN>`. New parameters are proposed in `work/C1/param_proposals.md`.
- **Content owners.** C1 (DYN) owns §1 to §5 and §8 to §13. The **mass-properties model** (§6) and the **effector and fuel models** (§7) are sections of this document because L1-AER-160, -220 and -720 place them here, but their content is written by C2 (FU) and C3 (EF) and merged at integration (I1). This draft states what DYN needs from them and leaves their content slots marked.
- **Open decisions.** Two items are open with the owner and are written so that the document is correct under either answer: the rotation-during-translation term (#81.1, §4.5) and the drag form (C1-Q03, §5.5). Section 13 lists every open item.

## 1. Frames, notation and units

The frames, signs and units are those of CONVENTIONS, without exception (L1-AER-740, CV-010).

| Item | Definition | Reference |
| --- | --- | --- |
| Local reference frame L | North-east-down, fixed to the datum plane, inertial | CV-120 to CV-140 |
| Vehicle-carried frame V | Origin at `O_B`, axes parallel to L | CV-150 |
| Body frame B | Origin `O_B` at the centre of gravity (CG); x to the nose, y to the right, z down | CV-160, CV-170 |
| Attitude | Unit quaternion `q`, scalar first, Hamilton product; `C_BL` from `q` as CV-250 gives | CV-250 |
| Euler angles | ψ, θ, φ, 3-2-1 sequence, derived from `q` by CV-260 | CV-210 to CV-260 |
| Body rates | `ω^B = (p, q_r, r)` (the pitch rate is written `q_r` here to keep it apart from the quaternion) | CV-280 |
| Forces, moments | `F^B = (X, Y, Z)`, `M^B = (M_x, M_y, M_z)` about `O_B` | CV-310, CV-320 |
| Units | SI; angles in radians | CV-710 to CV-730 |
| Time | Simulation time `t`, step index `k`, `t_k = k·Δt`, `Δt = [P-SYS-300]` | CV-810 to CV-840 |

Additional notation used here:

| Symbol | Meaning |
| --- | --- |
| `r^L = (x_N, y_E, z_D)` | Vehicle position (of the CG) in L (CV-410) |
| `v^L = (v_N, v_E, v_D)` | Vehicle velocity, relative to the ground, in L (CV-460) |
| `v^B = (u, v, w) = C_BL·v^L` | Vehicle velocity in body axes (CV-460) |
| `w^L` | Wind velocity in L (CV-470) |
| `v_a^L = v^L − w^L` | Air-relative velocity (CV-470) |
| `h = −z_D` | Altitude (CV-430) |
| `m` | Vehicle mass (CV-340), from FU |
| `J = diag(I_xx, I_yy, I_zz)` | Inertia tensor about `O_B` in B, diagonal (D61, CV-350), from FU |
| `g` | Gravitational acceleration magnitude `[P-DYN-010]` |
| `g^L = (0, 0, g)` | Gravitational acceleration vector in L (CV-180) |
| `F_c^B`, `M_c^B` | Control force and control moment, from EF |
| `D^L` | Drag force in L |
| `ρ(h)` | Air density (§5.3) |
| `a^L = dv^L/dt` | Vehicle acceleration (glossary) |
| `f^B` | Sensed acceleration (glossary; §8) |
| `[ω×]` | Cross-product matrix of `ω` |

## 2. Vehicle geometry

This section is the **vehicle geometry** of MS-DYN. It serves L1-AER-220 (the body shape from which the inertia is derived), L1-AER-240 (the nose) and L1-AER-250 (the crew station).

### 2.1 Body shape

The body is a **capsule**: a circular cylinder closed by two hemispheres of the cylinder's radius, the shape of a "Tic Tac" (AIRCRAFT_CHARACTERISTICS §1, L0-CON-140).

| Quantity | Symbol | Value |
| --- | --- | --- |
| Overall length, along `x_B` | `L_b` | `[P-DYN-020]` |
| Diameter | `D_b = 2R` | `[P-DYN-030]` |
| Length of the cylindrical part | `H = L_b − D_b` | derived; `[P-DYN-020]` must be at least `[P-DYN-030]` |

- The capsule axis is the body x axis. The capsule's geometric centre is at `O_B`, the CG.
- The capsule is symmetric under reflection in each of the three body coordinate planes. With a mass distribution of the same symmetry (FU, §6), the CG is at the geometric centre and the body axes are principal axes of inertia, so the products of inertia are zero (D61).
- The shape is provisional: L0-CON-140 carries "elongated body shape provisional, TBR, Martin, 2026-11-30" (TT-240, TT-430). The dimensions are TBR.

### 2.2 Nose

The **nose** is the end of the capsule on the positive body x axis, the body point `(L_b/2, 0, 0)`. It marks the designated forward direction (L0-CON-150, CV-170). Heading is the direction angle of the horizontal projection of `x_B` (CV-530).

### 2.3 Crew station

The crew station is the body-frame position `[P-DYN-400]` (L1-AER-250). It lies inside the capsule and forward of the CG (positive x component). It defines where the crew sits; the crew acceleration limit is evaluated at the CG, not here (D45, L1-AER-290). No quantity of this model is computed at the crew station.

### 2.4 What the shape is used for

The shape gives the mass properties (§6). It does not shape the drag under the recommended drag form (§5.5, option D1); under option D2 it gives the reference areas. It has no other role: there is no lift and no control surface (L1-AER-030, -040).

## 3. Vehicle state and outputs

This section is the **vehicle state** of MS-DYN.

### 3.1 State

At each simulation step `k` the vehicle state is:

| Element | Symbol | Frame | Unit |
| --- | --- | --- | --- |
| Position of the CG | `r^L` | L | m |
| Velocity of the CG | `v^L` | L (components north, east, down) | m/s |
| Attitude quaternion | `q` | L → B (CV-250) | 1 |
| Body rates | `ω^B = (p, q_r, r)` | B | rad/s |

These thirteen numbers are the integrated state of the rigid body. Under option T2 of §4.5 the model integrates `v^B` instead of `v^L`; the state reported is the same (`v^L = C_LB·v^B`).

### 3.2 Quantities derived at each step

| Quantity | Definition | Reference |
| --- | --- | --- |
| Velocity in body axes `v^B` | `C_BL·v^L` | CV-460 |
| Euler angles ψ, θ, φ | From `q` by CV-260; the reported quaternion has `q0 ≥ 0` | CV-250, CV-260 |
| Vehicle acceleration `a^L` | The time derivative of `v^L` given by the translational equation (§4.2), evaluated as §3.3 states | Glossary |
| Sensed acceleration `f^B` and its magnitude | §8, evaluated as §3.3 states | Glossary, L0-CON-310 |

The altitude, horizontal speed, vertical speed, heading and track are navigation quantities computed by NAV from the vehicle state (L1-AER-530); MS-DYN does not redefine them. The vehicle mass and the remaining fuel mass are FU outputs (L1-AER-180).

### 3.3 Evaluation instant of the acceleration quantities (proposed, TBR; DD-C1-04)

An acceleration depends on the inputs (control force, mass, wind), and the inputs change at step boundaries (§10.2). The acceleration quantities reported with step `k` are therefore defined as follows:

- for `k ≥ 1`: evaluated at `t_k` from the state of step `k` and the inputs held over the step from `t_{k−1}` to `t_k` (the value at the end of the step that produced the state);
- for `k = 0`: evaluated at `t_0` from the initial state and the inputs held over the first step, from `t_0` to `t_1`. These values become known when the TST commands the first step.

This makes the acceleration of step `k ≥ 1` available at the same time as the rest of the state of step `k`, so it can be part of the frame-start state (L1-AER-440). It is a convention of this model, not physics; the glossary entry *Vehicle state* is proposed for an update to say so (`work/C1/glossary_proposals.md`).

### 3.4 Outputs

| Output | Consumer | Interface |
| --- | --- | --- |
| Vehicle state of each step (§3.1, §3.2) | NAV, FC at the start of each control frame | Vehicle-model boundary ICD (IN-B1-01; L1-AER-430, -440) |
| Vehicle state and sensed acceleration of each step | TM (operational data) | ICD-AER-TST (L1-AER-640) |
| Ground-contact event record (§9) | TM and TST | ICD-AER-TST (L1-AER-260, -270; I-37, I-41) |

The wind is a vehicle-model input only. The flight software does not receive it (L1-AER-670).

## 4. Equations of motion

This section is the **equations of motion** of MS-DYN.

### 4.1 Assumptions

1. The vehicle is a rigid body with six degrees of freedom; there is no structural flexibility and no fuel slosh (L0-CON-010, L0-ASM-080).
2. The local reference frame L is inertial; the world is flat and does not rotate (L0-ASM-030, CV-110, CV-140).
3. The body origin is the CG, fixed in the body at every fuel state (L0-CON-130, CV-160, L1-AER-210).
4. The mass and the inertia vary with the fuel state, as FU gives them at each step (L1-AER-180, -220). Consumed fuel leaves the vehicle without imparting force or moment; its only effect is the loss of mass (L0-ASM-090). The equations therefore take the instantaneous mass properties: there is no thrust term `ṁ·v` and no `J̇·ω` term. (For mass that leaves the body with the local velocity of the body, the momentum it carries away cancels those terms exactly; L0-ASM-090 states this as the model.)
5. The body axes are principal axes of inertia: `J` is diagonal (D61).

### 4.2 Translational equation

The total force `F` is the sum of gravity, drag and the control force (§5.1). In L:

```
F^L = m·g^L + D^L + C_LB·F_c^B
dr^L/dt = v^L
```

The rate of change of the velocity is given by one of the two options of §4.5:

| | Option T1 — rotation-during-translation term retained (recommended) | Option T2 — term removed |
| --- | --- | --- |
| Equation integrated | `m·dv^L/dt = F^L` (Newton's second law in the inertial frame L) | `m·dv^B/dt = C_BL·F^L` (no `ω^B × v^B` term) |
| Same equation in the other frame | `dv^B/dt = C_BL·F^L/m − ω^B × v^B` | `dv^L/dt = F^L/m + ω^L × v^L` |
| Vehicle acceleration `a^L` | `F^L/m` | `F^L/m + ω^L × v^L` |
| Velocity under a yaw rotation with no force | `v^L` constant; `v^B` turns with the body | `v^B` constant; `v^L` turns with the heading |

`m` is the vehicle mass of the current step (assumption 4). Gravity enters as `m·g^L`, so the acceleration due to gravity does not depend on the mass.

### 4.3 Rotational equation

About the CG, in body axes, with the diagonal inertia tensor of the current step:

```
J·dω^B/dt + ω^B × (J·ω^B) = M_c^B
```

In components:

```
I_xx·dp/dt   = M_x + (I_yy − I_zz)·q_r·r
I_yy·dq_r/dt = M_y + (I_zz − I_xx)·r·p
I_zz·dr/dt   = M_z + (I_xx − I_yy)·p·q_r
```

The only external moment is the control moment (§5.1): gravity and drag act at the CG and give no moment under either drag form (§5.5). The product terms on the right are the gyroscopic term (§4.5).

### 4.4 Attitude kinematics

The attitude quaternion follows the body rates:

```
dq/dt = ½ · q ⊗ (0, ω^B)

dq0/dt = −½·(q1·p + q2·q_r + q3·r)
dq1/dt =  ½·(q0·p + q2·r − q3·q_r)
dq2/dt =  ½·(q0·q_r + q3·p − q1·r)
dq3/dt =  ½·(q0·r + q1·q_r − q2·p)
```

`q` stays a unit quaternion. The model keeps its norm within `[P-DYN-230]` of one at each step (L2-AER-DYN-060). How it does so (normalisation, choice of integrator) is a design matter.

### 4.5 Kinematic terms

This section is the **kinematic terms** list of MS-DYN. L1-AER-020 and L0-CON-030 exclude every term by which motion along one degree of freedom produces an acceleration along another degree of freedom in the body frame, other than the rigid-body kinematic terms that this section lists (D18, #81). Every other cross-axis term is excluded: there is no aerodynamic coupling (§5.5), no effector coupling (EF), and no product of inertia (D61, §6).

| ID | Term | Where it appears | Status | Effect in normal operation |
| --- | --- | --- | --- | --- |
| K-1 | Gyroscopic term `ω^B × (J·ω^B)` | Rotational equation (§4.3) | Retained (proposed; #81, confirmation C1-Q02) | Zero. With pitch and roll held at zero (D57) the body rates are `(0, 0, r)`, and every product term of §4.3 contains `p` or `q_r`. It is non-zero only during pitch or roll transients within `[P-AF-180]` and after fuel exhaustion, when the attitude is free (L1-AER-390). It is what conserves the angular momentum in a torque-free rotation (§11, check C-3). |
| K-2 | Rotation-during-translation term `ω^B × v^B` | Translational equation written in body axes (§4.2) | **Open: owner question #81.1.** Option T1 retains it (recommended), option T2 removes it | In Heading at a non-zero horizontal speed, a heading change turns the body under the velocity (T1) or turns the velocity with the body (T2). In Stationary, Hover and a turn in place the horizontal speed is near zero and the term is near zero. Vertical motion is unaffected under both options: with `ω^B = (0, 0, r)` the term has no body z component. |
| K-3 | Resolution of gravity, drag and wind in the body frame through the attitude, `C_BL` | Both equations, through `C_BL` and `C_LB` | Retained (inherent in a rigid body with body-fixed effectors; C1-Q02) | Gravity stays along `z_B` while pitch and roll are zero. A body-fixed control force turns with the heading in L. It is a change of frame, not a force. |

Notes:

- K-2 is a choice between two models, not a numerical detail. Option T1 is Newton's second law in an inertial frame: it conserves linear momentum, it is what the free-fall and terminal-velocity checks assume, and it is the standard rigid-body model. Option T2 reads D18 literally ("seen from the aircraft's body frame"): with no force, the velocity stays fixed in the body, so the vehicle's path turns with its heading. It is not Newtonian. Its consequences are listed with the question in `work/C1/issues.md` (C1-Q01).
- Whichever option the owner chooses, this table records it, and L2-AER-DYN-050 requires the model to contain exactly the terms listed here. L1-AER-020 can then cite this section when #81 closes (CR-C1-01).

## 5. External forces and moments

### 5.1 Total force and total moment

This section is the **total force and moment** of MS-DYN. It closes the list of L1-AER-050 and L0-CON-090.

```
F^L = m·g^L + D^L + C_LB·F_c^B
M^B = M_c^B
```

- Gravity (§5.2) and drag (§5.5) are the only external forces. Both act at the CG.
- The control force `F_c^B` and the control moment `M_c^B` come from the effectors only (EF, §7; L1-AER-080). They are the only source of moment.
- There is no aerodynamic force other than the drag force: no lift (L1-AER-030). There is no aerodynamic control surface and no force that depends on a surface deflection (L1-AER-040).
- Ground contact is not a force: it ends the run as a landing or a crash (§9; L1-AER-050, L0-ASM-110).
- Consumed fuel gives no force and no moment (L0-ASM-090).
- No electrical quantity exists in this model (L0-CON-160, D54).

### 5.2 Gravity model

This section is the **gravity model** of MS-DYN. Gravity is uniform: the acceleration `g^L = (0, 0, [P-DYN-010])` is the same everywhere and at every time, along `+z_L` (L0-ASM-040, CV-110, CV-180, L1-AER-060). The gravity force is `m·g^L` at the CG. There is no gravity-gradient moment. `[P-DYN-010]` is proposed equal to standard gravity, 9.806 65 m/s² (TBR, TT-150).

### 5.3 Atmosphere model

This section is the **atmosphere model** of MS-DYN. The air density is that of the **U.S. Standard Atmosphere, 1976**, which is identical to the ICAO Standard Atmosphere up to 32 km (D20, L0-ASM-060). It depends on altitude only and does not vary with time.

- **Altitude.** The standard is defined in geopotential altitude. On the flat world of CV-110, with uniform gravity, the geopotential altitude is taken equal to the altitude `h` of CV-430, by definition.
- **Constants of the standard.** These are constants of the named standard. They are not parameters, and they do not change if `[P-DYN-010]` changes.

| Constant | Value |
| --- | --- |
| Standard gravity used by the standard, `g_0` | 9.806 65 m/s² |
| Universal gas constant, `R*` | 8.314 32 J/(mol·K) |
| Molar mass of air, `M_0` | 0.028 964 4 kg/mol |

| Layer `b` | Base altitude `h_b` (m) | Base temperature `T_b` (K) | Lapse rate `L_b` (K/m) | Base pressure `p_b` (Pa) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 288.15 | −0.0065 | 101 325.0 |
| 1 | 11 000 | 216.65 | 0.0 | 22 632.06 |
| 2 | 20 000 | 216.65 | +0.0010 | 5 474.889 |
| 3 | 32 000 | 228.65 | +0.0028 | 868.0187 |

The model is defined from `h = 0` to the top of layer 3, `h = 47 000 m`. For `h_b ≤ h < h_{b+1}`:

```
T(h) = T_b + L_b·(h − h_b)
p(h) = p_b · (T_b / T(h)) ^ (g_0·M_0 / (R*·L_b))       if L_b ≠ 0
p(h) = p_b · exp(−g_0·M_0·(h − h_b) / (R*·T_b))         if L_b = 0
ρ(h) = p(h)·M_0 / (R*·T(h))
```

At `h = 0` this gives ρ = 1.2250 kg/m³. Only the density is used; temperature and pressure are not model outputs (CV-430). The maximum operating altitude `[P-SYS-200]` must lie within the model's range (note for I1, `work/C1/interface_needs.md`).

### 5.4 Wind model

This section is the **wind model** of MS-DYN. It defines the wind envelope that the performance requirements and budgets rely on (glossary *Wind envelope*; D17, D51, D62). The TST generates the wind and gives it with each step command (L1-AER-670); DYN uses the value it is given and does not check it.

The wind velocity is uniform in space, horizontal, and the sum of a steady wind and gusts (L0-ASM-050, CV-470):

```
w^L(t) = w_s + w_g(t),        w_D = 0
```

- **Steady wind.** `w_s` is a horizontal vector, constant over a run, with `|w_s| ≤ [P-SYS-430]`.
- **Gusts and bursts.** `w_g(t)` is a sequence of gust events that do not overlap. Event `j` has a horizontal unit direction `e_j`, an amplitude `A_j ≤ [P-SYS-560]`, a start time `t_j`, a rise time `T_r,j ≥ [P-SYS-570]`, a hold time `T_h,j ≥ 0` and a decay time `T_d,j ≥ [P-SYS-570]`. With `τ = t − t_j`:

```
w_g(t) = A_j·e_j·s_j(τ)
s_j(τ) = ½·(1 − cos(π·τ / T_r,j))                       0 ≤ τ < T_r,j          (rise)
s_j(τ) = 1                                              T_r,j ≤ τ < T_r,j + T_h,j   (hold)
s_j(τ) = ½·(1 + cos(π·(τ − T_r,j − T_h,j) / T_d,j))      next T_d,j               (decay)
s_j(τ) = 0                                              otherwise
```

  A gust and a burst are both gust events; they differ only by their hold time and amplitude, which the test procedure sets (D32). An event starts only when the previous one has decayed to zero.
- **Consequences used by the budgets.** The largest instantaneous wind speed is `[P-SYS-430] + [P-SYS-560]` (D51). The wind is continuous with a continuous rate. Its rate of change is at most `(π/2)·[P-SYS-560]/[P-SYS-570]`, and its second derivative at most `(π²/2)·[P-SYS-560]/[P-SYS-570]²`. There is no instantaneous step (D62).
- **Proposed rise time.** `[P-SYS-570]` = 2.0 s (TBR, TT-650): about the time a gust front of the longest FAR 25.341 gust gradient (350 ft, 107 m) takes to pass at the steady wind `[P-SYS-430]`. It is 20 times the control-loop latency `[P-SYS-480]`, so flight control can follow it. C4 confirms the gust share of `[P-FC-020]` and `[P-FC-010]` against it at I1 (FUNCTIONAL_ANALYSIS §7.2, §7.4).
- **Sampling.** The wind given with the command for the step from `t_k` to `t_{k+1}` is the wind at `t_k`. The model holds it over that step (§10.2). ICD-AER-TST fixes the signal (IN-C1-20).
- A wind that varies across the operating volume is outside this model (#84).

### 5.5 Drag model

This section is the **drag model** of MS-DYN. Drag acts on the air-relative velocity `v_a^L = v^L − w^L` (L1-AER-070, CV-470), with the density `ρ(h)` of the atmosphere model at the vehicle altitude. It acts at the CG. The form is a design choice of C1, bounded by L1-AER-020 and L1-AER-030; it is proposed as DD-C1-01 and DD-C1-02 and put to the owner for confirmation (C1-Q03). The recommended form is D1.

| | Option D1 — isotropic quadratic drag (recommended) | Option D2 — per-axis quadratic drag in body axes |
| --- | --- | --- |
| Force | `D^L = −½·ρ(h)·[P-DYN-100]·|v_a^L|·v_a^L` | `D_i^B = −½·ρ(h)·C_D,i·A_i·|v_a,i^B|·v_a,i^B` for `i = x, y, z`, with `v_a^B = C_BL·v_a^L` |
| Parameters | Drag area `[P-DYN-100]` (C_D·A, m²) | Three drag coefficients `C_D,i` (new parameters if chosen) and the reference areas from the capsule: `A_x = π·D_b²/4`, `A_y = A_z = H·D_b + π·D_b²/4` |
| Direction | Opposite to the air-relative velocity: no component perpendicular to it, so no lift | Not opposite to the air-relative velocity for an oblique flow: a cross-flow component exists |
| Attitude dependence | None | Through `C_BL` (the elongated shape) |
| Cross-axis property (L1-AER-020) | An air-relative velocity along one body axis gives a drag force along that axis only. With a velocity on two axes, the magnitude `|v_a|` is shared. | The drag along each body axis depends only on the air-relative velocity along that axis |
| Moment | None (acts at the CG) | None (acts at the CG) |

Common to both options:

- **No aerodynamic moment.** The drag acts at the CG and there is no rotational damping moment (DD-C1-01). A vehicle at fuel exhaustion keeps its angular momentum, as CONOPS SC-110 leg 11 and the L1-AER-200 and -390 rationales describe ("keeps the angular rate it had"). The drag-moment lines of the moment authority budget (L1-AER-140, FUNCTIONAL_ANALYSIS §7.1) are zero under this model.
- **No Mach or Reynolds dependence.** The coefficients are constant; this is a definition of the fictional vehicle.
- **Budget form.** Under D1 the drag at airspeed `V` is `D(V) = ½·ρ·[P-DYN-100]·V²` along the air-relative velocity, and its component along any body axis is at most `D(V)`. This is the `D(V)` of FUNCTIONAL_ANALYSIS §7.1. The budgets use the largest density in the operating volume, at the minimum operating altitude `[P-SYS-210]`.
- **Vacuum-equivalent configuration.** A vehicle parameter set with `[P-DYN-100] = 0` (D1), or each `C_D,i = 0` (D2), has no drag. The credibility checks of §11 use it.

Why D1 is recommended: it has no lift by construction (L1-AER-030 is then shown by inspection of one line), it has no attitude dependence, so translation and attitude are independent through the aerodynamics in every frame (L0-CON-020), it gives the single `D(V)` the L1 budgets are written with, and a pure motion along one body axis produces drag along that axis only (D18). AIRCRAFT_CHARACTERISTICS §1 says the exterior shape matters only through the mass properties, which D1 respects. D2 meets D18 in the stronger "per axis" reading but gives a cross-flow force for oblique flow, which an inspection of L1-AER-030 could read as lift.

## 6. Mass-properties model

This section is the **mass-properties model** of MS-DYN. **Content owner: C2 (FU).** L1-AER-220 asks MS-DYN to state the body shape and the mass distribution from which the inertia is derived. The shape is §2. The mass distribution, the fuel placement and whether the inertia varies with the fuel state are C2 decisions (L1-AER-220 rationale); C2's text is merged here at I1.

What DYN needs from FU, at each step `k` (IN-C1-01, IN-C1-02):

- the vehicle mass `m_k = [P-FU-030] + (remaining fuel mass)` (L1-AER-180);
- the three principal moments of inertia `I_xx`, `I_yy`, `I_zz` about the CG, in the body axes, with zero products of inertia (D61, CV-350);
- the CG at the body origin at every fuel state (L1-AER-210).

**Reference derivation (for C2).** For mass `m` distributed with uniform density over the solid capsule of §2.1 (radius `R = D_b/2`, cylinder length `H`):

```
m_cyl  = m · H / (H + 4R/3)          (cylinder part)
m_hem  = m · (2R/3) / (H + 4R/3)     (each hemisphere)
I_xx   = m_cyl·R²/2 + 2·m_hem·(2R²/5)
I_yy   = I_zz = m_cyl·(R²/4 + H²/12) + 2·m_hem·(2R²/5 + H²/4 + 3·H·R/8)
```

Any distribution that is symmetric under reflection in each body coordinate plane gives a diagonal tensor with the CG at the centre. An axisymmetric distribution about `x_B` also gives `I_yy = I_zz`, which the torque-free check C-3 can use. **C2 content slot:** mass distribution of the dry mass and of the fuel; inertia as a function of the remaining fuel mass; the parameters it needs.

## 7. Effector and fuel models

This section is the **effector and fuel models** of MS-DYN. **Content owners: C3 (EF) for §7.1, C2 (FU) for §7.2.** L1-AER-160 and -720 place these models in MS-DYN; their text is merged here at I1.

### 7.1 Effector model (C3)

What DYN needs from EF, for each step (IN-C1-10):

- the control force `F_c^B` and the control moment `M_c^B` about the CG, in body axes: the sum over the effectors of their effector outputs through their control effectiveness (L1-AER-100);
- one value per step, held over the step (§10.2);
- zero force and zero moment at fuel exhaustion (L1-AER-200).

**C3 content slot:** direction of action, control effectiveness, output limits and command response of each effector (L1-AER-090 to -110, -710).

### 7.2 Fuel model (C2)

What DYN needs: nothing directly. The fuel model gives the vehicle mass through FU (§6). Consumed fuel gives no force and no moment (L0-ASM-090), so the fuel mass flow does not enter the equations of motion.

**C2 content slot:** the translational and rotational consumption relationships and their parameters `[P-FU-040]`, `[P-FU-050]` (L1-AER-160, -170); the remaining fuel mass as the initial fuel mass minus the integral of the flow (L1-AER-190).

## 8. Sensed acceleration

This section is the **sensed acceleration** of MS-DYN. The sensed acceleration is the acceleration the crew feels: the sum of the non-gravitational forces on the vehicle divided by its mass (specific force), evaluated at the CG (glossary; D38, D45; L1-AER-290):

```
f^B = (F_c^B + C_BL·D^L) / m
|f| = magnitude of f^B
```

- It is evaluated at the CG, so rotation adds nothing to it (D45).
- In free fall it is zero (no control force, no drag). In a still-air hover at level attitude, with the control force equal to the weight, it is `g` along `−z_B` (glossary).
- Under option T1 (§4.5) it equals `a^L − g^L` resolved in B, the relation that FUNCTIONAL_ANALYSIS §7.2 uses for the crew budget. Under option T2 the vehicle acceleration also contains `ω^L × v^L`, which no force produces, so `f` and `a − g` differ by that term (C1-Q01).
- The ideal landing computes no touchdown shock (D53), and the vehicle is no longer airborne at the contact step, so no sensed acceleration is defined for the contact itself.
- It is evaluated at the instant §3.3 states.

## 9. Ground contact model

This section is the **ground contact model** of MS-DYN. The ground is the datum plane at altitude zero, flat, with no terrain (D8, CV-420). Ground contact is an ideal landing: there is no gear, bounce, friction or ground reaction force (D37, L0-ASM-110, L0-CON-290).

1. **Detection.** The **contact step** is the first simulation step at which the propagated altitude is at most zero (CV-940 "reaches"). The model checks every step from step 0. There is one contact step in a run. The contact step is the "contact sample" of L1-AER-280 and of the glossary *Landing envelope* (glossary proposal).
2. **Classification.** At the contact step, with the vertical speed `VS = −v_D` and the horizontal speed `V_H = √(v_N² + v_E²)` of that step's state (ground-referenced, CV-480, CV-490):
   - the contact is a **landing** when `|VS| ≤ [P-SYS-500]` and `V_H ≤ [P-SYS-510]` (L1-AER-280, D53);
   - otherwise it is a **crash**.
   There is no acceleration limit (D53). The speeds are not interpolated to the crossing instant: the classification uses the state of the contact step, which keeps it exact on the CV-840 time base.
3. **Reported position.** The state of the contact step is reported with the altitude set to zero and the propagated horizontal position and velocity unchanged, so that the altitude is never negative in a run (CV-420; DD-C1-03).
4. **Event record.** The model outputs one event record with the classification and the timestamp of the contact step (CV-840) to TM and to the TST (I-37, I-41). The TST ends the run on it (CONOPS §4.6).
5. **After contact.** If the TST commands a further step, the model keeps the state of the contact step and raises no further event.

## 10. Simulation step and integration

This section is the **simulation step** of MS-DYN.

### 10.1 Step

The model advances in fixed simulation steps of `Δt = [P-SYS-300]` (CV-820, F-TST-01). Each step command from the TST advances the state from step `k` at `t_k = k·Δt` to step `k + 1` (L1-AER-670). Simulation time is set by the step index, not accumulated (CV-820).

### 10.2 Inputs over a step

Over the step from `t_k` to `t_{k+1}` the following inputs are held constant at their step-`k` values:

| Input | Source |
| --- | --- |
| Control force `F_c^B` and control moment `M_c^B` | EF, effector outputs of step `k` |
| Vehicle mass `m` and principal moments of inertia | FU, step `k` |
| Wind velocity `w^L` | TST, given with the command for the step (§5.4) |

The state-dependent quantities (gravity resolved in body axes, the air-relative velocity, the density, the drag, the gyroscopic term) vary within the step with the state.

### 10.3 Integration

- The integration method is a design choice (D4). It is constrained only by the accuracy that the credibility checks of §11 state and by reproducibility.
- **Accuracy.** Over the accuracy horizon `[P-DYN-270]` of simulation time, the model meets the tolerances of checks C-1 to C-6 (§11). These tolerances bound the numerical error of the integration. Numerical integration error is not a share of any performance budget (FUNCTIONAL_ANALYSIS §7.4).
- **Reproducibility.** The state of step `k + 1` depends only on the state of step `k`, the inputs of step `k` and the vehicle parameter set (L1-AER-690, D59). It does not depend on wall-clock time, on the execution host's scheduling or on a random number.
- **Initial state.** Step 0 is the initial condition from the TST (L1-AER-660): position, velocity, attitude and body rates. The parameters come from the vehicle parameter set of the run.

## 11. Credibility checks

This section is the **credibility checks** of MS-DYN. Following NASA-STD-7009B and METHODOLOGY §10.3, each check compares the simulated motion with an independent solution: a closed form or a conservation law, computed outside the model. Each check names its configuration. The configurations are scenario choices of the test procedure (D32); the tolerances are parameters, because they are requirements on the model.

Common conditions: the vehicle parameter set is the run's, changed only as each check states. "Zero fuel" means an initial fuel mass of zero, so the effectors produce no force and no moment (L1-AER-200) and the mass is the dry mass `[P-FU-030]`, constant. A relative error is the error divided by the change of the quantity since `t_0`, or by its magnitude where the check says so.

| ID | Check | Configuration | Independent solution | Tolerance | Requirement |
| --- | --- | --- | --- | --- | --- |
| C-1 | Free fall | Zero fuel; vacuum-equivalent (§5.5); any initial position, velocity, attitude and body rates | `r^L(t) = r_0 + v_0·t + ½·g^L·t²`, `v^L(t) = v_0 + g^L·t`, until the contact step. Sensed acceleration zero. | Position and velocity error at each step, relative to the change since `t_0`: at most `[P-DYN-200]` | L2-AER-DYN-600 |
| C-2 | Free fall with drag to terminal vertical speed | Zero fuel; drag on; level attitude, zero body rates; still air and a steady wind of up to `[P-SYS-430]` without gusts | Horizontal velocity tends to the wind velocity. Vertical speed tends to `−v_exp(h)` with `v_t(h) = √(2·m·g / (ρ(h)·[P-DYN-100]))` (under option D2, `C_D,z·A_z` in place of `[P-DYN-100]`) and the quasi-steady correction for the density gradient `v_exp(h) = v_t(h)·(1 − v_t(h)²·(dρ/dh)/(4·g·ρ(h)))` | `|(|VS| − v_exp(h))| / v_exp(h)` at most `[P-DYN-210]` at each step once the procedure's settling interval has passed. The configuration keeps the neglected second-order term below a tenth of `[P-DYN-210]` (a large drag area gives a small `v_t`). | L2-AER-DYN-610 |
| C-3 | Torque-free rotation | Zero fuel (drag on or off: drag gives no moment); any initial body rates with `p`, `q_r` and `r` all non-zero | Angular momentum in L, `H^L = C_LB·J·ω^B`, constant; rotational kinetic energy `½·ω^B·J·ω^B` constant. If `I_yy = I_zz = I_t`: `p` constant, and `(q_r, r)` rotates at the rate `(I_t − I_xx)·p / I_t` | Relative change of `|H^L|`, of the direction of `H^L` (angle in rad) and of the kinetic energy over `[P-DYN-270]`: each at most `[P-DYN-220]` | L2-AER-DYN-620 |
| C-4 | Variable mass under a constant force | Vacuum-equivalent; level attitude, heading north, zero body rates; DYN driven with a prescribed constant control force `F` along `+x_B` and a prescribed mass `m(t_k) = m_0 − ṁ·t_k` in place of EF and FU outputs | `v_N(t) = v_N0 + (F/ṁ)·ln(m_0 / m(t))`; the vertical motion is the free fall of C-1 | Error in `v_N`, relative to its change since `t_0`: at most `[P-DYN-240]`. The procedure keeps `ṁ·Δt/(2·m)` below a tenth of `[P-DYN-240]`, so the hold of the mass over a step (§10.2) does not use up the tolerance. | L2-AER-DYN-630 |
| C-5 | Rotation during translation | Zero fuel; vacuum-equivalent; level attitude; initial horizontal velocity `V_0` and yaw rate `r_0`, `p = q_r = 0` | Option T1: `v_N, v_E` constant; `u, v` turn at `−r_0`. Option T2: `u, v` constant; the track minus the heading is constant and the horizontal speed stays `V_0`. Under both: the vertical motion is the free fall of C-1, and `r`, the pitch angle and the roll angle stay at their initial values. The option that applies is the one recorded in the **kinematic terms** list (§4.5). | Error in the horizontal velocity, relative to `V_0`: at most `[P-DYN-250]` over `[P-DYN-270]` | L2-AER-DYN-640 |
| C-6 | Unit attitude quaternion | Checks C-3 and C-5, and the reference mission SC-110 | `‖q‖ = 1` | `|‖q‖ − 1|` at most `[P-DYN-230]` at each step | L2-AER-DYN-060 |
| C-7 | Standard atmosphere | The density function alone | The published density table of the U.S. Standard Atmosphere, 1976, at the base altitude of each layer and at the midpoint of each layer | Relative error at most `[P-DYN-260]` | L2-AER-DYN-150 |
| C-8 | Fuel-mass integral | The reference mission SC-110 (FU check) | Initial fuel mass minus an independent integration of the recorded fuel mass flow | At most `[P-FU-060]` | FU (L1-AER-190; C2) |

C-4 and C-8 together check the mass decrease end to end: FU integrates the flow (C-8), and DYN uses the mass it is given (C-4). The sensed-acceleration definition is checked inside C-1 (zero in free fall) and by the prescribed-force case of L2-AER-DYN-300 (`g` in a hover).

**Input pedigree.** Section 12 gives the source and status of each parameter the model uses. **Sensitivity** of the key results to the uncertain parameters (drag area, gust rise time, mass properties) is a verification-planning task (Phase 5, V1).

## 12. Parameters and input pedigree

| Parameter | Name | Unit | Proposed value | Status | Source and pedigree |
| --- | --- | --- | --- | --- | --- |
| P-DYN-010 | Gravitational acceleration | m/s² | 9.806 65 | TBR (proposed Set at G2) | Standard gravity (CGPM 1901); L1-AER-060 |
| P-DYN-020 | Body overall length | m | 12.0 | TBR | C1 proposal for the provisional "Tic Tac" shape (L0-CON-140) |
| P-DYN-030 | Body diameter | m | 4.0 | TBR | C1 proposal (length-to-diameter ratio 3) |
| P-DYN-100 | Drag area | m² | 5.0 | TBR | C1 estimate: a round-nosed body of these dimensions has C_D ≈ 0.3 on its frontal area of 12.6 m² (3.8 m²) and more in cross-flow (Hoerner, *Fluid-Dynamic Drag*, 1965); confirmed at I1 with the authority budgets |
| P-DYN-200 | Free-fall check tolerance | 1 | 1·10⁻⁴ | TBR | C1 proposal; check C-1 |
| P-DYN-210 | Terminal vertical speed check tolerance | 1 | 1·10⁻³ | TBR | C1 proposal; check C-2 |
| P-DYN-220 | Torque-free rotation check tolerance | 1 | 1·10⁻⁴ | TBR | C1 proposal; check C-3 |
| P-DYN-230 | Quaternion norm tolerance | 1 | 1·10⁻⁶ | TBR | C1 proposal; check C-6 |
| P-DYN-240 | Variable-mass check tolerance | 1 | 1·10⁻⁴ | TBR | C1 proposal; check C-4 |
| P-DYN-250 | Rotation-during-translation check tolerance | 1 | 1·10⁻⁴ | TBR | C1 proposal; check C-5 |
| P-DYN-260 | Atmosphere density tolerance | 1 | 1·10⁻⁴ | TBR | C1 proposal; check C-7 (the table has five significant figures) |
| P-DYN-270 | Accuracy horizon | s | 3600 | TBR | C1 proposal; at least the longest run; to be raised to `[P-SYS-280]` if that is longer |
| P-DYN-400 | Crew station position | m | (4.0, 0.0, −1.0) | TBR | C1 proposal: forward of the CG, inside the capsule, above the axis |
| P-SYS-300 | Simulation step | s | 0.01 | TBR | B1 (L1-AER-670) |
| P-SYS-430, -560 | Steady wind, gust amplitude | m/s | 51.444, 25.722 | TBR | Owner (D51) |
| P-SYS-570 | Minimum gust rise time | s | 2.0 | TBD → TBR proposed | C1 proposal, §5.4 |
| P-SYS-500, -510 | Landing envelope | m/s | 3.458, 0.5 | TBR | Owner (D53) |
| P-FU-030 and FU mass properties | Dry mass, inertia | kg, kg·m² | — | TBD | C2 |

## 13. Open items

| Item | Where | Owner | Closure |
| --- | --- | --- | --- |
| Rotation-during-translation term: option T1 or T2 (#81.1, C1-Q01) | §4.2, §4.5, C-5 | Martin | G2 |
| Confirm the retained kinematic terms K-1 and K-3 and close #81 (C1-Q02) | §4.5 | Martin | G2 |
| Drag form D1 or D2, and no aerodynamic moment (C1-Q03; DD-C1-01, -02) | §5.5 | Martin | G2 |
| Gust shape and `[P-SYS-570]` value (C1-Q04; TT-650) | §5.4 | Martin | G2 (with the TST wind model and C4's budget check) |
| Body shape and dimensions (C1-Q05; L0-CON-140 TBR) | §2.1 | Martin | 2026-11-30 |
| Evaluation instant of the acceleration quantities (DD-C1-04) | §3.3 | Martin | G2 |
| Content of §6 and §7 | §6, §7 | C2, C3 | I1 |
| Parameter values P-DYN-020 to -400 | §12 | Martin | G2 |

## 14. Trace

| Section | L1 records | L2 DYN records |
| --- | --- | --- |
| §2 Vehicle geometry | L1-AER-220, -240, -250 | L2-AER-DYN-220, -230, -240 |
| §3 Vehicle state | L1-AER-010, -430, -440, -640 | L2-AER-DYN-020, -070, -310, -320, -330, -350 |
| §4 Equations of motion | L1-AER-010, -020, -180, -220 | L2-AER-DYN-010, -030, -040, -050, -060 |
| §5.1 Total force and moment | L1-AER-030, -040, -050 | L2-AER-DYN-100, -110, -160, -170, -180 |
| §5.2 Gravity model | L1-AER-060 | L2-AER-DYN-120 |
| §5.3 Atmosphere model | L1-AER-070 | L2-AER-DYN-150 |
| §5.4 Wind model | L1-AER-070, -670 | L2-AER-DYN-140, -410 |
| §5.5 Drag model | L1-AER-020, -030, -070 | L2-AER-DYN-130, -190 |
| §6 Mass-properties model | L1-AER-180, -210, -220 | L2-AER-DYN-200, -210 (and FU) |
| §7 Effector and fuel models | L1-AER-050, -160, -720 | L2-AER-DYN-180 (and EF, FU) |
| §8 Sensed acceleration | L1-AER-290, -640 | L2-AER-DYN-300 |
| §9 Ground contact model | L1-AER-260, -270, -280 | L2-AER-DYN-500 to -550 |
| §10 Simulation step | L1-AER-660, -670, -690 | L2-AER-DYN-400, -410, -420, -430, -440 |
| §11 Credibility checks | L1-AER-010, -020, -060, -070, -180 | L2-AER-DYN-060, -150, -600 to -640 |
| Whole document | L1-AER-720 | L2-AER-DYN-700 |
