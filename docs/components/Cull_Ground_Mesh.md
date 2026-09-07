# ![](/images/icons/Cull_Ground_Mesh.png) Cull Ground Mesh - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Cull%20Ground%20Mesh%22)

![](/images/components/Cull_Ground_Mesh-crop.png)

Cut building footprints out of a ground mesh to make an analysis ground mesh. The ground is quad-remeshed to Target Face Count (or taken as wired when that is 0), then every vertex under a building is removed together with the faces that use it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Building Mesh | Bldgs | Building meshes (joined internally). A ground vertex is culled when the vertical line through it pierces one of these faces, so the roofs are what matter; open-bottomed footprint extrusions are fine. | `Mesh` |
| Ground Mesh | Ground | Ground mesh(es) to cull. Remeshed to Target Face Count first, or culled exactly as wired when that is 0. | `Mesh` |
| Target Face Count | Target | Quad count QuadRemesh aims for before culling. 0 skips the remesh and culls the ground mesh as wired, so a hand-built grid keeps its faces. Default: 50000. | `Integer` |
| Triangulate | Tri | Shrink quads at the cut edge into triangles instead of dropping them, so the cut-out hugs the footprint. Off removes every face that touched a culled vertex. Does not triangulate the rest of the mesh. Default: true. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Culled Mesh | Mesh | Ground mesh with building footprints removed. | `Mesh` |