# ![](/images/icons/Noise_Area_Emitter.png) Noise Area Emitter - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Area%20Emitter%22)

![](/images/components/Noise_Area_Emitter-crop.png)

A fixed AREA source of sound for Noise Run, to ask "what if": a car park, a courtyard, a loading yard, a market. Give it a closed curve (its z is the source height, m) and a sound power level dB(A) PER SQUARE METRE — or a data sheet's eight octave levels per square metre — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). The area is cut into point sources that share it, so the total power is the area times the level, whatever the grid. No directivity, no reflection off the walls round it. For one unit use Noise Emitter, for a line Noise Line Emitter.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Areas |  | Closed curves, one per emitter, in metres; z is the height of the source itself (the average of the curve's points), so a car park is at about a metre and a roof terrace at the roof. | `Curve` |
| Sound Power | Lw | A-weighted sound power level PER SQUARE METRE, dB(A) re 1 pW/m², while it runs. One value per area or one for all. Ignored for an area that has Band Powers. | `Number` |
| Tilt |  | Spectral tilt about 1 kHz, dB per octave: 0 is flat, negative adds low frequencies. One value per area or one for all. Ignored for an area that has Band Powers. | `Number` |
| Band Powers | Bands | Sound power per square metre per octave band, dB, 63 125 250 500 1k 2k 4k 8k Hz: eight numbers per area, one branch per area (the last branch repeats). Wins over Sound Power and Tilt. | `Number` |
| Hours |  | Hours it runs in the day (of 12), evening (of 4) and night (of 8): three numbers. Empty is always on. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | The area emitters, for Noise Run. | `Generic Data` |