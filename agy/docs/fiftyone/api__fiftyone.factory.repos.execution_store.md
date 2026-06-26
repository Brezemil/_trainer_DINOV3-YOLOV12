---
source_url: https://docs.voxel51.com/api/fiftyone.factory.repos.execution_store.html
---

# fiftyone.factory.repos.execution_store#

Execution store repository interface and implementations.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`AbstractExecutionStoreRepo`() | Abstract base class for execution store repositories.  
---|---  
`ExecutionStoreRepo`([dataset_id,Â ...]) | Base class for execution store repositories.  
`MongoExecutionStoreRepo`(collection[,Â ...]) | MongoDB implementation of the execution store repository.  
`InMemoryExecutionStoreRepo`([dataset_id,Â ...]) | In-memory implementation of execution store repository.  
  
class fiftyone.factory.repos.execution_store.AbstractExecutionStoreRepo#
    

Bases: `ABC`

Abstract base class for execution store repositories.

**Methods:**

`create_store`(store_name[,Â metadata,Â policy]) | Create a store in the store collection.  
---|---  
`get_store`(store_name) | Get a store from the store collection.  
`has_store`(store_name) | Check if a store exists in the store collection.  
`list_stores`() | List all stores in the store collection.  
`count_stores`() | Count the number of stores in the store collection.  
`delete_store`(store_name) | Delete a store.  
`set_key`(store_name,Â key,Â value[,Â ttl,Â policy]) | Set a key in a store.  
`set_cache_key`(store_name,Â key,Â value[,Â ttl]) | Set a cache key in a store.  
`has_key`(store_name,Â key) | Check if a key exists in a store.  
`get_key`(store_name,Â key) | Get a key from a store.  
`update_ttl`(store_name,Â key,Â ttl) | Update the TTL of a key.  
`delete_key`(store_name,Â key) | Delete a key from a store.  
`list_keys`(store_name) | List all keys in a store.  
`count_keys`(store_name) | Count the number of keys in a store.  
`cleanup`() | Delete all stores in the global store collection.  
`clear_cache`([store_name]) | Clear all keys with either a `ttl` or `policy="evict"`.  
`has_store_global`(store_name) | Check if a store exists in the global store collection.  
`list_stores_global`() | List all stores in the global store collection.  
`count_stores_global`() | Count the number of stores in the global store collection.  
`delete_store_global`(store_name) | Delete a store from the global store collection.  
  
abstractmethod create_store(_store_name : str_, _metadata : Dict[str, Any] | None = None_, _policy : str = 'persist'_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Create a store in the store collection.

Parameters:
    

  * **store_name** (_str_) â the name of the store to create

  * **metadata** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_) â the metadata to store with the store



Returns:
    

the created store document

Return type:
    

