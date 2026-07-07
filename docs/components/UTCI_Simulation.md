# ![](/images/icons/UTCI_Simulation.png) UTCI (Simulation) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22UTCI%20%28Simulation%29%22)

![](/images/components/UTCI_Simulation-crop.png)

Compute annual per-probe UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| MRT | M | DataTree of annual MRT values {probe}(8760). Each branch = one probe. |
| Wind Speed | V | Annual per-probe wind field from the Wind Factors component (its Wind Speed output). Pedestrian-height speeds are lifted to the 10 m UTCI reference. Defaults to calm (0.5 m/s) when not connected. |
| Air Temperature | T | Annual hourly ambient air temperature (8760 values, °C). |
| Relative Humidity | RH | Annual hourly relative humidity (8760 values, %). |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| UTCI | U | DataTree {probe}(8760 hourly UTCI values). |
| Comfort Hours | H | No-thermal-stress hours per probe. |
| Comfort % (%) |  | Comfort percentage per probe. |
