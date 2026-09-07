# ![](/images/icons/Land_Cover_Runoff.png) Land Cover Runoff - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Land%20Cover%20Runoff%22)

![](/images/components/Land_Cover_Runoff-crop.png)

Fetches land-cover polygons around a lat/lon from OpenStreetMap (open data, no key) and classifies each into a Curve Number and an overland Manning's n.  This is the same Overpass query the Land Cover Roughness component makes, read for runoff instead of for wind — so wiring both on one site costs one fetch, not two. Unmapped tags are skipped rather than guessed at.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Site latitude in decimal degrees. | `Number` |
| Longitude | Lon | Site longitude in decimal degrees. | `Number` |
| Radius |  | Half-width in metres of the square window fetched around the site. Keep it close to the terrain's own extent: Overpass returns the FULL geometry of anything touching the window, and a large one drags in metro-scale polygons. | `Number` |
| Soil Group | Soil | Hydrologic soil group underneath. It shifts every Curve Number: the same lawn sheds far more on clay than on sand, so this is the single input here with the largest effect on the answer. B is the usual default when nothing local is known. | `Text` |
| Anchor |  | Model-space point the lat/lon maps to. Default is the origin. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zones |  | Runoff zones for Stormwater Grid. | `Generic Data` |
| Outlines | Curves | The classified polygons, so they can be edited or rebuilt by hand. | `Curve` |
| Classes |  | What each polygon was classified as. | `Text` |
| Curve Numbers | CN | Curve Number assigned to each polygon, for the chosen soil group. | `Number` |