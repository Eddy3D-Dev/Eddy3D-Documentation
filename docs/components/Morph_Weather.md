# ![](/images/icons/Morph_Weather.png) Morph Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Morph%20Weather%22)

![](/images/components/Morph_Weather-crop.png)

Morph a present-day EPW into future-climate EPWs with the Future Weather Generator (future-weather-generator.adai.pt), then feed the result to any Eddy3D workflow. Needs Java 17+ and the generator's .jar, which Eddy3D does not ship: download the distribution you need (CMIP6 Global, CORDEX-CMIP5 Europe, …) into ~/Eddy3D/FWG. The tool is licensed CC BY-NC-SA 4.0 — noncommercial use, attribution required.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Output Folder | Dir | Folder the morphed weather files are written to (one subfolder per baseline EPW). Unwired: ~/Eddy3D/FutureWeather. | `Text` |
| EPW | W | Path to the present-day EPW to morph — wire it straight from Download Weather. | `Text` |
| Scenarios | S | Emission pathways to generate, as the installed distribution names them (CMIP6 Global: ssp126, ssp245, ssp370, ssp585; CORDEX builds: rcp26, rcp45, rcp85). Empty runs the distribution's full default set. The Available output lists what your jar actually offers. | `Text` |
| Timeframes | T | Future periods to generate, e.g. 2050 and 2080 (the CMIP6 Global build centres them on 2036-2065 and 2066-2095). Empty runs the distribution's defaults. | `Text` |
| Settings | C | Optional Morph Settings — climate products, interpolation, uncertainty case, solar methods. Unwired, the generator runs on its own defaults. | `Generic Data` |
| FWG Jar | J | Path to the Future Weather Generator .jar. Unwired, Eddy3D looks in ~/Eddy3D/FWG, then Downloads, then the EDDY3D_FWG_JAR environment variable. | `Text` |
| Run | R | Morph the weather file. A full multi-model run takes minutes to hours; cancel from the right-click menu. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| EPW Files | EPW | Paths of the morphed weather files, one per scenario / period / model. | `Text` |
| Labels | L | What each file represents, aligned with EPW Files (e.g. ssp370_2050_ensemble). | `Text` |
| Available | A | The scenarios, periods and climate products the installed jar reports — read from its own help output, so it is correct for whichever distribution you have. | `Text` |
| Logs | Log | The run's full log, one line per item. | `Text` |