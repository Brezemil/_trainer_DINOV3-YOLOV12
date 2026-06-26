---
source_url: https://docs.voxel51.com/api/fiftyone.operators.sse.html
---

# fiftyone.operators.sse#

FiftyOne SSE operators.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SseOperatorConfig`(name,Â label,Â store_name[,Â ...]) |   
---|---  
`SseOperator`([_builtin]) |   
  
class fiftyone.operators.sse.SseOperatorConfig(_name_ , _label_ , _store_name_ , _description =None_, _icon =None_, _light_icon =None_, _dark_icon =None_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

class fiftyone.operators.sse.SseOperator(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

**Attributes:**

`IS_SSE_OPERATOR` |   
---|---  
`subscription_config` |   
`config` | The `OperatorConfig` for the operator.  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`execute`(ctx) | Executes the operator.  
---|---  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
IS_SSE_OPERATOR = True#
    

property subscription_config#
    

property config#
    

The `OperatorConfig` for the operator.

async execute(_ctx : [ExecutionContext](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
