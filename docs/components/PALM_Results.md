# ![](/images/icons/PALM_Results.png) PALM Results - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Results%22)

![](/images/components/PALM_Results-crop.png)

Read a PALM output field: one variable, one time frame, as values and a colored mesh over the domain. Variables and times available in the case are listed on every solve.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — PALM Run's Case Folder output. Empty uses the document's session case. | `Text` |
| File | F | Which output file to read. Averaged fields are the ones a comfort map wants. | `Text` |
| Variable | V | The PALM variable to read — pick from the catalog, type any name, or check the Variables output for what the file actually offers. Empty picks the first biometeorology variable present, else the first variable. | `Text` |
| Frame | T | Time frame index; -1 is the last frame written so far. | `Integer` |
| Domain | D | The PALM Domain OR the Static Driver's Driver output, to place the mesh in model space. Unwired, the mesh sits at the world origin — the spacing always comes from the file itself. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | The field as a colored mesh at z = 0 (blue low to red high). | `Mesh` |
| Values | Val | The field row-major, south-west first — one value per mesh face. | `Number` |
| Variables | Vars | Every data variable the file carries. | `Text` |
| Times | Ti | The simulated seconds of each frame in the file. | `Number` |
| Info | I | File, variable, frame and range. | `Text` |