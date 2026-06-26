---
source_url: https://docs.voxel51.com/integrations/lancedb.html
---

# LanceDB Integration#

[LanceDB](https://www.lancedb.com) is a serverless vector database with deep integrations with the Python ecosystem. It requires no setup and is free to use.

FiftyOne provides an API to create LanceDB tables and run similarity queries, both programmatically in Python and via point-and-click in the App.

## Basic recipe#

The basic workflow to use LanceDB to create a similarity index on your FiftyOne datasets and use this to query your data is as follows:

  1. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings

  3. Use the [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") method to generate a LanceDB table for the samples or object patches embeddings in a dataset by setting the parameter `backend="lancedb"` and specifying a `brain_key` of your choice

  4. Use this LanceDB table to query your data with [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity")

  5. If desired, delete the table




  
The example below demonstrates this workflow.

Note

You must install the [LanceDB Python client](https://github.com/lancedb/lancedb) to run this example:
    
    
    pip install lancedb
    

Note that, if you are using a custom LanceDB URI, you can store your credentials as described in this section to avoid entering them manually each time you interact with your LanceDB index.
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5# Step 1: Load your data into FiftyOne
     6dataset = foz.load_zoo_dataset("quickstart")
     7
     8# Steps 2 and 3: Compute embeddings and create a similarity index
     9lancedb_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="lancedb_index",
    13    backend="lancedb",
    14)
    

Once the similarity index has been generated, we can query our data in FiftyOne by specifying the `brain_key`:
    
    
     1# Step 4: Query your data
     2query = dataset.first().id  # query by sample ID
     3view = dataset.sort_by_similarity(
     4    query,
     5    brain_key="lancedb_index",
     6    k=10,  # limit to 10 most similar samples
     7)
     8
     9# Step 5 (optional): Cleanup
    10
    11# Delete the LanceDB table
    12lancedb_index.cleanup()
    13
    14# Delete run record from FiftyOne
    15dataset.delete_brain_run("lancedb_index")
    

## Setup#

You can get started using LanceDB by simply installing the [LanceDB Python client](https://github.com/lancedb/lancedb):
    
    
    pip install lancedb
    

### Using the LanceDB backend#

By default, calling [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") or [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") will use an sklearn backend.

To use the LanceDB backend, simply set the optional `backend` parameter of [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to `"lancedb"`:
    
    
    1import fiftyone.brain as fob
    2
    3fob.compute_similarity(..., backend="lancedb", ...)
    

Alternatively, you can permanently configure FiftyOne to use the LanceDB backend by setting the following environment variable:
    
    
    export FIFTYONE_BRAIN_DEFAULT_SIMILARITY_BACKEND=lancedb
    

or by setting the `default_similarity_backend` parameter of your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "default_similarity_backend": "lancedb"
    }
    

### LanceDB config parameters#

The LanceDB backend supports query parameters that can be used to customize your similarity queries. These parameters include:

  * **table_name** (_None_): the name of the LanceDB table to use. If none is provided, a new table will be created

  * **metric** (_âcosineâ_): the embedding distance metric to use when creating a new table. The supported values are `("cosine", "euclidean")`

  * **uri** (_â/tmp/lancedbâ_): the database URI to use




You can specify these parameters via any of the strategies described in the previous section. Hereâs an example of a [brain config](brain.md#brain-config) that includes all of the available parameters:
    
    
    {
        "similarity_backends": {
            "lancedb": {
                "table_name": "your-table",
                "metric": "euclidean",
                "uri": "/tmp/lancedb"
            }
        }
    }
    

However, typically these parameters are directly passed to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to configure a specific new index:
    
    
    1lancedb_index = fob.compute_similarity(
    2    ...
    3    backend="lancedb",
    4    brain_key="lancedb_index",
    5    table_name="your-table",
    6    metric="euclidean",
    7    uri="/tmp/lancedb",
    8)
    

## Managing brain runs#

FiftyOne provides a variety of methods that you can use to manage brain runs.

For example, you can call [`list_brain_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_brain_runs "fiftyone.core.collections.SampleCollection.list_brain_runs") to see the available brain keys on a dataset:
    
    
     1import fiftyone.brain as fob
     2
     3# List all brain runs
     4dataset.list_brain_runs()
     5
     6# Only list similarity runs
     7dataset.list_brain_runs(type=fob.Similarity)
     8
     9# Only list specific similarity runs
    10dataset.list_brain_runs(
    11    type=fob.Similarity,
    12    patches_field="ground_truth",
    13    supports_prompts=True,
    14)
    

Or, you can use [`get_brain_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_brain_info "fiftyone.core.collections.SampleCollection.get_brain_info") to retrieve information about the configuration of a brain run:
    
    
    1info = dataset.get_brain_info(brain_key)
    2print(info)
    

Use [`load_brain_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_results "fiftyone.core.collections.SampleCollection.load_brain_results") to load the [`SimilarityIndex`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex "fiftyone.brain.similarity.SimilarityIndex") instance for a brain run.

You can use [`rename_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_brain_run "fiftyone.core.collections.SampleCollection.rename_brain_run") to rename the brain key associated with an existing similarity results run:
    
    
    1dataset.rename_brain_run(brain_key, new_brain_key)
    

Finally, you can use [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") to delete the record of a similarity index computation from your FiftyOne dataset:
    
    
    1dataset.delete_brain_run(brain_key)
    

Note

Calling [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") only deletes the **record** of the brain run from your FiftyOne dataset; it will not delete any associated LanceDB table, which you can do as follows:
    
    
    # Delete the LanceDB table
    lancedb_index = dataset.load_brain_results(brain_key)
    lancedb_index.cleanup()
    

## Examples#

This section demonstrates how to perform some common vector search workflows on a FiftyOne dataset using the LanceDB backend.

### Create a similarity index#

In order to create a new LanceDB similarity index, you need to specify either the `embeddings` or `model` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"). Hereâs a few possibilities:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6model_name = "clip-vit-base32-torch"
     7model = foz.load_zoo_model(model_name)
     8brain_key = "lancedb_index"
     9
    10# Option 1: Compute embeddings on the fly from model name
    11fob.compute_similarity(
    12    dataset,
    13    model=model_name,
    14    backend="lancedb",
    15    brain_key=brain_key,
    16)
    17
    18# Option 2: Compute embeddings on the fly from model instance
    19fob.compute_similarity(
    20    dataset,
    21    model=model,
    22    backend="lancedb",
    23    brain_key=brain_key,
    24)
    25
    26# Option 3: Pass precomputed embeddings as a numpy array
    27embeddings = dataset.compute_embeddings(model)
    28fob.compute_similarity(
    29    dataset,
    30    embeddings=embeddings,
    31    backend="lancedb",
    32    brain_key=brain_key,
    33)
    34
    35# Option 4: Pass precomputed embeddings by field name
    36dataset.compute_embeddings(model, embeddings_field="embeddings")
    37fob.compute_similarity(
    38    dataset,
    39    embeddings="embeddings",
    40    backend="lancedb",
    41    brain_key=brain_key,
    42)
    

Note

You can customize the LanceDB index by passing any supported parameters as extra kwargs.

### Create a patch similarity index#

You can also create a similarity index for [object patches](brain.md#brain-object-similarity) within your dataset by specifying a `patches_field` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7fob.compute_similarity(
     8    dataset,
     9    patches_field="ground_truth",
    10    model="clip-vit-base32-torch",
    11    backend="lancedb",
    12    brain_key="lancedb_index",
    13)
    

Note

You can customize the LanceDB index by passing any supported parameters as extra kwargs.

### Connect to an existing index#

If you have already created a LanceDB table storing the embedding vectors for the samples or patches in your dataset, you can connect to it by passing the `table_name` to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",      # zoo model used (if applicable)
    10    embeddings=False,                   # don't compute embeddings
    11    table_name="your-table",            # the existing LanceDB table
    12    brain_key="lancedb_index",
    13    backend="lancedb",
    14)
    

### Add/remove embeddings from an index#

You can use [`add_to_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.add_to_index "fiftyone.brain.similarity.SimilarityIndex.add_to_index") and [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") to add and remove embeddings from an existing Lancedb index.

These methods can come in handy if you modify your FiftyOne dataset and need to update the LanceDB index to reflect these changes:
    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9lancedb_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="lancedb_index",
    13    backend="lancedb",
    14)
    15print(lancedb_index.total_index_size)  # 200
    16
    17view = dataset.take(10)
    18ids = view.values("id")
    19
    20# Delete 10 samples from a dataset
    21dataset.delete_samples(view)
    22
    23# Delete the corresponding vectors from the index
    24lancedb_index.remove_from_index(sample_ids=ids)
    25
    26# Add 20 samples to a dataset
    27samples = [fo.Sample(filepath="tmp%d.jpg" % i) for i in range(20)]
    28sample_ids = dataset.add_samples(samples)
    29
    30# Add corresponding embeddings to the index
    31embeddings = np.random.rand(20, 512)
    32lancedb_index.add_to_index(embeddings, sample_ids)
    33
    34print(lancedb_index.total_index_size)  # 210
    

### Retrieve embeddings from an index#

You can use [`get_embeddings()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.get_embeddings "fiftyone.brain.similarity.SimilarityIndex.get_embeddings") to retrieve embeddings from a LanceDB index by ID:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7lancedb_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="lancedb_index",
    11    backend="lancedb",
    12)
    13
    14# Retrieve embeddings for the entire dataset
    15ids = dataset.values("id")
    16embeddings, sample_ids, _ = lancedb_index.get_embeddings(sample_ids=ids)
    17print(embeddings.shape)  # (200, 512)
    18print(sample_ids.shape)  # (200,)
    19
    20# Retrieve embeddings for a view
    21ids = dataset.take(10).values("id")
    22embeddings, sample_ids, _ = lancedb_index.get_embeddings(sample_ids=ids)
    23print(embeddings.shape)  # (10, 512)
    24print(sample_ids.shape)  # (10,)
    

### Querying a LanceDB index#

You can query a LanceDB index by appending a [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage to any dataset or view. The query can be any of the following:

  * An ID (sample or patch)

  * A query vector of same dimension as the index

  * A list of IDs (samples or patches)

  * A text prompt (if [supported by the model](brain.md#brain-similarity-text))



    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="lancedb_index",
    13    backend="lancedb",
    14)
    15
    16# Query by vector
    17query = np.random.rand(512)  # matches the dimension of CLIP embeddings
    18view = dataset.sort_by_similarity(query, k=10, brain_key="lancedb_index")
    19
    20# Query by sample ID
    21query = dataset.first().id
    22view = dataset.sort_by_similarity(query, k=10, brain_key="lancedb_index")
    23
    24# Query by a list of IDs
    25query = [dataset.first().id, dataset.last().id]
    26view = dataset.sort_by_similarity(query, k=10, brain_key="lancedb_index")
    27
    28# Query by text prompt
    29query = "a photo of a dog"
    30view = dataset.sort_by_similarity(query, k=10, brain_key="lancedb_index")
    

Note

Performing a similarity search on a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") will **only** return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") once and then perform searches on subsets of the dataset by [constructing views](https://docs.voxel51.com/user_guide/using_views.html#using-views) that contain the images of interest.

### Advanced usage#

LanceDB is compatible with the Python ecosystem and can be used with pandas, numpy, and arrow:
    
    
    1lancedb_index = fob.compute_similarity(..., backend="lancedb", ...)
    2
    3# Retrieve the raw LanceDB table
    4table = lancedb_index.table
    5
    6df = table.to_pandas()  # get the table as a pandas dataframe
    7pa = table.to_arrow()   # get the table as an arrow table
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
