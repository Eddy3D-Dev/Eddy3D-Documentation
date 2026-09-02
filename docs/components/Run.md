# ![](/images/icons/Run.png) Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Run%22)

![](/images/components/Run-crop.png)

Mesh and run an OpenFOAM case on the selected engine (wind / indoor / UMF).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | An OpenFOAM case to run (wind study, indoor case, or UMF case). | `Generic Data` |
| Mesh | M | Mesh only. | `Boolean` |
| Simulate | S | Simulation only. | `Boolean` |
| Run All | R | Mesh, then run the simulation. | `Boolean` |
| Parallel | P | Run in parallel (decompose / MPI). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs | L | Run logs. | `Text` |