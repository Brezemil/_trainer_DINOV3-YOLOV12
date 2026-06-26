---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.camera.html
---

# fiftyone.core.threed.camera#

Camera definition for 3D visualization.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PerspectiveCamera`([position,Â look_at,Â up,Â ...]) | Represents the configuration of a 3D perspective camera.  
---|---  
  
class fiftyone.core.threed.camera.PerspectiveCamera(_position : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | None = None_, _look_at : [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3") | None = None_, _up : Literal['X', 'Y', 'Z', '-X', '-Y', '-Z'] | None = None_, _aspect : float | None = None_, _fov : float = 50.0_, _near : float = 0.1_, _far : float = 2000.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents the configuration of a 3D perspective camera.

Parameters:
    

  * **position** (_None_) â the position of the camera. If `None`, the camera position is calculated based on the bounding box of the scene

  * **look_at** (_None_) â the point the camera is looking at. If `None`, the camera looks at the center of the scene

  * **up** (_None_) â the orthonormal axis that is considered up. Must be one of âXâ, âYâ, âZâ, â-Xâ, â-Yâ, or â-Zâ. If `None`, it will fallback to the global `up` as defined in 3D plugin settings. If that too is not defined, it will fallback to âZâ

  * **aspect** (_None_) â the aspect ratio of the camera. If `None`, the aspect ratio is calculated based on the width and height of the canvas

  * **fov** (_50_) â camera frustum vertical field of view in degrees. If `None`, the field of view is 50 degrees

  * **near** (_0.1_) â the near clipping plane of the camera

  * **far** (_2000_) â the far clipping plane of the camera




**Attributes:**

`position` |   
---|---  
`look_at` |   
`up` |   
`aspect` |   
`fov` |   
`near` |   
`far` |   
  
**Methods:**

`as_dict`() |   
---|---  
  
property position: [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3")#
    

property look_at: [Vector3](api__fiftyone.core.threed.transformation.md#fiftyone.core.threed.transformation.Vector3 "fiftyone.core.threed.transformation.Vector3")#
    

property up: str | None#
    

property aspect#
    

property fov: float#
    

property near: float#
    

property far: float#
    

as_dict() → dict#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
