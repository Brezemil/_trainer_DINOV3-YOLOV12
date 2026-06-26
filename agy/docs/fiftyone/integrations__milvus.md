---
source_url: https://docs.voxel51.com/integrations/milvus.html
---

# Milvus Integration#

[Milvus](https://milvus.io/) is one of the most popular vector databases available, and weâve made it easy to use Milvusâs vector search capabilities on your computer vision data directly from FiftyOne!

Follow these simple instructions to get started using Milvus + FiftyOne.

FiftyOne provides an API to create Milvus collections, upload vectors, and run similarity queries, both programmatically in Python and via point-and-click in the App.

Note

Did you know? You can [search by natural language](brain.md#brain-similarity-text) using Milvus similarity indexes!

![object-similarity](../_images/brain-object-similarity.gif)

## Basic recipe#

The basic workflow to use Milvus to create a similarity index on your FiftyOne datasets and use this to query your data is as follows:

  1. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Compute embedding vectors for samples or patches in your dataset, or select a model to use to generate embeddings

  3. Use the [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") methodto generate a Milvus similarity index for the samples or object patches in a dataset by setting the parameter `backend="milvus"` and specifying a `brain_key` of your choice

  4. Use this Milvus similarity index to query your data with [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity")

  5. If desired, delete the index




  
The example below demonstrates this workflow.

Note

You must [connect to a Milvus server](https://milvus.io/docs/install_standalone-docker.md) and install the [Milvus Python client](https://github.com/milvus-io/pymilvus) to run this example:
    
    
    wget https://github.com/milvus-io/milvus/releases/download/v2.2.11/milvus-standalone-docker-compose.yml -O docker-compose.yml
    sudo docker compose up -d
    
    pip install pymilvus
    

Note that, if you are using a custom Milvus server, you can store your credentials as described in this section to avoid entering them manually each time you interact with your Milvus index.

First letâs load a dataset into FiftyOne and compute embeddings for the samples:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5# Step 1: Load your data into FiftyOne
     6dataset = foz.load_zoo_dataset("quickstart")
     7
     8# Steps 2 and 3: Compute embeddings and create a similarity index
     9milvus_index = fob.compute_similarity(
    10    dataset,
    11    brain_key="milvus_index",
    12    backend="milvus",
    13)
    

Once the similarity index has been generated, we can query our data in FiftyOne by specifying the `brain_key`:
    
    
     1# Step 4: Query your data
     2query = dataset.first().id  # query by sample ID
     3view = dataset.sort_by_similarity(
     4    query,
     5    brain_key="milvus_index",
     6    k=10,  # limit to 10 most similar samples
     7)
     8
     9# Step 5 (optional): Cleanup
    10
    11# Delete the Milvus collection
    12milvus_index.cleanup()
    13
    14# Delete run record from FiftyOne
    15dataset.delete_brain_run("milvus_index")
    

Note

Skip to this section to see a variety of common Milvus query patterns.

## Setup#

The easiest way to get started is to [install Milvus standalone via Docker Compose](https://milvus.io/docs/install_standalone-docker.md):
    
    
    wget https://github.com/milvus-io/milvus/releases/download/v2.2.11/milvus-standalone-docker-compose.yml -O docker-compose.yml
    sudo docker compose up -d
    

### Installing the Milvus client#

In order to use the Milvus backend, you must also install the [Milvus Python client](https://github.com/milvus-io/pymilvus):
    
    
    pip install pymilvus
    

### Using the Milvus backend#

By default, calling [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") or [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") will use an sklearn backend.

To use the Milvus backend, simply set the optional `backend` parameter of [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to `"milvus"`:
    
    
    1import fiftyone.brain as fob
    2
    3fob.compute_similarity(..., backend="milvus", ...)
    

Alternatively, you can permanently configure FiftyOne to use the Milvus backend by setting the following environment variable:
    
    
    export FIFTYONE_BRAIN_DEFAULT_SIMILARITY_BACKEND=milvus
    

or by setting the `default_similarity_backend` parameter of your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "default_similarity_backend": "milvus"
    }
    

### Authentication#

If you are using a custom Milvus server, you can provide your credentials in a variety of ways.

**Environment variables (recommended)**

The recommended way to configure your Milvus credentials is to store them in the environment variables shown below, which are automatically accessed by FiftyOne whenever a connection to Milvus is made.
    
    
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_URI=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_USER=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_PASSWORD=XXXXXX
    
    # also available if necessary
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_SECURE=true
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_TOKEN=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_DB_NAME=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_CLIENT_KEY_PATH=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_CLIENT_PEM_PATH=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_CA_PEM_PATH=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_SERVER_PEM_PATH=XXXXXX
    export FIFTYONE_BRAIN_SIMILARITY_MILVUS_SERVER_NAME=XXXXXX
    

**FiftyOne Brain config**

You can also store your credentials in your [brain config](brain.md#brain-config) located at `~/.fiftyone/brain_config.json`:
    
    
    {
        "similarity_backends": {
            "milvus": {
                "uri": "XXXXXX",
                "user": "XXXXXX",
                "password": "XXXXXX",
    
                # also available if necessary
                "secure": true,
                "token": "XXXXXX",
                "db_name": "XXXXXX",
                "client_key_path": "XXXXXX",
                "client_pem_path": "XXXXXX",
                "ca_pem_path": "XXXXXX",
                "server_pem_path": "XXXXXX",
                "server_name": "XXXXXX"
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide your Milvus credentials as keyword arguments each time you call methods like [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") that require connections to Milvus:
    
    
     1import fiftyone.brain as fob
     2
     3milvus_index = fob.compute_similarity(
     4    ...
     5    backend="milvus",
     6    brain_key="milvus_index",
     7    uri="XXXXXX",
     8    user="XXXXXX",
     9    password="XXXXXX",
    10
    11    # also available if necessary
    12    secure=True,
    13    token="XXXXXX",
    14    db_name="XXXXXX",
    15    client_key_path="XXXXXX",
    16    client_pem_path="XXXXXX",
    17    ca_pem_path="XXXXXX",
    18    server_pem_path="XXXXXX",
    19    server_name="XXXXXX",
    20)
    

Note that, when using this strategy, you must manually provide the credentials when loading an index later via [`load_brain_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_brain_results "fiftyone.core.collections.SampleCollection.load_brain_results"):
    
    
     1milvus_index = dataset.load_brain_results(
     2    "milvus_index",
     3    uri="XXXXXX",
     4    user="XXXXXX",
     5    password="XXXXXX",
     6
     7    # also available if necessary
     8    secure=True,
     9    token="XXXXXX",
    10    db_name="XXXXXX",
    11    client_key_path="XXXXXX",
    12    client_pem_path="XXXXXX",
    13    ca_pem_path="XXXXXX",
    14    server_pem_path="XXXXXX",
    15    server_name="XXXXXX",
    16)
    

### Milvus config parameters#

The Milvus backend supports a variety of query parameters that can be used to customize your similarity queries. These parameters include:

  * **collection_name** (_None_): the name of the Milvus collection to use or create. If none is provided, a new collection will be created

  * **metric** (_âdotproductâ_): the embedding distance metric to use when creating a new index. The supported values are `("cosine", "dotproduct", "euclidean")`

  * **consistency_level** (_âSessionâ_): the consistency level to use. Supported values are `("Strong", "Session", "Bounded", "Eventually")`




For detailed information on these parameters, see the [Milvus authentication documentation](https://milvus.io/docs/authenticate.md) and [Milvus consistency levels documentation](https://milvus.io/docs/consistency.md#Consistency-levels).

You can specify these parameters via any of the strategies described in the previous section. Hereâs an example of a [brain config](brain.md#brain-config) that includes all of the available parameters:
    
    
    {
        "similarity_backends": {
            "milvus": {
                "collection_name": "your_collection",
                "metric": "dotproduct",
                "consistency_level": "Strong"
            }
        }
    }
    

However, typically these parameters are directly passed to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to configure a specific new index:
    
    
    1milvus_index = fob.compute_similarity(
    2    ...
    3    backend="milvus",
    4    brain_key="milvus_index",
    5    collection_name="your_collection",
    6    metric="dotproduct",
    7    consistency_level="Strong",
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

Calling [`delete_brain_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_brain_run "fiftyone.core.collections.SampleCollection.delete_brain_run") only deletes the **record** of the brain run from your FiftyOne dataset; it will not delete any associated Milvus collection, which you can do as follows:
    
    
    # Delete the Milvus collection
    milvus_index = dataset.load_brain_results(brain_key)
    milvus_index.cleanup()
    

## Examples#

This section demonstrates how to perform some common vector search workflows on a FiftyOne dataset using the Milvus backend.

Note

All of the examples below assume you have configured your Milvus server and connection as described in this section.

### Create a similarity index#

In order to create a new Milvus similarity index, you need to specify either the `embeddings` or `model` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"). Hereâs a few possibilities:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6model_name = "clip-vit-base32-torch"
     7model = foz.load_zoo_model(model_name)
     8brain_key = "milvus_index"
     9
    10# Option 1: Compute embeddings on the fly from model name
    11fob.compute_similarity(
    12    dataset,
    13    model=model_name,
    14    backend="milvus",
    15    brain_key=brain_key,
    16)
    17
    18# Option 2: Compute embeddings on the fly from model instance
    19fob.compute_similarity(
    20    dataset,
    21    model=model,
    22    backend="milvus",
    23    brain_key=brain_key,
    24)
    25
    26# Option 3: Pass precomputed embeddings as a numpy array
    27embeddings = dataset.compute_embeddings(model)
    28fob.compute_similarity(
    29    dataset,
    30    embeddings=embeddings,
    31    backend="milvus",
    32    brain_key=brain_key,
    33)
    34
    35# Option 4: Pass precomputed embeddings by field name
    36dataset.compute_embeddings(model, embeddings_field="embeddings")
    37fob.compute_similarity(
    38    dataset,
    39    embeddings="embeddings",
    40    backend="milvus",
    41    brain_key=brain_key,
    42)
    

Note

You can customize the Milvus similarity index by passing any supported parameters as extra kwargs.

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
    11    backend="milvus",
    12    brain_key="milvus_patches",
    13)
    

Note

You can customize the Milvus index by passing any supported parameters as extra kwargs.

### Connect to an existing collection#

If you have already created a Milvus collection storing the embedding vectors for the samples or patches in your dataset, you can connect to it by passing the `collection_name` to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity"):
    
    
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
    11    collection_name="your_collection",  # the existing Milvus collection
    12    brain_key="milvus_index",
    13    backend="milvus",
    14)
    

### Add/remove embeddings from an index#

You can use [`add_to_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.add_to_index "fiftyone.brain.similarity.SimilarityIndex.add_to_index") and [`remove_from_index()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.remove_from_index "fiftyone.brain.similarity.SimilarityIndex.remove_from_index") to add and remove embeddings from an existing Milvus similarity index.

These methods can come in handy if you modify your FiftyOne dataset and need to update the Milvus similarity index to reflect these changes:
    
    
     1import numpy as np
     2
     3import fiftyone as fo
     4import fiftyone.brain as fob
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9milvus_index = fob.compute_similarity(
    10    dataset,
    11    model="clip-vit-base32-torch",
    12    brain_key="milvus_index",
    13    backend="milvus",
    14)
    15print(milvus_index.total_index_size)  # 200
    16
    17view = dataset.take(10)
    18ids = view.values("id")
    19
    20# Delete 10 samples from a dataset
    21dataset.delete_samples(view)
    22
    23# Delete the corresponding vectors from the index
    24milvus_index.remove_from_index(sample_ids=ids)
    25
    26# Add 20 samples to a dataset
    27samples = [fo.Sample(filepath="tmp%d.jpg" % i) for i in range(20)]
    28sample_ids = dataset.add_samples(samples)
    29
    30# Add corresponding embeddings to the index
    31embeddings = np.random.rand(20, 512)
    32milvus_index.add_to_index(embeddings, sample_ids)
    33
    34print(milvus_index.total_index_size)  # 210
    

### Retrieve embeddings from an index#

You can use [`get_embeddings()`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex.get_embeddings "fiftyone.brain.similarity.SimilarityIndex.get_embeddings") to retrieve embeddings from a Milvus index by ID:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7milvus_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="milvus_index",
    11    backend="milvus",
    12)
    13
    14# Retrieve embeddings for the entire dataset
    15ids = dataset.values("id")
    16embeddings, sample_ids, _ = milvus_index.get_embeddings(sample_ids=ids)
    17print(embeddings.shape)  # (200, 512)
    18print(sample_ids.shape)  # (200,)
    19
    20# Retrieve embeddings for a view
    21ids = dataset.take(10).values("id")
    22embeddings, sample_ids, _ = milvus_index.get_embeddings(sample_ids=ids)
    23print(embeddings.shape)  # (10, 512)
    24print(sample_ids.shape)  # (10,)
    

### Querying a Milvus index#

You can query a Milvus index by appending a [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage to any dataset or view. The query can be any of the following:

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
    12    brain_key="milvus_index",
    13    backend="milvus",
    14)
    15
    16# Query by vector
    17query = np.random.rand(512)  # matches the dimension of CLIP embeddings
    18view = dataset.sort_by_similarity(query, k=10, brain_key="milvus_index")
    19
    20# Query by sample ID
    21query = dataset.first().id
    22view = dataset.sort_by_similarity(query, k=10, brain_key="milvus_index")
    23
    24# Query by a list of IDs
    25query = [dataset.first().id, dataset.last().id]
    26view = dataset.sort_by_similarity(query, k=10, brain_key="milvus_index")
    27
    28# Query by text prompt
    29query = "a photo of a dog"
    30view = dataset.sort_by_similarity(query, k=10, brain_key="milvus_index")
    

Note

Performing a similarity search on a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") will **only** return results from the view; if the view contains samples that were not included in the index, they will never be included in the result.

This means that you can index an entire [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") once and then perform searches on subsets of the dataset by [constructing views](https://docs.voxel51.com/user_guide/using_views.html#using-views) that contain the images of interest.

### Accessing the Milvus client#

You can use the `collection` property of a Milvus index to directly access the underlying Milvus collection and use its methods as desired:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7milvus_index = fob.compute_similarity(
     8    dataset,
     9    model="clip-vit-base32-torch",
    10    brain_key="milvus_index",
    11    backend="milvus",
    12)
    13
    14print(milvus_index.collection)
    15
    16# The Milvus SDK is already initialized for you as well
    17import pymilvus
    18print(pymilvus.utility.list_collections())
    

### Advanced usage#

As previously mentioned, you can customize your Milvus indexes by providing optional parameters to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").

Hereâs an example of creating a similarity index backed by a customized Milvus similarity index. Just for fun, weâll specify a custom collection name, use euclidean distance, and populate the index for only a subset of our dataset:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7# Create a custom Milvus index
     8milvus_index = fob.compute_similarity(
     9    dataset,
    10    model="clip-vit-base32-torch",
    11    embeddings=False,  # we'll add embeddings below
    12    metric="euclidean",
    13    brain_key="milvus_index",
    14    backend="milvus",
    15    collection_name="custom_milvus_collection",
    16)
    17
    18# Add embeddings for a subset of the dataset
    19view = dataset.take(10)
    20embeddings, sample_ids, _ = milvus_index.compute_embeddings(view)
    21milvus_index.add_to_index(embeddings, sample_ids)
    22
    23print(milvus_index.collection)
    24
    25# The Milvus SDK is already initialized for you as well
    26import pymilvus
    27print(pymilvus.utility.list_collections())
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
