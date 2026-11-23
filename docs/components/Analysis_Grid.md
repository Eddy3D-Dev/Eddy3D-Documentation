# ![](/images/icons/Analysis_Grid.png) Analysis Grid - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Analysis%20Grid%22)

![](/images/components/Analysis_Grid-crop.png)

Analysis points with outward normals and per-cell areas over terrain and building surfaces, on one regular grid.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Surfaces to grid: Breps, Surfaces or Meshes — terrain and buildings together. A mesh is resampled at Spacing. Cells inside a closed solid or under the ground are left out. | `Geometry` |
| Spacing | S | Grid spacing in model units. 1.0 suits a facade; coarsen it for a district. | `Number` |
| Offset | O | Distance to push each point off its surface along the outward normal, so the surface does not shade its own grid. | `Number` |
| Max Tilt | MT | Keep only faces whose normal is within this many degrees of horizontal — i.e. how far from VERTICAL a face may lean and still count as facade. 90 keeps everything, so roofs and ground are included. | `Number` |
| Flip | F | Reverse every normal. Use when a surface's own orientation points into the building and the outward test could not tell — the Sun Path diagram makes this obvious. | `Boolean` |
| Ground Height | Height | Lift for cells that face up (ground, roofs): straight up by this much, instead of Offset. 1.1 puts ground points at body height while walls keep Offset. 0 = Offset everywhere. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | One point per cell, offset off the surface. | `Point` |
| Normals | N | Unit outward normal per point, aligned with Points. | `Vector` |
| Areas | A | Area each point represents — feed Sun Stats or Sunlight Compliance so results are weighted by area rather than by point count. | `Number` |
| Grid | G | The analysis mesh the points came from, for colouring results. | `Mesh` |
| Report | R | Cell count, total area and what was filtered out. | `Text` |