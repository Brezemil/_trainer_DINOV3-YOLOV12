---
source_url: https://docs.voxel51.com/api/fiftyone.operators.executor.html
---

# fiftyone.operators.executor#

FiftyOne operator execution.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ExecutionRunState`() | Enumeration of the available operator run states.  
---|---  
`InvocationRequest`(operator_uri[,Â params]) | Represents a request to invoke an operator.  
`ExecutionProgress`([progress,Â label]) | Represents the status of an operator execution.  
`Executor`([requests,Â logs]) | Handles the execution phase of the operator lifecycle.  
`ExecutionContext`([request_params,Â executor,Â ...]) | Represents the execution context of an operator.  
`ExecutionResult`([result,Â executor,Â error,Â ...]) | Represents the result of an operator execution.  
`PipelineExecutionContext`(active,Â ...[,Â ...]) | Represents the execution context of a pipeline.  
`ValidationError`(reason,Â property,Â path[,Â custom]) | A validation error.  
`ValidationContext`(ctx,Â inputs_property,Â operator) | Represents the validation context of an operator.  
`ExecutionOptions`([...]) | Represents the execution options of an operation.  
  
**Functions:**

`execute_operator`(operator_uri[,Â ctx]) | Executes the operator with the given name.  
---|---  
`execute_or_delegate_operator`(operator_uri,Â ...) | Executes the operator with the given name.  
`prepare_operator_executor`(operator_uri,Â ...) |   
`do_execute_operator`(operator,Â ctx[,Â exhaust]) |   
`do_execute_pipeline`(pipeline,Â ctx) | Executes the given pipeline in sequence.  
`resolve_type`(registry,Â operator_uri,Â ...) | Resolves the inputs property type of the operator with the given name.  
`resolve_type_with_context`(operator,Â context) | Resolves the "inputs" or "outputs" schema of an operator with the given context.  
`resolve_execution_options`(registry,Â ...) | Resolves the execution options of the operator with the given name.  
`resolve_placement`(operator,Â request_params) | Resolves the placement of the operator with the given name.  
  
**Exceptions:**

`ExecutionError` | An error that occurs while executing an operator.  
---|---  
  
class fiftyone.operators.executor.ExecutionRunState#
    

Bases: `object`

Enumeration of the available operator run states.

**Attributes:**

`SCHEDULED` |   
---|---  
`QUEUED` |   
`RUNNING` |   
`PROCESSING` |   
`COMPLETED` |   
`FAILED` |   
`TERMINAL_STATES` |   
  
SCHEDULED = 'scheduled'#
    

QUEUED = 'queued'#
    

RUNNING = 'running'#
    

PROCESSING = 'processing'#
    

COMPLETED = 'completed'#
    

FAILED = 'failed'#
    

TERMINAL_STATES = {'completed', 'failed'}#
    

class fiftyone.operators.executor.InvocationRequest(_operator_uri_ , _params =None_)#
    

Bases: `object`

Represents a request to invoke an operator.

Parameters:
    

  * **operator_uri** â the URI of the operator to invoke

  * **params** (_None_) â an optional dictionary of parameters




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.executor.ExecutionProgress(_progress =None_, _label =None_)#
    

Bases: `object`

Represents the status of an operator execution.

Parameters:
    

  * **progress** (_None_) â an optional float between 0 and 1 (0% to 100%)

  * **label** (_None_) â an optional label to display




class fiftyone.operators.executor.Executor(_requests =None_, _logs =None_)#
    

Bases: `object`

Handles the execution phase of the operator lifecycle.

Parameters:
    

  * **requests** (_None_) â an optional list of InvocationRequest objects

  * **logs** (_None_) â an optional list of log messages




**Methods:**

`trigger`(operator_name[,Â params]) | Triggers an invocation of the operator with the given name.  
---|---  
`log`(message) | Logs a message.  
`to_json`() |   
  
trigger(_operator_name_ , _params =None_)#
    

Triggers an invocation of the operator with the given name.

Parameters:
    

  * **operator_name** â the name of the operator

  * **params** (_None_) â a dictionary of parameters for the operator



Returns:
    

a [`fiftyone.operators.message.GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage "fiftyone.operators.message.GeneratedMessage") containing instructions for the FiftyOne App to invoke the operator

log(_message_)#
    

Logs a message.

to_json()#
    

fiftyone.operators.executor.execute_operator(_operator_uri_ , _ctx =None_, _** kwargs_)#
    

