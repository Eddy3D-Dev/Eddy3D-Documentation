# ![](/images/icons/HAM_Material.png) HAM Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22HAM%20Material%22)

![](/images/components/HAM_Material-crop.png)

Porous material for a HAM wall: a hamFoam material model plus density, specific heat and conductivity. The five HAMSTAD benchmark models arrive with their published properties; the rest supply curves only, so wire rho, c and lambda1.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Model | M | hamFoam buildingMaterialModel — the moisture retention and permeability curves. Compiled into the solver image; only these names exist. | `Text` |
| Density | rho | Density ρ (kg/m³). Unwired: the catalogued value, where the model has one. | `Number` |
| Specific Heat | c | Specific heat capacity (J/kg·K). Unwired: the catalogued value. | `Number` |
| Lambda Dry | L1 | Dry thermal conductivity λ1 (W/m·K). Unwired: the catalogued value. | `Number` |
| Lambda Moisture | L2 | Moisture-dependent conductivity λ2 (W·m²/kg·K), used as λ = λ1 + ws·λ2. Unwired: the catalogued value (0 for a model with no moisture term). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | M | Material for the HAM Wall component. | `Generic Data` |