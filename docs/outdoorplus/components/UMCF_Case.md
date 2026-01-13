## ![](../images/icons/UMCF_Case.png) UMCF Case

![](../images/components/UMCF_Case-crop.png)

Create, read, and manage an OutdoorPlus (UMCF) case. OutdoorPlus 0.0.20.0

#### Input
* ##### Read 
Read an existing case from the working directory.
* ##### Write 
Write the case files to the working directory.
* ##### Clear 
Delete all files for this case in the working directory.
* ##### Name 
Case folder name (no spaces).
* ##### Dir 
Folder for case files and results.
* ##### Air 
Air region for this case.
* ##### Vegetation 
Vegetation region for this case.
* ##### Building 
Building (solid) region for this case.
* ##### Terrain 
Terrain region for this simulation (optional).
* ##### Domain 
Domain and refinement box parameters.
* ##### Timing 
Case timing settings.
* ##### SimSettings 
Simulation control settings.
* ##### MeshSettings 
Simulation mesh settings.
* ##### ViewFactors 
View factor settings.
* ##### Custom 
Optional additional entries to merge into the case.

#### Output
* ##### Logs
Case modification logs.
* ##### Case
UMCF case instance.
* ##### DomBox
Resolved simulation domain box.
* ##### RefBox
Refinement box derived from the case.
* ##### TotalMesh
Total mesh for the case.
* ##### Building
Building mesh.