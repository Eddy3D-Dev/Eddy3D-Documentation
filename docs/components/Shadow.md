# ![](/images/icons/Shadow.png) Shadow - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Shadow%22)

![](/images/components/Shadow-crop.png)

Lit or shaded at each analysis point for one or more sun instants — the shadow's position, not accumulated sun hours.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Optional per-point normals. A sun below a point's own horizon counts as shaded without tracing — a floor cannot be lit from beneath. | `Vector` |
| Weather | W | Weather record from Download Weather or Open Weather. The sun's position for each evaluated hour comes from this file. | `Generic Data` |
| HOY | H | Hours of the year to evaluate [1-8760], one result branch per hour — wire the Hour Of Year component to name a date and time. Left empty, every DAYLIGHT hour of the year is evaluated, which on a large grid is a long run. | `Integer` |
| Offset | O | Distance to lift each point off its surface before tracing. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). The sun is rotated, not the model. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Lit | L | True where the sun's disc is visible. One branch per sun sample. | `Boolean` |
| Colors | Col | Sunlit yellow / shaded blue, matching the Sun Hours ramp's endpoints. | `Colour` |
| Sunlit Points | SP | Just the lit points, flattened — convenient for a preview. | `Point` |
| Report | R | Instants evaluated and the lit fraction of each. | `Text` |
| Result | Res | The whole solve — every point at every instant — as ONE item. Feed it to Deconstruct Shadow to expand only the instants you want to look at. This is the output to use for anything longer than a handful of hours: the trees above are points x instants of boxed Grasshopper data, and an annual study is tens of millions of them. | `Generic Data` |