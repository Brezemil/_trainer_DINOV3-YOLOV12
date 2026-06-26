---
source_url: https://docs.voxel51.com/api/fiftyone.factory.repos.delegated_operation.html
---

# fiftyone.factory.repos.delegated_operation#

FiftyOne delegated operation repository.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DelegatedOperationRepo`() | Base Class for a delegated operation repository.  
---|---  
`MongoDelegatedOperationRepo`([collection]) |   
  
class fiftyone.factory.repos.delegated_operation.DelegatedOperationRepo#
    

Bases: `object`

Base Class for a delegated operation repository.

**Methods:**

`queue_operation`(**kwargs) | Queue an operation to be executed by a delegated operator.  
---|---  
`add_child_error`(parent_id,Â child_id,Â ...) | Add an error message for a child operation to its parent.  
`update_run_state`(_id,Â run_state[,Â result,Â ...]) | Update the run state of an operation.  
`update_progress`(_id,Â progress) | Update the progress of an operation.  
`get_queued_operations`([operator,Â dataset_name]) | Get all queued operations.  
`get_scheduled_operations`([operator,Â ...]) | Get all scheduled operations.  
`get_running_operations`([operator,Â dataset_name]) | Get all running operations.  
`list_operations`([operator,Â dataset_name,Â ...]) | List all operations.  
`archive_operation`(_id) | Archive an operation.  
`unarchive_operation`(_id) | Unarchive an operation.  
`delete_operation`(_id) | Delete an operation.  
`delete_for_dataset`(dataset_id) | Delete an operation.  
`set_pinned`(_id[,Â pinned]) | Sets the pinned flag on / off.  
`set_label`(_id,Â label) | Sets the label for the delegated operation.  
`get`(_id) | Get an operation by id.  
`count`([filters,Â search]) | Count all operations.  
`ping`(_id) | Updates the updated_at field of an operation to keep it alive.  
  
queue_operation(_** kwargs: Any_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Queue an operation to be executed by a delegated operator.

add_child_error(_parent_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | str_, _child_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | str_, _error_message : str_) → None#
    

Add an error message for a child operation to its parent.

update_run_state(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _run_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") | None_, _result : [ExecutionResult](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") | None = None_, _run_link : str | None = None_, _progress : [ExecutionProgress](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") | None = None_, _required_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") | None = None_, _monitored : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Update the run state of an operation.

update_progress(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _progress : [ExecutionProgress](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Update the progress of an operation.

get_queued_operations(_operator : str = None_, _dataset_name =None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all queued operations.

get_scheduled_operations(_operator : str = None_, _dataset_name =None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all scheduled operations.

get_running_operations(_operator : str = None_, _dataset_name =None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all running operations.

list_operations(_operator : str = None_, _dataset_name : str = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") = None_, _run_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") = None_, _delegation_target : str = None_, _pinned : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = None_, _paging : [DelegatedOperationPagingParams](api__fiftyone.factory.md#fiftyone.factory.DelegatedOperationPagingParams "fiftyone.factory.DelegatedOperationPagingParams") = None_, _search : dict = None_, _include_archived : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _** kwargs: Any_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

List all operations.

archive_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Archive an operation.

unarchive_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Unarchive an operation.

delete_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Delete an operation.

delete_for_dataset(_dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_)#
    

Delete an operation.

set_pinned(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _pinned : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Sets the pinned flag on / off.

set_label(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _label : str_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Sets the label for the delegated operation.

get(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Get an operation by id.

count(_filters : dict = None_, _search : dict = None_) → int#
    

Count all operations.

ping(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_)#
    

Updates the updated_at field of an operation to keep it alive.

Parameters:
    

**_id** â the operation ID

class fiftyone.factory.repos.delegated_operation.MongoDelegatedOperationRepo(_collection : [Collection](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection "\(in PyMongo v4.17.0\)") = None_)#
    

Bases: `DelegatedOperationRepo`

**Attributes:**

`COLLECTION_NAME` |   
---|---  
`required_props` |   
  
**Methods:**

`queue_operation`(**kwargs) | Queue an operation to be executed by a delegated operator.  
---|---  
`set_pinned`(_id[,Â pinned]) | Sets the pinned flag on / off.  
`set_label`(_id,Â label) | Sets the label for the delegated operation.  
`add_child_error`(parent_id,Â child_id,Â ...) | Add an error message for a child operation to its parent.  
`update_run_state`(_id,Â run_state[,Â result,Â ...]) | Update the run state of an operation.  
`update_progress`(_id,Â progress) | Update the progress of an operation.  
`get_queued_operations`([operator,Â dataset_name]) | Get all queued operations.  
`get_scheduled_operations`([operator,Â ...]) | Get all scheduled operations.  
`get_running_operations`([operator,Â dataset_name]) | Get all running operations.  
`list_operations`([operator,Â dataset_name,Â ...]) | List all operations.  
`archive_operation`(_id) | Archive an operation.  
`unarchive_operation`(_id) | Unarchive an operation.  
`delete_operation`(_id) | Delete an operation.  
`delete_for_dataset`(dataset_id) | Delete an operation.  
`get`(_id) | Get an operation by id.  
`count`([filters,Â search]) | Count all operations.  
`ping`(_id) | Updates the updated_at field of an operation to keep it alive.  
  
COLLECTION_NAME = 'delegated_ops'#
    

required_props = ['operator', 'delegation_target', 'context', 'label']#
    

queue_operation(_** kwargs: Any_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Queue an operation to be executed by a delegated operator.

set_pinned(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _pinned : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Sets the pinned flag on / off.

set_label(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _label : str_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Sets the label for the delegated operation.

add_child_error(_parent_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | str_, _child_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | str_, _error_message : str_) → None#
    

Add an error message for a child operation to its parent.

update_run_state(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _run_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") | None_, _result : [ExecutionResult](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") | None = None_, _run_link : str | None = None_, _progress : [ExecutionProgress](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress") | None = None_, _required_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") | None = None_, _monitored : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Update the run state of an operation.

update_progress(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_, _progress : [ExecutionProgress](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress "fiftyone.operators.executor.ExecutionProgress")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Update the progress of an operation.

get_queued_operations(_operator : str = None_, _dataset_name : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") = None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all queued operations.

get_scheduled_operations(_operator : str = None_, _dataset_name : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") = None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all scheduled operations.

get_running_operations(_operator : str = None_, _dataset_name : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") = None_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

Get all running operations.

list_operations(_operator : str = None_, _dataset_name : str = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") = None_, _run_state : [ExecutionRunState](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState "fiftyone.operators.executor.ExecutionRunState") = None_, _delegation_target : str = None_, _pinned : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = None_, _paging : [DelegatedOperationPagingParams](api__fiftyone.factory.md#fiftyone.factory.DelegatedOperationPagingParams "fiftyone.factory.DelegatedOperationPagingParams") = None_, _search : dict = None_, _include_archived : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _** kwargs: Any_) → List[[DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")]#
    

List all operations.

archive_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Archive an operation.

unarchive_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Unarchive an operation.

delete_operation(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Delete an operation.

delete_for_dataset(_dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_)#
    

Delete an operation.

get(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_) → [DelegatedOperationDocument](api__fiftyone.factory.repos.delegated_operation_doc.md#fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument "fiftyone.factory.repos.delegated_operation_doc.DelegatedOperationDocument")#
    

Get an operation by id.

count(_filters : dict = None_, _search : dict = None_) → int#
    

Count all operations.

ping(__id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_)#
    

Updates the updated_at field of an operation to keep it alive.

Parameters:
    

**_id** â the operation ID

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
