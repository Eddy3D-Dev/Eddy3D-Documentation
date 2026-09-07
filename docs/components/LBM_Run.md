# ![](/images/icons/LBM_Run.png) LBM Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Run%22)

![](/images/components/LBM_Run-crop.png)

Launch a lattice-Boltzmann case from the LBM Case component (OpenLB in a container or natively, or FluidX3D on the GPU — whichever the case was built with). Writes the case first if it has not been written, then opens the solver in a terminal window. Read results with Probe (points), LBM Field (the probe layer) or FluidX3D Live View.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | The LBM case from the LBM Case component. | `Generic Data` |
| Run | R | Write the case (if needed) and launch the solver in a terminal window. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs | L | Run log / status. | `Text` |
| Case | C | Case directory the readers resolve against (the OpenLB case, or the FluidX3D VTK export directory) — plug into Probe, LBM Field or FluidX3D Live View. | `Text` |
| Domain | D | Resolved simulation domain in world coordinates, as on the LBM Case component. | `Box` |
| Folder | F | Case root folder: the OpenLB case directory, or the FluidX3D case root holding the source tree beside the VTK export directory that Case points at. | `Text` |