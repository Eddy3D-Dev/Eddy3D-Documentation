# ![](/images/icons/Case_Run.png) Case Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Case%20Run%22)

![](/images/components/Case_Run-crop.png)

Prepare and run a UMF case. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Case to prepare and/or run. | `Generic Data` |
| Parallel |  | Run the case in parallel if enabled. | `Boolean` |
| Prepare | Prep | Prepare meshing and case setup. | `Boolean` |
| Run |  | Run the simulation solver. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Updated case after prepare/run. | `Generic Data` |
| Logs |  | Latest execution logs. | `Text` |