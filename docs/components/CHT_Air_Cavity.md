# ![](/images/icons/CHT_Air_Cavity.png) CHT Air Cavity - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Air%20Cavity%22)

![](/images/components/CHT_Air_Cavity-crop.png)

A closed air cavity: solved as buoyant air (natural convection), coupled to the solids around it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Closed Brep, Mesh or Box of the air volume (model units are metres). | `Generic Data` |
| Name | N | Region name (letters/digits, no spaces). | `Text` |
| Inside Point | P | Optional point strictly inside the cavity. Unwired: derived automatically. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Cavity | C | Air cavity for the CHT Case component. | `Generic Data` |
| Inside Point | P | The point that names this region's mesh zone. | `Point` |