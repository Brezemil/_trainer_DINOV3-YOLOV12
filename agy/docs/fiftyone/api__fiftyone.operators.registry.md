---
source_url: https://docs.voxel51.com/api/fiftyone.operators.registry.html
---

# fiftyone.operators.registry#

FiftyOne operator registry.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_operator`(operator_uri[,Â enabled]) | Gets the operator with the given URI.  
---|---  
`list_operators`([enabled,Â builtin,Â type]) | Returns all available operators.  
`operator_exists`(operator_uri[,Â enabled]) | Checks if the given operator exists.  
  
**Classes:**

`OperatorRegistry`([enabled]) | Operator registry.  
---|---  
  
fiftyone.operators.registry.get_operator(_operator_uri_ , _enabled =True_)#
    

Gets the operator with the given URI.

Parameters:
    

  * **operator_uri** â the operator URI

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)



Returns:
    

an [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator")

Raises:
    

**ValueError** â if the operator is not found

fiftyone.operators.registry.list_operators(_enabled =True_, _builtin ='all'_, _type =None_)#
    

Returns all available operators.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)

  * **builtin** (_"all"_) â whether to include only builtin operators (True) or only non-builtin operators (False) or all operators (âallâ)

  * **type** (_None_) â whether to include only `"panel"` or `"operator"` type operators, or a specific [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") subclass to restrict to



Returns:
    

a list of [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") instances

fiftyone.operators.registry.operator_exists(_operator_uri_ , _enabled =True_)#
    

Checks if the given operator exists.

Parameters:
    

  * **operator_uri** â the operator URI

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)



Returns:
    

True/False

class fiftyone.operators.registry.OperatorRegistry(_enabled =True_)#
    

Bases: `object`

Operator registry.

enabled (True): whether to include only enabled operators (True) or
    

only disabled operators (False) or all operators (âallâ)

**Methods:**

`list_operators`([builtin,Â type]) | Lists the available FiftyOne operators.  
---|---  
`list_errors`() | Lists the errors that occurred during operator loading.  
`operator_exists`(operator_uri) | Checks if the operator exists.  
`can_execute`(operator_uri) | Whether the operator can be executed.  
`get_operator`(operator_uri) | Retrieves an operator by its URI.  
  
list_operators(_builtin =None_, _type =None_)#
    

Lists the available FiftyOne operators.

Parameters:
    

  * **builtin** (_None_) â whether to include only builtin operators (True) or only non-builtin operators (False)

  * **type** (_None_) â whether to include only `"panel"` or `"operator"` type operators, or a specific [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") subclass to restrict to



Returns:
    

a list of [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator") instances

list_errors()#
    

Lists the errors that occurred during operator loading.

Returns:
    

a list of errors

operator_exists(_operator_uri_)#
    

Checks if the operator exists.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

can_execute(_operator_uri_)#
    

Whether the operator can be executed.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

get_operator(_operator_uri_)#
    

Retrieves an operator by its URI.

Parameters:
    

**operator_uri** â the URI of an operator

Returns:
    

an [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator"), or None

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
