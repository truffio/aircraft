# B3 — Change requests for the landing gear and ground operations (D69, D70)

**Status:** Proposed by task B3, 2026-11-05, for owner approval. None is applied.
**Against:** L0 (`L0-baseline-1` plus later CRs; source `work/A1/L0_*.md`), L1 (`AER-L1-baseline-1` plus CR-C1-01 and CR-C2-01; source `work/B1/L1_AER.md`), specs/CONOPS.md, specs/CONVENTIONS.md, specs/GLOSSARY.md and specs/FUNCTIONAL_ANALYSIS.md, at branch c1_c2, commit 63499b8.
**Decisions applied:** D37 as revised by D69, D53, D54 (revised for the gear), D56 (extended with Takeoff and Land), D67, D68, D69, D70, D71, D72.

Part 1 is the register summary in the format of `registers/CHANGE_REQUESTS.md`, ready to append. Part 2 gives each CR in full, with the exact new wording. Quoted "old" text is copied from the current file. A record's fields that are not mentioned stay as they are. Each changed requirement record gets its Version raised by one, and its Status stays Baselined. The register rows to update are in `impact_list.md` §6.

Terms in *italics* are glossary terms. The new terms are defined in `glossary_proposals.md` §1, and the changed definitions are in CR-B3-50.

## Part 1 — Register summary

| ID | Raised by | Against (requirement ID) | Requested change | Reason | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| CR-B3-01 | B3 | L0-OBJ-030 | Rationale, roll-up guidance and Source: the mode catalogue is D56 extended by D69 (Takeoff, Land). | D69 adds two modes; the G4 roll-up checks the catalogue. | Proposed | — |
| CR-B3-02 | B3 | L0-CON-060 | Rationale and roll-up guidance: a control force or moment is any force or moment other than gravity, drag and the ground reaction. | Otherwise the ground reaction would count as a control force that the effectors must produce. | Proposed | — |
| CR-B3-03 | B3 | L0-CON-090 | Rationale and roll-up guidance: ground contact includes the ground reaction on the gear while the vehicle rests on the ground. Statement unchanged. | The closed list of external effects already names ground contact; its content changes (D69). | Proposed | — |
| CR-B3-04 | B3 | L0-CON-160 | Rationale: the landing gear moves without an energy model (no electrical power, no fuel). | D69 revises D54 for the gear; the absent-systems statement must not be read against it. | Proposed | — |
| CR-B3-05 | B3 | L0-CON-290 | Rationale, roll-up guidance, Source, TBD/TBR: landing on the extended gear, rest on the ground, a landing does not end the run, a contact with the gear not extended or after fuel exhaustion is a crash. Statement unchanged. | D37 said "no landing gear"; D68, D69. | Proposed | — |
| CR-B3-06 | B3 | L0-CON-310 | Rationale: the ideal gear computes no touchdown shock; at rest on the ground the crew feels 1 g. | D69. | Proposed | — |
| CR-B3-07 | B3 | L0-ASM-110 | Rewrite the assumption: ideal gear, rest on the ground, crash conditions. | The assumption says "No landing gear … is modelled" (D69). | Proposed | — |
| CR-B3-08 | B3 | L1-AER-050 | Statement and rationale: add the ground reaction, on the ground, to the total force and moment. | Rationale says "Ground contact is not a force"; resting on the gear needs one (D69, G2 §6). | Proposed | — |
| CR-B3-09 | B3 | L1-AER-080 | Rationale: control force excludes the ground reaction. | Follows CR-B3-02. | Proposed | — |
| CR-B3-10 | B3 | L1-AER-160 | Rationale: fuel is consumed in every airborne condition, none on the ground with the effectors off. | "Fuel is consumed in every flight condition" (D69). | Proposed | — |
| CR-B3-11 | B3 | L1-AER-200 | Rationale and Source: SC-110 leg 11; ground contact after exhaustion is a crash (D68); #59 answered. | G2-F23; D68. | Proposed | — |
| CR-B3-12 | B3 | L1-AER-260 | Statement and rationale: a landing is made on the extended gear with fuel remaining; the run goes on. | D68, D69; "the TST ends the run on the event". | Proposed | — |
| CR-B3-13 | B3 | L1-AER-270 | Statement and rationale: a crash is a contact outside the envelope, with the gear not extended, or at fuel exhaustion. | Complement of CR-B3-12 (D68, D69). | Proposed | — |
| CR-B3-14 | B3 | L1-AER-280 | Rationale: the ideal gear computes no shock; gear and fuel are conditions of a landing, not of the envelope. | "the ideal landing has no gear model" (D69). | Proposed | — |
| CR-B3-15 | B3 | L1-AER-290 | Rationale: touchdown on the ideal gear adds no share; at rest the sensed acceleration is 1 g. | D69. | Proposed | — |
| CR-B3-16 | B3 | L1-AER-310, L1-AER-330 | Rationale (and -330 Parameters): the operating volume is bounded below by a height above the ground [P-SYS-210]. | TT-820: the 5 ft minimum is measured below the body (D67, D70). | Proposed | — |
| CR-B3-17 | B3 | L1-AER-360 | Statement and rationale: the hover endurance runs from a takeoff at full fuel, followed by a hold of the hover. | Runs start on the ground (D69, G2 §6 on L2-AER-FU-290). | Proposed | — |
| CR-B3-18 | B3 | L1-AER-390, L1-AER-420, L1-AER-880 | Rationale only: level attitude on the ground; the off value of the axis references; the gear position as annunciation content. | Mechanism of D69 within the closed interfaces. | Proposed | — |
| CR-B3-19 | B3 | L1-AER-430 | Statement and rationale: the landing gear command into the vehicle model, the gear state out. | The gear is in the vehicle model; the closed boundary list must carry it (D69). | Proposed | — |
| CR-B3-20 | B3 | L1-AER-450 | Rationale and Source: catalogue D56 plus Takeoff and Land (D69). | D69. | Proposed | — |
| CR-B3-21 | B3 | L1-AER-470 | Statement and rationale: also annunciate a change of the landing gear position. | The crew must see the gear before a landing (N-060); recommended, can be dropped alone. | Proposed | — |
| CR-B3-22 | B3 | L1-AER-480 | Rationale and TBD/TBR: the panel engages each mode, Takeoff and Land included (D71); #79 answered. | D71. | Proposed | — |
| CR-B3-23 | B3 | L1-AER-530, L1-AER-890 | Statements: add the height above the ground to the navigation quantities. | Go to hover, Hover, Takeoff and Land guide on it (D70, CV-400). | Proposed | — |
| CR-B3-24 | B3 | L1-AER-580 | Rationale and TBD/TBR: #59 answered by D68; the C5 annunciation item remains. | G2-F13; D68. | Proposed | — |
| CR-B3-25 | B3 | L1-AER-640 | Statement: add the height above the ground, the gear state and the landing and crash events to the closed list. | D69. | Proposed | — |
| CR-B3-26 | B3 | L1-AER-660 | Statement, rationale, TBD/TBR: add the landing gear position to the initial condition; runs start on the ground. | "every scenario starts airborne" (D69). | Proposed | — |
| CR-B3-27 | B3 | L1-AER-720 | Statement: MS-DYN states the landing gear and ground contact model. | D69. | Proposed | — |
| CR-B3-28 | B3 | L1 (new records) | Add L1-AER-900 to -970 (`work/B3/L1_new_records.md`). | Gear, ground rest, effectors off, no fuel use, ground start, takeoff and landing capability (D69). | Proposed | — |
| CR-B3-29 | B3 | CONOPS status, §1, §1.1, §1.2 | Scope: takeoff and landing covered; labels TAKEOFF, LAND; decisions D1 to D72. | D69. | Proposed | — |
| CR-B3-30 | B3 | CONOPS §3 N-310, N-370; new N-450 | Needs: initial gear state; a landing does not end a run; new need for ground operations. | D69. | Proposed | — |
| CR-B3-31 | B3 | CONOPS §4.2 | Altitude, height above the ground, ground, operating volume. | "Each run starts with the vehicle airborne. There is no take-off." (D69, D70). | Proposed | — |
| CR-B3-32 | B3 | CONOPS §4.3, §4.4 | Panel: TAKEOFF and LAND engage commands, gear annunciation; mode groups, starting modes, arming, heading, catalogue rows. | D69, D70, D71. | Proposed | — |
| CR-B3-33 | B3 | CONOPS §4.5, §4.6, §5 | Fuel on the ground; run end on a crash only; ground start and airborne test starts. | D68, D69, B3-Q1. | Proposed | — |
| CR-B3-34 | B3 | CONOPS SC-100, SC-110, SC-200 | SC-100: #88 answered, from-below variation. SC-110: ground start, takeoff, landing, second takeoff, crash at the end. SC-200: run ends on a crash. | D68, D69, D70. | Proposed | — |
| CR-B3-35 | B3 | CONOPS new SC-130; §7.2, §8, §9 | New scenario: take off, hover, land and rest. Open questions, traceability and parameter tables updated. | D69 needs a scenario of its own. | Proposed | — |
| CR-B3-36 | B3 | CONVENTIONS CV-160, CV-420, CV-440, new CV-400, header | Define the height above the ground at the lowest point of the body; ground contact at the lowest point of the vehicle. | TT-820; D70 "measured below the body". | Proposed | — |
| CR-B3-37 | B3 | GLOSSARY (changed terms, list in Part 2) | Changed definitions as in `glossary_proposals.md` §2. 11 new terms in §1 (no CR needed). | Fixed definitions contradict D68 to D72. | Proposed | — |
| CR-B3-38 | B3 | FUNCTIONAL_ANALYSIS §2 (F-AER-01 to -03, -07 to -09, -12 to -14, new F-AER-15) | Function list for the gear, the ground reaction, the effectors off and the height above the ground. | D69. | Proposed | — |
| CR-B3-39 | B3 | FUNCTIONAL_ANALYSIS §3, §4 | Interfaces I-03, I-04, I-08, I-21, I-41; new I-43 to I-46; matrices; loop flow and frame sequence. | D69. | Proposed | — |
| CR-B3-40 | B3 | FUNCTIONAL_ANALYSIS §5, §6 | Vehicle-model boundary; allocation of functions and of the new L1 records. | D69. | Proposed | — |
| CR-B3-41 | B3 | FUNCTIONAL_ANALYSIS §7, §8 | Budgets: ground and liftoff in §7.2, hover endurance from takeoff in §7.3; L0 → L1 coverage. | D69. | Proposed | — |

