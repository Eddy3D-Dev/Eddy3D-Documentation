# ![](/images/icons/Wind_Climate.png) Wind Climate - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Climate%22)

![](/images/components/Wind_Climate-crop.png)

Long-term directional wind statistics for pedestrian comfort: for every direction sector (36 × 10° by default) and season (year + Dec-Feb, Mar-May, Jun-Aug, Sep-Nov, named for the hemisphere), the sector probability, the calm share and a Weibull c, k fitted by maximum likelihood to the non-calm hours of a MULTI-YEAR record — ERA5 via Open-Meteo (any coordinate, no key), the nearest NOAA ISD or GHCNh station, local EPW files or a CSV — or the City of London Annex A table. A typical year cannot carry a safety criterion: Lawson's 15 m/s for 0.022 % of the year is about two hours, and a TMY holds two hours of one composite year. Wire the Wind Climate output into Pedestrian Wind Comfort (with VAF's Speed Ratios) to classify from P(U > u) = Σ p·exp(−(u/(r·c))^k); the report says whether the record is long enough to measure the safety tail. Downloads run off the canvas and are cached per year in WeatherCache/WindRecords inside the Eddy3D folder of your local app data.Sources: ERA5 (Hersbach et al. 2020, Copernicus C3S) via Open-Meteo; NOAA NCEI Integrated Surface Database (ISD-Lite) and its successor GHCNh; City of London Wind Microclimate Guidelines (2019), Annex A.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | Src | Where the wind comes from. ERA5 (Open-Meteo): hourly 10 m reanalysis for the 0.25° cell at Latitude/Longitude, open-terrain exposure. ISD station (NOAA): the nearest station within 100 km covering half the years (or the one named in Station); NOAA stopped updating ISD-Lite in August 2025. GHCNh station (NOAA): its successor, current to the day before, for 2000 onward — the nearest station within 100 km that measures wind (screened on the last year), or the one named in Station; 12-34 MB a station-year, read once and kept as a small file. EPW files / CSV file: the paths in Files. City of London Annex A: the guideline's published table (c at 120 m, terrain-corrected for the City — not valid elsewhere). Global Wind Atlas (.lib file): a generalized wind climate you downloaded from globalwindatlas.info, path in Files — the class nearest Source Terrain's roughness length, at Reference Height (between the file's heights, linear in ln z; outside them it refuses). It is the wind over FLAT terrain of that roughness, not the local wind, and it has no seasons. | `Text` |
| Latitude | Lat | Site latitude (°). Optional when Location carries one. | `Number` |
| Longitude | Lon | Site longitude (°). Optional when Location carries one. | `Number` |
| Location | Loc | Optional: a Wind Conditions record (its site, else its station, gives the coordinates; its EPW is used for the EPW source) or an EPW path (its header's coordinates). | `Generic Data` |
| Files |  | EPW paths (each file is one year-block) for the EPW source, or one CSV path for the CSV source: UTC time (ISO 8601), speed m/s, direction ° from north, optional gust. | `Text` |
| Years |  | Years to fetch for ERA5 / ISD / GHCNh (GHCNh from 2000), as "1995-2024" or one year. 20-30 years is the usual record for a safety tail; each year is one request, cached on disk. | `Text` |
| Station | Stn | ISD: pin a station by USAF-WBAN (e.g. 037720-99999, London Heathrow). GHCNh: its 11-character GHCN id (e.g. USW00014739, Boston Logan) or an ISD id with a WBAN number. Empty = nearest. | `Text` |
| Sectors | N | Direction sectors, centred on north: 36 = 10° (City of London / ESDU), 16 = 22.5°. | `Integer` |
| Calm Threshold | Calm | Speeds below this (m/s) are calm — their own category, never a sector (an EPW or ISD calm carries direction 0, which would otherwise spike the north sector). The Weibull fits are truncated here. | `Number` |
| Source Terrain | SrcTerr | EN 1991-1-4 category the SOURCE speeds stand for. II (open country) for ERA5 — ECMWF brings its 10 m wind down with a short-grass roughness of 0.03 m — and for a WMO-sited anemometer. Change it when the station is known to stand elsewhere. | `Text` |
| Site Terrain | SiteTerr | EN 1991-1-4 category around the SITE: every speed is transferred by c_r,site/c_r,source at the Reference Height (the same factor Wind Conditions applies). 'None' keeps the source's speeds — then the ABL inlet should also be the source's terrain. | `Text` |
| Reference Height | Zref | Height (m) of the transfer, and the height the climate's speeds then describe — the ABL reference height, 10 m for a standard anemometer. The comfort classifier re-references the CFD ratios to it. | `Number` |
| Fetch |  | Download the years not yet cached (ERA5 / ISD / GHCNh). Local files and fully cached records build without it; a failed fetch stays reported until you press Fetch again or change the location. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Climate | Climate | The climate object — for Pedestrian Wind Comfort's Wind Climate input and the CLI (its JSON is what `E3D wind-climate --out` writes). | `Generic Data` |
| Directions | Dir | Sector centres (° from north, wind FROM). | `Number` |
| Probabilities | p | Annual share of all hours per sector (%); with the calm share they sum to 100. | `Number` |
| Weibull c | c | Annual Weibull scale per sector (m/s, after any transfer). | `Number` |
| Weibull k | k | Annual Weibull shape per sector. | `Number` |
| Calm |  | Annual calm share (%). | `Number` |
| Sector Table | Table | The annual sector table as Markdown (p, hours, mean, max, c, k, fit). | `Text` |
| Report |  | Origin, per-year completeness, exposure, transfer, every season's table, and whether the record is long enough to measure a 0.022 % safety tail. | `Text` |
| Rose Frequencies | Rose | Wind-rose petals: {sector}[speed band] annual frequency (%) from the fitted Weibulls, bands as in Rose Bands. | `Number` |
| Rose Bands | Bands | Speed-band labels for Rose Frequencies (m/s). | `Text` |