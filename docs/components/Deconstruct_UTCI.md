# ![](/images/icons/Deconstruct_UTCI.png) Deconstruct UTCI - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20UTCI%22)

![](/images/components/Deconstruct_UTCI-crop.png)

Probe-specific statistics and comfort hours/% from a UTCI or PET (Simulation) Result, without putting the full 8760-hour year on the canvas. Data only — wire the Result (or these outputs) into the Thermal Comfort Legend to draw a map. Comfort % is the outdoor thermal comfort autonomy (OTCA) of the selected hours; Stress, Weighted, Cold, Hot, Spatial and Continuous are its companion metrics, measured against the metric's own no-thermal-stress band. Method: Nazarian, Acero & Norford (2019), Building and Environment 155:145-160, doi:10.1016/j.buildenv.2019.03.028.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | R | Result output of the UTCI (Simulation) or PET (Simulation) component. | `Generic Data` |
| HOY |  | Hour(s) of year (1-8760) to restrict to. Leave unconnected for the whole year. Statistics and comfort hours/% are reduced over exactly these hours, so a July-afternoon list gives the July-afternoon comfort — no re-solve needed. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mean | Avg | Mean UTCI or PET (°C) per probe over the selected hours — the annual average when HOY is unconnected. | `Number` |
| Min |  | Lowest UTCI or PET (°C) per probe over the selected hours. | `Number` |
| Max |  | Highest UTCI or PET (°C) per probe over the selected hours. | `Number` |
| Comfort Hours | H | No-thermal-stress hours per probe, counted over the selected hours. | `Integer` |
| Comfort % | % | No-thermal-stress share (%) of the selected hours, per probe. | `Number` |
| UTCI | U | UTCI or PET (°C) at each selected hour — one branch per HOY, each holding every probe's value {hoy}(probe count). Populated ONLY when HOY is connected; with HOY unconnected this would be the entire year, which is the tree this component exists to avoid. | `Number` |
| Points | P | Probe positions carried inside the Result, aligned by index with every list above. Wire these into the Thermal Comfort Legend's Sensor Points to draw a map — or wire the Result straight into that component, which takes the positions itself. | `Point` |
| Thermal Stress | Stress | Thermal stress indicator ΔT_ave (°C) per probe: how far the selected hours sit outside the no-thermal-stress band on average. 0 when every hour is comfortable. | `Number` |
| Weighted Comfort % | Weighted | Weighted comfort autonomy OTCA_w (%) per probe: Comfort % scaled down by how far the uncomfortable hours deviate from the band. | `Number` |
| Cold % | Cold | Share (%) of the selected hours below the no-thermal-stress band, per probe. | `Number` |
| Hot % | Hot | Share (%) of the selected hours above the no-thermal-stress band, per probe. | `Number` |
| Spatial Comfort % | Spatial | Spatial OTCA: the share (%) of probes that are comfortable at least 50 % of the selected hours. Probes count equally, so this is an area share only on an even grid. | `Number` |
| Continuous Comfort % | Continuous | Continuous OTCA (%): as Spatial, but a probe below 50 % earns partial credit (40 % comfortable counts 0.8). | `Number` |
| P5 |  | 5th percentile UTCI or PET (°C) per probe over the selected hours — the cold end without the single coldest hour Min reports. | `Number` |
| P95 |  | 95th percentile UTCI or PET (°C) per probe over the selected hours — the hot end without the single hottest hour Max reports. | `Number` |