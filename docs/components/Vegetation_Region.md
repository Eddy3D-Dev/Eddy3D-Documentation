# ![](/images/icons/Vegetation_Region.png) Vegetation Region - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vegetation%20Region%22)

![](/images/components/Vegetation_Region-crop.png)

Create a vegetation region from tree crown solids. Pick a Tree Type preset for a typical leaf area density and foliage drag coefficient, or choose Custom and wire your own LAD. The output drives BOTH the Outdoor+ (OpenFOAM/UMF) case and the LBM Run component's Vegetation input, with consistent canopy drag.  Library sources — LAD (crown-average, m²/m³): Sjöman et al. (2021) Arboricult. Urban For. 47(6), plant area index of 64 urban species; Klingberg et al. (2017) Urban For. Urban Green. 26, Gothenburg leaf area mapping; ENVI-met Albero plant database conventions; Zhang et al. (2018) Atmosphere 9(5):198 and Beijing For. Univ. J. (2017) ENVI-met validations for subtropical evergreens. Cd (per frontal leaf area, 0.1–0.3): Katul et al. (2004) Boundary-Layer Meteorol. 113; Mayhead (1973) Agric. Meteorol. 12, conifer wind-tunnel drag; Gillies et al. (2002) J. Geophys. Res. 107(D24), drag vs. wind speed and crown streamlining. Note: NIST TN 2039 (2019) reports Cd ≈ 2.8 against total projected area per volume — a different normalization; do not mix it with the Cd·LAD convention used here. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Vegetation Mesh | Mesh | Tree crown / vegetation solids (closed meshes). Model the canopy volume, not the trunk. | `Mesh` |
| Leaf Area Density | LAD | Leaf area density (m2 of leaf per m3 of crown). Only used when Tree Type is Custom; presets bring their own typical value. | `Number` |
| Vegetation Properties | Props | Optional vegetation property settings (from the Vegetation Properties component). Carries Cd and the transpiration/radiation coefficients; defaults are used when unwired. | `Generic Data` |
| Mesh Settings | MeshSet | Optional meshing settings for vegetation. | `Generic Data` |
| Tree Type | Type | Vegetation library preset — archetypes and common urban species — that sets a typical leaf area density AND foliage drag coefficient for both engines (shown on the component banner). Custom uses the LAD input and Vegetation Properties Cd instead. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Vegetation Region | Vegetation | Vegetation region object: wire into the Outdoor+ case (UMF canopy region) and/or the LBM Run component's Vegetation input (porous drag cells). | `Generic Data` |