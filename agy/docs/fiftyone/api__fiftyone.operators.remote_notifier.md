---
source_url: https://docs.voxel51.com/api/fiftyone.operators.remote_notifier.html
---

# fiftyone.operators.remote_notifier#

FiftyOne operator server SSE notifier for execution store events.

This module provides an SSE notifier that listens for notification requests targeting a specific execution store. When a broadcast is sent to a store, all connected SSE clients subscribed to that store will receive the message.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`RemoteNotifier`() |   
---|---  
`SseNotifier`() | Handles the logic for broadcasting messages and managing client subscriptions for Server-Sent Events (SSE) notifications.  
  
class fiftyone.operators.remote_notifier.RemoteNotifier#
    

Bases: `ABC`

**Methods:**

`broadcast_to_store`(store_name,Â message) | Broadcast a message to all remote subscribers of the given store.  
---|---  
  
abstractmethod async broadcast_to_store(_store_name : str_, _message : str_) → None#
    

Broadcast a message to all remote subscribers of the given store.

Parameters:
    

  * **store_name** â The name of the store to which the message should be broadcast.

  * **message** â The message payload to send to the subscribers.




class fiftyone.operators.remote_notifier.SseNotifier#
    

Bases: `RemoteNotifier`

Handles the logic for broadcasting messages and managing client subscriptions for Server-Sent Events (SSE) notifications.

**Methods:**

`broadcast_to_store`(store_name,Â message) | Broadcast a message to all connected SSE clients subscribed to the specified store.  
---|---  
`get_event_source_response`(store_name[,Â ...]) | Creates an EventSourceResponse for a client subscribing to a specific store.  
`sync_current_state_for_client`(queue,Â store_name) | Broadcast the current state of the store to all connected clients.  
  
async broadcast_to_store(_store_name : str_, _message : str_) → None#
    

Broadcast a message to all connected SSE clients subscribed to the specified store. Handles disconnected clients gracefully without raising exceptions.

Parameters:
    

  * **store_name** â The name of the store to broadcast to.

  * **message** â The message to broadcast.




async get_event_source_response(_store_name : str_, _dataset_id : str | None = None_) → EventSourceResponse#
    

Creates an EventSourceResponse for a client subscribing to a specific store. It registers a new queue for the client and produces an async generator to stream events.

Parameters:
    

  * **store_name** â The name of the store to subscribe to.

  * **dataset_id** â Optional dataset ID to filter events by.



Returns:
    

An EventSourceResponse for streaming events to the client.

async sync_current_state_for_client(_queue : Queue_, _store_name : str_, _dataset_id : str | None = None_) → None#
    

Broadcast the current state of the store to all connected clients.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
