# ![](/images/icons/Noise_Receivers.png) Noise Receivers - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Noise%20Receivers%22)

![](/images/components/Noise_Receivers-crop.png)

Where the levels are asked for: a ground grid inside a disc at pedestrian height (1.5 m; set 4 m to match an END strategic map), and a point in front of every facade at every storey of the buildings wired in. Facade levels are free-field, without the reflection off the facade they stand before, as CNOSSOS and the END define them.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Buildings | Bldgs | Building solids (Breps, extrusions, meshes) or closed footprint curves. Facade receivers are placed around each; the ground grid leaves out what is inside. Branches are flattened. | `Geometry` |
| Centre |  | Centre of the study disc. | `Point` |
| Radius |  | Radius of the study disc, m. | `Number` |
| Spacing |  | Ground grid spacing, m. 2 m gives ~17,000 points on a 150 m disc; 5 m is a quick look. | `Number` |
| Height |  | Height of the ground grid above the terrain, m: 1.5 for a pedestrian, 4 for an END map. | `Number` |
| Storey Height | Storey | Vertical spacing of the facade receivers, m; the first sits 1.5 m above the building's base. | `Number` |
| Facade Spacing | FacadeSp | Spacing of the receivers along each facade, m. | `Number` |
| Roofs |  | Also place receivers over each roof, at Facade Spacing and Height above it (a roof terrace, a rooftop plant). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Receivers |  | The receiver set, for Noise Run. | `Generic Data` |
| Ground Points | Ground | The ground grid, to preview. | `Point` |
| Facade Points | Facades | The facade receivers, to preview — drawn on the wall; the receivers themselves stand 2 m in front of it. | `Point` |
| Roof Points | Roofs | The roof receivers (when Roofs is on), to preview. | `Point` |