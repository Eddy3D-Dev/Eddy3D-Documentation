# ![](/images/icons/LBM_Run_Settings.png) LBM Run Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22LBM%20Run%20Settings%22)

![](/images/components/LBM_Run_Settings-crop.png)

Solver controls for the container-based LBM wind engine (grid spacing, warmup and averaging windows, probe layer, GPU, container runtime).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Grid Spacing | dx | Lattice spacing in meters. Cell count grows with 1/dx^3 — halving dx costs 8x memory and ~16x time. | `Number` |
| Warmup | W | Physical seconds of simulated wind discarded before averaging starts. | `Number` |
| Averaging | A | Physical seconds of simulated wind averaged into the reported field. | `Number` |
| Probe Height | Hp | Height above ground of the pedestrian-level result layer (m). | `Number` |
| Probe Spacing | Sp | Spacing of the result grid (m). | `Number` |
| GPU |  | Run the CUDA build of the solver image (needs an NVIDIA GPU + container toolkit; Windows/Linux only — macOS containers have no CUDA). | `Boolean` |
| Runtime | Rt | Container runtime. Auto prefers Podman and falls back to Docker; both run the same OCI image. | `Text` |
| Image | Img | Container image override. Empty = pkastner/openlb-wind:latest. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | LBM run settings for the 'LBM Run' component. | `Generic Data` |