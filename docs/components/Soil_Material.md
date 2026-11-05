# ![](/images/icons/Soil_Material.png) Soil Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Soil%20Material%22)

![](/images/components/Soil_Material-crop.png)

Define soil material properties for terrain layers. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Density (rho) | Rho | Material density (rho) [kg/m³]. | `Number` |
| Heat Capacity (cap) | Cap | Specific heat capacity (cap) [J/kgK]. | `Number` |
| Thermal Conductivity 1 (lambda1) | Lam1 | First coefficient of thermal conductivity (lambda1) [W/mK]. Used in the formula: lambda = lambda1 + lambda2 * ws (where ws is moisture content). | `Number` |
| Thermal Conductivity 2 (lambda2) | Lam2 | Second coefficient of thermal conductivity (lambda2) [W/mK]. Used in the formula: lambda = lambda1 + lambda2 * ws (where ws is moisture content). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Soil Material Settings | Mat | Soil material settings for terrain layers. | `Generic Data` |