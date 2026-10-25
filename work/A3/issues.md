# A3 — Issues, conflicts and questions for the project owner

## Questions for the project owner

Each question has a proposed answer. The G0 reference points to the "Decisions for G0" table in `specs/CONVENTIONS.md` §11.

| ID | Question | Proposed answer | G0 ref. | Conventions |
| --- | --- | --- | --- | --- |
| A3-Q01 | Is the local reference frame north-east-down (NED) or east-north-up (ENU)? | NED, per AIAA R-004. It pairs with the forward-right-down body frame, and heading, track and radials read directly as standard angles. Requirements use altitude and vertical speed (positive up), never `z`. | G0-01 | CV-120, §2.1 |
| A3-Q02 | Is the attitude quaternion the authoritative attitude in the model state and the ICD, with Euler angles derived? | Yes. Pitch angles of ±90° are reachable on the Aeronef, and Euler angles are singular there. Requirements still use Euler angles. | G0-03 | CV-250, CV-260 |
| A3-Q03 | On the SI side, are angles in radians, or are degrees allowed in requirements and parameters? | Radians. Requirement statements carry no numbers, so degrees add no readability; one angle unit avoids conversion errors. Degrees stay crew-facing only. | G0-05 | CV-730 |
| A3-Q04 | Are heading, track, course and radials all referenced to true north, with no magnetic variation, in version 1? (plan Q4) | Yes. On the flat world, true north is the `+x_L` direction everywhere. | G0-06 | CV-510 |
| A3-Q05 | Is the air mass at rest (no wind) in version 1? | Yes. Airspeed equals ground speed, and horizontal speed is ground-referenced. Record it as an L0 assumption (A1). | G0-09 | CV-470 |
| A3-Q06 | Does the world have a ground surface the vehicle can contact (at the datum plane), or only a datum plane for altitude? | Datum plane only in version 1, with no ground contact model. Scenarios start airborne, and altitude may become negative without special behaviour. To confirm with the ConOps (A2) and MS-DYN (C1). | — | CV-420 |
| A3-Q07 | What is the crew-facing unit of fuel quantity? D7 does not cover it. | Pounds (lb, 1 lb = 0.453 592 37 kg exactly), consistent with North American practice. Alternative: kg. A fraction of initial fuel can be shown in addition, as an annunciation requirement. | — | CV-740, CV-750 |
| A3-Q08 | Are crew-facing parameters (selection steps, display resolutions) stored in their crew unit and marked crew-facing in `PARAMETERS.yaml`? | Yes. Add a `crew_unit: true` (or similar) field to the schema, so values like 100 ft/min stay exact. All other parameters stay SI. | G0-10 | CV-790 |
| A3-Q09 | In VOR radial tracking, does the crew select a course (as on an airliner course selector, flown TO or FROM) or a radial (outbound only)? | A course, so both inbound and outbound tracking are possible. The TO/FROM sense and the deviation definitions in CV-640 to CV-660 support it. Final choice with C5 and M7. | — | CV-630 |
| A3-Q10 | What is the sign of the VOR course deviation? | Positive when the vehicle is to the right of the selected course looking along the course (actual minus desired). The "fly toward the needle" sense is a display matter. | G0-12 | CV-650, CV-660 |
| A3-Q11 | Which rounding rule converts SI values to crew-shown values, and is north shown as 360 or 000? | Round half away from zero to the display resolution; north shown as 360, as on airliner selectors. These belong in TM and AF requirements, not in the conventions. | — | CV-520, CV-780 |
| A3-Q12 | For modes, is "active" the only state term, with "engaged" reserved for the autoflight system as a whole? | Yes: mode states are armed and active; the autoflight system is engaged or not. C5 confirms in AF_MODE_LOGIC. | — | Glossary |
| A3-Q13 | The conventions follow standard R-004 practice, but A3 did not have the text of ANSI/AIAA R-004-1992. Should the G0 inspector check them against the standard text? | Yes, if a copy is available. Otherwise record them as "consistent with R-004 practice" and fix them at G0 on their own merits. | — | §0 |
| A3-Q14 | Can the remaining G0 items be approved as recommended: body frame FRD with origin at the CG (G0-02), Euler ranges (G0-04), flat non-rotating world (G0-07), geometric altitude above the datum plane (G0-08), integer step index as the time base (G0-11), product-of-inertia sign (G0-13), error sign actual − target (G0-14), inclusive bounds (G0-15)? | Yes, as recommended in CONVENTIONS §11. | G0-02, -04, -07, -08, -11, -13, -14, -15 | §11 |

## Conflicts and notes for other artifacts

| ID | Artifact | Note | Proposed action |
| --- | --- | --- | --- |
| A3-N01 | METHODOLOGY §12, example ICD-AER-STP-005 | It says the local reference frame is "defined in model specification MS-DYN". The frame is now defined in CONVENTIONS CV-120. | MS-DYN (C1) and the ICD (I1) cite CONVENTIONS for frames; no change to METHODOLOGY (its example is illustrative). |
| A3-N02 | METHODOLOGY §8.5 | It suggests "vertical position and yaw angle" as defined terms. The conventions define *altitude* and *heading* for these. | None; requirements use altitude and heading. |
| A3-N03 | METHODOLOGY §8.5, LOW FUEL example | It states a fuel threshold in %. CV-720 stores dimensionless ratios as fractions. | FU (C2) writes the threshold parameter as a fraction; a percentage may still be shown to the crew. |
| A3-N04 | Plan §5, staging files | The plan lists `glossary_proposals.md` for each agent. A3 owns GLOSSARY.md directly, so it has no glossary proposals file. | None. |
| A3-N05 | Plan Q2 | Pitch and roll behaviour during guidance modes is still open. CV-550 and CV-970 require attitude to be stated separately in each mode. | B1 proposes the answer at G1; mode agents write attitude requirements explicitly. |
| A3-N06 | Parameter IDs | CONVENTIONS cites the proposed IDs `P-SYS-300`, `P-SYS-310`, `P-DYN-010`, `P-NAV-010` to `-050` and `P-TM-010` to `-070`. | If B2 renumbers, update the citations in CONVENTIONS. |
