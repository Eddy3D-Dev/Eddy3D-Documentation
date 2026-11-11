# ![](/images/icons/Layer_Runoff.png) Layer Runoff - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Layer%20Runoff%22)

![](/images/components/Layer_Runoff-crop.png)

Runoff zones from the ground layers a site model already has: wire LiDAR Site's Layer Outlines and Layer Kinds, and every outline becomes a zone with the Curve Number and overland Manning's n of what the ground there is (grass, park, forest, residential, paved…). The rain then falls on the same polygons the wind study's roughness and City Surface's layers were built from, with no second fetch.  A kind takes the hydrology of its typical OpenStreetMap tag, for the chosen soil group. Roads, paved areas and paths read as paved (CN 98). An outline whose name is not a ground kind (a roughness class such as roughly_open) is skipped and counted: wire Layer Kinds, not Layer Names. Put hand-drawn Runoff Zones after these to override them.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Layer Outlines | Layer | The ground layers' closed outlines: LiDAR Site's Layer Outlines, most specific first, as City Surface takes them. | `Curve` |
| Layer Kinds | Kinds | What the ground of each outline is (water, grass, park, forest, residential, roads, paved…): LiDAR Site's Layer Kinds, one per outline. | `Text` |
| Soil Group | Soil | Hydrologic soil group under the site: it decides the Curve Number of every pervious kind. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zones |  | Runoff zones for Stormwater Grid, least specific first: Grid stamps them in list order with the last one winning, so a pond in a park keeps its own surface. Put hand-drawn Runoff Zones AFTER these to override them. | `Generic Data` |
| Classes |  | The hydrologic class each zone was given. | `Text` |
| Curve Numbers | CN | Curve Number of each zone, for the chosen soil group. | `Number` |