# Aeronef — Model Specification MS-DYN

**Status:** Draft (task C1), version 2: G2 rework and landing gear (D69, D72, D73), for the G2 delta inspection. Not baselined.
**Date:** 2026-11-05
**Owner:** Martin (author: C1)
**Classification:** Protected design material. Not for release to the Reverse-Engineering Effort (RVS).
**Related:** [L1](../requirements/L1.md) (tag `AER-L1-baseline-1` plus CR-C1-01, CR-C2-01 and CR-B3-01 to -41, with L1-AER-900 to -970), the DYN section of L2 (draft `work/C1/L2_DYN.md`), [CONVENTIONS](CONVENTIONS.md), [GLOSSARY](GLOSSARY.md), [FUNCTIONAL_ANALYSIS](FUNCTIONAL_ANALYSIS.md), [PARAMETERS](../parameters/PARAMETERS.yaml), METHODOLOGY §7 and §10.3, plan §9 (D1–D73). Rework record: `work/C1/rework_G2_D69.md`.

## 0. Purpose, scope and how to cite

For a simulated vehicle the physics is the requirement (METHODOLOGY §7). This document states the physics that the Aeronef vehicle model reproduces: the frames and the state, the equations of motion, the external forces, the sensed acceleration, the landing gear and the ground contact, the simulation step and the independent checks that make the model credible. Short requirements in L1 and L2 point to it (INCOSE R23). It states *what* the model computes. It does not choose an integration method, a code structure or a data layout, except where a requirement needs it (D4).

- **Citing.** Requirement statements cannot carry section numbers (the lint forbids digits), so they cite a section by its name in bold below, for example "the **drag model** of MS-DYN". Each named section keeps its name for the life of the document.
- **Numbers.** Numbers in this document are definitions: exact mathematical constants, the constants of a named standard (the atmosphere of §5.3), the conventions and the configurations of the credibility checks (§11). Every value that the design can change is a parameter `P-<SUB>-<NNN>`. New parameters are proposed in `work/C1/param_proposals.md`.
- **Content owners.** C1 (DYN) owns §1 to §5 and §8 to §14. The **mass-properties model** (§6) and the **effector and fuel models** (§7) are sections of this document because L1-AER-160, -220 and -720 place them here, but their content is written by C2 (FU) and C3 (EF) and merged at integration (I1). This draft states what DYN needs from them and leaves their content slots marked.
- **Owner decisions.** The owner answered the C1 questions on 2026-11-05 (D64): the rotation-during-translation term is retained (§4.5), drag is isotropic with no aerodynamic moment (§5.5, read against D18 as D72 confirms), and the gust shape, the capsule and the proposed values are accepted. D69 adds the landing gear and the ground operations (§2.5, §9), D72 rules on the partial G2 (no long checks, §11) and D73 approves the B3 change package. The alternatives stay documented. Section 13 lists the items still open.

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
| `h = −z_D` | Altitude of the CG (CV-430) |
| `h_G` | Height above the ground: altitude of the lowest point of the body shape (CV-400, §2.6) |
| `h_low` | Altitude of the lowest point of the vehicle, body or gear (§2.6) |
| `m` | Vehicle mass (CV-340), from FU |
| `J = diag(I_xx, I_yy, I_zz)` | Inertia tensor about `O_B` in B, diagonal (D61, CV-350), from FU |
| `g` | Gravitational acceleration magnitude `[P-DYN-010]` |
| `g^L = (0, 0, g)` | Gravitational acceleration vector in L (CV-180) |
| `F_c^B`, `M_c^B` | Control force and control moment, from EF |
| `D^L` | Drag force in L |
| `R^L`, `M_R^B` | Ground reaction force in L and ground reaction moment in B, non-zero only on the ground (§9.6) |
| `λ` | Gear extension fraction, 0 retracted, 1 extended (§9.1) |
| `G` | On-ground flag of the gear state: true while the vehicle is on the ground (§9.6) |
| `ρ(h)` | Air density (§5.3) |
| `a^L = dv^L/dt` | Vehicle acceleration (glossary) |
| `f^B` | Sensed acceleration (glossary; §8) |
| `[ω×]` | Cross-product matrix of `ω` |

## 2. Vehicle geometry

This section is the **vehicle geometry** of MS-DYN. It serves L1-AER-220 (the body shape from which the inertia is derived), L1-AER-240 (the nose), L1-AER-250 (the crew station) and L1-AER-900 (the landing gear).

### 2.1 Body shape

The body is a **capsule**: a circular cylinder closed by two hemispheres of the cylinder's radius, the shape of a "Tic Tac" (AIRCRAFT_CHARACTERISTICS §1, L0-CON-140).

| Quantity | Symbol | Value |
| --- | --- | --- |
| Overall length, along `x_B` | `L_b` | `[P-DYN-020]` |
| Diameter | `D_b = 2R` | `[P-DYN-030]` |
| Length of the cylindrical part | `H = L_b − D_b` | derived; `[P-DYN-020]` must be at least `[P-DYN-030]` |
| Half-length of the cylindrical part | `a = H/2` | derived |

- The capsule axis is the body x axis. The capsule's geometric centre is at `O_B`, the CG.
- The capsule is symmetric under reflection in each of the three body coordinate planes. With a mass distribution of the same symmetry (FU, §6), the CG is at the geometric centre and the body axes are principal axes of inertia, so the products of inertia are zero (D61).
- The shape is provisional: L0-CON-140 carries "elongated body shape provisional, TBR, Martin, 2026-11-30" (TT-240, TT-430). The dimensions are TBR (TT-740, closure 2026-11-30).

### 2.2 Nose

The **nose** is the end of the capsule on the positive body x axis, the body point `(L_b/2, 0, 0)`. It marks the designated forward direction (L0-CON-150, CV-170). Heading is the direction angle of the horizontal projection of `x_B` (CV-530).

### 2.3 Crew station

The crew station is the body-frame position `[P-DYN-400]` (L1-AER-250). It lies inside the capsule and forward of the CG (positive x component). It defines where the crew sits; the crew acceleration limit is evaluated at the CG, not here (D45, L1-AER-290). No quantity of this model is computed at the crew station.

### 2.4 What the shape is used for

The shape gives the mass properties (§6) and the lowest point of the body for the ground contact (§2.6, §9). It does not shape the drag under the drag form chosen (§5.5, option D1, D64); under option D2 it gives the reference areas. It has no other role: there is no lift and no control surface (L1-AER-030, -040).

### 2.5 Landing gear geometry

The Aeronef has a retractable **landing gear** (D69, L1-AER-900). Its geometry is a C1 choice (DD-C1-08, proposed):

- **Contact points.** The gear touches the ground at four contact points. At extension fraction `λ` (§9.1) they are at the body-frame positions

  ```
  p_i(λ) = ( ±a,  ±R/2,  λ·(R + [P-DYN-040]) )        i = 1 … 4 (all four sign combinations)
  ```

  so their footprint spans the cylindrical part of the body, `H` long and `R` wide.
- **Extended** (`λ = 1`): the contact points are at `z_B = R + [P-DYN-040]`, that is `[P-DYN-040]` below the lowest point of the body at level attitude (L1-AER-900). On the ground at level attitude the CG altitude is the **rest altitude** `h_r = [P-DYN-030]/2 + [P-DYN-040]`, and the height above the ground is `[P-DYN-040]` (CV-400).
- **Retracted** (`λ = 0`): the contact points are at `z_B = 0`, inside the body (`(R/2)² < R²`), so no part of the gear is below the body and the body makes any ground contact (L1-AER-900 rationale).
- **In transit** (`0 < λ < 1`): the contact points move along `+z_B` between the two positions. They leave the body when `λ·(R + [P-DYN-040])` exceeds `√(R² − R²/4)`.
- **No other effect.** The gear has no mass, no inertia and no drag of its own, and its position changes no mass property, no drag and no moment (L1-AER-900, L0-CON-130). Its only force is the ground reaction while the vehicle is on the ground (§9.6).
- **Clearance at the hover height.** At the hover height `[P-AF-210]` (a height above the ground, D70) the extended gear clears the ground by `[P-AF-210] − [P-DYN-040]` (0.124 m with the database values; B3 param_proposals §3). This is an AF item (C5, P-AF-110); DYN only computes the contact.

