# ![](/images/icons/Download_Weather.png) Download Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Download%20Weather%22)

![](/images/components/Download_Weather-crop.png)

Pick an EPW weather file from a bundled catalog of 60,868 climate files — every TMYx station on climate.onebuilding.org plus the EnergyPlus store (IWEC, TMY3, CWEC, SWERA, …) — with your own folders and Morph Weather results listed alongside them. Click the Station widget and choose Browse library… for a searchable table with a map, or type a name, WMO id or direct URL. The catalog is searched offline; only the chosen file is downloaded, once, into the weather cache.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Station |  | Which climate file to use. Click the widget and choose Browse library… to pick from the catalog with a map and a spec sheet; the value stored is the file's own name (e.g. DEU_BE_Berlin-Tempelhof.AP.103840_TMYx.2009-2023). A station name, WMO id, country or dataset year still works as a search — the best match nearest the site wins — and a direct EPW or ZIP URL is downloaded as-is. | `Text` |
| Latitude | Lat | Site latitude in decimal degrees (north positive). With a site, the browser lists the nearest stations first, every row states its distance, and the map shows both. Optional — leave empty and the catalog is listed in publisher order. | `Number` |
| Longitude | Lon | Site longitude in decimal degrees (east positive). See Latitude. | `Number` |
| Folders | Dirs | Extra folders of .epw files to list beside the online catalogs — a studio library, measured AMY years, or a Morph Weather output folder (whose files are labelled with their scenario and horizon). Scanned recursively; each file's own LOCATION header supplies its position. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| EPW File | EPW | Path to the downloaded EPW weather file. | `Text` |
| Logs | L | Execution log. | `Text` |
| Stations | Stn | The catalog entries that matched, nearest the site first. One line per file: name, dataset, source and distance. | `Text` |
| Station | S | What the chosen file is: station, period, publisher, WMO id, position, elevation, time zone, ASHRAE climate zone and the design conditions its publisher states. | `Text` |
| Extra Files | X | The .stat and .ddy files that came with the EPW, when the publisher ships them — design days and the climate summary. Empty for a file that has none. | `Text` |