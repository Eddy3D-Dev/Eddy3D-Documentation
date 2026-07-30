# ![](/images/icons/Dataset_Curator.png) Dataset Curator - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Dataset%20Curator%22)

![](/images/components/Dataset_Curator-crop.png)

Compute and export wind dataset features from analysis points and building geometry.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points |  | Analysis points with absolute Z elevations. | `Point` |
| Buildings |  | Building Breps or meshes. | `Geometry` |
| case_dir |  | Case directory where Dataset and Scripts folders are created. | `Text` |
| U_ref |  | Reference wind speed in m/s. | `Number` |
| z_ref |  | Reference height in m. | `Number` |
| pedestrian_level |  | Pedestrian mounting height in m. | `Number` |
| wind_dir |  | Wind directions in degrees, positive clockwise. | `Number` |
| Run |  | Write dataset CSV and processing scripts. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| SDF |  | Negative distance to the nearest building surface. | `Number` |
| Bldg_height |  | Building roof elevation under each point. | `Number` |
| Z_relative |  | Relative sampling height. | `Number` |
| U_over_Uref |  | Log-law inlet speed normalized by U_ref. | `Number` |
| X_coords |  | Point X coordinates. | `Number` |
| Y_coords |  | Point Y coordinates. | `Number` |
| dir_sin |  | First wind direction X component. | `Number` |
| dir_cos |  | First wind direction Y component. | `Number` |
| CSV_Path | CSV | Generated CSV paths. | `Text` |