# ![](/images/icons/Cut_Fill.png) Cut Fill - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Cut%20Fill%22)

![](/images/components/Cut_Fill-crop.png)

Cut and fill between the existing ground and a proposed grading: where the proposed surface sits below the ground is CUT (red), where it sits above is FILL (blue), and the volumes come with the mesh. Compare design options on one depth scale (Depth Range), read the balance (Net: positive = material to bring in), and the bands say how deep the work goes.  Both surfaces are sampled at the centre of every raster cell inside the proposed surface's footprint; a cell's volume is depth × cell area, so halve the cell size where the grading is finer than the cells. Ground the proposed surface does not reach is not earthworks; a cell the existing ground misses is left out and counted. Depths within 5 mm of zero are unchanged.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Existing |  | The existing ground — a mesh, Brep or surface (branches are flattened). | `Geometry` |
| Proposed |  | The proposed grading — meshes, Breps or surfaces; their plan footprint is what gets rastered (branches are flattened). | `Geometry` |
| Cell Size | Cell | Raster cell size (m). Each cell is sampled once at its centre; use half the size of the smallest grading feature. | `Number` |
| Bands |  | Depth band edges (m, ascending). Each band holds the cut and the fill between its edge and the previous one; the last band is open. Default 0.25, 0.5, 1, 2. | `Number` |
| Depth Range | Range | Depth (m) at the ends of the colour scale, the same for cut and fill, so design options compare on one scale. 0 = the deepest cut or highest fill of this result. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh |  | The proposed surface as cells coloured by depth: red cut, blue fill, grey unchanged. | `Mesh` |
| Cells |  | Centre of every rastered cell both surfaces cover, on the proposed surface. | `Point` |
| Depths |  | Proposed minus existing at each of Cells (m): positive fill, negative cut. | `Number` |
| Cut |  | Cut volume (m³). | `Number` |
| Fill |  | Fill volume (m³). | `Number` |
| Net |  | Fill minus cut (m³): positive is material to bring in, negative to take away. | `Number` |
| Bands |  | One line per depth band: label, cut m³, cut m², fill m³, fill m² (tab-separated). | `Text` |
| Summary |  | Totals, extremes and the bands as text. | `Text` |