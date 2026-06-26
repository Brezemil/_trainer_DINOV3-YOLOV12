---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.transformation.html
---

# fiftyone.core.threed.transformation#

**Classes:**

`Vector3`([x,Â y,Â z]) | Represents a three-dimensional vector.  
---|---  
`Euler`([x,Â y,Â z,Â degrees,Â sequence]) | Represents intrinsic rotations about the object's own principal axes.  
`Quaternion`([x,Â y,Â z,Â w]) | Represents a quaternion.  
  
**Functions:**

`normalize_to_vec3`(v) |   
---|---  
`coerce_to_vec3`(v) |   
  
class fiftyone.core.threed.transformation.Vector3(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents a three-dimensional vector.

**Attributes:**

`x` |   
---|---  
`y` |   
`z` |   
  
**Methods:**

`to_arr`() | Converts the vector to a numpy array.  
---|---  
  
property x: float#
    

property y: float#
    

property z: float#
    

to_arr()#
    

Converts the vector to a numpy array.

class fiftyone.core.threed.transformation.Euler(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_, _degrees : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _sequence : Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'] = 'XYZ'_)#
    

Bases: `Vector3`

Represents intrinsic rotations about the objectâs own principal axes.

**Attributes:**

`degrees` |   
---|---  
`sequence` |   
`x` |   
`y` |   
`z` |   
  
**Methods:**

`to_quaternion`() | Converts the euler angles to a quaternion.  
---|---  
`to_arr`() | Converts the vector to a numpy array.  
  
property degrees: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

property sequence: Literal['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']#
    

to_quaternion()#
    

Converts the euler angles to a quaternion.

to_arr()#
    

Converts the vector to a numpy array.

property x: float#
    

property y: float#
    

property z: float#
    

class fiftyone.core.threed.transformation.Quaternion(_x : float = 0.0_, _y : float = 0.0_, _z : float = 0.0_, _w : float = 1.0_)#
    

Bases: [`BaseValidatedDataClass`](api__fiftyone.core.threed.validators.md#fiftyone.core.threed.validators.BaseValidatedDataClass "fiftyone.core.threed.validators.BaseValidatedDataClass")

Represents a quaternion.

**Attributes:**

`x` |   
---|---  
`y` |   
`z` |   
`w` |   
  
**Methods:**

`to_euler`([degrees,Â sequence]) | Converts the quaternion into euler angles.  
---|---  
`to_arr`() | Converts the quaternion to a numpy array.  
  
property x: float#
    

property y: float#
    

property z: float#
    

property w: float#
    

to_euler(_degrees =False_, _sequence ='XYZ'_)#
    

Converts the quaternion into euler angles.

to_arr()#
    

Converts the quaternion to a numpy array.

fiftyone.core.threed.transformation.normalize_to_vec3(_v : Vector3 | List[float] | Tuple[float] | array | None_) → Vector3 | None#
    

fiftyone.core.threed.transformation.coerce_to_vec3(_v : Vector3 | List[float] | Tuple[float] | array | None_) → Vector3 | None#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
