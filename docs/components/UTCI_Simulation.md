# ![](/images/icons/UTCI_Simulation.png) UTCI (Simulation) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22UTCI%20%28Simulation%29%22)

![](/images/components/UTCI_Simulation-crop.png)

Compute annual probe-specific UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| MRT | M | The MRT component's Result (preferred), or a DataTree of annual MRT values — {probe}(8760) or {hour}(probes), both accepted. | `Generic Data` |
| Wind Speed | V | Wind speed as an AnnualWindField (the VAF component's Wind Speed output — fed by CFD probe vectors or the ML Wind Predictor alike), one spatial list (one value per probe, held for all hours), or a {probe}(hours) / {hour}(probes) tree. An AnnualWindField on a different grid than the MRT sensors is resampled by nearest neighbor when both carry points. Pedestrian-height speeds are lifted to the 10 m UTCI reference. Defaults to calm (0.5 m/s) when unconnected. | `Generic Data` |
| Air Temperature | T | Annual hourly ambient air temperature (8760 values, °C). | `Number` |
| Relative Humidity | RH | Annual hourly relative humidity (8760 values, %). | `Number` |
| Transpose |  | Orientation of the UTCI tree output. Hours × Probes (default): one branch per hour, each holding every probe's value. Probes × Hours: one branch per probe, each holding that probe's year. | `Text` |
| Run | R | Enable UTCI calculation. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| UTCI | U | UTCI data tree. Default: {hour}(probes). With Transpose off: {probe}(hours). Only built while this output is WIRED: for a few thousand probes the full year is tens of millions of values on the canvas, and constructing them — not the UTCI math — is the wait. Prefer the Result output with Deconstruct UTCI. | `Number` |
| Comfort Hours | H | No-thermal-stress hours per probe. | `Integer` |
| Comfort % | % | Comfort percentage per probe. | `Number` |
| Result |  | The complete annual UTCI solve as ONE item — feed to Deconstruct UTCI for statistics, comfort maps and hour selections without materializing the year as a tree. Carries the MRT probes' positions when the MRT input was a Result. | `Generic Data` |