# ![](/images/icons/Land_Cover_Roughness.png) Land Cover Roughness - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Land%20Cover%20Roughness%22)

![](/images/components/Land_Cover_Roughness-crop.png)

Fetch land-cover polygons around a location from OpenStreetMap (open data, Overpass API) and classify each into an aerodynamic roughness length via the Davenport-Wieringa terrain classification — plus the terrain elevation around the site (AWS Terrain Tiles, open data). Outputs ready-made ground roughness zones and a terrain mesh for the wind case.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Site latitude in decimal degrees (WGS84), e.g. from the EPW header. | `Number` |
| Longitude | Lon | Site longitude in decimal degrees (WGS84). | `Number` |
| Radius | R | Half-size (m) of the square query window around the location. Optional; default is 500. | `Number` |
| Terrain Radius | TR | Half-size (m) of the terrain mesh window. Make it cover the WHOLE CFD domain floor (domain radius plus margins) — the land-cover zones only cover Radius, and the terrain must continue beyond them. Optional; default is 2 x Radius. | `Number` |
| Anchor | Plane | Model-space plane the lat/lon location maps to (polygons are placed on it, X = east, Y = north). Optional; default is the world XY origin. | `Plane` |
| Refinement Level | RefLvl | Snappy surface refinement level for the zone patches. Optional; default is 2. | `Integer` |
| Fetch |  | Press to query the Overpass API AND download the terrain tiles. Both requests run in the background (the canvas stays live); responses are cached on disk, so a canvas re-solve does not re-download. Right-click the component to force a refresh. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Ground Zones | Zones | Ground roughness zone objects, clipped to the query window; plug into the wind case Ground Roughness input. Each zone carries its outline, and the wind case splits the terrain along it at write time — the zone patches and the remaining ground always tile. The preview drapes them over the fetched terrain, tinted by z0 (light sand = smooth, dark earth = rough). | `Generic Data` |
| Boundaries | Crvs | Closed land-cover outline curves in model space. | `Curve` |
| Roughness Lengths | z0 | Roughness length z0 (m) per polygon. | `Number` |
| Land Cover | Class | Davenport class and source OSM tag per polygon (e.g. 'closed (landuse=forest)'). | `Text` |
| Terrain | T | The FULL terrain mesh around the site (AWS Terrain Tiles / SRTM-3DEP merge), placed on the anchor plane with elevation RELATIVE to the site (the location sits at the anchor origin); plug into the wind case Terrain input. The wind case splits the zone areas out of it at write time, so the meshed ground and the zone patches always tile without coincident surfaces. | `Mesh` |
| Site Elevation | Elev | Absolute elevation (m above sea level) of the location — the datum the Terrain mesh's z=0 corresponds to. | `Number` |