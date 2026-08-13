# ![](/images/icons/Velocity_Amplification_Factors_VAF.png) Velocity Amplification Factors (VAF) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Velocity%20Amplification%20Factors%20%28VAF%29%22)

![](/images/components/Velocity_Amplification_Factors_VAF-crop.png)

Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary Conditions | BC | OutdoorBoundaryConditions object from the ABL or Uniform Flow component. | `Generic Data` |
| Wind Velocity | U | DataTree of velocity vectors {direction}[probe] from the probe results. | `Vector` |
| EPW |  | Path to the EPW weather file. | `Text` |
| Probe Height | Height | Probing/pedestrian height in meters. | `Number` |
| Interpolate | Interp | Interpolate between bracketing wind directions. | `Boolean` |
| Points | P | Optional probe points in the same order as the Wind Velocity tree's branches. Embedded into the Wind Speed output so downstream components — the Pedestrian Wind Comfort mesh — know where each series lives without extra wiring. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Speed | Wind | Annual wind field object (every point's 8760-hour wind-speed series) for the Pedestrian Wind Comfort component. A single object rather than a data tree, so a few thousand probes stay fast. | `Generic Data` |
| Velocity Amplification Factors | VAF | DataTree {direction}[probe] of Velocity Amplification Factors (VAF) — local wind speed normalized by the reference (undisturbed) speed. | `Number` |