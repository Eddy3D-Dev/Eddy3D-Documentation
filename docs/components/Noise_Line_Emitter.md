# ![](/images/icons/Noise_Line_Emitter.png) Noise Line Emitter - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Line%20Emitter%22)

![](/images/components/Noise_Line_Emitter-crop.png)

A fixed LINE source of sound for Noise Run, to ask "what if": a conveyor, a rail spur, a row of loading bays, a queue. Give it a curve (its z is the source height, m) and a sound power level dB(A) PER METRE — or a data sheet's eight octave levels per metre — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). It is cut into point sources like a road, with no directivity and no reflection off the wall beside it. For one unit at one place use Noise Emitter.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Lines |  | Where each source runs, one curve per emitter, in metres; z is the height of the source itself. | `Curve` |
| Sound Power | Lw | A-weighted sound power level PER METRE of line, dB(A) re 1 pW/m, while it runs. One value per line or one for all. Ignored for a line that has Band Powers. | `Number` |
| Tilt |  | Spectral tilt about 1 kHz, dB per octave: 0 is flat, negative adds low frequencies. One value per line or one for all. Ignored for a line that has Band Powers. | `Number` |
| Band Powers | Bands | A data sheet's sound power per metre per octave band, dB, 63 125 250 500 1k 2k 4k 8k Hz: eight numbers per line, one branch per line (the last branch repeats). Wins over Sound Power and Tilt. | `Number` |
| Hours |  | Hours it runs in the day (of 12), evening (of 4) and night (of 8): three numbers. Empty is always on. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | The line emitters, for Noise Run. | `Generic Data` |