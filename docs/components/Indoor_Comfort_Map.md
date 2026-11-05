# ![](/images/icons/Indoor_Comfort_Map.png) Indoor Comfort Map - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Comfort%20Map%22)

![](/images/components/Indoor_Comfort_Map-crop.png)

Per-point thermal comfort from probed indoor CFD fields: PMV/PPD (EN ISO 7730), operative temperature, ISO 7730 draught rate (from k when probed, else Tu = 40 %), head-to-ankle temperature difference (ISO 7730 PD and ASHRAE 55 PPD), ADPI (ASHRAE 113, cooling) and the share of points meeting ISO 7730 categories A/B/C, EN 16798-1 I-IV and ASHRAE 55. Probe the same points for T, U, k (and T again at head and ankle height). Temperatures in kelvin — what OpenFOAM writes — are converted automatically. Not assessed: radiant asymmetry, floor temperature, and ASHRAE 55's SET method for points above 0.2 m/s (reported separately). Formulas pinned against pythermalcomfort (Tartarini & Schiavon 2020) and ISO 7730 Annex D.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Air Temperature | Ta | Air temperature at each occupant point, at body height (0.6 m seated / 1.1 m standing): the Probe's T (kelvin is converted) or °C. | `Generic Data` |
| Air Speed | V | Mean air speed at the same points: the Probe's U vectors (their magnitude is used) or speeds in m/s. | `Generic Data` |
| Turbulent Kinetic Energy | k | Probed k (m²/s²) at the same points, for the draught rate's turbulence intensity Tu = 100·√(2k/3)/v. Unwired: ISO 7730's default Tu = 40 %. | `Generic Data` |
| Radiant Temperature | Tr | Mean radiant temperature (°C or K): one value for the room or one per point. Unwired: equal to the air temperature (walls at air temperature — say so in a report). | `Generic Data` |
| Relative Humidity | RH | Relative humidity (%), one value or one per point. | `Number` |
| Head Temperature | Th | Air temperature at head height (1.1 m seated / 1.7 m standing), one per point. With Ankle Temperature it drives the vertical-difference criterion; also used as the draught (neck) temperature. | `Generic Data` |
| Ankle Temperature | Tf | Air temperature at ankle height (0.1 m), one per point. | `Generic Data` |
| Metabolic Rate | M | Metabolic rate (met). | `Number` |
| Clothing | Clo | Clothing insulation (clo). | `Number` |
| Posture | Pos | Seated or standing: sets which heights the head/ankle probes represent and the ASHRAE 55 gradient span. | `Text` |
| Control Temperature | Tc | ADPI control temperature (°C). Unwired: the mean of the air temperatures. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| PMV |  | Predicted Mean Vote per point (EN ISO 7730). | `Number` |
| PPD |  | Predicted Percentage Dissatisfied per point (%). | `Number` |
| Operative Temperature | To | Operative temperature per point (°C, ISO 7726). | `Number` |
| Draught Rate | DR | ISO 7730 draught rate per point (%). | `Number` |
| Vertical PD | PD | ISO 7730 percentage dissatisfied from the head-ankle difference per point (%); empty without head/ankle input. | `Number` |
| Effective Draft Temperature | EDT | ASHRAE 113 effective draft temperature per point (K). | `Number` |
| ISO 7730 Category | ISO | Best ISO 7730 category met per point (A/B/C/Outside). | `Text` |
| EN 16798-1 Category | EN | Best EN 16798-1 category met per point (I-IV/Outside). | `Text` |
| ASHRAE 55 | A55 | Per point: Compliant, NotCompliant, or ElevatedAirSpeed (above 0.2 m/s — the SET method applies, not assessed here). | `Text` |
| Summary | Sum | Occupied-zone statistics. | `Text` |
| Comfort Map | Map | The whole map, for the Ventilation & Comfort Report. | `Generic Data` |