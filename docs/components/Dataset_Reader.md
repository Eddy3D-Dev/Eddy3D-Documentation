# ![](/images/icons/Dataset_Reader.png) Dataset Reader - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Dataset%20Reader%22)

![](/images/components/Dataset_Reader-crop.png)

Read processed CSV datasets back into Grasshopper. Supports mag_U and all spatial features.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| CSV Path | Path | Path to the .csv file to read. | `Text` |
| Run |  | Trigger the reading process. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| SDF |  | Signed distance from building. | `Number` |
| Bldg_height |  | Building height. | `Number` |
| Z_relative |  | Relative height. | `Number` |
| U_over_Uref |  | Wind speed at height. | `Number` |
| mag_U |  | Simulated wind speed magnitude. | `Number` |
| X |  | X coordinate. | `Number` |
| Y |  | Y coordinate. | `Number` |
| dir_sin |  | Direction sin component. | `Number` |
| dir_cos |  | Direction cos component. | `Number` |
| Brep |  | Reconstructed building geometry (boxes) from CSV data. | `Geometry` |