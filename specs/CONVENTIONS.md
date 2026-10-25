# Aeronef — Conventions

**Status:** Proposed (Phase 1, task A3). Every convention is Proposed until the project owner fixes it at Gate G0.
**Date:** 2026-10-24
**Owner:** Martin
**Classification:** Protected design material. Not for release to the Reverse-Engineering Effort (REE).
**Related:** [GLOSSARY.md](GLOSSARY.md), [METHODOLOGY.md](../METHODOLOGY.md) §2 and §8.4 rule 12, [AIRCRAFT_REQUIREMENTS_PLAN.md](../AIRCRAFT_REQUIREMENTS_PLAN.md) §9 (D7, Q2–Q5).

## 0. Purpose, scope and how to cite

This document fixes the coordinate frames, sign conventions, angle definitions, units and time base that every Aeronef requirement, the model specification (MS-DYN), the interface control documents (ICDs), the parameter database and the operational data use. It defines quantities. It does not specify how any function computes, controls or displays them.

- **Basis.** The frames and signs are consistent with the practice of ANSI/AIAA R-004-1992, *Recommended Practice for Atmospheric and Space Flight Vehicle Coordinate Systems*, as described in public sources (no copy of the text is held; checked against public sources, decision D36): a right-handed body frame with x forward, y right and z down, a local-level north-east-down frame, and the yaw-pitch-roll (3-2-1) Euler sequence. Mass-properties terms are compatible with SAWE STD A-6. Where this document goes beyond R-004 (crew-facing units, the time base, VOR definitions, expression rules), it says so.
- **Citing.** A requirement cites a convention by its ID, for example "heading (CONVENTIONS CV-530)". Requirements use the defined names in this document and the [glossary](GLOSSARY.md), never a synonym.
- **IDs.** `CV-nnn`, grouped by section in blocks of one hundred, numbered in steps of 10. An ID is never reused. A deleted convention keeps its ID with status Deleted.
- **Status values.** Proposed → Fixed (at G0) → Changed (by an approved change request) or Deleted. Items that need an owner answer carry **TBR (Qn)** or a G0 decision reference **(G0-nn)**. Section 11 lists the G0 decisions. Items the owner has decided are **Fixed**, with the plan decision (Dnn, plan §9) that fixes them.
- **Section numbers and ID blocks.** Section n+1 holds the block `CV-n00`–`CV-n90` (Section 1 holds CV-0xx, Section 10 holds CV-9xx).
- **Numbers.** Numbers in this document are exact definitions (for example 1 ft = 0.3048 m, ranges of angles). Every other number is a parameter `P-<SUB>-<NNN>`, proposed in `work/A3/param_proposals.md` and held in `parameters/PARAMETERS.yaml`.
- **Scope.** The Aeronef element (AER) and the Aeronef side of its interfaces. The STP may use other frames internally, for example for graphics, provided it converts at its boundary as the ICD-AER-STP defines.

## 1. General conventions (CV-0xx)

### CV-010 — Applicability

Each Aeronef requirement, the MS-DYN, each Aeronef ICD, the parameter database and each operational data signal shall use the conventions in this document. A departure is allowed only through a change request against this document.
**Status:** Proposed.

### CV-020 — Right-handed frames

Every coordinate frame is orthonormal and right-handed: x × y = z.
**Status:** Proposed.

### CV-030 — Notation

| Notation | Meaning |
| --- | --- |
| `L`, `V`, `B` | Local reference frame (CV-120), vehicle-carried local frame (CV-150), body frame (CV-170) |
| `x_B`, `y_B`, `z_B` | Unit axes of frame B (likewise for L and V) |
| `v^F` | Components of vector `v` expressed in frame F |
| `C_BL` | Direction cosine matrix that maps components in L to components in B: `v^B = C_BL · v^L` |
| `ω_BL` | Angular velocity of B relative to L |
| `wrap360(a)`, `wrap180(a)` | Angle wrapping functions (CV-920) |
| `t`, `k`, `Δt` | Simulation time, step index, simulation step (CV-8xx) |

Symbols for each quantity are given with its definition. Requirements use the defined names; symbols are for the MS-DYN, the ICDs and the verification procedures.
**Status:** Proposed.

### CV-040 — Rotation sense

Rotations between frames are passive: a rotation re-expresses a fixed vector in a rotated frame. A positive rotation about an axis follows the right-hand rule about that axis.
**Status:** Proposed.

## 2. Coordinate frames (CV-1xx)

### CV-110 — World model: flat, non-rotating Earth

The Aeronef world is flat by definition. The ground reference is an infinite horizontal plane, the **datum plane** (CV-420). The world does not rotate. Gravity is uniform in magnitude and direction everywhere (direction per CV-180; magnitude is the MS-DYN parameter `P-DYN-010`).

Rationale: the Aeronef is fictional, so a flat world is a definition, not an approximation, and it carries no approximation error to verify. Spherical or ellipsoidal (WGS-84) models add geodetic conversions, convergence of meridians and Earth-rate terms that no objective needs. The alternative is recorded in G0-07.
**Status:** Fixed (G0-07: D35).

### CV-120 — Local reference frame L: axes

