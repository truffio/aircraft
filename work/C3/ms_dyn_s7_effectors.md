# MS-DYN §7.1 — Effector model (C3 content, for merge at I1)

**Status:** Draft (task C3), 2026-11-05. Proposed content for the C3 slot of `specs/MS-DYN.md` §7.1, which C1 owns. To be merged at I1 under the heading below, replacing the "What DYN needs from EF" list and the content-slot note. Protected design material, like the rest of MS-DYN.
**Serves:** L1-AER-080, -090, -100, -110, -120 to -140, -160, -200, -710, -720; L2-AER-EF-010 to -430; IN-C1-10 to -12, IN-C2-11, IN-C2-20 to -23.
**Notation:** as MS-DYN §1. Simulation step `k`, `Δt = [P-SYS-300]`. Vectors in the body frame B unless stated. `×` is the cross product.

---

### 7.1 Effector model

This section is the **effector model** of MS-DYN. **Content owner: C3 (EF).** It states what each effector is, how its output follows its command, when it is zero, and how the outputs make the control force `F_c^B` and the control moment `M_c^B` that DYN (§4, §5.1) and FU (§7.2) use. Nothing else defines an effector: there is no physical mechanism, no energy conversion and no electrical quantity (L0-CON-080, L0-CON-160, L1-AER-100).

#### 7.1.1 The effector set

The effector set has `n` effectors, `i = 1 … n`. `n` is the number of entries in each of the lists `[P-EF-100]` to `[P-EF-130]`, which have the same length. Each effector is a **force emitter** (DD-150): it pushes along a fixed unit direction through a fixed point of the body.

| Symbol | Meaning | Parameter | Kind (L1-AER-100) | Unit |
| --- | --- | --- | --- | --- |
| `d_i` | Direction of action, a unit vector in B; a positive output acts along `+d_i` (CV-330) | `[P-EF-100]`, entry `i` | Direction of action | 1 |
| `r_i` | Point of application, a body-frame position measured from the centre of gravity `O_B` | `[P-EF-110]`, entry `i` | Control effectiveness | m |
| `U_i` | Largest output: the maximum force magnitude of the effector (L0-CON-300) | `[P-EF-120]`, entry `i` | Output limits | N |
| `L_i` | Smallest output, with `−U_i ≤ L_i ≤ 0`: `L_i = −U_i` for an effector that pushes both ways, `L_i = 0` for one that pushes one way only | `[P-EF-130]`, entry `i` | Output limits | N |
| `τ` | Time constant of the command response, common to the set | `[P-EF-020]` | Command response | s |

Conditions on the values (checked by inspection of the parameter set, IN-EF-010): `|d_i| = 1` to floating-point rounding; `U_i > 0`; `−U_i ≤ L_i ≤ 0`, so that zero is a valid output; `τ > 0`. `d_i` and `r_i` are constants of the run (L1-AER-090, L2-AER-EF-020). The centre of gravity stays at `O_B` at every fuel state (L1-AER-210), so `r_i` is also the constant moment arm.

The **consumption parameters** are not effector parameters here: the fuel use is charged on the resultant control force and moment with the coefficients `[P-FU-040]` and `[P-FU-050]`, common to the set (§7.2, DD-110, L2-AER-FU-060).

#### 7.1.2 Control effectiveness

The **control effectiveness** of effector `i` is the control force and control moment about the centre of gravity per newton of effector output:

```
b_i = ( d_i ,  r_i × d_i )          (6 components: force N/N, moment N·m/N)
B   = [ b_1  b_2  …  b_n ]          (6 × n effectiveness matrix, constant over the run)
```

The effector command `c_i` and the effector output `u_i` are both forces in N along `d_i`, so the output per unit command in steady state is one (§7.1.4).

#### 7.1.3 Inputs of a step

| Input of step `k` | Symbol | Source | Definition |
| --- | --- | --- | --- |
| Effector command of effector `i` | `c_i(k)` | Flight control, across the vehicle-model boundary (L2-AER-EF-400) | The command flight control issues for the control frame that contains step `k` (L2-AER-EF-150). Commands are held for the frame (FUNCTIONAL_ANALYSIS §4.2). |
| Effector activation state | `s(k) ∈ {on, off}` | Flight control, with the effector commands (DD-180) | As for the commands. Before the first effector commands of a run, `s = off`. |
| Fuel availability | `φ(k) ∈ {available, not available}` | FU (L2-AER-FU-200) | Available when the remaining fuel mass at the start of step `k` is above zero (DD-130). |

