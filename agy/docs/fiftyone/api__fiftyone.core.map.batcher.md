---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.batcher.html
---

# fiftyone.core.map.batcher#

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



## Module contents#

Sample batcher package declaration.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SampleBatch`() | A sample batch  
---|---  
`SampleIdBatch`(*sample_ids) | Sample batch using ids  
`SampleSliceBatch`(start_idx,Â stop_idx) | Sample batch using slices  
  
class fiftyone.core.map.batcher.SampleBatch#
    

Bases: `ABC`

A sample batch

**Methods:**

`split`(sample_collection,Â num_workers[,Â ...]) | Create a list of sample batches  
---|---  
`create_subset`(sample_collection) | Create a sample collection from the batch  
  
**Attributes:**

`total` | Get the total number of samples in the batch  
---|---  
  
abstractmethod classmethod split(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _num_workers : int_, _batch_size : int | None = None_) → List[[SampleBatch](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")]#
    

Create a list of sample batches

abstract property total: int#
    

Get the total number of samples in the batch

abstractmethod create_subset(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_) → [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]#
    

Create a sample collection from the batch

class fiftyone.core.map.batcher.SampleIdBatch(_* sample_ids: [ObjectId](https://pymongo.readthedocs.io/en/stable/api/bson/objectid.html#bson.objectid.ObjectId "\(in PyMongo v4.17.0\)")_)#
    

Bases: [`SampleBatch`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")

Sample batch using ids

**Methods:**

`get_max_batch_size`() | Get max batch size  
---|---  
`split`(sample_collection,Â num_workers[,Â ...]) | Create a list of sample batches  
`create_subset`(sample_collection) | Create a sample collection from the batch  
  
**Attributes:**

`total` | Get the total number of samples in the batch  
---|---  
  
classmethod get_max_batch_size()#
    

Get max batch size

classmethod split(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _num_workers : int_, _batch_size : int | None = None_) → List[[SampleIdBatch](api__fiftyone.core.map.batcher.id_batch.md#fiftyone.core.map.batcher.id_batch.SampleIdBatch "fiftyone.core.map.batcher.id_batch.SampleIdBatch")]#
    

Create a list of sample batches

property total: int#
    

Get the total number of samples in the batch

create_subset(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_) → [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]#
    

Create a sample collection from the batch

class fiftyone.core.map.batcher.SampleSliceBatch(_start_idx : int_, _stop_idx : int_)#
    

Bases: [`SampleBatch`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")

Sample batch using slices

**Methods:**

`split`(sample_collection,Â num_workers[,Â ...]) | Create a list of sample batches  
---|---  
`create_subset`(sample_collection) | Create a sample collection from the batch  
  
**Attributes:**

`total` | Get the total number of samples in the batch  
---|---  
  
classmethod split(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _num_workers : int_, _batch_size : int | None = None_) → List[[SampleSliceBatch](api__fiftyone.core.map.batcher.slice_batch.md#fiftyone.core.map.batcher.slice_batch.SampleSliceBatch "fiftyone.core.map.batcher.slice_batch.SampleSliceBatch")]#
    

Create a list of sample batches

property total: int#
    

Get the total number of samples in the batch

create_subset(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_) → [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]#
    

Create a sample collection from the batch

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
