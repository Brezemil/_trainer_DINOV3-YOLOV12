---
source_url: https://docs.voxel51.com/api/fiftyone.operators.server.html
---

# fiftyone.operators.server#

FiftyOne operator server.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_operators`(registry) |   
---|---  
`create_response_generator`(generator) |   
`create_response_async_generator`(generator) |   
`create_permission_error`(uri) |   
  
**Classes:**

`ListOperators`(scope,Â receive,Â send) |   
---|---  
`ResolvePlacements`(scope,Â receive,Â send) |   
`ExecuteOperator`(scope,Â receive,Â send) |   
`ExecuteOperatorAsGenerator`(scope,Â receive,Â send) |   
`ResolveType`(scope,Â receive,Â send) |   
`ResolveExecutionOptions`(scope,Â receive,Â send) |   
`SubscribeToExecutionStoreAsOperator`(scope,Â ...) |   
  
fiftyone.operators.server.get_operators(_registry : [PermissionedOperatorRegistry](api__fiftyone.operators.permissions.md#fiftyone.operators.permissions.PermissionedOperatorRegistry "fiftyone.operators.permissions.PermissionedOperatorRegistry")_)#
    

class fiftyone.operators.server.ListOperators(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_)#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

class fiftyone.operators.server.ResolvePlacements(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_)#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

class fiftyone.operators.server.ExecuteOperator(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_) → dict#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

fiftyone.operators.server.create_response_generator(_generator_)#
    

async fiftyone.operators.server.create_response_async_generator(_generator_)#
    

fiftyone.operators.server.create_permission_error(_uri_)#
    

class fiftyone.operators.server.ExecuteOperatorAsGenerator(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_) → dict#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

class fiftyone.operators.server.ResolveType(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_) → dict#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

class fiftyone.operators.server.ResolveExecutionOptions(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_) → dict#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

class fiftyone.operators.server.SubscribeToExecutionStoreAsOperator(_scope : MutableMapping[str, Any]_, _receive : Callable[[], Awaitable[MutableMapping[str, Any]]]_, _send : Callable[[MutableMapping[str, Any]], Awaitable[None]]_)#
    

Bases: `HTTPEndpoint`

**Methods:**

`post`(request,Â data) |   
---|---  
`dispatch`() |   
`method_not_allowed`(request) |   
  
async post(_request : Request_, _data : dict_) → EventSourceResponse#
    

async dispatch() → None#
    

async method_not_allowed(_request : Request_) → Response#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
