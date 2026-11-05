# ![](/images/icons/Convert_Units.png) Convert Units - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Convert%20Units%22)

![](/images/components/Convert_Units-crop.png)

Convert values between the units Eddy3D works in — any unit into any other of the same kind, a single value or a whole hourly list. Temperature (°C, K, °F), speed (m/s, km/h, mph, kn), length, area, volume, pressure (Pa, hPa, inHg, psi), radiation (W/m², Btu/h·ft², kWh/m²), energy and power (kWh, Btu, kW, TR), mass, air flow (m³/s, cfm), rain rate, illuminance, humidity ratio (g/kg, gr/lb), enthalpy, U-value and conductivity, angle and time. EPW and every Eddy3D comfort input are in SI, OpenFOAM temperature fields are Kelvin: wire the values in, pick From and To.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Values | Val | Values to convert, in the From unit — a single value or a list (e.g. the 8760 hourly dry-bulb values of an EPW). NaN passes through. | `Number` |
| From |  | The unit the Values are in. The From unit decides what is converted (a speed, a pressure, a temperature …). A wired text ("K", "°F", "mph", "m3/h", "Celsius") works too. | `Text` |
| To |  | The unit to convert into — it has to measure the same thing as From, or the component says so. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Values | Val | The converted values, in the To unit — same order and length as the input. | `Number` |