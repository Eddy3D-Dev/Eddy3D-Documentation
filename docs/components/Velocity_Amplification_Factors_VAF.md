# ![](/images/icons/Velocity_Amplification_Factors_VAF.png) Velocity Amplification Factors (VAF) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Velocity%20Amplification%20Factors%20%28VAF%29%22)

![](/images/components/Velocity_Amplification_Factors_VAF-crop.png)

Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD or ML wind-prediction results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary Conditions | BC | OutdoorBoundaryConditions object from the ABL or Uniform Flow component. | `Generic Data` |
| Wind Velocity | U | DataTree {direction}[probe] of velocity vectors from the CFD probe results, OR of scalar wind speeds (m/s) from the Wind Predictor's Values output — either engine feeds the same annual wind field. | `Generic Data` |
| EPW |  | Path to the EPW weather file. | `Text` |
| Probe Height | Height | Probing/pedestrian height in meters. | `Number` |
| Interpolate | Interp | How each weather hour's direction is mapped onto the simulated directions — for any number of them. Interpolate blends the two BRACKETING directions by angular proximity; Nearest snaps to the closest simulated direction. A wired boolean from an older document still works: True means Interpolate, False means Nearest. | `Text` |
| Points | P | Optional probe points in the same order as the Wind Velocity tree's branches. Embedded into the Wind Speed output so downstream components — the Pedestrian Wind Comfort mesh — know where each series lives without extra wiring. | `Point` |
| Factors |  | What the Velocity Amplification Factors output carries. Annual (per hour) — the default: {hour}(probes), 8760 branches, each hour's factor resolved from the EPW's wind direction through the Interpolate setting; needs the EPW and is built only while the output is wired (prefer the one-item Annual VAF output into Deconstruct Wind). Spatial (per direction): {direction}(probes), one branch per simulated direction. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Speed | Wind | Annual wind field object (every point's 8760-hour wind-speed series) for the Pedestrian Wind Comfort component. A single object rather than a data tree, so a few thousand probes stay fast. | `Generic Data` |
| Velocity Amplification Factors | VAF | Velocity Amplification Factors (VAF) — local wind speed normalized by the reference (undisturbed) speed. Indexing follows the Factors setting: {direction}(probes) per simulated direction (default), or {hour}(probes) across all 8760 weather hours when Factors is set to Annual. | `Number` |
| Annual VAF | AVAF | The direction-mapped Velocity Amplification Factor at every probe for every weather hour, carried as ONE object (probes × 8760, dimensionless) — wire it into Deconstruct Wind for statistics, a colored mesh and per-hour values. Needs the EPW; empty until it is connected. This is the fast path: the tree output above materializes the same numbers as millions of items on the canvas. | `Generic Data` |