**Counts:** L0 7 (CR-B3-01 to -07, seven records); L1 21 (CR-B3-08 to -28: 24 changed records and 8 new records); CONOPS 7 (CR-B3-29 to -35); CONVENTIONS 1 (CR-B3-36: three conventions changed, one new); GLOSSARY 1 (CR-B3-37: 26 changed definitions); FUNCTIONAL_ANALYSIS 4 (CR-B3-38 to -41). Total 41.

## Part 2 — Change requests in full

### L0

#### CR-B3-01 — L0-OBJ-030 (mode catalogue)

- **Rationale**, old: "The mode catalogue is plan decision D56, which replaced D3 (CR-B1-08); direct manual flight controls are excluded (L0-CON-180). The modes themselves are defined at L2 (D33). Children must show (D41): (Inspection) each mode of the mode catalogue (D56) is covered by a requirement in the Aeronef branch that traces to this objective."
  New: "The mode catalogue is plan decision D56, which replaced D3 (CR-B1-08), with the Takeoff and Land modes added by D69 (CR-B3-01); direct manual flight controls are excluded (L0-CON-180). The modes themselves are defined at L2 (D33). Children must show (D41): (Inspection) each mode of the mode catalogue (D56, D69) is covered by a requirement in the Aeronef branch that traces to this objective."
- **Source:** "… AIRCRAFT_REQUIREMENTS_PLAN.md §9 D56" → "… AIRCRAFT_REQUIREMENTS_PLAN.md §9 D56, D69".
- **Version:** 3 → 4.
- **Reason:** D69 adds two modes acting on both axes. Without this change, the G4 roll-up would check the catalogue without them.
- **Recommendation:** approve. The statement stays black-box (D33).

#### CR-B3-02 — L0-CON-060 (control force definition)

- **Rationale**, old: "A control force or moment (glossary) is any force or moment other than gravity and aerodynamic drag. Children must show (D41): (Inspection) the model specification identifies the force effectors as the only source of force and moment other than gravity and aerodynamic drag."
  New: "A control force or moment (glossary) is any force or moment other than gravity, aerodynamic drag and the ground reaction that holds the Aeronef at rest on its landing gear (D69, L0-CON-090; CR-B3-02). Children must show (D41): (Inspection) the model specification identifies the force effectors as the only source of force and moment other than gravity, aerodynamic drag and the ground reaction."
- **Version:** 2 → 3.
- **Reason:** with a ground reaction in the model, the current definition would make it a control force, which the effectors alone may produce (L1-AER-080).
- **Recommendation:** approve.

#### CR-B3-03 — L0-CON-090 (external effects)

- **Statement:** unchanged ("… gravity, aerodynamic drag on the air-relative velocity and ground contact").
- **Rationale**, old: "Ground contact is the ideal landing of L0-CON-290 (D37). Children must show (D41): (Inspection) the model specification defines gravity and aerodynamic drag on the vehicle velocity relative to the air mass, including wind, as the only external forces and moments, and ground contact (L0-CON-290) as the only other external effect."
  New: "Ground contact is the ideal landing of L0-CON-290 (D37, revised by D69): the contact of the airborne vehicle with the ground and, while the Aeronef rests on the ground, the ground reaction that holds it at rest on its landing gear (CR-B3-03). Children must show (D41): (Inspection) the model specification defines gravity and aerodynamic drag on the vehicle velocity relative to the air mass, including wind, as the only external forces and moments in flight, and ground contact (L0-CON-290), with the ground reaction while the Aeronef rests on the ground, as the only other external effect."
- **Version:** 3 → 4.
- **Reason:** G2 §6: "resting on the gear needs a ground reaction … This also changes the closed list of L1-AER-050 and L0-CON-090." The L0 statement already names ground contact, so only its content changes.
- **Recommendation:** approve. No statement change is needed at L0, which keeps the aircraft a black box.

#### CR-B3-04 — L0-CON-160 (absent systems, editorial)

- **Rationale:** append "The landing gear (D69, which revises D54 for the gear) moves without an energy model: its movement uses no electrical power and no fuel (CR-B3-04)."
- **Version:** 3 → 4.
- **Reason:** D54 made the absence of systems a matter of writing no requirement for them. The gear is now a system the Aeronef has. This sentence keeps the electrical scope statement from being read against it.
- **Recommendation:** approve (editorial).

#### CR-B3-05 — L0-CON-290 (ground contact)

- **Statement:** unchanged ("The Aeronef project shall model ground contact of the Aeronef as a landing within the landing envelope and as a crash outside it.").
- **Rationale**, new (replaces the whole field):
  "G0 owner review (2026-10-25), decision D37: landing has to be modelled. Contact with the ground within a landing envelope is a successful landing; contact outside it is a crash. The owner revised D37 with D69 (2026-11-05): the Aeronef has an extendable landing gear. A landing is therefore a contact of the extended gear with the ground within the envelope. After it the Aeronef rests on the ground, stationary on its gear, until it takes off again, and a landing does not end the run. The gear is ideal: it has no spring, damping, bounce, sliding or tipping (L0-ASM-110). A contact with the gear not extended, or after fuel exhaustion (D68), is a crash whatever the speeds, and a crash ends the run. The envelope is two limits at the contact sample, on the vertical speed magnitude and on the horizontal speed. There is no acceleration limit, because the ideal gear computes no touchdown shock (D53, CR-B1-07). The limits are parameters set at a lower level (CR-B3-05). Children must show (D41): (Inspection) the model specification defines the landing gear, ground contact at the lowest point of the vehicle (the extended gear, or the body when the gear is not extended), a landing envelope of vertical and horizontal speed limits at the contact sample, the landing and crash outcomes, and the rest on the gear after a landing."
- **Source:** "Owner review at G0, 2026-10-25 (D8, D37, D53)" → "Owner review at G0, 2026-10-25 (D8, D37, D53); owner decisions D68, D69 (2026-11-05)".
- **TBD/TBR:** "Landing envelope limits TBD (lower level), Martin, closes at G2" → "Landing envelope limits TBR (P-SYS-500, P-SYS-510, TT-090), Martin, G2".
- **Version:** 3 → 4.
- **Reason:** "There is no landing gear, bounce or friction model" contradicts D69. "Fuel exhaustion … ground contact is a crash" is D68.
- **Recommendation:** approve. The statement can stay because "landing" and "crash" keep their L0 meaning, and the gear details stay out of the L0 statement (D33). Owner question B3-Q3 confirms the two crash conditions.

#### CR-B3-06 — L0-CON-310 (crew acceleration)

- **Rationale**, old: "The limit applies while the Aeronef is airborne: the ideal landing has no contact dynamics and computes no touchdown shock (L0-CON-290), and the vertical speed limit of the landing envelope stands in for the impact (D53, CR-B1-07)."
  New: "The limit applies while the Aeronef is airborne: the ideal landing gear has no contact dynamics and computes no touchdown shock (L0-CON-290, D69), and the vertical speed limit of the landing envelope stands in for the impact (D53, CR-B1-07). At rest on the ground the crew feels the ground reaction, 1 g, which is within the limit (CR-B3-06)."
