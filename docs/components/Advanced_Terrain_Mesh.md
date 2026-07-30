# ![](/images/icons/Advanced_Terrain_Mesh.png) Advanced Terrain Mesh - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Advanced%20Terrain%20Mesh%22)

![](/images/components/Advanced_Terrain_Mesh-crop.png)

Generate a multi-resolution terrain mesh from input geometry with a solid base. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | Geo | Input geometry used to generate the terrain mesh. | `Brep` |
| Inner Scale | Inner | Scale factor for the high-detail inner region. Optional; default is 0.5. | `Number` |
| Outer Scale | Outer | Scale factor for the low-detail outer region. Optional; default is 1.2. | `Number` |
| Base Height | Base | Height of the solid base below the terrain. Optional; default is 10. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Terrain Mesh | Mesh | Generated terrain mesh. | `Mesh` |