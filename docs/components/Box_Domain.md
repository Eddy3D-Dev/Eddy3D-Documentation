# ![](/images/icons/Box_Domain.png) Box Domain - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Box%20Domain%22)

![](/images/components/Box_Domain-crop.png)

Define simulation domain extents and refinement padding. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Cell Size | CS | Base cell size for the domain (model units). | `Integer` |
| Front Extension | Front | Padding in front of the geometry bounding box (model units). | `Number` |
| Back Extension | Back | Padding behind the geometry bounding box (model units). | `Number` |
| Side Extension | Side | Padding on the side faces of the geometry bounding box (model units). | `Number` |
| Top Extension | Top | Padding above the geometry bounding box (model units). | `Number` |
| Refinement Box Extension | Ref | Padding applied to the refinement box around the geometry (model units). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Domain Parameters | DP | Domain and refinement box parameters as a list. | `Number` |