- **Version:** 6 → 7.
- **Reason:** D69; *Airborne* is redefined (CR-B3-37).
- **Recommendation:** approve.

#### CR-B3-07 — L0-ASM-110 (ideal landing)

- **Assumption**, new: "Ground contact is ideal, and so is the landing gear: it has no spring, damping, bounce, friction, sliding or tipping model and no mass of its own. A contact of the extended gear with the ground within the landing envelope (limits on the vertical and horizontal speed at the contact sample, D53), with fuel remaining, is a successful landing. After it the vehicle comes to rest on the gear, stationary and at level attitude, and stays there until it takes off. Any other ground contact, including a contact with the gear not extended or after fuel exhaustion (D68), is a crash that ends the run."
- **Rationale**, new: "Owner decisions D8 and D37: the ground is at altitude zero on a flat Earth, and a landing model is required. The owner added the landing gear and ground operations on 2026-11-05 (D69, revising D37, D53 and D54 for the gear; CR-B3-07): runs start on the ground, and the Aeronef takes off and lands. An ideal gear reduces the landing to one envelope check and the rest on the ground to a static equilibrium. The envelope limits are parameters, set at a lower level. Revised by the owner at G0, 2026-10-25. Envelope quantities set by the owner at G1 (D53, CR-B1-07): no acceleration limit, because no touchdown shock is computed."
- **Affects**, new: "L0-CON-090 (ground reaction), L0-CON-290, L0-CON-310; model specification (landing gear and ground contact); TST run termination conditions (a crash ends the run, a landing does not); fuel-exhaustion reference mission; CONVENTIONS CV-400, CV-420; CONOPS §4.2"
- **Reason:** "No landing gear, bounce, friction or ground handling is modelled" contradicts D69.
- **Recommendation:** approve (the owner reviews every assumption, D29).

### L1

#### CR-B3-08 — L1-AER-050 (total force and moment)

- **Statement**, new: "The Aeronef shall compute the total force and moment on the vehicle as the sum of gravity, aerodynamic drag, the control forces and control moments and, while the Aeronef is on the ground, the ground reaction, in accordance with MS-DYN."
- **Rationale**, new: "L0-CON-090 limits the external effects to gravity, drag on the air-relative velocity and ground contact; L0-CON-060 makes the effectors the only source of control force and moment. Ground contact acts as a force only while the Aeronef rests on its landing gear on the ground: there the ground reaction of the MS-DYN ground contact model holds it at rest (L1-AER-920, D69). A ground contact of the airborne vehicle is classified as a landing or a crash (L1-AER-260 to -280; L0-ASM-110) and computes no touchdown shock (D53). Consumed fuel adds no force (L0-ASM-090). Children must show (D58): (Inspection) MS-DYN lists these four contributions and no other, with the ground reaction only on the ground; (Analysis) the free-fall and terminal-velocity checks of L1-AER-010 pass, and at rest on the ground the total force and the total moment are zero.
  Sufficiency: with L1-AER-060 (gravity), -070 (drag) and -920 (ground reaction), this record closes the list of forces and moments, which covers the force part of L0-CON-090 and the model side of L0-CON-060."
- **Source:** add "D69".
- **Version:** 1 → 2.
- **Reason:** "Ground contact is not a force: it ends the run" contradicts D69 (G2 §6).
- **Recommendation:** approve.

#### CR-B3-09 — L1-AER-080 (effectors as the only source)

- **Rationale**, old: "A control force or moment is any force or moment other than gravity and drag (glossary)." → new: "A control force or moment is any force or moment other than gravity, drag and the ground reaction (glossary, CR-B3-02)." Old: "Sufficiency: with L1-AER-050, which makes gravity and drag the only other contributions, …" → new: "Sufficiency: with L1-AER-050, which makes gravity, drag and, on the ground, the ground reaction the only other contributions, …".
- **Version:** 1 → 2.
- **Reason / recommendation:** follows CR-B3-02; approve.

#### CR-B3-10 — L1-AER-160 (fuel mass flow)

- **Rationale**, old: "Because the effectors counter gravity, fuel is consumed in every flight condition, hover included (CONOPS §4.5)." → new: "Because the effectors counter gravity, fuel is consumed in every airborne condition, hover included (CONOPS §4.5). On the ground, with the effectors off, no fuel is consumed (D69, L1-AER-930, -940)."
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-11 — L1-AER-200 (zero output at exhaustion)

- **Rationale**, old: "Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070): the vehicle then moves under gravity and drag alone and keeps its angular rate (CONOPS SC-110 leg 10). What the autoflight modes do at exhaustion is open at L2 (#59)."
  New: "Fuel exhaustion is nominal behaviour, not a failure (L0-ASM-070): the vehicle then moves under gravity and drag alone and keeps its angular rate (CONOPS SC-110 leg 11), and its ground contact is a crash (D68, L1-AER-270). What autoflight annunciates after exhaustion is set at L2 (C5, D68)."
- **Source:** "N-150; CONOPS §4.5, SC-110" → "N-150; CONOPS §4.5, SC-110; D68".
- **Version:** 1 → 2.
- **Reason:** G2-F23 (wrong leg number); D68 answered #59.
- **Recommendation:** approve.

#### CR-B3-12 — L1-AER-260 (landing)

- **Statement**, new: "When the Aeronef makes ground contact on its extended landing gear within the landing envelope with fuel remaining, the Aeronef shall report a landing in its operational data."
- **Rationale**, new: "Ideal landing on the gear (D37 revised by D69, L0-CON-290, L0-ASM-110): a contact of the extended gear within the envelope (L1-AER-280) is a landing. The gear is ideal. The vehicle comes to rest on it at the contact step and stays there until liftoff (L1-AER-920), and the run goes on. A contact after fuel exhaustion is a crash (D68), so fuel remaining is part of the condition. Children must show (D58): (Test) a descent to the ground on the extended gear, within the envelope and with fuel remaining, produces one landing event at the contact sample and no crash event.
  Sufficiency: with L1-AER-270 (crash), -280 (envelope), -900 (gear) and -920 (rest on the ground), this record defines ground contact, the envelope and both outcomes, as L0-CON-290 requires."
- **Source:** "D8, D37; CONOPS §4.2, §4.6" → "D8, D37, D68, D69; CONOPS §4.2, §4.6, SC-130".
- **Version:** 1 → 2.
- **Reason:** "There is no gear, bounce or friction model; the TST ends the run on the event" contradicts D69.
- **Recommendation:** approve, subject to B3-Q3.

#### CR-B3-13 — L1-AER-270 (crash)

- **Statement**, new: "When the Aeronef makes a ground contact that is outside the landing envelope, or with its landing gear not extended, or at fuel exhaustion, the Aeronef shall report a crash in its operational data."
- **Rationale**, new: "A ground contact that is not a landing (L1-AER-260) is a crash, which ends the run (D37, D68, D69, L0-CON-290). The three conditions are the complement of those of L1-AER-260, so the two records partition the contacts (D30). They are: a contact outside the speed envelope; a contact with the gear retracted or in transit, so that the body or a moving gear meets the ground; and a contact after fuel exhaustion (D68). The reference mission ends this way after fuel exhaustion (SC-110). Children must show (D58): (Test) each of the following produces one crash event at the contact sample: a free fall to the ground from fuel exhaustion, a contact just outside each speed limit, and a contact with the gear retracted within the speed limits.
  Sufficiency: see L1-AER-260."
- **Source:** "D37; CONOPS SC-110" → "D37, D68, D69; CONOPS SC-110".
- **Version:** 1 → 2.
- **Recommendation:** approve, subject to B3-Q3.

#### CR-B3-14 — L1-AER-280 (envelope)

- **Statement:** unchanged.
- **Rationale**, old: "There is no acceleration limit: the ideal landing has no gear model, so no touchdown shock is computed, and the vertical speed limit stands in for the impact (D53, #100)."
  New: "There is no acceleration limit: the ideal landing gear computes no touchdown shock, and the vertical speed limit stands in for the impact (D53, D69, #100). The gear position and the fuel are conditions of a landing, not part of the envelope (L1-AER-260, -270)."
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-15 — L1-AER-290 (crew g-limit)

- **Rationale**, old: "The ideal landing computes no touchdown shock (D53), so contact adds no further share." → new: "The ideal landing gear computes no touchdown shock (D53, D69), so contact adds no further share. At rest on the ground the sensed acceleration is that of the ground reaction, [P-DYN-010] upward, which is within the limit (L1-AER-920)."
- **Statement:** unchanged ("While the Aeronef is airborne …"); *Airborne* is redefined (CR-B3-37).
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-16 — L1-AER-310, L1-AER-330 (lower bound of the operating volume)

