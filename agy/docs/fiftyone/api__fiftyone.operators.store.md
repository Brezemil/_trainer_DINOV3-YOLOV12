---
source_url: https://docs.voxel51.com/api/fiftyone.operators.store.html
---

# fiftyone.operators.store#

  * [fiftyone.operators.store.models](api__fiftyone.operators.store.models.md)
    * [`KeyPolicy`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy)
      * [`KeyPolicy.PERSIST`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.PERSIST)
      * [`KeyPolicy.EVICT`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.EVICT)
      * [`KeyPolicy.encode()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.encode)
      * [`KeyPolicy.replace()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.replace)
      * [`KeyPolicy.split()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.split)
      * [`KeyPolicy.rsplit()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rsplit)
      * [`KeyPolicy.join()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.join)
      * [`KeyPolicy.capitalize()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.capitalize)
      * [`KeyPolicy.casefold()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.casefold)
      * [`KeyPolicy.title()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.title)
      * [`KeyPolicy.center()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.center)
      * [`KeyPolicy.count()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.count)
      * [`KeyPolicy.expandtabs()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.expandtabs)
      * [`KeyPolicy.find()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.find)
      * [`KeyPolicy.partition()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.partition)
      * [`KeyPolicy.index()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.index)
      * [`KeyPolicy.ljust()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.ljust)
      * [`KeyPolicy.lower()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.lower)
      * [`KeyPolicy.lstrip()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.lstrip)
      * [`KeyPolicy.rfind()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rfind)
      * [`KeyPolicy.rindex()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rindex)
      * [`KeyPolicy.rjust()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rjust)
      * [`KeyPolicy.rstrip()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rstrip)
      * [`KeyPolicy.rpartition()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.rpartition)
      * [`KeyPolicy.splitlines()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.splitlines)
      * [`KeyPolicy.strip()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.strip)
      * [`KeyPolicy.swapcase()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.swapcase)
      * [`KeyPolicy.translate()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.translate)
      * [`KeyPolicy.upper()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.upper)
      * [`KeyPolicy.startswith()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.startswith)
      * [`KeyPolicy.endswith()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.endswith)
      * [`KeyPolicy.removeprefix()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.removeprefix)
      * [`KeyPolicy.removesuffix()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.removesuffix)
      * [`KeyPolicy.isascii()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isascii)
      * [`KeyPolicy.islower()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.islower)
      * [`KeyPolicy.isupper()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isupper)
      * [`KeyPolicy.istitle()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.istitle)
      * [`KeyPolicy.isspace()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isspace)
      * [`KeyPolicy.isdecimal()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isdecimal)
      * [`KeyPolicy.isdigit()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isdigit)
      * [`KeyPolicy.isnumeric()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isnumeric)
      * [`KeyPolicy.isalpha()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isalpha)
      * [`KeyPolicy.isalnum()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isalnum)
      * [`KeyPolicy.isidentifier()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isidentifier)
      * [`KeyPolicy.isprintable()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.isprintable)
      * [`KeyPolicy.zfill()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.zfill)
      * [`KeyPolicy.format()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.format)
      * [`KeyPolicy.format_map()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.format_map)
      * [`KeyPolicy.maketrans()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy.maketrans)
    * [`KeyDocument`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument)
      * [`KeyDocument.store_name`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.store_name)
      * [`KeyDocument.key`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.key)
      * [`KeyDocument.value`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.value)
      * [`KeyDocument.dataset_id`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.dataset_id)
      * [`KeyDocument.created_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.created_at)
      * [`KeyDocument.updated_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.updated_at)
      * [`KeyDocument.expires_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.expires_at)
      * [`KeyDocument.policy`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.policy)
      * [`KeyDocument.get_expiration()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.get_expiration)
      * [`KeyDocument.from_dict()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.from_dict)
      * [`KeyDocument.to_mongo_dict()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument.to_mongo_dict)
    * [`StoreDocument`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument)
      * [`StoreDocument.key`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.key)
      * [`StoreDocument.value`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.value)
      * [`StoreDocument.metadata`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.metadata)
      * [`StoreDocument.dataset_id`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.dataset_id)
      * [`StoreDocument.expires_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.expires_at)
      * [`StoreDocument.from_dict()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.from_dict)
      * [`StoreDocument.get_expiration()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.get_expiration)
      * [`StoreDocument.policy`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.policy)
      * [`StoreDocument.to_mongo_dict()`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.to_mongo_dict)
      * [`StoreDocument.updated_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.updated_at)
      * [`StoreDocument.store_name`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.store_name)
      * [`StoreDocument.created_at`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.StoreDocument.created_at)
  * [fiftyone.operators.store.notification_service](api__fiftyone.operators.store.notification_service.md)
    * [`ChangeStreamNotificationService`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService)
      * [`ChangeStreamNotificationService.subscribe()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.subscribe)
      * [`ChangeStreamNotificationService.unsubscribe()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.unsubscribe)
      * [`ChangeStreamNotificationService.unsubscribe_all()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.unsubscribe_all)
      * [`ChangeStreamNotificationService.notify()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.notify)
      * [`ChangeStreamNotificationService.start()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.start)
      * [`ChangeStreamNotificationService.stop()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService.stop)
    * [`MongoChangeStreamNotificationService`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService)
      * [`MongoChangeStreamNotificationService.subscribe()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.subscribe)
      * [`MongoChangeStreamNotificationService.unsubscribe()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.unsubscribe)
      * [`MongoChangeStreamNotificationService.unsubscribe_all()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.unsubscribe_all)
      * [`MongoChangeStreamNotificationService.start()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.start)
      * [`MongoChangeStreamNotificationService.notify()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.notify)
      * [`MongoChangeStreamNotificationService.stop()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService.stop)
    * [`MongoChangeStreamNotificationServiceLifecycleManager`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationServiceLifecycleManager)
      * [`MongoChangeStreamNotificationServiceLifecycleManager.start_in_dedicated_thread()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationServiceLifecycleManager.start_in_dedicated_thread)
      * [`MongoChangeStreamNotificationServiceLifecycleManager.stop()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.MongoChangeStreamNotificationServiceLifecycleManager.stop)
    * [`is_notification_service_disabled()`](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.is_notification_service_disabled)
  * [fiftyone.operators.store.service](api__fiftyone.operators.store.service.md)
    * [`ExecutionStoreService`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService)
      * [`ExecutionStoreService.create_store()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.create_store)
      * [`ExecutionStoreService.clear_cache()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.clear_cache)
      * [`ExecutionStoreService.get_store()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.get_store)
      * [`ExecutionStoreService.list_stores()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.list_stores)
      * [`ExecutionStoreService.count_stores()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.count_stores)
      * [`ExecutionStoreService.has_store()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.has_store)
      * [`ExecutionStoreService.delete_store()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.delete_store)
      * [`ExecutionStoreService.set_key()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.set_key)
      * [`ExecutionStoreService.set_cache_key()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.set_cache_key)
      * [`ExecutionStoreService.has_key()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.has_key)
      * [`ExecutionStoreService.get_key()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.get_key)
      * [`ExecutionStoreService.delete_key()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.delete_key)
      * [`ExecutionStoreService.update_ttl()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.update_ttl)
      * [`ExecutionStoreService.list_keys()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.list_keys)
      * [`ExecutionStoreService.count_keys()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.count_keys)
      * [`ExecutionStoreService.cleanup()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.cleanup)
      * [`ExecutionStoreService.has_store_global()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.has_store_global)
      * [`ExecutionStoreService.list_stores_global()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.list_stores_global)
      * [`ExecutionStoreService.count_stores_global()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.count_stores_global)
      * [`ExecutionStoreService.delete_store_global()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.delete_store_global)
      * [`ExecutionStoreService.subscribe()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.subscribe)
      * [`ExecutionStoreService.unsubscribe()`](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService.unsubscribe)
  * [fiftyone.operators.store.store](api__fiftyone.operators.store.store.md)
    * [`ExecutionStore`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore)
      * [`ExecutionStore.create()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.create)
      * [`ExecutionStore.list_stores()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.list_stores)
      * [`ExecutionStore.get()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.get)
      * [`ExecutionStore.set()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.set)
      * [`ExecutionStore.set_cache()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.set_cache)
      * [`ExecutionStore.delete()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.delete)
      * [`ExecutionStore.has()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.has)
      * [`ExecutionStore.clear()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.clear)
      * [`ExecutionStore.clear_cache()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.clear_cache)
      * [`ExecutionStore.update_ttl()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.update_ttl)
      * [`ExecutionStore.update_policy()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.update_policy)
      * [`ExecutionStore.get_metadata()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.get_metadata)
      * [`ExecutionStore.list_keys()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.list_keys)
      * [`ExecutionStore.subscribe()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.subscribe)
      * [`ExecutionStore.unsubscribe()`](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore.unsubscribe)
  * [fiftyone.operators.store.subscription_registry](api__fiftyone.operators.store.subscription_registry.md)
    * [`LocalSubscriptionRegistry`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry)
      * [`LocalSubscriptionRegistry.subscribe()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry.subscribe)
      * [`LocalSubscriptionRegistry.unsubscribe()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry.unsubscribe)
      * [`LocalSubscriptionRegistry.unsubscribe_all()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry.unsubscribe_all)
      * [`LocalSubscriptionRegistry.empty_subscribers()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry.empty_subscribers)
      * [`LocalSubscriptionRegistry.get_subscribers()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry.get_subscribers)
    * [`InLocalMemorySubscriptionRegistry`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry)
      * [`InLocalMemorySubscriptionRegistry.subscribe()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry.subscribe)
      * [`InLocalMemorySubscriptionRegistry.unsubscribe()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry.unsubscribe)
      * [`InLocalMemorySubscriptionRegistry.unsubscribe_all()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry.unsubscribe_all)
      * [`InLocalMemorySubscriptionRegistry.get_subscribers()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry.get_subscribers)
      * [`InLocalMemorySubscriptionRegistry.empty_subscribers()`](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry.empty_subscribers)



## Module contents#

Execution store.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ExecutionStoreService`([repo,Â dataset_id,Â ...]) | Service for managing execution store operations.  
---|---  
`ExecutionStore`(store_name,Â store_service[,Â ...]) | Execution store.  
`StoreDocument`(store_name,Â key,Â value,Â ...) | Model representing a Store.  
`KeyDocument`(store_name,Â key,Â value,Â _id,Â ...) | Model representing a key in the store.  
`KeyPolicy`(value) | Defines the eviction policy for a key in the execution store.  
  
class fiftyone.operators.store.ExecutionStoreService(_repo : [ExecutionStoreRepo](api__fiftyone.factory.repos.execution_store.md#fiftyone.factory.repos.execution_store.ExecutionStoreRepo "fiftyone.factory.repos.execution_store.ExecutionStoreRepo") | None = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _collection_name : str = None_, _notification_service : [ChangeStreamNotificationService](api__fiftyone.operators.store.notification_service.md#fiftyone.operators.store.notification_service.ChangeStreamNotificationService "fiftyone.operators.store.notification_service.ChangeStreamNotificationService") | None = None_)#
    

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
    

KeyDocument

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

class fiftyone.operators.store.ExecutionStore(_store_name : str_, _store_service : [ExecutionStoreService](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService "fiftyone.operators.store.service.ExecutionStoreService")_, _default_policy : str = 'persist'_)#
    

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
  
static create(_store_name : str_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _default_policy : str = 'persist'_, _collection_name : str | None = None_) → [ExecutionStore](api__fiftyone.operators.store.store.md#fiftyone.operators.store.store.ExecutionStore "fiftyone.operators.store.store.ExecutionStore")#
    

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

class fiftyone.operators.store.StoreDocument(_store_name : str_, _key : str = '__store__'_, _value : dict[str_, _~typing.Any] | None=None_, __id : Any | None = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _created_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") = <factory>_, _updated_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None_, _expires_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None_, _policy : [KeyPolicy](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy "fiftyone.operators.store.models.KeyPolicy") = KeyPolicy.PERSIST_)#
    

Bases: [`KeyDocument`](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")

Model representing a Store.

**Attributes:**

`key` |   
---|---  
`value` |   
`metadata` | The metadata associated with the store.  
`dataset_id` |   
`expires_at` |   
`policy` |   
`updated_at` |   
`store_name` |   
`created_at` |   
  
**Methods:**

`from_dict`(doc) | Creates a KeyDocument from a dictionary.  
---|---  
`get_expiration`(ttl) | Gets the expiration date for a key with the given TTL.  
`to_mongo_dict`([exclude_id]) | Serializes the document to a MongoDB dictionary.  
  
key: str = '__store__'#
    

value: dict[str, Any] | None = None#
    

property metadata: dict[str, Any]#
    

The metadata associated with the store.

dataset_id: [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None#
    

expires_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

classmethod from_dict(_doc : dict[str, Any]_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Creates a KeyDocument from a dictionary.

static get_expiration(_ttl : int | None_) → [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

Gets the expiration date for a key with the given TTL.

policy: [KeyPolicy](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy "fiftyone.operators.store.models.KeyPolicy") = 'persist'#
    

to_mongo_dict(_exclude_id : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → dict[str, Any]#
    

Serializes the document to a MongoDB dictionary.

updated_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

store_name: str#
    

created_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

class fiftyone.operators.store.KeyDocument(_store_name : str_, _key : str_, _value : Any_, __id : Any | None = None_, _dataset_id : [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None_, _created_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") = <factory>_, _updated_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None_, _expires_at : [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None_, _policy : [KeyPolicy](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy "fiftyone.operators.store.models.KeyPolicy") = KeyPolicy.PERSIST_)#
    

Bases: `object`

Model representing a key in the store.

**Attributes:**

`store_name` |   
---|---  
`key` |   
`value` |   
`dataset_id` |   
`created_at` |   
`updated_at` |   
`expires_at` |   
`policy` |   
  
**Methods:**

`get_expiration`(ttl) | Gets the expiration date for a key with the given TTL.  
---|---  
`from_dict`(doc) | Creates a KeyDocument from a dictionary.  
`to_mongo_dict`([exclude_id]) | Serializes the document to a MongoDB dictionary.  
  
store_name: str#
    

key: str#
    

value: Any#
    

dataset_id: [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)") | None = None#
    

created_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime")#
    

updated_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

expires_at: [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None = None#
    

policy: [KeyPolicy](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyPolicy "fiftyone.operators.store.models.KeyPolicy") = 'persist'#
    

static get_expiration(_ttl : int | None_) → [datetime](api__fiftyone.utils.data.md#fiftyone.utils.data.datetime "datetime.datetime") | None#
    

Gets the expiration date for a key with the given TTL.

classmethod from_dict(_doc : dict[str, Any]_) → [KeyDocument](api__fiftyone.operators.store.models.md#fiftyone.operators.store.models.KeyDocument "fiftyone.operators.store.models.KeyDocument")#
    

Creates a KeyDocument from a dictionary.

to_mongo_dict(_exclude_id : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → dict[str, Any]#
    

Serializes the document to a MongoDB dictionary.

class fiftyone.operators.store.KeyPolicy(_value_)#
    

Bases: `str`, `Enum`

Defines the eviction policy for a key in the execution store.

  * `PERSIST`: The key is stored persistently and will never be automatically removed. It must be explicitly deleted.

  * `EVICT`: The key is considered cacheable and may be removed automatically if a TTL is set, or manually via `clear_cache()`.




**Attributes:**

`PERSIST` |   
---|---  
`EVICT` |   
  
**Methods:**

`encode`([encoding,Â errors]) | Encode the string using the codec registered for encoding.  
---|---  
`replace`(old,Â new[,Â count]) | Return a copy with all occurrences of substring old replaced by new.  
`split`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`rsplit`([sep,Â maxsplit]) | Return a list of the substrings in the string, using sep as the separator string.  
`join`(iterable,Â /) | Concatenate any number of strings.  
`capitalize`() | Return a capitalized version of the string.  
`casefold`() | Return a version of the string suitable for caseless comparisons.  
`title`() | Return a version of the string where each word is titlecased.  
`center`(width[,Â fillchar]) | Return a centered string of length width.  
`count`(sub[,Â start[,Â end]]) | Return the number of non-overlapping occurrences of substring sub in string S[start:end].  
`expandtabs`([tabsize]) | Return a copy where all tab characters are expanded using spaces.  
`find`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`partition`(sep,Â /) | Partition the string into three parts using the given separator.  
`index`(sub[,Â start[,Â end]]) | Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
`ljust`(width[,Â fillchar]) | Return a left-justified string of length width.  
`lower`() | Return a copy of the string converted to lowercase.  
`lstrip`([chars]) | Return a copy of the string with leading whitespace removed.  
`rfind`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rindex`(sub[,Â start[,Â end]]) | Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].  
`rjust`(width[,Â fillchar]) | Return a right-justified string of length width.  
`rstrip`([chars]) | Return a copy of the string with trailing whitespace removed.  
`rpartition`(sep,Â /) | Partition the string into three parts using the given separator.  
`splitlines`([keepends]) | Return a list of the lines in the string, breaking at line boundaries.  
`strip`([chars]) | Return a copy of the string with leading and trailing whitespace removed.  
`swapcase`() | Convert uppercase characters to lowercase and lowercase characters to uppercase.  
`translate`(table,Â /) | Replace each character in the string using the given translation table.  
`upper`() | Return a copy of the string converted to uppercase.  
`startswith`(prefix[,Â start[,Â end]]) | Return True if S starts with the specified prefix, False otherwise.  
`endswith`(suffix[,Â start[,Â end]]) | Return True if S ends with the specified suffix, False otherwise.  
`removeprefix`(prefix,Â /) | Return a str with the given prefix string removed if present.  
`removesuffix`(suffix,Â /) | Return a str with the given suffix string removed if present.  
`isascii`() | Return True if all characters in the string are ASCII, False otherwise.  
`islower`() | Return True if the string is a lowercase string, False otherwise.  
`isupper`() | Return True if the string is an uppercase string, False otherwise.  
`istitle`() | Return True if the string is a title-cased string, False otherwise.  
`isspace`() | Return True if the string is a whitespace string, False otherwise.  
`isdecimal`() | Return True if the string is a decimal string, False otherwise.  
`isdigit`() | Return True if the string is a digit string, False otherwise.  
`isnumeric`() | Return True if the string is a numeric string, False otherwise.  
`isalpha`() | Return True if the string is an alphabetic string, False otherwise.  
`isalnum`() | Return True if the string is an alpha-numeric string, False otherwise.  
`isidentifier`() | Return True if the string is a valid Python identifier, False otherwise.  
`isprintable`() | Return True if the string is printable, False otherwise.  
`zfill`(width,Â /) | Pad a numeric string with zeros on the left, to fill a field of the given width.  
`format`(*args,Â **kwargs) | Return a formatted version of S, using substitutions from args and kwargs.  
`format_map`(mapping) | Return a formatted version of S, using substitutions from mapping.  
`maketrans` | Return a translation table usable for str.translate().  
  
PERSIST = 'persist'#
    

EVICT = 'evict'#
    

encode(_encoding ='utf-8'_, _errors ='strict'_)#
    

Encode the string using the codec registered for encoding.

encoding
    

The encoding in which to encode the string.

errors
    

The error handling scheme to use for encoding errors. The default is âstrictâ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are âignoreâ, âreplaceâ and âxmlcharrefreplaceâ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

replace(_old_ , _new_ , _count =-1_, _/_)#
    

Return a copy with all occurrences of substring old replaced by new.

> count
>     
> 
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

split(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

rsplit(_sep =None_, _maxsplit =-1_)#
    

Return a list of the substrings in the string, using sep as the separator string.

> sep
>     
> 
> The separator used to split the string.
> 
> When set to None (the default value), will split on any whitespace character (including n r t f and spaces) and will discard empty strings from the result.
> 
> maxsplit
>     
> 
> Maximum number of splits. -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

join(_iterable_ , _/_)#
    

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: â.â.join([âabâ, âpqâ, ârsâ]) -> âab.pq.rsâ

capitalize()#
    

Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()#
    

Return a version of the string suitable for caseless comparisons.

title()#
    

Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

center(_width_ , _fillchar =' '_, _/_)#
    

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(_sub_[, _start_[, _end_]]) → int#
    

Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

expandtabs(_tabsize =8_)#
    

Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

partition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

index(_sub_[, _start_[, _end_]]) → int#
    

Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

ljust(_width_ , _fillchar =' '_, _/_)#
    

Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()#
    

Return a copy of the string converted to lowercase.

lstrip(_chars =None_, _/_)#
    

Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

rfind(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(_sub_[, _start_[, _end_]]) → int#
    

Return the highest index in S where substring sub is found, such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(_width_ , _fillchar =' '_, _/_)#
    

Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rstrip(_chars =None_, _/_)#
    

Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

rpartition(_sep_ , _/_)#
    

Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

splitlines(_keepends =False_)#
    

Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

strip(_chars =None_, _/_)#
    

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()#
    

Convert uppercase characters to lowercase and lowercase characters to uppercase.

translate(_table_ , _/_)#
    

Replace each character in the string using the given translation table.

> table
>     
> 
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()#
    

Return a copy of the string converted to uppercase.

startswith(_prefix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

endswith(_suffix_[, _start_[, _end_]]) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

removeprefix(_prefix_ , _/_)#
    

Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string.

removesuffix(_suffix_ , _/_)#
    

Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string.

isascii()#
    

Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

islower()#
    

Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isupper()#
    

Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

istitle()#
    

Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isspace()#
    

Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

isdecimal()#
    

Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()#
    

Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isnumeric()#
    

Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isalpha()#
    

Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isalnum()#
    

Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isidentifier()#
    

Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as âdefâ or âclassâ.

isprintable()#
    

Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

zfill(_width_ , _/_)#
    

Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

format(_* args_, _** kwargs_) → str#
    

Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (â{â and â}â).

format_map(_mapping_) → str#
    

Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (â{â and â}â).

static maketrans()#
    

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
