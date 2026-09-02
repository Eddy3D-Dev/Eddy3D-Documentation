# ![](/images/icons/Deconstruct_UTCI.png) Deconstruct UTCI - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20UTCI%22)

![](/images/components/Deconstruct_UTCI-crop.png)

Probe-specific statistics and comfort hours/% from a UTCI or PET (Simulation) Result, without putting the full 8760-hour year on the canvas. Data only — wire the Result (or these outputs) into the Thermal Comfort Legend to draw a map.

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