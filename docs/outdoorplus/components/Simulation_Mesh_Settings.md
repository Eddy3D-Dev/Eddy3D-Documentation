## ![](../images/icons/Simulation_Mesh_Settings.png) Simulation Mesh Settings

![](../images/components/Simulation_Mesh_Settings-crop.png)

Configure snappyHexMesh settings for the simulation. OutdoorPlus 0.0.20.0

#### Input
* ##### AddLayers 
Enable prism layers. Optional; default is true.
* ##### BoxLvl 
Refinement level inside the refinement box. Optional; default is 2.
* ##### MinCells 
Minimum refinement of cells. Optional; default is 0.
* ##### MaxUnbal 
Maximum load unbalance. Optional; default is 0.10.
* ##### CellsBetween 
Number of cells between refinement levels. Optional; default is 2.
* ##### FeatAngle 
Feature angle for edge detection (deg). Optional; default is 10.
* ##### SnapTol 
Snap tolerance. Optional; default is 1.0.
* ##### SnapSolve 
Solver iterations for snapping. Optional; default is 80.
* ##### SnapRelax 
Relaxation iterations for snapping. Optional; default is 8.
* ##### SnapFeat 
Feature snap iterations. Optional; default is 20.
* ##### InclAngle 
Identify a feature when face angle < includedAngle (deg). Optional; default is 90.

#### Output
* ##### Mesh
Simulation mesh settings for snappyHexMesh.