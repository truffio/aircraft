# C8 — Glossary proposals (FCP)

Proposals for `specs/GLOSSARY.md` from task C8. New terms need no change request; changed definitions of Fixed terms do (D43): C8 proposes **CR-C8-02** for the refinements in §2 (`work/C8/issues.md`).

## 1. New terms

| Term | Definition | Source |
| --- | --- | --- |
| Annunciation content | The data that *autoflight* gives the *flight control panel* at each *control frame* for the *annunciations*: the *mode state*, each *target* in use with the quantity it applies to, and the *gear position*, in SI. The panel presents it; autoflight decides it. | L1-AER-470, -880; ICD-FCP; L2-AER-FCP-060 |
| Crew interface output | The data items that the *flight control panel* outputs to the *crew* at each *output sample*: the mode state, target, gear-position and *fuel alert* *annunciations*, the *selector readouts* and the *indications*, in crew-facing units. No layout, graphics or symbology (*display format*). | L1-AER-490; L2-AER-FCP-030, -040 |
| Display resolution | The step to which a *shown value* is rounded: `[P-TM-020]` (altitude), `[P-TM-030]` (vertical speed), `[P-TM-040]` (horizontal speed), `[P-TM-050]` (heading, track), `[P-FCP-010]` (remaining fuel), in crew-facing units. | CV-780; L2-AER-FCP-210 |
| Fuel alert | The *annunciation* item that shows the fuel state to the *crew*: LOW FUEL while the fuel state indicates low fuel without *fuel exhaustion*, FUEL EXHAUSTED while it indicates fuel exhaustion, and no label otherwise. One label at a time. | L1-AER-570, -580; L2-AER-FCP-390 to -410 |
| Mode selection | A *crew selection* that asks *autoflight* to engage one *mode*: Stationary, Heading, Altitude hold, Go to altitude, Vertical speed, Go to hover, Takeoff or Land. Whether the mode arms, becomes active or is refused is decided by the mode logic, not by the panel. There is no mode selection for *Hover*. | D71; CONOPS §4.3; L2-AER-FCP-020 |
| Selectable range | The set of *selected values* a *selector* accepts: the multiples of its *selection resolution* between two limits, checked on the exact CV-750 conversion. | CV-760; L2-AER-FCP-100 to -130 |
| Selection resolution | The step between two selectable values of a *selector*: `[P-AF-010]` (altitude), `[P-AF-020]` (vertical speed), `[P-AF-030]` (horizontal speed), `[P-AF-040]` (heading), in crew-facing units. | CV-770; D71 |
| Selector | One of the four target selectors of the *flight control panel*: heading, horizontal speed, altitude (the target altitude) and vertical speed. Each holds one *selected value*, in its crew-facing unit, until the *crew* selects another that the selector accepts. | D56, D71; L2-AER-FCP-100 to -150 |
| Selector readout | The *annunciation* of the *selected value* that one *selector* holds, shown as selected, in its crew-facing unit, with no conversion. | D71; L2-AER-FCP-350 |
| Shown value | The value of an annunciated *target* or an *indication* as the *crew* sees it: the SI value divided by the exact CV-750 factor and rounded half away from zero to its *display resolution*; a heading or track that rounds to a full turn is shown as zero. | CV-750, CV-780; L2-AER-FCP-210, -220 |

## 2. Refined definitions (CR-C8-02)

| Term | Current | Proposed |
| --- | --- | --- |
| Annunciation | "Information the Aeronef presents to the *crew* about its state, for example the *armed* and *active* modes, their *targets* and the *gear position*. Annunciations are crew-facing; their values use crew-facing units." | "Information the Aeronef presents to the *crew* about its autoflight state and its alerts: the *mode state*, the *targets* in use, the *gear position*, the *fuel alert* and the *selector readouts* (the selected targets). Annunciations are crew-facing; their values use crew-facing units." |
| Flight control panel | "… Its own L2 subsystem, FCP (D55). There is no stick or yoke. Content defined at L2 (#79)." | "… Its own L2 subsystem, FCP (D55). There is no stick or yoke. Its content (D71, #79) is eight *mode selections*, four *selectors* and the *crew interface output* (L2-AER-FCP-020, -040). It converts between crew-facing units and SI, so that only SI values reach the rest of the Aeronef." |
| Crew selection | "One data item of the *crew interface* by which the *crew* selects a *mode* or a *selected value*, with its *timestamp*." | "One data item of the *crew interface* by which the *crew* makes a *mode selection* or gives a *selector* a *selected value*, with its *timestamp*." |
| Low-fuel alert | "The *annunciation* given when the *remaining fuel mass* falls below the fraction `[P-FU-020]` of `[P-FU-010]`. Its label is set at L2." | "The *fuel alert* LOW FUEL, given while the *remaining fuel mass* is below the fraction `[P-FU-020]` of `[P-FU-010]` and fuel remains (L2-AER-FCP-390). At *fuel exhaustion* it is replaced by FUEL EXHAUSTED." |
| Selected value | "A value the crew chooses for a *target*, in a crew-facing unit (for example a selected altitude in ft). It becomes the SI *target* by exact conversion." | Add: "It is held by its *selector* as selected, and accepted only within the *selectable range* of that selector." |
| Horizontal speed | "… Its selected value is flown by the *Heading* mode (D56)." | Add: "The selected horizontal speed is a ground speed, not an airspeed (D72)." |
