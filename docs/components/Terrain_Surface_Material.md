# ![](/images/icons/Terrain_Surface_Material.png) Terrain Surface Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Terrain%20Surface%20Material%22)

![](/images/components/Terrain_Surface_Material-crop.png)

Select a terrain surface material from the list and override its properties. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | Select a material from the list. | `Text` |
| Density (rho) | Rho | Material density (rho). Optional; default is 1980. | `Number` |
| Heat Capacity (cap) | Cap | Heat capacity (cap). Optional; default is 820. | `Number` |
| Thermal Conductivity 1 (lambda1) | Lam1 | Primary thermal conductivity (lambda1). Optional; default is 1.35. | `Number` |
| Thermal Conductivity 2 (lambda2) | Lam2 | Secondary thermal conductivity (lambda2). Optional; default is 0.0. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surface Material Settings | Mat | Terrain surface material settings. | `Generic Data` |