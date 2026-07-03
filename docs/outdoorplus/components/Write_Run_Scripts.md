## ![](../images/icons/Write_Run_Scripts.png) Write Run Scripts

![](../images/components/Write_Run_Scripts-crop.png)

Writes meshing and simulation scripts (.bat / .sh) into a Scripts/ folder under the wind study, so the workflow can be launched manually outside Grasshopper. The scripts match what the Run component executes. Write the study to disk first (Wind Case 'Write').  Version 1.0.0.827

#### Input
* ##### C 
The wind study to generate run scripts for (Wind Case output).
* ##### P 
Generate scripts that decompose and run in parallel (MPI).
* ##### N 
Number of subdomains (MPI ranks) for parallel meshing and simulation. Leave unset (or <= 1) for automatic: the case's decomposeParDict count if > 1, else half the host cores.
* ##### E 
OpenFOAM engine the scripts target. BlueCFD/WSL produce .bat; Docker produces .sh.
* ##### Probe 
Function-object / probes name the generated 05_PostProcess scripts sample. Match the Probe component's Name input. Default 'probes'.
* ##### W 
Set to true to (re)write the scripts into the study's Scripts/ folder.

#### Output
* ##### F
Path to the Scripts/ folder containing the generated batch/shell files.
* ##### L
Names of the scripts that were written.