---
source_url: https://docs.voxel51.com/api/fiftyone.operators.store.store.html
---

# fiftyone.operators.store.store#

Execution store class.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ExecutionStore`(store_name,Â store_service[,Â ...]) | Execution store.  
---|---  
  
class fiftyone.operators.store.store.ExecutionStore(_store_name : str_, _store_service : [ExecutionStoreService](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService "fiftyone.operators.store.service.ExecutionStoreService")_, _default_policy : str = 'persist'_)#
    

Bases: `object`

Execution store.

Parameters:
    

  * **store_name** â the name of the store

  * **store_service** â an [`fiftyone.operators.store.service.ExecutionStoreService`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService "fiftyone.operators.store.service.ExecutionStoreService")

  * **default_policy** (_"persist"_) â the default eviction policy for the store.




**Methods:**

`create`(store_name[,Â dataset_id,Â ...]) | Creates a new execution store.  
---|---  
`list_stores`() | Lists all stores in the execution store.  
`get`(key) | Retrieves a value from the store by its key.  
`set`(key,Â value[,Â ttl,Â policy]) | Sets the value of a key in the specified store.  
`set_cache`(key,Â value[,Â ttl]) | Sets a value in the store with the eviction policy set to "evict".  
`delete`(key) | Deletes a key from the store.  
`has`(key) | Checks if the store has a specific key.  
`clear`() | Clears all the data in the store.  
`clear_cache`() | Clears the cache for the store.  
`update_ttl`(key,Â new_ttl) | Updates the TTL for a specific key.  
`update_policy`(key,Â policy) | Updates the eviction policy for a specific key.  
`get_metadata`(key) | Retrieves the metadata for the given key.  
`list_keys`() | Lists all keys in the store.  
`subscribe`(callback) | Subscribes to changes in the store.  
`unsubscribe`(subscription_id) | Unsubscribes from changes in the store.  
  
static create(_store_name : str_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _default_policy : str = 'persist'_, _collection_name : str | None = None_) → ExecutionStore#
    

Creates a new execution store.

Parameters:
    

  * **store_name** â the name of the store

  * **dataset_id** â an optional dataset ID to scope the store to



Returns:
    

an ExecutionStore instance

list_stores() → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Lists all stores in the execution store.

Returns:
    

a list of store names

Return type:
    

[list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")

get(_key : str_) → Any | None#
    

Retrieves a value from the store by its key.

Parameters:
    

**key** â the key to retrieve the value for

Returns:
    

the value stored under the given key, or None if not found

set(_key : str_, _value : Any_, _ttl : int | None = None_, _policy =None_) → None#
    

Sets the value of a key in the specified store.

Parameters:
    

  * **key** â the key to set

  * **value** â the value to set

  * **ttl** (_None_) â an optional TTL in seconds

  * **policy** (_persist_) â the eviction policy for the key. Can be âpersistâ or âevictâ. If âpersistâ, the key will never be automatically removed. If âevictâ, the key may be removed automatically if a TTL is set, or manually via `clear_cache()`.



Returns:
    

a `fiftyone.store.models.KeyDocument`

set_cache(_key : str_, _value : Any_, _ttl : int | None = None_) → None#
    

Sets a value in the store with the eviction policy set to âevictâ.

Parameters:
    

  * **key** â the key to store the value under

  * **value** â the value to store

  * **ttl** (_None_) â the time-to-live in seconds




delete(_key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Deletes a key from the store.

Parameters:
    

**key** â the key to delete.

Returns:
    

True/False whether the key was deleted

has(_key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Checks if the store has a specific key.

Parameters:
    

**key** â the key to check

Returns:
    

True/False whether the key exists

clear() → None#
    

Clears all the data in the store.

clear_cache() → None#
    

Clears the cache for the store.

This will remove all keys that are eligible for eviction.

update_ttl(_key : str_, _new_ttl : int_) → None#
    

Updates the TTL for a specific key.

Parameters:
    

  * **key** â the key to update the TTL for

  * **new_ttl** â the new TTL in seconds




update_policy(_key : str_, _policy : str_) → None#
    

Updates the eviction policy for a specific key.

Parameters:
    

  * **key** â the key to update the policy for

  * **policy** â the new policy, either âpersistâ or âevictâ




get_metadata(_key : str_) → dict | None#
    

Retrieves the metadata for the given key.

Parameters:
    

**key** â the key to check

Returns:
    

a dict of metadata about the key

list_keys() → [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str]#
    

Lists all keys in the store.

Returns:
    

a list of keys in the store

subscribe(_callback : Callable[[[MessageData](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData "fiftyone.operators.message.MessageData")], None]_) → str#
    

Subscribes to changes in the store.

Parameters:
    

**callback** â a function that will be called when a change occurs in the store

Returns:
    

a subscription ID

unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribes from changes in the store.

Parameters:
    

**subscription_id** â the subscription ID to unsubscribe from

Returns:
    

True if the subscription was removed, False otherwise

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
