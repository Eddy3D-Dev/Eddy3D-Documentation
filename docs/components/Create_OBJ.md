# ![](/images/icons/Create_OBJ.png) Create OBJ - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Create%20OBJ%22)

![](/images/components/Create_OBJ-crop.png)

Export an OBJ mesh from a polyMesh description. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh Data | Data | Geometric and topological mesh data (UMFMesh). | `Generic Data` |
| File Name | File | Output OBJ file name or path. | `Text` |
| Face Indices | Faces | Optional face indices to include in the OBJ. | `Integer` |
| Write |  | Write the OBJ file when true. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Output Info | Info | OBJ export result message. | `Text` |
| Mesh Data | Data | Geometric and topological mesh data. | `Generic Data` |