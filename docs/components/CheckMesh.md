# ![](/images/icons/CheckMesh.png) CheckMesh - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CheckMesh%22)

![](/images/components/CheckMesh-crop.png)

Run the OpenFOAM checkMesh command for a case region. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Run |  | Run the checkMesh command. | `Boolean` |
| Case |  | Outdoor, Outdoor+, or Indoor case instance to check. | `Generic Data` |
| Region |  | Region name to check. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| CheckMesh Logs | Logs | Log output from the checkMesh command. | `Text` |