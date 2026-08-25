# ![](/images/icons/Pollutant_Source.png) Pollutant Source - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Pollutant%20Source%22)

![](/images/components/Pollutant_Source-crop.png)

Define a pollutant emission source for the wind study: a closed volume (stack tip, traffic corridor box, exhaust vent) releasing a named species at a mass rate. Wire into the Eddy3D Case component's Sources input; the species is transported as a passive scalar with turbulent diffusivity (Sct) on every direction case, and the concentration field (kg/m3) is read back by probing the species name.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | Geo | Closed mesh of the emitting volume, in metres. Thinner than the local mesh cells selects no cells — thicken it or refine around it. | `Mesh` |
| Species |  | Field name of the emitted species — pick a common one from the dropdown or type any OpenFOAM word. Sources sharing a name solve as ONE concentration field; distinct names each add a transport solve per iteration. | `Text` |
| Rate | kg/s | Total emission of this source in kg/s. The transport is linear, so results rescale to any other rate without re-running. | `Number` |
| Schmidt | Sct | Turbulent Schmidt number of the species (default 0.7, standard for atmospheric dispersion). Lower spreads the plume faster. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | Src | The source object for the Eddy3D Case component's Sources input. | `Generic Data` |