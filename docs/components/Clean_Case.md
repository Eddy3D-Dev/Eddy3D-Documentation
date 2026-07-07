# ![](/images/icons/Clean_Case.png) Clean Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Clean%20Case%22)

![](/images/components/Clean_Case-crop.png)

Delete mesh and/or simulation result directories from a wind study folder.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Case |  | Wind study (OutdoorCase) or path to the study folder. |
| Mode |  | 0 = Mesh only, 1 = Simulation results only, 2 = Both. |
| Run |  | Set to True to delete. Cannot be undone. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Logs | L | Deletion log. |
