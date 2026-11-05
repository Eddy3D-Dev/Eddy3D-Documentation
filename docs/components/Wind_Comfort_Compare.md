# ![](/images/icons/Wind_Comfort_Compare.png) Wind Comfort Compare - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Comfort%20Compare%22)

![](/images/components/Wind_Comfort_Compare-crop.png)

Compares pedestrian wind comfort between schemes — existing (baseline), proposed and optionally mitigated — at the same probe points: per-probe class transition, change in exceedance hours, suitability for the intended use, the City of London significance grade (on-site / off-site receptor tables: negligible, moderate or major, beneficial or adverse, and whether mitigation is required), Wellington WIND-S2 (no increase in hours at or above 2.5 m/s against the existing scheme), and count- or area-weighted summaries. Probes are matched by position; the Comparison output feeds Study Report.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Existing | Ex | Baseline scheme's annual Wind Speed field (Velocity Amplification Factors) — the existing site the others are compared against. | `Generic Data` |
| Proposed | Pr | Proposed scheme's annual Wind Speed field, at the same probe points. | `Generic Data` |
| Mitigated | Mi | Optional mitigated scheme's annual Wind Speed field. When wired, the significance and suitability outputs grade the mitigated scheme against the existing one. | `Generic Data` |
| Comfort Metric | Metric | Comfort criterion — the Pedestrian Wind Comfort vocabulary; City Lawson (CoL 2019) by default, whose significance tables the grading follows. | `Text` |
| Criteria |  | Optional Wind Comfort Criteria object; replaces the Comfort Metric pick. | `Generic Data` |
| Intended Use | Use | Optional intended pedestrian use — one for every probe or one per existing probe. A named use of the criterion (City Lawson: frequent sitting, occasional sitting, standing / entrance / bus stop, walking / pavement, service, cyclist), or a class letter ('C' = at most class C). Needed for suitability and most significance grades. | `Text` |
| Receptor | Rec | Optional 'on-site' or 'off-site' (default) — one for every probe or one per existing probe. On-site receptors are graded against the intended use only; off-site against the existing scheme too (City of London Wind Microclimate Guidelines 2019). | `Text` |
| Weights | Area | Optional area per existing probe — makes the summaries area-weighted instead of counting probes. | `Number` |
| Existing Gust | ExG | Optional Gust Speed field of the existing scheme (VAF, needs TKE). Without it gust-derived classes use mean × Gust Factor. | `Generic Data` |
| Proposed Gust | PrG | Optional Gust Speed field of the proposed scheme. | `Generic Data` |
| Mitigated Gust | MiG | Optional Gust Speed field of the mitigated scheme. | `Generic Data` |
| Gust Factor | G | 3-second gust / hourly mean ratio used where no gust field is wired (default 1.85). | `Number` |
| Match Tolerance | Tol | Distance (model units) within which a probe of one scheme is the same receptor as a probe of the existing scheme. Identical point lists match by index; otherwise the nearest point within this distance, and probes with none are left out and counted. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Class Change | dC | Per existing probe: compared class number minus existing class number (+ = windier by that many classes, 0 = same, - = calmer). 0 for probes left out. | `Integer` |
| Transition | T | Per probe, e.g. 'B → D (+2)'; empty for probes left out. | `Text` |
| Delta Hours | dH | Per probe: change in hours above the threshold of the intended use's class (the criterion's most lenient comfortable class when no use is given). | `Integer` |
| Suitable | OK | Per probe: whether the compared scheme is suitable for the intended use (safe and no windier than the use allows); false where no use was given. | `Boolean` |
| Significance | Sig | Per probe: City of London significance — Major/Moderate Beneficial, Negligible, Moderate/Major Adverse, or 'Not covered' / 'Not graded' where the tables say nothing. | `Text` |
| Mitigation Required | Mit | Per probe: the City of London tables require mitigation (on-site Moderate/Major Adverse, off-site Major Adverse). | `Boolean` |
| WIND-S2 | S2 | Per probe: Wellington WIND-S2 — the compared scheme does not increase the hours with hourly mean at or above 2.5 m/s against the existing one. | `Boolean` |
| Change Colors | CC | Per probe colour of the class change: greens calmer, grey unchanged, oranges to reds windier, dark red for a newly unsafe probe; light grey for probes left out. | `Colour` |
| Significance Colors | SC | Per probe colour of the significance grade. | `Colour` |
| Summary | Sum | Count- or area-weighted summary lines. | `Text` |
| Comparison | Cmp | The comparison object — wire it into Study Report. | `Generic Data` |