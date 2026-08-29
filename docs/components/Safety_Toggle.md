# ![](/images/icons/Safety_Toggle.png) Safety Toggle - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Safety%20Toggle%22)

![](/images/components/Safety_Toggle-crop.png)

A boolean toggle that is always FALSE when a file is opened. Useful for preventing automatic execution of heavy work. When Run is connected to several component inputs, they run one Grasshopper solution at a time in canvas order. Double-click to toggle.

#### Input

*None*

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Run |  | Boolean value (always FALSE on file open). Two or more directly connected components are triggered sequentially in canvas order. Run stays TRUE until manually toggled. | `Boolean` |