# ![](/images/icons/Infection_Risk.png) Infection Risk - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Infection%20Risk%22)

![](/images/components/Infection_Risk-crop.png)

Airborne infection risk by the Wells–Riley model, and the ASHRAE 241-2023 equivalent clean airflow check. Well-mixed: P = 1 − exp(−dose), with the room concentration rising from zero under outdoor air + air cleaning + deposition (0.24 /h) + viral inactivation (0.63 /h) (Buonanno, Stabile & Morawska 2020). Spatial: the Indoor Case's viral tracer, probed at the breathing zone, rescaled to quanta/m³ by what the case measured leaving the room (Exhaust Tracer × Carried Flow), or — without those — by the Viral Emitter's rate × MESHED zone volume; given both, the second cross-checks the first. Ventilation-only, as the CFD removes nothing else. The case writes the tracer per m³ of air, the carried flow in m³/s and each emitter's meshed zone volume on both the isothermal and the buoyant path, so the same wiring holds for both — wire a FINISHED solve: the cross-check tests the inputs, not convergence. ASHRAE 241: Table 5-1's ECAi per person × occupants (×2 for group vocalization, §5.1.3) against the achieved outdoor air + air cleaning (Eq. 6-1; in-duct cleaning = recirculated flow × single-pass efficiency, Eq. 7-1). CAVEATS: quanta emission rates are uncertain by orders of magnitude and depend on activity (breathing, speaking, singing) — compare designs rather than quote absolute risks; Wells–Riley covers long-range airborne transmission only; ASHRAE 241 also requires a building readiness plan and tested equipment, which this check does not cover.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Room Volume | V | Air volume of the room (m³). | `Number` |
| Outdoor Air | OA | The DESIGN outdoor (supply) airflow to the room, in L/s: the ASHRAE 241 achieved ECA and the well-mixed risk. The spatial map's tracer scaling uses Carried Flow instead (the flow the solved case really carried, which snapping makes differ from the design), and falls back to this only when Carried Flow is not wired. Below 0.1 L/s per occupant — a twenty-fifth of ASHRAE 62.1's 2.5 L/s — it is warned as a flow typed in m³/s (0.5 m³/s is 500 L/s). 0 is accepted: ASHRAE 241 lets Air Cleaning supply the whole ECA. | `Number` |
| Air Cleaning | ACS | Equivalent clean airflow from air cleaning (L/s): in-duct filters = recirculated flow × single-pass efficiency (MERV-A 11 or better, ASHRAE 241 §4.2.3), in-room cleaners = tested CADR. | `Number` |
| Space Type | Space | ASHRAE 241-2023 Table 5-1 occupancy category (a bare name such as 'Classroom' also works). | `Text` |
| Occupants | N | People in the breathing zone (ASHRAE 241 P_Z). | `Integer` |
| Group Vocalization | Voc | Singing, chanting or loud group speech: doubles the required ECA (ASHRAE 241 §5.1.3). | `Boolean` |
| Infectors | I | Infectious occupants present. | `Number` |
| Quanta Rate | q | Quanta emitted per infector per hour. ILLUSTRATIVE default — it spans orders of magnitude with activity (Buonanno et al. 2020); set it for the scenario. | `Number` |
| Breathing Rate | p | Inhalation rate of a susceptible (m³/h): 0.49 resting, 0.54 standing, 1.38 light exercise. | `Number` |
| Exposure | t | Exposure duration (h). | `Number` |
| Viral Tracer | C | Probed 'viral' tracer at breathing-zone points (optional — the spatial map). | `Generic Data` |
| Emitter Rate | IR | The Viral Emitter's Injection Rate (SPECIFIC, 1/s — per m³ of its zone). With Emitter Volume it scales the map when no solved Exhaust Tracer and Carried Flow are wired, and cross-checks them when they are. Several Viral Emitters: the cross-check compares Ce × Qc with the SUM r × Vz over all of them — with equal rates give this one rate and, as Emitter Volume, the sum of their zones' volumes (viralSourceVolume_0 + _1 + …). | `Number` |
| Emitter Volume | Vz | The MESHED volume of the Viral Emitter's zone, in m³, as the case writes it: Read Results with Dataset 'viralSourceVolume_0' (postProcessing/viralSourceVolume_0 — one per emitter, numbered like the solver's viralSource_0, whose "selected N cell(s) with volume V" it reproduces), its Values wired here — the LAST value is used. NOT the drawn box's volume: the rate is per m³ of the zone and boxToCell selects cells by centre, so the zone is whatever cells the box caught (the reference room's 1.8 m³ box meshed 1.4496 m³; typed as 1.8 the cross-check reads 0.805). Several Viral Emitters: the sum r × Vz over all of them is what the cross-check needs (see Emitter Rate). | `Number` |
| Exhaust Tracer | Ce | The FLUX-weighted mean of 'viral' in the air leaving the room, as the Indoor case writes it: Read Results with Dataset 'exhaustViral' (postProcessing/exhaustViral), its Values wired here — the LAST value, the final written time, is used (0 there means the case is not solved yet: a Warning). With Carried Flow it scales the map — Ce × Qc is the emission the case measured leaving — and Emitter Rate × Emitter Volume, when given, is checked against it. Not a point probed at the outlet: the exhaust carries the flux-weighted mean (the balance closes at 1.000 with it, 0.983 with the area average). | `Number` |
| Carried Flow | Qc | The flow the case CARRIED out of the room, as a VOLUME flow in m³/s (not a kg/s mass flow: nothing here can tell one from the other, and a mass flow reads about 15 % low): Read Results with Dataset 'exhaustFlow' (postProcessing/exhaustFlow, m³/s on the isothermal and the buoyant path), its Values wired straight in — the LAST value is used. Used ONLY for the spatial map: with the Exhaust Tracer it scales the tracer to quanta (Ce × Qc) and is what the emitter is cross-checked against. Outdoor Air stays the design flow of the ASHRAE 241 check and the well-mixed risk; a Carried Flow outside 0.03–30 × Outdoor Air (snapping and recirculation stay inside it: 5–10 % outdoor air is 10–20 ×) is warned as the L/s ↔ m³/s slip it is. The inlet's supplyFlow (negative, read as its magnitude) works too, but prefer exhaustFlow: on the buoyant path the supply is the colder, denser air and carries a smaller volume than leaves (0.5000 against 0.5008 m³/s at 300 W; about 2 % at a 3 kW heater, estimated). Unwired: Outdoor Air stands in for it, with a Remark. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Probability | P | Well-mixed infection probability per susceptible, from a clean room (%). | `Number` |
| Steady Probability | Pss | Same, with the room at steady state throughout (%) — an upper bound. | `Number` |
| Expected Cases | Cases | Susceptibles (occupants − infectors) × P. | `Number` |
| Point Probability | Pi | Per breathing-zone point, from the viral tracer (%). | `Number` |
| Required ECA | ECAreq | ASHRAE 241 V_ECAi (L/s). | `Number` |
| Achieved ECA | ECA | Outdoor air + air cleaning (L/s). | `Number` |
| ASHRAE 241 Pass | Pass | Achieved ≥ required. | `Boolean` |
| Summary | Sum | Readable summary. | `Text` |
| Infection Risk | Risk | The assessment, for the Ventilation & Comfort Report. | `Generic Data` |