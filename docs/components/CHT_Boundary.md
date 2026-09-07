# ![](/images/icons/CHT_Boundary.png) CHT Boundary - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Boundary%22)

![](/images/components/CHT_Boundary-crop.png)

Boundary condition on one face of the analysis box: fixed surface temperature, convective film (h + air temperature), or adiabatic. Unassigned faces are adiabatic.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Face | F | Which face of the analysis box this boundary applies to. | `Text` |
| Type | T | Boundary type. | `Text` |
| Temperature | C | Surface temperature (Fixed) or ambient air temperature (Convective), in °C. | `Number` |
| Heat Transfer Coefficient | h | Film coefficient h (W/m²K), Convective only. ISO 6946: ~7.7 interior, ~25 exterior. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary | B | Boundary for the CHT Case component. | `Generic Data` |