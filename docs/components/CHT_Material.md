# ![](/images/icons/CHT_Material.png) CHT Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Material%22)

![](/images/components/CHT_Material-crop.png)

Solid material for CHT heat transfer analysis. Catalog values (ISO 10456 / Incropera) seed the properties; wire a number to override one.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | M | Material from the catalog. | `Text` |
| Conductivity | k | Thermal conductivity λ (W/m·K). Unwired: the catalog value. | `Number` |
| Density | rho | Density ρ (kg/m³). Unwired: the catalog value. | `Number` |
| Specific Heat | c | Specific heat capacity (J/kg·K). Unwired: the catalog value. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | M | Material for the CHT Solid component. | `Generic Data` |