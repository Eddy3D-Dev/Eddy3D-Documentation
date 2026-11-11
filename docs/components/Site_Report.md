# ![](/images/icons/Site_Report.png) Site Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Site%20Report%22)

![](/images/components/Site_Report-crop.png)

Write a client-ready PDF site report from a weather file and the Rhino viewports: climate key statistics, wind rose and Weibull, climograph, psychrometric chart, hour-by-day year charts of solar radiation, wind speed and UTCI, the weather-only comfort scenarios (no sun / no wind / full protection), captured views, methodology and glossary, plus the natural-hazard record around the station (earthquakes from USGS, storms, floods, wildfires, volcanoes and landslides from NASA EONET, tsunami run-ups from NOAA NCEI; Hazards switches it off). Every sentence is assembled from the measured numbers by fixed rules. Results from other components that implement the report seam add their own chapters.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Folder | Dir | Output folder. Default: ~/Eddy3D/Reports. | `Text` |
| Title | T | Report title, printed on the cover and in the footer. | `Text` |
| Weather | W | The weather year: an EPW file path (e.g. from Download Weather) or an Eddy3D Weather object. | `Generic Data` |
| Views | V | Rhino viewport names to capture ("Perspective", "Top", or a named view). The first capture is the cover picture; the rest fill the Site views chapter. Empty: the active view. | `Text` |
| Images | Img | PNG or JPEG files to include after the captures (a rendering, a site photo); the file name is the caption. | `Text` |
| Results | R | Optional results that add chapters: a Share Pack (its Pack output — one chapter of map pages with the share of area per class, per set), a site's Origin (LiDAR Site's Origin output — a table in the methodology of which dataset each layer came from) or an object implementing the report seam. Others are ignored with a remark. | `Generic Data` |
| Author | A | Author or firm, printed on the cover. | `Text` |
| Logo | L | PNG or JPEG logo for the cover's corner; empty for the Eddy3D wordmark. | `Text` |
| Future | Fut | Projected years to compare with the present one: EPW paths from Morph Weather (labelled from their scenario and horizon) or Weather objects. Adds the Future climate chapter. | `Generic Data` |
| Hazards | Haz | Add the Natural hazards section: events within 100 km of the station from three public catalogues (USGS earthquakes M ≥ 4.5 since 1970, NASA EONET storms / floods / wildfires / volcanoes / landslides since 2015, NOAA NCEI tsunami run-ups since 1900), cached for 30 days. False skips the three requests; offline, the lines read "no data". | `Boolean` |
| Write | Go | Write the report. Edge-triggered: a click, or a wired value turning true, writes once. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| PDF |  | The written report. | `Text` |
| Summary | Sum | What was written, and anything worth knowing about it. | `Text` |