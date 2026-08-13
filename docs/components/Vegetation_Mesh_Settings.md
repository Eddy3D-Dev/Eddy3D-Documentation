# ![](/images/icons/Vegetation_Mesh_Settings.png) Vegetation Mesh Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vegetation%20Mesh%20Settings%22)

![](/images/components/Vegetation_Mesh_Settings-crop.png)

Configure mesh refinement for vegetation regions. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Feature Refinement | FR | Feature refinement level. Optional; default is 2. | `Integer` |
| Minimum Surface Refinement | MnSR | Minimum refinement on surfaces. Optional; default is 4. | `Integer` |
| Maximum Surface Refinement | MxSR | Maximum refinement on surfaces. Optional; default is 5. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Vegetation Mesh Settings | MeshSet | Mesh refinement settings for vegetation regions. | `Generic Data` |