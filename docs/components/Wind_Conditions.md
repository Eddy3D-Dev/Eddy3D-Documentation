# ![](/images/icons/Wind_Conditions.png) Wind Conditions - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Conditions%22)

![](/images/components/Wind_Conditions-crop.png)

Bin a year of EPW wind into direction sectors — frequency, speed histogram, mean speed and a Weibull fit per sector — with the station's origin (provider, id, period, coordinates, elevation) and the site's location in one record. Optionally transfers the station's speeds to the site's terrain per EN 1991-1-4 (the anemometer stands in open country; the site does not). Wire the record into the ABL component's Wind Directions: it supplies directions AND speeds, travels into the study manifest and the Study Report, and lets VAF scale the hourly series by the same factor.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| EPW |  | Path to the EPW weather file (Download Weather's EPW output). | `Text` |
| Sectors | N | Direction sectors around the compass; 16 = 22.5° sectors centred on the compass points (N, NNE, …). 8 and 36 are the other common choices. | `Integer` |
| Solve Sectors | Solve | How many sectors to SIMULATE. 0 or ≥ Sectors solves every sector; a divisor of Sectors takes every k-th (8 of 16 = the 45° compass); anything else takes the most frequent. The Directions/Speeds outputs and the ABL follow this choice; the record keeps every sector for the report. | `Integer` |
| Calm Threshold | Calm | Speeds below this (m/s) are calm: no usable direction, excluded from the sectors and reported as the calm share. | `Number` |
| Site Terrain | SiteTerr | EN 1991-1-4 terrain category around the SITE. Set it to transfer the station's speeds to the site: every sector speed is multiplied by c_r,site(z)/c_r,station(z) at the reference height (§4.3: c_r = k_r·ln(z/z0), k_r = 0.19·(z0/0.05)^0.07). Category IV at 10 m is ×0.54 of open country — an urban inlet fed the raw station speed overstates every pedestrian wind by nearly two. 'None' keeps the station's speeds. | `Text` |
| Station Terrain | StTerr | EN 1991-1-4 Table 4.1 terrain category around the STATION's anemometer. WMO exposure is open country — category II — which is the default and the right answer for nearly every airport TMY. Only read when Site Terrain is set. | `Text` |
| Reference Height | Zref | Height (m) the transfer is evaluated at — the ABL reference height, 10 m for a standard anemometer. | `Number` |
| Site Latitude | Lat | Optional site latitude (°), recorded with the study and reported with the station distance. | `Number` |
| Site Longitude | Lng | Optional site longitude (°). | `Number` |
| Site Elevation | Elev | Optional site elevation above sea level (m). Recorded beside the station's so a reader can judge whether the station represents the site. | `Number` |
| Speed Ratios | Ratios | Optional: the Speed Ratios object a solved study emits (Velocity Amplification Factors). With it, Critical Sectors ranks the sectors by what the SITE exceeds under them; without it the ranking is the station's own (every ratio 1), the prior before any CFD has run. | `Generic Data` |
| Threshold | Thresh | Speed (m/s, hourly mean at the reference height) whose exceedance ranks the sectors — the comfort criterion's threshold, e.g. 5 (NEN 8100 / Lawson walking). Default 5. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Conditions | WC | The record — wire into the ABL component's Wind Directions (and into VAF's Wind Conditions when a transfer is applied). | `Generic Data` |
| Directions | Dirs | Solved sector directions (° from north, wind-from). | `Number` |
| Speeds | U | Mean speed per solved sector (m/s) at the reference height, after any transfer. | `Number` |
| Frequencies | Freq | Share of non-calm hours per solved sector (%). | `Number` |
| Weibull k | k | Weibull shape per solved sector (dimensionless; NaN when a sector had too few hours). | `Number` |
| Weibull λ | λ | Weibull scale per solved sector (m/s), after any transfer. | `Number` |
| Report |  | The sector table and origin as Markdown. | `Text` |
| Critical Sectors | Critical | Every sector's direction (° from north), ranked by its share of the year the site spends above Threshold: sector frequency × P(site speed > Threshold \| that sector), the term the probabilistic comfort classifier sums. The top of the list is where a scale-resolving (DES) solve earns its cost; the rest can stay steady RANS. | `Number` |
| Critical Shares | Share | Each ranked sector's share (0-1) of the total exceedance, in the order of Critical Sectors. | `Number` |