# ![](/images/icons/CO2_Air_Quality.png) CO2 Air Quality - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22CO2%20Air%20Quality%22)

![](/images/components/CO2_Air_Quality-crop.png)

Grade indoor CO2 (ppm) against EN 16798-1 or another CO2-based IAQ standard.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Indoor CO2 | C | Indoor CO2 concentration(s) in ppm. | `Number` |
| Outdoor CO2 | O | Outdoor background in ppm. One value, or one per indoor reading. | `Number` |
| Standard | S | 0 EN 16798-1, 1 LEHB (JP), 2 SS 554 (SG), 3 HK EPD, 4 UBA (DE), 5 DOSH (MY), 6 NBR (BR). | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Index | I | IAQ class, 1 = best. The worst value differs per standard — never compare across standards. | `Integer` |
| Class | L | The class name the standard itself uses. | `Text` |
| Source | Src | Citation of the source document. | `Text` |