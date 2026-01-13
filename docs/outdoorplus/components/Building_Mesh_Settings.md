## ![](../images/icons/Building_Mesh_Settings.png) Building Mesh Settings

![](../images/components/Building_Mesh_Settings-crop.png)

Configure mesh refinement for building regions. OutdoorPlus 0.0.20.0

#### Input
* ##### FeatLvl 
Feature refinement level for extracted edges. Optional; default is 4.
* ##### SurfMin 
Minimum surface refinement level. Optional; default is 3.
* ##### SurfMax 
Maximum surface refinement level. Optional; default is 5.
* ##### RegDistMin 
Outer distance for the lower region refinement level. Optional; default is 2.
* ##### RegMin 
Lower region refinement level. Optional; default is 4.
* ##### RegDistMax 
Inner distance for the higher region refinement level. Optional; default is 1.
* ##### RegMax 
Upper region refinement level. Optional; default is 5.
* ##### Layers 
Number of prism layers to add. Optional; default is 3.

#### Output
* ##### Mesh
Building mesh settings for snappyHexMesh.