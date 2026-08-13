# ![](/images/icons/Sleep_Comfort.png) Sleep Comfort - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sleep%20Comfort%22)

![](/images/components/Sleep_Comfort-crop.png)

Sleep-adapted Gagge two-node model (Yan et al. 2022) for bedrooms.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Air Temperature | Ta | Dry-bulb air temperature (°C). | `Number` |
| Radiant Temperature | Tr | Mean radiant temperature (°C). | `Number` |
| Air Speed | V | Air speed (m/s). | `Number` |
| Relative Humidity | RH | Relative humidity (%). | `Number` |
| Sleepwear | Clo | Sleepwear insulation (clo). | `Number` |
| Quilt Thickness | Qt | Quilt thickness (cm). Sets the COVERED AREA, not the insulation — raise Clo for a warmer bed. | `Number` |
| Sleep Time | T | Minutes since falling asleep — drives the metabolic and core-temperature polynomials. | `Number` |
| Duration | D | Simulated minutes. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| SET |  | Standard Effective Temperature (°C). | `Number` |
| Sensation | TS | Predicted thermal sensation. | `Number` |
| Discomfort | DISC | Thermal discomfort. | `Number` |
| Skin Temp | Tsk | Mean skin temperature (°C). | `Number` |
| Core Temp | Tcr | Core temperature (°C). | `Number` |
| Wettedness | W | Skin wettedness (0-1). | `Number` |