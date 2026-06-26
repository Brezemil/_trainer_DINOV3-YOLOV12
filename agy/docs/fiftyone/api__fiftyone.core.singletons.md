---
source_url: https://docs.voxel51.com/api/fiftyone.core.singletons.html
---

# fiftyone.core.singletons#

FiftyOne singleton implementations.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DatasetSingleton`(*args,Â **kwargs) | Singleton metaclass for [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").  
---|---  
`DocumentSingleton` | Singleton metaclass interface for [`fiftyone.core.document.Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document") subclasses.  
`SampleSingleton`(*args,Â **kwargs) | Singleton metaclass for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").  
`FrameSingleton`(*args,Â **kwargs) | Singleton metaclass for [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame").  
  
class fiftyone.core.singletons.DatasetSingleton(_* args_, _** kwargs_)#
    

Bases: `type`

Singleton metaclass for [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

Datasets are singletons keyed by the datasetâs `name`.

Note that new [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") instances are always created if the `_create == True`.

**Methods:**

`mro`() | Return a type's method resolution order.  
---|---  
  
mro()#
    

Return a typeâs method resolution order.

class fiftyone.core.singletons.DocumentSingleton#
    

Bases: `type`

Singleton metaclass interface for [`fiftyone.core.document.Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document") subclasses.

The methods declared by this interface are used by the [`fiftyone.core.document.Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document") class to manage all instances of a class that implements this type.

**Methods:**

`mro`() | Return a type's method resolution order.  
---|---  
  
mro()#
    

Return a typeâs method resolution order.

class fiftyone.core.singletons.SampleSingleton(_* args_, _** kwargs_)#
    

Bases: `DocumentSingleton`

Singleton metaclass for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").

This metaclass maintains a weakref dictionary of all in-memory [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances keyed by `[collection name][sample ID]`.

**Methods:**

`mro`() | Return a type's method resolution order.  
---|---  
  
mro()#
    

Return a typeâs method resolution order.

class fiftyone.core.singletons.FrameSingleton(_* args_, _** kwargs_)#
    

Bases: `DocumentSingleton`

Singleton metaclass for [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame").

This metaclass maintains a weakref dictionary of all in-memory [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") instances keyed by `[collection name][sample ID][frame number]`.

**Methods:**

`mro`() | Return a type's method resolution order.  
---|---  
  
mro()#
    

Return a typeâs method resolution order.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
