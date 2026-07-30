# ![](/images/icons/MRT.png) MRT - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%22)

![](/images/components/MRT-crop.png)

Compute mean radiant temperature at the sensors. Direct-raycast shortwave by default; wire MRT Settings with reflections/diffuse radiation on to use the Radiance DDS engine.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surfaces | S | Tagged radiation surfaces (MRT Surface). | `Generic Data` |
| Sensors | P | Sensor probes (MRT Sensors). | `Generic Data` |
| EPW | W | Path to the EPW weather file. | `Text` |
| Settings | C | MRT settings (optional). | `Generic Data` |
| Working Directory | Dir | Working directory for the Radiance DDS run (used only when reflections/diffuse radiation is enabled). | `Text` |
| Run | R | Run the MRT analysis. | `Boolean` |
| Engine |  | Run Radiance/EnergyPlus natively or via the bundled radiance-energyplus Docker image. Only relevant when MRT Settings enables Radiance Reflections or EnergyPlus Surfaces. | `Text` |
| Hours of Year | HOY | Optional 1-based hour(s) of year to output. Connect one HOY for an hourly UMCF analysis; leave unconnected for the full 8760-hour annual result. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | Sensor positions. | `Point` |
| MRT | M | Annual MRT as {hour}(probes), preserving the Points output order in every branch. | `Number` |
| Sky Dome | D | The generated sky dome (preview). | `Mesh` |
| Probes | X | Solved probes (for UTCI component). | `Generic Data` |