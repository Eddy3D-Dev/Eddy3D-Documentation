## ![](../images/icons/UTCI_(Weather).png) UTCI (Weather)

![](../images/components/UTCI_(Weather)-crop.png)

Universal Thermal Climate Index from weather inputs. Connect an EPW (supplies wind, RH, ambient temp) and/or override Ambient Temp, RH, Wind, and MRT by hand. Item or list.

#### Input
* ##### W 
Path to an EPW weather file (optional). When connected, supplies Wind, Relative Humidity, and Ambient Temperature for any of those left unconnected. Manual inputs override the EPW.
* ##### M 
Mean radiant temperature (°C), as a single value or an hourly list. In EPW mode, MRT defaults to the ambient (dry-bulb) air temperature when not connected.
* ##### T 
Ambient (dry-bulb) air temperature (°C), value or list. Overrides the EPW; required in manual mode (no EPW).
* ##### RH 
Relative humidity (%), value or list. Overrides the EPW; required in manual mode.
* ##### V 
Wind speed at the 10 m UTCI reference height (m/s), value or list. Overrides the EPW; required in manual mode.

#### Output
* ##### U
Universal Thermal Climate Index (°C equivalent).
* ##### S
Thermal-stress category: 0 = no stress, negative = cold stress, positive = heat stress.
* ##### C
Thermal-stress category name.
* ##### H
No-thermal-stress hours (UTCI category 0). Emitted only when a full 8760-hour series is given.
* ##### %
Percentage of comfortable hours over the year. Emitted only when a full 8760-hour series is given.