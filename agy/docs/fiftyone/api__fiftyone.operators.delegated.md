---
source_url: https://docs.voxel51.com/api/fiftyone.operators.delegated.html
---

# fiftyone.operators.delegated#

FiftyOne delegated operations.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DelegatedOperationService`([repo]) | Service for executing delegated operations.  
---|---  
  
class fiftyone.operators.delegated.DelegatedOperationService(_repo =None_)#
    

Bases: `object`

Service for executing delegated operations.

**Methods:**

`queue_operation`(operator[,Â label,Â ...]) | Queues the given delegated operation for execution.  
---|---  
`set_progress`(doc_id,Â progress) | Sets the progress of the given delegated operation.  
`set_running`(doc_id[,Â progress,Â run_link,Â ...]) | Sets the given delegated operation to running state.  
`set_scheduled`(doc_id[,Â required_state]) | Sets the given delegated operation to scheduled state. :param doc_id: the ID of the delegated operation :param required_state: an optional [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state. :type required_state: None.  
`set_queued`(doc_id[,Â required_state]) | Sets the given delegated operation to queued state.  
`set_completed`(doc_id[,Â result,Â progress,Â ...]) | Sets the given delegated operation to completed state.  
`set_failed`(doc_id[,Â result,Â progress,Â ...]) | Sets the given delegated operation to failed state.  
`set_pinned`(doc_id[,Â pinned]) | Sets the pinned flag for the given delegated operation.  
`set_label`(doc_id,Â label) | Sets the pinned flag for the given delegated operation.  
`archive_operation`(doc_id) | Archives the given delegated operation.  
`unarchive_operation`(doc_id) | Unarchives the given delegated operation.  
`delete_operation`(doc_id) | Deletes the given delegated operation.  
`delete_for_dataset`(dataset_id) | Deletes all delegated operations associated with the given dataset.  
`rerun_operation`(doc_id) | Reruns the specified delegated operation.  
`get_queued_operations`([operator,Â dataset_name]) | Returns all queued delegated operations.  
`get_scheduled_operations`([operator,Â ...]) | Returns all scheduled delegated operations. :param operator: the optional name of the operator to return all the scheduled delegated operations for :type operator: None :param dataset_name: the optional name of the dataset to return all the scheduled delegated operations for :type dataset_name: None.  
`get_running_operations`([operator,Â dataset_name]) | Returns all running delegated operations. :param operator: the optional name of the operator to return all the running delegated operations for :type operator: None :param dataset_name: the optional name of the dataset to return all the running delegated operations for :type dataset_name: None.  
`get`(doc_id) | Returns the delegated operation with the given ID.  
`list_operations`([operator,Â dataset_name,Â ...]) | Lists the delegated operations matching the given criteria.  
`execute_queued_operations`([operator,Â ...]) | Executes queued delegated operations matching the given criteria.  
`count`([filters,Â search]) | Counts the delegated operations matching the given criteria.  
`execute_operation`(operation[,Â log,Â ...]) | Executes the given delegated operation.  
  
queue_operation(_operator_ , _label =None_, _delegation_target =None_, _context =None_, _metadata =None_, _pipeline =None_, _rerunnable =True_)#
    

Queues the given delegated operation for execution.

Parameters:
    

  * **operator** â the operator name

  * **delegation_target** (_None_) â an optional delegation target

  * **label** (_None_) â an optional label for the operation (will default to the operator if not supplied)

  * **context** (_None_) â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **metadata** (_None_) â an optional metadata dict containing properties below: \- inputs_schema: the schema of the operatorâs inputs \- outputs_schema: the schema of the operatorâs outputs

  * **pipeline** (_None_) â an optional [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline") to use for the operation, if this is a pipeline operator

  * **rerunnable** (_True_) â whether the operation can be rerun



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

set_progress(_doc_id_ , _progress_)#
    

Sets the progress of the given delegated operation.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **progress** â the [`fiftyone.operators.executor.ExecutionProgress`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") of the operation



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

set_running(_doc_id_ , _progress =None_, _run_link =None_, _required_state =None_, _monitored =False_)#
    

Sets the given delegated operation to running state.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **progress** (_None_) â an optional [`fiftyone.operators.executor.ExecutionProgress`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") of the operation

  * **run_link** (_None_) â an optional link to orchestrator-specific information about the operation

  * **required_state** (_None_) â an optional [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state.

  * **monitored** (_False_) â whether the operation is being monitored by an external process



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument` if the
    