No other quantity enters the effector model: in particular no element of the vehicle state, no wind, no air density, no mass and no other effector's command (L2-AER-EF-040). This is what keeps the effector model free of cross-axis and motion-dependent terms (L1-AER-020; the kinematic terms list §4.5 is unchanged by it).

#### 7.1.4 Command response

For each effector `i`, at each step `k`:

```
ĉ_i(k) = min( max( c_i(k), L_i ), U_i )                     clipped command

u_i(k) = 0                                                  if s(k) = off or φ(k) = not available
u_i(k) = u_i(k−1) + β · ( ĉ_i(k) − u_i(k−1) )               otherwise

β = 1 − exp( −Δt / τ ),        u_i(−1) = 0
```

where `u_i(k−1)` is the output of the previous step, or zero if the previous step had `s = off` or `φ = not available` (the lag restarts from zero; DD-160, DD-180).

Properties (each is used by a requirement):

1. **Exact first-order lag.** For a command held over the steps, the recursion is the exact sampled solution of `τ·du/dt + u = ĉ` at the step ends. `u_i(k)` is the value at the end of step `k`, and it is the output held over step `k` (§10.2, DD-100), so the output of a step already responds to the command of that step. The first change of output after a new command is therefore at the step at which the command applies (L2-AER-EF-150), and the control-loop latency to the first change is at most one control frame `[P-SYS-310]` (DD-020).
2. **Within the output limits.** `u_i(k)` is a convex combination of `u_i(k−1)` and `ĉ_i(k)`, both in `[L_i, U_i]` (zero is in the interval). By induction from `u_i(−1) = 0`, each output stays within its limits whatever the command (L1-AER-110, L2-AER-EF-110). A command beyond a limit is nominal: the output settles on the limit.
3. **No overshoot, unit steady-state gain.** For a step of the clipped command from a settled output `u_0` to `ĉ` applying at step `k_0`, the remaining difference after the output of step `k_0 + m` is

   ```
   | u_i(k_0 + m) − ĉ |  =  (1 − β)^(m+1) · | ĉ − u_0 |
   ```

   It decreases monotonically to zero: a held command is produced exactly (L1-AER-360 through L2-AER-EF-100).
4. **Response time.** The output is within the band `[P-EF-030]·|ĉ − u_0|` of `ĉ` from the first `m` with `(1 − β)^(m+1) ≤ [P-EF-030]`, that is after `m·Δt`, measured by CV-860 from the step at which the new command applies. With the proposed values `Δt = 0.01 s`, `τ = 0.015 s` (`1 − β = 0.513`) and `[P-EF-030] = 0.05`: `m = 4`, a response time of 0.04 s, inside `[P-EF-010] = 0.06 s` (L2-AER-EF-340). The latency budget closes: `[P-SYS-310] + [P-EF-010] = 0.02 + 0.06 = 0.08 s ≤ [P-SYS-480] = 0.1 s` (FUNCTIONAL_ANALYSIS §7.5). If `[P-SYS-300]` changes, `β` changes with it and the response time is rechecked.
5. **Zero output at once.** While fuel is not available or the effectors are off, each output is exactly zero, from the first such step and without passing through the lag (L1-AER-200, L2-AER-EF-200, -210). In a step that starts with fuel available the output follows the recursion for the whole step, and FU limits the fuel used in that step to the fuel left (DD-130, IN-C2-20).
6. **Step zero.** Before the first effector commands of a run the activation state is off and each output is zero (IN-C1-12). If the commands of the first control frame, at step 0, set the effectors on, `u_i(0) = β·ĉ_i(0)`; under the ground start of D69 they are off, so `u_i(0) = 0`. These are the outputs the step-0 acceleration quantities of §3.3 use (DD-080).

#### 7.1.5 Control force and control moment

At each step `k`, EF computes once:

```
F_c^B(k) = Σ_i  u_i(k) · d_i
M_c^B(k) = Σ_i  u_i(k) · ( r_i × d_i )          (about O_B, the centre of gravity)

or   w(k) = ( F_c^B(k), M_c^B(k) ) = B · u(k)
```

