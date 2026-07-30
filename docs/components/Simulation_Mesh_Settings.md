# ![](/images/icons/Simulation_Mesh_Settings.png) Simulation Mesh Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Simulation%20Mesh%20Settings%22)

![](/images/components/Simulation_Mesh_Settings-crop.png)

Configure snappyHexMesh settings for the simulation. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Add Layers | AddLayers | Enable prism layers. Optional; default is true. | `Boolean` |
| Box Refinement Level | BoxLvl | Refinement level inside the refinement box. Optional; default is 2. | `Integer` |
| Min Refinement Cells | MinCells | Minimum refinement of cells. Optional; default is 0. | `Integer` |
| Max Load Unbalance | MaxUnbal | Maximum load unbalance. Optional; default is 0.10. | `Number` |
| Cells Between Levels | CellsBetween | Number of cells between refinement levels. Optional; default is 2. | `Integer` |
| Resolve Feature Angle | FeatAngle | Feature angle for edge detection (deg). Optional; default is 10. | `Number` |
| Snap Tolerance | SnapTol | Snap tolerance. Optional; default is 1.0. | `Number` |
| Snap Solver Iterations | SnapSolve | Solver iterations for snapping. Optional; default is 80. | `Integer` |
| Snap Relax Iterations | SnapRelax | Relaxation iterations for snapping. Optional; default is 8. | `Integer` |
| Snap Feature Iterations | SnapFeat | Feature snap iterations. Optional; default is 20. | `Integer` |
| Included Angle | InclAngle | Identify a feature when face angle < includedAngle (deg). Optional; default is 90. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Simulation Mesh Settings | Mesh | Simulation mesh settings for snappyHexMesh. | `Generic Data` |