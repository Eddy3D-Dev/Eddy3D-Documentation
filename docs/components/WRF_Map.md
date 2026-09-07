# ![](/images/icons/WRF_Map.png) WRF Map - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Map%22)

![](/images/components/WRF_Map-crop.png)

Lat/lon graticule with labels, the run's own coastline from LANDMASK, and a site marker — in the same plane as the WRF Probe points and WRF Domain rectangles. Wire Labels + Label Points (and Site Label + Site Point) to a Text Tag to draw the annotations.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — WRF Run's Case Folder output; run_wrf is derived from it (a run_wrf path wired directly still works). Empty uses the document's session case. | `Text` |
| Domain | d | Which nest to map: 1 for d01, 2 for d02. | `Integer` |
| Graticule | G | Spacing of the lat/lon grid in degrees. Empty or 0 picks a round spacing that gives the domain a handful of lines; negative disables the graticule. | `Number` |
| Site Name | S | Label for the site marker. Empty uses the case folder's name. | `Text` |
| Site Latitude | Lat | Site latitude in degrees. Defaults to the domain centre. | `Number` |
| Site Longitude | Lon | Site longitude in degrees. Defaults to the domain centre. | `Number` |
| Z Height | Z | Height the map lines and labels are drawn at, in metres, so they print above the results underneath. Empty or 0 picks a height from the domain size. | `Number` |
| Line Weight | LW | Pixel width of the self-drawn border and urban lines; the graticule stays one pixel thinner. The curve outputs are unstyled — weight applies to the viewport drawing. | `Integer` |
| Label Style | LS | How the labels draw in the viewport. Text is plain 3d text that bakes and exports the way it looks; Bubbles are the classic screen-sized text dots. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Graticule | G | Lat/lon grid lines clipped to the domain. | `Curve` |
| Labels | L | Graticule labels, e.g. 34N or 84.5W, one per label point. | `Text` |
| Label Points | LP | Anchor for each graticule label, on the domain edge. | `Point` |
| Coastline | C | The run's own land/water boundary: LANDMASK contoured at 0.5. | `Curve` |
| Site Point | SP | The site marker position. | `Point` |
| Site Label | SL | The site marker text. | `Text` |
| Borders | B | Country and state borders inside the domain, from the embedded Natural Earth base map. | `Curve` |
| Urban Areas | U | Urban-area outlines inside the domain (Natural Earth 10m urban areas) — the metro footprint, not an administrative city limit. | `Curve` |
| Water | W | Lakes and ocean coastline inside the domain, from the base map. | `Curve` |