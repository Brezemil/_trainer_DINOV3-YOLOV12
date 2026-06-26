---
source_url: https://docs.voxel51.com/api/fiftyone.utils.quickstart.html
---

# fiftyone.utils.quickstart#

FiftyOne quickstart.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`quickstart`([video,Â port,Â address,Â remote]) | Runs the FiftyOne quickstart.  
---|---  
  
fiftyone.utils.quickstart.quickstart(_video =False_, _port =None_, _address =None_, _remote =False_)#
    

Runs the FiftyOne quickstart.

This method loads an interesting dataset from the Dataset Zoo, launches the App, and prints some suggestions for exploring the dataset.

Parameters:
    

  * **video** (_False_) â whether to launch a video dataset

  * **port** (_None_) â the port number to serve the App. If None, `fiftyone.config.default_app_port` is used

  * **address** (_None_) â the address to serve the App. If None, `fiftyone.config.default_app_address` is used

  * **remote** (_False_) â whether this is a remote session, and opening the App should not be attempted



Returns:
    

a tuple containing

  * dataset: the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") that was loaded

  * session: the [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") instance for the App that was launched




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
