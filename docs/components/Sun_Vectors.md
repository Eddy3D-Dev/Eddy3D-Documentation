# ![](/images/icons/Sun_Vectors.png) Sun Vectors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Vectors%22)

Builds a set of sun positions for a date-and-hour window at a chosen time step (6 minutes and finer), computed from site and clock rather than read from an EPW's hourly rows. Feeds Sun Path; the Sun Hours, Shadow and Solar Irradiation analysis components read a weather record directly and no longer need this wired in.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather | W | Optional weather object. When connected, Latitude, Longitude and Time Zone are read from it and override the numeric inputs below. | `Generic` |
| Latitude | Lat | Degrees north. | `Number` |
| Longitude | Lon | Degrees east. | `Number` |
| Time Zone | TZ | Hours ahead of UTC, standard time — not the summer offset. | `Number` |
| From Month | FM | Start month of the sample period [1-12]. Default 1. | `Integer` |
| From Day | FD | Start day [1-31]. Default 1. | `Integer` |
| To Month | TM | End month, inclusive [1-12]. Default 12. | `Integer` |
| To Day | TD | End day, inclusive [1-31]. Default 31 — together the From/To defaults span the full year. | `Integer` |
| Start Hour | SH | First hour of day [0-23]. | `Integer` |
| End Hour | EH | Last hour of day, exclusive [1-24]. Default 24. | `Integer` |
| Timestep | TS | Samples per hour. 1 = hourly (the old behaviour), 10 = a 6-minute step. Cost is linear in this — 10x the samples really is 10x the rays. | `Integer` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north (Ladybug's convention). | `Number` |
| Daylight Saving | DST | Treat the hour window as summer clock time. EPW data is standard time, so leave this off when matching a weather file. | `Boolean` |
| Elevation Cutoff | EC | Drop samples at or below this solar elevation. 0 keeps everything above the horizon; raise it to ignore the grazing sun that refraction makes unreliable. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sun Vectors | SV | Sun samples — direction, the hours each represents, and the instant sampled. Feeds Sun Path; the analysis components read a weather record directly instead. | `Generic` |
| Directions | D | The same directions as plain vectors, for drawing. | `Vector` |
| Hours | H | Hours each sample represents. Sums to the daylight in the period. | `Number` |
| Report | R | Sample count, daylight hours and the step used. | `Text` |
