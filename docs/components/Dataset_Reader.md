# ![](/images/icons/Dataset_Reader.png) Dataset Reader - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Dataset%20Reader%22)

![](/images/components/Dataset_Reader-crop.png)

Read processed CSV datasets back into Grasshopper. Supports mag_U and all spatial features.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Path |  | Path to the .csv file to read. |
| Run |  | Trigger the reading process. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| SDF |  | Signed distance from building. |
| Bldg_height |  | Building height. |
| Z_relative |  | Relative height. |
| U_over_Uref |  | Wind speed at height. |
| mag_U |  | Simulated wind speed magnitude. |
| X |  | X coordinate. |
| Y |  | Y coordinate. |
| dir_sin |  | Direction sin component. |
| dir_cos |  | Direction cos component. |
| brep |  | Reconstructed building geometry (boxes) from CSV data. |
