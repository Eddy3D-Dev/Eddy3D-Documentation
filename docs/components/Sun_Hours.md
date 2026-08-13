# ![](/images/icons/Sun_Hours.png) Sun Hours - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Hours%22)

![](/images/components/Sun_Hours-crop.png)

Direct sun hours and shadow by ray casting — an interactive preview, not a Radiance simulation.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. Meshes are triangulated internally. | `Mesh` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Optional point-specific surface normals. When supplied, a sun below a point's own horizon counts as shaded without tracing — a floor cannot be lit from beneath. | `Vector` |
| Sun Elevation | El | Hourly solar elevation (degrees). Hours at or below 0 are treated as night. | `Number` |
| Sun Azimuth | Az | Hourly solar azimuth (degrees clockwise from north), aligned with Sun Elevation. | `Number` |
| Start Hour | S | First hour of the period (0-8759). | `Integer` |
| End Hour | E | Last hour of the period, exclusive. | `Integer` |
| Offset | O | Distance to lift each point off its surface before tracing. Analysis grids usually sit ON geometry that also shades, and without this every point shadows itself. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sun Hours | H | Hours of direct sun at each point. | `Number` |
| Fraction | F | Sunlit hours as a fraction of the daylight hours considered (0-1). | `Number` |
| Colors | Col | Point-specific colour ramp over the sunlit fraction, for a mesh or point preview. | `Colour` |
| Report | R | Rays traced, daylight hours, and elapsed time. | `Text` |