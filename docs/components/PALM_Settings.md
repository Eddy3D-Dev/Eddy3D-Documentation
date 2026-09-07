# ![](/images/icons/PALM_Settings.png) PALM Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Settings%22)

![](/images/components/PALM_Settings-crop.png)

Steer the PALM-4U run: duration, wind, temperature and outputs. Forcing is idealized (constant wind, cyclic boundaries). Comfort switches on radiation and the biometeorology module, whose PET/UTCI/MRT maps are PALM-4U's point.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Duration | T | Simulated hours after spin-up. Two hours settles a street-resolving flow field; a diurnal comfort study wants 24. | `Number` |
| Spinup | Sp | Wall and soil spin-up in hours before the atmosphere starts. 0.5 is a floor for surface temperatures worth reading. | `Number` |
| Output Interval | Oi | Minutes between outputs; also the averaging window for the _av fields. | `Number` |
| Wind Speed | U | Driving wind speed (m/s), applied as a constant geostrophic wind. | `Number` |
| Wind Direction | Dir | Meteorological wind direction in degrees (wind FROM; 270 = westerly). | `Number` |
| Air Temperature | Ta | Near-surface air temperature (°C). | `Number` |
| Humidity | q | Near-surface specific humidity (kg water per kg air). 0.008 is a mild mid-latitude day. | `Number` |
| Date Time | Dt | Simulation start, 'YYYY-MM-DD hh:mm:ss +zz'. Drives the sun. | `Text` |
| Slice Height | H | Height above ground of the horizontal result slices (m). 2 m is pedestrian level. | `Number` |
| Output Variables | Out | PALM data_output names, one per item — pick from the catalog or type any name PALM knows. Empty uses the default set: pedestrian-level u/v/w/theta, surface temperature, and PET/UTCI/MRT when Comfort is on. | `Text` |
| Comfort | C | Run radiation and biometeorology (PET, UTCI, MRT maps). Off makes a plain LES — faster, wind only. | `Boolean` |
| Cores | N | MPI ranks for the run. Empty picks them automatically at launch: the container daemon's CPU count (on macOS and Docker Desktop the VM's allotment is the real ceiling), capped so every rank owns a worthwhile patch of the grid. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | The run settings. Feed to PALM Run. | `Generic Data` |
| Summary | Su | What will run, one line each. | `Text` |