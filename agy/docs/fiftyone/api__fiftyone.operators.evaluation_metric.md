---
source_url: https://docs.voxel51.com/api/fiftyone.operators.evaluation_metric.html
---

# fiftyone.operators.evaluation_metric#

Evaluation metric operators.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`EvaluationMetricConfig`(name[,Â label,Â ...]) | Configuration class for evaluation metrics.  
---|---  
`EvaluationMetric`([_builtin]) | Base class for evaluation metric operators.  
  
class fiftyone.operators.evaluation_metric.EvaluationMetricConfig(_name_ , _label =None_, _description =None_, _eval_types =None_, _aggregate_key =None_, _lower_is_better =True_, _** kwargs_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

Configuration class for evaluation metrics.

Parameters:
    

  * **name** â the name of the evaluation metric

  * **label** ([_name_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.name "fiftyone.core.session.events.Colorscale.name")) â a label for the evaluation metric

  * **description** (_None_) â a description of the evaluation metric

  * **eval_types** (_None_) â an optional list of evaluation method types that this metric supports

  * **aggregate_key** (_None_) â an optional key under which to store the metricâs aggregate value. This is used, for example, by [`metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.metrics "fiftyone.utils.eval.base.BaseEvaluationResults.metrics"). By default, the metricâs `name` is used as its key

  * **lower_is_better** (_True_) â whether lower values of the metric are better

  * ****kwargs** â other kwargs for [`fiftyone.operators.OperatorConfig`](api__fiftyone.operators.md#fiftyone.operators.OperatorConfig "fiftyone.operators.OperatorConfig")




**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

class fiftyone.operators.evaluation_metric.EvaluationMetric(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

Base class for evaluation metric operators.

**Methods:**

`resolve_input`(ctx) | Defines any necessary properties to collect this evaluation metric's parameters from a user during prompting.  
---|---  
`parse_parameters`(ctx,Â params) | Performs any necessary execution-time formatting to this evaluation metric's parameters.  
`compute`(samples,Â results,Â **kwargs) | Computes the evaluation metric for the given collection.  
`get_fields`(samples,Â config,Â eval_key) | Lists the fields that were populated by the evaluation metric with the given key, if any.  
`rename`(samples,Â config,Â eval_key,Â new_eval_key) | Performs any necessary operations required to rename this evaluation metric's key.  
`cleanup`(samples,Â config,Â eval_key) | Cleans up the results of the evaluation metric with the given key from the collection.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Executes the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
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
  
resolve_input(_ctx_)#
    

Defines any necessary properties to collect this evaluation metricâs parameters from a user during prompting.

Parameters:
    

**ctx** â an [`fiftyone.operators.ExecutionContext`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext "fiftyone.operators.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

parse_parameters(_ctx_ , _params_)#
    

Performs any necessary execution-time formatting to this evaluation metricâs parameters.

Parameters:
    

  * **ctx** â an [`fiftyone.operators.ExecutionContext`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext "fiftyone.operators.ExecutionContext")

  * **params** â a params dict




compute(_samples_ , _results_ , _** kwargs_)#
    

Computes the evaluation metric for the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **results** â an [`fiftyone.core.evaluation.EvaluationResults`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationResults "fiftyone.core.evaluation.EvaluationResults")

  * ****kwargs** â arbitrary metric-specific parameters



Returns:
    

an optional aggregate metric value to store on the results

get_fields(_samples_ , _config_ , _eval_key_)#
    

Lists the fields that were populated by the evaluation metric with the given key, if any.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key



Returns:
    

a list of fields

rename(_samples_ , _config_ , _eval_key_ , _new_eval_key_)#
    

Performs any necessary operations required to rename this evaluation metricâs key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key

  * **new_eval_key** â a new evaluation key




cleanup(_samples_ , _config_ , _eval_key_)#
    

Cleans up the results of the evaluation metric with the given key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key




add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

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
