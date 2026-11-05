# ![](/images/icons/Geometry_Repair.png) Geometry Repair - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Geometry%20Repair%22)

![](/images/components/Geometry_Repair-crop.png)

Check building geometry and repair it for snappyHexMesh: weld split vertices, remove degenerate and duplicate faces (and the shared walls of touching solids), orient every closed piece outward, optionally fill small holes and drop specks, then optionally rebuild it as a closed, manifold voxel WRAP — overlapping buildings fuse into one solid, courtyards open to the sky stay open, gaps narrower than about the wrap cell close. Runs in-process (no Python service). The case components already run the safe part automatically before meshing; use this to see what is wrong, to fill holes, or to wrap.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | Geometry to check and repair (all inputs are merged). Breps: mesh them first. | `Mesh` |
| Weld Tolerance | Tol | Corners closer than this are merged into one (model units). 0 merges exact duplicates only. Default 0.001 (1 mm in metres, Rhino's default tolerance). | `Number` |
| Max Hole Size | Hole | Close holes whose rim fits in this size (diagonal of the rim's bounds). 0 leaves every hole open. | `Number` |
| Min Piece Size | Min | Drop disconnected pieces smaller than this (diagonal of their bounds). 0 keeps every piece. | `Number` |
| Wrap |  | Replace the result by its closed voxel wrap: Off, If Leaky (only when the repaired mesh is still not watertight) or Always (also fuses overlapping buildings into one solid). | `Text` |
| Wrap Cell Size | Cell | Voxel size of the wrap. Features and gaps narrower than about this close; each block is wrapped in its own grid, coarsened (and said so) above 24M voxels. Use about half the snappyHexMesh cell at the building surface. | `Number` |
| Smoothing | Smooth | Taubin smoothing passes over the wrap's staircase (0 = none). Each corner stays within 0.3 cells of where it was; a pass that would fold a face is undone. | `Integer` |
| Run |  | Check and repair (and wrap). Resets when the run starts; a wired toggle held true re-runs when the geometry changes. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | The repaired (or wrapped) mesh. | `Mesh` |
| Watertight | WT | True when the result is closed, manifold and consistently oriented. | `Boolean` |
| Report | R | What was found before, what was changed, and what remains. | `Text` |
| Open Edges | Open | Open (boundary) edges of the INPUT: the rims of holes and gaps. | `Line` |
| Non-Manifold Edges | NM | Edges of the INPUT shared by three or more faces (fins, touching solids, internal walls). | `Line` |
| Bad Faces | Bad | Degenerate and duplicate faces of the INPUT. | `Mesh` |