- This is the whole of the control force and control moment: no bias, no interaction term, no other source (L1-AER-080, L2-AER-EF-120; §5.1).
- **One computation, two users (DD-190).** EF gives `F_c^B(k)` and `M_c^B(k)` to DYN (interface I-02; the equations of motion §4.2, §4.3) and the same values, with the outputs `u_i(k)`, to FU (interface I-01; the consumption relationships of §7.2). The fuel used and the motion therefore come from the same control force and moment (IN-C2-11, L2-AER-EF-130, -140).
- One value per step, held over the step from `t_k` to `t_{k+1}` (§10.2, DD-100).
- With `s = off` or `φ = not available`, `w(k) = 0`, so the consumption rate of §7.2 is zero: no fuel is used with the effectors off on the ground or after exhaustion (D68, D69).

#### 7.1.6 Achievable set and authority

With fuel available and the effectors on, the set of control force and moment pairs that the effector set can hold is

```
A = { B·u  :  L_i ≤ u_i ≤ U_i  for each i }
```

a convex polytope (a zonotope) in the six-dimensional force-and-moment space. It does not depend on the mass, the fuel state or the vehicle state. The authority requirements are containment conditions on `A`:

| Requirement | Condition on `A` | Check (independent, from the parameter database) |
| --- | --- | --- |
| L2-AER-EF-300 (L1-AER-120) | `(0, 0, −[P-SYS-400], 0, 0, 0) ∈ A` | Linear-programming feasibility: find `u` within limits with `B·u` equal to the wrench |
| L2-AER-EF-310 (L1-AER-130) | `±[P-SYS-410]` along `x_B` and `y_B`, `+[P-SYS-410]` along `z_B`, other components zero, each in `A` | As above, five cases |
| L2-AER-EF-320 (L1-AER-140) | `±[P-SYS-420]` about each body axis, other components zero, each in `A` | As above, six cases |
| L2-AER-EF-330 (L1-AER-310 to -350, -380, -460) | The authority box `X, Y ∈ [−P410, P410]`, `Z ∈ [−P400, P410]`, `M_x, M_y, M_z ∈ [−P420, P420]` is contained in `A` (DD-170) | Feasibility at each of the 64 corners of the box; `A` is convex, so the box is inside it |

Because each authority is a pure or a box-shaped demand, flight control can allocate each axis demand with the other components at zero and saturate each axis on its own (L1-AER-020 rationale, L1-AER-380). How it allocates, and its priority rule beyond the box, are FC's (FC1).

**Authority budgets (FUNCTIONAL_ANALYSIS §7.1, current database, sea-level density 1.225 kg/m³, isotropic drag `D(V) = ½·ρ·[P-DYN-100]·V²` of §5.5):**

| Item | Budget line | Value |
| --- | --- | --- |
| Maximum vehicle mass `m_max = [P-FU-030] + [P-FU-010]` | — | 1500 kg |
| Weight plus manoeuvre, `m_max·([P-DYN-010] + [P-SYS-440])` | P-SYS-400 | 36.77 kN |
| Drag in the fastest climb alone, `D([P-SYS-240])` | P-SYS-400 (FA §7.1 as written) | 2.85 kN → **39.62 kN** (G2-F04 verified) |
| Largest horizontal airspeed `V_h = [P-SYS-230] + [P-SYS-430] + [P-SYS-560]` (P-SYS-230 is a ground speed, D72) | — | 231.50 m/s |
| Vertical drag of a climb at `[P-SYS-240]` at `V_h` (shared magnitude, `½ρS·|v_a|·v_z`, G2-F06) | P-SYS-400 (combined case) | 21.80 kN → **58.57 kN** |
| Manoeuvre `m_max·[P-SYS-440]` | P-SYS-410 | 22.06 kN |
| Horizontal drag at `V_h`, level, `D(V_h)` | P-SYS-410 (FA §7.1) | 164.12 kN → **186.19 kN** (G2-F04 verified) |
| Horizontal drag at `V_h` in the fastest climb | P-SYS-410 (combined case) | 165.54 kN → **187.61 kN** |
| Downward need: fastest descent at `V_h`, drag up minus weight plus manoeuvre | within P-SYS-410 | 29.15 kN |
| Largest moment of inertia at full fuel, uniform capsule (§6 reference derivation, `[P-FU-080] = [P-FU-070]·[P-FU-010]/[P-FU-030]`) | P-SYS-420 | 15 975 kg·m² (`I_yy = I_zz`; `I_xx` = 2850) |
| `J_max·[P-SYS-270]` per second of onset time | P-SYS-420 | 1003.7 N·m/s; 2007.5 N·m for 0.5 s |
| Drag moment and moment to hold pitch and roll against it | P-SYS-420 | 0 (DD-050) |
| **Proposed (TBR)** | | `[P-SYS-400]` = 60 kN, `[P-SYS-410]` = 190 kN, `[P-SYS-420]` = 2000 N·m (reaches `[P-SYS-270]` in 0.50 s at `J_max`) |

