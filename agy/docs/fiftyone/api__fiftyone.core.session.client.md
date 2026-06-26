---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.client.html
---

# fiftyone.core.session.client#

Session server-sent events client.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Client`(address,Â auto,Â port,Â remote,Â start_time) |   
---|---  
  
class fiftyone.core.session.client.Client(_address : str_, _auto : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")_, _port : int_, _remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")_, _start_time : float_)#
    

Bases: `object`

**Attributes:**

`address` |   
---|---  
`auto` |   
`port` |   
`remote` |   
`start_time` |   
`origin` | The origin of the server  
`is_open` | Whether the client is connected  
  
**Methods:**

`open`(state) | Open the client connection  
---|---  
`close`() | Close the client connection  
`send_event`(event) | Sends an event to the server  
`add_event_listener`(event_name,Â listener) | Adds an event listener callback for the provided event name.  
`remove_event_listener`(event_name,Â listener) | Removes an event listener callback for the provided event name if it has been registered  
  
address: str#
    

auto: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

port: int#
    

remote: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

start_time: float#
    

property origin: str#
    

The origin of the server

property is_open: str#
    

Whether the client is connected

open(_state : [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")_) → None#
    

Open the client connection

Arg:
    

state: the initial state description

close()#
    

Close the client connection

send_event(_event : [CaptureNotebookCell](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell "fiftyone.core.session.events.CaptureNotebookCell") | [CloseSession](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession "fiftyone.core.session.events.CloseSession") | [DeactivateNotebookCell](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell "fiftyone.core.session.events.DeactivateNotebookCell") | [ReactivateNotebookCell](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell "fiftyone.core.session.events.ReactivateNotebookCell") | [SelectSamples](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples "fiftyone.core.session.events.SelectSamples") | [SelectLabels](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels "fiftyone.core.session.events.SelectLabels") | [SetColorScheme](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme "fiftyone.core.session.events.SetColorScheme") | [SetGroupSlice](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice "fiftyone.core.session.events.SetGroupSlice") | [SetSample](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample "fiftyone.core.session.events.SetSample") | [SetLabelSelectionStyle](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle "fiftyone.core.session.events.SetLabelSelectionStyle") | [SetSampleSelectionStyle](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle "fiftyone.core.session.events.SetSampleSelectionStyle") | [SetSpaces](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces "fiftyone.core.session.events.SetSpaces") | [StateUpdate](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate "fiftyone.core.session.events.StateUpdate") | [SetFieldVisibilityStage](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage "fiftyone.core.session.events.SetFieldVisibilityStage")_) → None#
    

Sends an event to the server

Parameters:
    

**event** â the event

add_event_listener(_event_name : str_, _listener : Callable_) → None#
    

Adds an event listener callback for the provided event name. Events sent from client and from the server connection will be dispatched to the listener

Parameters:
    

  * **event_name** â the event name

  * **listener** â the listener callback




remove_event_listener(_event_name : str_, _listener : Callable_) → None#
    

Removes an event listener callback for the provided event name if it has been registered

Parameters:
    

  * **event_name** â the event name

  * **listener** â the listener callback




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
