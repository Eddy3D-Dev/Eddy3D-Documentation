# ![](/images/icons/ML_Model.png) ML Model - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22ML%20Model%22)

![](/images/components/ML_Model-crop.png)

Download an ONNX wind-prediction model from HuggingFace for the Wind Predictor component. Yel 2.0 is public; Esen 1.0 and Poyraz 1.0 need a HuggingFace token. All are 8-channel Wind Predictor models. (Yel 1.0 is a different architecture — the GAN image model used by GAN Predict via its API — and cannot be loaded here.) Models cache in ~/Eddy3D/Models/ and are reused on subsequent runs (a model already downloaded to the old ~/SUS_LAB/ folder is moved over, not re-fetched).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Model |  | Select the ONNX model to download. | `Text` |
| HF Token | HFToken | HuggingFace access token (starts with hf_) or a file path to a .txt file containing the token. Required for private models (Esen, Poyraz). Not required for public models (Yel). | `Text` |
| Run |  | Set to True to validate the token and download the model if needed. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Status |  | Human-readable status / diagnostic message. | `Text` |
| File Path | FilePath | Full path to the cached ONNX model file, or null on failure. | `Text` |
| Progress |  | Download progress percentage (0–100). | `Number` |