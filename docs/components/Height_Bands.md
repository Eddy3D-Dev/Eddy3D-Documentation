# ![](/images/icons/Height_Bands.png) Height Bands - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Height%20Bands%22)

![](/images/components/Height_Bands-crop.png)

Refine the mesh in BANDS OF HEIGHT above the ground — level 3 within 4 m, level 2 within 10 m, level 1 within 24 m — everywhere on the site, not only near buildings. This is how the pedestrian layer gets resolved across open plazas and streets that no building refinement reaches. The bands follow the case's ground surfaces (terrain, ground ring and roughness zones), so on a sloped site they stay the same height above the ground; only a meshing dict with no ground surface gets the flat disk Centre and Radius describe. Wire Extras into the case component's Extras input beside any Refinement Region.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Heights | H | Band upper edges above ground (m), e.g. 4, 10, 24. Each gets the level at the same position in Levels; levels must not INCREASE with height. | `Number` |
| Levels | L | snappyHexMesh refinement level per band, aligned with Heights, e.g. 3, 2, 1 (each level halves the cell size). A single value applies to every band. | `Integer` |
| Centre | C | Optional centre of the ground disk (its Z is the ground level), used only when the case has no ground surface to follow. Default: the origin at Z = 0. | `Point` |
| Radius | R | Radius (m) of the ground disk, used only when the case has no ground surface to follow (the bands then cover the whole ground). Beyond the rim, cells are refined by their distance to the rim instead of to the ground. | `Number` |
| Name |  | Region key (a valid OpenFOAM word). | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Extras |  | The height-band region as case extras — wire into the case component's Extras input. | `Generic Data` |
| Status |  | What was defined. | `Text` |