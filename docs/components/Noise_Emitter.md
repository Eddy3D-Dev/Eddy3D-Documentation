# ![](/images/icons/Noise_Emitter.png) Noise Emitter - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Emitter%22)

![](/images/components/Noise_Emitter-crop.png)

A fixed point source of sound for Noise Run, to ask "what if": a rooftop plant, a generator, a car park gate, an event stage. Give it a point (its z is the source height, m) and a sound power level dB(A) — or a data sheet's eight octave levels, 63 Hz to 8 kHz, which win — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). It radiates equally in every direction, with no reflection off the wall or roof beside it. Wire it next to the road sources and compare two runs, with and without it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Position | Pos | Where each source stands, in metres; z is the height of the source itself (a rooftop unit: the roof plus its own height). One emitter per point. | `Point` |
| Sound Power | Lw | A-weighted sound power level, dB(A) re 1 pW, while it runs. One value per emitter or one for all. A small split air-conditioning unit is about 65, a rooftop chiller 85-95, a diesel generator 100-110. Ignored for an emitter that has Band Powers. | `Number` |
| Tilt |  | Spectral tilt about 1 kHz, dB per octave: 0 is flat, negative adds low frequencies (a fan, a transformer hums low), positive brightens. One value per emitter or one for all. Ignored for an emitter that has Band Powers. | `Number` |
| Band Powers | Bands | A data sheet's sound power per octave band, dB, 63 125 250 500 1k 2k 4k 8k Hz: eight numbers per emitter, one branch per emitter (the last branch repeats). Wins over Sound Power and Tilt. | `Number` |
| Hours |  | Hours it runs in the day (of 12), evening (of 4) and night (of 8): three numbers. Empty is always on; 0 0 8 is a night-time-only unit; 8 0 0 a daytime one. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sources |  | The emitters, for Noise Run. | `Generic Data` |