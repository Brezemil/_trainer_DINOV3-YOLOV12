---
source_url: https://docs.voxel51.com/plugins/api/plugins.panels.similarity_search.run_manager.html
---

# plugins.panels.similarity_search.run_manager#

Similarity search run manager.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_head_dataset_id`(dataset) | Get the head dataset ID for a given dataset or a snapshot.  
---|---  
  
**Classes:**

`RunManager`(ctx) | Manager class for persisting and retrieving similarity search runs.  
---|---  
  
plugins.panels.similarity_search.run_manager.get_head_dataset_id(_dataset_)#
    

Get the head dataset ID for a given dataset or a snapshot.

Parameters:
    

**dataset** â the dataset instance

Returns:
    

the head dataset ID as a string

class plugins.panels.similarity_search.run_manager.RunManager(_ctx_)#
    

Bases: `object`

Manager class for persisting and retrieving similarity search runs.

**Methods:**

`create_run`(run_params) | Create a new run entry.  
---|---  
`get_run`(run_id) | Get a run by ID.  
`set_run`(run_id,Â run_data) | Write a full run record to the store (atomic upsert).  
`update_run`(run_id,Â updates) | Update fields on an existing run (read-modify-write).  
`set_operator_run_id`(run_id,Â operator_run_id) | Link a delegated operation ID to a run and create index key.  
`find_run_by_operator_id`(operator_run_id) | Find a run by its delegated operation ID.  
`delete_run`(run_id) | Delete a run and its index keys.  
`list_runs`([owner,Â current_user_id,Â can_manage]) | List runs sorted by creation time (newest first).  
  
create_run(_run_params : Dict[str, Any]_) → Dict[str, Any]#
    

Create a new run entry.

Parameters:
    

**run_params** â run configuration parameters

Returns:
    

the full run data dict

get_run(_run_id : str_) → Dict | None#
    

Get a run by ID.

Parameters:
    

**run_id** â the run ID

Returns:
    

the run data dict, or None

set_run(_run_id : str_, _run_data : Dict[str, Any]_)#
    

Write a full run record to the store (atomic upsert).

Parameters:
    

  * **run_id** â the run ID

  * **run_data** â the complete run data dict




update_run(_run_id : str_, _updates : Dict[str, Any]_)#
    

Update fields on an existing run (read-modify-write).

For hot paths where the caller already holds the full run dict, prefer mutating locally and calling `set_run()` directly.

Parameters:
    

  * **run_id** â the run ID

  * **updates** â dict of fields to update




set_operator_run_id(_run_id : str_, _operator_run_id : str_)#
    

Link a delegated operation ID to a run and create index key.

Parameters:
    

  * **run_id** â the run ID

  * **operator_run_id** â the delegated operation document ID




find_run_by_operator_id(_operator_run_id : str_) → Dict | None#
    

Find a run by its delegated operation ID. O(1) lookup.

Parameters:
    

**operator_run_id** â the delegated operation document ID

Returns:
    

the run data dict, or None

delete_run(_run_id : str_)#
    

Delete a run and its index keys.

Parameters:
    

**run_id** â the run ID

list_runs(_owner : str | None = None_, _current_user_id : str | None = None_, _can_manage : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → List[Dict]#
    

List runs sorted by creation time (newest first).

Parameters:
    

  * **owner** â âmineâ to restrict to runs whose `created_by` matches `current_user_id`; âallâ or `None` returns every run.

  * **current_user_id** â the current userâs id. Required when `owner == "mine"`; ignored otherwise.

  * **can_manage** â whether the current user has manage permissions. Non-managers are always restricted to their own runs regardless of `owner`.



Returns:
    

list of run data dicts

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
