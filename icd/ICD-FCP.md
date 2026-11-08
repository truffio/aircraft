# ICD-FCP — Flight control panel

**Status:** Draft, written at integration (I1, 2026-11-08) from `work/C8/interface_needs.md` §1 to §4 and `work/C5/interface_needs.md` §3. Baselined with L2 at G2. The owner asked for a separate ICD for the panel boundaries (D63).
**Parties:** the flight control panel (FCP) with autoflight (AF), navigation (NAV) and the fuel subsystem (FU). The crew side of the panel (the crew interface input and output, in crew units) is in ICD-AER-TST §4.
**Classification:** Protected design material.
**Related:** [CONVENTIONS](../specs/CONVENTIONS.md) CV-740 to CV-780, [AF_MODE_LOGIC](../specs/AF_MODE_LOGIC.md), [FUNCTIONAL_ANALYSIS](../specs/FUNCTIONAL_ANALYSIS.md) I-16, I-18, I-19, I-06, L1-AER-880.

## 1. Scope

L1-AER-880 closes the data between the panel and the other functions: from the panel to autoflight, the mode selections and the targets in SI; from autoflight, navigation and the fuel subsystem to the panel, what the panel presents. **All data on this interface are in SI.** Crew units stay inside the panel, which converts at its boundary (CV-760 group 2, L1-AER-870, L2-AER-FCP-200). The panel receives no vehicle state and gives the vehicle model nothing.

## 2. Conventions

| Item | Rule |
| --- | --- |
| Timing | The panel executes first in the control frame (order FCP, NAV, AF, FC, DD-010). All items are those of the control frame that starts at the step with the timestamp (CV-840). The panel takes each crew selection timestamped after the previous frame start and at or before this one; within the frame it applies each selected value first, then gives AF the mode selections in timestamp order (receipt order for equal timestamps), with the selector targets of the end of the intake (DD-520). |
| Units | SI (CV-720). Heading in [0, 2π) rad. Altitude is the altitude of the centre of gravity (CV-430). Vertical speed is signed, positive up. |
| Refusals | A selection the panel refuses (a value outside its selectable range or off its resolution) changes nothing: the selector keeps its value, the target is unchanged and the selector is not reported as accepted (DD-530). |

## 3. FCP to AF (I-19)

| Item | Content | Unit and range | Panel record |
| --- | --- | --- | --- |
| Mode selections | The ordered list of the mode selections taken in the frame, each with its timestamp. Any of eight: STAT, HDG, ALT, GO ALT, V/S, GO HOVER, TAKEOFF, LAND. The panel filters none; AF decides each one against the mode state (AF_MODE_LOGIC §6). There is no Hover selection and no autoflight disengage selection (D71, D76) | Set of eight; may be empty | L2-AER-FCP-050, -080, -090 |
| Heading target | The heading selector's SI value | rad, [0, 2π) | L2-AER-FCP-100 |
| Horizontal speed target | The horizontal speed selector's SI value, a ground speed | m/s, 0 to [P-SYS-230] | L2-AER-FCP-110 |
| Altitude target | The altitude selector's SI value, a CG altitude | m, from [P-SYS-210] + [P-DYN-030]/2 to [P-SYS-200] | L2-AER-FCP-120 |
| Vertical speed target | The vertical speed selector's SI value | m/s, from −[P-SYS-250] to [P-SYS-240], zero included | L2-AER-FCP-130 |
| Accepted selectors | The subset of the four selectors that accepted a value in the frame | Subset of four | L2-AER-FCP-050, -090 |

At the first frame of a run the targets are those of the initial selected values and no selector is reported accepted (L2-AER-FCP-520, -530). The standard vertical speed [P-AF-220] is not a selector value. AF decides when Go to altitude uses it (AF_MODE_LOGIC TG-2). The panel never resets or synchronises a selector from AF data.

## 4. NAV to FCP (I-18)

By reference to ICD-NAV-AF §3: the altitude, the vertical speed, the horizontal speed, the heading and the track, each with its validity, in SI. FCP does not take the height above the ground, the horizontal position or the velocity components (they are not indications). The panel converts and rounds (CV-750, CV-780), and presents an invalid heading or track as not valid, with no shown value (CV-580, L2-AER-FCP-370). On the ground the altitude indication is the CG altitude at rest, [P-DYN-030]/2 + [P-DYN-040] (11 ft with the present values), not zero (CV-430).

## 5. AF to FCP (I-16): annunciation content

| Item | Content | Values | Panel record |
| --- | --- | --- | --- |
| Mode state | The five fields of AF_MODE_LOGIC §3: autoflight engaged; active horizontal mode; active vertical mode; active both-axes mode; armed mode | The identifiers of AF_MODE_LOGIC §2, or none. The set is fixed for every autoflight implementation. The empty mode state (nothing active, for example on the ground and after a landing) is valid content | L2-AER-FCP-320, -330 |
| Targets in use | Each target in use, with its quantity | Quantity in {altitude, vertical speed, horizontal speed, heading}; the value in SI. AF's own targets (the held altitude, the hover altitude, the standard vertical speed in use) go here; the reference position does not | L2-AER-FCP-330 |
| Gear position | The landing gear position, from the gear state | extended, retracted, in transit | L2-AER-FCP-340 |

AF writes no selector (IN-C8-06). If AF ever needs a selector reset, that is a new AF to FCP item and a change to L1-AER-880. The mode labels (STAT, HDG, ALT, GO ALT, V/S, GO HOVER, HOVER, TAKEOFF, LAND) are AF_MODE_LOGIC's and the panel shows them unchanged. The gear labels (GEAR DOWN, GEAR UP, GEAR TRANSIT) and the fuel alert labels are the panel's (DD-550, C8-Q03).

## 6. FU to FCP (I-06): fuel state

By reference to ICD-VM-FS §5: the remaining fuel mass in kg, the low-fuel indication and the fuel-exhaustion indication, read at the start of each control frame. The panel converts the remaining fuel mass to lb, rounds it to [P-FCP-010], and shows the fuel alert: FUEL EXHAUSTED while the exhaustion indication is set, LOW FUEL while only the low-fuel indication is set, no label otherwise (DD-550). The same item goes to AF, which uses only the fuel-exhaustion indication (L2-AER-AF-060).

## 7. Panel to TST and TM

The crew interface output (four annunciation items, four selector readouts, six indications with a validity flag each, in crew units) goes to the TST at each output sample (ICD-AER-TST §4, I-42). The crew selection records and the presented annunciations go to TM (ICD-AER-TST §5, I-36, I-38).

## 8. Rules

| ID | Rule |
| --- | --- |
| R-01 | The panel gives AF only the items of §3 and takes from AF only the items of §5 (L1-AER-880; L2-AER-FCP-050, -060). |
| R-02 | Every selector value that reaches AF is the exact CV-750 conversion of a crew-unit value that passed the range and resolution check on the exact conversion (DD-530). |
| R-03 | The panel and AF are not separate sources of a conversion: no crew unit crosses this interface. |

## 9. Traceability

| Panel side | L2-AER-FCP-010 to -140 (selections), -200 to -240 (conversion), -300 to -410 (presentation), -500 to -530 (records and initial values) |
| --- | --- |
| AF side | L2-AER-AF-050, -100, -120 to -140, -310, -320, -800 to -840 |
| L1 | L1-AER-470, -480, -490, -870, -880 |
| Decisions | DD-520, DD-530, DD-540, DD-550, DD-560 |
