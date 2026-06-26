---
source_url: https://docs.voxel51.com/plugins/api/plugins.panels.model_evaluation.html
---

# plugins.panels.model_evaluation#

  * [plugins.panels.model_evaluation.utils](plugins__api__plugins.panels.model_evaluation.utils.md)
    * [`compress_confusion_matrix()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.compress_confusion_matrix)
    * [`decompress_confusion_matrix()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.decompress_confusion_matrix)
    * [`compress_and_serialize()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.compress_and_serialize)
    * [`decompress_and_deserialize()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.decompress_and_deserialize)
    * [`compress_and_serialize_scenario()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.compress_and_serialize_scenario)
    * [`decompress_and_deserialize_scenario()`](plugins__api__plugins.panels.model_evaluation.utils.md#plugins.panels.model_evaluation.utils.decompress_and_deserialize_scenario)



## Module contents#

Model evaluation panel.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`EvaluationPanel`([_builtin]) |   
---|---  
  
class plugins.panels.model_evaluation.EvaluationPanel(__builtin =False_)#
    

Bases: [`Panel`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel "fiftyone.operators.panel.Panel")

**Attributes:**

`config` | The `OperatorConfig` for the operator.  
---|---  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`get_dataset`(ctx) |   
---|---  
`get_evaluation_id`(dataset,Â eval_key) |   
`get_evaluation_type`(config) |   
`get_permissions`(ctx) |   
`can_evaluate`(ctx) |   
`can_edit_note`(ctx) |   
`can_edit_status`(ctx) |   
`can_delete_evaluation`(ctx) |   
`can_rename`(ctx) |   
`can_delete_scenario`(ctx) |   
`can_edit_scenario`(ctx) |   
`on_load`(ctx) |   
`get_confidences`(per_class_metrics) |   
`get_avg_confidence`(confidences) |   
`get_confidence_distribution`(confidences) |   
`get_avg_iou`(per_class_metrics) |   
`get_tp_fp_fn`(info,Â results) |   
`get_map`(results) |   
`get_mar`(results) |   
`get_custom_metrics`(results) |   
`set_status`(ctx) |   
`set_note`(ctx) |   
`rename_evaluation`(ctx) |   
`delete_evaluation`(ctx) |   
`load_evaluation_view`(ctx) |   
`compute_avg_confs`(results) |   
`compute_avg_ious`(results) |   
`get_per_class_metrics`(info,Â results) |   
`get_confusion_matrix_colorscale`(matrix,Â ...) |   
`get_confusion_matrix`(results) |   
`get_correct_incorrect`(results) |   
`get_scenario`(ctx,Â scenario_id) |   
`load_scenarios`(ctx) |   
`get_evaluation_data`(ctx) |   
`get_evaluation_data_cache_key_fn`(ctx) |   
`get_evaluation_data_cacheable`(ctx) |   
`load_evaluation`(ctx) |   
`on_change_view`(ctx) |   
`has_evaluation_results`(dataset,Â eval_key) |   
`load_pending_evaluations`(ctx[,Â skip_update]) |   
`on_evaluate_model_success`(ctx) |   
`on_evaluate_model`(ctx) |   
`load_view`(ctx) |   
`load_compare_evaluation_results`(ctx) |   
`get_subset_def_data`(info,Â results,Â ...) |   
`get_scenario_data`(ctx,Â scenario) |   
`get_subset_def_data_for_eval_key`(ctx,Â scenario) | Builds and returns an execution cache key for each type of scenario.  
`get_scenario_data_cacheable`(ctx,Â scenario) |   
`validate_scenario_subsets`(ctx,Â scenario) | Validates the subsets in a scenario and compiles basic changes. 1. For view scenarios, check if the views exist in the dataset. 2. For sample_field and label_attribute scenarios, check if the field exists in the dataset. - If the field is tags, check if the tags exist.  
`load_scenario`(ctx) | Tries to load the scenario given its id and evaluation key If it fails, it shows an error page with options to edit/delete.  
`delete_scenario`(ctx) |   
`render`(ctx) | Defines the panel's layout and events.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Executes the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`on_startup`(ctx) |   
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
property config#
    

The `OperatorConfig` for the operator.

get_dataset(_ctx_)#
    

get_evaluation_id(_dataset_ , _eval_key_)#
    

get_evaluation_type(_config_)#
    

get_permissions(_ctx_)#
    

can_evaluate(_ctx_)#
    

can_edit_note(_ctx_)#
    

can_edit_status(_ctx_)#
    

can_delete_evaluation(_ctx_)#
    

can_rename(_ctx_)#
    

can_delete_scenario(_ctx_)#
    

can_edit_scenario(_ctx_)#
    

on_load(_ctx_)#
    

get_confidences(_per_class_metrics_)#
    

get_avg_confidence(_confidences_)#
    

get_confidence_distribution(_confidences_)#
    

get_avg_iou(_per_class_metrics_)#
    

get_tp_fp_fn(_info_ , _results_)#
    

get_map(_results_)#
    

get_mar(_results_)#
    

get_custom_metrics(_results_)#
    

set_status(_ctx_)#
    

set_note(_ctx_)#
    

rename_evaluation(_ctx_)#
    

delete_evaluation(_ctx_)#
    

load_evaluation_view(_ctx_)#
    

compute_avg_confs(_results_)#
    

compute_avg_ious(_results_)#
    

get_per_class_metrics(_info_ , _results_)#
    

get_confusion_matrix_colorscale(_matrix_ , _colorscale_name_ , _*_ , _logarithmic =False_)#
    

get_confusion_matrix(_results_)#
    

get_correct_incorrect(_results_)#
    

get_scenario(_ctx_ , _scenario_id_)#
    

load_scenarios(_ctx_)#
    

get_evaluation_data(_ctx_)#
    

get_evaluation_data_cache_key_fn(_ctx_)#
    

get_evaluation_data_cacheable(_ctx_)#
    

load_evaluation(_ctx_)#
    

on_change_view(_ctx_)#
    

has_evaluation_results(_dataset_ , _eval_key_)#
    

load_pending_evaluations(_ctx_ , _skip_update =False_)#
    

on_evaluate_model_success(_ctx_)#
    

on_evaluate_model(_ctx_)#
    

load_view(_ctx_)#
    

load_compare_evaluation_results(_ctx_)#
    

get_subset_def_data(_info_ , _results_ , _subset_def_ , _is_compare_)#
    

get_scenario_data(_ctx_ , _scenario_)#
    

get_subset_def_data_for_eval_key(_ctx_ , _scenario_)#
    

Builds and returns an execution cache key for each type of scenario.

get_scenario_data_cacheable(_ctx_ , _scenario_)#
    

validate_scenario_subsets(_ctx_ , _scenario_)#
    

Validates the subsets in a scenario and compiles basic changes. 1\. For view scenarios, check if the views exist in the dataset. 2\. For sample_field and label_attribute scenarios, check if the field exists in the dataset.

>   * If the field is tags, check if the tags exist.
> 
> 


returns the validated scenario and a list of changes. If the scenario is not valid, it will return an empty list of subsets. If the scenario is valid, it will return the original scenario with the validated subsets.

load_scenario(_ctx_)#
    

Tries to load the scenario given its id and evaluation key If it fails, it shows an error page with options to edit/delete.

delete_scenario(_ctx_)#
    

render(_ctx_)#
    

Defines the panelâs layout and events.

This method is called after every panel event is called (on load, button callback, context change event, etc).

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

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
    

on_startup(_ctx_)#
    

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
