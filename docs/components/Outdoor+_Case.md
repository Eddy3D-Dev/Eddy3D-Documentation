# ![](/images/icons/Outdoor+_Case.png) Outdoor+ Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Outdoor%2B%20Case%22)

![](/images/components/Outdoor+_Case-crop.png)

Create, read, and manage an Outdoor+ (UMF microclimate) case. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Read Case | Read | Read an existing case from the working directory. | `Boolean` |
| Write |  | Write the case files to the working directory. | `Boolean` |
| Clear Case | Clear | Delete all files for this case in the working directory. | `Boolean` |
| Case Name | Name | Case folder name (no spaces). | `Text` |
| Working Directory | Dir | Folder for case files and results. | `Text` |
| Air Region | Air | Air region for this case. | `Generic Data` |
| Vegetation Region | Vegetation | Optional vegetation region. Leave disconnected for cases without trees or canopy. | `Generic Data` |
| Building Region | BR | Building region of this case. | `Generic Data` |
| Terrain Region | Terrain | Terrain region for this simulation (optional). | `Generic Data` |
| Domain Parameters | Domain | Domain and refinement box parameters. | `Number` |
| Timing Settings | Timing | Case timing settings. | `Generic Data` |
| Simulation Settings | SimSettings | Simulation control settings. | `Generic Data` |
| Simulation Mesh Settings | MeshSettings | Simulation mesh settings. | `Generic Data` |
| View Factor Settings | ViewFactors | View factor settings. | `Generic Data` |
| Custom Entries | Custom | Optional additional entries to merge into the case. | `Generic Data` |
| Water Surface | Water | Optional coupled water surface from the Water Surface component. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Logs |  | Case modification logs. | `Text` |
| Case |  | UMF case instance. | `Generic Data` |
| Domain Box | DomBox | Resolved simulation domain box. | `Box` |
| Refinement Box | RefBox | Refinement box derived from the case. | `Box` |
| Total Mesh | TotalMesh | Total mesh for the case. | `Mesh` |
| Building |  | Building mesh. | `Mesh` |