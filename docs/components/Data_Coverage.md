# ![](/images/icons/Data_Coverage.png) Data Coverage - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Data%20Coverage%22)

![](/images/components/Data_Coverage-crop.png)

What Eddy3D can fetch for a site before anything is fetched: one line per layer — buildings, roof shapes, terrain, fine terrain, point cloud, tree crowns, land cover, climate, natural hazards — with its provider, detail, licence and whether it covers this site. Worldwide providers always do; LiDAR (AHN in the Netherlands, USGS 3DEP in the United States) by position; the weather catalogue by its nearest station. Use it to plan the site model and see where you will have to bring your own data (a LAS/LAZ file, a survey, an EPW).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Site latitude, degrees (north positive). | `Number` |
| Longitude | Lon | Site longitude, degrees (east positive). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Layers |  | One line per layer: layer \| provider \| detail \| licence \| state \| note. | `Text` |
| Covered |  | Per layer: whether a provider covers this site. | `Boolean` |
| Summary |  | How many layers are covered, and which are not. | `Text` |