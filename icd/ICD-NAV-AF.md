# ICD-NAV-AF — Navigation to autoflight

**Status:** Draft, written at integration (I1, 2026-11-08) from `work/C6/interface_needs.md` §2 and `work/C5/interface_needs.md` §1 and §4. Baselined with L2 at G2. The horizontal position (CR-C6-01) and the horizontal velocity components (CR-C5-01) are in L1-AER-530 and -890 since the owner's approval (D76).
**Parties:** navigation (NAV) gives; autoflight (AF) takes. The flight control panel (FCP) takes the same quantities through ICD-FCP, by reference to this document. TM records them (ICD-AER-TST).
**Classification:** Protected design material.
**Related:** [CONVENTIONS](../specs/CONVENTIONS.md) CV-400 to CV-580, [FUNCTIONAL_ANALYSIS](../specs/FUNCTIONAL_ANALYSIS.md) I-17, L1-AER-530, -890, -440.

## 1. Scope

The one interface by which AF gets the guidance quantities (L1-AER-890). AF receives no vehicle state (L1-AER-440): the quantities of this interface are its only knowledge of the vehicle's motion. NAV computes each quantity in closed form from the frame-start state, with no estimator, filter or memory between frames (DD-450). FC takes no data from NAV and reads the vehicle state directly (ICD-VM-FS).

## 2. Conventions

| Item | Rule |
| --- | --- |
| Units and frames | SI. Frames and sign conventions as the CONVENTIONS entry in the table of §3 states. Nothing crew-facing crosses (CV-760). |
| Timing | Once per control frame. The quantities of frame k are computed from the vehicle state of the frame's first simulation step (the frame-start state) and are ready before AF executes in that frame (order FCP, NAV, AF, FC, DD-010; L2-AER-NAV-310). The timestamp is the step index of the frame-start step (CV-840). |
| Validity | Each quantity goes with a validity flag (true = valid). The flag follows the rules of §3. A quantity with no validity rule is valid at every control frame. |
| Invalid values | While the heading is invalid its value is the CV-260 yaw angle, which is defined at every attitude (DD-460). While the track is invalid its value is zero (DD-430). The flag, not the value, tells which. |
| Hysteresis | None. Each validity is a function of the frame-start state alone, inclusive at the threshold (DD-440). |

## 3. Data items

| Item | Symbol | Unit | Frame / reference | Range | Definition | Validity rule | Value while invalid | NAV record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Altitude | h | m | Datum plane, positive up, at the CG | ≥ 0 in a run (CV-420) | CV-430: h = −z_D | Valid at each frame | — | L2-AER-NAV-010, -150 |
| Height above the ground | h_G | m | Datum plane, positive up, at the lowest point of the body shape (gear excluded) | ≥ 0 in a run | CV-400: h − P-DYN-030/2 − ((P-DYN-020 − P-DYN-030)/2)·\|sin θ\| | Valid at each frame | — | L2-AER-NAV-020, -150 |
| Horizontal position, north | x_N | m | L, north | Real | CV-410 | Valid at each frame | — | L2-AER-NAV-030, -150 |
| Horizontal position, east | y_E | m | L, east | Real | CV-410 | Valid at each frame | — | L2-AER-NAV-030, -150 |
| Horizontal velocity, north | v_N | m/s | Ground-referenced, components in L (and V) | Real | CV-460: north component of the vehicle velocity | Valid at each frame | — | L2-AER-NAV-080, -280 |
| Horizontal velocity, east | v_E | m/s | Ground-referenced, components in L (and V) | Real | CV-460: east component of the vehicle velocity | Valid at each frame | — | L2-AER-NAV-080, -280 |
| Horizontal speed | V_H | m/s | Ground-referenced (L) | ≥ 0 | CV-480: √(v_N² + v_E²) | Valid at each frame | — | L2-AER-NAV-040, -150 |
| Vertical speed | VS | m/s | Positive up | Real | CV-490: −v_D | Valid at each frame | — | L2-AER-NAV-050, -150 |
| Heading | ψ | rad | From true north, clockwise (CV-510, CV-520) | [0, 2π) | CV-530 by CV-260 from the quaternion | Valid while \|θ\| ≤ [P-NAV-030] (inclusive) | The CV-260 yaw angle | L2-AER-NAV-060, -120, -130 |
| Track | χ | rad | From true north, clockwise, ground-referenced | [0, 2π) | CV-540: wrap360(atan2(v_E, v_N)) | Valid while V_H ≥ [P-NAV-010] (inclusive) | 0 | L2-AER-NAV-070, -100, -110, -140 |

The horizontal velocity components give the direction of a residual motion below the track's validity speed, which Stationary, Go to hover and the hold of a position need (the stopping position and the initial references, L2-AER-AF-330).

## 4. Use by autoflight

| Item | Use |
| --- | --- |
| Altitude, height above the ground | Vertical guidance; Go to hover, Hover, Takeoff and Land guide on the height above the ground (CV-400, D70) |
| Horizontal position and velocity components | The stopping position and the reference position of a hold; the initial references (L2-AER-AF-040, -330, -920) |
| Horizontal speed, vertical speed | Heading mode, the capture and the condition for Hover |
| Heading | The initial heading reference; the mode logic does not depend on its validity (IN-C6-13) |
| Track | Not used by AF. The track tolerance [P-AF-140] is a test measure on NAV's track and applies only at a horizontal speed of at least [P-NAV-010] |

## 5. Rules

| ID | Rule |
| --- | --- |
| R-01 | AF takes the quantities only through this interface and uses a quantity only where its validity is true, except where §4 says otherwise (L2-AER-AF-040). |
| R-02 | NAV gives AF no vehicle state, no heading rate, no vehicle acceleration and no gear clearance. The gear clearance at the hover height is [P-AF-210] − [P-DYN-040] at level attitude, an AF computation (C6-Q08). |
| R-03 | The body geometry of the height above the ground ([P-DYN-020], [P-DYN-030]) and the thresholds [P-NAV-010], [P-NAV-030] are taken from the run's vehicle parameter set (C6-Q06, glossary *Vehicle parameter set*). |
| R-04 | NAV's outputs are exactly the CONVENTIONS definitions applied to the frame-start state; they agree with an independent computation from the recorded state within [P-NAV-060], [P-NAV-070] and [P-NAV-080] (L2-AER-NAV-320). |

## 6. Other recipients of the same quantities

| Recipient | Interface | Items |
| --- | --- | --- |
| FCP | ICD-FCP §4 (I-18) | Altitude, vertical speed, horizontal speed, heading, track, each with its validity. Not the height above the ground, the position or the velocity components. |
| TM | ICD-AER-TST, signal S-16 (I-35) | The navigation quantities with their validity and the frame-start timestamp (CR-C6-02, L1-AER-640). The horizontal position is in the recorded vehicle state. |

## 7. Traceability

| NAV side | L2-AER-NAV-010 to -150 (quantities), -200 to -290 (interfaces), -310 to -330 |
| --- | --- |
| AF side | L2-AER-AF-040, -070, -330, -920 |
| L1 | L1-AER-440, -530, -890 |
| Decisions | DD-430, DD-440, DD-450, DD-460 |
