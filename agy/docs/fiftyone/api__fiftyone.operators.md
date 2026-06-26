---
source_url: https://docs.voxel51.com/api/fiftyone.operators.html
---

# fiftyone.operators#

  * [fiftyone.operators.cache](api__fiftyone.operators.cache.md)
    * [fiftyone.operators.cache.decorator](api__fiftyone.operators.cache.decorator.md)
      * [`execution_cache()`](api__fiftyone.operators.cache.decorator.md#fiftyone.operators.cache.decorator.execution_cache)
    * [fiftyone.operators.cache.ephemeral](api__fiftyone.operators.cache.ephemeral.md)
      * [`get_ephemeral_cache()`](api__fiftyone.operators.cache.ephemeral.md#fiftyone.operators.cache.ephemeral.get_ephemeral_cache)
      * [`clear_all_ephemeral_caches()`](api__fiftyone.operators.cache.ephemeral.md#fiftyone.operators.cache.ephemeral.clear_all_ephemeral_caches)
    * [fiftyone.operators.cache.serialization](api__fiftyone.operators.cache.serialization.md)
      * [`auto_serialize()`](api__fiftyone.operators.cache.serialization.md#fiftyone.operators.cache.serialization.auto_serialize)
      * [`auto_deserialize()`](api__fiftyone.operators.cache.serialization.md#fiftyone.operators.cache.serialization.auto_deserialize)
    * [fiftyone.operators.cache.utils](api__fiftyone.operators.cache.utils.md)
      * [`resolve_cache_info()`](api__fiftyone.operators.cache.utils.md#fiftyone.operators.cache.utils.resolve_cache_info)
    * [Module contents](api__fiftyone.operators.cache.md#module-fiftyone.operators.cache)
      * [`execution_cache()`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache)
  * [fiftyone.operators.store](api__fiftyone.operators.store.md)
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
    * [Module contents](api__fiftyone.operators.store.md#module-fiftyone.operators.store)
      * [`ExecutionStoreService`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService)
        * [`ExecutionStoreService.create_store()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.create_store)
        * [`ExecutionStoreService.clear_cache()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.clear_cache)
        * [`ExecutionStoreService.get_store()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.get_store)
        * [`ExecutionStoreService.list_stores()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.list_stores)
        * [`ExecutionStoreService.count_stores()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.count_stores)
        * [`ExecutionStoreService.has_store()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.has_store)
        * [`ExecutionStoreService.delete_store()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.delete_store)
        * [`ExecutionStoreService.set_key()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.set_key)
        * [`ExecutionStoreService.set_cache_key()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.set_cache_key)
        * [`ExecutionStoreService.has_key()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.has_key)
        * [`ExecutionStoreService.get_key()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.get_key)
        * [`ExecutionStoreService.delete_key()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.delete_key)
        * [`ExecutionStoreService.update_ttl()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.update_ttl)
        * [`ExecutionStoreService.list_keys()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.list_keys)
        * [`ExecutionStoreService.count_keys()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.count_keys)
        * [`ExecutionStoreService.cleanup()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.cleanup)
        * [`ExecutionStoreService.has_store_global()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.has_store_global)
        * [`ExecutionStoreService.list_stores_global()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.list_stores_global)
        * [`ExecutionStoreService.count_stores_global()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.count_stores_global)
        * [`ExecutionStoreService.delete_store_global()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.delete_store_global)
        * [`ExecutionStoreService.subscribe()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.subscribe)
        * [`ExecutionStoreService.unsubscribe()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStoreService.unsubscribe)
      * [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore)
        * [`ExecutionStore.create()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.create)
        * [`ExecutionStore.list_stores()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.list_stores)
        * [`ExecutionStore.get()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.get)
        * [`ExecutionStore.set()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.set)
        * [`ExecutionStore.set_cache()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.set_cache)
        * [`ExecutionStore.delete()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.delete)
        * [`ExecutionStore.has()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.has)
        * [`ExecutionStore.clear()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.clear)
        * [`ExecutionStore.clear_cache()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.clear_cache)
        * [`ExecutionStore.update_ttl()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.update_ttl)
        * [`ExecutionStore.update_policy()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.update_policy)
        * [`ExecutionStore.get_metadata()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.get_metadata)
        * [`ExecutionStore.list_keys()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.list_keys)
        * [`ExecutionStore.subscribe()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.subscribe)
        * [`ExecutionStore.unsubscribe()`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore.unsubscribe)
      * [`StoreDocument`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument)
        * [`StoreDocument.key`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.key)
        * [`StoreDocument.value`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.value)
        * [`StoreDocument.metadata`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.metadata)
        * [`StoreDocument.dataset_id`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.dataset_id)
        * [`StoreDocument.expires_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.expires_at)
        * [`StoreDocument.from_dict()`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.from_dict)
        * [`StoreDocument.get_expiration()`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.get_expiration)
        * [`StoreDocument.policy`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.policy)
        * [`StoreDocument.to_mongo_dict()`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.to_mongo_dict)
        * [`StoreDocument.updated_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.updated_at)
        * [`StoreDocument.store_name`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.store_name)
        * [`StoreDocument.created_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.StoreDocument.created_at)
      * [`KeyDocument`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument)
        * [`KeyDocument.store_name`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.store_name)
        * [`KeyDocument.key`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.key)
        * [`KeyDocument.value`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.value)
        * [`KeyDocument.dataset_id`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.dataset_id)
        * [`KeyDocument.created_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.created_at)
        * [`KeyDocument.updated_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.updated_at)
        * [`KeyDocument.expires_at`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.expires_at)
        * [`KeyDocument.policy`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.policy)
        * [`KeyDocument.get_expiration()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.get_expiration)
        * [`KeyDocument.from_dict()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.from_dict)
        * [`KeyDocument.to_mongo_dict()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyDocument.to_mongo_dict)
      * [`KeyPolicy`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy)
        * [`KeyPolicy.PERSIST`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.PERSIST)
        * [`KeyPolicy.EVICT`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.EVICT)
        * [`KeyPolicy.encode()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.encode)
        * [`KeyPolicy.replace()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.replace)
        * [`KeyPolicy.split()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.split)
        * [`KeyPolicy.rsplit()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rsplit)
        * [`KeyPolicy.join()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.join)
        * [`KeyPolicy.capitalize()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.capitalize)
        * [`KeyPolicy.casefold()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.casefold)
        * [`KeyPolicy.title()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.title)
        * [`KeyPolicy.center()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.center)
        * [`KeyPolicy.count()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.count)
        * [`KeyPolicy.expandtabs()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.expandtabs)
        * [`KeyPolicy.find()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.find)
        * [`KeyPolicy.partition()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.partition)
        * [`KeyPolicy.index()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.index)
        * [`KeyPolicy.ljust()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.ljust)
        * [`KeyPolicy.lower()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.lower)
        * [`KeyPolicy.lstrip()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.lstrip)
        * [`KeyPolicy.rfind()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rfind)
        * [`KeyPolicy.rindex()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rindex)
        * [`KeyPolicy.rjust()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rjust)
        * [`KeyPolicy.rstrip()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rstrip)
        * [`KeyPolicy.rpartition()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.rpartition)
        * [`KeyPolicy.splitlines()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.splitlines)
        * [`KeyPolicy.strip()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.strip)
        * [`KeyPolicy.swapcase()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.swapcase)
        * [`KeyPolicy.translate()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.translate)
        * [`KeyPolicy.upper()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.upper)
        * [`KeyPolicy.startswith()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.startswith)
        * [`KeyPolicy.endswith()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.endswith)
        * [`KeyPolicy.removeprefix()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.removeprefix)
        * [`KeyPolicy.removesuffix()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.removesuffix)
        * [`KeyPolicy.isascii()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isascii)
        * [`KeyPolicy.islower()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.islower)
        * [`KeyPolicy.isupper()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isupper)
        * [`KeyPolicy.istitle()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.istitle)
        * [`KeyPolicy.isspace()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isspace)
        * [`KeyPolicy.isdecimal()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isdecimal)
        * [`KeyPolicy.isdigit()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isdigit)
        * [`KeyPolicy.isnumeric()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isnumeric)
        * [`KeyPolicy.isalpha()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isalpha)
        * [`KeyPolicy.isalnum()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isalnum)
        * [`KeyPolicy.isidentifier()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isidentifier)
        * [`KeyPolicy.isprintable()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.isprintable)
        * [`KeyPolicy.zfill()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.zfill)
        * [`KeyPolicy.format()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.format)
        * [`KeyPolicy.format_map()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.format_map)
        * [`KeyPolicy.maketrans()`](api__fiftyone.operators.store.md#fiftyone.operators.store.KeyPolicy.maketrans)



  * [fiftyone.operators.categories](api__fiftyone.operators.categories.md)
    * [`Categories`](api__fiftyone.operators.categories.md#fiftyone.operators.categories.Categories)
      * [`Categories.IMPORT`](api__fiftyone.operators.categories.md#fiftyone.operators.categories.Categories.IMPORT)
      * [`Categories.CURATE`](api__fiftyone.operators.categories.md#fiftyone.operators.categories.Categories.CURATE)
      * [`Categories.ANALYZE`](api__fiftyone.operators.categories.md#fiftyone.operators.categories.Categories.ANALYZE)
      * [`Categories.CUSTOM`](api__fiftyone.operators.categories.md#fiftyone.operators.categories.Categories.CUSTOM)
  * [fiftyone.operators.constants](api__fiftyone.operators.constants.md)
    * [`ViewTarget`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget)
      * [`ViewTarget.BASE_VIEW`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.BASE_VIEW)
      * [`ViewTarget.CURRENT_VIEW`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.CURRENT_VIEW)
      * [`ViewTarget.DATASET`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.DATASET)
      * [`ViewTarget.DATASET_VIEW`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.DATASET_VIEW)
      * [`ViewTarget.SELECTED_LABELS`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.SELECTED_LABELS)
      * [`ViewTarget.SELECTED_SAMPLES`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.SELECTED_SAMPLES)
      * [`ViewTarget.CUSTOM_VIEW_TARGET`](api__fiftyone.operators.constants.md#fiftyone.operators.constants.ViewTarget.CUSTOM_VIEW_TARGET)
  * [fiftyone.operators.decorators](api__fiftyone.operators.decorators.md)
    * [`coroutine_timeout()`](api__fiftyone.operators.decorators.md#fiftyone.operators.decorators.coroutine_timeout)
    * [`timeout()`](api__fiftyone.operators.decorators.md#fiftyone.operators.decorators.timeout)
    * [`raise_timeout_error()`](api__fiftyone.operators.decorators.md#fiftyone.operators.decorators.raise_timeout_error)
    * [`plugins_cache()`](api__fiftyone.operators.decorators.md#fiftyone.operators.decorators.plugins_cache)
    * [`dir_state()`](api__fiftyone.operators.decorators.md#fiftyone.operators.decorators.dir_state)
  * [fiftyone.operators.delegated](api__fiftyone.operators.delegated.md)
    * [`DelegatedOperationService`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService)
      * [`DelegatedOperationService.queue_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.queue_operation)
      * [`DelegatedOperationService.set_progress()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_progress)
      * [`DelegatedOperationService.set_running()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_running)
      * [`DelegatedOperationService.set_scheduled()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_scheduled)
      * [`DelegatedOperationService.set_queued()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_queued)
      * [`DelegatedOperationService.set_completed()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_completed)
      * [`DelegatedOperationService.set_failed()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_failed)
      * [`DelegatedOperationService.set_pinned()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_pinned)
      * [`DelegatedOperationService.set_label()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.set_label)
      * [`DelegatedOperationService.archive_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.archive_operation)
      * [`DelegatedOperationService.unarchive_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.unarchive_operation)
      * [`DelegatedOperationService.delete_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.delete_operation)
      * [`DelegatedOperationService.delete_for_dataset()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.delete_for_dataset)
      * [`DelegatedOperationService.rerun_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.rerun_operation)
      * [`DelegatedOperationService.get_queued_operations()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.get_queued_operations)
      * [`DelegatedOperationService.get_scheduled_operations()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.get_scheduled_operations)
      * [`DelegatedOperationService.get_running_operations()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.get_running_operations)
      * [`DelegatedOperationService.get()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.get)
      * [`DelegatedOperationService.list_operations()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.list_operations)
      * [`DelegatedOperationService.execute_queued_operations()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.execute_queued_operations)
      * [`DelegatedOperationService.count()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.count)
      * [`DelegatedOperationService.execute_operation()`](api__fiftyone.operators.delegated.md#fiftyone.operators.delegated.DelegatedOperationService.execute_operation)
  * [fiftyone.operators.evaluation_metric](api__fiftyone.operators.evaluation_metric.md)
    * [`EvaluationMetricConfig`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetricConfig)
      * [`EvaluationMetricConfig.risk_level`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetricConfig.risk_level)
      * [`EvaluationMetricConfig.to_json()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetricConfig.to_json)
    * [`EvaluationMetric`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric)
      * [`EvaluationMetric.resolve_input()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_input)
      * [`EvaluationMetric.parse_parameters()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.parse_parameters)
      * [`EvaluationMetric.compute()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.compute)
      * [`EvaluationMetric.get_fields()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.get_fields)
      * [`EvaluationMetric.rename()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.rename)
      * [`EvaluationMetric.cleanup()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.cleanup)
      * [`EvaluationMetric.add_secrets()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.add_secrets)
      * [`EvaluationMetric.builtin`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.builtin)
      * [`EvaluationMetric.config`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.config)
      * [`EvaluationMetric.execute()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.execute)
      * [`EvaluationMetric.method_to_uri()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.method_to_uri)
      * [`EvaluationMetric.name`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.name)
      * [`EvaluationMetric.resolve_delegation()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_delegation)
      * [`EvaluationMetric.resolve_execution_options()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_execution_options)
      * [`EvaluationMetric.resolve_output()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_output)
      * [`EvaluationMetric.resolve_placement()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_placement)
      * [`EvaluationMetric.resolve_run_name()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_run_name)
      * [`EvaluationMetric.resolve_type()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.resolve_type)
      * [`EvaluationMetric.risk_level`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.risk_level)
      * [`EvaluationMetric.to_json()`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.to_json)
      * [`EvaluationMetric.uri`](api__fiftyone.operators.evaluation_metric.md#fiftyone.operators.evaluation_metric.EvaluationMetric.uri)
  * [fiftyone.operators.events](api__fiftyone.operators.events.md)
  * [fiftyone.operators.executor](api__fiftyone.operators.executor.md)
    * [`ExecutionRunState`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState)
      * [`ExecutionRunState.SCHEDULED`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.SCHEDULED)
      * [`ExecutionRunState.QUEUED`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.QUEUED)
      * [`ExecutionRunState.RUNNING`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.RUNNING)
      * [`ExecutionRunState.PROCESSING`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.PROCESSING)
      * [`ExecutionRunState.COMPLETED`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.COMPLETED)
      * [`ExecutionRunState.FAILED`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.FAILED)
      * [`ExecutionRunState.TERMINAL_STATES`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionRunState.TERMINAL_STATES)
    * [`InvocationRequest`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.InvocationRequest)
      * [`InvocationRequest.to_json()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.InvocationRequest.to_json)
    * [`ExecutionProgress`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionProgress)
    * [`Executor`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.Executor)
      * [`Executor.trigger()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.Executor.trigger)
      * [`Executor.log()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.Executor.log)
      * [`Executor.to_json()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.Executor.to_json)
    * [`execute_operator()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.execute_operator)
    * [`execute_or_delegate_operator()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.execute_or_delegate_operator)
    * [`prepare_operator_executor()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.prepare_operator_executor)
    * [`do_execute_operator()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.do_execute_operator)
    * [`do_execute_pipeline()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.do_execute_pipeline)
    * [`resolve_type()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.resolve_type)
    * [`resolve_type_with_context()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.resolve_type_with_context)
    * [`resolve_execution_options()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.resolve_execution_options)
    * [`resolve_placement()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.resolve_placement)
    * [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext)
      * [`ExecutionContext.dataset`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.dataset)
      * [`ExecutionContext.dataset_name`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.dataset_name)
      * [`ExecutionContext.dataset_id`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.dataset_id)
      * [`ExecutionContext.view`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.view)
      * [`ExecutionContext.target_view()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.target_view)
      * [`ExecutionContext.view_target()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.view_target)
      * [`ExecutionContext.has_custom_view`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.has_custom_view)
      * [`ExecutionContext.spaces`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.spaces)
      * [`ExecutionContext.selected`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.selected)
      * [`ExecutionContext.selected_samples`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.selected_samples)
      * [`ExecutionContext.sample_selection_style`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.sample_selection_style)
      * [`ExecutionContext.label_selection_style`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.label_selection_style)
      * [`ExecutionContext.selected_labels`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.selected_labels)
      * [`ExecutionContext.extended_selection`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.extended_selection)
      * [`ExecutionContext.current_sample`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.current_sample)
      * [`ExecutionContext.active_fields`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.active_fields)
      * [`ExecutionContext.user_id`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.user_id)
      * [`ExecutionContext.user_request_token`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.user_request_token)
      * [`ExecutionContext.panel_id`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.panel_id)
      * [`ExecutionContext.panel_state`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.panel_state)
      * [`ExecutionContext.panel`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.panel)
      * [`ExecutionContext.delegated`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.delegated)
      * [`ExecutionContext.requesting_delegated_execution`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.requesting_delegated_execution)
      * [`ExecutionContext.delegation_target`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.delegation_target)
      * [`ExecutionContext.results`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.results)
      * [`ExecutionContext.secrets`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.secrets)
      * [`ExecutionContext.ops`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.ops)
      * [`ExecutionContext.group_slice`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.group_slice)
      * [`ExecutionContext.num_distributed_tasks`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.num_distributed_tasks)
      * [`ExecutionContext.query_performance`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.query_performance)
      * [`ExecutionContext.prompt_id`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.prompt_id)
      * [`ExecutionContext.operator_uri`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.operator_uri)
      * [`ExecutionContext.prompt()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.prompt)
      * [`ExecutionContext.secret()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.secret)
      * [`ExecutionContext.resolve_secret_values()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.resolve_secret_values)
      * [`ExecutionContext.trigger()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.trigger)
      * [`ExecutionContext.log()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.log)
      * [`ExecutionContext.set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress)
      * [`ExecutionContext.store()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.store)
      * [`ExecutionContext.serialize()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.serialize)
      * [`ExecutionContext.to_dict()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.to_dict)
    * [`ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult)
      * [`ExecutionResult.is_generator`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult.is_generator)
      * [`ExecutionResult.raise_exceptions()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult.raise_exceptions)
      * [`ExecutionResult.to_exception()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult.to_exception)
      * [`ExecutionResult.to_json()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult.to_json)
    * [`PipelineExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext)
      * [`PipelineExecutionContext.active`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext.active)
      * [`PipelineExecutionContext.curr_stage_index`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext.curr_stage_index)
      * [`PipelineExecutionContext.total_stages`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext.total_stages)
      * [`PipelineExecutionContext.pipeline_errors`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext.pipeline_errors)
      * [`PipelineExecutionContext.num_distributed_tasks`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext.num_distributed_tasks)
    * [`ExecutionError`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionError)
      * [`ExecutionError.add_note()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionError.add_note)
      * [`ExecutionError.args`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionError.args)
      * [`ExecutionError.with_traceback()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionError.with_traceback)
    * [`ValidationError`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationError)
      * [`ValidationError.to_json()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationError.to_json)
    * [`ValidationContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext)
      * [`ValidationContext.to_json()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.to_json)
      * [`ValidationContext.add_error()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.add_error)
      * [`ValidationContext.validate_enum()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.validate_enum)
      * [`ValidationContext.validate_list()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.validate_list)
      * [`ValidationContext.validate_property()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.validate_property)
      * [`ValidationContext.validate_object()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.validate_object)
      * [`ValidationContext.validate_primitive()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.validate_primitive)
      * [`ValidationContext.exists_or_non_required()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ValidationContext.exists_or_non_required)
    * [`ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions)
      * [`ExecutionOptions.allow_immediate_execution`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.allow_immediate_execution)
      * [`ExecutionOptions.allow_delegated_execution`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.allow_delegated_execution)
      * [`ExecutionOptions.allow_distributed_execution`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.allow_distributed_execution)
      * [`ExecutionOptions.default_choice_to_delegated`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.default_choice_to_delegated)
      * [`ExecutionOptions.min_distributed_tasks`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.min_distributed_tasks)
      * [`ExecutionOptions.max_distributed_tasks`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.max_distributed_tasks)
      * [`ExecutionOptions.recommended_distributed_tasks`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.recommended_distributed_tasks)
      * [`ExecutionOptions.available_orchestrators`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.available_orchestrators)
      * [`ExecutionOptions.orchestrator_registration_enabled`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.orchestrator_registration_enabled)
      * [`ExecutionOptions.update()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.update)
      * [`ExecutionOptions.to_dict()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions.to_dict)
  * [fiftyone.operators.message](api__fiftyone.operators.message.md)
    * [`MessageType`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageType)
      * [`MessageType.SUCCESS`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageType.SUCCESS)
      * [`MessageType.ERROR`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageType.ERROR)
    * [`GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage)
      * [`GeneratedMessage.to_json()`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage.to_json)
      * [`GeneratedMessage.to_json_line()`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage.to_json_line)
    * [`MessageMetadata`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageMetadata)
      * [`MessageMetadata.operation_type`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageMetadata.operation_type)
      * [`MessageMetadata.dataset_id`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageMetadata.dataset_id)
      * [`MessageMetadata.timestamp`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageMetadata.timestamp)
    * [`MessageData`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData)
      * [`MessageData.key`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.key)
      * [`MessageData.value`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.value)
      * [`MessageData.metadata`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.metadata)
      * [`MessageData.from_dict()`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.from_dict)
      * [`MessageData.from_json()`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.from_json)
      * [`MessageData.to_dict()`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.to_dict)
      * [`MessageData.to_json()`](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData.to_json)
  * [fiftyone.operators.operations](api__fiftyone.operators.operations.md)
    * [`Operations`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations)
      * [`Operations.clone_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clone_selected_samples)
      * [`Operations.clone_sample_field()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clone_sample_field)
      * [`Operations.rename_sample_field()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.rename_sample_field)
      * [`Operations.clear_sample_field()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_sample_field)
      * [`Operations.delete_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.delete_selected_samples)
      * [`Operations.delete_selected_labels()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.delete_selected_labels)
      * [`Operations.delete_sample_field()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.delete_sample_field)
      * [`Operations.print_stdout()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.print_stdout)
      * [`Operations.list_files()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.list_files)
      * [`Operations.reload_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.reload_samples)
      * [`Operations.reload_dataset()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.reload_dataset)
      * [`Operations.clear_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_selected_samples)
      * [`Operations.copy_view_as_json()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.copy_view_as_json)
      * [`Operations.view_from_json()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.view_from_json)
      * [`Operations.clear_panel_state()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_panel_state)
      * [`Operations.clear_panel_data()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_panel_data)
      * [`Operations.set_panel_state()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_panel_state)
      * [`Operations.set_panel_data()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_panel_data)
      * [`Operations.patch_panel_state()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.patch_panel_state)
      * [`Operations.patch_panel_data()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.patch_panel_data)
      * [`Operations.reduce_panel_state()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.reduce_panel_state)
      * [`Operations.apply_panel_state_path()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.apply_panel_state_path)
      * [`Operations.show_panel_output()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_panel_output)
      * [`Operations.open_panel()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.open_panel)
      * [`Operations.register_panel()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.register_panel)
      * [`Operations.open_all_panels()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.open_all_panels)
      * [`Operations.close_panel()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.close_panel)
      * [`Operations.close_all_panels()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.close_all_panels)
      * [`Operations.split_panel()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.split_panel)
      * [`Operations.open_dataset()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.open_dataset)
      * [`Operations.clear_view()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_view)
      * [`Operations.clear_sidebar_filters()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_sidebar_filters)
      * [`Operations.clear_all_stages()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_all_stages)
      * [`Operations.refresh_colors()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.refresh_colors)
      * [`Operations.show_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_selected_samples)
      * [`Operations.convert_extended_selection_to_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.convert_extended_selection_to_selected_samples)
      * [`Operations.set_selected_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_selected_samples)
      * [`Operations.set_sample_selection_style()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_sample_selection_style)
      * [`Operations.clear_sample_selection_style()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_sample_selection_style)
      * [`Operations.set_label_selection_style()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_label_selection_style)
      * [`Operations.clear_label_selection_style()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_label_selection_style)
      * [`Operations.set_view()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_view)
      * [`Operations.show_samples()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_samples)
      * [`Operations.console_log()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.console_log)
      * [`Operations.show_output()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_output)
      * [`Operations.set_progress()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_progress)
      * [`Operations.test_operator()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.test_operator)
      * [`Operations.set_selected_labels()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_selected_labels)
      * [`Operations.clear_selected_labels()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_selected_labels)
      * [`Operations.notify()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.notify)
      * [`Operations.set_extended_selection()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_extended_selection)
      * [`Operations.set_spaces()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_spaces)
      * [`Operations.set_active_fields()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_active_fields)
      * [`Operations.clear_active_fields()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.clear_active_fields)
      * [`Operations.track_event()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.track_event)
      * [`Operations.set_panel_title()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_panel_title)
      * [`Operations.set_group_slice()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.set_group_slice)
      * [`Operations.open_sample()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.open_sample)
      * [`Operations.close_sample()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.close_sample)
      * [`Operations.show_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.show_sidebar)
      * [`Operations.hide_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.hide_sidebar)
      * [`Operations.toggle_sidebar()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.toggle_sidebar)
      * [`Operations.browser_download()`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations.browser_download)
  * [fiftyone.operators.operator](api__fiftyone.operators.operator.md)
    * [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig)
      * [`OperatorConfig.risk_level`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig.risk_level)
      * [`OperatorConfig.to_json()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig.to_json)
    * [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator)
      * [`Operator.name`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.name)
      * [`Operator.uri`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.uri)
      * [`Operator.builtin`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.builtin)
      * [`Operator.config`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.config)
      * [`Operator.risk_level`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.risk_level)
      * [`Operator.resolve_delegation()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_delegation)
      * [`Operator.resolve_execution_options()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_execution_options)
      * [`Operator.execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute)
      * [`Operator.resolve_type()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_type)
      * [`Operator.resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input)
      * [`Operator.resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_output)
      * [`Operator.resolve_placement()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_placement)
      * [`Operator.resolve_run_name()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_run_name)
      * [`Operator.method_to_uri()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.method_to_uri)
      * [`Operator.to_json()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.to_json)
      * [`Operator.add_secrets()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.add_secrets)
    * [`PipelineOperator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator)
      * [`PipelineOperator.resolve_pipeline()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_pipeline)
      * [`PipelineOperator.add_secrets()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.add_secrets)
      * [`PipelineOperator.builtin`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.builtin)
      * [`PipelineOperator.config`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.config)
      * [`PipelineOperator.execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.execute)
      * [`PipelineOperator.method_to_uri()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.method_to_uri)
      * [`PipelineOperator.name`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.name)
      * [`PipelineOperator.resolve_delegation()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_delegation)
      * [`PipelineOperator.resolve_execution_options()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_execution_options)
      * [`PipelineOperator.resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_input)
      * [`PipelineOperator.resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_output)
      * [`PipelineOperator.resolve_placement()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_placement)
      * [`PipelineOperator.resolve_run_name()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_run_name)
      * [`PipelineOperator.resolve_type()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.resolve_type)
      * [`PipelineOperator.risk_level`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.risk_level)
      * [`PipelineOperator.to_json()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.to_json)
      * [`PipelineOperator.uri`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.PipelineOperator.uri)
  * [fiftyone.operators.panel](api__fiftyone.operators.panel.md)
    * [`PanelConfig`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelConfig)
      * [`PanelConfig.to_json()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelConfig.to_json)
      * [`PanelConfig.risk_level`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelConfig.risk_level)
    * [`Panel`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel)
      * [`Panel.render()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.render)
      * [`Panel.resolve_input()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_input)
      * [`Panel.on_startup()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.on_startup)
      * [`Panel.on_load()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.on_load)
      * [`Panel.execute()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.execute)
      * [`Panel.add_secrets()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.add_secrets)
      * [`Panel.builtin`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.builtin)
      * [`Panel.config`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.config)
      * [`Panel.method_to_uri()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.method_to_uri)
      * [`Panel.name`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.name)
      * [`Panel.resolve_delegation()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_delegation)
      * [`Panel.resolve_execution_options()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_execution_options)
      * [`Panel.resolve_output()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_output)
      * [`Panel.resolve_placement()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_placement)
      * [`Panel.resolve_run_name()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_run_name)
      * [`Panel.resolve_type()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.resolve_type)
      * [`Panel.risk_level`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.risk_level)
      * [`Panel.to_json()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.to_json)
      * [`Panel.uri`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.uri)
    * [`WriteOnlyError`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.WriteOnlyError)
      * [`WriteOnlyError.add_note()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.WriteOnlyError.add_note)
      * [`WriteOnlyError.args`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.WriteOnlyError.args)
      * [`WriteOnlyError.with_traceback()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.WriteOnlyError.with_traceback)
    * [`PanelRefBase`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefBase)
      * [`PanelRefBase.set()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefBase.set)
      * [`PanelRefBase.get()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefBase.get)
      * [`PanelRefBase.clear()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefBase.clear)
    * [`PanelRefState`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefState)
      * [`PanelRefState.set()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefState.set)
      * [`PanelRefState.clear()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefState.clear)
      * [`PanelRefState.apply()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefState.apply)
      * [`PanelRefState.get()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefState.get)
    * [`PanelRefData`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefData)
      * [`PanelRefData.set()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefData.set)
      * [`PanelRefData.get()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefData.get)
      * [`PanelRefData.clear()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRefData.clear)
    * [`PanelRef`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef)
      * [`PanelRef.data`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.data)
      * [`PanelRef.state`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.state)
      * [`PanelRef.id`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.id)
      * [`PanelRef.close()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.close)
      * [`PanelRef.set_state()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.set_state)
      * [`PanelRef.get_state()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.get_state)
      * [`PanelRef.set_data()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.set_data)
      * [`PanelRef.set_title()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef.set_title)
  * [fiftyone.operators.permissions](api__fiftyone.operators.permissions.md)
    * [`ManagedOperators`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.ManagedOperators)
      * [`ManagedOperators.has_operator()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.ManagedOperators.has_operator)
      * [`ManagedOperators.for_request()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.ManagedOperators.for_request)
    * [`PermissionedOperatorRegistry`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry)
      * [`PermissionedOperatorRegistry.can_execute()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.can_execute)
      * [`PermissionedOperatorRegistry.from_list_request()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.from_list_request)
      * [`PermissionedOperatorRegistry.from_exec_request()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.from_exec_request)
      * [`PermissionedOperatorRegistry.get_operator()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.get_operator)
      * [`PermissionedOperatorRegistry.list_errors()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.list_errors)
      * [`PermissionedOperatorRegistry.list_operators()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.list_operators)
      * [`PermissionedOperatorRegistry.operator_exists()`](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry.operator_exists)
  * [fiftyone.operators.registry](api__fiftyone.operators.registry.md)
    * [`get_operator()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.get_operator)
    * [`list_operators()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.list_operators)
    * [`operator_exists()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.operator_exists)
    * [`OperatorRegistry`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry)
      * [`OperatorRegistry.list_operators()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry.list_operators)
      * [`OperatorRegistry.list_errors()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry.list_errors)
      * [`OperatorRegistry.operator_exists()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry.operator_exists)
      * [`OperatorRegistry.can_execute()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry.can_execute)
      * [`OperatorRegistry.get_operator()`](api__fiftyone.operators.registry.md#fiftyone.operators.registry.OperatorRegistry.get_operator)
  * [fiftyone.operators.remote_notifier](api__fiftyone.operators.remote_notifier.md)
    * [`RemoteNotifier`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.RemoteNotifier)
      * [`RemoteNotifier.broadcast_to_store()`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.RemoteNotifier.broadcast_to_store)
    * [`SseNotifier`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.SseNotifier)
      * [`SseNotifier.broadcast_to_store()`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.SseNotifier.broadcast_to_store)
      * [`SseNotifier.get_event_source_response()`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.SseNotifier.get_event_source_response)
      * [`SseNotifier.sync_current_state_for_client()`](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.SseNotifier.sync_current_state_for_client)
  * [fiftyone.operators.server](api__fiftyone.operators.server.md)
    * [`get_operators()`](api__fiftyone.operators.server.md#fiftyone.operators.server.get_operators)
    * [`ListOperators`](api__fiftyone.operators.server.md#fiftyone.operators.server.ListOperators)
      * [`ListOperators.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ListOperators.post)
      * [`ListOperators.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ListOperators.dispatch)
      * [`ListOperators.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ListOperators.method_not_allowed)
    * [`ResolvePlacements`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolvePlacements)
      * [`ResolvePlacements.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolvePlacements.post)
      * [`ResolvePlacements.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolvePlacements.dispatch)
      * [`ResolvePlacements.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolvePlacements.method_not_allowed)
    * [`ExecuteOperator`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperator)
      * [`ExecuteOperator.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperator.post)
      * [`ExecuteOperator.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperator.dispatch)
      * [`ExecuteOperator.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperator.method_not_allowed)
    * [`create_response_generator()`](api__fiftyone.operators.server.md#fiftyone.operators.server.create_response_generator)
    * [`create_response_async_generator()`](api__fiftyone.operators.server.md#fiftyone.operators.server.create_response_async_generator)
    * [`create_permission_error()`](api__fiftyone.operators.server.md#fiftyone.operators.server.create_permission_error)
    * [`ExecuteOperatorAsGenerator`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperatorAsGenerator)
      * [`ExecuteOperatorAsGenerator.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperatorAsGenerator.post)
      * [`ExecuteOperatorAsGenerator.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperatorAsGenerator.dispatch)
      * [`ExecuteOperatorAsGenerator.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ExecuteOperatorAsGenerator.method_not_allowed)
    * [`ResolveType`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveType)
      * [`ResolveType.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveType.post)
      * [`ResolveType.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveType.dispatch)
      * [`ResolveType.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveType.method_not_allowed)
    * [`ResolveExecutionOptions`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveExecutionOptions)
      * [`ResolveExecutionOptions.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveExecutionOptions.post)
      * [`ResolveExecutionOptions.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveExecutionOptions.dispatch)
      * [`ResolveExecutionOptions.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.ResolveExecutionOptions.method_not_allowed)
    * [`SubscribeToExecutionStoreAsOperator`](api__fiftyone.operators.server.md#fiftyone.operators.server.SubscribeToExecutionStoreAsOperator)
      * [`SubscribeToExecutionStoreAsOperator.post()`](api__fiftyone.operators.server.md#fiftyone.operators.server.SubscribeToExecutionStoreAsOperator.post)
      * [`SubscribeToExecutionStoreAsOperator.dispatch()`](api__fiftyone.operators.server.md#fiftyone.operators.server.SubscribeToExecutionStoreAsOperator.dispatch)
      * [`SubscribeToExecutionStoreAsOperator.method_not_allowed()`](api__fiftyone.operators.server.md#fiftyone.operators.server.SubscribeToExecutionStoreAsOperator.method_not_allowed)
  * [fiftyone.operators.sse](api__fiftyone.operators.sse.md)
    * [`SseOperatorConfig`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperatorConfig)
      * [`SseOperatorConfig.risk_level`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperatorConfig.risk_level)
      * [`SseOperatorConfig.to_json()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperatorConfig.to_json)
    * [`SseOperator`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator)
      * [`SseOperator.IS_SSE_OPERATOR`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.IS_SSE_OPERATOR)
      * [`SseOperator.subscription_config`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.subscription_config)
      * [`SseOperator.config`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.config)
      * [`SseOperator.execute()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.execute)
      * [`SseOperator.add_secrets()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.add_secrets)
      * [`SseOperator.builtin`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.builtin)
      * [`SseOperator.method_to_uri()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.method_to_uri)
      * [`SseOperator.name`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.name)
      * [`SseOperator.resolve_delegation()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_delegation)
      * [`SseOperator.resolve_execution_options()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_execution_options)
      * [`SseOperator.resolve_input()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_input)
      * [`SseOperator.resolve_output()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_output)
      * [`SseOperator.resolve_placement()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_placement)
      * [`SseOperator.resolve_run_name()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_run_name)
      * [`SseOperator.resolve_type()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.resolve_type)
      * [`SseOperator.risk_level`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.risk_level)
      * [`SseOperator.to_json()`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.to_json)
      * [`SseOperator.uri`](api__fiftyone.operators.sse.md#fiftyone.operators.sse.SseOperator.uri)
  * [fiftyone.operators.types](api__fiftyone.operators.types.md)
    * [`Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline)
      * [`Pipeline.stages`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline.stages)
      * [`Pipeline.stage()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline.stage)
      * [`Pipeline.from_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline.from_json)
      * [`Pipeline.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline.to_json)
    * [`PipelineRunInfo`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo)
      * [`PipelineRunInfo.active`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.active)
      * [`PipelineRunInfo.expected_children`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.expected_children)
      * [`PipelineRunInfo.stage_index`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.stage_index)
      * [`PipelineRunInfo.child_errors`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.child_errors)
      * [`PipelineRunInfo.from_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.from_json)
      * [`PipelineRunInfo.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineRunInfo.to_json)
    * [`PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage)
      * [`PipelineStage.operator_uri`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.operator_uri)
      * [`PipelineStage.always_run`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.always_run)
      * [`PipelineStage.name`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.name)
      * [`PipelineStage.num_distributed_tasks`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.num_distributed_tasks)
      * [`PipelineStage.params`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.params)
      * [`PipelineStage.rerunnable`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.rerunnable)
      * [`PipelineStage.request_params_overrides`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.request_params_overrides)
      * [`PipelineStage.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage.to_json)
    * [`dedent()`](api__fiftyone.operators.types.md#fiftyone.operators.types.dedent)
    * [`BaseType`](api__fiftyone.operators.types.md#fiftyone.operators.types.BaseType)
      * [`BaseType.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.BaseType.to_json)
    * [`Void`](api__fiftyone.operators.types.md#fiftyone.operators.types.Void)
      * [`Void.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Void.to_json)
    * [`Object`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object)
      * [`Object.add_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.add_property)
      * [`Object.get_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.get_property)
      * [`Object.define_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.define_property)
      * [`Object.str()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.str)
      * [`Object.bool()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.bool)
      * [`Object.int()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.int)
      * [`Object.float()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.float)
      * [`Object.enum()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.enum)
      * [`Object.list()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.list)
      * [`Object.obj()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.obj)
      * [`Object.file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.file)
      * [`Object.uploaded_file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.uploaded_file)
      * [`Object.view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.view)
      * [`Object.loader()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.loader)
      * [`Object.btn()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.btn)
      * [`Object.img()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.img)
      * [`Object.message()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.message)
      * [`Object.grid()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.grid)
      * [`Object.dashboard()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.dashboard)
      * [`Object.plot()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.plot)
      * [`Object.h_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.h_stack)
      * [`Object.v_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.v_stack)
      * [`Object.menu()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.menu)
      * [`Object.btn_group()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.btn_group)
      * [`Object.md()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.md)
      * [`Object.media_player()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.media_player)
      * [`Object.arrow_nav()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.arrow_nav)
      * [`Object.map()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.map)
      * [`Object.oneof()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.oneof)
      * [`Object.tuple()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.tuple)
      * [`Object.tree()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.tree)
      * [`Object.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.clone)
      * [`Object.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.view_target)
      * [`Object.target_view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.target_view)
      * [`Object.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.to_json)
    * [`Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property)
      * [`Property.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property.to_json)
    * [`ResolvableProperty`](api__fiftyone.operators.types.md#fiftyone.operators.types.ResolvableProperty)
      * [`ResolvableProperty.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ResolvableProperty.to_json)
    * [`String`](api__fiftyone.operators.types.md#fiftyone.operators.types.String)
      * [`String.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.String.to_json)
    * [`Boolean`](api__fiftyone.operators.types.md#fiftyone.operators.types.Boolean)
      * [`Boolean.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Boolean.to_json)
    * [`Number`](api__fiftyone.operators.types.md#fiftyone.operators.types.Number)
      * [`Number.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Number.to_json)
    * [`List`](api__fiftyone.operators.types.md#fiftyone.operators.types.List)
      * [`List.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.List.to_json)
    * [`SampleID`](api__fiftyone.operators.types.md#fiftyone.operators.types.SampleID)
      * [`SampleID.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SampleID.to_json)
    * [`Enum`](api__fiftyone.operators.types.md#fiftyone.operators.types.Enum)
      * [`Enum.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Enum.to_json)
    * [`OneOf`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOf)
      * [`OneOf.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOf.to_json)
    * [`Tuple`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tuple)
      * [`Tuple.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tuple.to_json)
    * [`Tree`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tree)
      * [`Tree.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tree.to_json)
    * [`Map`](api__fiftyone.operators.types.md#fiftyone.operators.types.Map)
      * [`Map.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Map.to_json)
    * [`File`](api__fiftyone.operators.types.md#fiftyone.operators.types.File)
      * [`File.add_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.add_property)
      * [`File.arrow_nav()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.arrow_nav)
      * [`File.bool()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.bool)
      * [`File.btn()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.btn)
      * [`File.btn_group()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.btn_group)
      * [`File.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.clone)
      * [`File.dashboard()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.dashboard)
      * [`File.define_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.define_property)
      * [`File.enum()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.enum)
      * [`File.file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.file)
      * [`File.float()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.float)
      * [`File.get_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.get_property)
      * [`File.grid()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.grid)
      * [`File.h_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.h_stack)
      * [`File.img()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.img)
      * [`File.int()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.int)
      * [`File.list()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.list)
      * [`File.loader()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.loader)
      * [`File.map()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.map)
      * [`File.md()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.md)
      * [`File.media_player()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.media_player)
      * [`File.menu()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.menu)
      * [`File.message()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.message)
      * [`File.obj()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.obj)
      * [`File.oneof()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.oneof)
      * [`File.plot()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.plot)
      * [`File.str()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.str)
      * [`File.target_view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.target_view)
      * [`File.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.to_json)
      * [`File.tree()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.tree)
      * [`File.tuple()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.tuple)
      * [`File.uploaded_file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.uploaded_file)
      * [`File.v_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.v_stack)
      * [`File.view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.view)
      * [`File.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.File.view_target)
    * [`UploadedFile`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile)
      * [`UploadedFile.add_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.add_property)
      * [`UploadedFile.arrow_nav()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.arrow_nav)
      * [`UploadedFile.bool()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.bool)
      * [`UploadedFile.btn()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.btn)
      * [`UploadedFile.btn_group()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.btn_group)
      * [`UploadedFile.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.clone)
      * [`UploadedFile.dashboard()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.dashboard)
      * [`UploadedFile.define_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.define_property)
      * [`UploadedFile.enum()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.enum)
      * [`UploadedFile.file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.file)
      * [`UploadedFile.float()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.float)
      * [`UploadedFile.get_property()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.get_property)
      * [`UploadedFile.grid()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.grid)
      * [`UploadedFile.h_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.h_stack)
      * [`UploadedFile.img()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.img)
      * [`UploadedFile.int()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.int)
      * [`UploadedFile.list()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.list)
      * [`UploadedFile.loader()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.loader)
      * [`UploadedFile.map()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.map)
      * [`UploadedFile.md()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.md)
      * [`UploadedFile.media_player()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.media_player)
      * [`UploadedFile.menu()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.menu)
      * [`UploadedFile.message()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.message)
      * [`UploadedFile.obj()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.obj)
      * [`UploadedFile.oneof()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.oneof)
      * [`UploadedFile.plot()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.plot)
      * [`UploadedFile.str()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.str)
      * [`UploadedFile.target_view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.target_view)
      * [`UploadedFile.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.to_json)
      * [`UploadedFile.tree()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.tree)
      * [`UploadedFile.tuple()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.tuple)
      * [`UploadedFile.uploaded_file()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.uploaded_file)
      * [`UploadedFile.v_stack()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.v_stack)
      * [`UploadedFile.view()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.view)
      * [`UploadedFile.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.UploadedFile.view_target)
    * [`View`](api__fiftyone.operators.types.md#fiftyone.operators.types.View)
      * [`View.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.View.clone)
      * [`View.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.View.kwargs_to_json)
      * [`View.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.View.to_json)
    * [`InferredView`](api__fiftyone.operators.types.md#fiftyone.operators.types.InferredView)
      * [`InferredView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.InferredView.clone)
      * [`InferredView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.InferredView.kwargs_to_json)
      * [`InferredView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.InferredView.to_json)
    * [`Form`](api__fiftyone.operators.types.md#fiftyone.operators.types.Form)
      * [`Form.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Form.to_json)
      * [`Form.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Form.clone)
      * [`Form.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Form.kwargs_to_json)
    * [`ReadOnlyView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ReadOnlyView)
      * [`ReadOnlyView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ReadOnlyView.clone)
      * [`ReadOnlyView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ReadOnlyView.kwargs_to_json)
      * [`ReadOnlyView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ReadOnlyView.to_json)
    * [`Choice`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choice)
      * [`Choice.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choice.clone)
      * [`Choice.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choice.to_json)
      * [`Choice.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choice.kwargs_to_json)
    * [`Choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices)
      * [`Choices.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.choices)
      * [`Choices.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.values)
      * [`Choices.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.add_choice)
      * [`Choices.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.append)
      * [`Choices.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.clone)
      * [`Choices.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.to_json)
      * [`Choices.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Choices.kwargs_to_json)
    * [`RadioGroup`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup)
      * [`RadioGroup.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.to_json)
      * [`RadioGroup.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.add_choice)
      * [`RadioGroup.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.append)
      * [`RadioGroup.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.choices)
      * [`RadioGroup.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.clone)
      * [`RadioGroup.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.kwargs_to_json)
      * [`RadioGroup.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup.values)
    * [`Dropdown`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown)
      * [`Dropdown.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.add_choice)
      * [`Dropdown.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.append)
      * [`Dropdown.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.choices)
      * [`Dropdown.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.clone)
      * [`Dropdown.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.kwargs_to_json)
      * [`Dropdown.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.to_json)
      * [`Dropdown.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Dropdown.values)
    * [`Notice`](api__fiftyone.operators.types.md#fiftyone.operators.types.Notice)
      * [`Notice.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Notice.clone)
      * [`Notice.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Notice.kwargs_to_json)
      * [`Notice.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Notice.to_json)
    * [`Header`](api__fiftyone.operators.types.md#fiftyone.operators.types.Header)
      * [`Header.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Header.clone)
      * [`Header.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Header.kwargs_to_json)
      * [`Header.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Header.to_json)
    * [`Warning`](api__fiftyone.operators.types.md#fiftyone.operators.types.Warning)
      * [`Warning.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Warning.clone)
      * [`Warning.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Warning.kwargs_to_json)
      * [`Warning.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Warning.to_json)
    * [`Error`](api__fiftyone.operators.types.md#fiftyone.operators.types.Error)
      * [`Error.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Error.clone)
      * [`Error.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Error.kwargs_to_json)
      * [`Error.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Error.to_json)
    * [`Button`](api__fiftyone.operators.types.md#fiftyone.operators.types.Button)
      * [`Button.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Button.to_json)
      * [`Button.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Button.clone)
      * [`Button.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Button.kwargs_to_json)
    * [`OperatorExecutionButtonView`](api__fiftyone.operators.types.md#fiftyone.operators.types.OperatorExecutionButtonView)
      * [`OperatorExecutionButtonView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OperatorExecutionButtonView.clone)
      * [`OperatorExecutionButtonView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OperatorExecutionButtonView.kwargs_to_json)
      * [`OperatorExecutionButtonView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OperatorExecutionButtonView.to_json)
    * [`OneOfView`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOfView)
      * [`OneOfView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOfView.to_json)
      * [`OneOfView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOfView.clone)
      * [`OneOfView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OneOfView.kwargs_to_json)
    * [`ListView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ListView)
      * [`ListView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ListView.to_json)
      * [`ListView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ListView.clone)
      * [`ListView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ListView.kwargs_to_json)
    * [`TupleView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TupleView)
      * [`TupleView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TupleView.to_json)
      * [`TupleView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TupleView.clone)
      * [`TupleView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TupleView.kwargs_to_json)
    * [`TreeSelectionView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TreeSelectionView)
      * [`TreeSelectionView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TreeSelectionView.to_json)
      * [`TreeSelectionView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TreeSelectionView.clone)
      * [`TreeSelectionView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TreeSelectionView.kwargs_to_json)
    * [`CodeView`](api__fiftyone.operators.types.md#fiftyone.operators.types.CodeView)
      * [`CodeView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CodeView.to_json)
      * [`CodeView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CodeView.clone)
      * [`CodeView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CodeView.kwargs_to_json)
    * [`ColorView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ColorView)
      * [`ColorView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ColorView.to_json)
      * [`ColorView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ColorView.clone)
      * [`ColorView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ColorView.kwargs_to_json)
    * [`TabsView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView)
      * [`TabsView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.to_json)
      * [`TabsView.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.add_choice)
      * [`TabsView.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.append)
      * [`TabsView.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.choices)
      * [`TabsView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.clone)
      * [`TabsView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.kwargs_to_json)
      * [`TabsView.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView.values)
    * [`JSONView`](api__fiftyone.operators.types.md#fiftyone.operators.types.JSONView)
      * [`JSONView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.JSONView.clone)
      * [`JSONView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.JSONView.kwargs_to_json)
      * [`JSONView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.JSONView.to_json)
    * [`AutocompleteView`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView)
      * [`AutocompleteView.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.add_choice)
      * [`AutocompleteView.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.append)
      * [`AutocompleteView.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.choices)
      * [`AutocompleteView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.clone)
      * [`AutocompleteView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.kwargs_to_json)
      * [`AutocompleteView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.to_json)
      * [`AutocompleteView.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView.values)
    * [`FileView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView)
      * [`FileView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView.clone)
      * [`FileView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView.kwargs_to_json)
      * [`FileView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView.to_json)
    * [`LinkView`](api__fiftyone.operators.types.md#fiftyone.operators.types.LinkView)
      * [`LinkView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LinkView.to_json)
      * [`LinkView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LinkView.clone)
      * [`LinkView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LinkView.kwargs_to_json)
    * [`HiddenView`](api__fiftyone.operators.types.md#fiftyone.operators.types.HiddenView)
      * [`HiddenView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HiddenView.clone)
      * [`HiddenView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HiddenView.kwargs_to_json)
      * [`HiddenView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HiddenView.to_json)
    * [`LoadingView`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoadingView)
      * [`LoadingView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoadingView.clone)
      * [`LoadingView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoadingView.kwargs_to_json)
      * [`LoadingView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoadingView.to_json)
    * [`LoaderView`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoaderView)
      * [`LoaderView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoaderView.to_json)
      * [`LoaderView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoaderView.clone)
      * [`LoaderView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LoaderView.kwargs_to_json)
    * [`PillBadgeView`](api__fiftyone.operators.types.md#fiftyone.operators.types.PillBadgeView)
      * [`PillBadgeView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PillBadgeView.clone)
      * [`PillBadgeView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PillBadgeView.kwargs_to_json)
      * [`PillBadgeView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PillBadgeView.to_json)
    * [`PlotlyView`](api__fiftyone.operators.types.md#fiftyone.operators.types.PlotlyView)
      * [`PlotlyView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PlotlyView.to_json)
      * [`PlotlyView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PlotlyView.clone)
      * [`PlotlyView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PlotlyView.kwargs_to_json)
    * [`Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement)
      * [`Placement.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement.to_json)
    * [`Places`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places)
      * [`Places.SAMPLES_GRID_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.SAMPLES_GRID_ACTIONS)
      * [`Places.SAMPLES_GRID_SECONDARY_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.SAMPLES_GRID_SECONDARY_ACTIONS)
      * [`Places.SAMPLES_VIEWER_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.SAMPLES_VIEWER_ACTIONS)
      * [`Places.EMBEDDINGS_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.EMBEDDINGS_ACTIONS)
      * [`Places.HISTOGRAM_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.HISTOGRAM_ACTIONS)
      * [`Places.MAP_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.MAP_ACTIONS)
      * [`Places.MAP_SECONDARY_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.MAP_SECONDARY_ACTIONS)
      * [`Places.DISPLAY_OPTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.DISPLAY_OPTIONS)
      * [`Places.HEADER_ACTIONS`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.HEADER_ACTIONS)
      * [`Places.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places.to_json)
    * [`KeyValueView`](api__fiftyone.operators.types.md#fiftyone.operators.types.KeyValueView)
      * [`KeyValueView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.KeyValueView.clone)
      * [`KeyValueView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.KeyValueView.kwargs_to_json)
      * [`KeyValueView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.KeyValueView.to_json)
    * [`Column`](api__fiftyone.operators.types.md#fiftyone.operators.types.Column)
      * [`Column.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Column.clone)
      * [`Column.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Column.to_json)
      * [`Column.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Column.kwargs_to_json)
    * [`Action`](api__fiftyone.operators.types.md#fiftyone.operators.types.Action)
      * [`Action.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Action.clone)
      * [`Action.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Action.to_json)
      * [`Action.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Action.kwargs_to_json)
    * [`Tooltip`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tooltip)
      * [`Tooltip.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tooltip.clone)
      * [`Tooltip.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tooltip.to_json)
      * [`Tooltip.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Tooltip.kwargs_to_json)
    * [`TableView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView)
      * [`TableView.keys()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.keys)
      * [`TableView.add_column()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.add_column)
      * [`TableView.add_row_action()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.add_row_action)
      * [`TableView.add_tooltip()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.add_tooltip)
      * [`TableView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.clone)
      * [`TableView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.to_json)
      * [`TableView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TableView.kwargs_to_json)
    * [`MapView`](api__fiftyone.operators.types.md#fiftyone.operators.types.MapView)
      * [`MapView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MapView.to_json)
      * [`MapView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MapView.clone)
      * [`MapView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MapView.kwargs_to_json)
    * [`ProgressView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ProgressView)
      * [`ProgressView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ProgressView.to_json)
      * [`ProgressView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ProgressView.clone)
      * [`ProgressView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ProgressView.kwargs_to_json)
    * [`ImageView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ImageView)
      * [`ImageView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ImageView.clone)
      * [`ImageView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ImageView.kwargs_to_json)
      * [`ImageView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ImageView.to_json)
    * [`AlertView`](api__fiftyone.operators.types.md#fiftyone.operators.types.AlertView)
      * [`AlertView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AlertView.to_json)
      * [`AlertView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AlertView.clone)
      * [`AlertView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.AlertView.kwargs_to_json)
    * [`ToastView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ToastView)
      * [`ToastView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ToastView.clone)
      * [`ToastView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ToastView.kwargs_to_json)
      * [`ToastView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ToastView.to_json)
    * [`CheckboxView`](api__fiftyone.operators.types.md#fiftyone.operators.types.CheckboxView)
      * [`CheckboxView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CheckboxView.clone)
      * [`CheckboxView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CheckboxView.kwargs_to_json)
      * [`CheckboxView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.CheckboxView.to_json)
    * [`ErrorView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ErrorView)
      * [`ErrorView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ErrorView.clone)
      * [`ErrorView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ErrorView.kwargs_to_json)
      * [`ErrorView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ErrorView.to_json)
    * [`HeaderView`](api__fiftyone.operators.types.md#fiftyone.operators.types.HeaderView)
      * [`HeaderView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HeaderView.clone)
      * [`HeaderView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HeaderView.kwargs_to_json)
      * [`HeaderView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HeaderView.to_json)
    * [`ObjectView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ObjectView)
      * [`ObjectView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ObjectView.clone)
      * [`ObjectView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ObjectView.kwargs_to_json)
      * [`ObjectView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ObjectView.to_json)
    * [`RadioView`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView)
      * [`RadioView.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.add_choice)
      * [`RadioView.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.append)
      * [`RadioView.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.choices)
      * [`RadioView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.clone)
      * [`RadioView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.kwargs_to_json)
      * [`RadioView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.to_json)
      * [`RadioView.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioView.values)
    * [`SwitchView`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView)
      * [`SwitchView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView.clone)
      * [`SwitchView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView.kwargs_to_json)
      * [`SwitchView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView.to_json)
    * [`TextView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextView)
      * [`TextView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextView.clone)
      * [`TextView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextView.kwargs_to_json)
      * [`TextView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextView.to_json)
    * [`TextFieldView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextFieldView)
      * [`TextFieldView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextFieldView.to_json)
      * [`TextFieldView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextFieldView.clone)
      * [`TextFieldView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TextFieldView.kwargs_to_json)
    * [`FieldView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FieldView)
      * [`FieldView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FieldView.clone)
      * [`FieldView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FieldView.kwargs_to_json)
      * [`FieldView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FieldView.to_json)
    * [`LazyFieldView`](api__fiftyone.operators.types.md#fiftyone.operators.types.LazyFieldView)
      * [`LazyFieldView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LazyFieldView.to_json)
      * [`LazyFieldView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LazyFieldView.clone)
      * [`LazyFieldView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LazyFieldView.kwargs_to_json)
    * [`DropdownView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView)
      * [`DropdownView.add_choice()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.add_choice)
      * [`DropdownView.append()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.append)
      * [`DropdownView.choices`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.choices)
      * [`DropdownView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.clone)
      * [`DropdownView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.kwargs_to_json)
      * [`DropdownView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.to_json)
      * [`DropdownView.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView.values)
    * [`DateTimeView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DateTimeView)
      * [`DateTimeView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DateTimeView.clone)
      * [`DateTimeView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DateTimeView.kwargs_to_json)
      * [`DateTimeView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DateTimeView.to_json)
    * [`LabelValueView`](api__fiftyone.operators.types.md#fiftyone.operators.types.LabelValueView)
      * [`LabelValueView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LabelValueView.clone)
      * [`LabelValueView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LabelValueView.kwargs_to_json)
      * [`LabelValueView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.LabelValueView.to_json)
    * [`PrimitiveView`](api__fiftyone.operators.types.md#fiftyone.operators.types.PrimitiveView)
      * [`PrimitiveView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PrimitiveView.clone)
      * [`PrimitiveView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PrimitiveView.kwargs_to_json)
      * [`PrimitiveView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PrimitiveView.to_json)
    * [`SliderView`](api__fiftyone.operators.types.md#fiftyone.operators.types.SliderView)
      * [`SliderView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SliderView.clone)
      * [`SliderView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SliderView.kwargs_to_json)
      * [`SliderView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.SliderView.to_json)
    * [`TagsView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TagsView)
      * [`TagsView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TagsView.clone)
      * [`TagsView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TagsView.kwargs_to_json)
      * [`TagsView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TagsView.to_json)
    * [`Success`](api__fiftyone.operators.types.md#fiftyone.operators.types.Success)
      * [`Success.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Success.clone)
      * [`Success.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Success.kwargs_to_json)
      * [`Success.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Success.to_json)
    * [`ButtonView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonView)
      * [`ButtonView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonView.clone)
      * [`ButtonView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonView.kwargs_to_json)
      * [`ButtonView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonView.to_json)
    * [`MarkdownView`](api__fiftyone.operators.types.md#fiftyone.operators.types.MarkdownView)
      * [`MarkdownView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MarkdownView.clone)
      * [`MarkdownView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MarkdownView.kwargs_to_json)
      * [`MarkdownView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MarkdownView.to_json)
    * [`StatusButtonView`](api__fiftyone.operators.types.md#fiftyone.operators.types.StatusButtonView)
      * [`StatusButtonView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.StatusButtonView.clone)
      * [`StatusButtonView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.StatusButtonView.kwargs_to_json)
      * [`StatusButtonView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.StatusButtonView.to_json)
    * [`MediaPlayerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.MediaPlayerView)
      * [`MediaPlayerView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MediaPlayerView.clone)
      * [`MediaPlayerView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MediaPlayerView.kwargs_to_json)
      * [`MediaPlayerView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MediaPlayerView.to_json)
    * [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView)
      * [`FileExplorerView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView.clone)
      * [`FileExplorerView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView.kwargs_to_json)
      * [`FileExplorerView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView.to_json)
    * [`PromptView`](api__fiftyone.operators.types.md#fiftyone.operators.types.PromptView)
      * [`PromptView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PromptView.clone)
      * [`PromptView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PromptView.kwargs_to_json)
      * [`PromptView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PromptView.to_json)
    * [`ViewTargetOptions`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetOptions)
      * [`ViewTargetOptions.choices_view`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetOptions.choices_view)
      * [`ViewTargetOptions.values()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetOptions.values)
    * [`ViewTargetProperty`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty)
      * [`ViewTargetProperty.options`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty.options)
      * [`ViewTargetProperty.options`](api__fiftyone.operators.types.md#id0)
      * [`ViewTargetProperty.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty.to_json)
    * [`GridView`](api__fiftyone.operators.types.md#fiftyone.operators.types.GridView)
      * [`GridView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.GridView.to_json)
      * [`GridView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.GridView.clone)
      * [`GridView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.GridView.kwargs_to_json)
    * [`DashboardView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DashboardView)
      * [`DashboardView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DashboardView.to_json)
      * [`DashboardView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DashboardView.clone)
      * [`DashboardView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DashboardView.kwargs_to_json)
    * [`DrawerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DrawerView)
      * [`DrawerView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DrawerView.clone)
      * [`DrawerView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DrawerView.kwargs_to_json)
      * [`DrawerView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.DrawerView.to_json)
    * [`IconButtonView`](api__fiftyone.operators.types.md#fiftyone.operators.types.IconButtonView)
      * [`IconButtonView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.IconButtonView.clone)
      * [`IconButtonView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.IconButtonView.kwargs_to_json)
      * [`IconButtonView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.IconButtonView.to_json)
    * [`ModalView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ModalView)
      * [`ModalView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ModalView.clone)
      * [`ModalView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ModalView.kwargs_to_json)
      * [`ModalView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ModalView.to_json)
    * [`HStackView`](api__fiftyone.operators.types.md#fiftyone.operators.types.HStackView)
      * [`HStackView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HStackView.clone)
      * [`HStackView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HStackView.kwargs_to_json)
      * [`HStackView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.HStackView.to_json)
    * [`VStackView`](api__fiftyone.operators.types.md#fiftyone.operators.types.VStackView)
      * [`VStackView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.VStackView.to_json)
      * [`VStackView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.VStackView.clone)
      * [`VStackView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.VStackView.kwargs_to_json)
    * [`ButtonGroupView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonGroupView)
      * [`ButtonGroupView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonGroupView.to_json)
      * [`ButtonGroupView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonGroupView.clone)
      * [`ButtonGroupView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ButtonGroupView.kwargs_to_json)
    * [`MenuView`](api__fiftyone.operators.types.md#fiftyone.operators.types.MenuView)
      * [`MenuView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MenuView.to_json)
      * [`MenuView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MenuView.clone)
      * [`MenuView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.MenuView.kwargs_to_json)
    * [`ArrowNavView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ArrowNavView)
      * [`ArrowNavView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ArrowNavView.to_json)
      * [`ArrowNavView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ArrowNavView.clone)
      * [`ArrowNavView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ArrowNavView.kwargs_to_json)
    * [`FrameLoaderView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FrameLoaderView)
      * [`FrameLoaderView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FrameLoaderView.clone)
      * [`FrameLoaderView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FrameLoaderView.kwargs_to_json)
      * [`FrameLoaderView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.FrameLoaderView.to_json)
    * [`TimelineView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimelineView)
      * [`TimelineView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimelineView.clone)
      * [`TimelineView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimelineView.kwargs_to_json)
      * [`TimelineView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimelineView.to_json)
    * [`TimerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimerView)
      * [`TimerView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimerView.clone)
      * [`TimerView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimerView.kwargs_to_json)
      * [`TimerView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.TimerView.to_json)
    * [`ComponentView`](api__fiftyone.operators.types.md#fiftyone.operators.types.ComponentView)
      * [`ComponentView.clone()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ComponentView.clone)
      * [`ComponentView.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ComponentView.kwargs_to_json)
      * [`ComponentView.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ComponentView.to_json)
    * [`Container`](api__fiftyone.operators.types.md#fiftyone.operators.types.Container)
      * [`Container.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Container.kwargs_to_json)
      * [`Container.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Container.to_json)
    * [`PaperContainer`](api__fiftyone.operators.types.md#fiftyone.operators.types.PaperContainer)
      * [`PaperContainer.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PaperContainer.to_json)
      * [`PaperContainer.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.PaperContainer.kwargs_to_json)
    * [`OutlinedContainer`](api__fiftyone.operators.types.md#fiftyone.operators.types.OutlinedContainer)
      * [`OutlinedContainer.kwargs_to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OutlinedContainer.kwargs_to_json)
      * [`OutlinedContainer.to_json()`](api__fiftyone.operators.types.md#fiftyone.operators.types.OutlinedContainer.to_json)
    * [`RiskLevel`](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel)
      * [`RiskLevel.LOW`](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.LOW)
      * [`RiskLevel.MEDIUM`](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.MEDIUM)
      * [`RiskLevel.HIGH`](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.HIGH)
      * [`RiskLevel.DANGEROUS`](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.DANGEROUS)
  * [fiftyone.operators.utils](api__fiftyone.operators.utils.md)
    * [`ProgressHandler`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler)
      * [`ProgressHandler.emit()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.emit)
      * [`ProgressHandler.acquire()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.acquire)
      * [`ProgressHandler.addFilter()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.addFilter)
      * [`ProgressHandler.close()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.close)
      * [`ProgressHandler.createLock()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.createLock)
      * [`ProgressHandler.filter()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.filter)
      * [`ProgressHandler.flush()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.flush)
      * [`ProgressHandler.format()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.format)
      * [`ProgressHandler.get_name()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.get_name)
      * [`ProgressHandler.handle()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.handle)
      * [`ProgressHandler.handleError()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.handleError)
      * [`ProgressHandler.name`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.name)
      * [`ProgressHandler.release()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.release)
      * [`ProgressHandler.removeFilter()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.removeFilter)
      * [`ProgressHandler.setFormatter()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.setFormatter)
      * [`ProgressHandler.setLevel()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.setLevel)
      * [`ProgressHandler.set_name()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.ProgressHandler.set_name)
    * [`is_method_overridden()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.is_method_overridden)
    * [`is_new()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.is_new)
    * [`create_operator_response()`](api__fiftyone.operators.utils.md#fiftyone.operators.utils.create_operator_response)



## Module contents#

FiftyOne operators.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Operator`([_builtin]) | A FiftyOne operator.  
---|---  
`OperatorConfig`(name[,Â label,Â description,Â ...]) | A configuration for an operator.  
`PipelineOperator`([_builtin]) | A FiftyOne pipeline operator.  
`OperatorRegistry`([enabled]) | Operator registry.  
`ViewTarget`() | Choices for target view that an operator should operate on  
`EvaluationMetricConfig`(name[,Â label,Â ...]) | Configuration class for evaluation metrics.  
`EvaluationMetric`([_builtin]) | Base class for evaluation metric operators.  
`ExecutionContext`([request_params,Â executor,Â ...]) | Represents the execution context of an operator.  
`ExecutionOptions`([...]) | Represents the execution options of an operation.  
`ProgressHandler`(ctx[,Â logger,Â level]) | A logging handler that reports all logging messages issued while the handler's context manager is active to the provided execution context's [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") method.  
`Panel`([_builtin]) | A panel.  
`PanelConfig`(name,Â label[,Â help_markdown,Â ...]) | Configuration for a panel.  
`ExecutionStore`(store_name,Â store_service[,Â ...]) | Execution store.  
`Categories`(value) |   
`SseOperator`([_builtin]) |   
`SseOperatorConfig`(name,Â label,Â store_name[,Â ...]) |   
  
**Functions:**

`get_operator`(operator_uri[,Â enabled]) | Gets the operator with the given URI.  
---|---  
`list_operators`([enabled,Â builtin,Â type]) | Returns all available operators.  
`operator_exists`(operator_uri[,Â enabled]) | Checks if the given operator exists.  
`execute_operator`(operator_uri[,Â ctx]) | Executes the operator with the given name.  
`is_new`(release_date[,Â days]) | Determines if a feature is considered "new" based on its release date.  
`execution_cache`([_func,Â residency,Â ttl,Â ...]) | Decorator for caching function results in an [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore").  
  
class fiftyone.operators.Operator(__builtin =False_)#
    

Bases: `object`

A FiftyOne operator.

Operators represent an operation and the details of how to execute it.

FiftyOne operators contain enough information for a user interface to render a form or button allowing a user to execute the operation.

**Attributes:**

`name` |   
---|---  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
`builtin` | Whether the operator is builtin.  
`config` | The `OperatorConfig` for the operator.  
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
  
**Methods:**

`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
---|---  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`execute`(ctx) | Executes the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`to_json`() | Returns a JSON representation of the operator.  
`add_secrets`(secrets) | Adds secrets to the operator.  
  
property name#
    

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

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

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

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

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

class fiftyone.operators.OperatorConfig(_name_ , _label =None_, _description =None_, _dynamic =False_, _execute_as_generator =False_, _unlisted =False_, _on_startup =False_, _on_dataset_open =False_, _disable_schema_validation =False_, _delegation_target =None_, _icon =None_, _light_icon =None_, _dark_icon =None_, _allow_immediate_execution =True_, _allow_delegated_execution =False_, _default_choice_to_delegated =False_, _resolve_execution_options_on_change =None_, _allow_distributed_execution =False_, _rerunnable =True_, _risk_level =RiskLevel.DANGEROUS_, _** kwargs_)#
    

Bases: `object`

A configuration for an operator.

Parameters:
    

  * **name** â the name of the operator

  * **label** ([_name_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.name "fiftyone.core.session.events.Colorscale.name")) â a label for the operator

  * **description** (_None_) â a description of the operator

  * **dynamic** (_False_) â whether the operator inputs and outputs should be resolved when the input/output changes

  * **execute_as_generator** (_False_) â whether the operator should be executed as a generator

  * **unlisted** (_False_) â whether the operator should be hidden from the Operator Browser

  * **on_startup** (_False_) â whether the operator should be executed on startup

  * **on_dataset_open** (_False_) â whether the operator should be executed on opening a dataset

  * **disable_schema_validation** (_False_) â whether the operator built-in schema validation should be disabled

  * **icon** (_None_) â icon to show for the operator in the Operator Browser

  * **light_icon** (_None_) â icon to show for the operator in the Operator Browser when the App is in the light mode

  * **dark_icon** (_None_) â icon to show for the operator in the Operator Browser when the App is in the dark mode

  * **allow_immediate_execution** (_True_) â whether the operator should allow immediate execution

  * **allow_delegated_execution** (_False_) â whether the operator should allow delegated execution

  * **default_choice_to_delegated** (_False_) â whether to default to delegated execution, if allowed

  * **resolve_execution_options_on_change** (_None_) â whether to resolve execution options dynamically when inputs change. By default, this behavior will match the `dynamic` setting

  * **allow_distributed_execution** (_False_) â whether the operator supports distributing delegated execution across parallel workers.

  * **rerunnable** (_True_) â whether the operator can be re-run

  * **risk_level** ([_RiskLevel.DANGEROUS_](api__fiftyone.operators.types.md#fiftyone.operators.types.RiskLevel.DANGEROUS "fiftyone.operators.types.RiskLevel.DANGEROUS")) â the declared `RiskLevel` for this operator is mainly used by guardrail systems of an agent to classify tool calls. If `None`, the operator defaults to `RiskLevel.DANGEROUS`




**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

class fiftyone.operators.PipelineOperator(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

A FiftyOne pipeline operator.

A pipeline operator represents a linear composition of other operators, containing the details of how to create and execute the [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline")

FiftyOne pipeline operators contain enough information for a user interface to render a form or button allowing a user to execute the operation.

**Methods:**

`resolve_pipeline`(ctx) | Returns the resolved pipeline of the operator.  
---|---  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Not used for pipeline operators; pipelines are executed via stages  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
**Attributes:**

`builtin` | Whether the operator is builtin.  
---|---  
`config` | The `OperatorConfig` for the operator.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
resolve_pipeline(_ctx_)#
    

Returns the resolved pipeline of the operator.

Subclasses can implement this method to define the pipeline of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline"),

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

execute(_ctx_)#
    

Not used for pipeline operators; pipelines are executed via stages

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

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

class fiftyone.operators.OperatorRegistry(_enabled =True_)#
    

Bases: `object`

Operator registry.

enabled (True): whether to include only enabled operators (True) or
    

only disabled operators (False) or all operators (âallâ)

**Methods:**

`list_operators`([builtin,Â type]) | Lists the available FiftyOne operators.  
---|---  
`list_errors`() | Lists the errors that occurred during operator loading.  
`operator_exists`(operator_uri) | Checks if the operator exists.  
`can_execute`(operator_uri) | Whether the operator can be executed.  
`get_operator`(operator_uri) | Retrieves an operator by its URI.  
  
list_operators(_builtin =None_, _type =None_)#
    

Lists the available FiftyOne operators.

Parameters:
    

  * **builtin** (_None_) â whether to include only builtin operators (True) or only non-builtin operators (False)

  * **type** (_None_) â whether to include only `"panel"` or `"operator"` type operators, or a specific `fiftyone.operators.Operator` subclass to restrict to



Returns:
    

a list of `fiftyone.operators.Operator` instances

list_errors()#
    

Lists the errors that occurred during operator loading.

Returns:
    

a list of errors

operator_exists(_operator_uri_)#
    

Checks if the operator exists.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

can_execute(_operator_uri_)#
    

Whether the operator can be executed.

Parameters:
    

**operator_uri** â the URI of the operator

Returns:
    

True/False

get_operator(_operator_uri_)#
    

Retrieves an operator by its URI.

Parameters:
    

**operator_uri** â the URI of an operator

Returns:
    

an `fiftyone.operators.Operator`, or None

fiftyone.operators.get_operator(_operator_uri_ , _enabled =True_)#
    

Gets the operator with the given URI.

Parameters:
    

  * **operator_uri** â the operator URI

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)



Returns:
    

an `fiftyone.operators.Operator`

Raises:
    

**ValueError** â if the operator is not found

fiftyone.operators.list_operators(_enabled =True_, _builtin ='all'_, _type =None_)#
    

Returns all available operators.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)

  * **builtin** (_"all"_) â whether to include only builtin operators (True) or only non-builtin operators (False) or all operators (âallâ)

  * **type** (_None_) â whether to include only `"panel"` or `"operator"` type operators, or a specific `fiftyone.operators.Operator` subclass to restrict to



Returns:
    

a list of `fiftyone.operators.Operator` instances

fiftyone.operators.operator_exists(_operator_uri_ , _enabled =True_)#
    

Checks if the given operator exists.

Parameters:
    

  * **operator_uri** â the operator URI

  * **enabled** (_True_) â whether to include only enabled operators (True) or only disabled operators (False) or all operators (âallâ)



Returns:
    

True/False

class fiftyone.operators.ViewTarget#
    

Bases: `object`

Choices for target view that an operator should operate on

See [`fiftyone.operators.types.ViewTargetProperty()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty "fiftyone.operators.types.ViewTargetProperty") for details.

**Attributes:**

`BASE_VIEW` | Base view from which a generated view was created  
---|---  
`CURRENT_VIEW` | Current view in the app  
`DATASET` | Entire dataset  
`DATASET_VIEW` | Empty dataset view, i.e., `ctx.dataset.view()`.  
`SELECTED_LABELS` | Selected labels in the app view, if any.  
`SELECTED_SAMPLES` | Selected samples in the app view, if any.  
`CUSTOM_VIEW_TARGET` | Custom view target specified by the caller.  
  
BASE_VIEW = 'BASE_VIEW'#
    

Base view from which a generated view was created

If the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), base view is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

CURRENT_VIEW = 'CURRENT_VIEW'#
    

Current view in the app

DATASET = 'DATASET'#
    

Entire dataset

DATASET_VIEW = 'DATASET_VIEW'#
    

Empty dataset view, i.e., `ctx.dataset.view()`.

Note: unlikely to be useful in the typical case.

SELECTED_LABELS = 'SELECTED_LABELS'#
    

Selected labels in the app view, if any.

SELECTED_SAMPLES = 'SELECTED_SAMPLES'#
    

Selected samples in the app view, if any.

CUSTOM_VIEW_TARGET = 'CUSTOM_VIEW_TARGET'#
    

Custom view target specified by the caller.

When using this option, specify âcustom_view_targetâ in the operator parameters with a list of JSON-serialized view stages to apply.

class fiftyone.operators.EvaluationMetricConfig(_name_ , _label =None_, _description =None_, _eval_types =None_, _aggregate_key =None_, _lower_is_better =True_, _** kwargs_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

Configuration class for evaluation metrics.

Parameters:
    

  * **name** â the name of the evaluation metric

  * **label** ([_name_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.name "fiftyone.core.session.events.Colorscale.name")) â a label for the evaluation metric

  * **description** (_None_) â a description of the evaluation metric

  * **eval_types** (_None_) â an optional list of evaluation method types that this metric supports

  * **aggregate_key** (_None_) â an optional key under which to store the metricâs aggregate value. This is used, for example, by [`metrics()`](api__fiftyone.utils.eval.base.md#fiftyone.utils.eval.base.BaseEvaluationResults.metrics "fiftyone.utils.eval.base.BaseEvaluationResults.metrics"). By default, the metricâs `name` is used as its key

  * **lower_is_better** (_True_) â whether lower values of the metric are better

  * ****kwargs** â other kwargs for `fiftyone.operators.OperatorConfig`




**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

class fiftyone.operators.EvaluationMetric(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

Base class for evaluation metric operators.

**Methods:**

`resolve_input`(ctx) | Defines any necessary properties to collect this evaluation metric's parameters from a user during prompting.  
---|---  
`parse_parameters`(ctx,Â params) | Performs any necessary execution-time formatting to this evaluation metric's parameters.  
`compute`(samples,Â results,Â **kwargs) | Computes the evaluation metric for the given collection.  
`get_fields`(samples,Â config,Â eval_key) | Lists the fields that were populated by the evaluation metric with the given key, if any.  
`rename`(samples,Â config,Â eval_key,Â new_eval_key) | Performs any necessary operations required to rename this evaluation metric's key.  
`cleanup`(samples,Â config,Â eval_key) | Cleans up the results of the evaluation metric with the given key from the collection.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Executes the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
**Attributes:**

`builtin` | Whether the operator is builtin.  
---|---  
`config` | The `OperatorConfig` for the operator.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
resolve_input(_ctx_)#
    

Defines any necessary properties to collect this evaluation metricâs parameters from a user during prompting.

Parameters:
    

**ctx** â an `fiftyone.operators.ExecutionContext`

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

parse_parameters(_ctx_ , _params_)#
    

Performs any necessary execution-time formatting to this evaluation metricâs parameters.

Parameters:
    

  * **ctx** â an `fiftyone.operators.ExecutionContext`

  * **params** â a params dict




compute(_samples_ , _results_ , _** kwargs_)#
    

Computes the evaluation metric for the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **results** â an [`fiftyone.core.evaluation.EvaluationResults`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationResults "fiftyone.core.evaluation.EvaluationResults")

  * ****kwargs** â arbitrary metric-specific parameters



Returns:
    

an optional aggregate metric value to store on the results

get_fields(_samples_ , _config_ , _eval_key_)#
    

Lists the fields that were populated by the evaluation metric with the given key, if any.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key



Returns:
    

a list of fields

rename(_samples_ , _config_ , _eval_key_ , _new_eval_key_)#
    

Performs any necessary operations required to rename this evaluation metricâs key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key

  * **new_eval_key** â a new evaluation key




cleanup(_samples_ , _config_ , _eval_key_)#
    

Cleans up the results of the evaluation metric with the given key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an [`fiftyone.core.evaluation.EvaluationMethodConfig`](api__fiftyone.core.evaluation.md#fiftyone.core.evaluation.EvaluationMethodConfig "fiftyone.core.evaluation.EvaluationMethodConfig")

  * **eval_key** â an evaluation key




add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

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

fiftyone.operators.execute_operator(_operator_uri_ , _ctx =None_, _** kwargs_)#
    

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
    

[**ExecutionError**](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionError "fiftyone.operators.executor.ExecutionError") â if an error occurred while immediately executing an operation or scheduling a delegated operation

class fiftyone.operators.ExecutionContext(_request_params =None_, _executor =None_, _set_progress =None_, _delegated_operation_id =None_, _operator_uri =None_, _required_secrets =None_, _pipeline =None_)#
    

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

class fiftyone.operators.ExecutionOptions(_allow_immediate_execution =True_, _allow_delegated_execution =False_, _default_choice_to_delegated =False_, _allow_distributed_execution =False_, _min_distributed_tasks =2_, _max_distributed_tasks =None_, _recommended_distributed_tasks =None_, _** __)#
    

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
    

class fiftyone.operators.ProgressHandler(_ctx_ , _logger =None_, _level =None_)#
    

Bases: `Handler`

A logging handler that reports all logging messages issued while the handlerâs context manager is active to the provided execution contextâs [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") method.

Parameters:
    

  * **ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **logger** (_None_) â a specific `logging.Logger` for which to report records. By default, the root logger is used

  * **level** (_None_) â an optional logging level above which to report records. By default, the loggerâs effective level is used




**Methods:**

`emit`(record) | Do whatever it takes to actually log the specified logging record.  
---|---  
`acquire`() | Acquire the I/O thread lock.  
`addFilter`(filter) | Add the specified filter to this handler.  
`close`() | Tidy up any resources used by the handler.  
`createLock`() | Acquire a thread lock for serializing access to the underlying I/O.  
`filter`(record) | Determine if a record is loggable by consulting all the filters.  
`flush`() | Ensure all logging output has been flushed.  
`format`(record) | Format the specified record.  
`get_name`() |   
`handle`(record) | Conditionally emit the specified logging record.  
`handleError`(record) | Handle errors which occur during an emit() call.  
`release`() | Release the I/O thread lock.  
`removeFilter`(filter) | Remove the specified filter from this handler.  
`setFormatter`(fmt) | Set the formatter for this handler.  
`setLevel`(level) | Set the logging level of this handler.  
`set_name`(name) |   
  
**Attributes:**

`name` |   
---|---  
  
emit(_record_)#
    

Do whatever it takes to actually log the specified logging record.

This version is intended to be implemented by subclasses and so raises a NotImplementedError.

acquire()#
    

Acquire the I/O thread lock.

addFilter(_filter_)#
    

Add the specified filter to this handler.

close()#
    

Tidy up any resources used by the handler.

This version removes the handler from an internal map of handlers, _handlers, which is used for handler lookup by name. Subclasses should ensure that this gets called from overridden close() methods.

createLock()#
    

Acquire a thread lock for serializing access to the underlying I/O.

filter(_record_)#
    

Determine if a record is loggable by consulting all the filters.

The default is to allow the record to be logged; any filter can veto this and the record is then dropped. Returns a zero value if a record is to be dropped, else non-zero.

Changed in version 3.2: Allow filters to be just callables.

flush()#
    

Ensure all logging output has been flushed.

This version does nothing and is intended to be implemented by subclasses.

format(_record_)#
    

Format the specified record.

If a formatter is set, use it. Otherwise, use the default formatter for the module.

get_name()#
    

handle(_record_)#
    

Conditionally emit the specified logging record.

Emission depends on filters which may have been added to the handler. Wrap the actual emission of the record with acquisition/release of the I/O thread lock. Returns whether the filter passed the record for emission.

handleError(_record_)#
    

Handle errors which occur during an emit() call.

This method should be called from handlers when an exception is encountered during an emit() call. If raiseExceptions is false, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors. You could, however, replace this with a custom handler if you wish. The record which was being processed is passed in to this method.

property name#
    

release()#
    

Release the I/O thread lock.

removeFilter(_filter_)#
    

Remove the specified filter from this handler.

setFormatter(_fmt_)#
    

Set the formatter for this handler.

setLevel(_level_)#
    

Set the logging level of this handler. level must be an int or a str.

set_name(_name_)#
    

fiftyone.operators.is_new(_release_date_ , _days =30_)#
    

Determines if a feature is considered ânewâ based on its release date.

A feature is considered new if its release date is within the specified number of days.

Examples:
    
    
    is_new("2024-11-09")
    # True if today's date is within 30 days after 2024-11-09
    
    is_new(datetime(2024, 11, 9), days=15)
    # True if today's date is within 15 days after November 9, 2024
    
    is_new("2024-10-01", days=45)
    # False if today's date is more than 45 days after October 1, 2024
    

Parameters:
    

  * **release_date** â 

the release date of the feature, in one of the following formats:

    * a string in the format `"%Y-%m-%d"`, e.g., `"2024-11-09"`

    * a datetime instance

  * **days** (_30_) â the number of days for which the feature is considered new



Returns:
    

True/False whether the release date is within the specified number of days

class fiftyone.operators.Panel(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

A panel.

**Methods:**

`render`(ctx) | Defines the panel's layout and events.  
---|---  
`resolve_input`(ctx) | Returns the resolved input property.  
`on_startup`(ctx) |   
`on_load`(ctx) |   
`execute`(ctx) | Executes the operator.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
**Attributes:**

`builtin` | Whether the operator is builtin.  
---|---  
`config` | The `OperatorConfig` for the operator.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
render(_ctx_)#
    

Defines the panelâs layout and events.

This method is called after every panel event is called (on load, button callback, context change event, etc).

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

on_startup(_ctx_)#
    

on_load(_ctx_)#
    

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

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

class fiftyone.operators.PanelConfig(_name_ , _label_ , _help_markdown =None_, _alpha =False_, _beta =False_, _is_new =False_, _category =None_, _icon =None_, _light_icon =None_, _dark_icon =None_, _allow_multiple =False_, _surfaces : Literal['grid', 'modal', 'grid modal'] = 'grid'_, _priority =None_, _** kwargs_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

Configuration for a panel.

Parameters:
    

  * **name** â the name of the panel

  * **label** â the display name for the panel

  * **icon** (_None_) â the icon to show in the panelâs tab

  * **light_icon** (_None_) â the icon to show in the panelâs tab when the App is in light mode

  * **dark_icon** (_None_) â the icon to show in the panelâs tab when the App is in dark mode

  * **allow_multiple** (_False_) â whether to allow multiple instances of the panel to be opened

  * **surfaces** (_"grid"_) â the surfaces on which the panel can be displayed

  * **help_markdown** (_None_) â a markdown string to display in the panelâs help tooltip

  * **category** (_Category_) â the category id of the panel

  * **priority** (_None_) â the priority of the panel for sorting in the UI




**Methods:**

`to_json`() |   
---|---  
  
**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
to_json()#
    

property risk_level#
    

The declared `RiskLevel` for this operator.

class fiftyone.operators.ExecutionStore(_store_name : str_, _store_service : [ExecutionStoreService](api__fiftyone.operators.store.service.md#fiftyone.operators.store.service.ExecutionStoreService "fiftyone.operators.store.service.ExecutionStoreService")_, _default_policy : str = 'persist'_)#
    

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

class fiftyone.operators.Categories(_value_)#
    

Bases: `Enum`

**Attributes:**

`IMPORT` |   
---|---  
`CURATE` |   
`ANALYZE` |   
`CUSTOM` |   
  
IMPORT = 'import'#
    

CURATE = 'curate'#
    

ANALYZE = 'analyze'#
    

CUSTOM = 'custom'#
    

fiftyone.operators.execution_cache(__func =None_, _*_ , _residency ='hybrid'_, _ttl =None_, _max_size =None_, _link_to_dataset =True_, _key_fn =None_, _store_name =None_, _version =None_, _operator_scoped =False_, _user_scoped =False_, _prompt_scoped =False_, _jwt_scoped =False_, _collection_name =None_, _serialize =None_, _deserialize =None_)#
    

Decorator for caching function results in an [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore").

The function being cached must:

  * accept a [`ctx`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") as the first parameter

  * be idempotent, i.e., same inputs produce the same outputs

  * have serializable function arguments and return values

  * have no side effects




Note

When `residency != "ephemeral"`, cached values must be coerced to JSON safe types in order to be stored. By default, a default JSON converter is used that can handle many common types, but you can override this behavior if necessary by providing custom `serialize` and `deserialize` functions.

Examples:
    
    
    from fiftyone.operators import execution_cache
    
    # Default behavior: cache for the life of a dataset
    @execution_cache
    def expensive_query(ctx, path):
        return ctx.dataset.count_values(path)
    
    # Cache in-memory, and only while the current operator prompt modal is open
    @execution_cache(prompt_scoped=True, residency="ephemeral")
    def expensive_query(ctx, path):
        return ctx.dataset.count_values(path)
    
    # Cache with a custom TTL and store name
    class Processor:
        @execution_cache(ttl=60, store_name="processor_cache")
        def expensive_query(self, ctx, path):
            return ctx.dataset.count_values(path)
    
    #
    # Cache at the user-level
    #
    
    def custom_key_fn(ctx, path):
        return path, ctx.user_id
    
    @execution_cache(ttl=90, key_fn=custom_key_fn, jwt_scoped=True)
    def user_specific_query(ctx, path):
        return ctx.dataset.match(F("creator_id") == ctx.user_id).count_values(path)
    
    #
    # You can manually bypass/modify the cache if necessary
    #
    
    # Bypass the cache
    result = expensive_query.uncached(ctx, path)
    
    # Set the cache for the given arguments
    expensive_query.set_cache(ctx, path, value_to_cache)
    
    # Clear the cache for a specific input
    expensive_query.clear_cache(ctx, path)
    
    # Clear all cache entries for the function
    expensive_query.clear_all_caches()
    expensive_query.clear_all_caches(dataset_id=dataset._doc.id)
    

Parameters:
    

  * **residency** (_"hybrid"_) â 

the residency of the cache. Can be one of:

    * `"transient"`: the cache is stored in the execution store with `policy="evict"`

    * `"ephemeral"`: the cache is stored in memory and is cleared when the process ends

    * `"hybrid"` (default): a combination of transient and ephemeral. The cache is stored in memory and in the execution store. The memory cache is used first, and if the value is not found, it falls back to the execution store

  * **ttl** (_None_) â a time-to-live for cached values, in seconds

  * **max_size** (_None_) â a maximum size for ephemeral caches. The default size is 1024. The cache will evict the least recently used items when the size exceeds this limit

  * **link_to_dataset** (_True_) â whether to namespace cache entries to the current dataset. If True, any cached values are automatically deleted when the dataset is deleted

  * **key_fn** (_None_) â a custom function to generate cache keys. By default, the function arguments are used as the key by serializing them as JSON

  * **store_name** (_None_) â a custom name for the execution store backing the cache. Defaults to the function name

  * **version** (_None_) â a version number to prevent cache collisions when the function implementation changes

  * **operator_scoped** (_False_) â whether to tie the cache entry to the current operator

  * **user_scoped** (_False_) â whether to tie the cache entry to the current user

  * **prompt_scoped** (_False_) â whether to tie the cache entry to the current operator prompt

  * **jwt_scoped** (_False_) â whether to tie the cache entry to the current userâs JWT

  * **collection_name** (_None_) â override the default collection name for the execution store used by the cache. The default is `"execution_store"`

  * **serialize** (_None_) â a custom serialization function to use when caching values and function arguments

  * **deserialize** (_None_) â a custom deserialization function when retrieving cached values




class fiftyone.operators.SseOperator(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

**Attributes:**

`IS_SSE_OPERATOR` |   
---|---  
`subscription_config` |   
`config` | The `OperatorConfig` for the operator.  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`execute`(ctx) | Executes the operator.  
---|---  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
IS_SSE_OPERATOR = True#
    

property subscription_config#
    

property config#
    

The `OperatorConfig` for the operator.

async execute(_ctx : [ExecutionContext](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

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

class fiftyone.operators.SseOperatorConfig(_name_ , _label_ , _store_name_ , _description =None_, _icon =None_, _light_icon =None_, _dark_icon =None_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property risk_level#
    

The declared `RiskLevel` for this operator.

to_json()#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
