# ![](/images/icons/Face_Warnings.png) Face Warnings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Face%20Warnings%22)

![](/images/components/Face_Warnings-crop.png)

Visualize faces that fail tet decomposition during topoSet. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | UMF case containing the prepare log. | `Generic Data` |
| Mesh |  | Simulation domain mesh. | `Mesh` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Warning Faces | Faces | Mesh faces flagged in warning logs. | `Mesh` |
| Face Indices | Indices | Face indices with no base point found for a valid tet decomposition. | `Integer` |