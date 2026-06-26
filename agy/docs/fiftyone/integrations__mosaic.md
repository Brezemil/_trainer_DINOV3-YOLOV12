---
source_url: https://docs.voxel51.com/integrations/mosaic.html
---

# Databricks Mosaic AI Integration#

[Mosaic AI Vector Search](https://docs.databricks.com/en/generative-ai/vector-search.html) is a vector database that is built into the Databricks Data Intelligence Platform and integrated with its governance and productivity tools, and weâve made it easy to use Mosaicâs vector search capabilities on your computer vision data directly from FiftyOne!

Follow these simple instructions to get started using Mosaic + FiftyOne.

FiftyOne provides an API to create Mosaic indexes, upload vectors, and run similarity queries, both programmatically in Python and via point-and-click in the App.

Note

Did you know? You can [search by natural language](brain.md#brain-similarity-text) using Mosaic similarity indexes!

![image-similarity](../_images/brain-image-similarity.gif)

## Basic recipe#

The basic workflow to use Mosaic to create a similarity index on your FiftyOne datasets and query your data is as follows:

  1. Connect to your databricks workspace and [create a vector search endpoint](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html#create-a-vector-search-endpoint).

  2. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  3. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings

  4. Use the [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") method to generate a Mosaic similarity index for the samples or object patches in a dataset by setting the parameter `backend="mosaic"` and specifying a `brain_key` of your choice

  5. Use this Mosaic similarity index to query your data with [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity")

  6. If desired, delete the index




  
The example below demonstrates this workflow.

Note

You must have access to a databricks account with [vector search enabled](https://docs.databricks.com/en/generative-ai/vector-search.html#requirements) and install the [Databricks Vector Search Python package](https://api-docs.databricks.com/python/vector-search/databricks.vector_search.html) to run this example:
    
    
    pip install databricks-vectorsearch
    

Note that you need to provide credentials as described in this section to avoid entering them manually each time you interact with your Mosaic index.

First, letâs load a dataset into FiftyOne and compute embeddings for the samples:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5# Step 1: Load your data into FiftyOne
     6dataset = foz.load_zoo_dataset("quickstart")
     7
     8# Steps 2 and 3: Compute embeddings and create a similarity index
     9mosaic_index = fob.compute_similarity(
    10    dataset,
    11    brain_key="mosaic_index",
    12    backend="mosaic",
    13)
    

Once the similarity index has been generated, you can query your data in FiftyOne by specifying the `brain_key`:
    
    
     1# Step 4: Query your data
     2query = dataset.first().id  # query by sample ID
     3view = dataset.sort_by_similarity(
     4    query,
     5    brain_key="mosaic_index",
     6    k=10,  # limit to 10 most similar samples
     7)
     8
     9# Step 5 (optional): Cleanup
    10
    11# Delete the Mosaic index
    12mosaic_index.cleanup()
    13
    14# Delete run record from FiftyOne
    15dataset.delete_brain_run("mosaic_index")
    

Note

Skip to this section for a variety of common Mosaic query patterns.

## Setup#

To get started with Mosaic AI Vector Search, you need to have access to a Databricks workspace which satisfies the [requirements for vector search](https://docs.databricks.com/en/generative-ai/vector-search.html#requirements) and [create a vector search endpoint](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html#create-a-vector-search-endpoint). You also need to have a catalog and schema in Databricks where you want to create the vector search index.

### Installing the Mosaic AI Vector Search client#

In order to use the Mosaic backend, you must also install the [Databricks Vector Search Python package](https://api-docs.databricks.com/python/vector-search/databricks.vector_search.html)
    
    
    pip install databricks-vectorsearch
    

### Using the Mosaic backend#

By default, calling [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") or [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") will use an sklearn backend.

To use the Mosaic backend, simply set the optional `backend` parameter of [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to `"mosaic"`:
    
    
    1import fiftyone.brain as fob
    2
    3fob.compute_similarity(..., backend="mosaic", ...)
    

Alternatively, you can permanently configure FiftyOne to use the Mosaic backend by setting the following environment variable:
    
    
    export FIFTYONE_BRAIN_DEFAULT_SIMILARITY_BACKEND=mosaic
    

or by setting the `default_similarity_backend` parameter of your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "default_similarity_backend": "mosaic"
    }
    

### Authentication#

You can provide your credentials in a [variety of ways](https://docs.databricks.com/en/generative-ai/vector-search.html#data-protection-and-authentication).

**Environment variables (recommended)**

The recommended way to configure your Databricks credentials is to store them in the environment variables shown below, which are automatically accessed by FiftyOne whenever a connection to Databricks is made.
    
    
    export FIFTYONE_BRAIN_SIMILARITY_MOSAIC_WORKSPACE_URL=https://<unique-url>.cloud.databricks.com/
    export FIFTYONE_BRAIN_SIMILARITY_MOSAIC_PERSONAL_ACCESS_TOKEN=XXXXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MOSAIC_CATALOG_NAME=XXXXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MOSAIC_SCHEMA_NAME=XXXXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MOSAIC_ENDPOINT_NAME=XXXXXXXX
    

This is only one example of variables that can be used to authenticate an Mosaic client. Find more information [here.](https://docs.databricks.com/en/generative-ai/vector-search.html#data-protection-and-authentication)

**FiftyOne Brain config**

You can also store your credentials in your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "similarity_backends": {
            "mosaic": {
                "workspace_url": "https://<unique-url>.cloud.databricks.com/",
                "personal_access_token": "XXXXXXXX",
                "catalog_name": "XXXXXXXX",
                "schema_name": "XXXXXXXX",
                "endpoint_name": "XXXXXXXX"
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide credentials as keyword arguments each time you call methods like [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") that require connections to Databricks:
    
    
     1import fiftyone.brain as fob
     2
     3mosaic_index = fob.compute_similarity(
     4    ...
     5    backend="mosaic",
     6    brain_key="mosaic_index",
     7    workspace_url = "https://<unique-url>.cloud.databricks.com/",
     8    personal_access_token = "XXXXXXXX",
     9    catalog_name = "XXXXXXXX",
    10    schema_name = "XXXXXXXX",
    11    endpoint_name = "XXXXXXXX"
    12)
    

Note that, when using this strategy, you must manually provide the credentials when loading an index later via [`load_brain_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_results "fiftyone.core.collections.SampleCollection.load_brain_results"):
    
    
    1mosaic_index = dataset.load_brain_results(
    2    "mosaic_index",
    3    workspace_url = "https://<unique-url>.cloud.databricks.com/",
    4    personal_access_token = "XXXXXXXX",
    5    catalog_name = "XXXXXXXX",
    6    schema_name = "XXXXXXXX",
    7    endpoint_name = "XXXXXXXX"
    8)
    

### Mosaic config parameters#

The Mosaic backend supports the following parameter to customize your similarity queries.

  * **index_name** (_None_): the name of the Mosaic vector search index to use or create. If not specified, a new unique name is generated automatically




You can specify this parameter via any of the strategies described in the previous section. Hereâs an example of a [brain config](brain.md#brain-config) that includes all of the available parameters:
    
    
    {
        "similarity_backends": {
            "mosaic": {
                "index_name": "your-index"
            }
        }
    }
    

However, typically this parameter is directly passed to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to configure a specific new index:
    
    
    1mosaic_index = fob.compute_similarity(
    2    ...
    3    backend="mosaic",
    4    brain_key="mosaic_index",
    5    index_name="your-index",
    6)
    

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

Calling [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") only deletes the **record** of the brain run from your FiftyOne dataset; it will not delete any associated Mosaic index, which you can do as follows:
    
    
    # Delete the Mosaic index
    mosaic_index = dataset.load_brain_results(brain_key)
    mosaic_index.cleanup()
    

## Examples#

This section demonstrates how to perform some common vector search workflows on a FiftyOne dataset using the Mosaic backend.

Note

All of the examples below assume you have configured your Databricks account and credentials as described in this section.

### Create a similarity index#

In order to create a new Mosaic similarity index, you need to specify either the `embeddings` or `model` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"). Here are a few possibilities:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6model_name = "clip-vit-base32-torch"
     7model = foz.load_zoo_model(model_name)
     8brain_key = "mosaic_index"
     9
    10# Option 1: Compute embeddings on the fly from model name
    11fob.compute_similarity(
    12    dataset,
    13    model=model_name,
    14    backend="mosaic",
    15    brain_key=brain_key,
    16)
    17
    18# Option 2: Compute embeddings on the fly from model instance
    19fob.compute_similarity(
    20    dataset,
    21    model=model,
    22    backend="mosaic",
    23    brain_key=brain_key,
    24)
    25
    26# Option 3: Pass pre-computed embeddings as a numpy array
    27embeddings = dataset.compute_embeddings(model)
    28fob.compute_similarity(
    29    dataset,
    30    embeddings=embeddings,
    31    backend="mosaic",
    32    brain_key=brain_key,
    33)
    34
    35# Option 4: Pass pre-computed embeddings by field name
    36dataset.compute_embeddings(model, embeddings_field="embeddings")
    37fob.compute_similarity(
    38    dataset,
    39    embeddings="embeddings",
    40    backend="mosaic",
    41    brain_key=brain_key,
    42)
    

### Create a patch similarity index#

You can also create a similarity index for [object patches](brain.md#brain-object-similarity) within your dataset by including the `patches_field` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
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
    11    backend="mosaic",
    12    brain_key="mosaic_patches",
    13)
    

### Connect to an existing index#

If you have already created a Mosaic index storing the embedding vectors for the samples or patches in your dataset, you can connect to it by passing the `index_name` to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
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
    11    index_name="your-index",            # the existing Mosaic index
    12    brain_key="mosaic_index",
    13    backend="mosaic",
    14)
    

### Add/remove embeddings from an index#

You can use [`add_to_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.add_to_index "fiftyone.brain.similarity.SimilarityIndex.add_to_index") and [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") to add and remove embeddings from an existing Mosaic index, respectively.

These methods can come in handy if you modify your FiftyOne dataset and need to update the Mosaic index to reflect these changes:
    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9mosaic_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="mosaic_index",
    13    backend="mosaic",
    14)
    15print(mosaic_index.total_index_size)  # 200
    16
    17view = dataset.take(10)
    18ids = view.values("id")
    19
    20# Delete 10 samples from a dataset
    21dataset.delete_samples(view)
    22
    23# Delete the corresponding vectors from the index
    24mosaic_index.remove_from_index(sample_ids=ids)
    25
    26# Add 20 samples to a dataset
    27samples = [fo.Sample(filepath="tmp%d.jpg" % i) for i in range(20)]
    28sample_ids = dataset.add_samples(samples)
    29
    30# Add corresponding embeddings to the index
    31embeddings = np.random.rand(20, 512)
    32mosaic_index.add_to_index(embeddings, sample_ids)
    33
    34print(mosaic_index.total_index_size)  # 210
    

### Retrieve embeddings from an index#

You can use [`get_embeddings()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.get_embeddings "fiftyone.brain.similarity.SimilarityIndex.get_embeddings") to retrieve embeddings from a Mosaic index by ID:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7mosaic_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="mosaic_index",
    11    backend="mosaic",
    12)
    13
    14# Retrieve embeddings for the entire dataset
    15ids = dataset.values("id")
    16embeddings, sample_ids, _ = mosaic_index.get_embeddings(sample_ids=ids)
    17print(embeddings.shape)  # (200, 512)
    18print(sample_ids.shape)  # (200,)
    19
    20# Retrieve embeddings for a view
    21ids = dataset.take(10).values("id")
    22embeddings, sample_ids, _ = mosaic_index.get_embeddings(sample_ids=ids)
    23print(embeddings.shape)  # (10, 512)
    24print(sample_ids.shape)  # (10,)
    

### Querying a Mosaic index#

You can query a Mosaic index by appending a [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage to any dataset or view. The query can be any of the following:

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
    12    brain_key="mosaic_index",
    13    backend="mosaic",
    14)
    15
    16# Query by vector
    17query = np.random.rand(512)  # matches the dimension of CLIP embeddings
    18view = dataset.sort_by_similarity(query, k=10, brain_key="mosaic_index")
    19
    20# Query by sample ID
    21query = dataset.first().id
    22view = dataset.sort_by_similarity(query, k=10, brain_key="mosaic_index")
    23
    24# Query by a list of IDs
    25query = [dataset.first().id, dataset.last().id]
    26view = dataset.sort_by_similarity(query, k=10, brain_key="mosaic_index")
    27
    28# Query by text prompt
    29query = "a photo of a dog"
    30view = dataset.sort_by_similarity(query, k=10, brain_key="mosaic_index")
    

Note

Performing a similarity search on a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") will **only** return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") once and then perform searches on subsets of the dataset by [constructing views](https://docs.voxel51.com/user_guide/using_views.html#using-views) that contain the images of interest.

### Accessing the Mosaic client#

You can use the `client` property of a Mosaic index to directly access the underlying Mosaic client instance and use its methods as desired:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7mosaic_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="mosaic_index",
    11    backend="mosaic",
    12)
    13
    14mosaic_client = mosaic_index.client
    15print(mosaic_client)
    

### Advanced usage#

As previously mentioned, you can customize your Mosaic indexes by providing optional parameters to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").

Hereâs an example of creating a similarity index backed by a customized Mosaic index. Just for fun, weâll specify a custom index name and populate the index for only a subset of our dataset:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7# Create a custom Mosaic index
     8mosaic_index = fob.compute_similarity(
     9    dataset,
    10    model="clip-vit-base32-torch",
    11    embeddings=False,  # we'll add embeddings below
    12    brain_key="mosaic_index",
    13    backend="mosaic",
    14    index_name="custom-quickstart-index",
    15)
    16
    17# Add embeddings for a subset of the dataset
    18view = dataset.take(10)
    19embeddings, sample_ids, _ = mosaic_index.compute_embeddings(view)
    20mosaic_index.add_to_index(embeddings, sample_ids)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
