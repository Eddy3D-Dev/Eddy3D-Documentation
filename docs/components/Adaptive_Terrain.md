# ![](/images/icons/Adaptive_Terrain.png) Adaptive Terrain - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Adaptive%20Terrain%22)

![](/images/components/Adaptive_Terrain-crop.png)

Resample a terrain (meshes and/or breps) onto a graded mesh: Fine Size cells over the Focus, coarsening smoothly to Coarse Size away from it, and refined back down wherever the ground bends more than Tolerance. The mesh is conforming (no cracks where the size changes) and covers the terrain's plan bounding box. Solid closes it with a flat underside Depth below its lowest point and vertical side walls, ready for STL export or as a terrain body.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Terrain |  | Terrain meshes and/or breps. Heights are read straight down onto the topmost surface. | `Geometry` |
| Focus |  | Optional curves where the terrain is meshed finest: a closed curve is a region, an open one a line (a road, a river). Read in plan. Default: the middle half of the terrain's footprint. | `Curve` |
| Fine Size | Fine | Cell size (m) over the Focus and where the ground bends. | `Number` |
| Coarse Size | Coarse | Largest cell size (m), reached far from the Focus. | `Number` |
| Growth |  | How fast cells coarsen away from the Focus: size = Fine + (Growth − 1) × distance, so 1.2 doubles a 5 m cell about 25 m out. 1 keeps the whole terrain fine. | `Number` |
| Tolerance | Tol | Vertical tolerance (m): a cell is split where the ground inside it departs from its corners by more than this, so ridges, banks and cuttings keep their shape far from the Focus. 0 switches it off. | `Number` |
| Depth |  | How far (m) Solid's underside sits below the terrain's lowest point. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh |  | The resampled terrain surface (quads, with triangle fans where the size changes). | `Mesh` |
| Solid |  | The surface closed into a watertight solid: underside and side walls. | `Mesh` |