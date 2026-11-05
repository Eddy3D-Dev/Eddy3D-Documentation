# ![](/images/icons/Noise_Map.png) Noise Map - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Map%22)

![](/images/components/Noise_Map-crop.png)

Colours a run's receivers in the END 5 dB bands (yellow from 50-55, orange at 60, red at 65, blue above 80): a ground mesh of the grid, a vertical quad per facade receiver, and the points, values and colours behind them for custom tagging. Pick Lden or a single period. Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | The run from Noise Run. | `Generic Data` |
| Metric |  | Which level to draw: Lden, or one period (Lday 12 h, Levening 4 h, Lnight 8 h). Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Ground Mesh | Ground | The ground grid as coloured quads. | `Mesh` |
| Facade Mesh | Facades | A coloured quad per facade receiver. | `Mesh` |
| Points |  | Every receiver. | `Point` |
| Values |  | The chosen level per point, dB(A). | `Number` |
| Colors |  | Band colour per point. | `Colour` |
| Legend Labels | Labels | The bands, lowest first. | `Text` |
| Legend Colors | LegendColors | One colour per band label. | `Colour` |
| Roof Mesh | Roofs | A coloured quad on the roof under each roof receiver. | `Mesh` |