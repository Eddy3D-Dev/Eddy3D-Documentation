# ![](/images/icons/Cell_Size.png) Cell Size - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Cell%20Size%22)

![](/images/components/Cell_Size-crop.png)

Compute the snappyHexMesh refinement level needed to reach a target cell size (each level halves the cell size).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Base Cell Size | Base | Base cell size of the background mesh (meters). | `Number` |
| Target Cell Size | Target | Desired final cell size at the highest refinement level (meters). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Refinement Level | Level | Refinement level (n) required to reach the target cell size. | `Integer` |
| Refinement Level + 1 | Level+1 | One level higher than required (finer resolution). | `Integer` |