# ![](/images/icons/Prediction_Confidence.png) Prediction Confidence - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Prediction%20Confidence%22)

![](/images/components/Prediction_Confidence-crop.png)

Score an ML wind prediction per point: red outside the model's training window, where a feature lies outside the training envelope, or where models disagree by more than 25 %; amber near the window edge, in the envelope's outer 10 %, or where models differ by more than 10 %; green otherwise. The envelope is measured from Dataset Curator CSVs or Verify Prediction logs — none is shipped for the bundled models, because none is published. ML screening prediction, not CFD: use it to compare options, then confirm anything that matters with a Wind Study (planning authorities do not accept surrogate results).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points |  | The points the prediction was made at (absolute Z). | `Point` |
| Buildings |  | Building geometry, to measure SDF / Bldg_height / Z_relative for the envelope test (as the predictor does). | `Geometry` |
| Boundary Conditions | BC | The study's boundary conditions (reference height for U/U_ref). | `Generic Data` |
| Pedestrian Level | PedLevel | Pedestrian mounting height [m], as given to the predictor. | `Number` |
| Envelope |  | Training-envelope sources: Dataset Curator CSVs and/or Verify Prediction logs. | `Text` |
| Ensemble |  | Optional: the same direction predicted by two or more models, one branch per model, one value per point. | `Number` |
| Edge Margin | Margin | Distance [m] from the training window's edge counted as 'near'. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Level |  | 0 green, 1 amber, 2 red, per point. | `Integer` |
| Reasons |  | Why each point got its level. | `Text` |
| Colors |  | Traffic-light colour per point. | `Colour` |
| Summary |  | Counts per level and what was (and was not) checked. | `Text` |