The local reference frame L is fixed to the datum plane:

- `x_L` points to **north** (CV-510), horizontal;
- `y_L` points to **east**, horizontal;
- `z_L` points **down**, normal to the datum plane, in the direction of gravity.

This is the north-east-down (NED) local-level frame of R-004. The choice of NED over east-north-up (ENU) is decision G0-01; the trade is in Section 2.1.
**Status:** Fixed (G0-01: D21).

### CV-130 — Local reference frame L: origin

The origin `O_L` is a fixed point on the datum plane. Each world definition used by a scenario (vehicle initial position, VOR station positions) places objects relative to `O_L`. The location of `O_L` has no physical meaning; it is a reference point only.
**Status:** Proposed.

### CV-140 — Local reference frame L treated as inertial

Frame L is an inertial frame for the equations of motion (consequence of CV-110). All velocities, accelerations and angular velocities called "inertial" in the MS-DYN are relative to L.
**Status:** Fixed (G0-07: D35).

### CV-150 — Vehicle-carried local frame V

Frame V has its origin at the body origin `O_B` (CV-160) and axes parallel to L at all times (north, east, down). It is used to express the vehicle attitude (CV-210) and the vehicle velocity in north, east and down components. On the flat world of CV-110, `C_VL` is the identity matrix.
**Status:** Proposed.

### CV-160 — Body frame B: origin

The body origin `O_B` is the vehicle centre of gravity (CG). Because the CG is fixed in the body (constraint from AIRCRAFT_CHARACTERISTICS §4), `O_B` is a fixed point of the body. If a later version lets the CG move, `O_B` stays at the nominal CG, defined as a fixed body point, and the CG offset becomes a model quantity.

"Vehicle position", "altitude" and every motion quantity in Section 5 refer to `O_B` unless a requirement explicitly names another point.
**Status:** Fixed (G0-02: D35).

### CV-170 — Body frame B: axes

Frame B is fixed to the vehicle:

- `x_B`, the **longitudinal axis**, points from `O_B` toward the **nose**, along the vehicle's designated forward direction;
- `y_B`, the **lateral axis**, points to the right of the crew seated facing the nose (starboard);
- `z_B`, the **normal axis**, completes the right-handed frame and points "down" through the cockpit floor when the vehicle is at level attitude.

The exact body point the nose defines and the location of the cockpit relative to `O_B` belong to the MS-DYN geometry. With this definition, `x_B` is fixed by the designated forward direction, and `z_B` is fixed by the cockpit floor, which defines "up" for the crew.
**Status:** Fixed (G0-02: D35).

### CV-180 — Vertical direction and gravity

"Down" is `+z_L`, the direction of the gravitational acceleration. "Up" is `−z_L`. "Horizontal" means parallel to the datum plane (perpendicular to `z_L`). "Vertical" means parallel to `z_L`.
**Status:** Proposed.

### CV-190 — Frames not used in version 1

Wind axes, stability axes, Earth-centred inertial, Earth-centred Earth-fixed and geodetic frames are not used. The Aeronef has no aerodynamic lift and no control surfaces, so angle of attack and sideslip have no role in the forces. Drag is defined by the MS-DYN on the air-relative velocity (CV-470).
**Status:** Proposed.

### 2.1 Trade: NED versus ENU for frame L (decision G0-01)

| Criterion | NED (`x` north, `y` east, `z` down) | ENU (`x` east, `y` north, `z` up) |
| --- | --- | --- |
| Standard | The local-level frame of AIAA R-004 and of the flight-dynamics literature (Etkin, Stevens and Lewis) | Common in robotics (ROS REP-103), geodesy and some graphics tools; not the R-004 flight-vehicle frame |
| Pairing with the body frame | Pairs with the R-004 body frame (x forward, y right, z down): at zero Euler angles, B coincides with V, nose north, crew upright | Pairs naturally with a forward-left-up body frame; pairing with an R-004 body frame needs a fixed 180° rotation about x, a frequent source of sign errors |
| Heading and aviation angles | Yaw angle ψ equals heading measured clockwise from north, exactly as aviation and VOR radials use it | Yaw is measured counter-clockwise from east; heading = 90° − yaw, wrapped. Every heading, track and radial requirement needs this conversion |
| Altitude and vertical speed | Altitude is `−z`, vertical speed is `−v_D`: a sign flip | Altitude is `z`, vertical speed is `v_U`: no sign flip |
| Graphics and visualisation | The STP display needs a conversion (most 3-D engines are y-up or z-up) | Closer to z-up tools; still needs conversion for y-up engines |
| Reverse-engineering view | Telemetry using aviation-style angles is easier to relate to airliner-style manuals | Mixed conventions between telemetry and manuals |

**Recommendation: NED.** It is the convention R-004 calls for, it keeps the body and local frames aligned at zero attitude, and it makes heading, track and radials direct readings of standard angles. The one cost, the altitude sign flip, is contained by CV-430 and CV-490: requirements never use `z_L`; they use the defined quantities *altitude* and *vertical speed*, which are positive up. Display conversions are an STP concern at the ICD boundary.

## 3. Attitude and rotation (CV-2xx)

