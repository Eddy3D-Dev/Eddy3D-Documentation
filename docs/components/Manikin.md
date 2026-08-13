# ![](/images/icons/Manikin.png) Manikin - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Manikin%22)

![](/images/components/Manikin-crop.png)

A breathing occupant (LOD-0 body with a separate mouth patch) for the Indoor Species Case.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Position | P | Ground position of the body centre. | `Point` |
| Facing | F | Facing direction in plan. Snaps to the dominant axis — the LOD-0 body is axis-aligned. | `Vector` |
| Height | H | Body height (m). | `Number` |
| Mouth Size | M | Mouth patch edge length (m). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Manikin | M | Manikin for the Indoor Species Case component. | `Generic Data` |
| Preview | P | Body geometry for visual checking. | `Mesh` |
| Mouth | Mo | Mouth centre — a good probe location. | `Point` |