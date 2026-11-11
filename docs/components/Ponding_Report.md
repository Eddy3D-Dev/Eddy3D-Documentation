# ![](/images/icons/Ponding_Report.png) Ponding Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Ponding%20Report%22)

![](/images/components/Ponding_Report-crop.png)

One row per puddle: where it is, how much water, how deep, when it peaked and how long it took to drain — against the capacity of the hollow it sits in, so an overflowing depression is visible as such.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | A run from Stormwater Run. Needs a Full run — a Fast one has no water in it, only the capacity of the hollows. | `Generic Data` |
| Minimum Depth | MinDepth | Depth in MILLIMETRES a depression must reach to be reported. 25 mm is about where a puddle stops being a wet patch. | `Number` |
| Minimum Volume | MinVol | Volume in m³ a depression must reach to be reported. Keeps a report about the site from being a report about its raster. | `Number` |
| CSV Path | CSV | Optional file path to write the table to. The folder must exist. | `Text` |
| Write |  | Write the CSV to the path above. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Locations | Pts | Deepest point of each pond, at the water surface. | `Point` |
| Volumes | Vol | Water held at peak (m³). | `Number` |
| Areas | Area | Wetted area at peak (m²). | `Number` |
| Depths | Depth | Peak depth (mm). | `Number` |
| Drain Times | Drain | Minutes until the pond fell below the reporting depth. Empty where it never did — which means the water has nowhere to go within the simulated period. | `Number` |
| Table |  | The whole report as CSV text. | `Text` |