The upward authority is smaller than the other five, as D46 revised by D72 allows. Oversizing an authority costs no fuel: the consumption is charged on the resultant actually produced (DD-110).

#### 7.1.7 Reference layout (DD-200, TBR)

The layout is a design decision, not a requirement. This reference layout meets L2-AER-EF-300 to -330 with the proposed values and is the proposed content of `[P-EF-100]` to `[P-EF-130]`. Six effectors in three pairs, each pair parallel to one body axis and offset across the centre of gravity, each pushing both ways:

| `i` | `d_i` | `r_i` (m) | `U_i` (N) | `L_i` (N) | Pair gives |
| --- | --- | --- | --- | --- | --- |
| 1 | (1, 0, 0) | (0, 1.5, 0) | 100 000 | −100 000 | force along `x_B`; moment about `z_B` |
| 2 | (1, 0, 0) | (0, −1.5, 0) | 100 000 | −100 000 | |
| 3 | (0, 1, 0) | (0, 0, 1.5) | 100 000 | −100 000 | force along `y_B`; moment about `x_B` |
| 4 | (0, 1, 0) | (0, 0, −1.5) | 100 000 | −100 000 | |
| 5 | (0, 0, 1) | (4.0, 0, 0) | 100 000 | −100 000 | force along `z_B`; moment about `y_B` |
| 6 | (0, 0, 1) | (−4.0, 0, 0) | 100 000 | −100 000 | |

Each point lies inside the capsule of §2.1 (radius 2 m, half-length 6 m). Each pair acts on one force axis and one moment axis only: for the pair along `x_B`, `X = u_1 + u_2` and `M_z = −1.5·(u_1 − u_2)`, so the pair can hold any `(X, M_z)` with `|X| + |M_z|/1.5 ≤ 200 000`. Results (independent linear programming, C3 check):

| Check | Result |
| --- | --- |
| Largest pure force, each of the six directions | 200 kN (≥ `[P-SYS-410]` = 190 kN; ≥ `[P-SYS-400]` = 60 kN upward) |
| Largest pure moment about `x_B`, `y_B`, `z_B` | 300, 800, 300 kN·m (≥ 2000 N·m) |
| Authority box of L2-AER-EF-330, 64 corners | Each feasible; the box can be scaled by 1.045 before a corner fails (the `x_B` and `y_B` pairs at 190 kN plus 2000 N·m) |

#### 7.1.8 Independent checks of the effector model

These complete the credibility checks of §11 for the effector model (METHODOLOGY §10.3). They compare the model with a computation made outside it, from the recorded inputs and the parameter set.

| ID | Check | Independent solution | Tolerance | Requirement |
| --- | --- | --- | --- | --- |
| E-1 | Command response | The recursion of §7.1.4 from the recorded commands, activation state and fuel availability of each step | Floating-point rounding | L2-AER-EF-100 |
| E-2 | Control force and moment | `B·u(k)` from the recorded outputs and `[P-EF-100]`, `[P-EF-110]` | Floating-point rounding | L2-AER-EF-120 |
| E-3 | Output limits | `L_i ≤ u_i(k) ≤ U_i` at each sample, with commands beyond each limit | Exact | L2-AER-EF-110 |
| E-4 | Authority | Linear-programming feasibility of the wrenches of §7.1.6 | Floating-point rounding | L2-AER-EF-300 to -330 |
| E-5 | Response time | Property 4 of §7.1.4 | `[P-EF-010]` | L2-AER-EF-340 |

The credibility checks C-1 to C-5 run with zero fuel or with the effectors off; in both cases the effector model gives `w(k) = 0` exactly (property 5), so they need no change for EF.

#### 7.1.9 Open items (effector model)

| Item | Owner | Closure |
| --- | --- | --- |
| Command response form: first-order lag (DD-160, C3-Q01) | Martin | G2 |
| Values `[P-EF-010]`, `[P-EF-020]`, `[P-EF-030]`, `[P-EF-100]` to `[P-EF-130]`, TBR | Martin | G2 (I1) |
| `[P-SYS-420]` re-derived when `[P-FU-070]`, `[P-FU-080]` and the body dimensions are set (TT-770, TT-740) | C2, Martin | I1, 2026-11-30 |
| Effector activation state and who sets it (DD-180; D69, B3) | Martin, C4, C5 | After B3 approval |
