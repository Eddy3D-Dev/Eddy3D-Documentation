# ![](/images/icons/MRT.png) MRT - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%22)

![](/images/components/MRT-crop.png)

Mean radiant temperature at each sensor, hour by hour. MRT = shortwave + longwave.  SHORTWAVE — what the sensor absorbs from sun and sky. Either a direct raycast (default, pure C#) or the Radiance DDS chain (MRT Settings -> Radiance Reflections), which adds diffuse sky and interreflection off the surroundings. Radiance returns annual total and direct illuminance per sensor, which are mapped onto the probes' shortwave series.  LONGWAVE — what the sensor exchanges with everything around it, weighted by view factors traced from each sensor against the scene and the sky dome.  SURFACE TEMPERATURES come from ENERGYPLUS, not Radiance — Radiance is a light transport engine and computes no temperatures at all. With MRT Settings -> EnergyPlus Surfaces on, Eddy3D builds an epJSON from the polygons that actually matter to the sensors (those inside the cumulative view-factor percentile and above the small-face cutoff; everything else is demoted to a shading surface), runs EnergyPlus against the EPW, and maps the surface-specific temperatures out of the ESO back onto the geometry. With it off, every surrounding surface is simply assumed to sit at air temperature.  SKY TEMPERATURE is always Clark-Allen from dew point, dry bulb, opaque cloud cover and relative humidity — it needs no engine.  Method: Dogan, Kastner & Mermelstein (2021), Building and Environment 196:107762, doi:10.1016/j.buildenv.2021.107762; Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Working Directory | Dir | Root for everything this run writes. Used for the Radiance DDS run (only when reflections/diffuse radiation is enabled) and, with a Project, as its parent folder. | `Text` |
| Project |  | Optional project name. This run's working files and result cache live under <Working Directory>/<Project>/ instead of being mixed in with every other study — so one project's results can be found, copied or cleared on their own. Spaces and characters a folder name cannot hold are replaced (container mounts reject spaces).  Leave it blank and a friendly name is generated the same way a wind case's is (e.g. "swift-otter-fjord-lantern"). It is saved with the document, so re-running writes to the same folder — and a wind case in the same file shares the name, so the two studies sit in same-named folders under their own roots. | `Text` |
| Surfaces | S | Tagged radiation surfaces (MRT Surface). Branches are flattened — everything wired here forms one scene. | `Generic Data` |
| Sensors | P | Sensor probes (MRT Sensors). Branches are flattened. | `Generic Data` |
| EPW | W | Path to the EPW weather file. | `Text` |
| Settings | C | MRT settings (optional). Leave unconnected for the fast pure-C# path — direct-raycast shortwave, ambient surface temperatures, no external engine. Connecting MRT Settings turns on the high-fidelity Radiance and EnergyPlus engines, which its own defaults enable and which take considerably longer. | `Generic Data` |
| Engine |  | Run Radiance/EnergyPlus natively or via the bundled radiance-energyplus container image (Podman or Docker). Only relevant when MRT Settings enables Radiance Reflections or EnergyPlus Surfaces. | `Text` |
| Run | R | Run the MRT analysis. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sky Dome | D | The generated sky dome, shaded from a deep zenith to a pale horizon as vertex colours. Cosmetic — it carries no result. EMPTY unless "Show sky dome" is enabled in the right-click menu: the dome encloses the whole model, so it is off by default and is not built at all while off. | `Mesh` |
| Probes | X | Solved probes (for UTCI component). | `Generic Data` |
| Result | R | The whole solved MRT field as ONE item — every probe's full year. Feed it to Deconstruct MRT for probe-specific statistics or a chosen hour's tree, and to UTCI (Simulation), which reads it without any tree being built. | `Generic Data` |