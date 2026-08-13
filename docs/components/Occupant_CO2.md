# ![](/images/icons/Occupant_CO2.png) Occupant CO2 - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Occupant%20CO2%22)

![](/images/components/Occupant_CO2-crop.png)

CO2 generation rate of one occupant by age, activity and sex (Persily & de Jonge 2017).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Age | A | Occupant age in years (0-100). | `Number` |
| Metabolic Rate | M | Activity level in met. Must be one of 1.0, 1.2, 1.4, 1.6, 2.0, 3.0, 4.0 — the table is not interpolated. | `Number` |
| Sex | S | 0 = average of both (default), 1 = male, 2 = female. | `Integer` |
| Breathing Flow | BF | Breathing minute volume in L/min, used to convert the emission into an exhaled concentration. | `Number` |
| Breaths | B | Breathing rate (breaths per minute). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Occupant | O | This occupant, for the Indoor Species Case component — which then derives the mouth boundary from these numbers rather than from a guessed velocity. | `Generic Data` |
| CO2 Rate | Q | CO2 generation rate (L/s). | `Number` |
| Exhaled CO2 | E | Exhaled-breath CO2 concentration (ppm). | `Number` |
| Body Mass | kg | Mean body mass for the group (kg). | `Number` |
| BMR | B | Basal metabolic rate (MJ/day). | `Number` |
| Body Surface Area | BSA | Du Bois body surface area (m2), from the group's mass and a 171 cm height. | `Number` |
| Tidal Volume | TV | Air moved per breath (L). | `Number` |