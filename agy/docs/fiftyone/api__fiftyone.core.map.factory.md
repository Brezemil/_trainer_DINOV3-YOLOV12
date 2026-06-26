---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.factory.html
---

# fiftyone.core.map.factory#

Factory for mapping backends.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`MapperFactory`() | Manage mapper implementations  
---|---  
  
class fiftyone.core.map.factory.MapperFactory#
    

Bases: `object`

Manage mapper implementations

**Methods:**

`batch_methods`() | Get available batch methods  
---|---  
`mapper_keys`() | Get available mapper class keys  
`create`([mapper_key,Â num_workers,Â ...]) | Create a mapper instance  
  
classmethod batch_methods() → List[str]#
    

Get available batch methods

classmethod mapper_keys() → List[str]#
    

Get available mapper class keys

classmethod create(_mapper_key : str | None = None_, _num_workers : int | None = None_, _batch_method : str | None = None_, _batch_size : int | None = None_, _** mapper_extra_kwargs_) → [Mapper](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper "fiftyone.core.map.mapper.Mapper")#
    

Create a mapper instance

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
