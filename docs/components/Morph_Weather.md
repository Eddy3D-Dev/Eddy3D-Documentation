# ![](/images/icons/Morph_Weather.png) Morph Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Morph%20Weather%22)

Morphs a present-day EPW into future-climate EPWs by shelling out to the external Future Weather Generator (future-weather-generator.adai.pt) — Eddy3D does not implement the climate morphing itself and does not ship the tool, since it is licensed CC BY-NC-SA 4.0 (noncommercial). Wire the morphed EPW paths into any Eddy3D workflow that consumes weather: wind comfort, MRT/UTCI, indoor, UMF.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Output Folder | Dir | Folder the morphed weather files are written to, one subfolder per baseline EPW. Unwired: `~/Eddy3D/FutureWeather`. | `Text` |
| EPW | W | Path to the present-day EPW to morph — wire it straight from Download Weather. | `Text` |
| Scenarios | S | Emission pathways to generate, named as the installed distribution names them (CMIP6 Global: ssp126, ssp245, ssp370, ssp585; CORDEX builds: rcp26, rcp45, rcp85). Empty runs the distribution's full default set — the Available output lists what your jar actually offers. | `Text` |
| Timeframes | T | Future periods to generate, e.g. 2050 and 2080 (the CMIP6 Global build centers these on 2036-2065 and 2066-2095). Empty runs the distribution's defaults. | `Text` |
| Settings | C | Optional Morph Settings — climate products, interpolation, uncertainty case, solar methods. Unwired, the generator runs on its own defaults. | `Generic` |
| FWG Jar | J | Path to the Future Weather Generator `.jar`. Unwired, Eddy3D looks in `~/Eddy3D/FWG`, then Downloads, then the `EDDY3D_FWG_JAR` environment variable. | `Text` |
| Run | R | Morph the weather file. A full multi-model run takes minutes to hours; cancel it from the right-click menu. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| EPW Files | EPW | Paths of the morphed weather files, one per scenario / period / model. | `Text` |
| Labels | L | What each file represents, aligned with EPW Files (e.g. `ssp370_2050_ensemble`). | `Text` |
| Available | A | The scenarios, periods and climate products the installed jar reports, read from its own help output — correct for whichever distribution you have. | `Text` |
| Logs | Log | The run's full log, one line per item. | `Text` |

#### Notes

- **Needs Java 17+ and a separately downloaded Future Weather Generator `.jar`.** Eddy3D cannot bundle it (CC BY-NC-SA 4.0, noncommercial) and cannot auto-download it either — the vendor's URLs reject non-browser clients. Jar resolution order: the wired FWG Jar input, then a jar picked via the right-click menu, then `~/Eddy3D/FWG`, then Downloads, then the `EDDY3D_FWG_JAR` environment variable.
- **Right-click menu**: *Cancel run* (kills the running Java process); *Re-run* (forces a fresh run regardless of the Run toggle's current state); *Download Future Weather Generator…* (opens the vendor's download page in a browser); *Select FWG jar…* (file picker to point the component at a specific `.jar`); *Show capabilities* (a message box listing the scenarios, timeframes and models the installed jar reports).
- **Available is populated on every solve, independent of Run** — it probes the resolved jar's capabilities (cached on disk per jar) so you can check valid Scenario/Timeframe identifiers before ever running.
- A successful run adds a Remark naming the jar's version and the CC BY-NC-SA citation requirement.
- Run works whether it is a click-toggle or a wired boolean: a wired toggle held `true` still relaunches when the EPW or any other input changes. The Logs output is populated even when the run failed, since that's when it matters most.
