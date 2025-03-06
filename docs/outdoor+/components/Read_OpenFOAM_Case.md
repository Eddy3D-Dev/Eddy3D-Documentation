## ![](../images/icons/Read_OpenFOAM_Case.png) Read OpenFOAM Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D-UMCF/blob/release/UMCF/CMP/Meta/ReadOpenFOAMCaseCMP.cs)

![](../images/components/Read_OpenFOAM_Case.png)

Reads an OpenFOAM case and outputs a Case instance with all its files.

#### Input
* ##### D
Directory to OpenFOAM case.

#### Output
* ##### FCs
File Containers found in the case.
* ##### I
Names of files in the directory that were not `added to the case