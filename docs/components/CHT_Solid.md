# ![](/images/icons/CHT_Solid.png) CHT Solid - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Solid%22)

![](/images/components/CHT_Solid-crop.png)

A solid region of the CHT assembly: closed Brep/Mesh + material. The union of all solids and cavities must fill a rectangular box (the analysis domain).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Closed Brep, Mesh or Box of this body (model units are metres). | `Generic Data` |
| Name | N | Region name (letters/digits, no spaces) — appears in results and ParaView. | `Text` |
| Material | M | Material from the CHT Material component. | `Generic Data` |
| Inside Point | P | Optional point strictly inside the body. Unwired: derived automatically. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Solid | S | Solid region for the CHT Case component. | `Generic Data` |
| Inside Point | P | The point that names this region's mesh zone — check it sits inside the body. | `Point` |