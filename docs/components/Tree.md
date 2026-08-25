# ![](/images/icons/Tree.png) Tree - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Tree%22)

![](/images/components/Tree-crop.png)

Represents a tree as a porous zone for wind blocking (Darcy-Forchheimer). Feed into the wind case component.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | Geo | Tree/vegetation geometry (one per tree for correct sizing). | `Geometry` |
| Type |  | Crown density class (sets the Darcy-Forchheimer coefficients): Coarse, Medium or Dense — or a species from the shared vegetation library (same LAD and foliage Cd the Outdoor+ Vegetation Region and LBM engines use for that label, so one pick models the same tree in every engine). Wired text still works — the class keywords, a species label, or custom B and A coefficient triples on two lines. A wired LAI wins over the class. | `Text` |
| LAI |  | Leaf Area Index. Typical: 2 (sparse) to 6 (dense). Wins over Type when wired. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Trees |  | Tree porous-zone object; plug into the wind case Trees input. | `Generic Data` |