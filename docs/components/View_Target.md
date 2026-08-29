# ![](/images/icons/View_Target.png) View Target - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22View%20Target%22)

![](/images/components/View_Target-crop.png)

Fraction of a target's surface each observer point can see — which seats see the park, which units see the water. The target is sampled by area; rays are blocked by the context and by the target's own body.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Obstructing geometry between the observers and the target. Branches are flattened into one scene. The target itself must NOT be wired here. Optional — with nothing wired, only the target's own body occludes (a pure massing/self-occlusion study). | `Geometry` |
| Points | P | Observer points. | `Point` |
| Target | T | The geometry whose visibility is being rated. Branches are flattened into one target; it occludes itself, so a solid target's far side reads as hidden. | `Geometry` |
| Target Samples | S | Points the target is reduced to, allocated by area. More samples resolve partial views more finely; cost is linear per observer. | `Integer` |
| Offset | O | Clearance around ray endpoints, so observers and samples sitting ON geometry do not block themselves. | `Number` |
| Max Distance | D | Optional cap in metres — target samples farther than this count as not visible. | `Number` |
| Color Scheme | Ramp | Colour ramp for the Colors output. Viridis is perceptually uniform and colourblind-safe (use it in a figure); Grayscale suits a monochrome print. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Visibility | V | Fraction of the target's samples each observer can see, 0-1. | `Number` |
| Colors | Col | Point-specific colour ramp over visibility, for a mesh or point preview. | `Colour` |
| Target Points | TP | The area-weighted sample points the target was reduced to — preview these to judge whether Target Samples is enough. | `Point` |
| Report | R | Rays traced, samples, and elapsed time. | `Text` |