---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.database.html
---

# fiftyone.core.odm.database#

Database utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DatabaseConfigDocument`(conn[,Â version,Â type]) | Backing document for the database config.  
---|---  
  
**Functions:**

`get_db_config`() | Retrieves the database config.  
---|---  
`establish_db_conn`(config) | Establishes the database connection.  
`aggregate`(collection,Â pipelines[,Â hints,Â ...]) | Executes one or more aggregations on a collection.  
`ensure_connection`() | Ensures database connection exists  
`get_db_client`() | Returns a database client.  
`get_db_conn`() | Returns a connection to the database.  
`get_db_version`() | Returns the database version.  
`get_async_db_client`([use_global]) | Returns an async database client.  
`get_async_db_conn`([use_global]) | Returns an async connection to the database.  
`drop_database`() | Drops the database.  
`sync_database`() | Syncs all pending database writes to disk.  
`list_collections`() | Returns a list of all collection names in the database.  
`drop_collection`(collection_name) | Drops specified collection from the database.  
`drop_orphan_collections`([dry_run]) | Drops all orphan collections from the database.  
`drop_orphan_saved_views`([dry_run]) | Drops all orphan saved views from the database.  
`drop_orphan_generated_datasets`([dry_run]) | Marks all orphan generated datasets as non-persistent so that they will  
`drop_orphan_workspaces`([dry_run]) | Drops all orphan workspaces from the database.  
`drop_orphan_runs`([dry_run]) | Drops all orphan runs from the database.  
`drop_orphan_delegated_ops`([dry_run]) | Drops all orphan delegated operations from the database.  
`drop_orphan_stores`([dry_run]) | Drops all orphan execution stores from the database.  
`stream_collection`(collection_name) | Streams the contents of the collection to stdout.  
`get_collection_stats`(collection_name) | Sets stats about the collection.  
`count_documents`(coll,Â pipeline) |   
`export_document`(doc,Â json_path) | Exports the document to disk in JSON format.  
`export_collection`(docs,Â json_dir_or_path[,Â ...]) | Exports the collection to disk in JSON format.  
`import_document`(json_path) | Imports a document from JSON on disk.  
`import_collection`(json_dir_or_path[,Â key]) | Imports the collection from JSON on disk.  
`insert_documents`(docs,Â coll[,Â ordered,Â ...]) | Inserts documents into a collection.  
`bulk_write`(ops,Â coll[,Â ordered,Â batcher,Â ...]) | Performs a batch of write operations on a collection.  
`list_datasets`() | Returns the list of available FiftyOne datasets.  
`load_dataset`([id,Â name,Â reload]) | Loads the FiftyOne dataset with the given ID or name.  
`patch_saved_views`(dataset_name[,Â dry_run]) | Ensures that the saved view documents in the `views` collection for the given dataset exactly match the IDs in its dataset document.  
`patch_workspaces`(dataset_name[,Â dry_run]) | Ensures that the workspace documents in the `workspaces` collection for the given dataset exactly match the IDs in its dataset document.  
`patch_annotation_runs`(dataset_name[,Â dry_run]) | Ensures that the annotation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_brain_runs`(dataset_name[,Â dry_run]) | Ensures that the brain method runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_evaluations`(dataset_name[,Â dry_run]) | Ensures that the evaluation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`patch_runs`(dataset_name[,Â dry_run]) | Ensures that the runs in the `runs` collection for the given dataset exactly match the values in its dataset document.  
`delete_dataset`(name[,Â dry_run]) | Deletes the dataset with the given name.  
`delete_saved_view`(dataset_name,Â view_name[,Â ...]) | Deletes the saved view with the given name from the dataset with the given name.  
`delete_saved_views`(dataset_name[,Â dry_run]) | Deletes all saved views from the dataset with the given name.  
`delete_workspace`(dataset_name,Â workspace_name) | Deletes the workspace with the given name from the dataset with the given name.  
`delete_workspaces`(dataset_name[,Â dry_run]) | Deletes all workspaces from the dataset with the given name.  
`delete_annotation_run`(name,Â anno_key[,Â dry_run]) | Deletes the annotation run with the given key from the dataset with the given name.  
`delete_annotation_runs`(name[,Â dry_run]) | Deletes all annotation runs from the dataset with the given name.  
`delete_brain_run`(name,Â brain_key[,Â dry_run]) | Deletes the brain method run with the given key from the dataset with the given name.  
`delete_brain_runs`(name[,Â dry_run]) | Deletes all brain method runs from the dataset with the given name.  
`delete_evaluation`(name,Â eval_key[,Â dry_run]) | Deletes the evaluation run with the given key from the dataset with the given name.  
`delete_evaluations`(name[,Â dry_run]) | Deletes all evaluations from the dataset with the given name.  
`delete_run`(name,Â run_key[,Â dry_run]) | Deletes the run with the given key from the dataset with the given name.  
`delete_runs`(name[,Â dry_run]) | Deletes all runs from the dataset with the given name.  
`get_indexed_values`(collection,Â ...[,Â ...]) | Returns the values of the field(s) for all samples in the given collection that are covered by the index.  
  
class fiftyone.core.odm.database.DatabaseConfigDocument(_conn_ , _version =None_, _type =None_, _* args_, _** kwargs_)#
    

Bases: `object`

Backing document for the database config.

**Attributes:**

`version` |   
---|---  
`type` |   
  
**Methods:**

`save`() |   
---|---  
  
version: str#
    

type: str#
    

save()#
    

fiftyone.core.odm.database.get_db_config()#
    

Retrieves the database config.

Returns:
    

a `DatabaseConfigDocument`

fiftyone.core.odm.database.establish_db_conn(_config_)#
    

Establishes the database connection.

If `fiftyone.config.database_uri` is defined, then we connect to that URI. Otherwise, a [`fiftyone.core.service.DatabaseService`](api__fiftyone.core.service.md#fiftyone.core.service.DatabaseService "fiftyone.core.service.DatabaseService") is created.

Parameters:
    

**config** â a [`fiftyone.core.config.FiftyOneConfig`](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")

Raises:
    

  * **ConnectionError** â if a connection to `mongod` could not be established

  * [**FiftyOneConfigError**](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfigError "fiftyone.core.config.FiftyOneConfigError") â if `fiftyone.config.database_uri` is not defined and `mongod` could not be found

  * [**ServiceExecutableNotFound**](api__fiftyone.core.service.md#fiftyone.core.service.ServiceExecutableNotFound "fiftyone.core.service.ServiceExecutableNotFound") â if [`fiftyone.core.service.DatabaseService`](api__fiftyone.core.service.md#fiftyone.core.service.DatabaseService "fiftyone.core.service.DatabaseService") startup was attempted, but `mongod` was not found in `fiftyone.db.bin`

  * **RuntimeError** â if the `mongod` found does not meet FiftyOneâs requirements, or validation could not occur




fiftyone.core.odm.database.aggregate(_collection_ , _pipelines_ , _hints =None_, _maxTimeMS =None_, __stream =False_)#
    

Executes one or more aggregations on a collection.

> Multiple aggregations are executed using multiple threads, and their results are returned as lists rather than cursors.

Parameters:
    

  * **collection** â a `pymongo.collection.Collection` or `motor.motor_asyncio.AsyncIOMotorCollection`

  * **pipelines** â a MongoDB aggregation pipeline or a list of pipelines

  * **hints** (_None_) â a corresponding index hint or list of index hints for each pipeline

  * **maxTimeMS** (_None_) â max timeout for the request(s)



Returns:
    

  * If a single pipeline is provided, a `pymongo.command_cursor.CommandCursor` or `motor.motor_asyncio.AsyncIOMotorCommandCursor` is returned

  * If multiple pipelines are provided, each cursor is extracted into a list and the list of lists is returned




fiftyone.core.odm.database.ensure_connection()#
    

Ensures database connection exists

fiftyone.core.odm.database.get_db_client()#
    

Returns a database client.

Returns:
    

a `pymongo.mongo_client.MongoClient`

fiftyone.core.odm.database.get_db_conn()#
    

Returns a connection to the database.

Returns:
    

a `pymongo.database.Database`

fiftyone.core.odm.database.get_db_version()#
    

Returns the database version.

Returns:
    

a `packaging.version.Version`

fiftyone.core.odm.database.get_async_db_client(_use_global =False_)#
    

Returns an async database client.

Parameters:
    

**use_global** â whether to use the global client singleton

Returns:
    

a `motor.motor_asyncio.AsyncIOMotorClient`

fiftyone.core.odm.database.get_async_db_conn(_use_global =False_)#
    

Returns an async connection to the database.

Returns:
    

a `motor.motor_asyncio.AsyncIOMotorDatabase`

fiftyone.core.odm.database.drop_database()#
    

Drops the database.

fiftyone.core.odm.database.sync_database()#
    

Syncs all pending database writes to disk.

fiftyone.core.odm.database.list_collections()#
    

Returns a list of all collection names in the database.

Returns:
    

a list of all collection names

fiftyone.core.odm.database.drop_collection(_collection_name_)#
    

Drops specified collection from the database.

Parameters:
    

**collection_name** â the collection name

fiftyone.core.odm.database.drop_orphan_collections(_dry_run =False_)#
    

Drops all orphan collections from the database.

Orphan collections are collections that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_saved_views(_dry_run =False_)#
    

Drops all orphan saved views from the database.

Orphan saved views are saved view documents that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_generated_datasets(_dry_run =False_)#
    

Marks all orphan generated datasets as non-persistent so that they will
    

be deleted the next time non-persistent dataset cleanup runs.

Orphan generated datasets are datasets that were originally associated with a saved generated view that no longer exists.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_workspaces(_dry_run =False_)#
    

Drops all orphan workspaces from the database.

Orphan workspaces are workspace documents that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_runs(_dry_run =False_)#
    

Drops all orphan runs from the database.

Orphan runs are runs that are not associated with any known dataset or other collections used by FiftyOne.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_delegated_ops(_dry_run =False_)#
    

Drops all orphan delegated operations from the database.

Orphan delegated operations are those that are associated with a dataset that no longer exists in the database.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.drop_orphan_stores(_dry_run =False_)#
    

Drops all orphan execution stores from the database.

Orphan stores are those that are associated with a dataset that no longer exists in the database.

Parameters:
    

**dry_run** (_False_) â whether to log the actions that would be taken but not perform them

fiftyone.core.odm.database.stream_collection(_collection_name_)#
    

Streams the contents of the collection to stdout.

Parameters:
    

**collection_name** â the name of the collection

fiftyone.core.odm.database.get_collection_stats(_collection_name_)#
    

Sets stats about the collection.

Parameters:
    

**collection_name** â the name of the collection

Returns:
    

a stats dict

fiftyone.core.odm.database.count_documents(_coll_ , _pipeline_)#
    

fiftyone.core.odm.database.export_document(_doc_ , _json_path_)#
    

Exports the document to disk in JSON format.

Parameters:
    

  * **doc** â a BSON document dict

  * **json_path** â the path to write the JSON file




fiftyone.core.odm.database.export_collection(_docs_ , _json_dir_or_path_ , _key ='documents'_, _patt ='{idx:06d}-{id}.json'_, _num_docs =None_, _progress =None_)#
    

Exports the collection to disk in JSON format.

Parameters:
    

  * **docs** â an iterable containing the documents to export

  * **json_dir_or_path** â the path to write a single JSON file containing the entire collection, or a directory in which to write per-document JSON files

  * **key** (_"documents"_) â the field name under which to store the documents when `json_path` is a single JSON file

  * **(****"{idx** (_patt_) â 06d}-{id}.jsonâ): a filename pattern to use when `json_path` is a directory. The pattern may contain `idx` to refer to the index of the document in `docs` or `id` to refer to the documentâs ID

  * **num_docs** (_None_) â the total number of documents. If omitted, this must be computable via `len(docs)`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.core.odm.database.import_document(_json_path_)#
    

Imports a document from JSON on disk.

Parameters:
    

**json_path** â the path to the document

Returns:
    

a BSON document dict

fiftyone.core.odm.database.import_collection(_json_dir_or_path_ , _key ='documents'_)#
    

Imports the collection from JSON on disk.

Parameters:
    

  * **json_dir_or_path** â the path to a JSON file on disk, or a directory containing per-document JSON files

  * **key** (_"documents"_) â the field name under which the documents are stored when `json_path` is a single JSON file



Returns:
    

a tuple of

  * an iterable of BSON documents

  * the number of documents




fiftyone.core.odm.database.insert_documents(_docs_ , _coll_ , _ordered =False_, _batcher =None_, _progress =None_, _num_docs =None_)#
    

Inserts documents into a collection.

The `_id` field of the input documents will be populated if it is not already set.

Parameters:
    

  * **docs** â an iterable of BSON document dicts

  * **coll** â a pymongo collection

  * **ordered** (_False_) â whether the documents must be inserted in order

  * **batcher** (_None_) â an optional [`fiftyone.core.utils.Batcher`](api__fiftyone.core.utils.md#fiftyone.core.utils.Batcher "fiftyone.core.utils.Batcher") class to use to batch the documents, or `False` to strictly insert the documents in a single batch. By default, `fiftyone.config.default_batcher` is used

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_docs** (_None_) â the total number of documents. Only used when `progress=True`. If omitted, this will be computed via `len(docs)`, if possible



Returns:
    

a list of IDs of the inserted documents

fiftyone.core.odm.database.bulk_write(_ops_ , _coll_ , _ordered =False_, _batcher =None_, _progress =False_)#
    

Performs a batch of write operations on a collection.

Parameters:
    

  * **ops** â a list of pymongo operations

  * **coll** â a pymongo collection

  * **ordered** (_False_) â whether the operations must be performed in order

  * **batcher** (_None_) â an optional [`fiftyone.core.utils.Batcher`](api__fiftyone.core.utils.md#fiftyone.core.utils.Batcher "fiftyone.core.utils.Batcher") class to use to batch the operations, or `False` to strictly perform the operations in a single batch. By default, `fiftyone.config.default_batcher` is used

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

A list of [`pymongo.results.BulkWriteResult`](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.BulkWriteResult "\(in PyMongo v4.17.0\)") objects

fiftyone.core.odm.database.list_datasets()#
    

Returns the list of available FiftyOne datasets.

This is a low-level implementation of dataset listing that does not call [`fiftyone.core.dataset.list_datasets()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.list_datasets "fiftyone.core.dataset.list_datasets"), which is helpful if a database may be corrupted.

