# ![](/images/icons/Write_Run_Scripts.png) Write Run Scripts - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Write%20Run%20Scripts%22)

![](/images/components/Write_Run_Scripts-crop.png)

Writes meshing and simulation scripts (.bat / .sh) into a Scripts/ folder under the wind study, so the workflow can be launched manually outside Grasshopper. The scripts match what the Run component executes. Write the study to disk first (Wind Case 'Write').

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | The wind study to generate run scripts for (Wind Case output). | `Generic Data` |
| Parallel | P | Generate scripts that decompose and run in parallel (MPI). | `Boolean` |
| CPUs | N | Number of subdomains (MPI ranks) for parallel meshing and simulation. Leave unset (or <= 1) for automatic: the case's decomposeParDict count if > 1, else half the host cores. | `Integer` |
| Engine | E | OpenFOAM engine the scripts target. BlueCFD/WSL produce .bat; Docker produces .sh. | `Text` |
| Probe Name | Probe | FALLBACK only: the post-process scripts are generated automatically for every probe setup the Probe component(s) have written into the cases, each under its own chosen name (05_PostProcess_<name>_<case>). This input is used only when NO probe setup exists yet. Default 'probes'. | `Text` |
| Write | W | Set to true to (re)write the scripts into the study's Scripts/ folder. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Scripts Folder | F | Path to the Scripts/ folder containing the generated batch/shell files. | `Text` |
| Logs | L | Names of the scripts that were written. | `Text` |