### CV-210 — Euler-angle sequence

The attitude of frame B relative to frame V is described by three Euler angles applied in the yaw-pitch-roll order (z-y-x, also called 3-2-1), starting from V:

1. rotate by the **yaw angle** ψ about `z_V`;
2. then rotate by the **pitch angle** θ about the resulting intermediate y axis;
3. then rotate by the **roll angle** φ about the resulting x axis, which is `x_B`.
**Status:** Fixed (G0-03: D22).

### CV-220 — Euler-angle names and signs

| Angle | Symbol | Positive sense |
| --- | --- | --- |
| Yaw angle | ψ | Nose to the right (clockwise seen from above) |
| Pitch angle | θ | Nose up |
| Roll angle | φ | Right side down (rotation about `x_B` by the right-hand rule) |

On the Aeronef the yaw angle is the **heading** (CV-530). Requirements use "heading" for ψ and "pitch angle" and "roll angle" for θ and φ. The Aeronef has no wings, so "bank angle" and "wings level" are not used.
**Status:** Proposed.

### CV-230 — Euler-angle ranges

| Angle | Range (degrees) | Range (radians) |
| --- | --- | --- |
| ψ (heading) | [0, 360) | [0, 2π) |
| θ (pitch) | [−90, +90] | [−π/2, +π/2] |
| φ (roll) | (−180, +180] | (−π, +π] |

Values outside these ranges are brought back with the wrapping functions of CV-920.
**Status:** Fixed (G0-04: D35).

### CV-240 — Direction cosine matrix

With `c` for cosine and `s` for sine:

```
        | cθ·cψ               cθ·sψ               −sθ    |
C_BV =  | sφ·sθ·cψ − cφ·sψ    sφ·sθ·sψ + cφ·cψ    sφ·cθ  |
        | cφ·sθ·cψ + sφ·sψ    cφ·sθ·sψ − sφ·cψ    cφ·cθ  |
```

Because `C_VL` is the identity (CV-150), `C_BL = C_BV`.
**Status:** Proposed.

### CV-250 — Attitude quaternion

The attitude may also be represented by a unit quaternion `q = (q0, q1, q2, q3)`:

- scalar first (`q0` is the scalar part), Hamilton product convention;
- `q` represents the passive rotation from L to B and gives:

```
        | q0²+q1²−q2²−q3²    2(q1q2+q0q3)       2(q1q3−q0q2)    |
C_BL =  | 2(q1q2−q0q3)       q0²−q1²+q2²−q3²    2(q2q3+q0q1)    |
        | 2(q1q3+q0q2)       2(q2q3−q0q1)       q0²−q1²−q2²+q3² |
```

- `q` and `−q` describe the same attitude; a reported quaternion has `q0 ≥ 0`.

**Proposed use (G0-03):** the quaternion is the authoritative attitude in the dynamics state and in the ICD state vector, and the Euler angles are derived from it by CV-260. Reason: the Aeronef's attitude is independent of its motion, so pitch angles at or near ±90° are reachable and the Euler angles become singular there; a quaternion has no singularity. Requirements still state attitude in Euler angles, because those are what the crew-facing and mode requirements need. How the model integrates attitude is an MS-DYN design matter.
**Status:** Fixed (G0-03: D22).

### CV-260 — Euler angles from an attitude, and the singular case

The Euler angles reported for an attitude are, with `Cij` the elements of `C_BL`:

- θ = −asin(C13);
- if |C13| < 1: ψ = wrap360(atan2(C12, C11)) and φ = atan2(C23, C33);
- if |C13| = 1 (pitch angle of exactly ±90°): φ = 0 and ψ = wrap360(atan2(−C21, C22)).

At and near ±90° of pitch angle, the heading and the roll angle are not separately meaningful. Requirements that use the heading or the roll angle state the pitch-angle range in which they apply (CV-580).
**Status:** Proposed.

### CV-270 — Level attitude

The vehicle is at **level attitude** when θ = 0 and φ = 0. Heading is not constrained by level attitude.
**Status:** Proposed.

### CV-280 — Angular velocity and body rates

The vehicle angular velocity is `ω_BL`, the angular velocity of B relative to L, expressed in B: `ω^B = (p, q, r)`.

| Rate | Symbol | Positive sense |
| --- | --- | --- |
| Roll rate | p | About `+x_B`: right side down |
| Pitch rate | q | About `+y_B`: nose up |
| Yaw rate | r | About `+z_B`: nose right |

The pitch-rate symbol `q` is distinct from the quaternion `q` (CV-250) by context; ICD signal names use distinct names.
**Status:** Proposed.

### CV-290 — Euler-angle rates are not body rates

The Euler-angle rates (dψ/dt, dθ/dt, dφ/dt) differ from the body rates (p, q, r) except at level attitude. **Heading rate** is dψ/dt. A requirement on a rate names which one it constrains.
**Status:** Proposed.

## 4. Forces, moments and mass properties (CV-3xx)

### CV-310 — Body forces

A force is resolved in B as `F^B = (X, Y, Z)`, positive along `+x_B`, `+y_B`, `+z_B` (forward, right, down). Requirements name the axis in words, for example "the force along the body x axis".
**Status:** Proposed.

