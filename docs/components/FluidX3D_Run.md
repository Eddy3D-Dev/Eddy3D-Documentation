# ![](/images/icons/FluidX3D_Run.png) FluidX3D Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22FluidX3D%20Run%22)

![](/images/components/FluidX3D_Run-crop.png)

Prepare and launch a FluidX3D GPU wind simulation (builds the solver from source, runs on the GPU).  LICENSE: FluidX3D (ProjectPhysX) is free for NON-COMMERCIAL use only — public research, education, or personal use. Commercial use is not permitted. See the FluidX3D LICENSE.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case folder name below Working Directory. Letters, numbers, hyphens, and underscores only. | `Text` |
| Working Directory | Dir | Parent directory for named FluidX3D cases (optional; default ~/Eddy3D/Cases/FluidX3D). | `Text` |
| ABL |  | ABL inflow from the 'ABL Flow' component — the SAME boundary condition OpenFOAM uses. Supplies reference speed, reference height, roughness length and flow direction. Uses the first wind direction (FluidX3D runs one direction per case). | `Generic Data` |
| Domain |  | Simulation domain (optional). Accepts the Box Domain component's output — its Front/Back/Side/Top extensions override the auto margins (Cell Size and refinement are OpenFOAM meshing concepts and are ignored; resolution follows the VRAM budget) — or a plain Box, used verbatim as the domain extents. | `Generic Data` |
| Buildings | B | Building geometry to voxelize. | `Mesh` |
| Settings | S | FluidX3D run settings (optional; defaults used otherwise). | `Generic Data` |
| Clear |  | Delete this named case folder and all of its contents. | `Boolean` |
| Prepare | P | Build the case + solver from source (does not launch). | `Boolean` |
| Run | R | Prepare (if needed) and launch the GPU solver. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs | L | Run log / status. | `Text` |
| Folder | F | FluidX3D case root folder. | `Text` |
| Case | C | FluidX3D result (VTK directory) — plug into the Probe component's Case input. | `Text` |
| Domain | D | Resolved simulation domain in world coordinates. Updates live with the inputs — no Prepare needed; the standard preview renders it in the viewport. | `Box` |