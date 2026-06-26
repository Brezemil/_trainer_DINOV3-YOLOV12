---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.typing.html
---

# fiftyone.core.map.typing#

Miscellaneous types

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SampleCollection`(*args,Â **kwargs) | Type for sample collection  
---|---  
  
class fiftyone.core.map.typing.SampleCollection(_* args_, _** kwargs_)#
    

Bases: `Protocol`[`T`]

Type for sample collection

**Methods:**

`iter_samples`() |   
---|---  
`values`() |   
  
iter_samples(_* args_, _** kwargs_) → Iterator[T]#
    

values(_key : Literal['id']_, __enforce_natural_order : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → List[[ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")]#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
