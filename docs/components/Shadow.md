# ![](/images/icons/Shadow.png) Shadow - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Shadow%22)

Lit or shaded at each analysis point for one or more sun instants, by ray casting against the context — the shadow's position at a moment, not Sun Hours' accumulation over a period. It shares Sun Hours' solver, so a point counted lit here is exactly one Sun Hours would credit for that same sample.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Optional per-point normals. A sun below a point's own horizon counts as shaded without tracing — a floor cannot be lit from beneath. | `Vector` |
| Weather | W | Weather record from Download Weather or Open Weather. The sun's position for each evaluated hour comes from this file. | `Generic` |
| HOY | H | Hours of the year to evaluate [1-8760], one result branch per hour — wire the Hour Of Year component to name a date and time. Left empty, every daylight hour of the year is evaluated, which on a large grid is a long run. | `Integer` |
| Offset | O | Distance to lift each point off its surface before tracing. Default `0.01`. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). The sun is rotated, not the model. Default `0.0`. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Lit | L | True where the sun's disc is visible. One branch per sun sample. | `Boolean` |
| Colors | Col | Sunlit yellow / shaded blue, matching the Sun Hours ramp's endpoints. | `Colour` |
| Sunlit Points | SP | Just the lit points, flattened — convenient for a preview. | `Point` |
| Report | R | Instants evaluated and the lit fraction of each. | `Text` |

#### Notes

- **Weather is functionally required.** It is marked optional so the component can name the exact reason for itself ("Connect a weather record") rather than Grasshopper's generic "failed to collect data" — leaving it unwired still stops the solve.
- **HOY left empty evaluates every daylight hour of the year**, one branch each, which can be a long run on a large point grid; the same heavy-run warning Sun Hours uses fires here too.
- **Wiring several HOY values fans out to one branch per instant** across Lit, Colors and Sunlit Points — an animated shadow study is a slider on HOY, not a separate mechanism.
- **Documents saved before Weather + HOY existed** (when a Sun Vectors input fed the sun directly) are migrated on open. The old Offset wire is dropped rather than silently landing on the new HOY input — without the migration, a saved 0.01 offset would silently become "hour 0 of the year." A Remark reports how many wires were dropped and what to reconnect.
