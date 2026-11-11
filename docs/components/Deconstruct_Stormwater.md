# ![](/images/icons/Deconstruct_Stormwater.png) Deconstruct Stormwater - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20Stormwater%22)

![](/images/components/Deconstruct_Stormwater-crop.png)

Turns a stormwater result into meshes and numbers. This is the ONLY component that materialises the field — a run holds millions of values and emitting them all as a tree would freeze the canvas, so ask here for the field and the time you want.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | A run from Stormwater Run. | `Generic Data` |
| Field |  | Which field to draw. The (max) fields are peaks over the whole run — what a design is checked against — and are tracked every solver step, so they never miss a peak between snapshots. The (at time) fields read the stored snapshot nearest the Time input. The last three come from the terrain alone and are available from a Fast run. | `Text` |
| Time |  | Minutes from the storm's start, for the (at time) fields. The nearest stored snapshot is used. | `Number` |
| Range |  | Value range mapped onto the colour ramp. Leave unconnected to fit the data. Pin it when comparing two options — otherwise each rescales to its own maximum and the worse one can look identical to the better one. | `Domain` |
| Cutoff |  | Hide cells at or below this value. For a depth field it is in MILLIMETRES, and it is what stops a site-wide film of numerically-zero water from painting the whole model and hiding the ponding that matters. 10 mm is a sensible floor for ponding. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh |  | The field as a coloured mesh, one quad per cell. Cells rather than a smooth surface on purpose: the answer IS piecewise constant, and smoothing it would imply a resolution the model does not have. | `Mesh` |
| Points | Pts | Centre of every drawn cell. | `Point` |
| Values |  | Field value at each point — depth in mm, velocity in m/s, hazard as HR, area in m², slope in m/m. | `Number` |
| Colors |  | Colour at each point. | `Colour` |
| Range |  | The value range actually used, for a legend. | `Domain` |