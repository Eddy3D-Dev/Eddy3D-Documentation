# ![](/images/icons/Indoor_Species_Case.png) Indoor Species Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Species%20Case%22)

![](/images/components/Indoor_Species_Case-crop.png)

Build a CO2 species case (OpenFOAM 12 multicomponentFluid) with a breathing manikin.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case name (no spaces). | `Text` |
| Working Directory | Dir | Working directory (default ~/Eddy3D/Cases). | `Text` |
| Room | R | Room interior as an axis-aligned box. | `Box` |
| Cell Size | C | Background cell size (m). | `Number` |
| Manikin | M | Manikin from the Manikin component. | `Generic Data` |
| Vent | V | Vent (pressure outlet) centre, on a room wall. | `Point` |
| Breaths | B | Breathing rate (breaths per minute). | `Number` |
| Exhaled CO2 | E | Exhaled-breath CO2 (ppm). Ignored when Occupant is connected, which derives it. | `Number` |
| Occupant | O | Optional occupant (Occupant CO2 component). When given, the mouth's exhaled CO2 and peak velocity are derived from age, activity and minute volume instead of from the Exhaled CO2 and Breaths inputs. | `Generic Data` |
| Ambient CO2 | A | Initial/background CO2 (ppm). | `Number` |
| Duration | T | Simulated seconds. | `Number` |
| Probes | P | Probe points sampled for CO2 and temperature. | `Point` |
| Write | W | Click to write the case to disk. Resets automatically so it never re-writes on recompute. | `Boolean` |
| Clear | X | Click to delete the case folder. Resets automatically so it never re-deletes on recompute. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Directory | Dir | Where the case was written. | `Text` |
| Commands | Cmd | The OpenFOAM commands this case runs, in order. | `Text` |
| Logs | L | Write log / status. | `Text` |
| Case | C | The species case, for the Run component — mesh and solve from the canvas instead of pasting Commands into a terminal. Runs on the UMF engine profile: multicomponentFluid is not in the SimpleWind image. | `Generic Data` |