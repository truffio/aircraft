# Change requests

Upward change requests raised by a child level against its parent level.

| ID | Raised by | Against (requirement ID) | Requested change | Reason | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| CR-B1-01 | B1 | L0-OBJ-110 | Allocated to TST → TST, AER; rationale notes the deterministic Aeronef software (L1-AER-690). | The Aeronef runs inside every run; the TST alone cannot guarantee reproducibility. | Applied | Approved by the owner (#104, D50), 2026-10-28; L0-OBJ-110 v4. |
| CR-B1-02 | B1 | L0-CON-190 | Allocated to TST → TST, AER; rationale notes that no Aeronef function needs a display (L1-AER-700). | A display dependency inside the Aeronef would break the headless core. | Applied | Approved by the owner (#104, D50), 2026-10-28; L0-CON-190 v4. |
| CR-B1-03 | B1 | L0-ASM-050; CONOPS §4.2; CV-470; GLOSSARY *Wind* | The wind is horizontal and uniform in space, a steady wind plus gusts and bursts that vary in time; add the term *Gust*. | The owner adds gusts: steady wind up to 100 kt plus gusts up to 50 kt (#99). | Applied | Approved by the owner (#99, D51), 2026-10-28. |
| CR-B1-04 | B1 | L0-CON-160 | Allocated to AER → —; verified directly by inspection over the Aeronef branch instead of by roll-up. | The owner deletes L1-AER-230: no requirement is written for a system the Aeronef does not have (D54). | Applied | Approved by the owner (D54), 2026-11-04; L0-CON-160 v3. |
| CR-B1-05 | B1 | L0-ASM-030; CONOPS §1, §3, §4, §6 to §9; CV-560, CV-580, CV-610 to CV-670 and the VOR and flight-path-angle mentions in CONVENTIONS; GLOSSARY mode and VOR terms | Remove VOR and the flight path angle; replace the mode material with the D56 catalogue and the D57 attitude rule; withdraw SC-010, -030, -070, -080 and add SC-120 (turn in place); delete CV-560 and CV-610 to CV-670 (IDs kept, status Deleted). | The owner replaced the mode catalogue (D56) and fixed pitch and roll at zero (D57). | Applied | Approved by the owner (D56, D57), 2026-11-04. |
| CR-B1-06 | B2 | L0-CON-310 | TBD/TBR field: P-SYS-120 TBR → closed. | The owner confirmed 3 g (D45, #97); P-SYS-120 is Set in PARAMETERS.yaml. | Applied | Approved by the owner (D45), 2026-10-28; applied 2026-11-04; L0-CON-310 v5. |
