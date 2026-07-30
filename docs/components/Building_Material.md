# ![](/images/icons/Building_Material.png) Building Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Building%20Material%22)

![](/images/components/Building_Material-crop.png)

Select a building material from the list and override its properties.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | Select a material from the list. | `Text` |
| Density (rho) | Rho | Material density (rho). Optional; default is 1600. | `Number` |
| Heat Capacity (cap) | Cap | Heat capacity (cap). Optional; default is 1000. | `Number` |
| Thermal Conductivity 1 (lambda1) | Lam1 | Primary thermal conductivity (lambda1). Optional; default is 0.682. | `Number` |
| Thermal Conductivity 2 (lambda2) | Lam2 | Secondary thermal conductivity (lambda2). Optional; default is 0.0. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material Settings | Mat | Building material settings. | `Generic Data` |