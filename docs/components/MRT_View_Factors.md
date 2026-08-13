# ![](/images/icons/MRT_View_Factors.png) MRT View Factors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20View%20Factors%22)

![](/images/components/MRT_View_Factors-crop.png)

Assembles tagged surfaces + sensors into a radiation model, builds the sky dome, and solves probe-to-polygon view factors. Feed the VF Model to SurfaceTemp (EnergyPlus) and/or MRT Solve. The sweep is the expensive part of an MRT run — solving it once here lets the downstream stages re-run without repeating it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surfaces | S | Tagged radiation surfaces (MRT Surface). | `Generic Data` |
| Sensors | P | Sensor probes (MRT Sensors). | `Generic Data` |
| Sky Dome Subdivisions | SkyDiv | Resolution of the internal MRT sky hemisphere, as a SUBDIVISION LEVEL: the dome has 6 x 4^level faces, half of them above the horizon. Higher levels smooth the view factors but cost time on every probe; 5 (3072 patches) is ample for MRT. | `Text` |
| Fidelity | Fid | How much of the occlusion raycasting to spend. Balanced (default): polygons whose view factor is below 5e-5 are assumed visible instead of raycast — each such polygon can shift the normalized result by less than that, and the sweep runs several times faster. Fast: same idea at 2e-4, and the sky dome is capped at 768 patches (level 4) — the dome only refines the probe-specific sky view fraction, which 768 patches already pin to ±0.02 of the 3072-patch answer. Quick iteration on big models. Reference: every contribution above the 1e-5 floor is raycast (the original behavior). Use for the final run when publishing numbers. Sky patches are always raycast at every fidelity. | `Text` |
| Run | R | Solve the view factors. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| VF Model | VF | The assembled radiation model with solved view factors. Feed to SurfaceTemp (EnergyPlus) and MRT Solve. | `Generic Data` |
| Sky Dome | D | The sky dome mesh (preview). | `Mesh` |
| Log |  | The run's full log, one line per item — stages, sizes, engine choice, timings. | `Text` |