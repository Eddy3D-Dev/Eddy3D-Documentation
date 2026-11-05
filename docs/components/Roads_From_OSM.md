# ![](/images/icons/Roads_From_OSM.png) Roads From OSM - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Roads%20From%20OSM%22)

![](/images/components/Roads_From_OSM-crop.png)

Every driveable road around a site from OpenStreetMap, as Road Sources with STREET-TYPE DEFAULTS for traffic: a residential street a few hundred vehicles a day, a primary road fifteen thousand, a motorway sixty thousand. A posted maxspeed wins over the class speed; four lanes carry twice the two-lane default. These are placeholders for a count — override the roads that matter with Road Source. Roads are placed in metres east/north of the site, at z = 0.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Site latitude, decimal degrees — the model origin. | `Number` |
| Longitude | Lon | Site longitude, decimal degrees. | `Number` |
| Radius |  | Half-size of the window the roads are fetched for, m. Noise carries: take the study radius plus 150-300 m so the roads just outside the disc are in. | `Number` |
| Fetch |  | Fetch the roads from OpenStreetMap (Overpass). A window already fetched is read from the cache; pressing again refreshes it. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | One line source per road, for Noise Run. | `Generic Data` |
| Roads |  | The centrelines, in metres east/north of the site, to preview. | `Curve` |
| Log |  | What was read, what was skipped, and where the answer came from. | `Text` |