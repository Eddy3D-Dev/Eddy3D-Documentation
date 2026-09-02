# ![](/images/icons/STL_Exporter.png) STL Exporter - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22STL%20Exporter%22)

![](/images/components/STL_Exporter-crop.png)

Export geometry to STL format for OpenFOAM or other CFD tools. Supports meshes and Breps (auto-meshed); binary or ASCII, single or multiple files.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | Geo | Meshes or Breps to export. | `Geometry` |
| File Path | File | Destination file path (.stl). | `Text` |
| Mode |  | Export mode: Binary or ASCII encoding, as one file or one file per input geometry ("List"). Also accepts the legacy index 0-3. | `Text` |
| Edge Length | Edge | Optional: maximum edge length for auto-meshing Breps (m). 0 = default meshing. | `Number` |

#### Output

*None*