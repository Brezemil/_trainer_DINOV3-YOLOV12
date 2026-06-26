---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.notebooks.html
---

# fiftyone.core.session.notebooks#

Session notebook handling.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`NotebookCell`(address,Â height,Â handle,Â port,Â ...) |   
---|---  
  
**Functions:**

`capture`(cell,Â data[,Â proxy_url]) |   
---|---  
`display`(client,Â cell[,Â proxy_url,Â reactivate]) | Displays a running FiftyOne instance.  
`display_ipython`(client,Â cell[,Â proxy_url,Â ...]) |   
`display_colab`(client,Â cell[,Â proxy_url,Â ...]) | Display a FiftyOne instance in a Colab output frame.  
`display_databricks`(client,Â cell[,Â ...]) | Display a FiftyOne instance in a Databricks output frame.  
  
class fiftyone.core.session.notebooks.NotebookCell(_address : str_, _height : int_, _handle : 'IPython.display.DisplayHandle'_, _port : int_, _subscription : str_)#
    

Bases: `object`

**Attributes:**

`address` |   
---|---  
`height` |   
`handle` |   
`port` |   
`subscription` |   
  
address: str#
    

height: int#
    

handle: DisplayHandle#
    

port: int#
    

subscription: str#
    

fiftyone.core.session.notebooks.capture(_cell : NotebookCell_, _data : [CaptureNotebookCell](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell "fiftyone.core.session.events.CaptureNotebookCell")_, _proxy_url : str = None_) → None#
    

fiftyone.core.session.notebooks.display(_client : [Client](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client "fiftyone.core.session.client.Client")_, _cell : NotebookCell_, _proxy_url : str = None_, _reactivate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Displays a running FiftyOne instance.

fiftyone.core.session.notebooks.display_ipython(_client : [Client](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client "fiftyone.core.session.client.Client")_, _cell : NotebookCell_, _proxy_url : str = None_, _reactivate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _** kwargs: Dict[str, str | [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")]_) → None#
    

fiftyone.core.session.notebooks.display_colab(_client : [Client](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client "fiftyone.core.session.client.Client")_, _cell : NotebookCell_, _proxy_url : str = None_, _reactivate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → None#
    

Display a FiftyOne instance in a Colab output frame.

The Colab VM is not directly exposed to the network, so the Colab runtime provides a service worker tunnel to proxy requests from the end userâs browser through to servers running on the Colab VM: the output frame may issue requests to <https://localhost>:<port> (HTTPS only), which will be forwarded to the specified port on the VM.

It does not suffice to create an iframe and let the service worker redirect its traffic (<iframe src=âhttps://localhost:6006â>), because for security reasons service workers cannot intercept iframe traffic. Instead, we manually fetch the FiftyOne index page with an XHR in the output frame, and inject the raw HTML into document.body.

fiftyone.core.session.notebooks.display_databricks(_client : [Client](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client "fiftyone.core.session.client.Client")_, _cell : NotebookCell_, _proxy_url : str = None_, _reactivate : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_)#
    

Display a FiftyOne instance in a Databricks output frame.

The Databricks driver port is accessible via a proxy url and can be displayed inside an IFrame.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
