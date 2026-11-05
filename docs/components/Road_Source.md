# ![](/images/icons/Road_Source.png) Road Source - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Road%20Source%22)

![](/images/components/Road_Source-crop.png)

A road as a CNOSSOS-EU line source: its centreline, a daily traffic total, the heavy-vehicle share and a speed. One item per curve, or one value for all of them. Feed the sources to Noise Run.  The daily total is split 70/20/10 % over day (07-19), evening (19-23) and night (23-07), and heavies half-and-half between two-axle and multi-axle trucks — the neutral defaults when a count says no more.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Roads |  | Road centrelines, one curve per road, in metres with z at the road surface. | `Curve` |
| Daily Traffic | AADT | Annual average daily traffic, vehicles per day, both directions. One value per road or one for all. A residential street carries a few hundred, a primary road ten to twenty thousand, a motorway fifty thousand and more. | `Number` |
| Heavy Share | Heavy | Share of heavy vehicles (> 3.5 t) in the total, 0-1. Urban streets 0.02-0.05, arterials 0.05-0.10, motorways 0.10-0.20. | `Number` |
| Speed |  | Representative speed, km/h. Heavy vehicles are capped at 80. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | One line source per road, for Noise Run. | `Generic Data` |