# ![](/images/icons/CHT_Case.png) CHT Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CHT%20Case%22)

![](/images/components/CHT_Case-crop.png)

Build a conjugate heat transfer case from solids, air cavities and boundaries. Wire the Case output into the Run component (Containerized engine). Method: Kastner & Dogan (2020), SimAUD 2020 405-412, https://www.researchgate.net/publication/346039320_Solving_Thermal_Bridging_Problems_for_Architectural_Applications_with_OpenFOAM.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case name (no spaces). | `Text` |
| Working Directory | Dir | Working directory (default ~/Eddy3D/Cases). | `Text` |
| Solids | S | Solid regions (CHT Solid components). | `Generic Data` |
| Cavities | C | Air cavities (CHT Air Cavity components). | `Generic Data` |
| Boundaries | B | Face boundary conditions (CHT Boundary components). Unassigned faces are adiabatic. | `Generic Data` |
| Cell Size | CS | Background cell size (m). | `Number` |
| Refinement | R | Surface refinement level (each level halves the cell size at region surfaces). | `Integer` |
| Initial Temperature | T0 | Initial temperature (°C). | `Number` |
| Duration | D | Transient: simulated seconds — run long enough to reach steady state (the reference wall assembly converged well before 10000 s). Steady State on: the ITERATION budget instead (500 is OpenFOAM's own default for a steady CHT case). | `Number` |
| Steady State | SS | Solve to steady state instead of marching in time. Right for U-values and thermal bridges, which are defined on the converged field. Duration then counts iterations. | `Boolean` |
| Extras |  | Optional user additions from the Refinement Region and Custom Function Object components. Applied every time the case is written. foamMultiRun scopes function objects per region, so set a Region on each one. | `Generic Data` |
| Engine |  | OpenFOAM engine. CHT currently supports Docker/Podman containers only. | `Text` |
| Write | W | Click to write the case to disk. Resets automatically so it never re-writes on recompute. | `Boolean` |
| Clear | X | Click to delete the case folder. Resets automatically so it never re-deletes on recompute. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Directory | Dir | Where the case was written. | `Text` |
| Commands | Cmd | The OpenFOAM commands this case runs, in order. | `Text` |
| Logs | L | Write log / status. | `Text` |
| Case | C | The CHT case for the Run component (Containerized engine only for now). | `Generic Data` |