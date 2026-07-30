# ![](/images/icons/Building_Mesh_Settings.png) Building Mesh Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Building%20Mesh%20Settings%22)

![](/images/components/Building_Mesh_Settings-crop.png)

Configure mesh refinement for building regions.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Feature Refinement | FeatLvl | Feature refinement level for extracted edges. Optional; default is 4. | `Integer` |
| Surface Level Min | SurfMin | Minimum surface refinement level. Optional; default is 3. | `Integer` |
| Surface Level Max | SurfMax | Maximum surface refinement level. Optional; default is 3. | `Integer` |
| Layer Count | Layers | Number of prism layers to add. Optional; default is 2. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Building Mesh Settings | Mesh | Building mesh settings for snappyHexMesh. | `Generic Data` |