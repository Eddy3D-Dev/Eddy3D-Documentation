# ![](/images/icons/LBM_Run.png) LBM Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Run%22)

![](/images/components/LBM_Run-crop.png)

Prepare and launch a container-based OpenLB wind simulation (Smagorinsky LES, time-averaged pedestrian wind field). Uses the same ABL inflow object as the OpenFOAM and FluidX3D engines. Needs Docker Desktop or podman; the solver image is pulled on first run.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case folder name below Working Directory. Letters, numbers, hyphens, and underscores only. | `Text` |
| Working Directory | Dir | Parent directory for named LBM cases (optional; default ~/Eddy3D/Cases/LBM). Must not contain spaces when running in a container (the case becomes a bind-mount source); the Native runtime has no such restriction. | `Text` |
| ABL |  | ABL inflow from the 'ABL Flow' component — the SAME boundary condition the OpenFOAM engines use (reference speed, reference height, roughness length, direction). Uses the first wind direction (one direction per case). | `Generic Data` |
| Domain |  | Simulation domain (optional). Accepts the Box Domain component's output — its Front/Back/Side/Top extensions override the auto margins (Cell Size and refinement are OpenFOAM meshing concepts and are ignored; lattice spacing comes from the LBM settings) — or a plain Box, used verbatim as the domain extents. | `Generic Data` |
| Probes | Pts | Probe points, OpenFOAM-style (optional): the solver samples the time-averaged wind at EXACTLY these world-frame locations, in this order, instead of the default grid (the full domain at Probe Height). Wire the same sensor points you would probe an OpenFOAM case with; LBM Field returns them in the same order. | `Point` |
| Buildings | B | Building geometry. | `Mesh` |
| Terrain | T | Terrain / ground context meshes (optional; merged with the buildings). | `Mesh` |
| Vegetation | Veg | Tree crowns (optional): closed solid meshes, or the Outdoor+ 'Vegetation Region' object — the SAME trees can drive the UMF case and this engine. Simulated as porous canopy cells that slow the wind without blocking it. Vegetation Region objects carry their own Cd x LAD; plain meshes use the Vegetation Drag setting. | `Generic Data` |
| Settings | S | LBM run settings (optional; defaults used otherwise). | `Generic Data` |
| Clear |  | Delete this named case folder and all of its contents. | `Boolean` |
| Prepare | P | Write the case (STL + case.xml + launch script) without running. | `Boolean` |
| Run | R | Prepare (if needed) and launch the solver container in a terminal window. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs | L | Run log / status. | `Text` |
| Case | C | LBM case directory — plug into the 'LBM Field' component to read results. | `Text` |
| Domain | D | Resolved simulation domain in world coordinates (wind-aligned, matching how the lattice actually sits around the buildings). Updates live with the inputs — no Prepare needed; the standard preview renders it in the viewport. | `Box` |
| Folder | F | Case ROOT folder. Identical to Case for OpenLB; for FluidX3D it is the parent that holds the FluidX3D source tree beside the VTK export directory that Case points at. | `Text` |