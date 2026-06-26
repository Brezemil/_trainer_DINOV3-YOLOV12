---
source_url: https://docs.voxel51.com/api/fiftyone.operators.cache.html
---

# fiftyone.operators.cache#

  * [fiftyone.operators.cache.decorator](api__fiftyone.operators.cache.decorator.md)
    * [`execution_cache()`](api__fiftyone.operators.cache.decorator.md#fiftyone.operators.cache.decorator.execution_cache)
  * [fiftyone.operators.cache.ephemeral](api__fiftyone.operators.cache.ephemeral.md)
    * [`get_ephemeral_cache()`](api__fiftyone.operators.cache.ephemeral.md#fiftyone.operators.cache.ephemeral.get_ephemeral_cache)
    * [`clear_all_ephemeral_caches()`](api__fiftyone.operators.cache.ephemeral.md#fiftyone.operators.cache.ephemeral.clear_all_ephemeral_caches)
  * [fiftyone.operators.cache.serialization](api__fiftyone.operators.cache.serialization.md)
    * [`auto_serialize()`](api__fiftyone.operators.cache.serialization.md#fiftyone.operators.cache.serialization.auto_serialize)
    * [`auto_deserialize()`](api__fiftyone.operators.cache.serialization.md#fiftyone.operators.cache.serialization.auto_deserialize)
  * [fiftyone.operators.cache.utils](api__fiftyone.operators.cache.utils.md)
    * [`resolve_cache_info()`](api__fiftyone.operators.cache.utils.md#fiftyone.operators.cache.utils.resolve_cache_info)



## Module contents#

Execution cache.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`execution_cache`([_func,Â residency,Â ttl,Â ...]) | Decorator for caching function results in an [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore").  
---|---  
  
fiftyone.operators.cache.execution_cache(__func =None_, _*_ , _residency ='hybrid'_, _ttl =None_, _max_size =None_, _link_to_dataset =True_, _key_fn =None_, _store_name =None_, _version =None_, _operator_scoped =False_, _user_scoped =False_, _prompt_scoped =False_, _jwt_scoped =False_, _collection_name =None_, _serialize =None_, _deserialize =None_)#
    

Decorator for caching function results in an [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore").

The function being cached must:

  * accept a [`ctx`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") as the first parameter

  * be idempotent, i.e., same inputs produce the same outputs

  * have serializable function arguments and return values

  * have no side effects




Note

When `residency != "ephemeral"`, cached values must be coerced to JSON safe types in order to be stored. By default, a default JSON converter is used that can handle many common types, but you can override this behavior if necessary by providing custom `serialize` and `deserialize` functions.

Examples:
    
    
    from fiftyone.operators import execution_cache
    
    # Default behavior: cache for the life of a dataset
    @execution_cache
    def expensive_query(ctx, path):
        return ctx.dataset.count_values(path)
    
    # Cache in-memory, and only while the current operator prompt modal is open
    @execution_cache(prompt_scoped=True, residency="ephemeral")
    def expensive_query(ctx, path):
        return ctx.dataset.count_values(path)
    
    # Cache with a custom TTL and store name
    class Processor:
        @execution_cache(ttl=60, store_name="processor_cache")
        def expensive_query(self, ctx, path):
            return ctx.dataset.count_values(path)
    
    #
    # Cache at the user-level
    #
    
    def custom_key_fn(ctx, path):
        return path, ctx.user_id
    
    @execution_cache(ttl=90, key_fn=custom_key_fn, jwt_scoped=True)
    def user_specific_query(ctx, path):
        return ctx.dataset.match(F("creator_id") == ctx.user_id).count_values(path)
    
    #
    # You can manually bypass/modify the cache if necessary
    #
    
    # Bypass the cache
    result = expensive_query.uncached(ctx, path)
    
    # Set the cache for the given arguments
    expensive_query.set_cache(ctx, path, value_to_cache)
    
    # Clear the cache for a specific input
    expensive_query.clear_cache(ctx, path)
    
    # Clear all cache entries for the function
    expensive_query.clear_all_caches()
    expensive_query.clear_all_caches(dataset_id=dataset._doc.id)
    

Parameters:
    

  * **residency** (_"hybrid"_) â 

the residency of the cache. Can be one of:

    * `"transient"`: the cache is stored in the execution store with `policy="evict"`

    * `"ephemeral"`: the cache is stored in memory and is cleared when the process ends

    * `"hybrid"` (default): a combination of transient and ephemeral. The cache is stored in memory and in the execution store. The memory cache is used first, and if the value is not found, it falls back to the execution store

  * **ttl** (_None_) â a time-to-live for cached values, in seconds

  * **max_size** (_None_) â a maximum size for ephemeral caches. The default size is 1024. The cache will evict the least recently used items when the size exceeds this limit

  * **link_to_dataset** (_True_) â whether to namespace cache entries to the current dataset. If True, any cached values are automatically deleted when the dataset is deleted

  * **key_fn** (_None_) â a custom function to generate cache keys. By default, the function arguments are used as the key by serializing them as JSON

  * **store_name** (_None_) â a custom name for the execution store backing the cache. Defaults to the function name

  * **version** (_None_) â a version number to prevent cache collisions when the function implementation changes

  * **operator_scoped** (_False_) â whether to tie the cache entry to the current operator

  * **user_scoped** (_False_) â whether to tie the cache entry to the current user

  * **prompt_scoped** (_False_) â whether to tie the cache entry to the current operator prompt

  * **jwt_scoped** (_False_) â whether to tie the cache entry to the current userâs JWT

  * **collection_name** (_None_) â override the default collection name for the execution store used by the cache. The default is `"execution_store"`

  * **serialize** (_None_) â a custom serialization function to use when caching values and function arguments

  * **deserialize** (_None_) â a custom deserialization function when retrieving cached values




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
