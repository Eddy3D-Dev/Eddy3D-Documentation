# ![](/images/icons/Planting_Suitability.png) Planting Suitability - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Planting%20Suitability%22)

![](/images/components/Planting_Suitability-crop.png)

Nursery-label planting suitability from a Sun Hours study: Sunny (6 h or more of direct sun a day), Part sun (4-6 h), Partial shade (2-4 h) or Shade (under 2 h) per point, flagged morning sun or afternoon sun when more than 70 % of it falls on one side of solar noon. Thresholds are editable: there is no accredited standard and some extension services draw the shade edge at 4 h. Method: Grenfell (2025), UC Master Gardeners of Placer County, University of California Agriculture and Natural Resources, https://ucanr.edu/site/uc-master-gardeners-placer-county/article/definitions-light-requirements.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Morning Hours | AM | Direct-sun hours before solar noon at each point — Sun Hours' Morning Hours output. | `Number` |
| Afternoon Hours | PM | Direct-sun hours after solar noon at each point — Sun Hours' Afternoon Hours output. | `Number` |
| Sunny Hours | Sun | Direct sun at or above this is Sunny (full sun). | `Number` |
| Part Sun Hours | Part | At or above this, below Sunny Hours: Part sun. | `Number` |
| Partial Shade Hours | PShade | At or above this, below Part Sun Hours: Partial shade. Below it: Shade. | `Number` |
| Lopsided Fraction | Lop | Share of a point's direct sun that must fall on one side of solar noon before it is flagged morning sun or afternoon sun (strictly more than this; 0.5-1). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Category | Cat | Per point: Sunny, Part sun, Partial shade or Shade, with ' · morning sun' or ' · afternoon sun' appended when the split is lopsided. | `Text` |
| Colors | Col | One colour per point by category — amber, yellow, leaf green, deep green from sun to shade — for a mesh or point preview. | `Colour` |
| Legend | L | One line per band with the thresholds in use, plus the timing rule. | `Text` |
| Summary | S | Points per category and per timing. | `Text` |