update was performed, else `None`.

set_scheduled(_doc_id_ , _required_state =None_)#
    

Sets the given delegated operation to scheduled state. :param doc_id: the ID of the delegated operation :param required_state: an optional

> [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state.

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument` if the
    

update was performed, else `None`.

set_queued(_doc_id_ , _required_state =None_)#
    

Sets the given delegated operation to queued state.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **required_state** (_None_) â an optional [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state.



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument` if the
    

update was performed, else `None`.

set_completed(_doc_id_ , _result =None_, _progress =None_, _run_link =None_, _required_state =None_)#
    

Sets the given delegated operation to completed state.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **result** (_None_) â the [`fiftyone.operators.executor.ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") of the operation

  * **progress** (_None_) â an optional [`fiftyone.operators.executor.ExecutionProgress`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") of the operation

  * **run_link** (_None_) â an optional link to orchestrator-specific information about the operation

  * **required_state** (_None_) â an optional [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state.



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument` if the
    

update was performed, else `None`.

set_failed(_doc_id_ , _result =None_, _progress =None_, _run_link =None_, _required_state =None_, _update_pipeline =None_)#
    

Sets the given delegated operation to failed state.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **result** (_None_) â the [`fiftyone.operators.executor.ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") of the operation

  * **progress** (_None_) â an optional [`fiftyone.operators.executor.ExecutionProgress`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") of the operation

  * **run_link** (_None_) â an optional link to orchestrator-specific information about the operation

  * **required_state** (_None_) â an optional [`fiftyone.operators.executor.ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") required state of the operation. If provided, the update will only be performed if the referenced operation matches this state.

  * **update_pipeline** (_None_) â an optional ID of the parent operation to update with this failure message, applicable only for pipeline children. If provided, the parent operation will NOT be marked as failed, but the error message will be recorded in its pipeline run info.



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument` if the
    

update was performed, else `None`.

set_pinned(_doc_id_ , _pinned =True_)#
    

Sets the pinned flag for the given delegated operation.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **pinned** (_True_) â the boolean pinned flag



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

set_label(_doc_id_ , _label_)#
    

Sets the pinned flag for the given delegated operation.

Parameters:
    

  * **doc_id** â the ID of the delegated operation

  * **label** â the label to set



Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

archive_operation(_doc_id_)#
    

Archives the given delegated operation.

Parameters:
    

**doc_id** â the ID of the delegated operation

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

unarchive_operation(_doc_id_)#
    

Unarchives the given delegated operation.

Parameters:
    

**doc_id** â the ID of the delegated operation

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

delete_operation(_doc_id_)#
    

Deletes the given delegated operation.

Parameters:
    

**doc_id** â the ID of the delegated operation

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

delete_for_dataset(_dataset_id_)#
    

Deletes all delegated operations associated with the given dataset.

Parameters:
    

**dataset_id** â the ID of the dataset

rerun_operation(_doc_id_)#
    

Reruns the specified delegated operation.

Parameters:
    

**doc_id** â the ID of the delegated operation

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

get_queued_operations(_operator =None_, _dataset_name =None_)#
    

Returns all queued delegated operations.

Parameters:
    

  * **operator** (_None_) â the optional name of the operator to return all the queued delegated operations for

  * **dataset_name** (_None_) â the optional name of the dataset to return all the queued delegated operations for



Returns:
    

a list of `fiftyone.factory.repos.DelegatedOperationDocument`

get_scheduled_operations(_operator =None_, _dataset_name =None_)#
    

Returns all scheduled delegated operations. :param operator: the optional name of the operator to return all

> the scheduled delegated operations for

Parameters:
    

**dataset_name** (_None_) â the optional name of the dataset to return all the scheduled delegated operations for

Returns:
    

a list of `fiftyone.factory.repos.DelegatedOperationDocument`

get_running_operations(_operator =None_, _dataset_name =None_)#
    

Returns all running delegated operations. :param operator: the optional name of the operator to return all

> the running delegated operations for

Parameters:
    

**dataset_name** (_None_) â the optional name of the dataset to return all the running delegated operations for

Returns:
    

a list of `fiftyone.factory.repos.DelegatedOperationDocument`

get(_doc_id_)#
    

Returns the delegated operation with the given ID.

Parameters:
    

**doc_id** â the ID of the delegated operation

Returns:
    

a `fiftyone.factory.repos.DelegatedOperationDocument`

list_operations(_operator =None_, _dataset_name =None_, _dataset_id =None_, _run_state =None_, _delegation_target =None_, _paging =None_, _search =None_, _include_archived =False_, _** kwargs_)#
    

Lists the delegated operations matching the given criteria.

Parameters:
    

  * **operator** (_None_) â the optional name of the operator to return all the delegated operations for

  * **dataset_name** (_None_) â the optional name of the dataset to return all the delegated operations for

  * **dataset_id** (_None_) â the optional id of the dataset to return all the delegated operations for

  * **run_state** (_None_) â the optional run state of the delegated operations to return

  * **delegation_target** (_None_) â the optional delegation target of the delegated operations to return

  * **paging** (_None_) â optional [`fiftyone.factory.DelegatedOperationPagingParams`](api__fiftyone.factory.md#fiftyone.factory.DelegatedOperationPagingParams "fiftyone.factory.DelegatedOperationPagingParams")

  * **search** (_None_) â optional search term dict

  * **include_archived** (_False_) â whether to include archived operations



Returns:
    

a list of `fiftyone.factory.repos.DelegatedOperationDocument`

execute_queued_operations(_operator =None_, _delegation_target =None_, _dataset_name =None_, _limit =None_, _log =False_, _monitor =False_, _check_interval_seconds =60_, _stdout_capture =None_, _on_monitor_ping =None_, _** kwargs_)#
    

Executes queued delegated operations matching the given criteria.

Parameters:
    

  * **operator** (_None_) â the optional name of the operator to execute all the queued delegated operations for

  * **delegation_target** (_None_) â the optional delegation target of the delegated operations to execute

  * **dataset_name** (_None_) â the optional name of the dataset to execute all the queued delegated operations for

  * **limit** (_None_) â the optional limit of the number of delegated operations to execute

  * **log** (_False_) â the optional boolean flag to log the execution of the delegated operations

  * **monitor** (_False_) â if we should monitor the state of the operator in a subprocess.

  * **check_interval_seconds** (_60_) â how many seconds to wait between polling operator status.

  * **stdout_capture** (_None_) â an optional callable returning a context manager that captures stdout/stderr into logging. Must be picklable (e.g. a top-level function) for spawn context.

  * **on_monitor_ping** (_None_) â an optional callback `fn(child_pid)` invoked on each monitor ping




count(_filters =None_, _search =None_)#
    

Counts the delegated operations matching the given criteria.

Parameters:
    

  * **filters** (_None_) â a filter dict

  * **search** (_None_) â a search term dict



Returns:
    

the number of matching operations

execute_operation(_operation_ , _log =False_, _run_link =None_, _monitor =False_, _check_interval_seconds =60_, _stdout_capture =None_, _on_monitor_ping =None_)#
    

Executes the given delegated operation.

Parameters:
    

  * **operation** â the `fiftyone.factory.repos.DelegatedOperationDocument`

  * **log** (_False_) â the optional boolean flag to log the execution of the delegated operations

  * **run_link** (_None_) â an optional link to orchestrator-specific information about the operation

  * **monitor** (_False_) â if we should monitor the state of the operator in a subprocess.

  * **check_interval_seconds** (_60_) â how many seconds to wait between polling operator status.

  * **stdout_capture** (_None_) â an optional callable returning a context manager that captures stdout/stderr into logging. Must be picklable (e.g. a top-level function) for spawn context.

  * **on_monitor_ping** (_None_) â an optional callback `fn(child_pid)` invoked on each monitor ping




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
