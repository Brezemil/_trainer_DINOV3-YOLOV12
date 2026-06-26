---
source_url: https://docs.voxel51.com/api/fiftyone.factory.repos.delegated_operation_doc.html
---

# fiftyone.factory.repos.delegated_operation_doc#

FiftyOne delegated operation repository document.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DelegatedOperationDocument`([operator,Â ...]) |   
---|---  
  
class fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument(_operator : str = None_, _delegation_target : str = None_, _context : [ExecutionContext](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") = None_, _is_remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _rerunnable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_)#
    

Bases: `object`

**Attributes:**

`num_distributed_tasks` | Returns the number of distributed tasks in this operation, if any.  
---|---  
  
**Methods:**

`from_pymongo`(doc) |   
---|---  
`to_pymongo`() |   
  
property num_distributed_tasks#
    

Returns the number of distributed tasks in this operation, if any.

from_pymongo(_doc : dict_)#
    

to_pymongo() → dict#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