Returns:
    

a list of `Dataset` names

fiftyone.core.odm.database.load_dataset(_id =None_, _name =None_, _reload =False_)#
    

Loads the FiftyOne dataset with the given ID or name.

Parameters:
    

  * **id** (_None_) â the ID of the dataset

  * **name** (_None_) â the name of the dataset

  * **reload** (_False_) â whether to reload the dataset if necessary



Returns:
    

a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

fiftyone.core.odm.database.patch_saved_views(_dataset_name_ , _dry_run =False_)#
    

Ensures that the saved view documents in the `views` collection for the given dataset exactly match the IDs in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.patch_workspaces(_dataset_name_ , _dry_run =False_)#
    

Ensures that the workspace documents in the `workspaces` collection for the given dataset exactly match the IDs in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.patch_annotation_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the annotation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.patch_brain_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the brain method runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.patch_evaluations(_dataset_name_ , _dry_run =False_)#
    

Ensures that the evaluation runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.patch_runs(_dataset_name_ , _dry_run =False_)#
    

Ensures that the runs in the `runs` collection for the given dataset exactly match the values in its dataset document.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_dataset(_name_ , _dry_run =False_)#
    

Deletes the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_saved_view(_dataset_name_ , _view_name_ , _dry_run =False_)#
    

Deletes the saved view with the given name from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_saved_view()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **view_name** â the name of the saved view

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_saved_views(_dataset_name_ , _dry_run =False_)#
    

