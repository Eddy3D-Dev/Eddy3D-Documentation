# ![](/images/icons/PALM_Land_Cover.png) PALM Land Cover - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Land%20Cover%22)

![](/images/components/PALM_Land_Cover-crop.png)

Fetch OpenStreetMap land cover over the PALM domain and classify it into PALM surface types. Feed the output into PALM Case's Land Cover input. Urban block polygons are skipped and reported — paint those by hand.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Domain | D | The PALM Domain whose window is fetched. | `Generic Data` |
| Fetch | F | Fetch (or re-fetch, bypassing the 30-day cache) the OSM land cover. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Land Cover | LC | Classified patches for PALM Case. | `Generic Data` |
| Outlines | O | The patch outlines in model space, for inspection. | `Curve` |
| Report | R | Patch counts per class, and the OSM tags that were skipped. | `Text` |