- **L1-AER-310 rationale**, old: "The operating volume is bounded by [P-SYS-210], [P-SYS-200] and [P-SYS-220]" → new: "The operating volume is bounded below by the minimum operating height above the ground [P-SYS-210] (CV-400), above by the altitude [P-SYS-200] and horizontally by [P-SYS-220]". Old children-must-show: "in level flight at the minimum and the maximum operating altitude" → new: "in level flight at the lowest altitude of the operating volume and at [P-SYS-200]". Version 1 → 2.
- **L1-AER-330 rationale**, old: "the selectable altitude is bounded below by [P-SYS-210] (L2, C8)" → new: "the selectable altitude is bounded below by the altitude at which the height above the ground is [P-SYS-210] at level attitude, that is [P-SYS-210] plus half of [P-DYN-030] (CV-400; L2, C8)". **Parameters:** add P-DYN-030. **TBD/TBR:** add "P-DYN-030 value TBR (TT-740)". Version 1 → 2.
- **Reason:** TT-820. D67 sets the minimum at the hover height, and D70 measures the hover height below the body. As a CG altitude, 1.524 m would place the body 0.48 m below the ground.
- **Recommendation:** approve with CR-B3-36 and the P-SYS-210 change in `param_proposals.md` §2.

#### CR-B3-17 — L1-AER-360 (hover endurance)

- **Statement**, new: "When autoflight takes off from the ground with an initial fuel mass of [P-FU-010] and then holds the horizontal position and the hover height with no wind applied, the Aeronef shall stay airborne with fuel remaining for at least [P-SYS-280] from the start of the takeoff."
- **Rationale**, new: "Fuel budget (FUNCTIONAL_ANALYSIS §7.3). Runs start on the ground (D69), so the endurance from full fuel begins with a takeoff: a climb to the hover height and the gear retraction, followed by Hover (D69). Holding the horizontal position and the hover height in still air is the condition in which the effectors only counter gravity. It therefore sets the endurance at full fuel and maximum mass (CONOPS SC-110 variation). With no wind and no motion there is no drag. With a consumption proportional to force, [P-FU-010] must be at least [P-FU-030] times the exponential of the product of the translational consumption coefficient [P-FU-040], [P-DYN-010] and [P-SYS-280], minus one (L2-AER-FU-290). The fuel of the takeoff is a small part of the margin [P-FU-100]: it covers a climb of [P-AF-210] minus [P-DYN-040] at [P-AF-240] and the gear retraction. Stationary with Altitude hold, which this record also covered before D69, now needs a climb first and is not the endurance case. Children must show (D58): (Test) from a ground start at full fuel, the time from the takeoff to fuel exhaustion while autoflight holds the horizontal position and the hover height in still air is at least [P-SYS-280].
  Sufficiency: the finite supply of L0-CON-100 must still allow useful missions. This record turns that into a measurable endurance, and with L1-AER-310 to -350 and -960 it completes the envelope for L0-OBJ-030."
- **Parameters:** "P-FU-010, P-SYS-280, P-FU-030, P-FU-040, P-DYN-010" → add "P-FU-100, P-AF-210, P-DYN-040, P-AF-240".
- **TBD/TBR**, new: "P-SYS-280 value TBR (TT-800), P-FU-010, P-FU-030, P-FU-040, P-FU-100 values TBR (TT-110, TT-120, TT-790), Martin, G2 (I1)". This also refreshes the stale "TBD" copies (G2 §7).
- **Source:** add "D69".
- **Version:** 1 → 2.
- **Reason:** G2 §6: "the run now begins with a Takeoff, so its fuel and time count against L1-AER-360 'from an initial fuel mass of [P-FU-010]', while the closed form starts at the hold."
- **Recommendation:** approve. The alternative, an airborne start in Hover at full fuel, depends on B3-Q1 and does not test the operational case.

#### CR-B3-18 — L1-AER-390, L1-AER-420, L1-AER-880 (rationale only)

- **L1-AER-390:** append to the rationale: "On the ground the landing gear holds the attitude level (L1-AER-920), so the record needs no on-ground case." Version 1 → 2.
- **L1-AER-420:** after "flight control receives no mode information, so no control law can depend on the mode logic (D15, D33).", insert: "On the ground the axis references take an off value, with which flight control commands zero effector output (the effectors off, D69, L1-AER-930); the off value carries no mode information." Version 1 → 2.
- **L1-AER-880:** old "Autoflight gives the annunciation content (which modes, which targets, D55)" → new "Autoflight gives the annunciation content (which modes, which targets and the landing gear position, D55, D69; L1-AER-470)". Version 1 → 2.
- **Reason:** D69 needs an effectors-off command and a gear annunciation path. Using the existing closed interfaces keeps D15 (FC is unaware of the modes) and avoids a new link from DYN to FCP.
- **Recommendation:** approve. C4 and C5 confirm the off value at L2. If C4 prefers FC to read the gear state instead, only L1-AER-420 changes back.

#### CR-B3-19 — L1-AER-430 (vehicle-model boundary)

- **Statement**, new: "The Aeronef shall exchange data between its vehicle model and its flight software only as effector commands and the landing gear command into the vehicle model and as vehicle state, gear state, mass properties and fuel state out of it."
- **Rationale:** after "The list is closed.", insert: "The landing gear is part of the vehicle model (DYN, D69). Autoflight commands it, retracting it in Takeoff and extending it in Land, and reads the gear state: the gear position and whether the vehicle is on the ground (glossary). The gear state is the perfect-knowledge counterpart of a weight-on-gear signal (L0-ASM-010)." The children-must-show text is unchanged.
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-20 — L1-AER-450 (guidance through the catalogue)

- **Rationale**, old: "The catalogue is plan decision D56: independent horizontal modes (Stationary, Heading) and vertical modes (Altitude hold, Go to altitude, Vertical speed), plus Go to hover and Hover, which govern both axes."
  New: "The catalogue is plan decision D56, extended by D69: independent horizontal modes (Stationary, Heading) and vertical modes (Altitude hold, Go to altitude, Vertical speed), plus Go to hover, Hover, Takeoff and Land, which govern both axes."
  After "Sufficiency: with … the envelope L1-AER-310 to -360", add ", and the takeoff and landing capabilities L1-AER-960 and -970".
- **Source:** "N-050, N-190; D33, D56" → "N-050, N-190; D33, D56, D69".
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-21 — L1-AER-470 (annunciation)

- **Statement**, new: "When the mode state, a target or the landing gear position changes, the Aeronef shall annunciate the new mode state, target or gear position to the crew within [P-SYS-470]."
- **Rationale:** after the first sentence, add: "The landing gear position (extended, retracted, in transit) is annunciated too, because a landing needs the gear extended (L1-AER-260) and the crew needs to know what the vehicle will do next (N-060). AF passes it to FCP as annunciation content, from the gear state (L1-AER-430, -880)."
- **Version:** 1 → 2.
- **Reason:** D69 makes the gear position a condition of a landing. The crew sees it as on an airliner.
- **Recommendation:** approve. This CR is the one optional item. If it is rejected, drop it together with the gear wording of CR-B3-18 (L1-AER-880) and the annunciation line of CR-B3-32; nothing else depends on it.

#### CR-B3-22 — L1-AER-480 (crew selections)

- **Rationale**, old: "The selections are those of the flight control panel: the modes and the heading, horizontal speed, target altitude and vertical speed selectors (D56). The panel is its own subsystem, FCP (D55, #80.3); its detailed content is #79."
  New: "The selections are those of the flight control panel: a button that engages each mode, Takeoff and Land included, and the heading, horizontal speed, target altitude and vertical speed selectors (D56, D69, D71). The panel is its own subsystem, FCP (D55, #80.3); its content is set by D71 (#79)."
- **TBD/TBR:** "Flight control panel content (#79), Martin, G2 (C8)" → "—" (TT-560 closes, D71).
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-23 — L1-AER-530, L1-AER-890 (height above the ground)

- **L1-AER-530 statement**, new: "The Aeronef shall compute, at each control frame, its altitude, height above the ground, horizontal speed, vertical speed, heading and track from its vehicle state, as CONVENTIONS CV-400 to CV-550 define them." **Rationale:** add "The height above the ground (CV-400, D70) is the guidance quantity of Go to hover, Hover, Takeoff and Land; it uses the body geometry [P-DYN-020] and [P-DYN-030]." **Source:** "N-190; CV-430 to CV-580" → "N-190; CV-400 to CV-580; D70". Version 1 → 2.
- **L1-AER-890 statement**, new: "The Aeronef shall pass its altitude, height above the ground, horizontal speed, vertical speed, heading and track, with their validity, from navigation to autoflight through the one interface defined in ICD-NAV-AF." **Source:** "CV-430 to CV-580" → "CV-400 to CV-580". Version 1 → 2.
- **Reason:** TT-820. The hover height is measured below the body (D70), and plan C6 already lists "height above the ground" for NAV.
- **Recommendation:** approve.

