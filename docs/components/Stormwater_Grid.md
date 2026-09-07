# ![](/images/icons/Stormwater_Grid.png) Stormwater Grid - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Stormwater%20Grid%22)

![](/images/components/Stormwater_Grid-crop.png)

Rasterises the graded terrain into the DEM the solver runs on.  Buildings become no-flow WALLS rather than raised ground: raising them fabricates a ridge at the footprint edge that sheds water in whatever direction the rasterised edge happens to face, and lets water pond on roofs.  Breaklines are how a 1 m grid stays usable. A kerb, a swale invert or a threshold is sub-cell at 1 m and every one of them controls where the water goes — sampling the terrain at cell centres averages them away. Burning them along the cell path keeps the control without paying for a fine raster over the whole site.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Terrain |  | The graded surface: meshes, Breps or surfaces. Branches are flattened — everything wired here is one site. Where surfaces overlap in plan the TOP one is taken, since water runs on the upper surface. | `Geometry` |
| Cell Size | Cell | Raster cell size in metres. 1–5 m compares options across a catchment; 0.25–0.5 m is needed only when a sub-metre feature itself drives the answer — and before reaching for it, try burning that feature in as a Breakline, which is far cheaper and, on the repository's own test case, recovers the retention a fine raster resolves to within about 7%. | `Number` |
| Buildings | Bldgs | Building footprints as closed curves, or solids whose plan silhouette is taken. These become no-flow walls. Branches are flattened. | `Geometry` |
| Breaklines | Break | Kerbs, swale inverts, thresholds and low walls, as curves. Each is burned along the cells it crosses so it survives a coarse grid.  The Breakline Offsets input says what each does: a positive value raises the ground by that much (a 150 mm kerb is 0.15), a negative value cuts a swale, and 0 sets the ground to the curve's own z. | `Curve` |
| Breakline Offsets | Offset | One height change (m) per breakline, or a single value for all of them. Positive raises, negative cuts, 0 takes the curve's own elevation. | `Number` |
| Zones |  | Runoff zones (Runoff Zones, Land Cover Runoff). Later zones overwrite earlier ones where they overlap, so list order reads as layer order. | `Generic Data` |
| Buildings Are | BldgMode | Walls (default): water goes around a building, and the rain that lands on its roof is not modelled. Roofs drain to grade: the same, plus the roof's rainfall is injected at the cells ringing the footprint — what actually happens when downpipes discharge to the surface. On a dense site the roofs are a large share of the impervious area, and dropping them under-predicts everything downstream. | `Text` |
| Supersample | Super | Terrain samples per cell edge: 1 takes the cell centre, 2 or 3 averages an n×n grid inside it. Smooths a coarsely-meshed terrain. It does NOT recover sub-cell features — averaging a kerb into the cell mean is precisely how it disappears, which is what Breaklines are for. | `Integer` |
| Default Manning's n | n | Overland roughness for any cell no zone covers. 0.015 suits paving; raise it if the untagged majority of the site is soft. | `Number` |
| Default Runoff Coefficient | C | Fraction of rain that runs off any cell no zone covers. 1.0 treats the untagged site as sealed, which is the conservative reading. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Grid |  | The rasterised site, for Stormwater Run. | `Generic Data` |
| Preview |  | The DEM as a mesh — off-site cells omitted, blocked cells included so buildings read as solid. | `Mesh` |
| Summary |  | Cell count, extent, elevation range and what was excluded. | `Text` |