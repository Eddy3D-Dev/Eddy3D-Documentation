# ![](/images/icons/Refinement_Region.png) Refinement Region - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Refinement%20Region%22)

![](/images/components/Refinement_Region-crop.png)

Define a custom snappyHexMesh refinement region (a box, solid or surface) — refines the cells inside/near the geometry to the chosen level. Wire Extras into a case component so the region is written every time the case is written; or wire a written Case in and press Apply to edit the dictionaries in place (which a later re-write undoes).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Optional. An already-written case to edit in place — any Eddy3D OpenFOAM case (wind, Outdoor+ microclimate, indoor, CHT) or a loaded study. Leave it empty and wire the Extras output into the case component instead, which is the durable route: a region applied here is erased the next time the case is written. | `Generic Data` |
| Geometry | Geo | The region geometry: a Box/closed Brep/Mesh (use mode inside/outside) or an open surface (use mode distance). Written as an STL into the mesh case. | `Generic Data` |
| Name |  | Region key (a valid OpenFOAM word, e.g. "towerWake"). | `Text` |
| Level | Lvl | snappyHexMesh refinement level inside/near the region (e.g. 2). Default 2. | `Integer` |
| Mode |  | inside (refine the whole closed region), outside (refine everything outside it), or distance (refine within Distance metres of the surface). Default inside. | `Text` |
| Distance | Dist | For distance mode: refinement band width in metres. Default 10. | `Number` |
| Bake | Apply | Write the region STL and snappyHexMeshDict entries into the wired Case's already-written dictionaries (idempotent). Momentary button; re-run meshing afterward to apply the new region. Not needed for the Extras route, which writes the region with the case. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Status |  | What was written, and where. | `Text` |
| Extras |  | The refinement region as case data. Wire this into a case component's Extras input so it is written into snappyHexMeshDict every time the case is written — including after a re-write, which is what editing the dictionaries in place cannot survive. | `Generic Data` |