### CV-320 — Body moments

A moment about `O_B` is resolved in B as `M^B = (L, M, N)`: rolling, pitching and yawing moment, positive about `+x_B`, `+y_B`, `+z_B` by the right-hand rule. Because `L` also names frame L, ICDs and requirements use "moment about the body x axis" (or `M_x`, `M_y`, `M_z`) in place of the single letters.
**Status:** Proposed.

### CV-330 — Effector direction

Each effector i has a fixed unit direction vector `d_i` in B (and, for a moment-producing effector, a fixed unit moment axis). A positive effector output acts along `+d_i`. Whether an effector can produce a negative output, and the layout of the `d_i`, are effector (EF) requirements or design decisions, not conventions.
**Status:** Proposed.

### CV-340 — Mass-properties reference

Mass, moments of inertia and products of inertia are given about `O_B` (the CG) and in the body axes of B. Fuel quantity is a mass, in kilograms (CV-720). Vehicle mass is dry mass plus remaining fuel mass.
**Status:** Proposed.

### CV-350 — Inertia tensor sign convention

Moments of inertia are `Ixx = ∫(y² + z²) dm`, `Iyy = ∫(x² + z²) dm`, `Izz = ∫(x² + y²) dm`. Products of inertia are defined with a positive integral, `Ixy = ∫ x·y dm`, `Ixz = ∫ x·z dm`, `Iyz = ∫ y·z dm`, and enter the inertia tensor with a negative sign:

```
      |  Ixx  −Ixy  −Ixz |
J  =  | −Ixy   Iyy  −Iyz |
      | −Ixz  −Iyz   Izz |
```

Parameter entries for products of inertia state this definition, because standards and tools differ on the sign.
**Status:** Fixed (G0-13: D35).

## 5. Position, altitude, distance and velocity (CV-4xx)

### CV-410 — Position

The **vehicle position** is the position of `O_B` in L: `(x_N, y_E, z_D)`, in metres. The **horizontal position** is `(x_N, y_E)`. Requirements state vertical position as altitude (CV-430), never as `z_D`.
**Status:** Proposed.

### CV-420 — Altitude datum

The altitude datum is the datum plane, `z_L = 0`, which contains `O_L`. It plays the role of mean sea level in the Aeronef world. The datum plane is also the ground: the world is flat with no terrain, and altitude zero is ground level (D8). Ground contact is an ideal landing when it is within the landing envelope and a crash otherwise (D37, L0-CON-290), so altitude is never negative in a run.
**Status:** Fixed (G0-08: D35).

### CV-430 — Altitude

**Altitude** `h` is the vertical distance of `O_B` above the datum plane, positive up: `h = −z_D`. It is a geometric altitude. Pressure altitude, barometric setting and atmospheric pressure are not used in version 1. If the MS-DYN makes air density depend on altitude, it uses this altitude.
**Status:** Fixed (G0-08: D35).

### CV-440 — Height

**Height** is the vertical distance of `O_B` above a stated reference point or surface other than the datum plane, positive up, for example "height above the VOR station". A requirement that uses "height" names its reference. "Height" alone, and "height above ground", are not used in version 1.
**Status:** Proposed.

### CV-450 — Distance

- **Horizontal distance** between two points is the distance between their projections on the datum plane.
- **Slant range** is the three-dimensional distance between two points.
- **Vertical separation** is the difference of their altitudes.

A requirement that uses a distance names which one.
**Status:** Proposed.

### CV-460 — Velocity and speed

The **vehicle velocity** `v` is the time derivative of the vehicle position in L (velocity relative to the ground). Its components are `v^V = (v_N, v_E, v_D)` (north, east, down) and `v^B = (u, v, w)` along the body axes, with `v^B = C_BL · v^V`. The **speed** of the vehicle, called **total speed** in requirements, is `|v|`.

The word "speed" alone is not used in requirements: they use *total speed*, *horizontal speed* (CV-480), *vertical speed* (CV-490) or *airspeed* (CV-470).
**Status:** Proposed.

### CV-470 — Air-relative velocity and airspeed

The **air-relative velocity** is the vehicle velocity minus the velocity of the air mass at `O_B`. **Airspeed** is its magnitude. In version 1 the air mass moves with a uniform **wind velocity** `w`, the same everywhere in the operating volume and set by the test environment for each run (D17, L0-ASM-050). The air-relative velocity is `v − w`; in a run with no wind applied it equals the vehicle velocity.
**Status:** Fixed (G0-09: D17).

### CV-480 — Horizontal speed

**Horizontal speed** `V_H` is the magnitude of the horizontal component of the vehicle velocity: `V_H = √(v_N² + v_E²)`, relative to the ground, always ≥ 0. It does not depend on attitude or heading. With wind (CV-470) it differs from the horizontal airspeed; with no wind applied it equals it.
**Status:** Proposed.

### CV-490 — Vertical speed

**Vertical speed** `VS` is the rate of change of altitude: `VS = dh/dt = −v_D`, positive when climbing. It does not depend on attitude.
**Status:** Proposed.

## 6. Direction reference and direction angles (CV-5xx)

### CV-510 — North reference

