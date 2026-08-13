# ![](/images/icons/Gmsh_Mesh.png) Gmsh Mesh - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Gmsh%20Mesh%22)

![](/images/components/Gmsh_Mesh-crop.png)

Creates a STL mesh from geometry using the gmsh application. Useful to create healthy mesh topologies for building elements.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Brep | B | Brep geometry to mesh | `Brep` |
| Max Size | Max | Maximum element size. Default value: 1.0. | `Number` |
| Min Size | Min | Minimum element size. Default value: 0.5. | `Number` |
| Run |  | Run the gmsh process | `Boolean` |
| Remove bottom faces | RBF | If true, delete bottom faces located on the XY plane (Z=0). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | The resulting STL mesh | `Mesh` |
| Logs | L | Execution logs from gmsh | `Text` |