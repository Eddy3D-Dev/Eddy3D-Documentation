# ![](/images/icons/Hour_of_Year.png) Hour of Year - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Hour%20of%20Year%22)

![](/images/components/Hour_of_Year-crop.png)

Convert a start date/time and optional end date/time into hour-of-year values (1–8760) for indexing annual hourly data.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Start Month | StartMonth | Start month [1-12]. | `Integer` |
| Start Day | StartDay | Start day [1-31]. | `Integer` |
| Start Hour | StartHour | Start hour [0-23]. | `Integer` |
| End Month | EndMonth | Optional end month [1-12]. | `Integer` |
| End Day | EndDay | Optional end day [1-31]. | `Integer` |
| End Hour | EndHour | Optional end hour [0-23]. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Hours of Year | HOY | Inclusive hour-of-year values [1-8760]. | `Integer` |
| Date Times | Dates | Corresponding date and time values. | `Generic Data` |