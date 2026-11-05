# ![](/images/icons/Verify_Prediction.png) Verify Prediction - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Verify%20Prediction%22)

![](/images/components/Verify_Prediction-crop.png)

Compare an ML wind prediction with a CFD result at the same points: VDI 3783-9 hit rate (D = 0.25, W = 0.05·U_ref; ≥ 0.66 passes), FAC2, Willmott's index of agreement, R, bias, MAE and RMSE per direction and overall, plus the per-point deviation. Write appends the compared points to a verification log (Dataset Curator columns + U_pred + U_cfd) that is retraining data and a training envelope for Prediction Confidence. ML screening prediction, not CFD: use it to compare options, then confirm anything that matters with a Wind Study (planning authorities do not accept surrogate results).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points |  | The points both results were sampled at (absolute Z). | `Point` |
| Predicted |  | ML wind speeds [m/s], one branch per wind direction (the Wind Predictor's Values output). | `Number` |
| CFD |  | CFD wind speeds [m/s] at the same points, one branch per direction in the same order (e.g. Probe \|U\|). | `Number` |
| Boundary Conditions | BC | The study's boundary conditions: U_ref sets the hit rate's absolute tolerance W = 0.05·U_ref and the log's normalised columns; the wind directions label the branches. | `Generic Data` |
| Buildings |  | Optional: building geometry, so the log carries SDF / Bldg_height exactly as the Dataset Curator writes them. | `Geometry` |
| Pedestrian Level | PedLevel | Pedestrian mounting height [m] for the log's features. | `Number` |
| Log |  | Verification log CSV to append to (created with its header when new). | `Text` |
| Case |  | A name for this comparison in the log. | `Text` |
| Write |  | Append the compared points to the log. Fires once per set of inputs, also when wired. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Metrics |  | Agreement metrics: overall first, then one block per direction. | `Text` |
| Hit Rate | HitRate | VDI 3783-9 hit rate per direction (then overall, last). | `Number` |
| Passes |  | Hit rate ≥ 0.66 per direction (then overall, last). | `Boolean` |
| Deviation | Dev | Predicted − CFD [m/s] per point, one branch per direction. | `Number` |
| Colors |  | Per point: green within the hit-rate tolerance, blue over-predicted, red under-predicted. | `Colour` |