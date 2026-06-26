---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.mapper.html
---

# fiftyone.core.map.mapper#

Abstract mapping backend

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`check_if_return_is_sample`(sample_collection,Â ...) | Check if the map function returns a sample  
---|---  
  
**Classes:**

`Mapper`(batch_cls,Â num_workers[,Â batch_size,Â ...]) | Base class for mapping samples in parallel  
---|---  
`LocalMapper`(batch_cls,Â num_workers[,Â ...]) | Base class for mapping samples in parallelizing on the same machine  
  
fiftyone.core.map.mapper.check_if_return_is_sample(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _map_fcn : Callable[[T], R]_) → [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Check if the map function returns a sample

class fiftyone.core.map.mapper.Mapper(_batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int_, _batch_size : int | None = None_, _default_progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_)#
    

Bases: `ABC`

Base class for mapping samples in parallel

**Methods:**

`create`(*,Â config,Â batch_cls[,Â num_workers,Â ...]) | Create a new mapper instance  
---|---  
`map_samples`(sample_collection,Â map_fcn,Â *[,Â ...]) | Applies map function to each sample and returns an iterator of the results.  
  
**Attributes:**

`num_workers` | Number of workers to use  
---|---  
`batch_size` | Number of samples per worker batch  
  
classmethod create(_*_ , _config : [FiftyOneConfig](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")_, _batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int | None = None_, _batch_size : int | None = None_, _** ___)#
    

Create a new mapper instance

property num_workers: int#
    

Number of workers to use

property batch_size: int | None#
    

Number of samples per worker batch

map_samples(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _map_fcn : Callable[[T | U], R]_, _*_ , _iter_fcn : Callable[[[SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]], Iterable[Tuple[[ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)"), U]]] | None = None_, _progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | Literal['workers'] | None = None_, _save : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _skip_failures : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[Tuple[[ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)"), R]]#
    

Applies map function to each sample and returns an iterator of the results.

Parameters:
    

  * **sample_collection** ([_SampleCollection_](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") _[__T_ _]_) â The sample collection to map.

  * **map_fcn** (_Callable_ _[__[__Union_ _[__T_ _,__U_ _]__]__,__R_ _]_) â The map function to apply to each sample.

  * **iter_fcn** (_Callable_ _[__[__T_ _]__,__U_ _]_) â The function to iterate over the sample collection. If not provided the iteration function used is iter_samples.

  * **progress** (_Union_ _[_[_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__Literal_ _[__"workers"__]__]_) â Whether or not and how to render progress.

  * **save** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â Whether to save mutated samples mutated in the map function. Only valid when using the iter_fcn is None. Defaults to False.

  * **skip_failures** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â Whether to gracefully continue without raising an error if the map function raises an exception for a sample. Defaults to True.



Yields:
    

_Iterator[Tuple[bson.ObjectId, R]]_ â

The sample ID and the result of
    

the map function for the sample.

class fiftyone.core.map.mapper.LocalMapper(_batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int_, _batch_size : int | None = None_, _default_progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_)#
    

Bases: `Mapper`, `ABC`

Base class for mapping samples in parallelizing on the same machine

**Attributes:**

`batch_size` | Number of samples per worker batch  
---|---  
`num_workers` | Number of workers to use  
  
**Methods:**

`create`(*,Â config,Â batch_cls[,Â num_workers,Â ...]) | Create a new mapper instance  
---|---  
`map_samples`(sample_collection,Â map_fcn,Â *[,Â ...]) | Applies map function to each sample and returns an iterator of the results.  
  
property batch_size: int | None#
    

Number of samples per worker batch

classmethod create(_*_ , _config : [FiftyOneConfig](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")_, _batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int | None = None_, _batch_size : int | None = None_, _** ___)#
    

Create a new mapper instance

map_samples(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _map_fcn : Callable[[T | U], R]_, _*_ , _iter_fcn : Callable[[[SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]], Iterable[Tuple[[ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)"), U]]] | None = None_, _progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | Literal['workers'] | None = None_, _save : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _skip_failures : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_) → Iterator[Tuple[[ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)"), R]]#
    

Applies map function to each sample and returns an iterator of the results.

Parameters:
    

  * **sample_collection** ([_SampleCollection_](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") _[__T_ _]_) â The sample collection to map.

  * **map_fcn** (_Callable_ _[__[__Union_ _[__T_ _,__U_ _]__]__,__R_ _]_) â The map function to apply to each sample.

  * **iter_fcn** (_Callable_ _[__[__T_ _]__,__U_ _]_) â The function to iterate over the sample collection. If not provided the iteration function used is iter_samples.

  * **progress** (_Union_ _[_[_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__Literal_ _[__"workers"__]__]_) â Whether or not and how to render progress.

  * **save** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â Whether to save mutated samples mutated in the map function. Only valid when using the iter_fcn is None. Defaults to False.

  * **skip_failures** ([_bool_](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") _,__optional_) â Whether to gracefully continue without raising an error if the map function raises an exception for a sample. Defaults to True.



Yields:
    

_Iterator[Tuple[bson.ObjectId, R]]_ â

The sample ID and the result of
    

the map function for the sample.

property num_workers: int#
    

Number of workers to use

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
