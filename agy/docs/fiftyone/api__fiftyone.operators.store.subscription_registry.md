---
source_url: https://docs.voxel51.com/api/fiftyone.operators.store.subscription_registry.html
---

# fiftyone.operators.store.subscription_registry#

Subscription registry class.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`LocalSubscriptionRegistry`() | Abstract base class for subscription registry.  
---|---  
`InLocalMemorySubscriptionRegistry`() |   
  
class fiftyone.operators.store.subscription_registry.LocalSubscriptionRegistry#
    

Bases: `ABC`

Abstract base class for subscription registry.

**Methods:**

`subscribe`(store_name,Â callback[,Â dataset_id]) | Registers a subscription for a given store.  
---|---  
`unsubscribe`(subscription_id) | Unsubscribes a subscription by its id.  
`unsubscribe_all`(store_name) | Unsubscribes all subscriptions for a given store.  
`empty_subscribers`() | Empties all subscribers.  
`get_subscribers`(store_name) | Retrieves all subscriptions for a given store.  
  
abstractmethod subscribe(_store_name : str_, _callback : Callable[[str], None]_, _dataset_id : str | None = None_) → str#
    

Registers a subscription for a given store. Returns a unique subscription id.

Parameters:
    

  * **store_name** â The name of the store to subscribe to.

  * **callback** â The callback to call when a change occurs.

  * **dataset_id** â Optional dataset ID to filter changes by.




abstractmethod unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribes a subscription by its id. Returns True if a subscription was removed.

abstractmethod unsubscribe_all(_store_name : str_)#
    

Unsubscribes all subscriptions for a given store.

abstractmethod empty_subscribers() → None#
    

Empties all subscribers.

abstractmethod get_subscribers(_store_name : str_) → Dict[str, Tuple[Callable[[str], None], str | None]]#
    

Retrieves all subscriptions for a given store. Returns a dictionary mapping subscription id to a tuple of (callback, dataset_id).

class fiftyone.operators.store.subscription_registry.InLocalMemorySubscriptionRegistry#
    

Bases: `LocalSubscriptionRegistry`

**Methods:**

`subscribe`(store_name,Â callback[,Â dataset_id]) | Registers a subscription for a given store.  
---|---  
`unsubscribe`(subscription_id) | Unsubscribes a subscription by its id.  
`unsubscribe_all`(store_name) | Unsubscribes all subscriptions for a given store.  
`get_subscribers`(store_name) | Retrieves all subscriptions for a given store.  
`empty_subscribers`() | Empties all subscribers.  
  
subscribe(_store_name : str_, _callback : Callable[[str], None]_, _dataset_id : str | None = None_) → str#
    

Registers a subscription for a given store. Returns a unique subscription id.

Parameters:
    

  * **store_name** â The name of the store to subscribe to.

  * **callback** â The callback to call when a change occurs.

  * **dataset_id** â Optional dataset ID to filter changes by.




unsubscribe(_subscription_id : str_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Unsubscribes a subscription by its id. Returns True if a subscription was removed.

unsubscribe_all(_store_name : str_)#
    

Unsubscribes all subscriptions for a given store.

get_subscribers(_store_name : str_) → Dict[str, Tuple[Callable[[str], None], str | None]]#
    

Retrieves all subscriptions for a given store. Returns a dictionary mapping subscription id to a tuple of (callback, dataset_id).

empty_subscribers() → None#
    

Empties all subscribers.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
