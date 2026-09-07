# ![](/images/icons/HAM_Wall.png) HAM Wall - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22HAM%20Wall%22)

![](/images/components/HAM_Wall-crop.png)

Layered build-up for a HAM case, OUTSIDE layer first. Materials and thicknesses are read in parallel, so their counts must match.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Materials | M | Materials from HAM Material, OUTSIDE layer first. Branches are flattened — the whole wire makes one wall. | `Generic Data` |
| Thicknesses | T | Layer thicknesses (m), in the same order as Materials. Branches are flattened. | `Number` |
| Names | N | Optional layer names (letters, digits, - and _; no spaces). They become cellZone names in the case. Unwired: derived from the material models. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wall | W | Build-up for the HAM Case component. | `Generic Data` |
| Thickness | T | Total build-up thickness (m). | `Number` |