# ![](/images/icons/MRT_Dataset_Curator.png) MRT Dataset Curator - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Dataset%20Curator%22)

![](/images/components/MRT_Dataset_Curator-crop.png)

Export the solved MRT field as a machine-learning dataset: one row per sensor per hour with spatial features, hourly climate drivers and the MRT/UTCI targets.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Probes | X | Solved probes from the MRT component. Sensors that never went through the solve carry no MRT series and are rejected. | `Generic Data` |
| Buildings | B | Building Breps or meshes, used for the signed-distance and roof-height features. Leave unconnected to write those columns as NaN. | `Geometry` |
| UTCI | U | Optional UTCI tree from the UTCI (Simulation) component, {hour}(probes) or {probe}(hours). Branch order must match the Probes list. Unconnected writes NaN. | `Number` |
| EPW | W | Path to the EPW weather file — supplies the hourly climate columns (DNI, DHI, GHI, dry-bulb, RH, wind, sun position). Unconnected writes those columns as NaN. | `Text` |
| Folder | F | Output folder for the CSV parts. Created if it does not exist. | `Text` |
| Name | N | File-name stem; parts are written as {Name}_part0001.csv. Defaults to the folder name. | `Text` |
| Ground Level | G | Datum the relative height and roof height are measured from. Defaults to the lowest sensor. Pin it explicitly when curating several cases into one dataset, or the datum shifts with the sensor grid and the height features stop being comparable. | `Number` |
| Rows per File | RPF | Soft cap on data rows per CSV part (default 2,000,000). An hour is never split across parts, so a case with more sensors than this writes one hour per part. | `Integer` |
| Run | R | Write the dataset. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Files | F | The written CSV parts, in order. | `Text` |
| Rows | R | Total data rows written, excluding headers. | `Integer` |
| Columns | C | The dataset's column names, in write order. | `Text` |