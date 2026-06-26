---
source_url: https://docs.voxel51.com/api/fiftyone.operators.cache.utils.html
---

# fiftyone.operators.cache.utils#

Execution cache utils.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`resolve_cache_info`(ctx,Â ctx_index,Â args,Â ...) | Resolves the cache key, store, and memory cache for a given function call, including scope-based keys.  
---|---  
  
fiftyone.operators.cache.utils.resolve_cache_info(_ctx_ , _ctx_index_ , _args_ , _kwargs_ , _key_fn_ , _func_ , _*_ , _residency ='transient'_, _operator_scoped =False_, _user_scoped =False_, _prompt_scoped =False_, _jwt_scoped =False_, _collection_name =None_, _max_size =None_)#
    

Resolves the cache key, store, and memory cache for a given function call, including scope-based keys.

Returns:
    

(cache_key, store, memory_cache, skip_cache)

Return type:
    

A tuple

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