**North** is the direction of `+x_L`. It is true north by definition, and on the flat world of CV-110 it is the same direction everywhere (true north and grid north coincide). Heading, track, course and VOR radials are all referenced to true north. Magnetic north and magnetic variation are not modelled in version 1. The word "magnetic" is not used in requirements.
**Status:** Fixed (G0-06: D12).

### CV-520 — Direction angles in the horizontal plane

A **direction angle** (heading, track, course, radial, bearing) is measured in the horizontal plane from north, positive clockwise seen from above (toward east), in the range [0°, 360°) (in radians, [0, 2π)). North is 0. How the crew-facing value of north is shown (for example "360" or "000") is a display requirement, not a convention.
**Status:** Proposed.

### CV-530 — Heading

**Heading** ψ is the direction in which the nose points: the direction angle of the horizontal projection of `x_B`. It equals the Euler yaw angle of CV-210 for every pitch angle other than ±90°. Heading is defined by attitude only. It does not depend on the vehicle velocity.
**Status:** Proposed.

### CV-540 — Track

**Track** χ is the direction of horizontal motion: the direction angle of the horizontal velocity `(v_N, v_E)`, so χ = wrap360(atan2(v_E, v_N)). It is ground-referenced. Track is defined by velocity only and does not depend on attitude. It is undefined when the horizontal speed is zero, and requirements that use track state the validity condition of CV-580.
**Status:** Proposed.

### CV-550 — Heading and track are independent

On the Aeronef, translation does not require the vehicle to turn or tilt, so heading and track are independent: any heading can be combined with any track. Likewise pitch angle and flight path angle are independent, and roll angle has no effect on the direction of motion. The **relative track** wrap180(χ − ψ) is the direction of horizontal motion relative to the nose: 0 means moving nose-first, +90° means moving to the right, ±180° means moving tail-first. A requirement on the direction of motion uses track; a requirement on where the vehicle points uses heading. The behaviour of the attitude axes in each guidance mode is open question Q2 (TBR).
**Status:** Fixed (D10).

### CV-560 — Flight path angle

The **flight path angle** γ is the angle between the vehicle velocity and the horizontal plane, positive when climbing: γ = atan2(VS, V_H), in the range [−90°, +90°]. It depends on velocity only, not on pitch angle. It is undefined when the total speed is zero (CV-580). "Climb on flight path angle" means γ > 0; "descent on flight path angle" means γ < 0.
**Status:** Proposed.

### CV-570 — Climb, descent and level flight

The vehicle is **climbing** when VS > 0, **descending** when VS < 0 and in **level flight** when VS = 0. Requirements that judge these states from data use the tolerance parameters of the requirement concerned (CV-930). Level flight is a property of motion. It is unrelated to level attitude (CV-270).
**Status:** Proposed.

### CV-580 — Validity of direction quantities

Some direction quantities are undefined, or ill-conditioned, at specific states:

| Quantity | Undefined when | Validity threshold (parameter) |
| --- | --- | --- |
| Heading, roll angle | Pitch angle = ±90° | `P-NAV-030`: maximum absolute pitch angle for which heading is valid (TBD) |
| Track | Horizontal speed = 0 | `P-NAV-010`: minimum horizontal speed for which track is valid (TBD) |
| Flight path angle | Total speed = 0 | `P-NAV-020`: minimum total speed for which flight path angle is valid (TBD) |
| VOR radial | Horizontal distance from the station = 0 | `P-NAV-040`: minimum horizontal distance for which the radial is valid (TBD) |

How the Aeronef behaves when a quantity is invalid (validity flags, annunciation, mode reversion) is a requirement matter for NAV, AF and TM. The thresholds are parameters, not conventions.
**Status:** Proposed.

## 7. VOR geometry (CV-6xx)

The VOR fidelity is open question Q4. The definitions below follow the plan's proposal for Q4: ground stations at fixed positions in L, radials referenced to true north, an ideal signal within a reception range, and no noise in version 1.

### CV-610 — VOR station

A **VOR station** is a fixed point `S` in L, given by its north and east coordinates and its altitude, with an identifier. Station positions are part of the world definition (CV-130).
**Status:** Fixed (D12).

### CV-620 — Radial

The **radial** of the vehicle from a station, `R_ac`, is the direction angle (CV-520) of the horizontal line from the station to the vehicle: the bearing *from* the station. The vehicle on the 090 radial is due east of the station. A radial is a property of position only, independent of heading and track. A radial is also a half-line on the datum plane: "radial R" means the set of horizontal positions whose bearing from the station is R.
**Status:** Fixed (D12).

### CV-630 — Selected course

The **selected course** C is the direction angle of the path the vehicle is to follow along a radial line through the station. A selected course C is flown **outbound** on radial C (away from the station) or **inbound** on radial wrap360(C + 180°) (toward the station). Whether the crew selects a course (as on an airliner course selector) or a radial is issue A3-Q09. The definitions in CV-640 to CV-660 work for both, because a selected radial R used outbound is the course C = R.
**Status:** Fixed (D14).

### CV-640 — TO/FROM sense

