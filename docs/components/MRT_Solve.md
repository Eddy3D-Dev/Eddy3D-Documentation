# ![](/images/icons/MRT_Solve.png) MRT Solve - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Solve%22)

![](/images/components/MRT_Solve-crop.png)

Solves MRT on a prepared VF Model: shortwave (direct raycast, or Radiance DDS when MRT Settings enables reflections) + view-factor longwave. Wire the VF Model straight from MRT View Factors for ambient/FFT surface temperatures, or through SurfaceTemp (EnergyPlus) for E+ temperatures. Result feeds Deconstruct MRT and UTCI. Method: Dogan, Kastner & Mermelstein (2021), Building and Environment 196:107762, doi:10.1016/j.buildenv.2021.107762; Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Working Directory | Dir | Folder the Radiance case is written to. Only needed when MRT Settings enables Radiance Reflections. | `Text` |
| VF Model | VF | Solved model from MRT View Factors, optionally enriched by SurfaceTemp (EnergyPlus). | `Generic Data` |
| EPW | W | Path to the EPW weather file. | `Text` |
| Settings | C | Optional MRT Settings. Unconnected = fast pure-C# path (raycast shortwave). | `Generic Data` |
| Engine |  | Run Radiance natively or via the bundled container image. Only relevant when MRT Settings enables Radiance Reflections. | `Text` |
| Run | R | Solve MRT. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Probes | X | Solved probes (for UTCI component). | `Generic Data` |
| Result | R | The complete MRT solve as one item — feed to Deconstruct MRT and UTCI. | `Generic Data` |
| Log |  | The run's full log, one line per item — stages, sizes, engine choice, timings. | `Text` |