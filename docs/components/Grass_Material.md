# ![](/images/icons/Grass_Material.png) Grass Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Grass%20Material%22)

![](/images/components/Grass_Material-crop.png)

Create a soil-backed grass surface material for the urbanMicroclimateFoam terrain heat, radiation, and evapotranspiration model. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Density |  | Soil substrate density [kg/m³]. | `Number` |
| Heat Capacity | HeatCap | Soil substrate specific heat capacity [J/(kg·K)]. | `Number` |
| Dry Conductivity | Lambda1 | Soil substrate dry thermal conductivity [W/(m·K)]. | `Number` |
| Moisture Conductivity | Lambda2 | Moisture-dependent conductivity coefficient. | `Number` |
| Drag Coefficient | Cd | Grass drag coefficient. | `Number` |
| Leaf Area Index | LAI | Grass leaf area index. | `Number` |
| Leaf Area Density | LAD | Grass leaf area density [1/m]. | `Number` |
| Evaporation Sides | EvapSides | Number of evaporating leaf sides (1 or 2). | `Integer` |
| Shortwave Extinction | Beta | Shortwave extinction coefficient. | `Number` |
| Longwave Exchange | BetaLW | Longwave exchange coefficient. | `Number` |
| Soil Albedo | Albedo | Shortwave albedo of the soil below the grass (0–1). | `Number` |
| Surface Resistance | Resistance | Grass surface resistance to evapotranspiration [s/m]. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Grass Material | Material | Soil substrate and simpleGrass settings for the Terrain Region Surface Material input. | `Generic Data` |