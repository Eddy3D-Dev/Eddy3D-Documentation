# ![](/images/icons/Grass.png) Grass - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Grass%22)

![](/images/components/Grass-crop.png)

Define grass patches and parameters for the terrain. OutdoorPlus

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Boundary |  | Closed curves for grass areas (projected onto the terrain mesh). |
| Cd |  | Grass drag coefficient (Cd). Optional; default is 0.2. |
| LAI |  | Leaf area index (LAI). Optional; default is 2. |
| LAD |  | Leaf area density (LAD). Optional; default is 1. |
| EvapSides |  | Evaporation sides parameter (nEvapSides). Optional; default is 1. |
| Beta |  | Beta parameter. Optional; default is 0.5. |
| BetaLW |  | Longwave beta parameter (betaLW). Optional; default is 1000. |
| Albedo |  | Soil albedo (albedoSoil). Optional; default is 0.4. |
| rs |  | Grass surface resistance to evapotranspiration (rs) [s/m]. Optional; default is 250 (matches the OpenFOAM 12 urbanMicroclimateFoam tutorials). |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Grass |  | Grass settings for the case. |
