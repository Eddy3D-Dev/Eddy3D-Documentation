# ![](/images/icons/WRF_Probe.png) WRF Probe - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Probe%22)

![](/images/components/WRF_Probe-crop.png)

Sample a surface field of a WRF run over the whole domain, one point per grid cell. Points are in metres about the domain centre, matching the WRF Domain rectangles. Wire Points + Values into the Scalar Field Viewer, or Points + Vectors into the Vector Field Viewer, for the display.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — WRF Run's Case Folder output; run_wrf is derived from it (a run_wrf path wired directly still works). Empty uses the document's session case. | `Text` |
| Domain | d | Which nest to sample: 1 for d01, 2 for d02. | `Integer` |
| Field | F | What to sample at every cell. Wind also fills the Vectors output; the temperatures are converted from Kelvin; rain is RAINC + RAINNC since the run start. Custom reads the Variable input as a raw wrfout dataset name. | `Text` |
| Variable | V | Raw wrfout dataset name, used only when Field is Custom. It must be a 2-D surface field (south_north x west_east). | `Text` |
| Frame | i | Which history frame to sample: 0 for the first, -1 for the last. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | One point per grid cell centre, metres about the domain centre, z = 0. | `Point` |
| Values | N | The sampled field, one value per point, in the field's stated unit. | `Number` |
| Vectors | V | 10 m wind vectors, one per point, m/s — only for the wind field. | `Vector` |
| Report | R | What was sampled: file, frame instant, grid size, and the value range. | `Text` |
| Mesh | M | A quad mesh over the grid, one vertex per cell centre in the same order as Points and Values — color it by Values (or let Flex Legend do it) for a heatmap. | `Mesh` |