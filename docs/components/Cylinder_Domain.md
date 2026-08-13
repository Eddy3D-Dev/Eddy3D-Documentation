# ![](/images/icons/Cylinder_Domain.png) Cylinder Domain - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Cylinder%20Domain%22)

![](/images/components/Cylinder_Domain-crop.png)

Define a cylindrical simulation domain for Eddy3D. One cylindrical mesh serves all wind directions; the cylinder side faces switch between inlet and outlet per direction. The auto radius targets the 3% frontal-blockage limit of ASCE/SEI CWE Prestandard AC 6-8b, which the case component verifies. Model surrounding buildings within ~240 m of the study area (ASCE 49 proximity guidance) before trusting results near the context edge.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Core Cell Size | Cell | Cell size of the inner core blocks in meters. Default: 25. | `Number` |
| Inner Core Size | Inner | Half-size of the square inner core in meters. -1 = auto from the building footprint. | `Number` |
| Outer Radius | Radius | Outer radius of the cylindrical domain in meters. -1 = auto from the building height. | `Number` |
| Height |  | Height of the cylindrical domain in meters. -1 = auto from the building height. | `Number` |
| Radial Multiplier | RadMult | Cell growth factor from the core toward the perimeter. Default: 2. | `Number` |
| Core Divisions | Divs | Cells per core block (and per perimeter segment, tangentially). Refines the core without changing the block layout that Core Cell Size sets; the preview core grid densifies to match. Default: 1. | `Integer` |
| Refinement Box Extension | Refine | Padding of the refinement box around the geometry (m). -1 = auto: 27.5% of the building footprint. | `Number` |
| Radial Grading | Grade | Far-field cell coarsening across the perimeter ring (outer cell size / inner cell size). 1 = uniform; >1 keeps fine cells at the buildings but grows the outer cells. The default 7 coarsens the far field aggressively (far fewer cells downwind); lower it (1-3) for a gentler, more uniform ring. Default: 7. | `Number` |
| Core Roundness | Round | Rounds the O-grid inner core from a square (0) toward a circle (1). Higher values even out the radial gap to the outer boundary, cutting the corner non-orthogonality of the square core. 0 keeps the classic square core. 0.65 is the checkMesh-sweep optimum (lowest max non-orthogonality across mesh resolutions; skewness stays well within limits). Default: 0.65. | `Number` |
| Vertical Grading | GradeZ | Vertical cell expansion ratio (top cell size / bottom cell size). 1 = uniform; >1 keeps fine cells near the ground and coarsens aloft (typical for an ABL). A checkMesh sweep showed non-orthogonality/skewness are unaffected by this; the only cost is background aspect ratio. The default 35 strongly refines the near-ground layer; ease it down if convergence struggles. Default: 35. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Domain Parameters | Domain | Cylindrical domain parameters (-1 entries mean auto-sized from the building geometry); plug into the wind case Domain input. | `Generic Data` |