For a selected course C and a vehicle radial `R_ac`, the sense is **FROM** when |wrap180(R_ac − C)| < 90° (the vehicle is beyond the station in the course direction) and **TO** when |wrap180(R_ac − C)| > 90°. At exactly 90° (abeam the station) the sense is undefined. Any band of ambiguity around 90° is a NAV requirement matter.
**Status:** Fixed (D12).

### CV-650 — Course deviation (angular)

The **course deviation** δ is the signed angle between the selected course line and the line from the station to the vehicle, positive when the vehicle is to the **right** of the selected course, looking along the course direction:

- FROM: δ = wrap180(R_ac − C);
- TO: δ = wrap180(C + 180° − R_ac).

The sign follows CV-910 (actual minus desired, as a lateral offset). A course deviation indicator conventionally shows the course relative to the vehicle ("fly toward the needle"), the opposite sign. How the deviation is shown to the crew is a display requirement, not a convention.
**Status:** Proposed (G0-12).

### CV-660 — Cross-track deviation (linear)

The **cross-track deviation** `d` is the signed horizontal distance from the vehicle to the line through the station along the selected course, positive to the right of the course looking along the course direction: `d = D_H · sin(R_ac − C)`, where `D_H` is the horizontal distance from the station to the vehicle. The same formula holds in the TO and FROM senses.
**Status:** Proposed (G0-12).

### CV-670 — Reception range

A station's signal is received when the vehicle is within the **reception range** `P-NAV-050` of the station (TBD). Whether reception range is measured as horizontal distance or slant range (CV-450), and whether a cone of silence above the station is modelled, are NAV requirement matters under D12 (ideal VOR). Outside reception, the radial, sense and deviations are not available.
**Status:** Fixed (D12).

## 8. Units (CV-7xx)

### CV-710 — SI for requirements, model and signals

Requirements, the MS-DYN, internal signals, ICD signals and operational data use SI units. The exceptions are the crew-facing units under the rule in CV-760.
**Status:** Proposed.

### CV-720 — SI units by quantity

| Quantity | Unit |
| --- | --- |
| Length, position, distance, altitude | m |
| Time, duration | s |
| Frequency, rate of execution | Hz |
| Mass, fuel quantity | kg |
| Fuel mass flow | kg/s |
| Velocity, speed | m/s |
| Acceleration | m/s² |
| Force | N |
| Moment | N·m |
| Moment and product of inertia | kg·m² |
| Density | kg/m³ |
| Angle (attitude, heading, track, flight path angle, radial, course, deviation) | rad (see CV-730) |
| Angular rate | rad/s |
| Angular acceleration | rad/s² |
| Dimensionless ratios | 1 (written as a fraction, not as a percentage, in signals and parameters) |
**Status:** Proposed.

### CV-730 — Angles on the SI side are in radians

All angles and angular rates in requirements (through their parameters), the model, signals and parameters are in radians and radians per second. Degrees appear only as a crew-facing unit (CV-740). Because requirement statements carry no numbers (only parameter IDs), radians cost no readability; they avoid mixed angle units in the model and the parameter database.

The alternative is to admit degrees in requirements as a unit accepted for use with SI. It is recorded in G0-05.
**Status:** Fixed (G0-05: D23).

### CV-740 — Crew-facing units (decision D7)

The units for everything the crew selects or sees are North American aviation units:

| Quantity | Crew-facing unit | Symbol |
| --- | --- | --- |
| Altitude (and other vertical distances shown to the crew) | foot | ft |
| Vertical speed | foot per minute | ft/min |
| Horizontal speed (and any other speed shown to the crew) | knot | kt |
| Horizontal distance (for example distance to a VOR station) | nautical mile | NM |
| Heading, track, flight path angle, radial, course | degree | ° (deg) |
| Fuel quantity | pound | lb |
| Durations shown to the crew (for example flight time) | hour or minute | h, min |

Fuel is shown in pounds (D9). Time is shown in whatever unit makes sense: vertical rates in ft/min, durations in hours or minutes (D34).
**Status:** Fixed (D7, D9, D34).

### CV-750 — Exact conversion factors

These factors are exact by definition and are used without rounding:

| Crew-facing unit | SI value |
| --- | --- |
| 1 ft | 0.3048 m |
| 1 NM | 1852 m |
| 1 kt | 1852/3600 m/s (= 0.514 444… m/s, a repeating decimal: use the fraction) |
| 1 ft/min | 0.3048/60 m/s = 0.00508 m/s |
| 1 min | 60 s |
| 1° | π/180 rad |
| 1 h | 3600 s |
| 1 lb (fuel, D9) | 0.453 592 37 kg |

Conversion from SI to crew units uses the inverse of these factors (for example, altitude in ft = h / 0.3048).
**Status:** Proposed. The factors themselves are exact international definitions.

### CV-760 — Where crew-facing units may appear

Crew-facing units appear only in:

1. requirements whose subject is a crew selection: the selectable range, the selection resolution or the way a selected value is entered;
2. requirements whose subject is an annunciation or a value shown to the crew: the shown value, its resolution and its format;
3. the parameters used only by those requirements (CV-790);
4. operational data signals that record a crew-facing value as selected or as shown, in addition to the SI signal for the same quantity, with the unit stated in the signal definition.

