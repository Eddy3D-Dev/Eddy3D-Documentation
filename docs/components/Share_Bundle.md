# ![](/images/icons/Share_Bundle.png) Share Bundle - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Share%20Pack%22)

![](/images/components/Share_Bundle-crop.png)

Write results as files anyone can open without Rhino: ONE self-contained HTML viewer (top-down map with pan/zoom and an orbiting 3D view, sets and layers, legend, hover readout, KPI tables, wind rose, swipe and difference comparison between sets, print to PDF — works offline from the file), glTF binaries (.glb, one per layer, for web/VR/AR viewers), float32 GeoTIFFs (UTM when the site latitude/longitude is given), a PDF report and slide-ready PNGs. Wire one Values branch per layer over the Points (or a Mesh with per-vertex or per-face values). Every file states that the results were computed by the solver and that Eddy3D is the front end.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Folder | Dir | Output folder. Empty with a Study wired: the bundle goes to <case folder>/share. | `Text` |
| Title | T | Title of the bundle; also names the files. Left at the default with a Study wired: "<study name> — results". | `Text` |
| Points | P | Sample points (e.g. the pedestrian grid). Each value branch with one value per point is a point layer. | `Point` |
| Mesh | M | Result surface instead of points: a branch with one value per mesh VERTEX or per mesh FACE is a mesh layer. | `Mesh` |
| Values | V | One branch per layer (e.g. a comfort class, a speed, one branch per wind direction). NaN = no data. | `Number` |
| Layer Names | N | One name per branch (or one for all). Default: Layer 1, Layer 2, … | `Text` |
| Sets | S | One set name per branch (or one for all): switchable groups such as directions, seasons, or "Existing" / "Proposed". Two sets holding layers of the same name get the viewer's swipe and difference comparison. | `Text` |
| Units | U | Unit per branch (or one for all), e.g. m/s, °C. | `Text` |
| Classes | C | Class table for categorical layers: a Wind Comfort Criteria object, a metric name ("Lawson LDDC", "Davenport" …) or class labels best first. Applied to every branch whose values are category numbers (1..n; 0 = no data, as Pedestrian Wind Comfort's Rank). | `Generic Data` |
| Context | Ctx | Buildings, terrain, trees, ground layers, in the site's clay look. A mesh from City Surface, LiDAR Site, Site Look or Site Context is drawn as what it is (trees green, water blue …); any other mesh as a building. Empty with a wind Study wired: the building and terrain surfaces the study was meshed from. | `Mesh` |
| Latitude | Lat | Latitude of the model origin (0,0), +Y north. With Longitude, GeoTIFFs are written in UTM and the viewer reads out latitude/longitude. Empty: the Study's wind-climate site, if any. | `Number` |
| Longitude | Lon | Longitude of the model origin (0,0). | `Number` |
| Study |  | The case the results came from: a Wind Study (or its folder), or any case a Probe accepts. Fills every input left empty — Folder (<case>/share), Title, site, Context — and adds the origin (engine, directions, Eddy3D version, the study report, the wind climate as a wind rose). A Wind Conditions record may be wired too (the wind rose). | `Generic Data` |
| Formats | F | Which files: a choice, or a list such as "html,glb,tif,pdf,png". | `Text` |
| Write | W | Write the bundle. Edge-triggered: a click, or a wired value turning true, writes once. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Files |  | The files the last write produced. | `Text` |
| Summary | Sum | What was written, and anything worth knowing about it. | `Text` |
| Bundle |  | The bundle as an object (built on every solve, no Write needed): wire into Site Report's Results for a chapter of map pages with the share of area per class. | `Generic Data` |