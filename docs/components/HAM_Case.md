# ![](/images/icons/HAM_Case.png) HAM Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22HAM%20Case%22)

![](/images/components/HAM_Case-crop.png)

Build a heat-and-moisture case for a layered wall. Wire the Case output into the Run component (Containerized engine — hamFoam ships only in the container). Pick a Preset to reproduce one of the two HAMSTAD benchmark tutorials.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case name (no spaces). | `Text` |
| Working Directory | Dir | Working directory (default ~/Eddy3D/Cases). | `Text` |
| Preset | P | Custom builds the case from the inputs below. The two HAMSTAD entries reproduce the upstream hamFoam tutorials exactly and IGNORE every input below this one. | `Text` |
| Wall |  | Build-up from the HAM Wall component. Not read under a preset. | `Generic Data` |
| Outside | O | Exterior climate (HAM Climate). Not read under a preset. | `Generic Data` |
| Inside | I | Interior climate (HAM Climate). Not read under a preset. | `Generic Data` |
| Initial Temperature | T0 | Initial wall temperature (°C). | `Number` |
| Initial RH | RH0 | Initial relative humidity of the wall (%). Sets the capillary pressure the solver starts from; it derives the moisture content from that through each material's own retention curve. | `Number` |
| Cell Size | CS | Target cell size through the wall (m). Cells are additionally clustered toward every layer face. | `Number` |
| Grading | G | Expansion ratio clustering cells toward both faces of every layer. Surface moisture fluxes need sub-millimetre first cells; uniform spacing diverges within the first steps. | `Number` |
| Duration | D | Simulated duration (days). | `Number` |
| Write Interval | WI | Result write interval (hours). | `Number` |
| Extras |  | Optional user function objects from the Custom Function Object component, applied every time the case is written. A HAM wall has no snappyHexMesh step, so refinement regions do not apply here — the component says so rather than ignoring them silently. | `Generic Data` |
| Write | W | Click to write the case to disk. Resets automatically so it never re-writes on recompute. | `Boolean` |
| Clear | X | Click to delete the case folder. Resets automatically so it never re-deletes on recompute. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Directory | Dir | Where the case was written. | `Text` |
| Commands | Cmd | The OpenFOAM commands this case runs, in order. | `Text` |
| Logs | L | Write log / status. | `Text` |
| Case | C | The HAM case for the Run component (Containerized engine only). | `Generic Data` |