Every other requirement, and every model quantity, internal signal and ICD signal, is in SI. A requirement in group 1 or 2 that links a crew-facing value to an SI quantity cites CV-750 for the conversion.
**Status:** Proposed.

### CV-770 — Conversion of crew selections

A **selected value** entered by the crew in a crew-facing unit becomes the corresponding SI **target** by multiplication by the exact CV-750 factor, without intermediate rounding. The selection resolution (for example the step between selectable altitudes) is a parameter of the selection requirement.
**Status:** Proposed.

### CV-780 — Display resolution and rounding

The resolution with which a crew-facing value is shown, and the rounding rule from the SI value (for example round half away from zero), are requirement matters for AF and TM. They are parameters (proposed `P-TM-020` to `P-TM-070`, TBD), not conventions. Until those requirements exist, no rounding rule is implied.
**Status:** Proposed.

### CV-790 — Units in the parameter database

Every parameter has a unit. A parameter used by the SI-side requirements has an SI unit (CV-720, CV-730). A parameter used only by a requirement in CV-760 groups 1 or 2 (for example a vertical-speed selection step) is stored in its crew-facing unit, so that its value is exact as specified (100 ft/min rather than 0.508 m/s), and is marked as crew-facing. This needs a field in the parameter database schema (issue A3-Q08).
**Status:** Fixed (G0-10: D34).

## 9. Time base (CV-8xx)

### CV-810 — Simulation time

**Simulation time** `t` is the independent time variable of the vehicle model, in seconds. `t = 0` is the instant at which a run's initial conditions apply. Simulation time is independent of wall-clock time: a run may execute faster or slower than real time without any change to `t`.
**Status:** Proposed.

### CV-820 — Simulation step

The vehicle model advances in fixed **simulation steps** of duration `Δt = P-SYS-300` (TBD), consistent with F-STP-01 (execution at a fixed step). The **step index** `k` is an integer counted from 0 at `t = 0`. The simulation time of step k is `t_k = k · Δt`, defined by that product and not by accumulating steps.
**Status:** Fixed (G0-11: D35).

### CV-830 — Control frame and output sample

- A **control frame** is one execution of the flight-control or autoflight functions. The control frame period is `P-SYS-310` (TBD).
- An **output sample** is one record of operational data. The output sample period is `P-TM-010` (TBD).

Whether these periods equal the simulation step or are integer multiples of it is an ICD-AER-STP matter.
**Status:** Proposed.

### CV-840 — Timestamps

Each output sample, crew selection and event record carries its **timestamp**: the step index k and the simulation time `t_k` of the step to which it belongs. The step index is authoritative. `t_k` is derived from it by CV-820 and is included for readability. A value timestamped k is the value at `t_k`. Whether an input timestamped k first affects the state at step k or at step k + 1 is fixed in the ICD-AER-STP.
**Status:** Fixed (G0-11: D35).

### CV-850 — Time in requirements

Every duration and time limit in a requirement is in simulation time, in seconds, through a parameter. Wall-clock time appears only in STP requirements on execution speed.
**Status:** Proposed.

### CV-860 — Measuring a response time

A requirement of the form "when <trigger>, … within T" is measured from the **trigger time**, the timestamp of the first sample at which the trigger condition is true, to the timestamp of the first sample at which the response condition is true. The response satisfies the requirement when that difference is ≤ T (CV-940). A requirement that needs a different measurement (for example "and remains true for T2") states it.
**Status:** Proposed.

### CV-870 — No calendar time in the model

The vehicle model has no date, time of day or calendar epoch. Run identification metadata (wall-clock start time, software version) belongs to the STP.
**Status:** Proposed.

## 10. Rules for expressing requirements (CV-9xx)

### CV-910 — Sign of errors and deviations

An **error** or **deviation** is actual value minus target value: e = actual − target. A positive altitude error means the vehicle is above the target. A positive heading error means the nose is to the right of the target heading (after CV-930 wrapping). For lateral deviations (CV-650, CV-660), "actual minus target" means positive to the right of the desired path.
**Status:** Fixed (G0-14: D35).

### CV-920 — Angle wrapping functions

- `wrap360(a)` returns the angle equal to `a` modulo 360° in [0°, 360°) (in radians, [0, 2π)).
- `wrap180(a)` returns the angle equal to `a` modulo 360° in (−180°, +180°] (in radians, (−π, +π]).

Direction angles (CV-520) are reported with `wrap360`. Roll angle and angular differences are reported with `wrap180`.
**Status:** Proposed.

### CV-930 — Angular differences

The difference between two direction angles, for example a heading error or a track error, is always wrap180(a − b), the shortest signed angle, so that 359° and 1° differ by 2°, not 358°. A requirement that intends the long way round states it explicitly.
**Status:** Proposed.

### CV-940 — Bounds and comparisons

- "Within X of the target" means |actual − target| ≤ X, inclusive, with angles differenced by CV-930.
- "At most X" means ≤ X, and "at least X" means ≥ X.
- "Exceeds X" means > X, and "falls below X" means < X.
- "Reaches X" means the first sample at which the quantity is ≥ X when increasing, or ≤ X when decreasing.
**Status:** Fixed (G0-15: D35).

