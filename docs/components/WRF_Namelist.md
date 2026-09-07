# ![](/images/icons/WRF_Namelist.png) WRF Namelist - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Namelist%22)

![](/images/components/WRF_Namelist-crop.png)

Write namelist.wps for a WRF project. The text is produced on every solve; the Write toggle saves it to <Working Directory>/run_wps/namelist.wps.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Working Directory | Dir | The root the case folder sits under; namelist.wps is written to <root>/<Case Name>/run_wps/. Empty uses ~/Eddy3D/WRF and the document's session case name — the same folder WRF Run resolves, so the two agree with nothing wired. A full project path with an empty Case Name is used as-is. | `Text` |
| Project | P | The WRF project from the WRF Domain component. | `Generic Data` |
| Geog Data Path | G | Folder holding the WPS static geographical data (the WPS_GEOG extract). Defaults to the shared tree WRF Geo Data downloads into. Clear it and the namelist carries a placeholder path that geogrid will reject — deliberately, so an unconfigured run fails at once rather than halfway through. | `Text` |
| Start | S | Start of the simulated period, UTC. Accepts '2024-01-15_00:00:00', '2024-01-15 00:00' or '2024-01-15'. Defaults to the most recent GFS cycle that has finished posting — the same default WRF Met Data uses. | `Text` |
| End | E | End of the simulated period, UTC. Same formats as Start. Defaults to a day after Start. | `Text` |
| Interval | I | Seconds between the driving meteorological files. 21600 (6 h) matches GFS and most reanalyses; 10800 (3 h) matches the higher-frequency products. | `Integer` |
| Write | W | Write namelist.wps to disk. Resets itself after one write. | `Boolean` |
| Case Name | Case | The case folder under Working Directory. Empty uses the document's session case name — the one WRF Run mints. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Namelist | N | The generated namelist.wps. | `Text` |
| Path | Pa | Where the namelist was written, or would be written. | `Text` |