# ![](/images/icons/PALM_Domain.png) PALM Domain - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Domain%22)

![](/images/components/PALM_Domain-crop.png)

Define the PALM-4U grid: cells, spacing and the site's latitude/longitude. The domain's lower-left corner sits at the Origin point in the Rhino model (world origin by default), with y pointing north. Feed the output to PALM Case and PALM Run.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Latitude of the domain's lower-left (south-west) corner, decimal degrees. Drives the sun position for radiation and comfort. | `Number` |
| Longitude | Lon | Longitude of the domain's lower-left corner, decimal degrees east. | `Number` |
| Cell Size | dx | Horizontal grid spacing in metres. PALM-4U urban runs use square cells (dx = dy); 2 m resolves streets and courtyards, 4–10 m a district. | `Number` |
| Cells X | nx | Number of cells across the domain in x (east). | `Integer` |
| Cells Y | ny | Number of cells across the domain in y (north). | `Integer` |
| Cells Z | nz | Number of vertical levels. The domain top should clear the tallest building by a factor of 3 or more. | `Integer` |
| Vertical Spacing | dz | Vertical grid spacing in metres. Empty follows Cell Size, which is what a street-resolving run wants. | `Number` |
| Origin | O | Rhino model point of the domain's lower-left corner. Default 0,0,0. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Domain | D | The PALM domain. Feed to PALM Case, which rasterizes the scene onto it and writes the run. | `Generic Data` |
| Boundary | B | The domain footprint as a rectangle in model space — what the static driver will rasterize. | `Curve` |
| Summary | S | Grid, extent and anchor, one line each. | `Text` |