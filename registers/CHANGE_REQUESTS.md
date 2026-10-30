# Change requests

Upward change requests raised by a child level against its parent level.

| ID | Raised by | Against (requirement ID) | Requested change | Reason | Status | Resolution |
| --- | --- | --- | --- | --- | --- | --- |
| CR-B1-01 | B1 | L0-OBJ-110 | Allocated to TST → TST, AER; rationale notes the deterministic Aeronef software (L1-AER-690). | The Aeronef runs inside every run; the TST alone cannot guarantee reproducibility. | Applied | Approved by the owner (#104, D50), 2026-10-28; L0-OBJ-110 v4. |
| CR-B1-02 | B1 | L0-CON-190 | Allocated to TST → TST, AER; rationale notes that no Aeronef function needs a display (L1-AER-700). | A display dependency inside the Aeronef would break the headless core. | Applied | Approved by the owner (#104, D50), 2026-10-28; L0-CON-190 v4. |
| CR-B1-03 | B1 | L0-ASM-050; CONOPS §4.2; CV-470; GLOSSARY *Wind* | The wind is horizontal and uniform in space, a steady wind plus gusts and bursts that vary in time; add the term *Gust*. | The owner adds gusts: steady wind up to 100 kt plus gusts up to 50 kt (#99). | Applied | Approved by the owner (#99, D51), 2026-10-28. |