[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")

abstractmethod get_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument") | None#
    

Get a store from the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to get

Returns:
    

the store document, or None if the store does not exist

Return type:
    

Optional[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

abstractmethod has_store(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod list_stores() → List[str]#
    

List all stores in the store collection.

Returns:
    

a list of store names

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

abstractmethod count_stores() → int#
    

Count the number of stores in the store collection.

Returns:
    

the number of stores

Return type:
    

int

abstractmethod delete_store(_store_name : str_) → int#
    

Delete a store.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod set_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_, _policy : str = 'persist'_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a key in a store.

Parameters:
    

  * **store_name** (_str_) â The name of the store to set the key in.

  * **key** (_str_) â The key to set.

  * **value** (_Any_) â The value to associate with the key.

  * **ttl** (_Optional_ _[__int_ _]_) â Optional TTL (in seconds) after which the key will expire and be automatically removed.

  * **policy** (_str_) â The eviction policy for the key. One of: \- `"persist"` (default): Key is persistent until deleted. \- `"evict"`: Key is eligible for eviction or cache clearing.



Returns:
    

The created or updated key document.

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

abstractmethod set_cache_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a cache key in a store. :param store_name: the name of the store to set the cache key in :type store_name: str :param key: the cache key to set :type key: str :param value: the value to set :type value: Any :param ttl: the TTL of the cache key :type ttl: Optional[int]

Returns:
    

the created or updated cache key document

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

abstractmethod has_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a key exists in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to check

  * **key** (_str_) â the key to check



Returns:
    

True if the key exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod get_key(_store_name : str_, _key : str_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument") | None#
    

Get a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to get the key from

  * **key** (_str_) â the key to get



Returns:
    

the key document, or None if the key does not exist

Return type:
    

Optional[[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")]

abstractmethod update_ttl(_store_name : str_, _key : str_, _ttl : int_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Update the TTL of a key.

Parameters:
    

  * **store_name** (_str_) â the name of the store to update the TTL for

  * **key** (_str_) â the key to update the TTL for

  * **ttl** (_int_) â the new TTL



Returns:
    

True if the TTL was updated, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod delete_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Delete a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to delete the key from

  * **key** (_str_) â the key to delete



Returns:
    

True if the key was deleted, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod list_keys(_store_name : str_) → List[str]#
    

List all keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to list keys for

Returns:
    

a list of keys in the store

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

abstractmethod count_keys(_store_name : str_) → int#
    

Count the number of keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to count keys for

Returns:
    

the number of keys in the store

Return type:
    

int

abstractmethod cleanup() → int#
    

Delete all stores in the global store collection.

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod clear_cache(_store_name : str | None = None_) → int#
    

Clear all keys with either a `ttl` or `policy="evict"`.

Parameters:
    

**store_name** (_Optional_ _[__str_ _]_) â the name of the store to clear. If None, all stores will be queried for deletion.

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod has_store_global(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod list_stores_global() → List[[StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")]#
    

List all stores in the global store collection.

Returns:
    

a list of store documents

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

abstractmethod count_stores_global() → int#
    

Count the number of stores in the global store collection.

Returns:
    

the number of stores

Return type:
    

int

abstractmethod delete_store_global(_store_name : str_) → int#
    

Delete a store from the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

class fiftyone.factory.repos.execution_store.ExecutionStoreRepo(_dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_)#
    

Bases: `AbstractExecutionStoreRepo`

Base class for execution store repositories.

Each instance operates in a context: \- If a dataset_id is provided, it operates on stores associated with that dataset. \- If no dataset_id is provided, it operates on stores not associated with any dataset.

To operate on all stores across all contexts, use the `XXX_global()` methods that this class provides.

**Methods:**

`subscribe`(store_name,Â callback) | Subscribe to changes in a store.  
---|---  
`unsubscribe`(subscription_id) | Unsubscribe from changes in a store.  
`cleanup`() | Delete all stores in the global store collection.  
`clear_cache`([store_name]) | Clear all keys with either a `ttl` or `policy="evict"`.  
`count_keys`(store_name) | Count the number of keys in a store.  
`count_stores`() | Count the number of stores in the store collection.  
`count_stores_global`() | Count the number of stores in the global store collection.  
`create_store`(store_name[,Â metadata,Â policy]) | Create a store in the store collection.  
`delete_key`(store_name,Â key) | Delete a key from a store.  
`delete_store`(store_name) | Delete a store.  
`delete_store_global`(store_name) | Delete a store from the global store collection.  
`get_key`(store_name,Â key) | Get a key from a store.  
`get_store`(store_name) | Get a store from the store collection.  
`has_key`(store_name,Â key) | Check if a key exists in a store.  
`has_store`(store_name) | Check if a store exists in the store collection.  
`has_store_global`(store_name) | Check if a store exists in the global store collection.  
`list_keys`(store_name) | List all keys in a store.  
`list_stores`() | List all stores in the store collection.  
`list_stores_global`() | List all stores in the global store collection.  
`set_cache_key`(store_name,Â key,Â value[,Â ttl]) | Set a cache key in a store.  
`set_key`(store_name,Â key,Â value[,Â ttl,Â policy]) | Set a key in a store.  
`update_ttl`(store_name,Â key,Â ttl) | Update the TTL of a key.  
  
subscribe(_store_name : str_, _callback : Callable[[str], None]_) → str#
    

Subscribe to changes in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to subscribe to

  * **callback** (_Callable_ _[__[__str_ _]__,__None_ _]_) â the callback to call when a change occurs



Returns:
    

the subscription ID

Return type:
    

str

Raises:
    

**ValueError** â if no notification service is available

unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribe from changes in a store.

Parameters:
    

**subscription_id** (_str_) â the subscription ID to unsubscribe

Returns:
    

True if the subscription was removed, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

Raises:
    

**ValueError** â if no notification service is available

abstractmethod cleanup() → int#
    

Delete all stores in the global store collection.

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod clear_cache(_store_name : str | None = None_) → int#
    

Clear all keys with either a `ttl` or `policy="evict"`.

Parameters:
    

**store_name** (_Optional_ _[__str_ _]_) â the name of the store to clear. If None, all stores will be queried for deletion.

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod count_keys(_store_name : str_) → int#
    

Count the number of keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to count keys for

Returns:
    

the number of keys in the store

Return type:
    

int

abstractmethod count_stores() → int#
    

Count the number of stores in the store collection.

Returns:
    

the number of stores

Return type:
    

int

abstractmethod count_stores_global() → int#
    

Count the number of stores in the global store collection.

Returns:
    

the number of stores

Return type:
    

int

abstractmethod create_store(_store_name : str_, _metadata : Dict[str, Any] | None = None_, _policy : str = 'persist'_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Create a store in the store collection.

Parameters:
    

  * **store_name** (_str_) â the name of the store to create

  * **metadata** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_) â the metadata to store with the store



Returns:
    

the created store document

Return type:
    

[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")

abstractmethod delete_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Delete a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to delete the key from

  * **key** (_str_) â the key to delete



Returns:
    

True if the key was deleted, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod delete_store(_store_name : str_) → int#
    

Delete a store.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod delete_store_global(_store_name : str_) → int#
    

Delete a store from the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

abstractmethod get_key(_store_name : str_, _key : str_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument") | None#
    

Get a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to get the key from

  * **key** (_str_) â the key to get



Returns:
    

the key document, or None if the key does not exist

Return type:
    

Optional[[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")]

abstractmethod get_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument") | None#
    

Get a store from the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to get

Returns:
    

the store document, or None if the store does not exist

Return type:
    

Optional[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

abstractmethod has_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a key exists in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to check

  * **key** (_str_) â the key to check



Returns:
    

True if the key exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod has_store(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod has_store_global(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

abstractmethod list_keys(_store_name : str_) → List[str]#
    

List all keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to list keys for

Returns:
    

a list of keys in the store

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

abstractmethod list_stores() → List[str]#
    

List all stores in the store collection.

Returns:
    

a list of store names

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

abstractmethod list_stores_global() → List[[StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")]#
    

List all stores in the global store collection.

Returns:
    

a list of store documents

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

abstractmethod set_cache_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a cache key in a store. :param store_name: the name of the store to set the cache key in :type store_name: str :param key: the cache key to set :type key: str :param value: the value to set :type value: Any :param ttl: the TTL of the cache key :type ttl: Optional[int]

Returns:
    

the created or updated cache key document

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

abstractmethod set_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_, _policy : str = 'persist'_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a key in a store.

Parameters:
    

  * **store_name** (_str_) â The name of the store to set the key in.

  * **key** (_str_) â The key to set.

  * **value** (_Any_) â The value to associate with the key.

  * **ttl** (_Optional_ _[__int_ _]_) â Optional TTL (in seconds) after which the key will expire and be automatically removed.

  * **policy** (_str_) â The eviction policy for the key. One of: \- `"persist"` (default): Key is persistent until deleted. \- `"evict"`: Key is eligible for eviction or cache clearing.



Returns:
    

The created or updated key document.

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

abstractmethod update_ttl(_store_name : str_, _key : str_, _ttl : int_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Update the TTL of a key.

Parameters:
    

  * **store_name** (_str_) â the name of the store to update the TTL for

  * **key** (_str_) â the key to update the TTL for

  * **ttl** (_int_) â the new TTL



Returns:
    

True if the TTL was updated, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

class fiftyone.factory.repos.execution_store.MongoExecutionStoreRepo(_collection_ , _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_)#
    

Bases: `ExecutionStoreRepo`

MongoDB implementation of the execution store repository.

**Attributes:**

`COLLECTION_NAME` |   
---|---  
  
**Methods:**

`create_store`(store_name[,Â metadata,Â policy]) | Create a store in the store collection.  
---|---  
`clear_cache`([store_name]) | Clear all keys with either a `ttl` or `policy="evict"`.  
`get_store`(store_name) | Get a store from the store collection.  
`has_store`(store_name) | Check if a store exists in the store collection.  
`list_stores`() | List all stores in the store collection.  
`count_stores`() | Count the number of stores in the store collection.  
`delete_store`(store_name) | Delete a store.  
`set_key`(store_name,Â key,Â value[,Â ttl,Â policy]) | Set a key in a store.  
`set_cache_key`(store_name,Â key,Â value[,Â ttl]) | Set a cache key in a store.  
`has_key`(store_name,Â key) | Check if a key exists in a store.  
`get_key`(store_name,Â key) | Get a key from a store.  
`update_ttl`(store_name,Â key,Â ttl) | Update the TTL of a key.  
`delete_key`(store_name,Â key) | Delete a key from a store.  
`list_keys`(store_name) | List all keys in a store.  
`count_keys`(store_name) | Count the number of keys in a store.  
`cleanup`() | Delete all stores in the global store collection.  
`has_store_global`(store_name) | Check if a store exists in the global store collection.  
`list_stores_global`() | List all stores in the global store collection.  
`count_stores_global`() | Count the number of stores in the global store collection.  
`delete_store_global`(store_name) | Delete a store from the global store collection.  
`subscribe`(store_name,Â callback) | Subscribe to changes in a store.  
`unsubscribe`(subscription_id) | Unsubscribe from changes in a store.  
  
COLLECTION_NAME = 'execution_store'#
    

create_store(_store_name : str_, _metadata : Dict[str, Any] | None = None_, _policy : str = 'persist'_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Create a store in the store collection.

Parameters:
    

  * **store_name** (_str_) â the name of the store to create

  * **metadata** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_) â the metadata to store with the store



Returns:
    

the created store document

Return type:
    

[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")

clear_cache(_store_name =None_) → int#
    

Clear all keys with either a `ttl` or `policy="evict"`.

Parameters:
    

**store_name** (_Optional_ _[__str_ _]_) â the name of the store to clear. If None, all stores will be queried for deletion.

Returns:
    

the number of documents deleted

Return type:
    

int

get_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument") | None#
    

Get a store from the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to get

Returns:
    

the store document, or None if the store does not exist

Return type:
    

Optional[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

has_store(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_stores() → List[str]#
    

List all stores in the store collection.

Returns:
    

a list of store names

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

count_stores() → int#
    

Count the number of stores in the store collection.

Returns:
    

the number of stores

Return type:
    

int

delete_store(_store_name : str_) → int#
    

Delete a store.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

set_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_, _policy : str = 'persist'_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a key in a store.

Parameters:
    

  * **store_name** (_str_) â The name of the store to set the key in.

  * **key** (_str_) â The key to set.

  * **value** (_Any_) â The value to associate with the key.

  * **ttl** (_Optional_ _[__int_ _]_) â Optional TTL (in seconds) after which the key will expire and be automatically removed.

  * **policy** (_str_) â The eviction policy for the key. One of: \- `"persist"` (default): Key is persistent until deleted. \- `"evict"`: Key is eligible for eviction or cache clearing.



Returns:
    

The created or updated key document.

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

set_cache_key(_store_name_ , _key_ , _value_ , _ttl =None_)#
    

Set a cache key in a store. :param store_name: the name of the store to set the cache key in :type store_name: str :param key: the cache key to set :type key: str :param value: the value to set :type value: Any :param ttl: the TTL of the cache key :type ttl: Optional[int]

Returns:
    

the created or updated cache key document

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

has_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a key exists in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to check

  * **key** (_str_) â the key to check



Returns:
    

True if the key exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

get_key(_store_name : str_, _key : str_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument") | None#
    

Get a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to get the key from

  * **key** (_str_) â the key to get



Returns:
    

the key document, or None if the key does not exist

Return type:
    

Optional[[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")]

update_ttl(_store_name : str_, _key : str_, _ttl : int_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Update the TTL of a key.

Parameters:
    

  * **store_name** (_str_) â the name of the store to update the TTL for

  * **key** (_str_) â the key to update the TTL for

  * **ttl** (_int_) â the new TTL



Returns:
    

True if the TTL was updated, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

delete_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Delete a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to delete the key from

  * **key** (_str_) â the key to delete



Returns:
    

True if the key was deleted, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_keys(_store_name : str_) → List[str]#
    

List all keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to list keys for

Returns:
    

a list of keys in the store

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

count_keys(_store_name : str_) → int#
    

Count the number of keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to count keys for

Returns:
    

the number of keys in the store

Return type:
    

int

cleanup() → int#
    

Delete all stores in the global store collection.

Returns:
    

the number of documents deleted

Return type:
    

int

has_store_global(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_stores_global() → List[[StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")]#
    

List all stores in the global store collection.

Returns:
    

a list of store documents

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

count_stores_global() → int#
    

Count the number of stores in the global store collection.

Returns:
    

the number of stores

Return type:
    

int

delete_store_global(_store_name : str_) → int#
    

Delete a store from the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

subscribe(_store_name : str_, _callback : Callable[[str], None]_) → str#
    

Subscribe to changes in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to subscribe to

  * **callback** (_Callable_ _[__[__str_ _]__,__None_ _]_) â the callback to call when a change occurs



Returns:
    

the subscription ID

Return type:
    

str

Raises:
    

**ValueError** â if no notification service is available

unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribe from changes in a store.

Parameters:
    

**subscription_id** (_str_) â the subscription ID to unsubscribe

Returns:
    

True if the subscription was removed, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

Raises:
    

**ValueError** â if no notification service is available

class fiftyone.factory.repos.execution_store.InMemoryExecutionStoreRepo(_dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_)#
    

Bases: `ExecutionStoreRepo`

In-memory implementation of execution store repository.

**Methods:**

`create_store`(store_name[,Â metadata,Â policy]) | Create a store in the store collection.  
---|---  
`clear_cache`([store_name]) | Clear all keys with either a `ttl` or `policy="evict"`.  
`get_store`(store_name) | Get a store from the store collection.  
`has_store`(store_name) | Check if a store exists in the store collection.  
`list_stores`() | List all stores in the store collection.  
`count_stores`() | Count the number of stores in the store collection.  
`delete_store`(store_name) | Delete a store.  
`set_key`(store_name,Â key,Â value[,Â ttl,Â policy]) | Set a key in a store.  
`set_cache_key`(store_name,Â key,Â value[,Â ttl]) | Set a cache key in a store.  
`has_key`(store_name,Â key) | Check if a key exists in a store.  
`get_key`(store_name,Â key) | Get a key from a store.  
`update_ttl`(store_name,Â key,Â ttl) | Update the TTL of a key.  
`update_policy`(store_name,Â key,Â policy) |   
`delete_key`(store_name,Â key) | Delete a key from a store.  
`list_keys`(store_name) | List all keys in a store.  
`count_keys`(store_name) | Count the number of keys in a store.  
`cleanup`() | Delete all stores in the global store collection.  
`has_store_global`(store_name) | Check if a store exists in the global store collection.  
`list_stores_global`() | List all stores in the global store collection.  
`count_stores_global`() | Count the number of stores in the global store collection.  
`delete_store_global`(store_name) | Delete a store from the global store collection.  
`subscribe`(store_name,Â callback) | Subscribe to changes in a store.  
`unsubscribe`(subscription_id) | Unsubscribe from changes in a store.  
  
create_store(_store_name : str_, _metadata : Dict[str, Any] | None = None_, _policy : str = 'persist'_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")#
    

Create a store in the store collection.

Parameters:
    

  * **store_name** (_str_) â the name of the store to create

  * **metadata** (_Optional_ _[__Dict_ _[__str_ _,__Any_ _]__]_) â the metadata to store with the store



Returns:
    

the created store document

Return type:
    

[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")

clear_cache(_store_name =None_) → int#
    

Clear all keys with either a `ttl` or `policy="evict"`.

Parameters:
    

**store_name** (_Optional_ _[__str_ _]_) â the name of the store to clear. If None, all stores will be queried for deletion.

Returns:
    

the number of documents deleted

Return type:
    

int

get_store(_store_name : str_) → [StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument") | None#
    

Get a store from the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to get

Returns:
    

the store document, or None if the store does not exist

Return type:
    

Optional[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

has_store(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_stores() → List[str]#
    

List all stores in the store collection.

Returns:
    

a list of store names

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

count_stores() → int#
    

Count the number of stores in the store collection.

Returns:
    

the number of stores

Return type:
    

int

delete_store(_store_name : str_) → int#
    

Delete a store.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

set_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_, _policy : str = 'persist'_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Set a key in a store.

Parameters:
    

  * **store_name** (_str_) â The name of the store to set the key in.

  * **key** (_str_) â The key to set.

  * **value** (_Any_) â The value to associate with the key.

  * **ttl** (_Optional_ _[__int_ _]_) â Optional TTL (in seconds) after which the key will expire and be automatically removed.

  * **policy** (_str_) â The eviction policy for the key. One of: \- `"persist"` (default): Key is persistent until deleted. \- `"evict"`: Key is eligible for eviction or cache clearing.



Returns:
    

The created or updated key document.

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

set_cache_key(_store_name : str_, _key : str_, _value : Any_, _ttl : int | None = None_) → None#
    

Set a cache key in a store. :param store_name: the name of the store to set the cache key in :type store_name: str :param key: the cache key to set :type key: str :param value: the value to set :type value: Any :param ttl: the TTL of the cache key :type ttl: Optional[int]

Returns:
    

the created or updated cache key document

Return type:
    

[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")

has_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a key exists in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to check

  * **key** (_str_) â the key to check



Returns:
    

True if the key exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

get_key(_store_name : str_, _key : str_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument") | None#
    

Get a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to get the key from

  * **key** (_str_) â the key to get



Returns:
    

the key document, or None if the key does not exist

Return type:
    

Optional[[KeyDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument "fiftyone.operators.store.KeyDocument")]

update_ttl(_store_name : str_, _key : str_, _ttl : int_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Update the TTL of a key.

Parameters:
    

  * **store_name** (_str_) â the name of the store to update the TTL for

  * **key** (_str_) â the key to update the TTL for

  * **ttl** (_int_) â the new TTL



Returns:
    

True if the TTL was updated, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

update_policy(_store_name : str_, _key : str_, _policy : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

delete_key(_store_name : str_, _key : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Delete a key from a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to delete the key from

  * **key** (_str_) â the key to delete



Returns:
    

True if the key was deleted, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_keys(_store_name : str_) → List[str]#
    

List all keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to list keys for

Returns:
    

a list of keys in the store

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str]

count_keys(_store_name : str_) → int#
    

Count the number of keys in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to count keys for

Returns:
    

the number of keys in the store

Return type:
    

int

cleanup() → int#
    

Delete all stores in the global store collection.

Returns:
    

the number of documents deleted

Return type:
    

int

has_store_global(_store_name : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if a store exists in the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to check

Returns:
    

True if the store exists, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

list_stores_global() → List[[StoreDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument "fiftyone.operators.store.models.StoreDocument")]#
    

List all stores in the global store collection.

Returns:
    

a list of store documents

Return type:
    

[List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[[StoreDocument](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument "fiftyone.operators.store.StoreDocument")]

count_stores_global() → int#
    

Count the number of stores in the global store collection.

Returns:
    

the number of stores

Return type:
    

int

delete_store_global(_store_name : str_) → int#
    

Delete a store from the global store collection.

Parameters:
    

**store_name** (_str_) â the name of the store to delete

Returns:
    

the number of documents deleted

Return type:
    

int

subscribe(_store_name : str_, _callback : Callable[[str], None]_) → str#
    

Subscribe to changes in a store.

Parameters:
    

  * **store_name** (_str_) â the name of the store to subscribe to

  * **callback** (_Callable_ _[__[__str_ _]__,__None_ _]_) â the callback to call when a change occurs



Returns:
    

the subscription ID

Return type:
    

str

Raises:
    

**ValueError** â if no notification service is available

unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribe from changes in a store.

Parameters:
    

**subscription_id** (_str_) â the subscription ID to unsubscribe

Returns:
    

True if the subscription was removed, False otherwise

Return type:
    

[bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")

Raises:
    

**ValueError** â if no notification service is available

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
