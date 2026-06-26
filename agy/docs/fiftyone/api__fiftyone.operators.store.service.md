---
source_url: https://docs.voxel51.com/api/fiftyone.operators.store.service.html
---

# fiftyone.operators.store.service#

Execution store service.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ExecutionStoreService`([repo,Â dataset_id,Â ...]) | Service for managing execution store operations.  
---|---  
  
class fiftyone.operators.store.service.ExecutionStoreService(_repo : [ExecutionStoreRepo](api__fiftyone.factory.repos.execution_store.md#fiftyone.factory.repos.execution_store.ExecutionStoreRepo "fiftyone.factory.repos.execution_store.ExecutionStoreRepo") | None = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _collection_name : str = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_)#
    

Bases: `object`

Service for managing execution store operations.

Note that each instance of this service has a context:

  * If a `dataset_id` is provided (or a `repo` associated with one), this instance operates on stores associated with that dataset

  * If no `dataset_id` is provided (or a `repo` is provided that is not associated with one), this instance operates on stores that are not associated with a dataset




To operate on all stores across all contexts, use the `XXX_global()` methods that this class provides.

Parameters:
    

  * **repo** (_None_) â a [`fiftyone.factory.repos.execution_store.ExecutionStoreRepo`](api__fiftyone.factory.repos.execution_store.md#fiftyone.factory.repos.execution_store.ExecutionStoreRepo "fiftyone.factory.repos.execution_store.ExecutionStoreRepo") If not provided, a new [`fiftyone.factory.repos.execution_store.MongoExecutionStoreRepo`](api__fiftyone.factory.repos.execution_store.md#fiftyone.factory.repos.execution_store.MongoExecutionStoreRepo "fiftyone.factory.repos.execution_store.MongoExecutionStoreRepo") will be created

  * **dataset_id** (_None_) â a dataset ID (ObjectId) to scope operations to

  * **collection_name** (_None_) â a collection name to use for the execution store. If repo is provided, this argument is ignored

  * **notification_service** (_None_) â an optional notification service for the repository




**Methods:**

`create_store`(store_name[,Â metadata,Â policy]) | Creates a new store with the specified name.  
---|---  
`clear_cache`([store_name]) | Clears all cache entries in the execution stores.  
`get_store`(store_name) | Gets the specified store for the current context.  
`list_stores`() | Lists all stores for the current context.  
`count_stores`() | Counts the stores for the current context.  
`has_store`(store_name) | Determines whether the specified store exists in the current context.  
`delete_store`(store_name) | Deletes the specified store.  
`set_key`(store_name,Â key,Â value[,Â ttl,Â policy]) | Sets the value of a key in the specified store.  
`set_cache_key`(store_name,Â key,Â value[,Â ttl]) | Sets the value of a cache key in the specified store.  
`has_key`(store_name,Â key) | Determines whether the specified key exists in the specified store.  
`get_key`(store_name,Â key) | Retrieves the value of a key from the specified store.  
`delete_key`(store_name,Â key) | Deletes the specified key from the store.  
`update_ttl`(store_name,Â key,Â new_ttl) | Updates the TTL of the specified key in the store.  
`list_keys`(store_name) | Lists all keys in the specified store.  
`count_keys`(store_name) | Counts the keys in the specified store.  
`cleanup`() | Deletes all stores associated with the current context.  
`has_store_global`(store_name) | Determines whether a store with the given name exists across all datasets and the global context.  
`list_stores_global`() | Lists the stores across all datasets and the global context.  
`count_stores_global`() | Counts the stores across all datasets and the global context.  
`delete_store_global`(store_name) | Deletes the specified store across all datasets and the global context.  
`subscribe`(store_name,Â callback) | Subscribe to changes in a store.  
`unsubscribe`(subscription_id) | Unsubscribe from changes in a store.  
  
create_store(_store_name : str_, _metadata : dict[str, Any] | None = None_, _policy : str = 'persist'_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Creates a new store with the specified name.

Parameters:
    

**store_name** â the name of the store

Returns:
    

a `fiftyone.store.models.StoreDocument`

clear_cache(_store_name =None_) → None#
    

Clears all cache entries in the execution stores.

get_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Gets the specified store for the current context.

Parameters:
    

**store_name** â the name of the store

Returns:
    

a `fiftyone.store.models.StoreDocument`

list_stores() → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Lists all stores for the current context.

Returns:
    

a list of store names

count_stores() → int#
    

Counts the stores for the current context.

Returns:
    

the number of stores

has_store(_store_name_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Determines whether the specified store exists in the current context.

Parameters:
    

**store_name** â the name of the store

Returns:
    

True/False

delete_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Deletes the specified store.

Parameters:
    

**store_name** â the name of the store

Returns:
    

a `fiftyone.store.models.StoreDocument`

set_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_, _policy : str = 'persist'_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Sets the value of a key in the specified store.

Keys can be either **persistent** or **cacheable** , depending on the provided `policy` or whether a TTL (time-to-live) is set.

  * If `policy="persist"` (default), the key will remain in the store until explicitly deleted.

  * If `policy="evict"`, the key may be evicted by the system or manually removed using `clear_cache()`.

  * If a TTL is provided, the key is **always** treated as `policy="evict"`.




Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to set

  * **value** â the value to set

  * **ttl** (_None_) â an optional TTL in seconds

  * **policy** (_persist_) â the eviction policy for the key. Can be âpersistâ or âevictâ. If âpersistâ, the key will never be automatically removed. If âevictâ, the key may be removed automatically if a TTL is set, or manually via `clear_cache()`.



Returns:
    

The created or updated key document.

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

set_cache_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Sets the value of a cache key in the specified store.

Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to set

  * **value** â the value to set

  * **ttl** (_None_) â an optional TTL in seconds




has_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Determines whether the specified key exists in the specified store.

Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to check




get_key(_store_name : str_, _key : str_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Retrieves the value of a key from the specified store.

Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to retrieve



Returns:
    

a `fiftyone.store.models.KeyDocument`

delete_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Deletes the specified key from the store.

Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to delete



Returns:
    

True if the key was deleted, False otherwise

update_ttl(_store_name : str_, _key : str_, _new_ttl : int_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Updates the TTL of the specified key in the store.

Parameters:
    

  * **store_name** â the name of the store

  * **key** â the key to update the TTL for

  * **new_ttl** â the new TTL in seconds



Returns:
    

a `fiftyone.store.models.KeyDocument`

list_keys(_store_name : str_) → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Lists all keys in the specified store.

Parameters:
    

**store_name** â the name of the store

Returns:
    

a list of keys in the store

count_keys(_store_name : str_) → int#
    

Counts the keys in the specified store.

Parameters:
    

**store_name** â the name of the store

Returns:
    

the number of keys in the store

cleanup() → None#
    

Deletes all stores associated with the current context.

has_store_global(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Determines whether a store with the given name exists across all datasets and the global context.

Parameters:
    

**store_name** â the name of the store

Returns:
    

True/False

list_stores_global() → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[[StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")]#
    

Lists the stores across all datasets and the global context.

Returns:
    

a list of `fiftyone.store.models.StoreDocument`

count_stores_global() → int#
    

Counts the stores across all datasets and the global context.

Returns:
    

the number of stores

delete_store_global(_store_name : str_) → int#
    

Deletes the specified store across all datasets and the global context.

Parameters:
    

**store_name** â the name of the store

Returns:
    

the number of stores deleted

subscribe(_store_name : str_, _callback : Callable[[str], None]_) → str#
    

Subscribe to changes in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to subscribe to

  * **callback** (_Callable_ _[__[__str_ _]__,__None_ _]_) â the callback to call when a change occurs



Returns:
    

the subscription ID

Return type:
    

str

unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribe from changes in a store.

Parameters:
    

**subscription_id** (_str_) â the subscription ID to unsubscribe

Returns:
    

True if the subscription was removed, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
