---
source_url: https://docs.voxel51.com/integrations/redis.html
---

# Redis Vector Search Integration#

[Redis](https://redis.com) is the leading open source in-memory data store, and weâve made it easy to use Redisâ [vector search capabilities](https://redis.com/solutions/use-cases/vector-database) on your computer vision data directly from FiftyOne!

Follow these simple instructions to configure a Redis server and get started using Redis + FiftyOne.

FiftyOne provides an API to create Redis vector search indexes, upload vectors, and run similarity queries, both programmatically in Python and via point-and-click in the App.

Note

Did you know? You can [search by natural language](brain.md#brain-similarity-text) using Redis similarity indexes!

![image-similarity](../_images/brain-image-similarity.gif)

## Basic recipe#

The basic workflow to use Redis to create a similarity index on your FiftyOne datasets and use this to query your data is as follows:

  1. Start a Redis service locally

  2. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  3. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings

  4. Use the [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") method to generate a Redis similarity index for the samples or object patches in a dataset by setting the parameter `backend="redis"` and specifying a `brain_key` of your choice

  5. Use this Redis similarity index to query your data with [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity")

  6. If desired, delete the index




  
The example below demonstrates this workflow.

Note

You must [launch a Redis server](https://redis.io/docs/install/install-stack) and install the [Redis Python client](https://github.com/redis/redis-py) to run this example:
    
    
    brew tap redis-stack/redis-stack
    brew install redis-stack
    redis-stack-server
    
    pip install redis
    

Note that, if you are using a custom Redis server, you can store your credentials as described in this section to avoid entering them manually each time you interact with your Redis index.

First letâs load a dataset into FiftyOne and compute embeddings for the samples:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5# Step 1: Load your data into FiftyOne
     6dataset = foz.load_zoo_dataset("quickstart")
     7
     8# Steps 2 and 3: Compute embeddings and create a similarity index
     9redis_index = fob.compute_similarity(
    10    dataset,
    11    brain_key="redis_index",
    12    backend="redis",
    13)
    

Once the similarity index has been generated, we can query our data in FiftyOne by specifying the `brain_key`:
    
    
     1# Step 4: Query your data
     2query = dataset.first().id  # query by sample ID
     3view = dataset.sort_by_similarity(
     4    query,
     5    brain_key="redis_index",
     6    k=10,  # limit to 10 most similar samples
     7)
     8
     9# Step 5 (optional): Cleanup
    10
    11# Delete the Redis vector search index
    12redis_index.cleanup()
    13
    14# Delete run record from FiftyOne
    15dataset.delete_brain_run("redis_index")
    

Note

Skip to this section for a variety of common Redis query patterns.

## Setup#

The easiest way to get started with Redis is to [install Redis Stack](https://redis.io/docs/install/install-stack):
    
    
    brew tap redis-stack/redis-stack
    brew install redis-stack
    redis-stack-server
    

### Installing the Redis client#

In order to use the Redis backend, you must also install the [Redis Python client](https://github.com/redis/redis-py):
    
    
    pip install redis
    

### Using the Redis backend#

By default, calling [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") or [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") will use an sklearn backend.

To use the Redis backend, simply set the optional `backend` parameter of [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to `"redis"`:
    
    
    1import fiftyone.brain as fob
    2
    3fob.compute_similarity(..., backend="redis", ...)
    

Alternatively, you can permanently configure FiftyOne to use the Redis backend by setting the following environment variable:
    
    
    export FIFTYONE_BRAIN_DEFAULT_SIMILARITY_BACKEND=redis
    

or by setting the `default_similarity_backend` parameter of your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "default_similarity_backend": "redis"
    }
    

### Authentication#

If you are using a custom Redis server, you can provide your credentials in a variety of ways.

**Environment variables (recommended)**

The recommended way to configure your Redis credentials is to store them in the environment variables shown below, which are automatically accessed by FiftyOne whenever a connection to Redis is made.
    
    
    export FIFTYONE_BRAIN_SIMILARITY_REDIS_HOST=localhost
    export FIFTYONE_BRAIN_SIMILARITY_REDIS_PORT=6379
    export FIFTYONE_BRAIN_SIMILARITY_REDIS_DB=0
    export FIFTYONE_BRAIN_SIMILARITY_REDIS_USERNAME=username
    export FIFTYONE_BRAIN_SIMILARITY_REDIS_PASSWORD=password
    

**FiftyOne Brain config**

You can also store your credentials in your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "similarity_backends": {
            "redis": {
                "host": "localhost",
                "port": 6379,
                "db": 0,
                "username": "username",
                "password": "password"
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide credentials as keyword arguments each time you call methods like [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") that require connections to Redis:
    
    
     1import fiftyone.brain as fob
     2
     3redis_index = fob.compute_similarity(
     4    ...
     5    backend="redis",
     6    brain_key="redis_index",
     7    host="localhost",
     8    port=6379,
     9    db=0,
    10    username="username",
    11    password="password",
    12)
    

Note that, when using this strategy, you must manually provide the credentials when loading an index later via [`load_brain_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_results "fiftyone.core.collections.SampleCollection.load_brain_results"):
    
    
    1redis_index = dataset.load_brain_results(
    2    "redis_index",
    3    host="localhost",
    4    port=6379,
    5    db=0,
    6    username="username",
    7    password="password",
    8)
    

### Redis config parameters#

The Redis backend supports a variety of query parameters that can be used to customize your similarity queries. These parameters include:

  * **index_name** (_None_): the name of the Redis vector search index to use or create. If not specified, a new unique name is generated automatically

  * **metric** (_âcosineâ_): the distance/similarity metric to use when creating a new index. The supported values are `("cosine", "dotproduct", "euclidean")`

  * **algorithm** (_âFLATâ_): the search algorithm to use. The supported values are `("FLAT", "HNSW")`




For detailed information on these parameters, see the [Redis documentation](https://redis.io/docs/get-started/vector-database).

You can specify these parameters via any of the strategies described in the previous section. Hereâs an example of a [brain config](brain.md#brain-config) that includes all of the available parameters:
    
    
    {
        "similarity_backends": {
            "redis": {
                "index_name": "your-index",
                "metric": "cosine",
                "algorithm": "FLAT"
            }
        }
    }
    

However, typically these parameters are directly passed to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to configure a specific new index:
    
    
    1redis_index = fob.compute_similarity(
    2    ...
    3    backend="redis",
    4    brain_key="redis_index",
    5    index_name="your-index",
    6    metric="cosine",
    7    algorithm="FLAT",
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

Calling [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") only deletes the **record** of the brain run from your FiftyOne dataset; it will not delete any associated Redis index, which you can do as follows:
    
    
    # Delete the Redis vector search index
    redis_index = dataset.load_brain_results(brain_key)
    redis_index.cleanup()
    

## Examples#

This section demonstrates how to perform some common vector search workflows on a FiftyOne dataset using the Redis backend.

Note

All of the examples below assume you have configured your Redis server as described in this section.

### Create a similarity index#

In order to create a new Redis similarity index, you need to specify either the `embeddings` or `model` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"). Hereâs a few possibilities:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6model_name = "clip-vit-base32-torch"
     7model = foz.load_zoo_model(model_name)
     8brain_key = "redis_index"
     9
    10# Option 1: Compute embeddings on the fly from model name
    11fob.compute_similarity(
    12    dataset,
    13    model=model_name,
    14    backend="redis",
    15    brain_key=brain_key,
    16)
    17
    18# Option 2: Compute embeddings on the fly from model instance
    19fob.compute_similarity(
    20    dataset,
    21    model=model,
    22    backend="redis",
    23    brain_key=brain_key,
    24)
    25
    26# Option 3: Pass precomputed embeddings as a numpy array
    27embeddings = dataset.compute_embeddings(model)
    28fob.compute_similarity(
    29    dataset,
    30    embeddings=embeddings,
    31    backend="redis",
    32    brain_key=brain_key,
    33)
    34
    35# Option 4: Pass precomputed embeddings by field name
    36dataset.compute_embeddings(model, embeddings_field="embeddings")
    37fob.compute_similarity(
    38    dataset,
    39    embeddings="embeddings",
    40    backend="redis",
    41    brain_key=brain_key,
    42)
    

Note

You can customize the Redis index by passing any supported parameters as extra kwargs.

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
    11    backend="redis",
    12    brain_key="redis_patches",
    13)
    

Note

You can customize the Redis index by passing any supported parameters as extra kwargs.

### Connect to an existing index#

If you have already created a Redis index storing the embedding vectors for the samples or patches in your dataset, you can connect to it by passing the `index_name` to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
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
    11    index_name="your-index",            # the existing Redis index
    12    brain_key="redis_index",
    13    backend="redis",
    14)
    

### Add/remove embeddings from an index#

You can use [`add_to_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.add_to_index "fiftyone.brain.similarity.SimilarityIndex.add_to_index") and [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") to add and remove embeddings from an existing Redis index.

These methods can come in handy if you modify your FiftyOne dataset and need to update the Redis index to reflect these changes:
    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9redis_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="redis_index",
    13    backend="redis",
    14)
    15print(redis_index.total_index_size)  # 200
    16
    17view = dataset.take(10)
    18ids = view.values("id")
    19
    20# Delete 10 samples from a dataset
    21dataset.delete_samples(view)
    22
    23# Delete the corresponding vectors from the index
    24redis_index.remove_from_index(sample_ids=ids)
    25
    26# Add 20 samples to a dataset
    27samples = [fo.Sample(filepath="tmp%d.jpg" % i) for i in range(20)]
    28sample_ids = dataset.add_samples(samples)
    29
    30# Add corresponding embeddings to the index
    31embeddings = np.random.rand(20, 512)
    32redis_index.add_to_index(embeddings, sample_ids)
    33
    34print(redis_index.total_index_size)  # 210
    

### Retrieve embeddings from an index#

You can use [`get_embeddings()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.get_embeddings "fiftyone.brain.similarity.SimilarityIndex.get_embeddings") to retrieve embeddings from a Redis index by ID:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7redis_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="redis_index",
    11    backend="redis",
    12)
    13
    14# Retrieve embeddings for the entire dataset
    15ids = dataset.values("id")
    16embeddings, sample_ids, _ = redis_index.get_embeddings(sample_ids=ids)
    17print(embeddings.shape)  # (200, 512)
    18print(sample_ids.shape)  # (200,)
    19
    20# Retrieve embeddings for a view
    21ids = dataset.take(10).values("id")
    22embeddings, sample_ids, _ = redis_index.get_embeddings(sample_ids=ids)
    23print(embeddings.shape)  # (10, 512)
    24print(sample_ids.shape)  # (10,)
    

### Querying a Redis index#

You can query a Redis index by appending a [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage to any dataset or view. The query can be any of the following:

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
    12    brain_key="redis_index",
    13    backend="redis",
    14)
    15
    16# Query by vector
    17query = np.random.rand(512)  # matches the dimension of CLIP embeddings
    18view = dataset.sort_by_similarity(query, k=10, brain_key="redis_index")
    19
    20# Query by sample ID
    21query = dataset.first().id
    22view = dataset.sort_by_similarity(query, k=10, brain_key="redis_index")
    23
    24# Query by a list of IDs
    25query = [dataset.first().id, dataset.last().id]
    26view = dataset.sort_by_similarity(query, k=10, brain_key="redis_index")
    27
    28# Query by text prompt
    29query = "a photo of a dog"
    30view = dataset.sort_by_similarity(query, k=10, brain_key="redis_index")
    

Note

Performing a similarity search on a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") will **only** return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") once and then perform searches on subsets of the dataset by [constructing views](https://docs.voxel51.com/user_guide/using_views.html#using-views) that contain the images of interest.

### Accessing the Redis client#

You can use the `client` property of a Redis index to directly access the underlying Redis client instance and use its methods as desired:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7redis_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="redis_index",
    11    backend="redis",
    12)
    13
    14redis_client = redis_index.client
    15index_name = redis_index.config.index_name
    16print(redis_client)
    17print(redis_client.ft(index_name).info())
    

### Advanced usage#

As previously mentioned, you can customize your Redis index by providing optional parameters to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").

In particular, the `algorithm` parameter may impact the quality of your query results, as well as the time and memory required to perform approximate nearest neighbor searches.

Hereâs an example of creating a similarity index backed by a customized Redis index. Just for fun, weâll specify a custom index name, use dot product similarity, and populate the index for only a subset of our dataset:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7# Create a custom Redis index
     8redis_index = fob.compute_similarity(
     9    dataset,
    10    model="clip-vit-base32-torch",
    11    embeddings=False,  # we'll add embeddings below
    12    brain_key="redis_index",
    13    backend="redis",
    14    index_name="custom-quickstart-index",
    15    metric="dotproduct",
    16    algorithm="HNSW",
    17)
    18
    19# Add embeddings for a subset of the dataset
    20view = dataset.take(10)
    21embeddings, sample_ids, _ = redis_index.compute_embeddings(view)
    22redis_index.add_to_index(embeddings, sample_ids)
    23
    24redis_client = redis_index.client
    25index_name = redis_index.config.index_name
    26print(redis_client.ft(index_name).info())
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
