# ![](/images/icons/CHT_Exterior_Air.png) CHT Exterior Air - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Exterior%20Air%22)

![](/images/components/CHT_Exterior_Air-crop.png)

A volume of air that is meshed but never solved: the solids facing it get the surface film set here. Cheaper and steadier than solving a cavity, and the ISO 10211 convention.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Closed Brep, Mesh or Box of the air volume (model units are metres). | `Generic Data` |
| Name | N | Region name (letters/digits, no spaces). | `Text` |
| Type | T | What the solids facing this volume see: a convective film, a fixed surface temperature, or adiabatic. | `Text` |
| Temperature | C | Ambient air temperature (Convective) or surface temperature (Fixed), in °C. | `Number` |
| Heat Transfer Coefficient | h | Film coefficient h (W/m²K), Convective only. ISO 6946: ~7.7 interior, ~25 exterior. | `Number` |
| Inside Point | P | Optional point strictly inside the volume. Unwired: derived automatically. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Exterior | E | Exterior air for the CHT Case component. | `Generic Data` |
| Inside Point | P | The point that names this region's mesh zone. | `Point` |