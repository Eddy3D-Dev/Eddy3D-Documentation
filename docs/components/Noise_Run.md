# ![](/images/icons/Noise_Run.png) Noise Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Run%22)

![](/images/components/Noise_Run-crop.png)

Road-traffic noise after CNOSSOS-EU (Directive 2015/996, 2021/1226 coefficients): the emission of every road and the propagation to every receiver — divergence, air absorption, the ground effect on the mean plane, diffraction over roofs and crests — summed per octave band and period into Lday, Levening, Lnight and Lden. Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours.  PROTOTYPE LIMITS: homogeneous atmospheric conditions only (no favourable-propagation share, so distant levels run a little low); no facade reflections; no path around a corner (a receiver behind a block gets the over-the-roof path only, which reads low); one ground factor for the whole site; no rail, aircraft or industry. Not a compliance calculation.  Method: CNOSSOS-EU, Commission Directive (EU) 2015/996 Annex II (road emission §2.2, propagation §2.5), coefficients per Delegated Directive (EU) 2021/1226, https://eur-lex.europa.eu/eli/dir/2015/996/oj — pinned against NoiseModelling (Université Gustave Eiffel) on the ISO/TR 17534-4 cases.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | Road sources from Road Source and/or Roads From OSM, and point and line sources from Noise Emitter and Noise Line Emitter. | `Generic Data` |
| Receivers |  | The receiver set from Noise Receivers. | `Generic Data` |
| Buildings | Bldgs | Building solids or meshes: what blocks and diffracts the sound. Branches are flattened. | `Geometry` |
| Terrain |  | Terrain meshes or surfaces. Flat at the lowest building base (z = 0 with no buildings) when unwired. Branches are flattened. | `Geometry` |
| Ground |  | CNOSSOS ground factor of the whole site: hard (asphalt, paving, water — a city centre), mixed, or soft (grass, soil — a park). Soft ground lowers mid-frequency levels at distance; hard ground is the conservative choice. | `Text` |
| Cell Size | Cell | Raster cell of the scene heightfield, m. 5 m is a quick look on a large site; 1 m resolves ordinary buildings. A wall thinner than a cell is not seen. | `Number` |
| Engine | Eng | Auto: the OpenCL GPU when one answers, else the CPU. GPU: the GPU, and a fallback to the CPU is reported, never silent. CPU: every core. Same CNOSSOS terms either way; the GPU hands the rare section it cannot decide in single precision back to the CPU. | `Text` |
| Run |  | Solve the map. Works as an inline button or as a wired toggle — with a wire held true, the run relaunches whenever the inputs change. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | The whole run as ONE item, for Noise Map. | `Generic Data` |
| Lden |  | Lden per receiver, dB(A), in receiver order. Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours. | `Number` |
| Lnight |  | Lnight per receiver, dB(A). | `Number` |
| Points |  | The receivers as solved, re-seated on the terrain. | `Point` |
| Summary |  | Counts, extremes, timing and the caveats. | `Text` |