# ![](/images/icons/Solar_Irradiation.png) Solar Irradiation - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Solar%20Irradiation%22)

![](/images/components/Solar_Irradiation-crop.png)

Cumulative incident solar energy per point in kWh/m² — beam plus isotropic sky plus ground reflection. An interactive preview, not a Radiance simulation.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Per-point surface normals. Without them every point is treated as HORIZONTAL, which is right for a ground grid and badly wrong for a facade. | `Vector` |
| Weather | W | Weather record from Download Weather or Open Weather. Both the sun's position and the direct/diffuse irradiance for each hour come from this one file. | `Generic Data` |
| HOY | H | Hours of the year to accumulate [1-8760] — wire the Hour Of Year component to name a date and time. Left empty, every DAYLIGHT hour of the year is accumulated, which is the annual total. | `Integer` |
| Timestep | T | Sun samples per hour. 1 is hourly; 10 gives a 6-minute step, which resolves the shadow edge far better (docs/SUN_ANALYSIS.md). The irradiance is still the file's HOURLY value — a finer step refines WHERE the beam lands, not the weather itself. | `Integer` |
| Sky View | SVF | Optional sky view fraction per point, from Sky Exposure. Without it the sky is treated as fully open, which overstates diffuse in any real street. | `Number` |
| Ground Reflectance | GR | Albedo for the ground-reflected term. | `Number` |
| Offset | O | Distance to lift each point off its surface before tracing. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). The sun is rotated, not the model. | `Number` |
| Canopy | Cn | Optional canopy layers from the Canopy component. Vegetation here attenuates the BEAM only — the isotropic sky term is unaffected, because a canopy that dims the sun also blocks sky, and the sky view fraction already accounts for it if you measured SVF with the canopy in place. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Total | T | Total incident irradiation, kWh/m². | `Number` |
| Direct | Dir | Beam component, kWh/m². | `Number` |
| Diffuse | Dif | Sky diffuse component, kWh/m². | `Number` |
| Reflected | Ref | Ground-reflected component, kWh/m². | `Number` |
| Colors | Col | Colour ramp over the total. | `Colour` |
| Report | R | Totals, rays and the assumptions used. | `Text` |