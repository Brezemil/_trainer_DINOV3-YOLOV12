---
source_url: https://docs.voxel51.com/api/fiftyone.core.map.batcher.slice_batch.html
---

# fiftyone.core.map.batcher.slice_batch#

Abstract mapping backend

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SampleSliceBatch`(start_idx,Â stop_idx) | Sample batch using slices  
---|---  
  
class fiftyone.core.map.batcher.slice_batch.SampleSliceBatch(_start_idx : int_, _stop_idx : int_)#
    

Bases: [`SampleBatch`](api__fiftyone.core.map.batcher.batch.md#fiftyone.core.map.batcher.batch.SampleBatch "fiftyone.core.map.batcher.batch.SampleBatch")

Sample batch using slices

**Methods:**

`split`(sample_collection,Â num_workers[,Â ...]) | Create a list of sample batches  
---|---  
`create_subset`(sample_collection) | Create a sample collection from the batch  
  
**Attributes:**

`total` | Get the total number of samples in the batch  
---|---  
  
classmethod split(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_, _num_workers : int_, _batch_size : int | None = None_) → List[SampleSliceBatch]#
    

Create a list of sample batches

property total: int#
    

Get the total number of samples in the batch

create_subset(_sample_collection : [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]_) → [SampleCollection](api__fiftyone.core.map.typing.md#fiftyone.core.map.typing.SampleCollection "fiftyone.core.map.typing.SampleCollection")[T]#
    

Create a sample collection from the batch

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