#### CR-B3-24 — L1-AER-580 (fuel exhaustion annunciation)

- **Rationale**, old: "the effectors stop (L1-AER-200). What the modes do then is L2 (#59)." → new: "the effectors stop (L1-AER-200), and the ground contact that follows is a crash (D68). What autoflight annunciates then is set at L2 (C5, D68)."
- **TBD/TBR:** "Autoflight state after fuel exhaustion (#59), Martin, G2 (C2, C5)" → "—". The open item becomes the C5 annunciation item of TT-580, rewritten (`impact_list.md` §6).
- **Version:** 1 → 2.
- **Reason:** D68 answered #59 (G2-F13, G2 §7).
- **Recommendation:** approve.

#### CR-B3-25 — L1-AER-640 (vehicle responses in the operational data)

- **Statement**, new: "The Aeronef shall record in its operational data, at each output sample, its vehicle state, its altitude, height above the ground, horizontal speed, vertical speed, heading and track, its sensed acceleration at the centre of gravity, its vehicle mass, its remaining fuel mass, its gear state and each landing and crash event."
- **Rationale:** add "The gear state and the height above the ground let the TST assess the takeoffs, landings and rests on the ground (L1-AER-920 to -970)."
- **Version:** 1 → 2.
- **Recommendation:** approve.

#### CR-B3-26 — L1-AER-660 (initial condition)

- **Statement**, new: "The Aeronef shall accept from the TST, at the start of each run, an initial condition of position, velocity, attitude, body rates, landing gear position, fuel mass, autoflight mode state and targets."
- **Rationale**, old: "The TST sets the whole starting state of a run (N-310, CONOPS §4.6), and every scenario starts airborne (CONOPS §4.2). The mode state is a data item here; which mode states are valid at start is L2 (#60)."
  New: "The TST sets the whole starting state of a run (N-310, CONOPS §4.6). A run starts on the ground, at rest on its extended landing gear with the effectors off (D69, L1-AER-950). A test procedure may also start a run airborne, with the gear retracted, for example for a credibility check or a test at altitude (owner question B3-Q1). The mode state is a data item here; which mode states are valid at start is L2 (#60, C5), and on the ground the recommendation is that no mode is active." The rest is unchanged. **Children must show**, new: "(Test) the first output sample of a run reports the initial condition it was given, for a ground start and for an airborne start."
- **Source:** add "D69".
- **TBD/TBR**, new: "Valid initial mode states (#60), Martin, G2 (C5); airborne initial conditions (B3-Q1), Martin, B3 approval".
- **Version:** 1 → 2.
- **Recommendation:** approve. If the answer to B3-Q1 is "no", delete the airborne sentence and the "airborne start" test case.

#### CR-B3-27 — L1-AER-720 (MS-DYN content)

- **Statement**, new: "The Aeronef shall have a baselined model specification, MS-DYN, that states its equations of motion, its gravity, drag and wind model, its landing gear and ground contact model, and its effector, fuel and mass-properties models."
- **Version:** 1 → 2.
- **Recommendation:** approve. The list is closed, so the gear model must be named.

#### CR-B3-28 — New L1 records L1-AER-900 to -970

- **Requested change:** add the eight records of `work/B3/L1_new_records.md` to `work/B1/L1_AER.md`, after L1-AER-890:

| ID | Type | Statement (short) | Parents | Allocated to |
| --- | --- | --- | --- | --- |
| L1-AER-900 | Constraint | Retractable landing gear, contact points [P-DYN-040] below the body | L0-CON-290, L0-CON-130 | DYN |
| L1-AER-910 | Functional | Gear reaches the commanded position within [P-DYN-050] | L0-CON-290, L0-OBJ-030 | DYN, AF |
| L1-AER-920 | Model fidelity | On the ground: at rest on the extended gear under the ground reaction | L0-CON-090, L0-CON-290 | DYN |
| L1-AER-930 | Functional | On the ground, not taking off: zero control force and moment after [P-SYS-480] | L0-CON-100, L0-OBJ-030 | AF, FC, EF |
| L1-AER-940 | Model fidelity | Zero fuel mass flow at zero control force and moment | L0-CON-120, L0-CON-100 | FU |
| L1-AER-950 | Functional | Ground start: at rest on the extended gear, level, effectors off | L0-OBJ-010, L0-OBJ-030 | DYN, AF, FC |
| L1-AER-960 | Performance | Takeoff reaches the hover height, gear retracted, position held, wind up to [P-SYS-580] | L0-OBJ-030 | AF, FC, EF |
| L1-AER-970 | Performance | Landing from the hover in the wind envelope is a landing | L0-OBJ-030, L0-CON-290 | AF, FC, EF |

- **Reason:** D69 gives the Aeronef behaviours that no L1 record covers: the gear, the rest on the ground, the effectors off, no fuel use, the ground start, the takeoff and the landing.
- **Recommendation:** approve. L1-AER-960 depends on B3-Q2. Without a wind limit, its wind clause becomes "within the wind envelope", and the drag step at liftoff would break L1-AER-300 at dry mass (`issues.md` N-05).

### CONOPS

#### CR-B3-29 — Status, §1, §1.1, §1.2

- **Status line:** append "Landing gear, ground start, Takeoff and Land added (D68 to D71, CR-B3-29 to -35, 2026-11-05)."
- **§1, third bullet**, old "nominal scenarios (`SC-nnn`) that cover the autoflight mode catalogue (AIRCRAFT_REQUIREMENTS_PLAN.md §9, D56), a reference mission to fuel exhaustion, …" → new "nominal scenarios (`SC-nnn`) that cover the autoflight mode catalogue (AIRCRAFT_REQUIREMENTS_PLAN.md §9, D56, with Takeoff and Land added by D69), a reference mission from the ground to fuel exhaustion, …".
- **§1, "Not covered"**, old "Take-off and ground operations. Landing is covered only as an ideal landing (Section 4.2, D37)." → new "Movement on the ground (taxiing): the vehicle is stationary on the ground. Takeoff and landing are covered with an ideal landing gear (Section 4.2, D37, D69)."
- **§1.1, last bullet:** the label list becomes "(STAT, HDG, ALT, GO ALT, V/S, GO HOVER, HOVER, TAKEOFF, LAND)".
- **§1.2:** "Decisions D1 to D57 (§9)" → "Decisions D1 to D72 (§9)".

#### CR-B3-30 — Needs N-310, N-370 and new N-450

- **N-310**, stakeholder words: "I need to set up the whole starting state: position, velocity, attitude, fuel, landing gear, modes and targets." Meaning: "The Aeronef accepts a complete initial condition at the start of a run, on the ground (D69) or, for a test, airborne, including the active and armed modes and their targets."
- **N-370**, meaning: "Each run has defined end conditions (Section 4.6). A crash ends a run; a landing does not."
- **New row**: | N-450 | SH-01 | "I want the craft to sit on the ground with everything off, take off from there, and land again, without burning fuel while it waits." | The Aeronef rests on an extendable landing gear with its effectors off and no fuel use. Runs start there, and it takes off and lands under autoflight (D69). |

#### CR-B3-31 — §4.2 Operating environment

- **Altitude bullet**, new: "**Altitude** is the height of the centre of gravity above the ground plane, positive up (CV-430). The ground plane is at zero altitude. The **height above the ground** is the height of the lowest point of the body above the ground plane (CV-400). The hover height `[P-AF-210]` and the minimum operating height `[P-SYS-210]` are heights above the ground (D67, D70). At level attitude the height above the ground is the altitude minus half the body diameter `[P-DYN-030]`. On the ground, on the extended gear, it equals the gear length `[P-DYN-040]`."
- **Ground bullet**, new: "**Ground.** The ground plane is at altitude zero, with no terrain (D8). The Aeronef has an extendable landing gear (D69). It rests on the ground on the extended gear, stationary and at level attitude, with the effectors off and no fuel consumption. A contact of the extended gear with the ground within the landing envelope (limits on the vertical and horizontal speed at contact, D53), with fuel remaining, is a landing: the vehicle comes to rest and the run goes on. Any other ground contact is a crash that ends the run (L0-CON-290): outside the envelope, with the gear not extended, or after fuel exhaustion (D68). Each run starts on the ground (D69). Section 5 covers test runs that start airborne."
- **Operating volume bullet**, new: "**Operating volume.** Nominal flight takes place between a minimum operating height above the ground `[P-SYS-210]` and a maximum operating altitude `[P-SYS-200]`, within a horizontal radius `[P-SYS-220]` of the local frame origin. Takeoff and Land fly between the ground and the hover height."
- **Definitions list:** add "- **Height above the ground:** the height of the lowest point of the body above the ground plane (CV-400)." Cite "CV-400" in the lead-in list "(fixed in the conventions: …)".