### 2.6 Lowest point of the body and of the vehicle

The body's x axis points along `x_B`; its down component in L is `−sin θ` (CV-250, CV-260). The capsule is the set of points within `R` of the axis segment from `−a·x_B` to `+a·x_B`, so its lowest point is at the altitude

```
h_G = h − R − a·|sin θ|
```

which is the **height above the ground** of CV-400 (it does not depend on the roll angle, because the capsule is axisymmetric about `x_B`). NAV computes `h_G` as a navigation quantity (L1-AER-530); this model uses the same expression for the ground contact.

The altitude of a body-fixed point `p` is `h − (C_LB·p)_D`, with `(·)_D` the down component in L. The **lowest point of the vehicle** is at the altitude

```
h_low = min( h_G,  min_i [ h − (C_LB·p_i(λ))_D ] )
```

The gear is the lowest point when its lowest contact point is at or below `h_G`. A contact point inside the body is never below `h_G`, because the capsule is convex, so `h_low = h_G` whenever the gear is retracted.

## 3. Vehicle state and outputs

This section is the **vehicle state** of MS-DYN.

### 3.1 Integrated state

At each simulation step `k` the **integrated state** is (L2-AER-DYN-020; G2-F15):

| Element | Symbol | Frame | Unit |
| --- | --- | --- | --- |
| Position of the CG | `r^L` | L | m |
| Velocity of the CG | `v^L` | L (components north, east, down) | m/s |
| Attitude quaternion | `q` | L → B (CV-250) | 1 |
| Body rates | `ω^B = (p, q_r, r)` | B | rad/s |

These thirteen numbers are the quantities the equations of motion integrate while the vehicle is airborne (§4). On the ground they are held at the rest state (§9.6). Under option T2 of §4.5 the model integrates `v^B` instead of `v^L`; the state reported is the same (`v^L = C_LB·v^B`). The *vehicle state* of the glossary is the integrated state plus the quantities derived from it (§3.2).

### 3.2 Quantities derived at each step

| Quantity | Definition | Reference |
| --- | --- | --- |
| Velocity in body axes `v^B` | `C_BL·v^L` | CV-460 |
| Euler angles ψ, θ, φ | From `q` by CV-260; the reported quaternion has `q0 ≥ 0` | CV-250, CV-260 |
| Vehicle acceleration `a^L` | The time derivative of `v^L` given by the translational equation (§4.2), evaluated as §3.3 states | Glossary |
| Sensed acceleration `f^B` and its magnitude | §8, evaluated as §3.3 states | Glossary, L0-CON-310 |

The altitude, height above the ground, horizontal speed, vertical speed, heading and track are navigation quantities computed by NAV from the vehicle state (L1-AER-530); MS-DYN does not redefine them (§2.6 gives the same body geometry that CV-400 uses). The vehicle mass and the remaining fuel mass are FU outputs (L1-AER-180).

### 3.3 Gear state

The **gear state** is a DYN item separate from the vehicle state (L1-AER-430, -640; glossary *Gear state*). At each step `k` it is:

| Element | Values | Source |
| --- | --- | --- |
| Gear position | extended (`λ = 1`), retracted (`λ = 0`) or in transit (`0 < λ < 1`) | Landing gear model (§9.1) |
| On the ground | true from the start of the on-ground state to its liftoff step, false otherwise (§9.6) | Ground contact model (§9.6) |

The extension fraction `λ` itself is internal to the model.

### 3.4 Evaluation instant of the acceleration quantities (DD-080, with DD-C1-11)

An acceleration depends on the inputs (control force, mass, wind), and the inputs change at step boundaries (§10.2). The acceleration quantities reported with step `k` are therefore defined as follows (DD-080, accepted, D64):

- for `k ≥ 1`: evaluated at `t_k` from the state of step `k` and the inputs held over the step from `t_{k−1}` to `t_k` (the value at the end of the step that produced the state);
- for `k = 0`: evaluated at `t_0` from the initial state and the inputs held over the first step, from `t_0` to `t_1`. These values become known when the TST commands the first step.

Additions for the ground operations (DD-C1-11, proposed):

- **At a contact step** (§9.3), the acceleration quantities are evaluated from the propagated state of that step, before the landing arrest or the crash adjustment of §9.5, with the inputs of the step that produced it. They are airborne values: the arrest on the ideal gear is not an acceleration, and no touchdown shock is computed (D53, D69).
- **On the ground** (`G` true over the step from `t_{k−1}` to `t_k`, and no liftoff at step `k − 1`), the total force and moment include the ground reaction (§9.6). The vehicle acceleration is then zero and the sensed acceleration is `−C_BL·g^L`, of magnitude `[P-DYN-010]`, upward. This holds for step 0 of a start on the ground.

This makes the acceleration of step `k ≥ 1` available at the same time as the rest of the state of step `k`, so it can be part of the frame-start state (L1-AER-440). It is a convention of this model, not physics; the glossary entry *Vehicle state* states it (CR-C1-02).

### 3.5 Outputs

| Output | Consumer | Interface |
| --- | --- | --- |
| Vehicle state of each step (§3.1, §3.2) | NAV, FC at the start of each control frame | Vehicle-model boundary ICD (IN-B1-01; L1-AER-430, -440) |
| Gear state of each step (§3.3) | AF at the start of each control frame | Vehicle-model boundary ICD (L1-AER-430) |
| Vehicle state, gear state and sensed acceleration of each step | TM (operational data) | ICD-AER-TST (L1-AER-640) |
| Ground-contact event record, landing or crash (§9.8) | TM and TST | ICD-AER-TST (L1-AER-260, -270; I-37, I-41) |
| Initial-condition error (§10.3) | TST | ICD-AER-TST (glossary *Initial-condition error*) |

The wind is a vehicle-model input only. The flight software does not receive it (L1-AER-670).

## 4. Equations of motion

This section is the **equations of motion** of MS-DYN.

### 4.1 Assumptions

1. The vehicle is a rigid body with six degrees of freedom; there is no structural flexibility and no fuel slosh (L0-CON-010, L0-ASM-080).
2. The local reference frame L is inertial; the world is flat and does not rotate (L0-ASM-030, CV-110, CV-140).
3. The body origin is the CG, fixed in the body at every fuel state and at every gear position (L0-CON-130, CV-160, L1-AER-210, -900).
4. The mass and the inertia vary with the fuel state, as FU gives them at each step (L1-AER-180, -220). Consumed fuel leaves the vehicle without imparting force or moment; its only effect is the loss of mass (L0-ASM-090). The equations therefore take the instantaneous mass properties: there is no thrust term `ṁ·v` and no `J̇·ω` term. (For mass that leaves the body with the local velocity of the body, the momentum it carries away cancels those terms exactly; L0-ASM-090 states this as the model.)
5. The body axes are principal axes of inertia: `J` is diagonal (D61).
6. The equations below propagate the motion while the vehicle is airborne. While it is on the ground the integrated state is held at the rest state (§9.6), where the ground reaction makes the total force and moment zero.

### 4.2 Translational equation

The total force `F` is the sum of gravity, drag, the control force and, on the ground, the ground reaction (§5.1). While airborne, in L:

```
F^L = m·g^L + D^L + C_LB·F_c^B
dr^L/dt = v^L
```

The rate of change of the velocity is given by one of the two options of §4.5:

