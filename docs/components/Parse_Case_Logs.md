# ![](/images/icons/Parse_Case_Logs.png) Parse Case Logs - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Parse%20Case%20Logs%22)

![](/images/components/Parse_Case_Logs-crop.png)

Parses log files in a case folder and reports any FOAM errors. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Case to parse logs from. | `Generic Data` |
| Run |  | Parse log files when true. Optional; default is false. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Log Summary | Summary | Summary of log parsing results. | `Text` |
| Errors |  | Errors found in log files. | `Text` |
| Warnings |  | Warnings found in log files. | `Text` |