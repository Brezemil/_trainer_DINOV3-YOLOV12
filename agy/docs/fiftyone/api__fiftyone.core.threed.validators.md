---
source_url: https://docs.voxel51.com/api/fiftyone.core.threed.validators.html
---

# fiftyone.core.threed.validators#

Simple validator utilities

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`validate_bool`(v[,Â nullable]) |   
---|---  
`validate_choice`(v,Â options[,Â nullable]) |   
`validate_color`(v[,Â nullable]) |   
`validate_float`(v[,Â nullable]) |   
`validate_list`(v[,Â length,Â nullable]) |   
  
**Classes:**

`BaseValidatedDataClass`() |   
---|---  
  
fiftyone.core.threed.validators.validate_bool(_v : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

fiftyone.core.threed.validators.validate_choice(_v : Any_, _options : frozenset_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

fiftyone.core.threed.validators.validate_color(_v : str | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

fiftyone.core.threed.validators.validate_float(_v : float | None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

fiftyone.core.threed.validators.validate_list(_v : Any_, _length : int | None = None_, _nullable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")#
    

class fiftyone.core.threed.validators.BaseValidatedDataClass#
    

Bases: `object`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
