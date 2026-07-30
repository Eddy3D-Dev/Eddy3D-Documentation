# ![](/images/icons/UTCI_Simulation.png) UTCI (Simulation) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22UTCI%20%28Simulation%29%22)

![](/images/components/UTCI_Simulation-crop.png)

Compute annual per-probe UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| MRT | M | DataTree of annual MRT values {probe}(8760). Each branch = one probe. | `Number` |
| Wind Speed | V | Wind speed as an AnnualWindField, one spatial list (one value per probe, held for all hours), or a {probe}(hours) / {hour}(probes) tree. Pedestrian-height speeds are lifted to the 10 m UTCI reference. Defaults to calm (0.5 m/s) when unconnected. | `Generic Data` |
| Air Temperature | T | Annual hourly ambient air temperature (8760 values, °C). | `Number` |
| Relative Humidity | RH | Annual hourly relative humidity (8760 values, %). | `Number` |
| Transpose |  | True (default): UTCI tree is {hour}(probes), typically 8760 branches with one value per probe. False: UTCI tree is {probe}(hours). | `Boolean` |
| Run |  | Enable UTCI calculation. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| UTCI | U | UTCI data tree. Default: {hour}(probes). With Transpose off: {probe}(hours). | `Number` |
| Comfort Hours | H | No-thermal-stress hours per probe. | `Integer` |
| Comfort % | % | Comfort percentage per probe. | `Number` |