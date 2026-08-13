# ![](/images/icons/Deconstruct_MRT.png) Deconstruct MRT - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20MRT%22)

![](/images/components/Deconstruct_MRT-crop.png)

Probe-specific statistics (and optionally the raw hours) from an MRT Result, without putting the full 8760-hour year on the canvas.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | R | Result output of the MRT component. | `Generic Data` |
| HOY |  | Hour(s) of year (1-8760) to restrict to. Leave unconnected for the whole year. The statistics are reduced over exactly these hours, so a July-afternoon list gives the July-afternoon mean — no re-solve needed. | `Integer` |
| Statistic | Stat | Statistic used to color the preview mesh: Mean, Min, or Max over the selected HOY. Defaults to Mean. | `Text` |
| Radius |  | Half-width of each colored square centered on an MRT probe point. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mean | Avg | Mean radiant temperature (°C) per probe over the selected hours — the annual average when HOY is unconnected. | `Number` |
| Min |  | Lowest mean radiant temperature (°C) per probe over the selected hours. | `Number` |
| Max |  | Highest mean radiant temperature (°C) per probe over the selected hours. | `Number` |
| MRT | M | Mean radiant temperature (°C) at each selected hour — one branch per HOY, each holding every probe's value {hoy}(probe count). Populated ONLY when HOY is connected; with HOY unconnected this would be the entire year, which is the tree this component exists to avoid. Note that a large HOY list is inherently expensive: every value asked for here becomes an object on the canvas. | `Number` |
| Mesh |  | Colored probe mesh for the selected Mean, Min, or Max statistic. Uses the same default jet color ramp and square markers as Wind Predictor. | `Mesh` |