### CV-950 — Naming axes and components

A requirement names a component by its frame and axis in words ("velocity along the body y axis", "north component of position", "moment about the body z axis"). Unqualified "x", "lateral" or "vertical" is not used for a component. In this document, "lateral" means along `y_B` when it refers to the body and "horizontal" means parallel to the datum plane.
**Status:** Proposed.

### CV-960 — Defined quantity names only

Requirements use the quantity names defined here: altitude, height (with reference), horizontal distance, slant range, total speed, horizontal speed, vertical speed, airspeed, heading, track, relative track, flight path angle, pitch angle, roll angle, radial, selected course, course deviation and cross-track deviation. Airliner terms that do not apply to the Aeronef (bank angle, angle of attack, indicated airspeed, Mach number, magnetic heading) are not used.
**Status:** Proposed.

### CV-970 — Attitude stated separately from motion

Because attitude is independent of motion (CV-550), a requirement that constrains the motion (position, altitude, speed, track, flight path angle) does not imply anything about the attitude, and the reverse. Pitch and roll stay level in every mode (D10); each mode's heading behaviour is stated by its own requirements.
**Status:** Fixed (D10).

## 11. Decisions for G0

The project owner decides these items at Gate G0. Each row gives the recommendation of this proposal and the owner's decision (2026-10-25, plan §9). Decisions taken become **Fixed** in the convention concerned.

| ID | Decision | Options | Recommendation | Conventions | Owner decision |
| --- | --- | --- | --- | --- | --- |
| G0-01 | Local reference frame axes | NED; ENU | **NED** (R-004, aligns with the FRD body frame, aviation angles read directly). Altitude and vertical speed defined positive up to contain the sign flip | CV-120, §2.1 | Accepted (D21) |
| G0-02 | Body frame origin and axes | Origin at the CG or at a geometric reference point; FRD (x forward, y right, z down) or FLU | **Origin at the fixed CG; FRD axes** per R-004 | CV-160, CV-170 | Accepted (D35) |
| G0-03 | Attitude representation | Euler angles only; quaternion authoritative with Euler angles derived | **3-2-1 Euler angles for requirements; scalar-first Hamilton unit quaternion as the authoritative attitude in the state and ICD**, because pitch angles of ±90° are reachable | CV-210, CV-250 | Accepted (D22) |
| G0-04 | Euler-angle ranges | Heading [0, 360) or (−180, 180]; roll (−180, 180] | **Heading [0°, 360°), pitch [−90°, +90°], roll (−180°, +180°]** | CV-230 | Accepted (D35) |
| G0-05 | Angle unit on the SI side | Radians everywhere except crew-facing; degrees allowed in requirements and parameters | **Radians**: requirement statements carry no numbers, so degrees add no readability, and one angle unit avoids conversion errors | CV-730 | Accepted (D23) |
| G0-06 | North reference | True north, no magnetic variation; magnetic north with a variation model | **True north, no magnetic variation** in version 1 | CV-510 | Accepted (D12) |
| G0-07 | World model | Flat, non-rotating, uniform gravity; spherical or WGS-84 rotating Earth | **Flat, non-rotating, uniform gravity, by definition** | CV-110, CV-140 | Accepted (D35) |
| G0-08 | Altitude datum and definition | Geometric altitude above the datum plane; pressure altitude | **Geometric altitude of the CG above the datum plane, positive up**; no pressure altitude | CV-420, CV-430 | Accepted (D35) |
| G0-09 | Air mass | Still air (no wind); wind model | **Still air in version 1**, so airspeed equals ground speed; recorded as an L0 assumption | CV-470 | **D17: wind**, not still air |
| G0-10 | Units of crew-facing parameters | All parameters in SI; crew-facing parameters in crew units, marked | **Crew-facing parameters in crew units, marked crew-facing**, so values like 100 ft/min stay exact | CV-790 | Accepted (D34) |
| G0-11 | Time base | Integer step index authoritative; floating time authoritative | **Integer step index authoritative, `t_k = k·Δt`, `t = 0` at initial conditions** | CV-820, CV-840 | Accepted (D35) |
| G0-12 | VOR course deviation sign | Positive right of course (actual − desired); positive "fly right" (CDI sense) | **Positive when the vehicle is right of the selected course**; the CDI fly-to sense is a display matter | CV-650, CV-660 | Deferred to L2 (#54) |
| G0-13 | Product-of-inertia sign | Positive-integral products with negative tensor off-diagonals; the opposite | **Positive-integral products, negative off-diagonals** | CV-350 | Accepted (D35) |
| G0-14 | Error and deviation sign | Actual − target; target − actual | **Actual − target** | CV-910 | Accepted (D35) |
| G0-15 | Bound inclusivity | "Within X" inclusive (≤); exclusive (<) | **Inclusive** | CV-940 | Accepted (D35) |

Questions that are not conventions but affect them (crew fuel unit, ground surface, course versus radial selection, parameter schema) were raised in `work/A3/issues.md` and answered in GitHub issues #46 to #58 (decisions D8, D9, D14, D34).
