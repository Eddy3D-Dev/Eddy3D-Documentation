# ![](/images/icons/WRF_Domain.png) WRF Domain - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Domain%22)

![](/images/components/WRF_Domain-crop.png)

Define a WRF domain and the parent grids nested around it. Domains are specified INNERMOST-FIRST: the grid you set here is the finest one, and each nest ratio adds a coarser parent around it. Outputs the project the WRF Namelist component writes, and the domain extents as rectangles centred on the innermost domain.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | Latitude of the innermost domain's centre, in decimal degrees (north positive). | `Number` |
| Longitude | Lon | Longitude of the innermost domain's centre, in decimal degrees (east positive). | `Number` |
| Projection | Proj | Map projection for the whole domain stack. Lambert conformal suits mid latitudes, Mercator the tropics, Polar the high latitudes, and Lat-Lon is a plain geographic grid whose cell size is in DEGREES rather than metres. | `Text` |
| Cell Size | dx | Grid spacing of the innermost domain, in metres (or degrees for a Lat-Lon grid). Each parent is this multiplied by the nest ratios. | `Number` |
| Grid X | nx | Number of cells across the innermost domain in x. May be rounded UP so the grid spans a whole number of parent cells. | `Integer` |
| Grid Y | ny | Number of cells across the innermost domain in y. May be rounded UP so the grid spans a whole number of parent cells. | `Integer` |
| Nest Ratios | R | One parent grid per entry, innermost parent first. Each value is how many of the child's cells fit across one of this parent's — WPS supports odd ratios only in practice, and 3 is the usual choice. Clear it for a single domain. | `Integer` |
| Nest Padding | P | How many of its OWN cells each parent extends beyond its child, on all four sides. One value applies to every parent; a list gives one per parent. Default 5. | `Integer` |
| True Lat 1 | T1 | First standard parallel, in degrees. Used by Lambert, Mercator and Polar; ignored by Lat-Lon. | `Number` |
| True Lat 2 | T2 | Second standard parallel, in degrees. Lambert only. Setting it equal to True Lat 1 gives a tangent cone. | `Number` |
| Stand Lon | SL | Longitude the projection is centred on, in degrees. Leave unwired to follow the domain centre, which is what a single-site study wants. | `Number` |
| Geog Data Res | G | geog_data_res per domain, innermost-first — the WPS static dataset resolution geogrid reads. One value applies to every domain. Defaults to 'lowres', which is what WRF Geo Data's default download installs; asking for '30s' against a low-res tree fails inside geogrid, minutes into a run. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Project | P | The WRF project. Feed this to the WRF Namelist component. | `Generic Data` |
| Domains | D | Domain extents as rectangles, outermost-first (d01 first, matching the namelist). Drawn in metres about the innermost domain's centre, so the innermost rectangle is centred on the Rhino origin. For a Lat-Lon grid the units are degrees. | `Curve` |
| Summary | S | One line per domain, d01-first: grid size, spacing, extent and centre. | `Text` |