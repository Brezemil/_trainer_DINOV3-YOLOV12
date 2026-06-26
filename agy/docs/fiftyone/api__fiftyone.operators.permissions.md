---
source_url: https://docs.voxel51.com/api/fiftyone.operators.permissions.html
---

# fiftyone.operators.permissions#

FiftyOne operator permissions.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ManagedOperators`([managed_operators]) |   
---|---  
`PermissionedOperatorRegistry`(managed_operators) |   
  
class fiftyone.operators.permissions.ManagedOperators(_managed_operators =None_)#
    

Bases: `object`

**Methods:**

`has_operator`(operator_uri) |   
---|---  
`for_request`(request[,Â dataset_ids]) |   
  
has_operator(_operator_uri_)#
    

async classmethod for_request(_request_ , _dataset_ids =None_)#
    

class fiftyone.operators.permissions.PermissionedOperatorRegistry(_managed_operators_)#
    

Bases: [`OperatorRegistry`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry "fiftyone.operators.registry.OperatorRegistry")

**Methods:**

`can_execute`(operator_uri) | Whether the operator can be executed.  
---|---  
`from_list_request`(request[,Â dataset_ids]) |   
`from_exec_request`(request[,Â dataset_ids]) |   
`get_operator`(operator_uri) | Retrieves an operator by its URI.  
`list_errors`() | Lists the errors that occurred during operator loading.  
`list_operators`([builtin,Â type]) | Lists the available FiftyOne operators.  
`operator_exists`(operator_uri) | Checks if the operator exists.  
  
can_execute(_operator_uri_)#
    

Whether the operator can be executed.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

async classmethod from_list_request(_request_ , _dataset_ids =None_)#
    

async classmethod from_exec_request(_request_ , _dataset_ids =None_)#
    

get_operator(_operator_uri_)#
    

Retrieves an operator by its URI.

Parameters:
    

**operator_uri** â the URI of an operator

Returns:
    

an [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator"), or None

list_errors()#
    

Lists the errors that occurred during operator loading.

Returns:
    

a list of errors

list_operators(_builtin =None_, _type =None_)#
    

Lists the available FiftyOne operators.

Parameters:
    

  * **builtin** (_None_) â whether to include only builtin operators (True) or only non-builtin operators (False)

  * **type** (_None_) â whether to include only `"panel"` or `"operator"` type operators, or a specific [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") subclass to restrict to



Returns:
    

a list of [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") instances

operator_exists(_operator_uri_)#
    

Checks if the operator exists.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
