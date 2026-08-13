# ![](/images/icons/Land_Cover_Roughness.png) Land Cover Roughness - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Land%20Cover%20Roughness%22)

![](/images/components/Land_Cover_Roughness-crop.png)

Fetch land-cover polygons around a location from OpenStreetMap (open data, Overpass API) and classify each into an aerodynamic roughness length via the Davenport-Wieringa terrain classification. Outputs ready-made ground roughness zones for the wind case.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Site latitude in decimal degrees (WGS84), e.g. from the EPW header. | `Number` |
| Longitude | Lon | Site longitude in decimal degrees (WGS84). | `Number` |
| Radius | R | Half-size (m) of the square query window around the location. Optional; default is 500. | `Number` |
| Anchor | Plane | Model-space plane the lat/lon location maps to (polygons are placed on it, X = east, Y = north). Optional; default is the world XY origin. | `Plane` |
| Refinement Level | RefLvl | Snappy surface refinement level for the zone patches. Optional; default is 2. | `Integer` |
| Fetch |  | Press to query the Overpass API. The request runs in the background (the canvas stays live) and fails over between public mirrors; responses are cached on disk per query, so a canvas re-solve does not re-download. Right-click the component to force a refresh. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Ground Zones | Zones | Ground roughness zone objects (flat meshes at the anchor plane); plug into the wind case Ground Roughness input, or rebuild your own plate from the boundary curves. | `Generic Data` |
| Boundaries | Crvs | Closed land-cover outline curves in model space. | `Curve` |
| Roughness Lengths | z0 | Roughness length z0 (m) per polygon. | `Number` |
| Land Cover | Class | Davenport class and source OSM tag per polygon (e.g. 'closed (landuse=forest)'). | `Text` |