# ![](/images/icons/PET_Simulation.png) PET (Simulation) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PET%20%28Simulation%29%22)

![](/images/components/PET_Simulation-crop.png)

Compute annual probe-specific PET (Höppe) from simulation outputs: MRT and wind-speed data trees, plus air temperature, relative humidity and the person. Solves in the background; cancel from the right-click menu. For a single point, use "Thermal Comfort".

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| MRT | M | The MRT component's Result (preferred), or a DataTree of annual MRT values — {probe}(8760) or {hour}(probes), both accepted. | `Generic Data` |
| Wind Speed | V | Wind speed as an AnnualWindField (the VAF component's Wind Speed output — fed by CFD probe vectors or the ML Wind Predictor alike), one spatial list (one value per probe, held for all hours), or a {probe}(hours) / {hour}(probes) tree. An AnnualWindField on a different grid than the MRT sensors is resampled by nearest neighbor when both carry points. PET takes the wind AT the body, so pedestrian-height speeds are used as they are (UTCI lifts them to 10 m; PET does not). Defaults to calm (0.5 m/s) when unconnected. | `Generic Data` |
| Air Temperature | T | Annual hourly ambient air temperature (8760 values, °C). | `Number` |
| Relative Humidity | RH | Annual hourly relative humidity (8760 values, %). | `Number` |
| Pressure | Press | Air pressure [hPa]. | `Number` |
| Age |  | Age [years]. | `Integer` |
| Sex |  | Male, Female, or Average. | `Text` |
| Height |  | Body height [m]. | `Number` |
| Weight |  | Body weight [kg]. | `Number` |
| Body Position | Pos | Standing, Sitting, or Crouching. | `Text` |
| Clothing Insulation | Icl | Clothing insulation [clo]. | `Number` |
| Metabolic Rate | MET | Metabolic rate [W]. | `Number` |
| Climate Type | Climate | Assessment scale: Temperate (Matzarakis & Mayer) or Humid (Lin & Matzarakis, shifted +8..+10 °C). Changes only how PET is classified as comfortable, never the PET value. | `Text` |
| Transpose |  | Orientation of the PET tree output. Hours × Probes (default): one branch per hour, each holding every probe's value. Probes × Hours: one branch per probe, each holding that probe's year. | `Text` |
| Run | R | Start the annual PET solve. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| PET |  | PET data tree. Default: {hour}(probes). With Transpose off: {probe}(hours). Only built while this output is WIRED: for a few thousand probes the full year is tens of millions of values on the canvas, and constructing them — not the PET model — is the wait. Prefer the Result output with Deconstruct UTCI. | `Number` |
| Comfort Hours | H | No-thermal-stress hours per probe on the chosen climate's PET scale. | `Integer` |
| Comfort % | % | Comfort percentage per probe. | `Number` |
| Result |  | The complete annual PET solve as ONE item — feed to Deconstruct UTCI for statistics, comfort hours/% over any hour selection, or straight into the Thermal Comfort Legend for a map (its PET bands follow the Climate Type). Carries the MRT probes' positions when the MRT input was a Result. | `Generic Data` |