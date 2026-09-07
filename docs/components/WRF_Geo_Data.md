# ![](/images/icons/WRF_Geo_Data.png) WRF Geo Data - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Geo%20Data%22)

![](/images/components/WRF_Geo_Data-crop.png)

Check and download the WPS static geographical data geogrid needs. Reports what is installed against the mandatory field list, and fetches the bundle that closes the gap.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geog Folder | Dir | Where the WPS geographical data lives (the WPS_GEOG tree). This is what geog_data_path in namelist.wps points at. Empty uses the shared tree every Eddy3D WRF project reads, so it matches WRF Namelist's Geog Data Path with nothing wired. | `Text` |
| Resolution | Res | The geog_data_res your namelist uses — 'lowres' or a resolution such as '30s'. Decides which mandatory field list is checked. 'default' means the highest resolution installed. Any other GEOGRID.TBL selector can be typed or wired in. | `Text` |
| Download | Get | Which archive to fetch. The three bundles carry everything geogrid needs at a given resolution; the individual datasets are extras — NLCD and NUDAPT are the ones worth having for a US urban study. | `Text` |
| Fetch | F | Download and extract the selected archive. Runs in the background; the canvas stays usable. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geog Path | P | The folder, to wire into WRF Namelist's Geog Data Path. | `Text` |
| Ready | R | True when every mandatory field for the chosen resolution is present. | `Boolean` |
| Status | S | What is installed, what is missing, and what to download. | `Text` |