Deletes all saved views from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_saved_view()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_workspace(_dataset_name_ , _workspace_name_ , _dry_run =False_)#
    

Deletes the workspace with the given name from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_workspace()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **workspace_name** â the name of the workspace

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_workspaces(_dataset_name_ , _dry_run =False_)#
    

Deletes all workspaces from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or `fiftyone.core.collections.SampleCollection.load_workspace()`, which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Parameters:
    

  * **dataset_name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_annotation_run(_name_ , _anno_key_ , _dry_run =False_)#
    

Deletes the annotation run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **anno_key** â the annotation key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_annotation_runs(_name_ , _dry_run =False_)#
    

Deletes all annotation runs from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_runs "fiftyone.core.collections.SampleCollection.delete_annotation_runs"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_brain_run(_name_ , _brain_key_ , _dry_run =False_)#
    

Deletes the brain method run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **brain_key** â the brain key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_brain_runs(_name_ , _dry_run =False_)#
    

Deletes all brain method runs from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_brain_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_runs "fiftyone.core.collections.SampleCollection.delete_brain_runs"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_evaluation(_name_ , _eval_key_ , _dry_run =False_)#
    

Deletes the evaluation run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_evaluation()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_evaluation "fiftyone.core.collections.SampleCollection.delete_evaluation"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **eval_key** â the evaluation key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_evaluations(_name_ , _dry_run =False_)#
    

