# ![](/images/icons/LBM_Field.png) LBM Field - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Field%22)

![](/images/components/LBM_Field-crop.png)

Read the time-averaged pedestrian wind field from an LBM case directory. Outputs world-frame points and velocity vectors — plug both into the Wind Field Viewer.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | LBM case directory (the 'Case' output of the LBM Run component). | `Text` |
| Refresh | R | Re-read the results (toggle while a run is in progress). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | Probe points (world frame). | `Point` |
| Velocity | V | Time-averaged velocity per point (m/s, world frame). | `Vector` |
| Speed | S | Speed magnitude per point (m/s). | `Number` |
| Status | St | Read status. | `Text` |