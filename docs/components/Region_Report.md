# ![](/images/icons/Region_Report.png) Region Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Region%20Report%22)

![](/images/components/Region_Report-crop.png)

Reads the storm against regions you drew — courtyards, plots, streets: how deep each one stood, whether it passed the threshold, and how much of the ground draining into it lies outside it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | A run from Stormwater Run. A Fast run gives the Upslope Share only — it routes no water, so every depth reads zero. | `Generic Data` |
| Regions |  | Closed curves in plan, one per region: courtyards, plots, a street. They may overlap. | `Curve` |
| Threshold |  | Depth in MILLIMETRES above which a region counts as flooded. 100 mm is about a kerb. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Locations | Pts | Deepest point of each region, at the water surface. | `Point` |
| Depths | Depth | Peak depth anywhere in the region (mm). | `Number` |
| Flooded |  | True where the region stood deeper than Threshold. | `Boolean` |
| Flooded Areas | Area | Area of the region that stood deeper than Threshold (m²). | `Number` |
| Upslope Share | Upslope | Percent of the ground draining into the region that lies OUTSIDE it — how much of its water is somebody else's rain. Read off the terrain alone (uniform rain, no losses, steepest descent over the filled surface): it says where water comes from, not how much arrives. | `Number` |
| Summary |  | The count as a sentence. | `Text` |