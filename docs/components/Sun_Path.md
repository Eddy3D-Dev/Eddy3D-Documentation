# ![](/images/icons/Sun_Path.png) Sun Path - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Path%22)

![](/images/components/Sun_Path-crop.png)

Daily sun arcs, analemmas and sun positions as curves and points — north-aware, drawn from the same solar geometry the sun studies use.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather | W | Optional weather object; Latitude, Longitude and Time Zone are read from it. | `Generic Data` |
| Latitude | Lat | Degrees north. | `Number` |
| Longitude | Lon | Degrees east. | `Number` |
| Time Zone | TZ | Hours ahead of UTC, standard time. | `Number` |
| Center | C | Where the dome is centred. | `Point` |
| Radius | R | Dome radius in model units. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north. | `Number` |
| Arc Days | AD | Day-of-year values to draw arcs for. Empty draws the solstices and the equinox. | `Integer` |
| Sun Vectors | SV | Optional sun samples to place as points on the dome — wire the same ones the study uses and the diagram shows exactly what was traced. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Arcs | A | One daily sun arc per requested day, above the horizon. | `Curve` |
| Analemmas | An | One analemma per hour of the day — the sun's position at that clock hour across the year. | `Curve` |
| Suns | S | Sun positions for the wired Sun Vectors, on the dome. | `Point` |
| Compass | Cp | Horizon circle, oriented to the given north. | `Circle` |
| Report | R | Site, north and what was drawn. | `Text` |