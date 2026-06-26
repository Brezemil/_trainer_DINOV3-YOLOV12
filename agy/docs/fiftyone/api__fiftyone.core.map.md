---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.html
---

# fiftyone.core.map#

  * [fiftyone.core.map.batcher](api__fiftyone.core.map.batcher.md)
    * [fiftyone.core.map.batcher.batch](api__fiftyone.core.map.batcher.batch.md)
      * [`SampleBatch`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch)
        * [`SampleBatch.split()`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch.split)
        * [`SampleBatch.total`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch.total)
        * [`SampleBatch.create_subset()`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch.create_subset)
    * [fiftyone.core.map.batcher.id_batch](api__fiftyone.core.map.batcher.id_batch.md)
      * [`SampleIdBatch`](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch)
        * [`SampleIdBatch.get_max_batch_size()`](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch.get_max_batch_size)
        * [`SampleIdBatch.split()`](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch.split)
        * [`SampleIdBatch.total`](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch.total)
        * [`SampleIdBatch.create_subset()`](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch.create_subset)
    * [fiftyone.core.map.batcher.slice_batch](api__fiftyone.core.map.batcher.slice_batch.md)
      * [`SampleSliceBatch`](api__fiftyone.core.map.batcher.slice_batch.md#fiftyone.core.map.batcher.slice_batch.SampleSliceBatch)
        * [`SampleSliceBatch.split()`](api__fiftyone.core.map.batcher.slice_batch.md#fiftyone.core.map.batcher.slice_batch.SampleSliceBatch.split)
        * [`SampleSliceBatch.total`](api__fiftyone.core.map.batcher.slice_batch.md#fiftyone.core.map.batcher.slice_batch.SampleSliceBatch.total)
        * [`SampleSliceBatch.create_subset()`](api__fiftyone.core.map.batcher.slice_batch.md#fiftyone.core.map.batcher.slice_batch.SampleSliceBatch.create_subset)
    * [Module contents](api__fiftyone.core.map.batcher.md#module-fiftyone.core.map.batcher)
      * [`SampleBatch`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleBatch)
        * [`SampleBatch.split()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleBatch.split)
        * [`SampleBatch.total`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleBatch.total)
        * [`SampleBatch.create_subset()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleBatch.create_subset)
      * [`SampleIdBatch`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleIdBatch)
        * [`SampleIdBatch.get_max_batch_size()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleIdBatch.get_max_batch_size)
        * [`SampleIdBatch.split()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleIdBatch.split)
        * [`SampleIdBatch.total`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleIdBatch.total)
        * [`SampleIdBatch.create_subset()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleIdBatch.create_subset)
      * [`SampleSliceBatch`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleSliceBatch)
        * [`SampleSliceBatch.split()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleSliceBatch.split)
        * [`SampleSliceBatch.total`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleSliceBatch.total)
        * [`SampleSliceBatch.create_subset()`](api__fiftyone.core.map.batcher.md#fiftyone.core.map.batcher.SampleSliceBatch.create_subset)



  * [fiftyone.core.map.factory](api__fiftyone.core.map.factory.md)
    * [`MapperFactory`](api__fiftyone.core.map.factory.md#fiftyone.core.map.factory.MapperFactory)
      * [`MapperFactory.batch_methods()`](api__fiftyone.core.map.factory.md#fiftyone.core.map.factory.MapperFactory.batch_methods)
      * [`MapperFactory.mapper_keys()`](api__fiftyone.core.map.factory.md#fiftyone.core.map.factory.MapperFactory.mapper_keys)
      * [`MapperFactory.create()`](api__fiftyone.core.map.factory.md#fiftyone.core.map.factory.MapperFactory.create)
  * [fiftyone.core.map.mapper](api__fiftyone.core.map.mapper.md)
    * [`check_if_return_is_sample()`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.check_if_return_is_sample)
    * [`Mapper`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper)
      * [`Mapper.create()`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper.create)
      * [`Mapper.num_workers`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper.num_workers)
      * [`Mapper.batch_size`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper.batch_size)
      * [`Mapper.map_samples()`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper.map_samples)
    * [`LocalMapper`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper)
      * [`LocalMapper.batch_size`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper.batch_size)
      * [`LocalMapper.create()`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper.create)
      * [`LocalMapper.map_samples()`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper.map_samples)
      * [`LocalMapper.num_workers`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper.num_workers)
  * [fiftyone.core.map.process](api__fiftyone.core.map.process.md)
    * [`ProcessMapper`](api__fiftyone.core.map.process.md#fiftyone.core.map.process.ProcessMapper)
      * [`ProcessMapper.create()`](api__fiftyone.core.map.process.md#fiftyone.core.map.process.ProcessMapper.create)
      * [`ProcessMapper.batch_size`](api__fiftyone.core.map.process.md#fiftyone.core.map.process.ProcessMapper.batch_size)
      * [`ProcessMapper.map_samples()`](api__fiftyone.core.map.process.md#fiftyone.core.map.process.ProcessMapper.map_samples)
      * [`ProcessMapper.num_workers`](api__fiftyone.core.map.process.md#fiftyone.core.map.process.ProcessMapper.num_workers)
  * [fiftyone.core.map.threading](api__fiftyone.core.map.threading.md)
    * [`ThreadMapper`](api__fiftyone.core.map.threading.md#fiftyone.core.map.threading.ThreadMapper)
      * [`ThreadMapper.create()`](api__fiftyone.core.map.threading.md#fiftyone.core.map.threading.ThreadMapper.create)
      * [`ThreadMapper.batch_size`](api__fiftyone.core.map.threading.md#fiftyone.core.map.threading.ThreadMapper.batch_size)
      * [`ThreadMapper.map_samples()`](api__fiftyone.core.map.threading.md#fiftyone.core.map.threading.ThreadMapper.map_samples)
      * [`ThreadMapper.num_workers`](api__fiftyone.core.map.threading.md#fiftyone.core.map.threading.ThreadMapper.num_workers)
  * [fiftyone.core.map.typing](api__fiftyone.core.map.typing.md)
    * [`SampleCollection`](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection)
      * [`SampleCollection.iter_samples()`](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection.iter_samples)
      * [`SampleCollection.values()`](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection.values)



## Module contents#

Map package declaration.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Mapper`(batch_cls,Â num_workers[,Â batch_size,Â ...]) | Base class for mapping samples in parallel  
---|---  
`MapperFactory`() | Manage mapper implementations  
`ProcessMapper`(batch_cls,Â num_workers[,Â ...]) | Executes map_samples using multiprocessing.  
`ThreadMapper`(batch_cls,Â num_workers[,Â ...]) | Executes map_samples with threading using iter_samples.  
  
class fiftyone.core.map.Mapper(_batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int_, _batch_size : int | None = None_, _default_progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_)#
    

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

class fiftyone.core.map.MapperFactory#
    

Bases: `object`

Manage mapper implementations

**Methods:**

`batch_methods`() | Get available batch methods  
---|---  
`mapper_keys`() | Get available mapper class keys  
`create`([mapper_key,Â num_workers,Â ...]) | Create a mapper instance  
  
classmethod batch_methods() → List[str]#
    

Get available batch methods

classmethod mapper_keys() → List[str]#
    

Get available mapper class keys

classmethod create(_mapper_key : str | None = None_, _num_workers : int | None = None_, _batch_method : str | None = None_, _batch_size : int | None = None_, _** mapper_extra_kwargs_) → [Mapper](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.Mapper "fiftyone.core.map.mapper.Mapper")#
    

Create a mapper instance

class fiftyone.core.map.ProcessMapper(_batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int_, _batch_size : int | None = None_, _default_progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_)#
    

Bases: [`LocalMapper`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper "fiftyone.core.map.mapper.LocalMapper")

Executes map_samples using multiprocessing.

**Methods:**

`create`(*,Â config,Â batch_cls[,Â num_workers,Â ...]) | Create a new mapper instance  
---|---  
`map_samples`(sample_collection,Â map_fcn,Â *[,Â ...]) | Applies map function to each sample and returns an iterator of the results.  
  
**Attributes:**

`batch_size` | Number of samples per worker batch  
---|---  
`num_workers` | Number of workers to use  
  
classmethod create(_*_ , _config : [FiftyOneConfig](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")_, _batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int | None = None_, _batch_size : int | None = None_, _** ___)#
    

Create a new mapper instance

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

property num_workers: int#
    

Number of workers to use

class fiftyone.core.map.ThreadMapper(_batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int_, _batch_size : int | None = None_, _default_progress : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_)#
    

Bases: [`LocalMapper`](api__fiftyone.core.map.mapper.md#fiftyone.core.map.mapper.LocalMapper "fiftyone.core.map.mapper.LocalMapper")

Executes map_samples with threading using iter_samples.

**Methods:**

`create`(*,Â config,Â batch_cls[,Â num_workers,Â ...]) | Create a new mapper instance  
---|---  
`map_samples`(sample_collection,Â map_fcn,Â *[,Â ...]) | Applies map function to each sample and returns an iterator of the results.  
  
**Attributes:**

`batch_size` | Number of samples per worker batch  
---|---  
`num_workers` | Number of workers to use  
  
classmethod create(_*_ , _config : [FiftyOneConfig](api__fiftyone.core.config.md#fiftyone.core.config.FiftyOneConfig "fiftyone.core.config.FiftyOneConfig")_, _batch_cls : Type[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]_, _num_workers : int | None = None_, _batch_size : int | None = None_, _** ___)#
    

Create a new mapper instance

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

property num_workers: int#
    

Number of workers to use

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
