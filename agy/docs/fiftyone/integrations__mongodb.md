---
source_url: https://docs.voxel51.com/integrations/mongodb.html
---

# MongoDB Vector Search Integration#

[MongoDB](https://www.mongodb.com) is the leading open source database for unstructured data, and weâve made it easy to use MongoDB Atlasâ [vector search capabilities](https://www.mongodb.com/products/platform/atlas-vector-search) on your computer vision data directly from FiftyOne!

Follow these simple instructions to configure a MongoDB Atlas cluster and get started using MongoDB Atlas + FiftyOne.

FiftyOne provides an API to create MongoDB Atlas vector search indexes, upload vectors, and run similarity queries, both programmatically in Python and via point-and-click in the App.

Note

Did you know? You can [search by natural language](brain.md#brain-similarity-text) using MongoDB similarity indexes!

![image-similarity](../_images/brain-image-similarity.gif)

## Basic recipe#

The basic workflow to use MongoDB Atlas to create a similarity index on your FiftyOne datasets and use this to query your data is as follows:

  1. Configure a MongoDB Atlas cluster

  2. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  3. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings

  4. Use the [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") method to generate a MongoDB similarity index for the samples or object patches in a dataset by setting the parameter `backend="mongodb"` and specifying a `brain_key` of your choice

  5. Use this MongoDB similarity index to query your data with [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity")

  6. If desired, delete the index




  
The example below demonstrates this workflow.

Note

You must configure a MongoDB Atlas 7.0 or later cluster and provide its [connection string](user_guide__config.md#configuring-mongodb-connection) to run this example:
    
    
    export FIFTYONE_DATABASE_NAME=fiftyone
    export FIFTYONE_DATABASE_URI='mongodb+srv://$USERNAME:$PASSWORD@fiftyone.XXXXXX.mongodb.net/?retryWrites=true&w=majority'
    

First letâs load a dataset into FiftyOne and compute embeddings for the samples:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5# Step 1: Load your data into FiftyOne
     6dataset = foz.load_zoo_dataset("quickstart")
     7
     8# Steps 2 and 3: Compute embeddings and create a similarity index
     9mongodb_index = fob.compute_similarity(
    10    dataset,
    11    embeddings="embeddings",  # the field in which to store the embeddings
    12    brain_key="mongodb_index",
    13    backend="mongodb",
    14)
    

Once the similarity index has been generated, we can query our data in FiftyOne by specifying the `brain_key`:
    
    
     1# Wait for the index to be ready for querying...
     2assert mongodb_index.ready
     3
     4# Step 4: Query your data
     5query = dataset.first().id  # query by sample ID
     6view = dataset.sort_by_similarity(
     7    query,
     8    brain_key="mongodb_index",
     9    k=10,  # limit to 10 most similar samples
    10)
    11
    12# Step 5 (optional): Cleanup
    13
    14# Delete the MongoDB vector search index
    15mongodb_index.cleanup()
    16
    17# Delete run record from FiftyOne
    18dataset.delete_brain_run("mongodb_index")
    

Note

Skip to this section for a variety of common MongoDB query patterns.

## Setup#

In order to use MongoDB vector search, you must connect your FiftyOne installation to MongoDB Atlas, which you can do by navigating to <https://cloud.mongodb.com>, creating an account, and following the instructions there to configure your cluster.

Note

You must be running MongoDB Atlas 7.0 or later in order to programmatically create vector search indexes ([source](https://www.mongodb.com/docs/manual/release-notes/7.0/#atlas-search-index-management)).

As of this writing, Atlasâ shared tier (M0, M2, M5) is running MongoDB 6. In order to use MongoDB 7, you must upgrade to an M10 cluster, which starts at $0.08/hour.

### Configuring your connection string#

You can connect FiftyOne to your MongoDB Atlas cluster by simply providing its [connection string](user_guide__config.md#configuring-mongodb-connection):
    
    
    export FIFTYONE_DATABASE_NAME=fiftyone
    export FIFTYONE_DATABASE_URI='mongodb+srv://$USERNAME:$PASSWORD@fiftyone.XXXXXX.mongodb.net/?retryWrites=true&w=majority'
    

### Using the MongoDB backend#

By default, calling [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") or [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") will use an sklearn backend.

To use the MongoDB backend, simply set the optional `backend` parameter of [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to `"mongodb"`:
    
    
    1import fiftyone.brain as fob
    2
    3fob.compute_similarity(..., backend="mongodb", ...)
    

Alternatively, you can permanently configure FiftyOne to use the MonogDB backend by setting the following environment variable:
    
    
    export FIFTYONE_BRAIN_DEFAULT_SIMILARITY_BACKEND=mongodb
    

or by setting the `default_similarity_backend` parameter of your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "default_similarity_backend": "mongodb"
    }
    

### MongoDB config parameters#

The MongoDB backend supports a variety of query parameters that can be used to customize your similarity queries. These parameters include:

  * **index_name** (_None_): the name of the MongoDB vector search index to use or create. If not specified, a new unique name is generated automatically

  * **metric** (_âcosineâ_): the distance/similarity metric to use when creating a new index. The supported values are `("cosine", "dotproduct", "euclidean")`




For detailed information on these parameters, see the [MongoDB documentation](https://www.mongodb.com/docs/atlas/atlas-search/field-types/knn-vector).

You can specify these parameters via any of the strategies described in the previous section. Hereâs an example of a [brain config](brain.md#brain-config) that includes all of the available parameters:
    
    
    {
        "similarity_backends": {
            "mongodb": {
                "index_name": "your-index",
                "metric": "cosine"
            }
        }
    }
    

However, typically these parameters are directly passed to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to configure a specific new index:
    
    
    1mongodb_index = fob.compute_similarity(
    2    ...
    3    backend="mongodb",
    4    brain_key="mongodb_index",
    5    index_name="your-index",
    6    metric="cosine",
    7)
    

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

Calling [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") only deletes the **record** of the brain run from your FiftyOne dataset; it will not delete any associated MongoDB vector search index, which you can do as follows:
    
    
    # Delete the MongoDB vector search index
    mongodb_index = dataset.load_brain_results(brain_key)
    mongodb_index.cleanup()
    

## Examples#

This section demonstrates how to perform some common vector search workflows on a FiftyOne dataset using the MongoDB backend.

Note

All of the examples below assume you have configured your MongoDB Atlas cluster as described in this section.

### Create a similarity index#

In order to create a new MongoDB similarity index, you need to specify either the `embeddings` or `model` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"). Hereâs a few possibilities:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6model_name = "clip-vit-base32-torch"
     7model = foz.load_zoo_model(model_name)
     8brain_key = "mongodb_index"
     9
    10# Option 1: Compute embeddings on the fly from model name
    11fob.compute_similarity(
    12    dataset,
    13    model=model_name,
    14    embeddings="embeddings",  # the field in which to store the embeddings
    15    backend="mongodb",
    16    brain_key=brain_key,
    17)
    18
    19# Option 2: Compute embeddings on the fly from model instance
    20fob.compute_similarity(
    21    dataset,
    22    model=model,
    23    embeddings="embeddings",  # the field in which to store the embeddings
    24    backend="mongodb",
    25    brain_key=brain_key,
    26)
    27
    28# Option 3: Pass precomputed embeddings as a numpy array
    29embeddings = dataset.compute_embeddings(model)
    30fob.compute_similarity(
    31    dataset,
    32    embeddings=embeddings,
    33    embeddings_field="embeddings",  # the field in which to store the embeddings
    34    backend="mongodb",
    35    brain_key=brain_key,
    36)
    37
    38# Option 4: Pass precomputed embeddings by field name
    39# Note that MongoDB vector indexes require list fields
    40embeddings = dataset.compute_embeddings(model)
    41dataset.set_values("embeddings", embeddings.tolist())
    42fob.compute_similarity(
    43    dataset,
    44    embeddings="embeddings",  # the field that contains the embeddings
    45    backend="mongodb",
    46    brain_key=brain_key,
    47)
    

Note

You can customize the MongoDB index by passing any supported parameters as extra kwargs.

### Create a patch similarity index#

Warning

The MongoDB backend does not yet support indexing object patches, so the code below will not yet run. Check back soon!

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
    11    embeddings="embeddings",  # the attribute in which to store the embeddings
    12    backend="mongodb",
    13    brain_key="mongodb_patches",
    14)
    

Note

You can customize the MongoDB index by passing any supported parameters as extra kwargs.

### Connect to an existing index#

If you have already created a MongoDB index storing the embedding vectors for the samples or patches in your dataset, you can connect to it by passing the `index_name` to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
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
    11    index_name="your-index",            # the existing MongoDB index
    12    brain_key="mongodb_index",
    13    backend="mongodb",
    14)
    

### Add/remove embeddings from an index#

You can use [`add_to_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.add_to_index "fiftyone.brain.similarity.SimilarityIndex.add_to_index") and [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") to add and remove embeddings from an existing Mongodb index.

These methods can come in handy if you modify your FiftyOne dataset and need to update the Mongodb index to reflect these changes:
    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9mongodb_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    embeddings="embeddings",  # the field in which to store the embeddings
    13    brain_key="mongodb_index",
    14    backend="mongodb",
    15)
    16print(mongodb_index.total_index_size)  # 200
    17
    18view = dataset.take(10)
    19ids = view.values("id")
    20
    21# Delete 10 samples from a dataset
    22dataset.delete_samples(view)
    23
    24# Delete the corresponding vectors from the index
    25mongodb_index.remove_from_index(sample_ids=ids)
    26
    27# Add 20 samples to a dataset
    28samples = [fo.Sample(filepath="tmp%d.jpg" % i) for i in range(20)]
    29sample_ids = dataset.add_samples(samples)
    30
    31# Add corresponding embeddings to the index
    32embeddings = np.random.rand(20, 512)
    33mongodb_index.add_to_index(embeddings, sample_ids)
    34
    35print(mongodb_index.total_index_size)  # 210
    

### Retrieve embeddings from an index#

You can use [`get_embeddings()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.get_embeddings "fiftyone.brain.similarity.SimilarityIndex.get_embeddings") to retrieve embeddings from a Mongodb index by ID:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7mongodb_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    embeddings="embeddings",  # the field in which to store the embeddings
    11    brain_key="mongodb_index",
    12    backend="mongodb",
    13)
    14
    15# Retrieve embeddings for the entire dataset
    16ids = dataset.values("id")
    17embeddings, sample_ids, _ = mongodb_index.get_embeddings(sample_ids=ids)
    18print(embeddings.shape)  # (200, 512)
    19print(sample_ids.shape)  # (200,)
    20
    21# Retrieve embeddings for a view
    22ids = dataset.take(10).values("id")
    23embeddings, sample_ids, _ = mongodb_index.get_embeddings(sample_ids=ids)
    24print(embeddings.shape)  # (10, 512)
    25print(sample_ids.shape)  # (10,)
    

### Querying a MongoDB index#

You can query a MongoDB index by appending a [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage to any dataset or view. The query can be any of the following:

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
     9mongodb_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    embeddings="embeddings",  # the field in which to store the embeddings
    13    brain_key="mongodb_index",
    14    backend="mongodb",
    15)
    16
    17# Wait for the index to be ready for querying...
    18assert mongodb_index.ready
    19
    20# Query by vector
    21query = np.random.rand(512)  # matches the dimension of CLIP embeddings
    22view = dataset.sort_by_similarity(query, k=10, brain_key="mongodb_index")
    23
    24# Query by sample ID
    25query = dataset.first().id
    26view = dataset.sort_by_similarity(query, k=10, brain_key="mongodb_index")
    27
    28# Query by a list of IDs
    29query = [dataset.first().id, dataset.last().id]
    30view = dataset.sort_by_similarity(query, k=10, brain_key="mongodb_index")
    31
    32# Query by text prompt
    33query = "a photo of a dog"
    34view = dataset.sort_by_similarity(query, k=10, brain_key="mongodb_index")
    

Note

Performing a similarity search on a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") will **only** return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") once and then perform searches on subsets of the dataset by [constructing views](https://docs.voxel51.com/user_guide/using_views.html#using-views) that contain the images of interest.

### Checking if an index is ready#

You can use the `ready` property of a MongoDB index to check whether a newly created vector search index is ready for querying:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7mongodb_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    embeddings="embeddings",  # the field in which to store the embeddings
    11    brain_key="mongodb_index",
    12    backend="mongodb",
    13)
    14
    15# Wait for the index to be ready for querying...
    16assert mongodb_index.ready
    

### Advanced usage#

As previously mentioned, you can customize your MongoDB index by providing optional parameters to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").

Hereâs an example of creating a similarity index backed by a customized MongoDB index. Just for fun, weâll specify a custom index name, use dot product similarity, and populate the index for only a subset of our dataset:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7# Create a custom MongoDB index
     8mongodb_index = fob.compute_similarity(
     9    dataset,
    10    model="clip-vit-base32-torch",
    11    embeddings_field="embeddings",  # the field in which to store the embeddings
    12    embeddings=False,               # add embeddings later
    13    brain_key="mongodb_index",
    14    backend="mongodb",
    15    index_name="custom-quickstart-index",
    16    metric="dotproduct",
    17)
    18
    19# Add embeddings for a subset of the dataset
    20view = dataset[:20]
    21embeddings, sample_ids, _ = mongodb_index.compute_embeddings(view)
    22mongodb_index.add_to_index(embeddings, sample_ids)
    23
    24print(mongodb_index.total_index_size)  # 20
    25print(mongodb_index.config.index_name)  # custom-quickstart-index
    26print(mongodb_index.config.metric)  # dotproduct
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
