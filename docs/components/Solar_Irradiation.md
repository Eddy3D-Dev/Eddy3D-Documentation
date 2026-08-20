# ![](/images/icons/Solar_Irradiation.png) Solar Irradiation - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Solar%20Irradiation%22)

Cumulative incident solar energy at each point, in kWh/m² — beam plus an isotropic sky term plus a single-albedo ground reflection. An interactive preview, not a Radiance simulation: no interreflection, no material response, no spectral detail, so use MRT/UTCI when the number has to be defensible and this component to compare orientations while the design is still moving.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Per-point surface normals. Without them every point is treated as horizontal, which is right for a ground grid and badly wrong for a facade. | `Vector` |
| Weather | W | Weather record from Download Weather or Open Weather. Both the sun's position and the direct/diffuse irradiance for each hour come from this one file. | `Generic` |
| HOY | H | Hours of the year to accumulate [1-8760] — wire the Hour Of Year component to name a date and time. Left empty, every daylight hour of the year is accumulated, which is the annual total. | `Integer` |
| Timestep | T | Sun samples per hour. 1 is hourly; 10 gives a 6-minute step, which resolves the shadow edge far better. The irradiance is still the file's hourly value — a finer step refines where the beam lands, not the weather itself. Default 1. | `Integer` |
| Sky View | SVF | Optional sky view fraction per point, from Sky Exposure. Without it the sky is treated as fully open, which overstates diffuse in any real street. | `Number` |
| Ground Reflectance | GR | Albedo for the ground-reflected term. | `Number` |
| Offset | O | Distance to lift each point off its surface before tracing. Default 0.01. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). The sun is rotated, not the model. Default 0. | `Number` |
| Canopy | Cn | Optional canopy layers from the Canopy component. Vegetation here attenuates the beam only — the isotropic sky term is unaffected, because a canopy that dims the sun also blocks sky, and the sky view fraction already accounts for it if SVF was measured with the canopy in place. | `Generic` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Total | T | Total incident irradiation, kWh/m². | `Number` |
| Direct | Dir | Beam component, kWh/m². | `Number` |
| Diffuse | Dif | Sky diffuse component, kWh/m². | `Number` |
| Reflected | Ref | Ground-reflected component, kWh/m². | `Number` |
| Colors | Col | Colour ramp over the total. | `Colour` |
| Report | R | Totals, rays and the assumptions used. | `Text` |

#### Notes

- **Weather replaced three older inputs.** Before this component took a single Weather record, it took Sun Vectors, Direct Normal and Diffuse Horizontal separately. A document saved under that layout has those three wires dropped on open (Weather carries the sun's position and both irradiance series on its own), and the component posts a one-time Remark naming how many wires were lost.
- Ground Reflectance defaults to the component's built-in `SolarIrradiation.DefaultGroundReflectance` constant, not a literal — check the current build if the exact default value matters.
