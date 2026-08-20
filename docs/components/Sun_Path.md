# ![](/images/icons/Sun_Path.png) Sun Path - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Path%22)

Draws the sun's daily arcs, hourly analemmas and sampled sun positions as curves and points on a dome — pure geometry built from the same solar calculation the sun studies use, with no new physics. It exists to let a wrong north, a southern-hemisphere sign error, or an off-by-one time zone show up visually instead of hiding in a table of numbers.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather | W | Optional weather object. When wired, Latitude, Longitude and Time Zone below are read from it instead of the manual values. | `Generic` |
| Latitude | Lat | Site latitude in degrees north. Default 0°. | `Number` |
| Longitude | Lon | Site longitude in degrees east. Default 0°. | `Number` |
| Time Zone | TZ | Hours ahead of UTC, standard time. Default 0. | `Number` |
| Center | C | Point the sun dome is centred on. Default the world origin. | `Point` |
| Radius | R | Dome radius in model units. Default 100; must be positive or the component errors. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north. Default 0°. | `Number` |
| Arc Days | AD | Day-of-year values to draw arcs for. Left empty, draws the June/December solstices and the March equinox instead. | `Integer` |
| Sun Vectors | SV | Optional sun samples to place as points on the dome — wire the same ones a sun study traced and the diagram shows exactly what was sampled. | `Generic` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Arcs | A | One curve per requested day, tracing the sun's path across the sky wherever it is above the horizon. | `Curve` |
| Analemmas | An | One curve per hour of the day (24 total) — the sun's position at that clock hour, sampled across the year. | `Curve` |
| Suns | S | The wired Sun Vectors placed as points on the dome. | `Point` |
| Compass | Cp | Horizon circle at the dome's radius, oriented to the given North. | `Circle` |
| Report | R | Text summary of the site, the north offset, and what was drawn (arc days, analemma count, sun count). | `Text` |
