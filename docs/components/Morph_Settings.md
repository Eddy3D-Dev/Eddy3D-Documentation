# ![](/images/icons/Morph_Settings.png) Morph Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Morph%20Settings%22)

![](/images/components/Morph_Settings-crop.png)

Engine settings for Morph Weather: the method (Future Weather Generator or the World Bank CCKP anomalies), climate products, spatial interpolation, uncertainty case and solar methods. Every value left empty stays on the Future Weather Generator's own default; the CCKP methods ignore the generator-only settings.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Models | M | Climate products (GCMs for the CMIP6 Global build, GCM-RCM pairs for CORDEX) named as the distribution names them — see Morph Weather's Available output. Empty uses the distribution's full model set. | `Text` |
| Ensemble | E | Also produce the multi-model ensemble mean. This is the file most studies report. | `Boolean` |
| Interpolation | I | How the monthly climate signal is interpolated from the model grid to the site: IDW (inverse distance over four valid points), NP (nearest point), AVG4P (four-point mean), BI (bilinear), SCI/SGBI/STBI (structured-grid variants). | `Text` |
| Uncertainty | U | Which case of the model spread to take: CENTRAL, the sigma shifts, or the WARM_DRY / WARM_HUMID / HIGH_SOLAR / LOW_SOLAR corners. | `Text` |
| Sigma | s | Sigma multiplier for the sigma-based uncertainty variants. | `Number` |
| Winter Shift | Ws | Extra winter dry-bulb spread in K, on top of the morphed signal. 0 leaves it alone. | `Number` |
| Summer Shift | Ss | Extra summer dry-bulb spread in K, on top of the morphed signal. 0 leaves it alone. | `Number` |
| Decomposition | D | Solar decomposition model used to rebuild the direct/diffuse split, e.g. MULTIMODEL_CONSTRAINED_ENSEMBLE. Your jar's help lists the installed set. | `Text` |
| Illuminance | L | Illuminance model used to recompute the lux columns, e.g. PEREZ_1990. | `Text` |
| Present Day | P | Also write the present-day control file, processed through the same chain — the honest baseline to compare a future file against. | `Boolean` |
| Threads | N | Worker threads for the morphing engine. Empty or 0 leaves the count to the engine. | `Integer` |
| Method |  | Which engine morphs the file. Future Weather Generator: the Java application you install (needs its jar). CCKP median / 10th / 90th percentile: the World Bank Climate Change Knowledge Portal's CMIP6 ensemble at 0.25° — monthly anomalies of temperature, humidity, wind, solar and longwave radiation read for the site's grid cell, applied to the file as monthly shifts and stretches. No key, no Java; pressure, cloud cover, wind direction and rain stay as in the present-day file. The percentiles are taken per variable and month, so the 10th and 90th are the ends of the model spread, not two coherent climates. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | C | Settings for Morph Weather. | `Generic Data` |