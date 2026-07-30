# ![](/images/icons/Tree.png) Tree - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Tree%22)

![](/images/components/Tree-crop.png)

Represents a tree as a porous zone for wind blocking (Darcy-Forchheimer). Feed into the wind case component.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | Geo | Tree/vegetation geometry (one per tree for correct sizing). | `Geometry` |
| Type |  | Tree density type: 'coarse', 'medium', or 'dense'. Or custom Darcy-Forchheimer B and A coefficient triples on two lines. | `Text` |
| LAI |  | Leaf Area Index. Typical: 2 (sparse) to 6 (dense). Alternative to Type. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Trees |  | Tree porous-zone object; plug into the wind case Trees input. | `Generic Data` |