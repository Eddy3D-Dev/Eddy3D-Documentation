# ![](/images/icons/Terrain_Region.png) Terrain Region - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Terrain%20Region%22)

![](/images/components/Terrain_Region-crop.png)

Create a terrain region with materials and depth settings. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surface Material | SurfMat | Material settings for the surface layer. | `Generic Data` |
| Soil Material | SoilMat | Material settings for the soil layer. | `Generic Data` |
| Surface Depth | SurfDepth | Surface layer depth. Optional; default is 0.1. | `Number` |
| Soil Depth | SoilDepth | Soil layer depth. Optional; default is 1.9. | `Number` |
| Terrain Temperature | Temp | Initial terrain temperature (deg C). Optional; default is 25. | `Number` |
| Mesh Settings | MeshSet | Optional meshing settings for the terrain region. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Terrain Region | Terrain | Terrain region object for the case. | `Generic Data` |