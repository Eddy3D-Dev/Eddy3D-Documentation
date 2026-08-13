# ![](/images/icons/Download_Weather.png) Download Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Download%20Weather%22)

![](/images/components/Download_Weather-crop.png)

Download an EPW weather file from a direct URL, or search climate.onebuilding.org by station name, WMO ID, or dataset year.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Search |  | Direct EPW or weather ZIP URL; or a station name, WMO ID, country, state, or dataset year (e.g. 'New York', '725030', '2009-2023'). | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| EPW File | EPW | Path to the downloaded EPW weather file. | `Text` |
| Logs | L | Execution log. | `Text` |
| Stations | Stn | Stations matching the search filter. | `Text` |