Deletes all evaluations from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_evaluations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_evaluations "fiftyone.core.collections.SampleCollection.delete_evaluations"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_run(_name_ , _run_key_ , _dry_run =False_)#
    

Deletes the run with the given key from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_run "fiftyone.core.collections.SampleCollection.delete_run"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **run_key** â the run key

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.delete_runs(_name_ , _dry_run =False_)#
    

Deletes all runs from the dataset with the given name.

This is a low-level implementation of deletion that does not call [`fiftyone.core.dataset.load_dataset()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.load_dataset "fiftyone.core.dataset.load_dataset") or [`fiftyone.core.collections.SampleCollection.delete_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_runs "fiftyone.core.collections.SampleCollection.delete_runs"), which is helpful if a datasetâs backing document or collections are corrupted and cannot be loaded via the normal pathways.

Note that, as this method does not load [`fiftyone.core.runs.Run`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run "fiftyone.core.runs.Run") instances, it does not call [`fiftyone.core.runs.Run.cleanup()`](api__fiftyone.core.runs.md#fiftyone.core.runs.Run.cleanup "fiftyone.core.runs.Run.cleanup").

Parameters:
    

  * **name** â the name of the dataset

  * **dry_run** (_False_) â whether to log the actions that would be taken but not perform them




fiftyone.core.odm.database.get_indexed_values(_collection_ , _field_or_fields_ , _*_ , _index_key =None_, _query =None_, _values_only =False_, __stream =False_)#
    

Returns the values of the field(s) for all samples in the given collection that are covered by the index. Raises an error if the field is not indexed.

Parameters:
    

  * **collection** â a `pymongo.collection.Collection` or `motor.motor_asyncio.AsyncIOMotorCollection`

  * **field_or_fields** â the field name or list of field names to retrieve.

  * **index_key** (_None_) â the name of the index to use. If None, the default index name will be constructed from the field name(s).

  * **query** (_None_) â a dict selection filter to apply when querying. For performance, this should only include fields that are in the specified index.

  * **values_only** (_False_) â whether to remove field names from the resulting list. If True, the field names are removed and only the values will be returned as a list for each sample. If False, the field names are preserved and the values will be returned as a dict for each sample.



Returns:
    

a list of values for the specified field or index keys for each sample sorted in the same order as the index

Raises:
    

**ValueError** â if the field is not indexed

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
