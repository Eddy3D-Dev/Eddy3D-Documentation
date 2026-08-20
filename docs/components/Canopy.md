# ![](/images/icons/Canopy.png) Canopy - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Canopy%22)

Vegetation that dims the sun rather than blocking it — a crown passes part of the beam, and can optionally lose that effect outside its leaf season. Wire its Canopy output into the Canopy input of Sun Hours or Solar Irradiation; putting the same geometry in a study's plain Context socket instead makes it fully opaque year-round, with no seasonal or partial-transmittance behavior.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Canopy geometry — crowns, hedges, shade structures. Accepts multiple items. | `Geometry` |
| Crown Transmittance | T | Fraction of the beam a whole crown passes, 0-1 (default 0.2). Typical summer broadleaf 0.1-0.3; bare winter canopy 0.6-0.8. Converted internally to a per-crossing value on the assumption the crown mesh is closed — set Per Crossing to skip that conversion. | `Number` |
| Per Crossing | PC | Treat Crown Transmittance as the per-surface-crossing value directly, with no closed-crown conversion. Use for single-surface canopies: slats, sails, awnings. Default off. | `Boolean` |
| Leaf On | On | Day of year the canopy comes into leaf, 1-365. Leave both leaf inputs at 0 for an evergreen that shades all year. Default 0. | `Integer` |
| Leaf Off | Off | Last day of year the canopy is in leaf, 1-365. A window that wraps the new year (e.g. 274 to 105) is a southern-hemisphere season and is handled. Default 0. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Canopy | C | Canopy layer for the Canopy input of Sun Hours or Solar Irradiation. | `Generic` |
| Report | R | Transmittance as applied, the leaf window, and the triangle count. | `Text` |

#### Notes

- Crown Transmittance is validated to 0-1. Setting it to exactly 1 draws a Warning (the canopy then casts no shade at all); setting it to exactly 0 draws a Remark suggesting the geometry go in the study's Context socket instead, since opaque geometry there gets the faster any-hit trace, while a Canopy always needs the slower all-hit trace.
- Leaf On and Leaf Off must both be 0 (evergreen) or both fall in 1-365 — a half-specified window is rejected as an error rather than silently clamped to day 1 or 365.
- Geometry items that fail to mesh are skipped with a Warning and simply do not shade.