Executes the operator with the given name.

Parameters:
    

  * **operator_uri** â the URI of the operator

  * **ctx** (_None_) â 

a dictionary of parameters defining the execution context. The supported keys are:

    * `dataset`: a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or the name of a dataset to process. This is required unless a `view` is provided

    * `view` (None): an optional [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to process

    * `selected` ([]): an optional list of selected sample IDs

    * `selected_labels` ([]): an optional list of selected labels in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

    * `current_sample` (None): an optional ID of the current sample being processed

    * `extended_selection` (None): an optional extended selection of the view.

    * `params`: a dictionary of parameters for the operator. Consult the operatorâs documentation for details

    * `request_delegation` (False): whether to request delegated execution, if supported by the operator

    * `delegation_target` (None): an optional orchestrator on which to schedule the operation, if it is delegated

    * `active_fields` ([]): a list of active field names

    * `workspace_name` (None): an optional name of the workspace to use for the operation

    * `spaces` (None): an optional dictionary defining spaces to use for the operation

    * `group_slice` (None): an optional group slice to use for the operationâs view. This is only applicable to group datasets

    * `query_performance` (None): whether to enable query performance

>     * `num_distributed_tasks` (None): the number of tasks to split
>
>> the operation into, if it is delegated.

  * ****kwargs** â you can optionally provide any of the supported `ctx` keys as keyword arguments rather than including them in `ctx`



Returns:
    

an `ExecutionResult`, or an `asyncio.Task` if you run this method in a notebook context

Raises:
    

**ExecutionError** â if an error occurred while immediately executing an operation or scheduling a delegated operation

async fiftyone.operators.executor.execute_or_delegate_operator(_operator_uri_ , _request_params_ , _exhaust =False_)#
    

Executes the operator with the given name.

Parameters:
    

  * **operator_uri** â the URI of the operator

  * **request_params** â a dictionary of parameters for the operator

  * **exhaust** (_False_) â whether to immediately exhaust generator operators



Returns:
    

an `ExecutionResult`

async fiftyone.operators.executor.prepare_operator_executor(_operator_uri_ , _request_params_ , _set_progress =None_, _delegated_operation_id =None_, _pipeline_ctx =None_)#
    

async fiftyone.operators.executor.do_execute_operator(_operator_ , _ctx_ , _exhaust =False_)#
    

async fiftyone.operators.executor.do_execute_pipeline(_pipeline_ , _ctx_)#
    

Executes the given pipeline in sequence.

Parameters:
    

  * **pipeline** â a [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline")

  * **ctx** â the `ExecutionContext` of the pipeline



Returns:
    

a tuple of (error, error message string) if an error occurred, or None. Pipelines do not return results directly

async fiftyone.operators.executor.resolve_type(_registry_ , _operator_uri_ , _request_params_)#
    

Resolves the inputs property type of the operator with the given name.

Parameters:
    

  * **registry** â an [`fiftyone.operators.OperatorRegistry`](api__fiftyone.operators.md#fiftyone.operators.OperatorRegistry "fiftyone.operators.OperatorRegistry")

  * **operator_uri** â the URI of the operator

  * **request_params** â a dictionary of request parameters



Returns:
    

the type of the inputs [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property") of the operator, or None

async fiftyone.operators.executor.resolve_type_with_context(_operator_ , _context_)#
    

Resolves the âinputsâ or âoutputsâ schema of an operator with the given context.

Parameters:
    

  * **operator** â the [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator")

  * **context** â the `ExecutionContext` of an operator



Returns:
    

the âinputsâ or âoutputsâ schema [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property") of an operator, or None

async fiftyone.operators.executor.resolve_execution_options(_registry_ , _operator_uri_ , _request_params_)#
    

Resolves the execution options of the operator with the given name.

Parameters:
    

  * **registry** â an [`fiftyone.operators.registry.OperatorRegistry`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry "fiftyone.operators.registry.OperatorRegistry")

  * **operator_uri** â the URI of the operator

  * **request_params** â a dictionary of request parameters



Returns:
    

a `fiftyone.operators.executor.ExecutionOptions` or None

fiftyone.operators.executor.resolve_placement(_operator_ , _request_params_)#
    

Resolves the placement of the operator with the given name.

Parameters:
    

  * **operator** â the [`fiftyone.operators.operator.Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

  * **request_params** â a dictionary of request parameters



Returns:
    

the placement of the operator or `None`

class fiftyone.operators.executor.ExecutionContext(_request_params =None_, _executor =None_, _set_progress =None_, _delegated_operation_id =None_, _operator_uri =None_, _required_secrets =None_, _pipeline =None_)#
    

Bases: `AbstractContextManager`

Represents the execution context of an operator.

Operators can use the execution context to access the view, dataset, and selected samples, as well as to trigger other operators.

Parameters:
    

  * **request_params** (_None_) â an optional dictionary of request parameters

  * **executor** (_None_) â an optional `Executor` instance

  * **set_progress** (_None_) â an optional function to set the progress of the current operation

  * **delegated_operation_id** (_None_) â an optional ID of the delegated operation

  * **operator_uri** (_None_) â the unique id of the operator

  * **required_secrets** (_None_) â the list of required secrets from the pluginâs definition

  * **pipeline** (_None_) â an optional `PipelineExecutionContext` with information about the current pipeline execution, if this operator is being executed as part of a pipeline




**Attributes:**

`dataset` | The [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.  
---|---  
`dataset_name` | The name of the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.  
`dataset_id` | The ID of the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.  
`view` | The [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") being operated on.  
`has_custom_view` | Whether the operator has a custom view.  
`spaces` | The current spaces layout in the FiftyOne App.  
`selected` | The list of selected IDs (if any).  
`selected_samples` | A list of selected sample dicts, if any.  
`sample_selection_style` | The current sample grid selection style config, if any.  
`label_selection_style` | The current label selection style config (if any).  
`selected_labels` | A list of selected labels (if any).  
`extended_selection` | The extended selection of the view (if any).  
`current_sample` | The ID of the current sample being processed (if any).  
`active_fields` | The list of currently active fields in the FiftyOne App sidebar.  
`user_id` | The ID of the user executing the operation, if known.  
`user_request_token` | The request token authenticating the user executing the operation, if known.  
`panel_id` | The ID of the panel that invoked the operator, if any.  
`panel_state` | The current panel state.  
`panel` | A [`fiftyone.operators.panel.PanelRef`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef "fiftyone.operators.panel.PanelRef") instance that you can use to read and write the state and data of the current panel.  
`delegated` | Whether the operation was delegated.  
`requesting_delegated_execution` | Whether delegated execution was requested for the operation.  
`delegation_target` | The orchestrator to which the operation was delegated (if any).  
`results` | A `dict` of results for the current operation.  
`secrets` | A read-only mapping of keys to their resolved values.  
`ops` | A [`fiftyone.operators.operations.Operations`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") instance that you can use to trigger builtin operations on the current context.  
`group_slice` | The current group slice of the view (if any).  
`num_distributed_tasks` | The number of tasks this job should be split into.  
`query_performance` | Whether query performance is enabled.  
`prompt_id` | An identifier for the prompt, unique to each instance of a user opening a prompt in the FiftyOne App.  
`operator_uri` | The URI of the target operator.  
  
**Methods:**

`target_view`([param_name]) | The target view for the operator being executed.  
---|---  
`view_target`([param_name]) | The target view for the operator being executed.  
`prompt`(operator_uri[,Â params,Â on_success,Â ...]) | Prompts the user to execute the operator with the given URI.  
`secret`(key) | Retrieves the secret with the given key.  
`resolve_secret_values`(keys,Â **kwargs) | Resolves the values of the given secrets keys.  
`trigger`(operator_name[,Â params]) | Triggers an invocation of the operator with the given name.  
`log`(message) | Logs a message to the browser console.  
`set_progress`([progress,Â label]) | Sets the progress of the current operation.  
`store`(store_name) | Retrieves the execution store with the given name.  
`serialize`() | Serializes the execution context.  
`to_dict`() | Returns the properties of the execution context as a dict.  
  
property dataset#
    

The [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.

property dataset_name#
    

The name of the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.

property dataset_id#
    

The ID of the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") being operated on.

property view#
    

The [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") being operated on.

target_view(_param_name ='view_target'_)#
    

The target view for the operator being executed.

Parameters:
    

**param_name** (_"view_target"_) â the name of the enum parameter defining the target view choice

Returns:
    

a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

view_target(_param_name ='view_target'_)#
    

The target view for the operator being executed.

Parameters:
    

**param_name** (_"view_target"_) â the name of the enum parameter defining the target view choice

Returns:
    

a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

property has_custom_view#
    

Whether the operator has a custom view.

property spaces#
    

The current spaces layout in the FiftyOne App.

property selected#
    

The list of selected IDs (if any).

Derived from `selected_samples` when available, otherwise falls back to `request_params["selected"]`.

property selected_samples#
    

A list of selected sample dicts, if any.

Each dict has `id` and `type` (`"default"` or `"alt"`), where type corresponds to a key in `sample_selection_style`.

Despite its name, `selected_samples` represents whatever sample grid items are in the current view: samples, patches, clips, or frames.

property sample_selection_style#
    

The current sample grid selection style config, if any.

A dict with a `default` key and optional `alt` key specifying icon styles.

property label_selection_style#
    

The current label selection style config (if any).

A dict with a `default` key and optional `alt` key specifying label selection visual styles.

property selected_labels#
    

A list of selected labels (if any).

Items are dictionaries with the following keys:

  * `label_id`: the ID of the label

  * `sample_id`: the ID of the sample containing the label

  * `field`: the field name containing the label

  * `frame_number`: the frame number containing the label (only applicable to video samples)

  * `type`: the selection type (`"default"` or `"alt"`)




property extended_selection#
    

The extended selection of the view (if any).

property current_sample#
    

The ID of the current sample being processed (if any).

When executed via the FiftyOne App, this is set when the user opens a sample in the modal.

property active_fields#
    

The list of currently active fields in the FiftyOne App sidebar.

property user_id#
    

The ID of the user executing the operation, if known.

property user_request_token#
    

The request token authenticating the user executing the operation, if known.

property panel_id#
    

The ID of the panel that invoked the operator, if any.

property panel_state#
    

The current panel state.

Only available when the operator is invoked from a panel.

property panel#
    

A [`fiftyone.operators.panel.PanelRef`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef "fiftyone.operators.panel.PanelRef") instance that you can use to read and write the state and data of the current panel.

Only available when the operator is invoked from a panel.

property delegated#
    

Whether the operation was delegated.

property requesting_delegated_execution#
    

Whether delegated execution was requested for the operation.

property delegation_target#
    

The orchestrator to which the operation was delegated (if any).

property results#
    

A `dict` of results for the current operation.

property secrets#
    

A read-only mapping of keys to their resolved values.

property ops#
    

A [`fiftyone.operators.operations.Operations`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") instance that you can use to trigger builtin operations on the current context.

property group_slice#
    

The current group slice of the view (if any).

property num_distributed_tasks#
    

The number of tasks this job should be split into.

property query_performance#
    

Whether query performance is enabled.

property prompt_id#
    

An identifier for the prompt, unique to each instance of a user opening a prompt in the FiftyOne App.

property operator_uri#
    

The URI of the target operator.

prompt(_operator_uri_ , _params =None_, _on_success =None_, _on_error =None_, _skip_prompt =False_)#
    

Prompts the user to execute the operator with the given URI.

Parameters:
    

  * **operator_uri** â the URI of the operator

  * **params** (_None_) â a dictionary of parameters for the operator

  * **on_success** (_None_) â a callback to invoke if the user successfully executes the operator

  * **on_error** (_None_) â a callback to invoke if the execution fails

  * **skip_prompt** (_False_) â whether to skip the prompt



Returns:
    

a [`fiftyone.operators.message.GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage "fiftyone.operators.message.GeneratedMessage") containing instructions for the FiftyOne App to prompt the user

secret(_key_)#
    

Retrieves the secret with the given key.

Parameters:
    

**key** â a secret key

Returns:
    

the secret value

async resolve_secret_values(_keys_ , _** kwargs_)#
    

Resolves the values of the given secrets keys.

Parameters:
    

  * **keys** â a list of secret keys

  * ****kwargs** â additional keyword arguments to pass to the secrets client for authentication if required




trigger(_operator_name_ , _params =None_)#
    

Triggers an invocation of the operator with the given name.

This method is only available when the operator is invoked via the FiftyOne App. You can check this via `ctx.executor`.

Example:
    
    
    def execute(self, ctx):
        # Trigger the `reload_dataset` operator after this operator
        # finishes executing
        ctx.trigger("reload_dataset")
    
        # Immediately trigger the `reload_dataset` operator while a
        # generator operator is executing
        yield ctx.trigger("reload_dataset")
    

Parameters:
    

  * **operator_name** â the name of the operator

  * **params** (_None_) â a dictionary of parameters for the operator



Returns:
    

a [`fiftyone.operators.message.GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage "fiftyone.operators.message.GeneratedMessage") containing instructions for the FiftyOne App to invoke the operator

log(_message_)#
    

Logs a message to the browser console.

Note

This method is only available to non-delegated operators. You can only use this method during the execution of an operator.

Parameters:
    

**message** â a message to log

Returns:
    

a [`fiftyone.operators.message.GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage "fiftyone.operators.message.GeneratedMessage") containing instructions for the FiftyOne App to invoke the operator

set_progress(_progress =None_, _label =None_)#
    

Sets the progress of the current operation.

Parameters:
    

  * **progress** (_None_) â an optional float between 0 and 1 (0% to 100%)

  * **label** (_None_) â an optional label to display




store(_store_name_)#
    

Retrieves the execution store with the given name.

The store is automatically created if necessary.

Parameters:
    

**store_name** â the name of the store

Returns:
    

a [`fiftyone.operators.store.ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore")

serialize()#
    

Serializes the execution context.

Returns:
    

a JSON dict

to_dict()#
    

Returns the properties of the execution context as a dict.

class fiftyone.operators.executor.ExecutionResult(_result =None_, _executor =None_, _error =None_, _error_message =None_, _validation_ctx =None_, _delegated =False_, _outputs_schema =None_, _is_sse =False_)#
    

Bases: `object`

Represents the result of an operator execution.

Parameters:
    

  * **result** (_None_) â the execution result

  * **executor** (_None_) â an `Executor`

  * **error** (_None_) â an error traceback, if an error occurred

  * **error_message** (_None_) â an error message, if an error occurred

  * **validation_ctx** (_None_) â a `ValidationContext`

  * **delegated** (_False_) â whether execution was delegated

  * **outputs_schema** (_None_) â a JSON dict representing the output schema of the operator

  * **is_sse** (_False_) â whether execution was from an operator handling server-sent events (SSE)




**Attributes:**

`is_generator` | Whether the result is a generator or an async generator.  
---|---  
  
**Methods:**

`raise_exceptions`() | Raises an `ExecutionError` (only) if the operation failed.  
---|---  
`to_exception`() | Returns an `ExecutionError` representing a failed execution result.  
`to_json`() | Returns a JSON dict representation of the result.  
  
property is_generator#
    

Whether the result is a generator or an async generator.

raise_exceptions()#
    

Raises an `ExecutionError` (only) if the operation failed.

to_exception()#
    

Returns an `ExecutionError` representing a failed execution result.

Returns:
    

a `ExecutionError`, or None if the execution did not fail

to_json()#
    

Returns a JSON dict representation of the result.

Returns:
    

a JSON dict

class fiftyone.operators.executor.PipelineExecutionContext(_active_ , _curr_stage_index_ , _total_stages_ , _pipeline_errors =None_, _num_distributed_tasks =0_, _** __)#
    

Bases: `object`

Represents the execution context of a pipeline.

Operators can use the pipeline execution context to access information about the current pipeline execution, if they are a child operation in a pipeline.

**Attributes:**

`active` | Whether the pipeline is currently active, i.e., having no failures in prior stages  
---|---  
`curr_stage_index` | Index of the pipeline's current execution stage  
`total_stages` | The total number of stages in the pipeline  
`pipeline_errors` | Mapping from past pipeline child operation str IDs to error messages, if available  
`num_distributed_tasks` | The number of distributed tasks in the current stage  
  
active: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether the pipeline is currently active, i.e., having no failures in prior stages

curr_stage_index: int#
    

Index of the pipelineâs current execution stage

total_stages: int#
    

The total number of stages in the pipeline

pipeline_errors: dict[str, str] | None = None#
    

Mapping from past pipeline child operation str IDs to error messages, if available

num_distributed_tasks: int = 0#
    

The number of distributed tasks in the current stage

exception fiftyone.operators.executor.ExecutionError#
    

Bases: `Exception`

An error that occurs while executing an operator.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.operators.executor.ValidationError(_reason_ , _property_ , _path_ , _custom =False_)#
    

Bases: `object`

A validation error.

Parameters:
    

  * **reason** â the reason

  * **property** â the property

  * **path** â the path




**Methods:**

`to_json`() | Returns a JSON dict representation of the error.  
---|---  
  
to_json()#
    

Returns a JSON dict representation of the error.

Returns:
    

a JSON dict

class fiftyone.operators.executor.ValidationContext(_ctx_ , _inputs_property_ , _operator_)#
    

Bases: `object`

Represents the validation context of an operator.

Parameters:
    

  * **ctx** â the `ExecutionContext`

  * **inputs_property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property") of the operator inputs

  * **operator** â the [`fiftyone.operators.operator.Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")




**Methods:**

`to_json`() | Returns a JSON dict representation of the context.  
---|---  
`add_error`(error) | Adds a validation error.  
`validate_enum`(path,Â property,Â value) | Validates an enum value.  
`validate_list`(path,Â property,Â value) | Validates a list value.  
`validate_property`(path,Â property,Â value) | Validates a property value.  
`validate_object`(path,Â property,Â value) | Validates an object value.  
`validate_primitive`(path,Â property,Â value) | Validates a primitive value.  
`exists_or_non_required`(property,Â value) |   
  
to_json()#
    

Returns a JSON dict representation of the context.

Returns:
    

a JSON dict

add_error(_error_)#
    

Adds a validation error.

Parameters:
    

**error** â a `ValidationError`

validate_enum(_path_ , _property_ , _value_)#
    

Validates an enum value.

Parameters:
    

  * **path** â the path to the property

  * **property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

  * **value** â the value to validate



Returns:
    

a `ValidationError`, if the value is invalid

validate_list(_path_ , _property_ , _value_)#
    

Validates a list value.

Parameters:
    

  * **path** â the path to the property

  * **property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

  * **value** â the value to validate



Returns:
    

a `ValidationError`, if the value is invalid

validate_property(_path_ , _property_ , _value_)#
    

Validates a property value.

Parameters:
    

  * **path** â the path to the property

  * **property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

  * **value** â the value to validate



Returns:
    

a `ValidationError`, if the value is invalid

validate_object(_path_ , _property_ , _value_)#
    

Validates an object value.

Parameters:
    

  * **path** â the path to the property

  * **property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

  * **value** â the value to validate



Returns:
    

a `ValidationError`, if the value is invalid

validate_primitive(_path_ , _property_ , _value_)#
    

Validates a primitive value.

Parameters:
    

  * **path** â the path to the property

  * **property** â the [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

  * **value** â the value to validate



Returns:
    

a `ValidationError`, if the value is invalid

exists_or_non_required(_property_ , _value_)#
    

class fiftyone.operators.executor.ExecutionOptions(_allow_immediate_execution =True_, _allow_delegated_execution =False_, _default_choice_to_delegated =False_, _allow_distributed_execution =False_, _min_distributed_tasks =2_, _max_distributed_tasks =None_, _recommended_distributed_tasks =None_, _** __)#
    

Bases: `object`

Represents the execution options of an operation.

Parameters:
    

  * **allow_immediate_execution** (_True_) â whether the operation can be executed immediately

  * **allow_delegated_execution** (_False_) â whether the operation can be delegated to an orchestrator

  * **default_choice_to_delegated** (_False_) â whether to default to delegated execution, if allowed

  * **allow_distributed_execution** (_False_) â whether the operator supports distributing delegated execution across parallel workers. Only valid for delegated operations.

  * **min_distributed_tasks** (_2_) â the minimum number of tasks that a distributed delegated operation can be split into. None means no limit. Only valid for distributed and delegated operations.

  * **max_distributed_tasks** (_None_) â the maximum number of tasks that a distributed delegated operation can be split into. None means no limit. Only valid for distributed and delegated operations.

  * **recommended_distributed_tasks** (_None_) â the recommended number of tasks that a distributed delegated operation should be split into. None means no recommendation. Only valid for distributed and delegated operations.




**Attributes:**

`allow_immediate_execution` |   
---|---  
`allow_delegated_execution` |   
`allow_distributed_execution` |   
`default_choice_to_delegated` |   
`min_distributed_tasks` |   
`max_distributed_tasks` |   
`recommended_distributed_tasks` |   
`available_orchestrators` |   
`orchestrator_registration_enabled` |   
  
**Methods:**

`update`([available_orchestrators]) |   
---|---  
`to_dict`() |   
  
property allow_immediate_execution#
    

property allow_delegated_execution#
    

property allow_distributed_execution#
    

property default_choice_to_delegated#
    

property min_distributed_tasks#
    

property max_distributed_tasks#
    

property recommended_distributed_tasks#
    

property available_orchestrators#
    

property orchestrator_registration_enabled#
    

update(_available_orchestrators =None_)#
    

to_dict()#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