| | Option T1 — rotation-during-translation term retained (chosen, D64) | Option T2 — term removed |
| --- | --- | --- |
| Equation integrated | `m·dv^L/dt = F^L` (Newton's second law in the inertial frame L) | `m·dv^B/dt = C_BL·F^L` (no `ω^B × v^B` term) |
| Same equation in the other frame | `dv^B/dt = C_BL·F^L/m − ω^B × v^B` | `dv^L/dt = F^L/m + ω^L × v^L` |
| Vehicle acceleration `a^L` | `F^L/m` | `F^L/m + ω^L × v^L` |
| Velocity under a yaw rotation with no force | `v^L` constant; `v^B` turns with the body | `v^B` constant; `v^L` turns with the heading |

`m` is the vehicle mass of the current step (assumption 4). Gravity enters as `m·g^L`, so the acceleration due to gravity does not depend on the mass.

### 4.3 Rotational equation

About the CG, in body axes, with the diagonal inertia tensor of the current step, while airborne:

```
J·dω^B/dt + ω^B × (J·ω^B) = M_c^B
```

In components:

```
I_xx·dp/dt   = M_x + (I_yy − I_zz)·q_r·r
I_yy·dq_r/dt = M_y + (I_zz − I_xx)·r·p
I_zz·dr/dt   = M_z + (I_xx − I_yy)·p·q_r
```

While airborne the only external moment is the control moment (§5.1): gravity and drag act at the CG and give no moment under either drag form (§5.5). The product terms on the right are the gyroscopic term (§4.5).

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

This section is the **kinematic terms** list of MS-DYN. L1-AER-020 and L0-CON-030 exclude every term by which motion along one degree of freedom produces an acceleration along another degree of freedom in the body frame, other than the rigid-body kinematic terms that this section lists (D18, #81). Every other cross-axis term is excluded: there is no effector coupling (EF), no product of inertia (D61, §6), and the drag meets D18 in the reading recorded below.

| ID | Term | Where it appears | Status | Effect in normal operation |
| --- | --- | --- | --- | --- |
| K-1 | Gyroscopic term `ω^B × (J·ω^B)` | Rotational equation (§4.3) | Retained (D64; #81 closed) | Zero. With pitch and roll held at zero (D57) the body rates are `(0, 0, r)`, and every product term of §4.3 contains `p` or `q_r`. It is non-zero only during pitch or roll transients within `[P-AF-180]` and after fuel exhaustion, when the attitude is free (L1-AER-390). It is what conserves the angular momentum in a torque-free rotation (§11, check C-3). |
| K-2 | Rotation-during-translation term `ω^B × v^B` | Translational equation written in body axes (§4.2) | **Retained** (option T1, D64; #81.1 closed). Option T2, removing it, is not used | In Heading at a non-zero horizontal speed, a heading change turns the body under the velocity (T1) or turns the velocity with the body (T2). In Stationary, Hover, Takeoff, Land, on the ground and in a turn in place the horizontal speed is near zero and the term is near zero. Vertical motion is unaffected under both options: with `ω^B = (0, 0, r)` the term has no body z component. |
| K-3 | Resolution of gravity, drag, the control force and the ground reaction through the attitude, `C_BL` and `C_LB` | Both equations, and the ground reaction (§9.6) | Retained (inherent in a rigid body with body-fixed effectors; D64) | Gravity stays along `z_B` while pitch and roll are zero. A body-fixed control force turns with the heading in L. It is a change of frame, not a force. |

**Drag and D18 (D72, answering G2 Q3; G2-F06).** Under the isotropic drag of §5.5 (option D1, D64), a motion along one body axis gives a drag force along that axis only, so a translation along one axis causes no acceleration along another (D18; L2-AER-DYN-190). For an oblique air-relative velocity the drag along each body axis depends on the other components through the shared airspeed magnitude `|v_a|`: the drag along `x_B` is `−½·ρ·[P-DYN-100]·|v_a|·v_a,x`. The owner accepts this as meeting D18 (D72): it is not a term by which motion along one axis produces a force along another, because the force along each axis stays proportional to, and opposite to, the motion along that axis. It is recorded here so that the roll-up of L0-CON-030 and L1-AER-020 has an explicit basis.

Notes:

- K-2 is a choice between two models, not a numerical detail. Option T1 is Newton's second law in an inertial frame: it conserves linear momentum, it is what the free-fall and terminal-velocity checks assume, and it is the standard rigid-body model. Option T2 reads D18 literally ("seen from the aircraft's body frame"): with no force, the velocity stays fixed in the body, so the vehicle's path turns with its heading. It is not Newtonian. The owner chose T1 (D64); T2 is kept here only to record the alternative.
- With T1, the lateral acceleration of a turn depends on the ground velocity (horizontal speed times heading rate). [P-SYS-230] is a ground speed (D72), so with a tailwind the airspeed exceeds it but the turn acceleration does not; C5 bounds the commanded heading rate so that the horizontal speed times the heading rate stays within `[P-AF-200]` (D72; IN-C1-32).
- L2-AER-DYN-050 requires the model to contain exactly the terms listed here, and L1-AER-020 cites this section (CR-C1-01).

## 5. External forces and moments

### 5.1 Total force and total moment

This section is the **total force and moment** of MS-DYN. It closes the list of L1-AER-050 and L0-CON-090.

```
F^L = m·g^L + D^L + C_LB·F_c^B + R^L
M^B = M_c^B + M_R^B
```

- Gravity (§5.2) and drag (§5.5) are the only external forces while airborne. Both act at the CG.
- The control force `F_c^B` and the control moment `M_c^B` come from the effectors only (EF, §7; L1-AER-080). While airborne they are the only source of moment. On the ground with the effectors off they are zero (L1-AER-930).
- The **ground reaction** `R^L`, `M_R^B` acts only while the vehicle is on the ground, through the extended landing gear (§9.6; L1-AER-920). It balances the other forces and moments, so that the vehicle stays at rest. It is not a control force (CR-B3-02). It is zero while airborne.
- A ground contact of the airborne vehicle is not a force: it is detected and classified as a landing or a crash (§9.3, §9.4). The landing arrest computes no touchdown shock (D53), and a crash ends the run (L0-ASM-110 as revised by CR-B3-07).
- There is no aerodynamic force other than the drag force: no lift (L1-AER-030). There is no aerodynamic control surface and no force that depends on a surface deflection (L1-AER-040). The landing gear adds no drag (§2.5).
- Consumed fuel gives no force and no moment (L0-ASM-090).
- No electrical quantity exists in this model (L0-CON-160, D54); the gear moves without an energy model (CR-B3-04).

### 5.2 Gravity model

This section is the **gravity model** of MS-DYN. Gravity is uniform: the acceleration `g^L = (0, 0, [P-DYN-010])` is the same everywhere and at every time, along `+z_L` (L0-ASM-040, CV-110, CV-180, L1-AER-060). The gravity force is `m·g^L` at the CG. There is no gravity-gradient moment. `[P-DYN-010]` is standard gravity, 9.806 65 m/s² (Set, D64; TT-150 closed).

A **gravity-free check configuration** is a vehicle parameter set with `[P-DYN-010] = 0`. Only the credibility checks C-3 and C-5 use it (§11, D72): without gravity no ground contact ends them, so they can run over the accuracy horizon `[P-DYN-270]`. The atmosphere does not depend on `[P-DYN-010]` (§5.3).

### 5.3 Atmosphere model

This section is the **atmosphere model** of MS-DYN. The air density is that of the **U.S. Standard Atmosphere, 1976**, which is identical to the ICAO Standard Atmosphere up to 32 km (D20, L0-ASM-060). It depends on altitude only and does not vary with time.

- **Altitude.** The standard is defined in geopotential altitude. On the flat world of CV-110, with uniform gravity, the geopotential altitude is taken equal to the altitude `h` of CV-430, by definition (DD-090).
- **Constants of the standard.** These are constants of the named standard. They are not parameters, and they do not change if `[P-DYN-010]` changes.

| Constant | Value |
| --- | --- |
| Standard gravity used by the standard, `g_0` | 9.806 65 m/s² |
| Universal gas constant, `R*` | 8.314 32 J/(mol·K) |
| Molar mass of air, `M_0` | 0.028 964 4 kg/mol |

The seven layers of the standard up to 84 852 m geopotential (86 km geometric) are used (DD-C1-07, proposed, which extends the range of DD-090; G2-F08):

| Layer `b` | Base altitude `h_b` (m) | Base temperature `T_b` (K) | Lapse rate `L_b` (K/m) | Base pressure `p_b` (Pa) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 288.15 | −0.0065 | 101 325.0 |
| 1 | 11 000 | 216.65 | 0.0 | 22 632.06 |
| 2 | 20 000 | 216.65 | +0.0010 | 5 474.889 |
| 3 | 32 000 | 228.65 | +0.0028 | 868.0187 |
| 4 | 47 000 | 270.65 | 0.0 | 110.9063 |
| 5 | 51 000 | 270.65 | −0.0028 | 66.938 87 |
| 6 | 71 000 | 214.65 | −0.0020 | 3.956 420 |

For `h_b ≤ h < h_{b+1}` (with `h_7 = 84 852 m`):

```
T(h) = T_b + L_b·(h − h_b)
p(h) = p_b · (T_b / T(h)) ^ (g_0·M_0 / (R*·L_b))       if L_b ≠ 0
p(h) = p_b · exp(−g_0·M_0·(h − h_b) / (R*·T_b))         if L_b = 0
ρ(h) = p(h)·M_0 / (R*·T(h))
```

- **Below zero.** The layer-0 equations also apply for `h < 0` (the standard defines them down to −5 000 m). The CG is never below the datum plane in a reported state (CV-420), but an integrator may evaluate the drag inside a step that ends at a contact step, and the density is then defined.
- **Above the top.** For `h ≥ 84 852 m` the density is zero (vacuum). No run of the operating volume reaches it: from the maximum operating altitude `[P-SYS-200]` (45 720 m) a ballistic climb to it needs a vertical speed of about 875 m/s.
- At `h = 0` this gives ρ = 1.2250 kg/m³; at 47 000 m, 1.4275·10⁻³ kg/m³; at 84 852 m, 6.958·10⁻⁶ kg/m³. Only the density is used; temperature and pressure are not model outputs (CV-430). The maximum operating altitude `[P-SYS-200]` lies within layer 3 (IN-C1-39 closed).

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
- **At liftoff.** The wind envelope at a liftoff is limited to `[P-SYS-580]` (D73, B3-2; L1-AER-960): on the ground the ground reaction holds the vehicle against the drag of the wind, and at liftoff that drag acts at once on the airborne vehicle (§9.6). DYN does not check the limit; the TST applies it.
- **Rise time.** `[P-SYS-570]` = 2.0 s (TBR, TT-650; accepted by the owner, D64): for a vehicle near rest, about the time a gust front of the longest FAR 25.341 gust gradient (350 ft, 107 m) takes to pass at the steady wind `[P-SYS-430]`. For a moving vehicle the passage time of a frozen gradient is shorter (0.46 s at an airspeed of 231.5 m/s), but this model is uniform in space and defined in time, so the rise time is a definition of the envelope, not a passage time (G2-F25). It is 20 times the control-loop latency `[P-SYS-480]`, so flight control can follow it. C4 confirms the gust share of `[P-FC-020]` and `[P-FC-010]` against it at I1 (FUNCTIONAL_ANALYSIS §7.2, §7.4).
- **Sampling.** The wind given with the command for the step from `t_k` to `t_{k+1}` is the wind at `t_k`. The model holds it over that step (§10.2). ICD-AER-TST fixes the signal (IN-C1-20).
- A wind that varies across the operating volume is outside this model (#84).

### 5.5 Drag model

This section is the **drag model** of MS-DYN. Drag acts on the air-relative velocity `v_a^L = v^L − w^L` (L1-AER-070, CV-470), with the density `ρ(h)` of the atmosphere model at the vehicle altitude. It acts at the CG. The form is a design choice of C1, bounded by L1-AER-020 and L1-AER-030; it is recorded as DD-050 and DD-060, and the owner chose D1 (D64).

| | Option D1 — isotropic quadratic drag (chosen, D64) | Option D2 — per-axis quadratic drag in body axes |
| --- | --- | --- |
| Force | `D^L = −½·ρ(h)·[P-DYN-100]·|v_a^L|·v_a^L` | `D_i^B = −½·ρ(h)·C_D,i·A_i·|v_a,i^B|·v_a,i^B` for `i = x, y, z`, with `v_a^B = C_BL·v_a^L` |
| Parameters | Drag area `[P-DYN-100]` (C_D·A, m²) | Three drag coefficients `C_D,i` (new parameters if chosen) and the reference areas from the capsule: `A_x = π·D_b²/4`, `A_y = A_z = H·D_b + π·D_b²/4` |
| Direction | Opposite to the air-relative velocity: no component perpendicular to it, so no lift | Not opposite to the air-relative velocity for an oblique flow: a cross-flow component exists |
| Attitude dependence | None | Through `C_BL` (the elongated shape) |
| Cross-axis property (L1-AER-020) | An air-relative velocity along one body axis gives a drag force along that axis only. With a velocity on two axes, the magnitude `|v_a|` is shared; this meets D18 (D72, §4.5). | The drag along each body axis depends only on the air-relative velocity along that axis |
| Moment | None (acts at the CG) | None (acts at the CG) |

Common to both options:

- **No aerodynamic moment.** The drag acts at the CG and there is no rotational damping moment (DD-050). A vehicle at fuel exhaustion keeps its angular momentum, as CONOPS SC-110 leg 11 and the L1-AER-200 and -390 rationales describe ("keeps the angular rate it had"). The drag-moment lines of the moment authority budget (L1-AER-140, FUNCTIONAL_ANALYSIS §7.1) are zero under this model.
- **No Mach or Reynolds dependence.** The coefficients are constant; this is a definition of the fictional vehicle.
- **No gear drag.** The landing gear adds no drag in any position (§2.5, L1-AER-900).
- **On the ground.** The vehicle is at rest, so the air-relative velocity is minus the wind and the drag is `½·ρ(h_r)·[P-DYN-100]·|w^L|·w^L`, along the wind. The ground reaction balances it (§9.6).
- **Budget form.** Under D1 the drag at airspeed `V` is `D(V) = ½·ρ·[P-DYN-100]·V²` along the air-relative velocity, and its component along any body axis is at most `D(V)`. This is the `D(V)` of FUNCTIONAL_ANALYSIS §7.1. The budgets use the sea-level density ρ(0) = 1.225 kg/m³, the largest density that a vehicle at or above the ground meets (the operating volume is bounded below by a height above the ground, CR-B3-16, and Takeoff and Land fly down to the ground). `[P-SYS-230]` is a ground speed (D72, G2-F03), so the largest airspeed is `[P-SYS-230] + [P-SYS-430] + [P-SYS-560]` (231.5 m/s with the database values).
- **Vacuum-equivalent configuration.** A vehicle parameter set with `[P-DYN-100] = 0` (D1), or each `C_D,i = 0` (D2), has no drag. The credibility checks of §11 use it.

Why D1 (chosen by the owner, D64): it has no lift by construction (L1-AER-030 is then shown by inspection of one line), it has no attitude dependence, so translation and attitude are independent through the aerodynamics in every frame (L0-CON-020), it gives the single `D(V)` the L1 budgets are written with, and a pure motion along one body axis produces drag along that axis only (D18). AIRCRAFT_CHARACTERISTICS §1 says the exterior shape matters only through the mass properties, which D1 respects. D2 meets D18 in the stronger "per axis" reading but gives a cross-flow force for oblique flow, which an inspection of L1-AER-030 could read as lift.

## 6. Mass-properties model

This section is the **mass-properties model** of MS-DYN. **Content owner: C2 (FU).** L1-AER-220 asks MS-DYN to state the body shape and the mass distribution from which the inertia is derived. The shape is §2. The mass distributions of the dry mass and of the fuel, the fuel placement and the derivation of the inertia are C2's (DD-120, D65; G2-F16); C2's text is merged here at I1.

What DYN needs from FU, at each step `k` (IN-C1-01, IN-C1-02):

- the vehicle mass `m_k = [P-FU-030] + (remaining fuel mass)` (L1-AER-180);
- the inertia tensor about the CG, in the body axes: three principal moments of inertia `I_xx`, `I_yy`, `I_zz` with zero products of inertia (D61, CV-350);
- the CG at the body origin at every fuel state and at every gear position (L1-AER-210, -900). The CG position therefore does not cross the FU–DYN interface I-04 (G2-F05; FUNCTIONAL_ANALYSIS I-04 as aligned by CR-B3-39).

**Reference derivation (for C2).** For mass `m` distributed with uniform density over the solid capsule of §2.1 (radius `R = D_b/2`, cylinder length `H`):

```
m_cyl  = m · H / (H + 4R/3)          (cylinder part)
m_hem  = m · (2R/3) / (H + 4R/3)     (each hemisphere)
I_xx   = m_cyl·R²/2 + 2·m_hem·(2R²/5)
I_yy   = I_zz = m_cyl·(R²/4 + H²/12) + 2·m_hem·(2R²/5 + H²/4 + 3·H·R/8)
```

Any distribution that is symmetric under reflection in each body coordinate plane gives a diagonal tensor with the CG at the centre. An axisymmetric distribution about `x_B` also gives `I_yy = I_zz`, which the torque-free check C-3 can use. The landing gear has no mass (L1-AER-900). **C2 content slot** (aligned with L2-AER-FU-280, G2-F16): the mass distribution of the dry mass and of the fuel; the vehicle mass and the centre of gravity; the inertia as a function of the remaining fuel mass (DD-120); the parameters it needs.

## 7. Effector and fuel models

This section is the **effector and fuel models** of MS-DYN. **Content owners: C3 (EF) for §7.1, C2 (FU) for §7.2.** L1-AER-160 and -720 place these models in MS-DYN; their text is merged here at I1.

### 7.1 Effector model (C3)

What DYN needs from EF, for each step (IN-C1-10):

- the control force `F_c^B` and the control moment `M_c^B` about the CG, in body axes, computed once by EF from the effector outputs through their control effectiveness (L1-AER-100; DD-C3-05, D73);
- one value per step, held over the step (§10.2);
- zero force and zero moment at fuel exhaustion (L1-AER-200) and with the effectors off (L1-AER-930; IN-C3-03);
- zero at step 0 of a start on the ground, where the effectors are off (L1-AER-950; IN-C1-12 answered by C3).

**C3 content slot:** direction of action, control effectiveness, output limits and command response of each effector (L1-AER-090 to -110, -710). C3's text is `work/C3/ms_dyn_s7_effectors.md`, merged here at I1 (IN-C3-01).

### 7.2 Fuel model (C2)

What DYN needs: the fuel availability of each step, for the classification of a ground contact (§9.4; D68; FUNCTIONAL_ANALYSIS I-03 as revised by CR-B3-39). Otherwise nothing directly: the fuel model gives the vehicle mass through FU (§6), and consumed fuel gives no force and no moment (L0-ASM-090), so the fuel mass flow does not enter the equations of motion.

**C2 content slot** (aligned with L2-AER-FU-280, G2-F16): the translational and rotational consumption relationships and their parameters `[P-FU-040]`, `[P-FU-050]`, with zero flow at zero control force and moment (L1-AER-160, -170, -940; DD-110); the fuel accounting, the remaining fuel mass as the initial fuel mass minus the integral of the flow, with the exhaustion-step limit (L1-AER-190; DD-130); the fuel availability (L1-AER-200).

## 8. Sensed acceleration

This section is the **sensed acceleration** of MS-DYN. The sensed acceleration is the acceleration the crew feels: the sum of the non-gravitational forces on the vehicle divided by its mass (specific force), evaluated at the CG (glossary; D38, D45; L1-AER-290):

```
f^B = (F_c^B + C_BL·(D^L + R^L)) / m
|f| = magnitude of f^B
```

- It is evaluated at the CG, so rotation adds nothing to it (D45).
- In free fall it is zero (no control force, no drag). In a still-air hover at level attitude, with the control force equal to the weight, it is `g` along `−z_B` (glossary).
- At rest on the ground the ground reaction makes it `−C_BL·g^L`, of magnitude `[P-DYN-010]`, upward (L1-AER-920, CR-B3-15).
- With the rotation-during-translation term retained (option T1, D64) it equals `a^L − g^L` resolved in B, airborne and on the ground; this is the relation that FUNCTIONAL_ANALYSIS §7.2 uses for the crew budget.
- At a contact step it is the airborne value of the propagated state (§3.4). The landing arrest on the ideal gear is not an acceleration and computes no touchdown shock (D53, D69).
- It is evaluated at the instant §3.4 states.

## 9. Landing gear and ground contact

This section holds the **landing gear model** (§9.1) and the **ground contact model** (§9.2 to §9.9) of MS-DYN (L1-AER-720 as revised by CR-B3-27). The ground is the datum plane at altitude zero, flat, with no terrain (D8, CV-420). The landing gear and the ground contact are ideal: there is no spring, damping, bounce, friction, sliding or tipping model (D37 as revised by D69, L0-ASM-110 as revised by CR-B3-07, L0-CON-290). The geometry is §2.5 and §2.6.

### 9.1 Landing gear model

- **Gear position and extension fraction.** The gear has an extension fraction `λ ∈ [0, 1]`. The gear position (§3.3) is extended at `λ = 1`, retracted at `λ = 0` and in transit otherwise.
- **Landing gear command.** Autoflight commands the gear to extend or to retract across the vehicle-model boundary (L1-AER-430 as revised by CR-B3-19; L1-AER-910). The command is issued once per control frame and held over the steps of the frame, like the effector commands (§10.2). Before the first landing gear command of a run, the commanded position is the gear position of the initial condition.
- **Movement while airborne.** While the vehicle is airborne, whenever the gear position differs from the commanded position, the gear moves toward it at the constant rate of one full travel in `[P-DYN-050]` (DD-C1-08):

  ```
  λ(k+1) = min(1, λ(k) + Δt/[P-DYN-050])     if the command of step k is "extend"
  λ(k+1) = max(0, λ(k) − Δt/[P-DYN-050])     if the command of step k is "retract"
  ```

  A full transit therefore takes `[P-DYN-050]` (to within one step; L1-AER-910). A command that reverses a transit moves the gear back from its current fraction, so it reaches the new position sooner. A command given before the vehicle becomes airborne (on the ground) takes effect from the first airborne step.
- **On the ground.** While the vehicle is on the ground the gear is held extended (`λ = 1`) whatever the command (L1-AER-910 rationale, L1-AER-920): a retraction there would drop the body onto the ground.
- **After a crash.** The gear position is held with the rest of the state (§9.7).
- **No other effect.** The gear position changes no mass property, no drag and no moment (§2.5).

### 9.2 Airborne and on the ground

At each step the vehicle is in one of three states: **airborne**, **on the ground** or **crashed** (glossary *Airborne*, *On the ground*, *Crash* as revised by CR-B3-37):

| State | Begins | Ends |
| --- | --- | --- |
| Airborne | At the start of a run that starts airborne (§10.3), or at the step after a liftoff step (§9.6) | At the next contact step (§9.3), which is not airborne |
| On the ground | At the start of a run on the ground (§10.3), or at the contact step of a landing (§9.4) | At its liftoff step (§9.6), the last step on the ground |
| Crashed | At the contact step of a crash (§9.4) | At the end of the run |

### 9.3 Detection: the contact step

While the vehicle is airborne, the **contact step** is the first simulation step at which the propagated altitude `h_low` of the lowest point of the vehicle (§2.6), with the gear at its extension fraction of that step, is at or below zero (CV-940 "reaches"). The model checks every airborne step. There is no detection while the vehicle is on the ground or crashed. A run can have several contact steps: one at each landing, and at most one crash, which ends the run. The contact step is the "contact sample" of L1-AER-280 and of the glossary *Landing envelope*.

### 9.4 Classification

At the contact step, with the propagated state of that step: the vertical speed `VS = −v_D`, the horizontal speed `V_H = √(v_N² + v_E²)` (ground-referenced, CV-480, CV-490), the gear position, the point that is lowest (§2.6) and the fuel availability of the step from FU (I-03; §7.2):

- the contact is a **landing** when all of these hold (L1-AER-260 and -280 as revised by CR-B3-12, -14; D53, D68, D69):
  1. the gear position is extended;
  2. the lowest point of the vehicle is a contact point of the gear (the vehicle touches on its gear, not on its body);
  3. fuel is available;
  4. `|VS| ≤ [P-SYS-500]` and `V_H ≤ [P-SYS-510]`;
- otherwise it is a **crash** (L1-AER-270 as revised by CR-B3-13): outside the speed envelope, with the gear retracted or in transit, with the body touching first, or at fuel exhaustion, whatever the speeds (D73, B3-3).

There is no acceleration limit (D53). The speeds are not interpolated to the crossing instant: the classification uses the propagated state of the contact step, which keeps it exact on the CV-840 time base.

### 9.5 State reported at the contact step (DD-070, revised by DD-C1-10)

- **Landing.** The state of the contact step is reported as the **rest state** (§9.6) at the propagated horizontal position and the propagated heading. The vehicle is on the ground from this step (L1-AER-920). The run goes on.
- **Crash.** The propagated state is reported with its altitude raised by `−h_low`, so that the lowest point of the vehicle is on the datum plane; the horizontal position, the velocity, the attitude and the body rates stay as propagated (CV-420: no point of the vehicle below the datum plane, CR-B3-36).
- In both cases the classification (§9.4) and the acceleration quantities of the step (§3.4) use the propagated state, before the report. The CG is never at altitude zero: at a landing it is at the rest altitude `h_r`, and at a crash at least `R` above the datum plane.

### 9.6 On the ground: rest state, ground reaction and liftoff

- **Rest state.** The rest state at a horizontal position `(x_N, y_E)` and a heading `ψ_r` is: position `r^L = (x_N, y_E, −h_r)` with `h_r = [P-DYN-030]/2 + [P-DYN-040]` (§2.5); velocity zero; attitude level at heading `ψ_r`, that is `q = (cos(ψ_r/2), 0, 0, sin(ψ_r/2))`, sign as CV-250; body rates zero; gear extended (L1-AER-920). At level attitude the extended gear contact points are then on the datum plane.
- **Held.** While the vehicle is on the ground, the integrated state of each step is the rest state of the step before: it is held, not integrated (DD-C1-11). The heading is held too: a control moment about `z_B` does not turn the vehicle on the ground.
- **Ground reaction.** Over each step from `t_k` that the vehicle spends on the ground (step `k` on the ground and not its liftoff step), the ground applies through the gear the force and moment

  ```
  R^L   = −( m·g^L + D^L + C_LB·F_c^B )
  M_R^B = −M_c^B
  ```

  with the inputs of step `k` (§10.2). The total force and moment of §5.1 are then zero, which is the static equilibrium of the ideal gear: no sliding in the wind, no tipping, no turning (L1-AER-920). While airborne `R^L` and `M_R^B` are zero.
- **Liftoff.** Step `k` on the ground is the **liftoff step** when the upward component of the control force exceeds the weight:

  ```
  −(C_LB·F_c^B(k))_D > m(k)·[P-DYN-010]
  ```

  with the control force and mass of step `k`. The wind is horizontal (§5.4), so the drag at rest has no vertical component and the condition is the same as "the ground would have to pull" (glossary *Liftoff*). At the liftoff step the reported state is still the rest state, and `G` is still true. The step from `t_k` to `t_{k+1}` is propagated by the equations of motion of §4 with no ground reaction; step `k + 1` is airborne, and from it the ground contact is detected again (§9.3) and the gear follows its command (§9.1). The liftoff condition is evaluated at each step on the ground, including the contact step of a landing and step 0 of a start on the ground.
- **Consequences.** On the ground the vehicle acceleration is zero and the sensed acceleration is `[P-DYN-010]` upward (§3.4, §8). At liftoff in a wind, the drag of the wind acts at once on the airborne vehicle, which is why the wind at liftoff is limited to `[P-SYS-580]` (§5.4, L1-AER-960). The effectors are off on the ground except while autoflight is taking off (L1-AER-930); that is an EF, FC and AF matter, and DYN applies whatever control force EF gives.

### 9.7 Crash

At a crash the TST ends the run (I-41; L1-AER-270 as revised). If the TST commands a further step, the model keeps the state of the contact step (§9.5), applies no ground reaction and raises no further event.

### 9.8 Event records

At each contact step the model outputs one event record, with the classification (landing or crash) and the timestamp of the contact step (CV-840), to TM and to the TST (I-37, I-41). A landing does not end the run; the TST ends the run on a crash (CONOPS §4.6 as revised by CR-B3-33).

### 9.9 Start on the ground

An initial condition with the landing gear extended is a start on the ground (§10.3; DD-C1-09, proposed). The vehicle is on the ground from step 0, in the rest state at the horizontal position and the heading of the initial condition (L1-AER-950).

## 10. Simulation step and integration

This section is the **simulation step** of MS-DYN.

### 10.1 Step

The model advances in fixed simulation steps of `Δt = [P-SYS-300]` (CV-820, F-TST-01). Each step command from the TST advances the state from step `k` at `t_k = k·Δt` to step `k + 1` (L1-AER-670). Simulation time is set by the step index, not accumulated (CV-820).

### 10.2 Inputs over a step

Over the step from `t_k` to `t_{k+1}` the following inputs are held constant at their step-`k` values (DD-100):

| Input | Source |
| --- | --- |
| Control force `F_c^B` and control moment `M_c^B` | EF, effector outputs of step `k` |
| Vehicle mass `m` and inertia tensor | FU, step `k` |
| Fuel availability (for the classification at a contact step) | FU, step `k` (DD-130) |
| Landing gear command | AF, the command of the control frame that contains step `k` (§9.1) |
| Wind velocity `w^L` | TST, given with the command for the step (§5.4) |

The state-dependent quantities (gravity resolved in body axes, the air-relative velocity, the density, the drag, the gyroscopic term) vary within the step with the state. The fuel availability used to classify a contact at step `k` is that of step `k`.

### 10.3 Integration and initial state

- The integration method is a design choice (D4). It is constrained only by the accuracy that the credibility checks of §11 state and by reproducibility.
- **Accuracy.** The model meets the tolerances of the credibility checks of §11 in their configurations: C-1, C-2 and C-4 at each step of their run to the contact step or to their end; C-3 and C-5 over the accuracy horizon `[P-DYN-270]` (600 s, D72) in the gravity-free check configuration; C-6 at each step of C-3, C-5 and the reference mission; C-9 at each step on the ground. No check runs for the duration of a long hold (D72, G2-F01). These tolerances bound the numerical error of the integration. Numerical integration error is not a share of any performance budget (FUNCTIONAL_ANALYSIS §7.4).
- **Reproducibility.** The state of step `k + 1` depends only on the state of step `k`, the inputs of step `k` and the vehicle parameter set (L1-AER-690, D59). It does not depend on wall-clock time, on the execution host's scheduling or on a random number.
- **Initial state** (L1-AER-660 as revised by CR-B3-26, L1-AER-950; D73, B3-1). The parameters come from the vehicle parameter set of the run. The landing gear position of the initial condition decides the kind of start (DD-C1-09):
  - **Start on the ground** (gear extended): the operational start, and the start of the reference mission SC-110 and of SC-130. Step 0 is the rest state (§9.6) at the horizontal position and the heading of the initial condition; the vehicle is on the ground. The altitude of the initial condition is replaced by the rest altitude `h_r` (I1 decides whether ICD-AER-TST carries it for a ground start; IN-C1-21). The model raises an initial-condition error naming each item if the initial velocity, the initial body rates, the initial pitch angle or the initial roll angle is not zero, and the run does not start.
  - **Airborne start** (gear retracted): allowed only for test runs and credibility checks (D73, B3-1). Step 0 is the position, velocity, attitude and body rates of the initial condition; the vehicle is airborne. The model raises an initial-condition error if the lowest point of the body is at or below the datum plane (`h_G ≤ 0`, §2.6).
  - A gear position other than extended or retracted is not a valid initial condition item (ICD-AER-TST, IN-C1-21).

## 11. Credibility checks

This section is the **credibility checks** of MS-DYN. Following NASA-STD-7009B and METHODOLOGY §10.3, each check compares the simulated motion with an independent solution: a closed form, a conservation law or a static equilibrium, computed outside the model. Each check names its configuration. The configurations are definitions of the checks; the test procedure sets the remaining scenario values (D32). The tolerances are parameters, because they are requirements on the model.

**Common conditions.**

- The vehicle parameter set is the run's, changed only as each check states.
- C-1 to C-5 start airborne, with the landing gear retracted, as credibility checks may (D73, B3-1; §10.3).
- "Zero fuel" means an initial fuel mass of zero, so the effectors produce no force and no moment (L1-AER-200) and the mass is the dry mass `[P-FU-030]`, constant. The effectors off give the same zero force and moment (L1-AER-930; IN-C3-03).
- **Relative error.** At step `k ≥ 1`, the relative error of a vector quantity is the norm of its error divided by the largest norm of the change of its expected value from `t_0` to any step up to `k`; for a scalar, the absolute values. It is not evaluated at step 0, where the state is the initial condition exactly (L2-AER-DYN-430). Where a check divides by another quantity (C-2, C-5), it says so (G2-F14).

| ID | Check | Configuration | Independent solution | Tolerance | Requirement |
| --- | --- | --- | --- | --- | --- |
| C-1 | Free fall | Zero fuel; vacuum-equivalent (§5.5); airborne start at any position with `h_G > 0`, any velocity, attitude and body rates | `r^L(t) = r_0 + v_0·t + ½·g^L·t²`, `v^L(t) = v_0 + g^L·t`, until the contact step. Sensed acceleration zero. | Relative error of the position and of the velocity at each step to the contact step: at most `[P-DYN-200]` | L2-AER-DYN-600 |
| C-2 | Free fall with drag to terminal vertical speed | Zero fuel; drag on; level attitude, zero body rates; released at rest vertically at the altitude 3 000 m, with a horizontal velocity equal to the steady wind velocity; still air, and a steady wind of up to `[P-SYS-430]` without gusts | Horizontal velocity equal to the wind velocity. Vertical speed tends to `−v_exp(h)` with `v_t(h) = √(2·m·g / (ρ(h)·[P-DYN-100]))` (under option D2, `C_D,z·A_z` in place of `[P-DYN-100]`) and the quasi-steady correction for the density gradient `v_exp(h) = v_t(h)·(1 − v_t(h)²·(dρ/dh)/(4·g·ρ(h)))` | At each step from the altitude 1 500 m down to the contact step: `|(|VS| − v_exp(h))| / v_exp(h)` at most `[P-DYN-210]`, and the horizontal velocity error divided by the wind speed at most `[P-DYN-210]` (G2-F02). | L2-AER-DYN-140, -610 |
| C-3 | Torque-free rotation | Zero fuel; **gravity-free check configuration** (§5.2) (drag on or off: drag gives no moment); zero initial velocity; initial body rates `p`, `q_r` and `r` all non-zero, each of magnitude at most `[P-SYS-270]` | Angular momentum in L, `H^L = C_LB·J·ω^B`, constant; rotational kinetic energy `½·ω^B·J·ω^B` constant. If `I_yy = I_zz = I_t`: `p` constant, and `(q_r, r)` rotates at the rate `(I_t − I_xx)·p / I_t` | Relative change of `|H^L|`, change of the direction of `H^L` (angle in rad) and relative change of the kinetic energy, at each step over `[P-DYN-270]`: each at most `[P-DYN-220]` (G2-F01) | L2-AER-DYN-620 |
| C-4 | Variable mass under a constant force | Vacuum-equivalent; level attitude, heading north, zero body rates; DYN driven with a prescribed constant control force `F` along `+x_B` and a prescribed mass `m(t_k) = m_0 − ṁ·t_k` in place of EF and FU outputs | `v_N(t) = v_N0 + (F/ṁ)·ln(m_0 / m(t))`; the vertical motion is the free fall of C-1 | Relative error of `v_N`: at most `[P-DYN-240]`. The procedure keeps `ṁ·Δt/(2·m)` below a tenth of `[P-DYN-240]`, so the hold of the mass over a step (§10.2) does not use up the tolerance. | L2-AER-DYN-630 |
| C-5 | Rotation during translation | Zero fuel; gravity-free check configuration and vacuum-equivalent; level attitude; initial horizontal velocity `V_0` of magnitude at most `[P-SYS-230]`, zero vertical velocity; yaw rate `r_0` of magnitude at most `[P-SYS-270]`, `p = q_r = 0` | Option T1 (retained, D64): `v_N, v_E` constant; `u, v` turn at `−r_0`. Option T2: `u, v` constant; the track minus the heading is constant and the horizontal speed stays `V_0`. Under both: the vertical velocity stays zero, and `r`, the pitch angle and the roll angle stay at their initial values. The option that applies is the one recorded in the **kinematic terms** list (§4.5). | At each step over `[P-DYN-270]`: the horizontal velocity error divided by `V_0` at most `[P-DYN-250]`; the yaw rate error divided by `|r_0|` at most `[P-DYN-250]`; the pitch and roll angles within `[P-DYN-250]` rad of zero (G2-F01, G2-F14) | L2-AER-DYN-640 |
| C-6 | Unit attitude quaternion | Checks C-3 and C-5, and the reference mission SC-110 | `‖q‖ = 1` | `|‖q‖ − 1|` at most `[P-DYN-230]` at each step | L2-AER-DYN-060 |
| C-7 | Standard atmosphere | The density function alone | The density of the standard computed independently from its defining equations (the layer table of §5.3 and the hydrostatic equation) at the geopotential altitude equal to `h` (DD-090), at the base altitude and the midpoint of each of the seven layers and at 84 852 m; the base values agree with the published table of the standard read by geopotential altitude, not by geometric altitude (G2-F07) | Relative error at most `[P-DYN-260]` | L2-AER-DYN-150 |
| C-8 | Fuel-mass integral | The reference mission SC-110, which now includes a rest on the ground (leg 7a) with zero flow (FU check) | Initial fuel mass minus an independent summation of the FU fuel mass flow of each simulation step times `Δt` (per-step data, G2-F22) | At most `[P-FU-060]` | FU (L1-AER-190; C2) |
| C-9 | Rest on the ground and liftoff | (a) Start on the ground; effectors off; still air, and a steady wind of `[P-SYS-430]` with a gust event of amplitude `[P-SYS-560]` (the strongest wind of the envelope). (b) Start on the ground; still air; vacuum-equivalent; DYN driven with a prescribed control force along `−z_B` that rises linearly through the weight, and a prescribed constant mass, in place of the EF and FU outputs | (a) Static equilibrium: at each step the integrated state equals the rest state of step 0; the gear is extended and the vehicle on the ground; the vehicle acceleration is zero; the sensed acceleration is `(0, 0, −g)` in B; the ground reaction is `−(m·g^L + D^L)`, with `D^L` the drag of the wind on the vehicle at rest. (b) The liftoff step is the first step at which the prescribed upward force exceeds `m·g`; from it the vertical motion is the closed form of a constant mass under the prescribed force and gravity | (a) Exact for the held state; the sensed acceleration magnitude equals `[P-DYN-010]` and the ground reaction the closed form, to floating-point rounding. (b) The liftoff step exactly; the altitude and the vertical speed after it within the relative error `[P-DYN-200]` | L2-AER-DYN-570, -580, -590 |

**Notes on the configurations.**

- **C-2 (G2-F02).** The settled vertical speed differs from `v_exp(h)` by the neglected higher-order terms, which grow with altitude. With the database values (dry mass 1000 kg, `[P-DYN-100]` = 5 m²) and an exact integration of the vertical equation, the residual in the checked band (1 500 m down to the contact step, after a release at rest at 3 000 m) is at most 3.1·10⁻⁴, about a third of `[P-DYN-210]`; the release from rest has settled by 1 500 m (C1 computation with a fourth-order integration at 0.002 s, recorded in `work/C1/rework_G2_D69.md`). A release higher than 3 000 m or a band reaching higher than 1 500 m can exceed the tolerance (the residual reaches `[P-DYN-210]` near 5.2 km, G2; a release at rest at 3 000 m checked from 2 000 m gives 4.2·10⁻³, because the fall has not settled). The vehicle starts with the horizontal velocity of the wind, so the air-relative velocity is vertical and the wind case has the same expected vertical speed and residual as still air, while a drag computed on the ground velocity would fail both parts of the check. A release at rest relative to the ground in a wind of `[P-SYS-430]` would still be 1.7·10⁻² from the wind speed horizontally at 1 500 m, which is why the configuration does not use it. If the vehicle parameter set changes the dry mass or the drag area, the procedure recomputes the residual. The band lies in layer 0 of the atmosphere, so the closed form does not cross a layer boundary.
- **C-3, C-5 (G2-F01, D72).** Without gravity the vehicle does not fall, so no contact step ends the check before `[P-DYN-270]`. The initial altitude is any altitude of the operating volume; with zero initial vertical velocity it does not change. The body-rate bound `[P-SYS-270]` is the largest heading rate of the envelope, so the integrator is exercised at the rates the vehicle can reach.
- **C-9.** The rest and the liftoff are exact consequences of the ground contact model (§9.6), so the check is an independent re-computation of the equilibrium and of the threshold, not a tolerance on an integration, apart from the motion after liftoff.

C-4 and C-8 together check the mass decrease end to end: FU integrates the flow (C-8), and DYN uses the mass it is given (C-4). The sensed-acceleration definition is checked inside C-1 (zero in free fall), by the prescribed-force case of L2-AER-DYN-300 (`g` in a hover) and by C-9 (`g` at rest on the ground).

**Input pedigree.** Section 12 gives the source and status of each parameter the model uses. **Sensitivity** of the key results to the uncertain parameters (drag area, gust rise time, mass properties, gear length) is a verification-planning task (Phase 5, V1).

## 12. Parameters and input pedigree

| Parameter | Name | Unit | Value | Status | Source and pedigree |
| --- | --- | --- | --- | --- | --- |
| P-DYN-010 | Gravitational acceleration | m/s² | 9.806 65 | Set (D64) | Standard gravity (CGPM 1901); L1-AER-060. Zero only in the gravity-free check configuration (§5.2) |
| P-DYN-020 | Body overall length | m | 12.0 | TBR (TT-740, 2026-11-30) | C1 proposal for the provisional "Tic Tac" shape (L0-CON-140), accepted (D64) |
| P-DYN-030 | Body diameter | m | 4.0 | TBR (TT-740, 2026-11-30) | C1 proposal (length-to-diameter ratio 3), accepted (D64) |
| P-DYN-040 | Landing gear length | m | 1.4 | TBR (TT-830) | Owner (D69): a little less than the hover height; rest altitude 3.4 m (§2.5) |
| P-DYN-050 | Landing gear transit time | s | 3.0 | TBR (TT-850, B3) | B3 proposal (D73); L1-AER-910 |
| P-DYN-100 | Drag area | m² | 5.0 | TBR (TT-750) | C1 estimate: a round-nosed body of these dimensions has C_D ≈ 0.3 on its frontal area of 12.6 m² (3.8 m²) and more in cross-flow (Hoerner, *Fluid-Dynamic Drag*, 1965); kept by the owner with D46 revised (D72); confirmed at I1 with the authority budgets |
| P-DYN-200 | Free-fall check tolerance | 1 | 1·10⁻⁴ | TBR (TT-760) | C1 proposal (D64); checks C-1, C-9 |
| P-DYN-210 | Terminal vertical speed check tolerance | 1 | 1·10⁻³ | TBR (TT-760) | C1 proposal (D64); check C-2 |
| P-DYN-220 | Torque-free rotation check tolerance | 1 | 1·10⁻⁴ | TBR (TT-760) | C1 proposal (D64); check C-3 |
| P-DYN-230 | Quaternion norm tolerance | 1 | 1·10⁻⁶ | TBR (TT-760) | C1 proposal (D64); check C-6 |
| P-DYN-240 | Variable-mass check tolerance | 1 | 1·10⁻⁴ | TBR (TT-760) | C1 proposal (D64); check C-4 |
| P-DYN-250 | Rotation-during-translation check tolerance | 1 | 1·10⁻⁴ | TBR (TT-760) | C1 proposal (D64); check C-5 |
| P-DYN-260 | Atmosphere density tolerance | 1 | 1·10⁻⁴ | TBR (TT-760) | C1 proposal (D64); check C-7 (the table has five significant figures) |
| P-DYN-270 | Accuracy horizon | s | 600 | TBR (TT-760) | Owner (D72, G2-F01): the horizon of checks C-3 and C-5 in the gravity-free check configuration; no check runs for a long hold |
| P-DYN-400 | Crew station position | m | (4.0, 0.0, −1.0) | TBR (TT-140) | C1 proposal (D64): forward of the CG, inside the capsule, above the axis |
| P-SYS-200 | Maximum operating altitude | m | 45 720 | TBR (TT-010) | Owner (D67); inside layer 3 of the atmosphere model (§5.3) |
| P-SYS-230 | Maximum horizontal speed | m/s | 154.333 | Set (D66) | Owner (D66); a ground speed (D72); C-5 bound and the drag budget (§5.5) |
| P-SYS-270 | Maximum heading rate | rad/s | 0.062 832 | TBR (TT-010) | Owner (D67); C-3 and C-5 rate bound |
| P-SYS-300 | Simulation step | s | 0.01 | TBR (TT-070) | B1 (L1-AER-670) |
| P-SYS-430, -560 | Steady wind, gust amplitude | m/s | 51.444, 25.722 | TBR (TT-030) | Owner (D51); C-2, C-9 |
| P-SYS-570 | Minimum gust rise time | s | 2.0 | TBR (TT-650) | C1 proposal accepted (D64), §5.4 |
| P-SYS-580 | Maximum wind speed at liftoff | m/s | 38.583 | TBR (TT-860, B3) | B3 proposal (D73, B3-2); pedigree only: DYN does not check it (§5.4) |
| P-SYS-500, -510 | Landing envelope | m/s | 3.458, 0.5 | TBR (TT-090) | Owner (D53) |
| P-AF-210 | Hover height above the ground | m | 1.524 | Set (D70) | Owner (D70); pedigree only: the gear clearance at the hover height (§2.5) |
| P-FU-010, P-FU-030 | Fuel capacity, dry mass | kg | 500, 1000 | TBR (TT-110, TT-120) | C2 (D65) |
| P-FU-070, P-FU-080 | Principal moments of inertia (dry, full fuel) | kg·m² | — | TBD (TT-770) | Derived in §6 (C2, I1) |

## 13. Open items

| Item | Where | Owner | Closure |
| --- | --- | --- | --- |
| Body dimensions with the provisional shape (L0-CON-140 TBR; TT-740) | §2.1, §12 | Martin | 2026-11-30 |
| Gear length `[P-DYN-040]` (TT-830) and transit time `[P-DYN-050]` (TT-850) | §2.5, §9.1, §12 | Martin | G2 |
| Gear geometry, ground start, crash adjustment and ground reaction (DD-C1-07 to -11, proposed) | §2.5, §3.4, §5.3, §9, §10.3 | Martin | G2 (delta inspection) |
| Ground-start altitude item in ICD-AER-TST (IN-C1-21) | §10.3 | I1 | I1 |
| `[P-SYS-570]` confirmed against the FC budgets (TT-650) | §5.4 | C4 | I1 |
| Content of §6 and §7 (TT-780) | §6, §7 | C2, C3 | I1 |
| Parameter values P-DYN-100 to -400, TBR (TT-750, TT-760, TT-140) | §12 | Martin | G2 |

## 14. Trace

| Section | L1 records | L2 DYN records |
| --- | --- | --- |
| §2 Vehicle geometry | L1-AER-220, -240, -250, -900 | L2-AER-DYN-220, -230, -240, -250, -260 |
| §3 Vehicle state | L1-AER-010, -430, -440, -640 | L2-AER-DYN-020, -070, -290, -310, -320, -330, -340, -350, -360 |
| §4 Equations of motion | L1-AER-010, -020, -180, -220 | L2-AER-DYN-010, -030, -040, -050, -060 |
| §5.1 Total force and moment | L1-AER-030, -040, -050, -920 | L2-AER-DYN-100, -110, -160, -170, -180, -580 |
| §5.2 Gravity model | L1-AER-060 | L2-AER-DYN-120 |
| §5.3 Atmosphere model | L1-AER-070 | L2-AER-DYN-150 |
| §5.4 Wind model | L1-AER-070, -670 | L2-AER-DYN-140, -410 |
| §5.5 Drag model | L1-AER-020, -030, -070 | L2-AER-DYN-130, -190 |
| §6 Mass-properties model | L1-AER-180, -210, -220 | L2-AER-DYN-200, -210 (and FU) |
| §7 Effector and fuel models | L1-AER-050, -160, -270, -720 | L2-AER-DYN-180, -370 (and EF, FU) |
| §8 Sensed acceleration | L1-AER-290, -640, -920 | L2-AER-DYN-300 |
| §9.1 Landing gear model | L1-AER-900, -910, -920, -430 | L2-AER-DYN-260, -270, -280, -290, -360 |
| §9.2 to §9.9 Ground contact model | L1-AER-260, -270, -280, -290, -920, -950 | L2-AER-DYN-500 to -590, -450 |
| §10 Simulation step | L1-AER-660, -670, -690, -950 | L2-AER-DYN-400, -410, -420, -430, -440, -450, -460, -470 |
| §11 Credibility checks | L1-AER-010, -020, -060, -070, -180, -920 | L2-AER-DYN-060, -140, -150, -570 to -590, -600 to -640 |
| Whole document | L1-AER-720 | L2-AER-DYN-700 |