#### CR-B3-32 — §4.3 Crew and §4.4 Autoflight operating concept

- **§4.3 selection table**, last row: "Mode engage commands: STAT, HDG, ALT, GO ALT, V/S, GO HOVER, TAKEOFF, LAND (D71)".
- **§4.3 annunciations**, new: "**Annunciations** show the active horizontal and vertical modes, the armed mode, the selected targets and the landing gear position (extended, retracted or in transit) (Section 4.4)." (Drop the gear position if CR-B3-21 is rejected.)
- **§4.4 Mode groups**, last sentence, new: "**Go to hover**, **Hover**, **Takeoff** and **Land** are the only modes that govern both axes: while one of them is active, it replaces both the horizontal and the vertical mode."
- **§4.4 Starting modes**, new: "**Starting modes.** A run starts on the ground with the effectors off and, as recommended to C5, no mode active (D69, #60). Takeoff is the mode engaged from there. A test run that starts airborne (Section 5) starts with the modes and targets of its initial condition."
- **§4.4 Armed and active**, replace the last sentence: "Two modes arm others. **Altitude hold** arms with Go to altitude and with Vertical speed, and captures the selected altitude. **Hover** arms with Go to hover and with Takeoff, and engages once the vehicle is stationary at the hover height `[P-AF-210]`; after a Takeoff, it engages once the gear is retracted (C5 confirms)."
- **§4.4 Attitude, second heading bullet**, new: "in Stationary, Go to hover, Hover, Takeoff and Land, the heading is held at its value when the mode became active."
- **§4.4 catalogue**, Go to hover row, "What it does": "From whatever the vehicle is flying, brings it to zero velocity on all axes at the hover height `[P-AF-210]`, descending from above or climbing from below (D70); arms Hover". Scenarios: add SC-130.
- **§4.4 catalogue**, Hover row, Scenarios: add SC-130.
- **§4.4 catalogue**, new rows:
  | Takeoff | Both | None | Engaged on the ground: switches the effectors on, climbs vertically at `[P-AF-240]` to the hover height `[P-AF-210]` over its ground position, retracts the gear and hands over to Hover (D69) | — / TAKEOFF (HOVER armed) | SC-130, SC-110 |
  | Land | Both | None | Engaged only from Hover: extends the gear, descends vertically at `[P-AF-240]`, lands within the landing envelope, then switches the effectors off, so that no more fuel is used (D69) | — / LAND | SC-130, SC-110 |

#### CR-B3-33 — §4.5, §4.6 and §5

- **§4.5**, old "Because the effectors must counter gravity, fuel is consumed in every flight condition, including Hover and Stationary." → new "Because the effectors must counter gravity, fuel is consumed in every airborne condition, including Hover and Stationary. On the ground the effectors are off and no fuel is consumed (D69)."
- **§4.5**, old "The vehicle then moves under gravity and drag alone. Fuel exhaustion is nominal behaviour (SC-110). What the autoflight modes do after exhaustion is defined in detailed design (TBR, #59)." → new "The vehicle then moves under gravity and drag alone, and its ground contact is a crash (D68). Fuel exhaustion is nominal behaviour (SC-110); running out of fuel is the crew's to avoid, with the LOW FUEL alert. What the annunciations show after exhaustion is set by C5 (D68)."
- **§4.6**, initial condition bullet: "position, velocity, attitude, angular rate, landing gear position, fuel quantity, active and armed modes, and selected targets. A run starts on the ground (D69)".
- **§4.6**, old "The run ends when the TST's end condition is met: the scenario's end condition, a maximum run time set by the TST, or ground contact (a landing within the envelope, or a crash; D37)." → new "The run ends when the TST's end condition is met: the scenario's end condition, a maximum run time set by the TST, or a crash (D37, D68, D69). A landing does not end the run."
- **§5**, first common condition, new: "The vehicle starts on the ground, at rest on its extended gear with the effectors off and no mode active (D69). For the flight scenarios SC-020 to SC-120, a test procedure may instead start the run airborne (owner question B3-Q1): the vehicle is then inside the operating volume at `H_INIT`, with a height above the ground of at least `[P-SYS-210]`, the gear retracted, the effectors on and the modes of the scenario active. Otherwise each such scenario begins with a Takeoff and the selections that reach its initial condition."

#### CR-B3-34 — SC-100, SC-110, SC-200

- **SC-100 TBR**, new: "**Answered (D70):** engaged below the hover height, Go to hover climbs to it. Open: how the crew leaves Hover (C5)."
- **SC-100**, new variation after "Variation SC-100 / wind": "**Variation SC-100 / from below.** GO HOVER is engaged during a Land, below the hover height. The vehicle climbs back to the hover height and Hover engages (D70). Whether the gear retracts is set by C5."
- **SC-110 initial conditions**, new: "On the ground at rest on the extended gear, effectors off, no mode active. Fuel at full capacity `[P-FU-010]`, so mass at its maximum. Heading `HDG_INIT`."
- **SC-110 profile:** add leg 0 before leg 1, replace leg 1, and insert legs 7a and 7b after leg 7. Change leg 8's "Leg ends when" text, and leg 11's "Active" column and vehicle-behaviour text. The leg numbers 1 to 11 are kept, because MS-DYN, L1-AER-200 and the FU records cite them.

| Leg | Crew selections | Active (after captures) | Armed | Vehicle behaviour | Leg ends when |
| --- | --- | --- | --- | --- | --- |
| 0 | TAKEOFF | TAKEOFF, then HOVER | HOVER | Powers up, lifts off, climbs vertically at `[P-AF-240]` to the hover height, retracts the gear (as SC-130). | HOVER active |
| 1 | None | HOVER | — | Holds the hover height and position for `T_1`. | `T_1` elapsed |
| 7a | LAND | LAND | — | Extends the gear, descends at `[P-AF-240]`, lands within the envelope, switches the effectors off; rests on the ground for `T_7A` with the remaining fuel constant (as SC-130). | `T_7A` elapsed on the ground |
| 7b | TAKEOFF | TAKEOFF, then HOVER | HOVER | As leg 0. | HOVER active |
| 11 | None | (C5, D68) | — | FUEL EXHAUSTED annunciated. Effectors produce zero force and zero moment. The vehicle falls under gravity and drag, keeps the angular rate it had at exhaustion, and its ground contact is a crash (D68). | Crash, or TST maximum run time |

  Leg 2 now leaves Hover by engaging HDG and GO ALT (C5: how the crew leaves Hover). Leg 8 starts from HOVER after leg 7b.
- **SC-110 expected behaviour:** "The fuel quantity decreases throughout the mission and never increases" → "The fuel quantity never increases; it decreases in every airborne leg and is constant during the rest of leg 7a". Add "Leg 0 and leg 7b meet SC-130 (takeoff), and leg 7a meets SC-130 (landing and rest)". "The run ends at ground contact, normally a crash, because the vehicle is outside the landing envelope (D37)." → "The run ends at the ground contact after exhaustion, which is a crash (D68)."
- **SC-110 hover endurance variation**, new: "From the same initial condition, TAKEOFF is engaged at the start and HOVER kept until the fuel is exhausted. The time from the TAKEOFF engagement to exhaustion is at least `[P-SYS-280]` (L1-AER-360)."
- **SC-110 end conditions:** "Ground contact, or TST maximum run time" → "Crash, or TST maximum run time". **Needs:** add N-450. **TBR**, new: "As in the scenarios each leg repeats. How the crew leaves Hover in legs 2 and 8 (C5). Annunciations after fuel exhaustion (C5, D68)."
- **SC-200 step 5:** "… the maximum run time or ground contact." → "… the maximum run time or a crash."

#### CR-B3-35 — New SC-130; §7.2, §8, §9

