---
source_url: https://docs.voxel51.com/api/fiftyone.operators.store.notification_service.html
---

# fiftyone.operators.store.notification_service#

Notification service for ExecutionStore using MongoDB Change Streams.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ChangeStreamNotificationService`() | Abstract base class for change stream notification services.  
---|---  
`MongoChangeStreamNotificationService`(...[,Â ...]) |   
`MongoChangeStreamNotificationServiceLifecycleManager`(...) |   
  
**Functions:**

`is_notification_service_disabled`() | Check if the notification service is disabled.  
---|---  
  
class fiftyone.operators.store.notification_service.ChangeStreamNotificationService#
    

Bases: `ABC`

Abstract base class for change stream notification services.

**Methods:**

`subscribe`(store_name,Â callback[,Â dataset_id]) | Register a local subscriber for a specific store.  
---|---  
`unsubscribe`(subscription_id) | Unsubscribe local subscribers from a specific store.  
`unsubscribe_all`(store_name) | Unsubscribe from all changes in a store.  
`notify`(store_name,Â message_data) | Notify local subscribers and remote listeners of a change.  
`start`() | Start watching for database changes.  
`stop`() | Stop watching for database changes.  
  
abstractmethod subscribe(_store_name : str_, _callback : Callable[[str], None]_, _dataset_id : str | None = None_) → str#
    

Register a local subscriber for a specific store.

Parameters:
    

  * **store_name** â The name of the store to subscribe to.

  * **callback** â The callback to call when a change occurs.

  * **dataset_id** â Optional dataset ID to filter changes by.



Returns:
    

The subscription id.

abstractmethod unsubscribe(_subscription_id : str_)#
    

Unsubscribe local subscribers from a specific store.

Parameters:
    

**subscription_id** â The subscription id to unsubscribe from.

abstractmethod unsubscribe_all(_store_name : str_)#
    

Unsubscribe from all changes in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to unsubscribe from

abstractmethod notify(_store_name : str_, _message_data : [MessageData](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData "fiftyone.operators.message.MessageData")_) → None#
    

Notify local subscribers and remote listeners of a change.

Parameters:
    

  * **store_name** â The name of the store that changed.

  * **message** â The message to notify subscribers with.




abstractmethod async start() → None#
    

Start watching for database changes.

abstractmethod async stop() → None#
    

Stop watching for database changes.

class fiftyone.operators.store.notification_service.MongoChangeStreamNotificationService(_collection_name : str_, _remote_notifier : [RemoteNotifier](api__fiftyone.operators.remote_notifier.md#fiftyone.operators.remote_notifier.RemoteNotifier "fiftyone.operators.remote_notifier.RemoteNotifier") = None_, _registry : [LocalSubscriptionRegistry](api__fiftyone.operators.store.subscription_registry.md#fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry "fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry") = None_)#
    

Bases: `ChangeStreamNotificationService`

**Methods:**

`subscribe`(store_name,Â callback[,Â dataset_id]) | Register a local subscriber for a specific store.  
---|---  
`unsubscribe`(subscription_id) | Unsubscribe from a specific store.  
`unsubscribe_all`(store_name) | Unsubscribe from all changes in a store.  
`start`(dedicated_event_loop) | Start watching the collection for changes using change streams or polling.  
`notify`(store_name,Â message_data) | Notify local subscribers and remote listeners of a change.  
`stop`() | Signal stop watching the collection for changes.  
  
subscribe(_store_name : str_, _callback : Callable[[str], None]_, _dataset_id : str | None = None_) → str#
    

Register a local subscriber for a specific store.

Parameters:
    

  * **store_name** â The name of the store to subscribe to.

  * **callback** â The callback to call when a change occurs.

  * **dataset_id** â Optional dataset ID to filter changes by.



Returns:
    

The subscription id.

unsubscribe(_subscription_id : str_)#
    

Unsubscribe from a specific store.

Parameters:
    

**subscription_id** â The subscription id to unsubscribe from.

unsubscribe_all(_store_name : str_)#
    

Unsubscribe from all changes in a store.

Parameters:
    

**store_name** (_str_) â the name of the store to unsubscribe from

async start(_dedicated_event_loop : AbstractEventLoop_) → None#
    

Start watching the collection for changes using change streams or polling.

async notify(_store_name : str_, _message_data : [MessageData](api__fiftyone.operators.message.md#fiftyone.operators.message.MessageData "fiftyone.operators.message.MessageData")_) → None#
    

Notify local subscribers and remote listeners of a change. Handles exceptions gracefully to prevent failures when clients disconnect.

Parameters:
    

  * **store_name** â The name of the store that changed

  * **message_data** â The message data to notify subscribers with




async stop() → None#
    

Signal stop watching the collection for changes. Assume this is called from thread safe context.

class fiftyone.operators.store.notification_service.MongoChangeStreamNotificationServiceLifecycleManager(_notification_service : MongoChangeStreamNotificationService_)#
    

Bases: `object`

**Methods:**

`start_in_dedicated_thread`() | Create a dedicated event loop in a new thread and start the notification service.  
---|---  
`stop`() |   
  
start_in_dedicated_thread() → None#
    

Create a dedicated event loop in a new thread and start the notification service.

async stop() → None#
    

fiftyone.operators.store.notification_service.is_notification_service_disabled() → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if the notification service is disabled.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
