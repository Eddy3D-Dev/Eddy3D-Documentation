# ![](/images/icons/Create_Mesh.png) Create Mesh - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Create%20Mesh%22)

![](/images/components/Create_Mesh-crop.png)

Create a visualization mesh from polyMesh point/face data. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | UMF case used to locate the mesh data. | `Generic Data` |
| Region |  | Region name to visualize. | `Text` |
| Face Indices | Faces | Optional face indices to visualize. | `Integer` |
| Run |  | Generate the mesh when true. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Unified Mesh | Mesh | Generated unified mesh. | `Mesh` |
| Mesh Data | Data | Geometric and topological mesh data. | `Generic Data` |
| Number of Faces | FaceCount | Total face count in the polyMesh. | `Integer` |
| Number of Points | PointCount | Total point count in the polyMesh. | `Integer` |