- **New §6.3 scenario**, after SC-100:

  > #### SC-130 — Take off, hover, land and rest
  >
  > **Purpose.** Show the ground operations of D69. A run starts on the ground with the effectors off. Takeoff lifts the vehicle to the hover height and retracts the gear. Land extends the gear and touches down within the landing envelope. The vehicle then rests on the ground with no fuel used.
  >
  > **Initial conditions.** On the ground at rest on the extended gear, effectors off, no mode active, heading `HDG_INIT`, fuel `FUEL_INIT` above the low-fuel threshold. Still air.
  >
  > **Crew selections.** TAKEOFF at `T_TO`; LAND at `T_LD`, after Hover has engaged.
  >
  > | Step | Trigger | Active | Armed | Vehicle behaviour |
  > | --- | --- | --- | --- | --- |
  > | 1 | Crew engages TAKEOFF | TAKEOFF | HOVER | The effectors power up. The vehicle lifts off and climbs vertically at `[P-AF-240]`, heading and horizontal position held, pitch and roll zero. |
  > | 2 | Height above the ground reaches `[P-AF-210]` | TAKEOFF | HOVER | The vehicle holds the hover height. The gear retracts within `[P-DYN-050]`, and the gear position is annunciated. |
  > | 3 | Gear retracted, vehicle stationary at the hover height | HOVER | — | Holds the hover height and the position over the ground. |
  > | 4 | Crew engages LAND | LAND | — | The gear extends within `[P-DYN-050]`; the vehicle then descends vertically at `[P-AF-240]`. |
  > | 5 | Ground contact on the extended gear | LAND, then none (C5) | — | Landing event. The vehicle is at rest on the gear; the effectors are off within `[P-SYS-480]`. |
  > | 6 | On the ground for `T_REST` | None | — | The vehicle stays at rest; the remaining fuel is constant; the sensed acceleration is 1 g. |
  >
  > **Expected vehicle behaviour.** The horizontal position stays within `[P-SYS-450]` of its value on the ground. At the contact, the vertical speed magnitude is at most `[P-SYS-500]` and the horizontal speed at most `[P-SYS-510]`, and the gear is extended. From `[P-SYS-480]` after the contact, every effector output is zero and the remaining fuel mass does not change. The heading stays within `[P-AF-130]` of `HDG_INIT`.
  >
  > **Variation SC-130 / wind.** As SC-130 with a steady wind and gusts within the wind envelope during the hover and the landing. The takeoff is made in a wind of at most `[P-SYS-580]` (owner question B3-Q2).
  >
  > **Variation SC-130 / zero fuel.** The run starts with no fuel. FUEL EXHAUSTED is annunciated; the vehicle stays on the ground. Whether TAKEOFF is accepted is set by C5.
  >
  > **Variation SC-130 / go to hover during the landing.** GO HOVER is engaged during step 4. The vehicle climbs back to the hover height and Hover engages (D70).
  >
  > **Variation SC-130 / second takeoff.** After step 6, TAKEOFF is engaged again, and the vehicle repeats steps 1 to 3.
  >
  > **End conditions.** On the ground at rest, effectors off, for `T_REST`.
  >
  > **Needs exercised.** N-050, N-060, N-150, N-210, N-310, N-450.
  >
  > **TBR.** The mode state after the landing, and the selections accepted on the ground (C5, #60). Whether LAND stays annunciated on the ground (C5). The gear labels (C5, C8).

- **§7.2 A2-Q02:** append "**Revised (D69):** runs start on the ground on a landing gear; Takeoff and Land are modes; a landing does not end the run."
- **§7.2 A2-Q04:** append "**Owner (D68):** the effectors stop, the vehicle falls and its ground contact is a crash; the annunciations after exhaustion are C5's."
- **§7.2 A2-Q05:** append "On the ground, no mode is active (recommended to C5, D69, #60)."
- **§8.1:** add row "| SC-130 | N-050, N-060, N-150, N-210, N-310, N-450 | Takeoff, Hover, Land, Go to hover |". SC-110 modes: "All seven modes" → "All nine modes". Closing sentence: "Each of the nine modes of D56 and D69 is exercised by at least one scenario of its own and by SC-110."
- **§9 table:** rename P-SYS-210 "Minimum operating height above the ground" and P-AF-210 "Hover height above the ground (D56, D70; CV-400)". Add P-AF-240 "Takeoff and landing vertical speed", P-DYN-030 "Body diameter", P-DYN-040 "Landing gear length", P-DYN-050 "Landing gear transit time", P-SYS-480 "Control-loop latency", P-SYS-500 and P-SYS-510 "Landing envelope", and P-SYS-580 "Maximum wind speed at liftoff".

### CONVENTIONS

#### CR-B3-36 — CV-160, CV-420, CV-440, new CV-400, header

- **New CV-400**, placed after CV-440, which it refines. CV-400 is the only free ID of the CV-4xx block, and IDs are never reused:

  > ### CV-400 — Height above the ground
  >
  > **Height above the ground** `h_G` is the vertical distance from the datum plane up to the lowest point of the body shape, positive up. The body shape is the capsule of the MS-DYN vehicle geometry, of length `P-DYN-020` and diameter `P-DYN-030` along `x_B`; the landing gear is not part of it. With h the altitude (CV-430) and θ the pitch angle (CV-220):
  >
  > `h_G = h − P-DYN-030/2 − ((P-DYN-020 − P-DYN-030)/2)·|sin θ|`
  >
  > At level attitude, `h_G = h − P-DYN-030/2`. On the ground, at rest on the extended landing gear, `h_G` equals the gear length `P-DYN-040` (D69). The hover height (`P-AF-210`) and the minimum operating height (`P-SYS-210`) are heights above the ground (D67, D70). Requirements on the altitude of the vehicle use the altitude of CV-430: the selected altitude, Altitude hold, the maximum operating altitude and the atmosphere. Requirements on the clearance of the body above the ground use the height above the ground. Ground contact is detected at the lowest point of the vehicle, which is the extended gear or the body (MS-DYN ground contact model).
  > **Status:** Proposed (D69, D70, CR-B3-36).

- **CV-160**, second paragraph, new: "'Vehicle position', 'altitude' and every motion quantity in Section 5 refer to `O_B` unless a requirement explicitly names another point. The height above the ground (CV-400) is defined at the lowest point of the body." **Status:** Changed (D69, CR-B3-36).
- **CV-420**, last two sentences, new: "The Aeronef rests on the ground on its extended landing gear, and a ground contact of the airborne vehicle is a landing or a crash (D37, D69, L0-CON-290). So no point of the vehicle is below the datum plane in a run, and the height above the ground (CV-400) is never negative." **Status:** Changed (D69, CR-B3-36).
- **CV-440**, last two sentences, old: "On the flat ground of D8, "height above the ground" equals the altitude; the hover height of D56 (`P-AF-210`) is such a height, and requirements state it as an altitude." → new: "The **height above the ground** is defined separately, at the lowest point of the body rather than at `O_B` (CV-400, D70)." **Status:** Changed (D70, CR-B3-36).
- **Header:** "… the latest is CR-B1-10 (2026-11-04)" → "… the latest is CR-B3-36 (2026-11-05)". **Related:** "D7–D62" → "D7–D72".
- **Reason:** TT-820. CV-430 places the altitude at the CG, while D70 measures the hover height below the body, and D69 measures the gear length from the lowest point of the body. As it stands, CV-440 says the hover height is stated as an altitude, which would put the CG 5 ft above the ground and the body 0.48 m below it.
- **Recommendation:** approve. Altitude stays the CG altitude, so MS-DYN, the atmosphere, the crew altitude indication and the selected altitude do not change. Only the ground-related quantities move to the new height.

### GLOSSARY

#### CR-B3-37 — Changed definitions

- **Requested change:** apply the changed definitions of `glossary_proposals.md` §2 to these 26 fixed terms: *Accuracy horizon*, *Airborne*, *Annunciation*, *Axis reference*, *Contact step*, *Control force, control moment*, *Crash*, *Dynamics model*, *Fuel exhaustion*, *Go to hover*, *Ground contact*, *Hover*, *Hover height*, *Initial condition*, *Landing*, *Landing envelope*, *Mode catalogue*, *Mode group*, *Navigation*, *Navigation quantities*, *Operating volume*, *Reference mission*, *Sensed acceleration*, *Total force, total moment*, *Vehicle-model boundary* and *Wind envelope*. Merge the 11 new terms of §1; no CR is needed for them.
- **Reason:** the fixed definitions contradict D68 to D72. For example, *Ground contact* says "There is no landing gear", *Airborne* says "between the start of a run and ground contact", and *Hover height* says "On the flat ground (D8) it is an altitude".
- **Recommendation:** approve. *Accuracy horizon* follows D72 rather than D69; G2 §6 lists it with the D69 impact.

### FUNCTIONAL_ANALYSIS

#### CR-B3-38 — §2 Function list

| ID | Change |
| --- | --- |
| F-AER-01 | Refinement: append "Zero output with the effectors off (D69, L1-AER-930)." |
| F-AER-02 | Refinement: append "Zero flow at zero effector output (L1-AER-940); none on the ground (D69)." |
| F-AER-03 | Function: "Propagate six-degree-of-freedom rigid-body motion under control forces, gravity, drag and, on the ground, the ground reaction". Inputs: add "gear state". Refinement: append "On the ground the ground reaction holds the vehicle at rest on the gear until liftoff (D69, L1-AER-920)." |
| F-AER-07 | Outputs: "axis references, with the off value on the ground (D69)". |
| F-AER-08 | Inputs: add "gear state". Outputs: add "landing gear command". Refinement: "Catalogue D56 with Takeoff and Land (D69): one horizontal and one vertical mode at a time, independent; Go to hover, Hover, Takeoff and Land govern both. Arming and transitions are L2 (C5)." |
| F-AER-09 | Outputs: "altitude, height above the ground, horizontal speed, vertical speed, heading, track, validity". Refinement: "Definitions CV-400 to CV-550 …". |
| F-AER-12 | Function: "Detect ground contact, classify it as a landing or a crash, and hold the vehicle at rest on the ground". Inputs → outputs: "Vehicle state, gear position, fuel availability → landing or crash event, gear state (on the ground or not)". Refinement: "Ideal landing on an ideal landing gear (D37, D69, L0-CON-290). The envelope is two speed limits (D53); a landing also needs the gear extended and fuel remaining (D68). After a landing the vehicle rests until liftoff. The TST ends the run on a crash." |
| F-AER-13 | Inputs: add "the gear position, as annunciation content". |
| F-AER-14 | Inputs: "initial condition, including the landing gear position (a ground start, D69, or an airborne test start)". |
| F-AER-15 (new) | Function: "Extend and retract the landing gear". Inputs → outputs: "Landing gear command → gear position (extended, retracted, in transit)". Refinement: "New (D69). Transit time [P-DYN-050]; on the ground the gear stays extended; the gear changes no mass property and no drag (L1-AER-900, -910)." Subsystem: DYN. |

- **Lead-in paragraph:** "F-AER-09 to 14 are new …" → "F-AER-09 to 15 are new: … run set-up (14) and landing gear (15)."
- **"Functions not on the list, on purpose":** add "movement on the ground (taxiing: the vehicle is stationary on the ground, D69)".

#### CR-B3-39 — §3 N² matrix and interfaces, §4 control-loop flow

- **§3.2, changed rows:**
  - I-03 "F-02 → F-01" → "F-02 → F-01, F-12": "Fuel availability (remaining fuel mass above zero); F-12 uses it to classify a contact (D68)".
  - I-04: "Vehicle mass, inertia tensor (diagonal: principal body axes, D61)". Following G2-F05, the centre-of-gravity position does not cross I-04; this is the recommended I1 resolution and is aligned here.
  - I-08: "Lowest point of the vehicle and velocity at the contact step (D53, CV-400); gear position".
  - I-21: "Initial state, including the landing gear position; initial fuel mass; vehicle parameter set".
  - I-41: "Landing or crash event (the TST ends the run on a crash)".
- **§3.2, new rows:**
  - I-43 | F-08 → F-15 | Landing gear command | Vehicle-model boundary (L1-AER-430)
  - I-44 | F-15 → F-03, F-12 | Gear position | MS-DYN
  - I-45 | F-12, F-15 → F-08, F-11 | Gear state: gear position, on the ground or not | Vehicle-model boundary (L1-AER-430); ICD-AER-TST for the operational data
  - I-46 | F-12 → F-03 | On-ground state, from which the ground reaction applies | MS-DYN
- **§3.1 matrix:** add row and column F-15. The cells are F-08 → F-15 I-43; F-15 → F-03 I-44; F-15 → F-12 I-44; F-15 → F-11 I-45; F-12 → F-08 I-45; F-12 → F-03 I-46; F-12 → F-11 I-37, I-45; F-02 → F-12 I-03; F-14 → F-15 I-21.
- **§3.3 subsystem matrix:** AF → DYN "× gear command"; DYN → AF "× gear state"; DYN → TM "× state, events, gear state"; FU → DYN "× mass, inertia, fuel availability".
- **§4.1 flowchart:** add `F08 -- gear command --> F15[F-AER-15 Landing gear]`, `F15 --> F03`, `F15 --> F12`, `F12 -- gear state --> F08`.
- **§4.2 sequence, order 7:** "F-AER-01, -02, -03, -12, -15".

#### CR-B3-40 — §5 Logical architecture, §6 Allocation

- **§5.1 flowchart:** add `AF -- gear command: vehicle-model boundary --> DYN` and `DYN -- gear state --> AF`. The DYN node label becomes "DYN dynamics, environment, landing gear, ground contact".
- **§5.1 boundary table**, vehicle-model boundary row: "Effector commands and the landing gear command in; vehicle state, gear state, mass properties and fuel state out | L1-AER-430, -440".
- **§5.2 item 5**, new: "**Physics stays physics.** Fuel exhaustion, saturation, the crew g-limit and the ground reaction are handled in the layer that owns them (EF, FC, DYN), not as mode logic. Autoflight only commands the gear and switches the effectors off through the axis references (D69)."
- **§6.1:** DYN functions add F-AER-15, and DYN "Owns" adds "landing gear (geometry, movement), ground reaction and rest on the ground, gear state". AF "Owns": "Mode logic (Takeoff and Land included), guidance, landing gear command, effectors off on the ground, manoeuvre acceleration limit, annunciation content (gear position included)". EF "Owns": add "zero output with the effectors off". FU "Owns": add "zero flow at zero output". NAV "Owns": "Guidance quantities, height above the ground included, and their validity".
- **§6.2 table:** update the short texts of L1-AER-050, -260, -270, -360, -430, -470, -530, -640, -660, -720 and -890 to the new statements (CR-B3-08 to -27). Allocations do not change. Add rows:

| L1 ID | Type | Requirement (short) | Parent(s) | DYN | FU | EF | FC | AF | FCP | NAV | TM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1-AER-900 | Constraint | have a retractable landing gear whose ground contact points, when extended, lie [P-DYN-040] below … | L0-CON-290, L0-CON-130 | ● |  |  |  |  |  |  |  |
| L1-AER-910 | Functional | bring its landing gear to the commanded position within [P-DYN-050]. | L0-CON-290, L0-OBJ-030 | ● |  |  |  | ● |  |  |  |
| L1-AER-920 | Model fidelity | rest on its extended landing gear at level attitude with zero vehicle velocity … | L0-CON-090, L0-CON-290 | ● |  |  |  |  |  |  |  |
| L1-AER-930 | Functional | produce zero control force and zero control moment … on the ground … | L0-CON-100, L0-OBJ-030 |  |  | ● | ● | ● |  |  |  |
| L1-AER-940 | Model fidelity | compute a zero fuel mass flow for each simulation step in which its effectors produce zero … | L0-CON-120, L0-CON-100 |  | ● |  |  |  |  |  |  |
| L1-AER-950 | Functional | start at rest on its extended landing gear … with its effectors off. | L0-OBJ-010, L0-OBJ-030 | ● |  |  | ● | ● |  |  |  |
| L1-AER-960 | Performance | reach the hover height [P-AF-210] with its landing gear retracted … | L0-OBJ-030 |  |  | ● | ● | ● |  |  |  |
| L1-AER-970 | Performance | make its ground contact on its extended landing gear within the landing envelope. | L0-OBJ-030, L0-CON-290 |  |  | ● | ● | ● |  |  |  |

- **§6.2 count row:** DYN 27, FU 23, EF 26, FC 27, AF 25, FCP 15, NAV 9, TM 10, leaf 17.
- **§5.3 table, FCP row:** "-660, -680" unchanged.

#### CR-B3-41 — §7 Budgets, §8 Coverage

- **§7.2:** add after the closure rule: "**Ground and liftoff (D69).** At rest on the ground the sensed acceleration is that of the ground reaction, [P-DYN-010]; the touchdown on the ideal gear is not computed (D53). On the ground the ground reaction holds the vehicle against the drag of the wind. At liftoff that drag acts as a step that the flight software cannot anticipate (L1-AER-670). At dry mass and sea-level density, the takeoff wind limit [P-SYS-580] keeps the step within [P-FC-020] (L1-AER-960, owner question B3-Q2)."
- **§7.3:** hover endurance row, rule, new: "From a takeoff at full fuel (D69), Hover in still air: the effectors only counter gravity. The takeoff is inside the margin [P-FU-100]." Add row: "| No consumption on the ground | — | Zero flow at zero control force and moment (L1-AER-940); the effectors are off on the ground (L1-AER-930). |"
- **§8:** add the new children: L0-OBJ-010 adds L1-AER-950; L0-OBJ-030 adds L1-AER-910, -930, -950, -960, -970; L0-CON-090 adds L1-AER-920; L0-CON-100 adds L1-AER-930, -940; L0-CON-120 adds L1-AER-940; L0-CON-130 adds L1-AER-900; L0-CON-290 adds L1-AER-900, -910, -920, -970.
- **Header "Related":** "§9 (D1–D63)" → "§9 (D1–D72)".
