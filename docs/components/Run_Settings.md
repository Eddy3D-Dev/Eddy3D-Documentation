# ![](/images/icons/Run_Settings.png) Run Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Run%20Settings%22)

![](/images/components/Run_Settings-crop.png)

Configure solver run controls for Eddy3D.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Iter |  | Total solver iterations (endTime). Optional; default is 1000. |
| WriteInt |  | Write interval in iterations. Optional; default is 20. |
| Keep |  | Number of time directories to keep (purgeWrite). Optional; default is 3. |
| Turb |  | RANS turbulence model (OpenFOAM 12). The four best for urban wind: Realizable k-ε (default; AIJ/COST732 best practice for pedestrian wind), Standard k-ε (ABL baseline), RNG k-ε (high-strain / recirculation), and SST k-ω (separation, near-wall). All run on the template's existing fields. |
| CPU |  | Number of CPUs/subdomains for parallel runs. -1 (default) = auto: all cores but one. Optional. |
| Algo |  | Pressure-velocity coupling for the steady solver. SIMPLE (default) is the robust, conservatively under-relaxed baseline. SIMPLEC adds the consistent correction so it tolerates much higher relaxation (p 0.7, U/turbulence 0.9), which usually converges in fewer iterations on a good urban mesh — try it for speed, fall back to SIMPLE if a hard case stalls or oscillates. Optional; default is SIMPLE. |
| Age |  | Solve the mean age of air (OpenFOAM 'age' function object) during the run. Age [s] is the time since the air at each point entered the domain — the urban ventilation/stagnation map (low = well flushed, high = trapped in canyons/courtyards). Adds a cheap scalar transport solved at each write; the 'age' field is then viewable in ParaView or probe-able. Optional; default is false. |
| Robust |  | Numerics on a 1-5 accuracy<->robustness dial that sets the convection schemes, under-relaxation factors and non-orthogonal correctors together. 1 = most accurate (second-order convection, high relaxation) — captures wakes/eddies but needs a good mesh; 5 = most robust (first-order upwind, heavy relaxation) — always converges but smears wakes by numerical diffusion; 3 = balanced TVD. 4 reproduces the shipped baseline, so the default changes nothing. Pairs with the algorithm: SIMPLEC tolerates the higher-relaxation accurate levels (1-2) best. Optional; default is 4. |
| PotFoam |  | Initialise velocity/pressure with a quick potentialFoam (potential-flow Laplace) solve before simpleFoam, so the run starts from a developed, divergence-free field instead of a uniform one. Removes the first-iteration velocity overshoot of a cold start and shortens convergence. Complements the Warm-up Iterations ramp (potentialFoam seeds the field; the ramp damps the first iterations with first-order upwind + heavy turbulence relaxation). Optional; default is off (shipped behaviour). |
| Warmup |  | Run this many initial iterations with robust 1st-order upwind + heavy turbulence under-relaxation, then ramp up to the numerics dial for the rest of the run. Tames the cold-start velocity overshoot without losing final accuracy. -1 (default) = automatic: scales with the robustness dial (robust levels 4-5 warm up, accurate levels 1-2 do not). 0 = force off. >0 = explicit count. |
| Monitors |  | Write the domain min/max-magnitude and volume-average of the solved fields (U, p, k, ε/ω, νt) each write-time. Cheap convergence + stability monitor — the max \|U\| trace flags a cold-start overshoot or divergence early. Default off. |
| PedAvg |  | Write the area-average of U on a horizontal plane at pedestrian height (1.75 m) each write — the comfort-relevant mean wind speed, sampled from the live mesh (no topoSet). Default off. |
| Cp |  | Write the surface pressure coefficient (Cp) field each write, computed from the ABL wind speed at building height (dynamic pressure reference). View it on the building surfaces in ParaView. Default off. |
| Conv |  | Auto-stop tolerance: the solver stops once the p, U and turbulence initial residuals all drop below this value (SIMPLE residualControl) — typically 30-60 % faster than running the full iteration count. Default 1e-4; 0 disables auto-stop (always runs all iterations). |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| RunSet |  | Run settings for the solver. |
| Logs |  | Debug logs from settings generation. |
