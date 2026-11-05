# ![](/images/icons/Shadow_Animation.png) Shadow Animation - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Shadow%20Animation%22)

![](/images/components/Shadow_Animation-crop.png)

Play a daily shadow study: the day is traced once between sunrise and sunset, then Play / Time / Speed step through it. Up to eight named time ranges colour the shade and get their own statistics; Export writes the active viewport as PNG frames (and an MP4 when ffmpeg is on PATH).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Shading geometry: buildings, terrain, canopies. | `Geometry` |
| Points | P | Analysis points. | `Point` |
| Weather | W | Weather record from Download Weather or Open Weather — its site sets the sun and its time zone the clock (standard time, no daylight saving). | `Generic Data` |
| Month | Mon | Month of the study date, 1-12. | `Integer` |
| Day |  | Day of the month of the study date. | `Integer` |
| Hours | Hrs | Local hours to animate, e.g. 8 To 18. Always clamped to the date's sunrise and sunset, so the default 0 To 24 is the whole day. | `Domain` |
| Step |  | Minutes between frames, at least 1. | `Number` |
| Ranges | Rng | Up to eight named time ranges, one per line: "Morning 7-11", "Lunch 11:30-13:15". They may overlap (the earlier line colours the shared frames; statistics count them in both) or leave gaps (shade there keeps the plain shade colour). | `Text` |
| Range Colors | RCol | One colour per range, in order. Missing colours come from a built-in palette. | `Colour` |
| Offset | O | Distance to lift each point off its surface before tracing. | `Number` |
| North | Nth | Counter-clockwise degrees from the model's +Y axis to true north. | `Number` |
| Speed | Spd | Playback speed in frames per second (0.1-20); also the MP4's frame rate. | `Number` |
| Time | T | Scrub: a local hour (e.g. 14.5) jumps to the nearest frame whenever this value changes. Wire a slider over the Hours range. | `Number` |
| Play |  | Advance one frame per tick while on; off pauses on the current frame. | `Boolean` |
| Folder | Dir | Folder Export writes frame_0000.png … (and shadow_animation.mp4) into. | `Text` |
| Engine | Eng | Who traces the rays. Auto: the OpenCL GPU when there is one, else the CPU. GPU: the OpenCL GPU; a fallback to the CPU is reported, never silent. CPU: the SIMD BVH on every core. | `Text` |
| Export | Exp | Capture the active viewport at every frame. Edge-triggered: a click, or a wired value turning true, exports once. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Time | T | Local hour of the frame shown. | `Number` |
| Lit | L | Lit or shaded at each point, this frame. | `Boolean` |
| Colors | Col | This frame: sunlit yellow; shaded points take the colour of the range the frame falls in, or the plain shade blue in a gap. | `Colour` |
| Sunlit Points | SP | Just the lit points, this frame. | `Point` |
| Range Shade | RS | Per range (one branch each, in range order), each point's share of that range's frames spent in shade, 0-1. Empty branch for a range no frame falls in. | `Number` |
| Legend | Leg | Legend labels matching Legend Colors: each range with its daylight-clamped hours, then plain shade and sunlit. | `Text` |
| Legend Colors | LCol | Colours for Legend. | `Colour` |
| Report | R | Daylight window, frames, per-range statistics and the last export's result. | `Text` |