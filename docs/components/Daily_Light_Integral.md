# ![](/images/icons/Daily_Light_Integral.png) Daily Light Integral - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Daily%20Light%20Integral%22)

![](/images/components/Daily_Light_Integral-crop.png)

Daily Light Integral per point in mol/m²/day — the photosynthetically active photons (400-700 nm) landing on each point per day, averaged over the analysed period.  Shares Solar Irradiation's geometry: beam plus isotropic sky plus a ground term, no interreflection. The ground albedo here is a PAR albedo and is much lower than the broadband one. Vegetation is deliberately not accepted — see the Canopy note in the docs.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain. A tree crown here blocks the beam COMPLETELY — the Canopy component's transmittance is broadband and cannot be applied to PAR. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Normals | N | Per-point surface normals. Without them every point is treated as HORIZONTAL, which is right for a planting bed or a green roof and wrong for a facade. | `Vector` |
| Weather | W | Weather record from Download Weather or Open Weather. Both the sun's position and the direct/diffuse irradiance for each hour come from this one file. | `Generic Data` |
| HOY | H | Hours of the year to analyse [1-8760]. Left empty, every DAYLIGHT hour of the year is analysed, which gives the annual mean and the full monthly breakdown. | `Integer` |
| Timestep | T | Sun samples per hour. 1 is hourly; 10 gives a 6-minute step. The irradiance is still the file's HOURLY value — a finer step refines WHERE the beam lands, not the weather itself. | `Integer` |
| Sky View | SVF | Optional sky view fraction per point, from Sky Exposure. Without it the sky is treated as fully open, which overstates diffuse in any real courtyard — and a courtyard is where this metric is usually asked. | `Number` |
| Ground PAR Reflectance | GR | PAR albedo of the ground for the reflected term. NOT the broadband albedo: vegetation absorbs PAR and reflects near-infrared, so grass is near 0.05 in PAR against ~0.23 broadband. Only tilted surfaces see any of it. | `Number` |
| Offset | O | Distance to lift each point off its surface before tracing. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). The sun is rotated, not the model. | `Number` |
| Conversion | Cv | How broadband shortwave becomes PAR photons — a PAR energy fraction times a quanta-per-joule factor. Logan & Faust (default): 0.45 x 4.48 µmol/J = 0.00726 mol/Wh, the pair behind the published US daily-light-integral maps, calibrated against global horizontal irradiance. Ecological: 0.50 x 4.60 µmol/J, the generic convention used in flux-tower work. Runs about 14% higher. Neither is universal — both assume a daylight spectrum on an unfiltered surface. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| DLI |  | Mean daily light integral per point over the analysed period, mol/m²/day. | `Number` |
| Colors | Col | Colour ramp over the mean DLI. | `Colour` |
| Result | Res | The whole solve as one item — the monthly breakdown included. Wire Deconstruct DLI to expand it; twelve months over a large grid is the tree this output exists to avoid putting on the canvas. | `Generic Data` |
| Report | R | Range, days analysed, rays and the assumptions used. | `Text` |