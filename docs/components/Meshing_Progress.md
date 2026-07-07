# ![](/images/icons/Meshing_Progress.png) Meshing Progress - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Meshing%20Progress%22)

![](/images/components/Meshing_Progress-crop.png)

Monitor blockMesh, surfaceFeatures, and snappyHexMesh progress from the mesh case logs.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Case |  | Wind case (from the wind case component or Load Wind Case). |
| Live |  | Set to true to re-read the meshing logs once a second — no external timer needed. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Progress |  | Estimated meshing progress from 0 to 1. |
| Phase |  | Current meshing phase. |
| Done |  | True when meshing has finished. |
| Status |  | Status text (errors, remaining time). |
