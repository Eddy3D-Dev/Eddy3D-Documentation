# ![](/images/icons/LBM_Case.png) LBM Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Case%22)

![](/images/components/LBM_Case-crop.png)

Build a lattice-Boltzmann wind case from the ABL, the geometry and a settings object, and write it to disk. Wire 'LBM Run Settings' for OpenLB or 'FluidX3D Run Settings' for FluidX3D (nothing = OpenLB). Feed the Case output to LBM Run, then to Probe, LBM Field or FluidX3D Live View — the same Case → Run → Probe chain as the OpenFOAM wind study.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case folder name below Working Directory. Letters, numbers, hyphens, and underscores only. | `Text` |
| Working Directory | Dir | Parent directory for named LBM cases (optional; default ~/Eddy3D/Cases/LBM, or ~/Eddy3D/Cases/FluidX3D for the GPU engine). Must not contain spaces when running in a container (the case becomes a bind-mount source); the Native runtime has no such restriction. | `Text` |
| ABL |  | ABL inflow from the 'ABL Flow' component — the SAME boundary condition the OpenFOAM engines use (reference speed, reference height, roughness length, direction). Uses the first wind direction (one direction per case). | `Generic Data` |
| Domain |  | Simulation domain (optional). Accepts the Box Domain component's output — its Front/Back/Side/Top extensions override the auto margins (Cell Size and refinement are OpenFOAM meshing concepts and are ignored; lattice spacing comes from the settings) — or a plain Box, used verbatim as the domain extents. | `Generic Data` |
| Buildings | B | Building geometry. | `Mesh` |
| Terrain | T | Terrain / ground context meshes (optional; merged with the buildings). | `Mesh` |
| Vegetation | Veg | Tree crowns (optional; OpenLB only): closed solid meshes, or the Outdoor+ 'Vegetation Region' object — the SAME trees can drive the UMF case and this engine. Simulated as porous canopy cells that slow the wind without blocking it. Vegetation Region objects carry their own Cd x LAD; plain meshes use the Vegetation Drag setting. FluidX3D has no canopy model and ignores this input. | `Generic Data` |
| Settings | S | 'LBM Run Settings' (OpenLB) or 'FluidX3D Run Settings' (FluidX3D). Optional; nothing means OpenLB with defaults. | `Generic Data` |
| Write | W | Write the case to disk (STL + case files + launch script) without running it. | `Boolean` |
| Clear |  | Delete this named case folder and all of its contents — for FluidX3D also the results left in the shared source tree. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs | L | Case status / write log. | `Text` |
| Case | C | The LBM case: wire into LBM Run to launch it, and into Probe / LBM Field / FluidX3D Live View to read it (text sockets receive the case directory). | `Generic Data` |
| Domain | D | Resolved simulation domain in world coordinates (wind-aligned for OpenLB, world-aligned for FluidX3D). Updates live with the inputs — no Write needed; the standard preview renders it in the viewport. | `Box` |
| Folder | F | Case root folder: the OpenLB case directory, or the FluidX3D case root holding the source tree beside the VTK export directory that Case points at. | `Text` |