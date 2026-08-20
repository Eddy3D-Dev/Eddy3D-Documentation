# ![](/images/icons/Facade_Grid.png) Facade Grid - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Facade%20Grid%22)

Grids surfaces into analysis points with outward normals and per-cell areas, at a spacing suited to a single building rather than a district. Normals come from mesh face winding after Rhino's `UnifyNormals` — consistent across the mesh, but not provably outward for an open surface, which is why the Flip input exists.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Surfaces to grid: Breps, Surfaces or Meshes. | `Geometry` |
| Spacing | S | Grid spacing in model units. Default 1.0, which suits a facade; coarsen it for a district. | `Number` |
| Offset | O | Distance to push each point off its surface along the outward normal, so the surface does not shade its own grid. Default 0.05. | `Number` |
| Max Tilt | MT | Keep only faces whose normal is within this many degrees of horizontal — i.e. how far from VERTICAL a face may lean and still count as facade. Default 90, which keeps everything, so roofs and ground are included. | `Number` |
| Flip | F | Reverse every normal. Use when a surface's own orientation points into the building and the outward test could not tell — the Sun Path diagram makes this obvious. Default false. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | One point per cell, offset off the surface. | `Point` |
| Normals | N | Unit outward normal per point, aligned with Points. | `Vector` |
| Areas | A | Area each point represents — feed Sun Stats or Sunlight Compliance so results are weighted by area rather than by point count. | `Number` |
| Grid | G | The analysis mesh the points came from, for colouring results. | `Mesh` |
| Report | R | Cell count, total area and what was filtered out. | `Text` |
