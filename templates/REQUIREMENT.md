# Requirement record template

Every requirement in a level file is one record: a `###` heading with its ID, then a fenced block tagged `req` with the METHODOLOGY 13.3 fields. Scripts parse only the `req` blocks.

- One field per line, `Field: value`. A long value continues on following lines indented by two spaces.
- Field names and order are fixed as below. Every field is present; use `—` when a field does not apply.
- Tailoring for this cycle: `Criticality: Not assessed`; the Safety type is not used.
- Numbers never appear in the Statement; reference parameters as `[P-<SUB>-<NNN>]` and list them under Parameters.
- IDs follow METHODOLOGY 9.1: `L0-OBJ-nnn`, `L0-CON-nnn`, `L0-SUC-nnn` (L0), `L1-AER-nnn` (L1), `L<n>-AER-<SUB>[-<ITEM>]-<NNN>` below (D31: the level prefix matches the Level field). Steps of 10; never reuse an ID.

### L2-AER-AF-PH-010

```req
ID:            L2-AER-AF-PH-010
Level:         L3
Type:          Functional | Performance | Interface | Constraint | Model fidelity | Documentation
Statement:     [While <state>,] [when <trigger>,] the <element> shall <response> <performance>.
Rationale:     Why it exists; assumptions; design decision if derived.
  Sufficiency: how this and its siblings fully cover the parent.
Parent(s):     <IDs> | Derived (DD-nnn)
Source:        <ConOps scenario | stakeholder need | trade study>
Allocated to:  <child elements> | —
Criticality:   Not assessed
Verification:  Inspection | Analysis | Demonstration | Test — <TP-|AN-|DM-|IN-nnn | TBD>; success criteria: <...>
Parameters:    <P-xx-nnn, ...> | —
TBD/TBR:       <item, owner, date> | —
Owner:         Martin
Status:        Draft
Version:       1
```

## Assumption record (L0 assumptions register)

```asm
ID:            L0-ASM-010
Assumption:    <statement>
Rationale:     <why it is reasonable>
Affects:       <requirement IDs or areas>
Owner:         Martin
Status:        Open | Confirmed | Retired
```
