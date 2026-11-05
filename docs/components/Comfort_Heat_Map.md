# ![](/images/icons/Comfort_Heat_Map.png) Comfort Heat Map - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Comfort%20Heat%20Map%22)

![](/images/components/Comfort_Heat_Map-crop.png)

365 × 24 heat maps of one probe's UTCI or PET — sun and wind, wind without sun, sun without wind, neither — from the same MRT, wind and weather inputs as UTCI (Simulation). Sun is removed by setting MRT to the air temperature and wind by holding 0.5 m/s, exactly as the Site Report's scenarios do. Export writes SVG, PDF and PNG.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| MRT | M | The MRT component's Result (preferred), or a DataTree of annual MRT values — {probe}(8760) or {hour}(probes), both accepted. | `Generic Data` |
| Wind Speed | V | Wind speed as for UTCI (Simulation): an AnnualWindField, one value per probe, or a tree. Defaults to calm (0.5 m/s) when unconnected. | `Generic Data` |
| Air Temperature | T | Annual hourly ambient air temperature (8760 values, °C). | `Number` |
| Relative Humidity | RH | Annual hourly relative humidity (8760 values, %). | `Number` |
| Probe |  | Index of the probe to map (0-based, in the MRT Result's probe order). | `Integer` |
| Metric |  | UTCI, or PET on the temperate or humid assessment scale. PET uses the defaults of PET (Simulation): 35 years, average sex, 1.75 m, 75 kg, standing, 0.9 clo, 80 W, 1013.25 hPa. | `Text` |
| Folder |  | Where Export writes the files. Defaults to ~/Eddy3D/Charts. | `Text` |
| Export | E | Write the four maps as SVG, PDF and PNG into Folder. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Scenarios | S | The four scenario names, in the order of the Values branches. | `Text` |
| Values | V | The metric (°C) at every hour of the probe's year, one branch per scenario {scenario}(hours). | `Number` |
| Comfort % | % | Share of hours in the no-thermal-stress class, per scenario. | `Number` |
| Files | F | The SVG, PDF and PNG paths Export wrote. | `Text` |