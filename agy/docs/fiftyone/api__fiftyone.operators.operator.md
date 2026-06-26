---
source_url: https://docs.voxel51.com/api/fiftyone.operators.operator.html
---

# fiftyone.operators.operator#

FiftyOne operators.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`OperatorConfig`(name[,Â label,Â description,Â ...]) | A configuration for an operator.  
---|---  
`Operator`([_builtin]) | A FiftyOne operator.  
`PipelineOperator`([_builtin]) | A FiftyOne pipeline operator.  
  
class fiftyone.operators.operator.OperatorConfig(_name_ , _label =None_, _description =None_, _dynamic =False_, _execute_as_generator =False_, _unlisted =False_, _on_startup =False_, _on_dataset_open =False_, _disable_schema_validation =False_, _delegation_target =None_, _icon =None_, _light_icon =None_, _dark_icon =None_, _allow_immediate_execution =True_, _allow_delegated_execution =False_, _default_choice_to_delegated =False_, _resolve_execution_options_on_change =None_, _allow_distributed_execution =False_, _rerunnable =True_, _risk_level =RiskLevel.DANGEROUS_, _** kwargs_)#
    

Bases: `object`

A configuration for an operator.

Parameters:
    

  * **name** â the name of the operator

  * **label** ([_name_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.name "fiftyone.core.session.events.Colorscale.name")) â a label for the operator

  * **description** (_None_) â a description of the operator

  * **dynamic** (_False_) â whether the operator inputs and outputs should be resolved when the input/output changes

  * **execute_as_generator** (_False_) â whether the operator should be executed as a generator

  * **unlisted** (_False_) â whether the operator should be hidden from the Operator Browser

  * **on_startup** (_False_) â whether the operator should be executed on startup

  * **on_dataset_open** (_False_) â whether the operator should be executed on opening a dataset

  * **disable_schema_validation** (_False_) â whether the operator built-in schema validation should be disabled

  * **icon** (_None_) â icon to show for the operator in the Operator Browser

  * **light_icon** (_None_) â icon to show for the operator in the Operator Browser when the App is in the light mode

  * **dark_icon** (_None_) â icon to show for the operator in the Operator Browser when the App is in the dark mode

  * **allow_immediate_execution** (_True_) â whether the operator should allow immediate execution

  * **allow_delegated_execution** (_False_) â whether the operator should allow delegated execution

  * **default_choice_to_delegated** (_False_) â whether to default to delegated execution, if allowed

  * **resolve_execution_options_on_change** (_None_) â whether to resolve execution options dynamically when inputs change. By default, this behavior will match the `dynamic` setting

  * **allow_distributed_execution** (_False_) â whether the operator supports distributing delegated execution across parallel workers.

  * **rerunnable** (_True_) â whether the operator can be re-run

  * **risk_level** ([_RiskLevel.DANGEROUS_](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.DANGEROUS "fiftyone.operators.types.RiskLevel.DANGEROUS")) â the declared `RiskLevel` for this operator is mainly used by guardrail systems of an agent to classify tool calls. If `None`, the operator defaults to `RiskLevel.DANGEROUS`




**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

class fiftyone.operators.operator.Operator(__builtin =False_)#
    

Bases: `object`

A FiftyOne operator.

Operators represent an operation and the details of how to execute it.

FiftyOne operators contain enough information for a user interface to render a form or button allowing a user to execute the operation.

**Attributes:**

`name` |   
---|---  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
`builtin` | Whether the operator is builtin.  
`config` | The `OperatorConfig` for the operator.  
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
  
**Methods:**

`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
---|---  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`execute`(ctx) | Executes the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`to_json`() | Returns a JSON representation of the operator.  
`add_secrets`(secrets) | Adds secrets to the operator.  
  
property name#
    

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

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

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

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

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

class fiftyone.operators.operator.PipelineOperator(__builtin =False_)#
    

Bases: `Operator`

A FiftyOne pipeline operator.

A pipeline operator represents a linear composition of other operators, containing the details of how to create and execute the [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline")

FiftyOne pipeline operators contain enough information for a user interface to render a form or button allowing a user to execute the operation.

**Methods:**

`resolve_pipeline`(ctx) | Returns the resolved pipeline of the operator.  
---|---  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Not used for pipeline operators; pipelines are executed via stages  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
**Attributes:**

`builtin` | Whether the operator is builtin.  
---|---  
`config` | The `OperatorConfig` for the operator.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
resolve_pipeline(_ctx_)#
    

Returns the resolved pipeline of the operator.

Subclasses can implement this method to define the pipeline of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline"),

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

execute(_ctx_)#
    

Not used for pipeline operators; pipelines are executed via stages

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
