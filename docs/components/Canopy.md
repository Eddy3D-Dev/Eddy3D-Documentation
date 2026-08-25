# ![](/images/icons/Canopy.png) Canopy - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Canopy%22)

![](/images/components/Canopy-crop.png)

Vegetation that attenuates the sun instead of blocking it, with an optional leaf-on/leaf-off season. Feed the Canopy input of Sun Hours or Solar Irradiation.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Canopy geometry — crowns, hedges, shade structures. | `Geometry` |
| Crown Transmittance | T | Fraction of the beam a WHOLE crown passes, 0-1. Typical summer broadleaf 0.1-0.3; bare winter canopy 0.6-0.8. Converted to a per-crossing value assuming the crown mesh is closed. | `Number` |
| Per Crossing | PC | Treat Crown Transmittance as the per-SURFACE-crossing value instead, with no closed-crown conversion. Use for single-surface canopies: slats, sails, awnings. | `Boolean` |
| Leaf On | On | Day of year the canopy comes into leaf (1-365). Leave both leaf inputs at 0 for an evergreen that shades all year. | `Integer` |
| Leaf Off | Off | Last day of year the canopy is in leaf (1-365). A window that wraps the new year (e.g. 274 to 105) is a southern-hemisphere season and is handled. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Canopy | C | Canopy layer for the Canopy input of Sun Hours or Solar Irradiation. | `Generic Data` |
| Report | R | Transmittance as applied, the leaf window, and the triangle count. | `Text` |