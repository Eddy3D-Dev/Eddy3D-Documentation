# ![](/images/icons/MRT_Settings.png) MRT Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Settings%22)

![](/images/components/MRT_Settings-crop.png)

Configuration for the MRT + UTCI analysis.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Small Face Cutoff | F | Faces below this area (m²) are ignored by the thermal model. | `Number` |
| Radiance Reflections | Rad | High-fidelity shortwave via the Radiance DDS chain (true, default) vs the pure-C# raycast (false). Requires a Radiance install (or the containerized engine). | `Boolean` |
| EnergyPlus Surfaces | EP | Where the SURROUNDING surfaces' temperatures come from, which is what drives the longwave half of MRT. true (default): EnergyPlus. Eddy3D builds an epJSON from the polygons that matter to the sensors — those inside the cumulative view-factor percentile and above the Small Face Cutoff, with the rest demoted to shading surfaces — runs E+ against the EPW, and maps the surface-specific temperatures out of the ESO back onto the geometry. false: every surface is assumed to sit at air temperature. Note this is EnergyPlus, not Radiance: Radiance transports light and computes no temperatures. Requires an EnergyPlus install (or the containerized engine on the MRT component); a missing engine throws rather than silently falling back to ambient. | `Boolean` |
| Engine Timeout | T | Wall-clock cap in minutes for each external engine run (Radiance DDS, EnergyPlus). Raise for large urban scenes. | `Integer` |
| Radiance Quality | Q | Accuracy of the Radiance shortwave chain (ambient bounces and sampling). 0 Draft: sky and sun only, no interreflection — about 10% off Reference  [-ab 1 -ad 512 -lw 0.0005 (sun -ad 256)] 1 Fast: one reflection, for iterating — about 4% off  [-ab 2 -ad 1024 -lw 0.00025 (sun -ad 256)] 2 Standard: the historical default — about 2% off  [-ab 3 -ad 2000 -lw 0.0001 (sun -ad 256)] 3 Accurate: street-canyon interreflection converging — about 1.4% off  [-ab 5 -ad 4096 -lw 0.00006 (sun -ad 256)] 4 High: deep canyons and high-albedo facades — about 0.9% off  [-ab 8 -ad 8192 -lw 0.00003 (sun -ad 512)] 5 Reference: validation runs — the yardstick the others are measured against  [-ab 12 -ad 10000 -lw 0.000025 (sun -ad 1024)] Percentages are the measured departure from Reference on a triangulated 73k-polygon neighborhood. Total runtime barely moves between levels (1.10-1.14x end to end): the flags do scale the ray tracing 3.6x, but that is only 4-15% of the chain — the rest is the annual sky matrices. So choose on accuracy. Standard is the default and reproduces the flags used before this input existed. Only applies when Radiance Reflections is on. | `Text` |
| Parallelize | Par | How many processes the Radiance chain spreads its sensors over. The annual matrix multiplies (dctimestep + rmtxop) are ~60% of the chain and scale with sensor count — at 4500 sensors they are most of the run — and neither program has a threading flag, so running several over slices of the sensors is the only way to use more than one core on them. Auto (default) picks one process per core, never splitting below 500 sensors a block. Off runs the single-process chain exactly as it was before this existed. This never changes the answer: every sensor is traced by identical commands against identical octrees and sky matrices; only which file it was listed in differs. Only applies when Radiance Reflections is on. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | MRT settings for the MRT component. | `Generic Data` |