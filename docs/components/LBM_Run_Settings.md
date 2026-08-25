# ![](/images/icons/LBM_Run_Settings.png) LBM Run Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Run%20Settings%22)

![](/images/components/LBM_Run_Settings-crop.png)

Solver controls for the container-based LBM wind engine (grid spacing, warmup and averaging windows, probe layer, GPU, container runtime).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Grid Spacing | dx | Lattice spacing in meters. Cell count grows with 1/dx^3 — halving dx costs 8x memory and ~16x time. | `Number` |
| Warmup | W | Physical seconds of simulated wind discarded before averaging starts. 0 = auto: two domain flow-throughs (length / reference speed), at least 60 s — fixed seconds quietly under-run large domains. | `Number` |
| Averaging | A | Physical seconds of simulated wind averaged into the reported field. 0 = auto: four domain flow-throughs, at least 120 s. | `Number` |
| Probe Height | Hp | Height above ground of the pedestrian-level result layer (m). | `Number` |
| Probe Spacing | Sp | Spacing of the result grid (m). | `Number` |
| GPU |  | Run the CUDA build of the solver image (needs an NVIDIA GPU + container toolkit; Windows/Linux only — macOS containers have no CUDA). | `Boolean` |
| Runtime | Rt | How the solver runs. Auto prefers Podman, falls back to Docker, then to a native install; Docker and Podman run the same OCI image. Native runs a host-installed eddy3dWind executable with NO container at all — the Windows path when neither Podman nor Docker Desktop is an option. Native is CPU (OpenMP) only; the CUDA build ships as a container image. | `Text` |
| Image | Img | Container image override. Empty = pkastner/openlb-wind:latest. | `Text` |
| Jitter | Jit | Slowly vary the inflow direction by a few degrees (deterministic). Seeds resolved unsteadiness a steady analytic inflow lacks, so exposed upstream areas stop reading unrealistically calm. Off = perfectly steady inflow. | `Boolean` |
| Jitter Amplitude | Jd | Direction variation in degrees when Jitter is on. | `Number` |
| Vegetation Drag | Veg | Crown density for PLAIN meshes wired into the LBM Run component's Vegetation input, as Cd x leaf area density (1/m): 0.1 sparse, 0.25 typical, 0.5 dense. Vegetation Region objects carry their own Cd x LAD and ignore this. | `Number` |
| Perturbed Inflow | UQ | Run a perturbed-inflow ensemble instead of a single solve: members re-run the case with the inflow speed varied +/-10% and direction +/-6 deg (realistic measurement uncertainty); LBM Field then reports the mean plus a per-point spread that flags wake regions where the result is inflow-sensitive. Runtime scales with Ensemble. | `Boolean` |
| Ensemble | N | Member count when Perturbed Inflow is on (3 = nominal + speed pair, 5 adds the direction pair, up to 9). | `Integer` |
| Vegetation Density | VegD | Crown density preset for PLAIN vegetation meshes (sets Vegetation Drag = Cd x LAD). Custom uses the Vegetation Drag input. Vegetation Region objects carry their own Cd x LAD and ignore both. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | LBM run settings for the 'LBM Run' component. | `Generic Data` |