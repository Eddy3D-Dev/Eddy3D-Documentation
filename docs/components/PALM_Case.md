# ![](/images/icons/PALM_Case.png) PALM Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Case%22)

![](/images/components/PALM_Case-crop.png)

Write the PALM-4U case: the static driver (terrain, buildings, tree canopies and the ground surface mosaic, rasterized onto the domain grid) and the _p3d namelist that runs it. Geometry inputs take trees of meshes/Breps; branches are flattened — everything wired belongs to ONE scene. Ground not covered by any input takes the Ground Cover class. The viewport shows the domain, its boundary conditions and the rasterized surface the solver will actually see.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Case | The case folder under Working Directory. Empty mints a session name shared by every PALM component on this document. | `Text` |
| Working Directory | Dir | The root the case folder sits under; empty uses ~/Eddy3D/PALM. | `Text` |
| Domain | D | The PALM Domain to rasterize onto. | `Generic Data` |
| Buildings | B | Building solids or roof surfaces; each ITEM becomes one building id. Branches are flattened. | `Geometry` |
| Trees | Tr | Tree crown volumes (closed meshes/Breps); each becomes leaf area density between its bottom and top. Branches are flattened. | `Geometry` |
| Terrain | T | Terrain surface (mesh or Brep). Branches are flattened. Empty means flat ground. | `Geometry` |
| Vegetation | V | Ground painted as vegetation, using the Vegetation Type. Branches are flattened. | `Geometry` |
| Pavement | P | Ground painted as pavement (streets, plazas). Branches are flattened. | `Geometry` |
| Water | W | Ground painted as water. Branches are flattened. | `Geometry` |
| Land Cover | LC | PALM Land Cover patches (OSM). Painted below the explicit geometry above. | `Generic Data` |
| Building Type | BT | PALM building_type for every building: construction era and use drive the wall, roof and window properties the urban surface model applies. | `Text` |
| Vegetation Type | VT | Class for ground wired into Vegetation. | `Text` |
| Pavement Type | PT | Class for ground wired into Pavement. | `Text` |
| Water Type | WT | Class for ground wired into Water. | `Text` |
| Ground Cover | G | What UNCLAIMED ground becomes — always a vegetation class, because unpainted urban ground is far more often grass than asphalt; paint pavement, never assume it. | `Text` |
| Soil Type | ST | PALM soil_type under every vegetation and pavement cell — drives the soil column's heat and moisture transport. | `Text` |
| Leaf Area Density | LAD | Leaf area density written inside tree crowns (m² m⁻³). 1–2 is a typical broadleaf canopy. | `Number` |
| Settings | S | PALM Settings — duration, wind, temperature, outputs. Written into the _p3d beside the driver, so a settings change needs a re-Write before it can reach a run. Empty writes the defaults (2 h, 3 m/s westerly, comfort on). | `Generic Data` |
| Write | Wr | Rasterize and write the static driver and the _p3d namelist into the case's INPUT folder. | `Boolean` |
| Clear | Cl | Delete this case's PALM artifacts — the JOBS tree (driver, namelist, results, monitoring), the live-run tmp tree and the launch script. The case folder itself and anything else in it are left alone. Refused while a run looks active. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Driver | Dr | The written case (driver path + namelist + contents summary). Feed to PALM Run. | `Generic Data` |
| Path | P | Where the driver was written. | `Text` |
| Report | R | What was rasterized: cell counts per class, terrain shift, the boundary conditions and the forcing, and anything skipped. | `Text` |
| Namelist | Nl | The _p3d this case writes, as text — the same string that goes to disk on Write. | `Text` |
| Domain Box | Box | The simulation domain as a box in model space. | `Box` |