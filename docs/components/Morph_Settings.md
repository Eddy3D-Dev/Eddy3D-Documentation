# ![](/images/icons/Morph_Settings.png) Morph Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Morph%20Settings%22)

Optional engine settings for Morph Weather: which climate products to use, how the signal is interpolated onto the site, which uncertainty case to take, and how the solar fields are recomputed. Every input is optional — leave a value unwired and the Future Weather Generator falls back to its own default for it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Models | M | Climate products to morph against — GCMs for the CMIP6 Global build, GCM-RCM pairs for CORDEX — named exactly as the distribution names them (see Morph Weather's Available output). Empty uses the distribution's full model set. | `Text` |
| Ensemble | E | Also produce the multi-model ensemble mean — the file most studies report. Default `true`. | `Boolean` |
| Interpolation | I | How the monthly climate signal is interpolated from the model grid to the site: IDW (inverse distance over four valid points), NP (nearest point), AVG4P (four-point mean), BI (bilinear), SCI/SGBI/STBI (structured-grid variants). Dropdown; defaults to "Engine default", which passes nothing and lets the Future Weather Generator choose. | `Text` |
| Uncertainty | U | Which case of the model spread to take: CENTRAL, the sigma shifts, or the WARM_DRY / WARM_HUMID / HIGH_SOLAR / LOW_SOLAR corners. Dropdown; defaults to "Engine default". | `Text` |
| Sigma | s | Sigma multiplier for the sigma-based uncertainty variants (PLUS_ONE_SIGMA / MINUS_ONE_SIGMA). Only takes effect when Uncertainty is set to one of those two variants. | `Number` |
| Winter Shift | Ws | Extra winter dry-bulb spread in K, on top of the morphed signal. 0 leaves it alone. | `Number` |
| Summer Shift | Ss | Extra summer dry-bulb spread in K, on top of the morphed signal. 0 leaves it alone. | `Number` |
| Decomposition | D | Solar decomposition model used to rebuild the direct/diffuse split, e.g. MULTIMODEL_CONSTRAINED_ENSEMBLE. Your jar's own help output lists the installed set. | `Text` |
| Illuminance | L | Illuminance model used to recompute the lux columns, e.g. PEREZ_1990. | `Text` |
| Present Day | P | Also write the present-day control file, processed through the same chain — the honest baseline to compare a future file against. Default `false`. | `Boolean` |
| Threads | N | Worker threads for the morphing engine. Empty or 0 leaves the count to the engine. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | C | The assembled engine settings — wire into Morph Weather's Settings input. | `Generic` |

#### Notes

- No Run toggle: this is a pure settings bundle, split out of the Morph Weather run component the same way MRT Settings is split out of MRT Run, so the run component's socket column stays short. It solves whenever its inputs change.
- Interpolation and Uncertainty are dropdowns seeded from the engine's own known method/variant lists, with an extra leading "Engine default" entry — picking it (the default) sends nothing downstream so the Future Weather Generator uses its own default rather than a value forced by this component.
- Wiring Sigma without also setting Uncertainty to PLUS_ONE_SIGMA or MINUS_ONE_SIGMA raises a Warning ("Uncertainty Sigma only takes effect together with a sigma-based Uncertainty variant") — Sigma is otherwise silently ignored.
- The component's Message banner on the canvas summarises the live configuration (model count, whether Ensemble is on, the chosen Interpolation/Uncertainty), or reads "Defaults" when nothing has been changed.
