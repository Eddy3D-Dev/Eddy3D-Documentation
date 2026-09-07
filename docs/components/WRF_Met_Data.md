# ![](/images/icons/WRF_Met_Data.png) WRF Met Data - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Met%20Data%22)

![](/images/components/WRF_Met_Data-crop.png)

Download the meteorological GRIB files that drive a WRF run. The file list and the Vtable are shown before you fetch anything, so a window can be checked first.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| GRIB Folder | Dir | Where to put the downloaded GRIB files. Wire this to WRF Run's GRIB Folder. Empty uses the grib folder under the resolved case (Working Directory + Case Name), which is where WRF Run looks with nothing wired. | `Text` |
| Source | Src | Where to fetch from. NOMADS needs no account but keeps only about ten days; RDA has the archive and needs a free account. | `Text` |
| Start | S | First instant the run needs, UTC. e.g. 2024-01-15_00:00:00. Defaults to the most recent GFS cycle that has finished posting. | `Text` |
| End | E | Last instant the run needs, UTC. Defaults to a day after Start. | `Text` |
| Interval | I | Hours between boundary files. 6 is the usual GFS spacing; 3 gives a smoother forcing and twice the download. | `Integer` |
| Resolution | R | GFS grid spacing. 0p25 is a quarter degree — the operational default and what you want unless the download is a problem. | `Text` |
| Credential | Cr | For RDA only. Give the PATH of a file containing your API token, or the NAME of an environment variable holding it — never the value itself. Grasshopper saves a component's text inputs into the .gh document in plain text, so a literal would be published with the definition. | `Text` |
| Fetch | F | Download the files listed above. Runs in the background. | `Boolean` |
| Working Directory | WD | The root the case folder sits under when GRIB Folder is empty. Empty uses ~/Eddy3D/WRF. | `Text` |
| Case Name | Case | The case folder under Working Directory when GRIB Folder is empty. Empty uses the document's session case name — the one WRF Run mints. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| GRIB Folder | P | The folder, to wire into WRF Run. | `Text` |
| Vtable | V | The ungrib variable table this product needs. Wire to WRF Run's Vtable. | `Text` |
| Files | Fs | The files that make up this window. | `Text` |
| Status | St | What will be fetched, and what happened. | `Text` |