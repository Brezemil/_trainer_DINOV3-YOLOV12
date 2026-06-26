---
source_url: https://docs.voxel51.com/api/fiftyone.operators.decorators.html
---

# fiftyone.operators.decorators#

FiftyOne operator decorators.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`coroutine_timeout`(seconds) |   
---|---  
`timeout`(seconds) |   
`raise_timeout_error`(seconds) |   
`plugins_cache`(func) | Decorator that returns cached function results as long as no plugins have been modified since last time.  
`dir_state`(dirpath) |   
  
fiftyone.operators.decorators.coroutine_timeout(_seconds_)#
    

fiftyone.operators.decorators.timeout(_seconds : int_)#
    

fiftyone.operators.decorators.raise_timeout_error(_seconds_)#
    

fiftyone.operators.decorators.plugins_cache(_func_)#
    

Decorator that returns cached function results as long as no plugins have been modified since last time.

fiftyone.operators.decorators.dir_state(_dirpath_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
