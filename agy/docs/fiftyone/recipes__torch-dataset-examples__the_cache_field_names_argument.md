---
source_url: https://docs.voxel51.com/recipes/torch-dataset-examples/the_cache_field_names_argument.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/recipes/torch-dataset-examples/the_cache_field_names_argument.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/recipes/torch-dataset-examples/the_cache_field_names_argument.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/recipes/torch-dataset-examples/the_cache_field_names_argument.ipynb)

# Speed Up FiftyOneTorchDataset with Cached Fields#

This recipe demonstrates how to improve data loading performance when using FiftyOne datasets in PyTorch by preloading specific fields into memory. Instead of querying the database at runtime, you can cache fields (such as id, filepath, or detections) for faster iteration during training. Specifically, it covers:

  * Loading a dataset and creating a subset view
  * Using the SimpleGetItem wrapper class with `vectorize=True` to specify which fields to cache
  * Understanding how cached fields change the input to your `get_item` function
  * Building a new `get_item` that works with cached dicts for efficient training



## Setup#

If you havenât already, install FiftyOne:
    
    
    [ ]:
    
    
    
    !pip install fiftyone
    

In this tutorial, weâll use [PyTorch](https://pytorch.org/) for working with tensors and inspecting sample data. To follow along, youâll need to install `torch` and `torchvision`, if necessary:
    
    
    [ ]:
    
    
    
    !pip install torch torchvision
    

## Import Libraries#
    
    
    [ ]:
    
    
    
    %load_ext autoreload
    %autoreload 2
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone.utils.torch import FiftyOneTorchDataset
    import urllib.request
    

This recipe requires a helper file, utils.py, which contains reusable functions for building get_item methods, creating dataloaders, and setting up models. The following cell will automatically download the file into your working directory so it can be imported directly.
    
    
    [ ]:
    
    
    
    url = "https://cdn.voxel51.com/tutorials_torch_dataset_examples/notebook_the_cache_field_names_argument/utils.py"
    urllib.request.urlretrieve(url, "utils.py")
    
    
    
    [2]:
    
    
    
    import utils
    
    
    
    [ ]:
    
    
    
    import torch
    from torch.utils.data import DataLoader
    import numpy as np
    import torchvision.transforms.v2 as transforms
    from torchvision import tv_tensors
    import matplotlib.pyplot as plt
    import matplotlib.patches as plt_patches
    from PIL import Image
    from utils import SimpleGetItem
    
    
    
    [4]:
    
    
    
    torch.multiprocessing.set_start_method('forkserver')
    

## Caching Fields with `vectorize=True`#

Typically, the `FiftyOneTorchDataset` opens up a connection to the backing database for the given samples passed and queries it for the needed samples during runtime. This is pretty slow, and we donât want this overhead in our training loop. To get around this, we can use `vectorize=True` along with a `GetItem` object that specifies which fields to cache. When `vectorize=True` is passed to `to_torch`, the `FiftyOneTorchDataset` object will preload the specified fields into memory so that we can quickly access them during training. This makes a very significant difference for the speed of sample retrieval. If you find that you are bottlenecked by the speed of your dataloader when using `FiftyOneTorchDataset`, consider using this approach. To make this easier, we provide a `SimpleGetItem` helper class in `utils.py` that wraps your function and specifies which field names to cache. This class needs to be imported from a proper Python module (not defined in the notebook) to work correctly with PyTorchâs multiprocessing DataLoader workers. Here is a tutorial on how it works.

## Load Dataset#
    
    
    [5]:
    
    
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    
    
    Dataset already downloaded
    Loading existing dataset 'quickstart'. To reload from disk, either delete the existing dataset or provide a custom `dataset_name` to use
    
    
    
    [6]:
    
    
    
    # make sure it's persistent
    print(dataset.persistent)
    
    # if it's not, set this variable to True
    if not dataset.persistent:
        dataset.persistent = True
    
    
    
    True
    
    
    
    [7]:
    
    
    
    some_interesting_view = dataset.take(100)
    

## Specifying Fields to Cache#

Here is an example of what happens when we specify field names to cache using `SimpleGetItem` and `vectorize=True`. We will use an identity `get_item` function to see what the dataset is returning for us on query.
    
    
    [8]:
    
    
    
    def get_item_identity(x):
        return x
    
    
    
    [9]:
    
    
    
    fields_of_interest = ['id', 'filepath']
    
    
    
    [10]:
    
    
    
    # Notice that as soon as we construct the dataset, our fields are serialized and put in memory
    # We wrap our function with SimpleGetItem to specify which fields to cache
    get_item_wrapper = SimpleGetItem(get_item_identity, fields_of_interest)
    torch_dataset = some_interesting_view.to_torch(get_item_wrapper, vectorize=True)
    
    
    
    [11]:
    
    
    
    # when we access the dataset, we get a dictionary with the values we wanted
    print(torch_dataset[0])
    
    
    
    {'id': '67be7706acd35912dc493b84', 'filepath': '/home/jacobs/fiftyone/quickstart/data/000591.jpg'}
    

## A New `get_item`#

Recall that in the previous example, our `get_item` function took a FiftyOne Sample as input, and returned model inputs. This will not work in this case, because as we saw, when `vectorize=True` is used with cached fields, the `FiftyOneTorchDataset` will give us a dict with keys and values corresponding to the fields we specified. Letâs rewrite our `get_item` function from the last example to account for this.
    
    
    [12]:
    
    
    
    augmentations = transforms.Compose([
        transforms.CenterCrop(512),
        transforms.ClampBoundingBoxes()
    ])
    def get_item_cached(sample_dict):
        res = {}
        image = Image.open(sample_dict['filepath'])
        og_wh = np.array([image.width, image.height])
        image = tv_tensors.Image(image)
        detections = sample_dict['ground_truth.detections.bounding_box']
        if detections is None:
            detections = []
        detections_tensor = torch.tensor(detections) if len(detections) > 0 \
            else torch.zeros((0,4))
        res['box'] = tv_tensors.BoundingBoxes(detections_tensor * torch.tensor([*og_wh, *og_wh]),
            format=tv_tensors.BoundingBoxFormat('XYWH'),
            canvas_size=image.shape[-2:]
        )
        res['label'] = sample_dict['ground_truth.detections.label']
        res['id'] = sample_dict['id']
        image, res = augmentations(image, res)
        return image, res
    
    
    
    [13]:
    
    
    
    # we have to make sure we pass all of the fields used by our get_item
    fields_of_interest = [
        'id',
        'filepath',
        'ground_truth.detections.bounding_box',
        'ground_truth.detections.label'
    ]
    # Wrap our function with SimpleGetItem to specify which fields to cache
    get_item_wrapper = SimpleGetItem(get_item_cached, fields_of_interest)
    torch_dataset = some_interesting_view.to_torch(get_item_wrapper, vectorize=True)
    

## Visualizing the result#

Same as before, we can visualize the result
    
    
    [14]:
    
    
    
    # run this a couple of times to look through samples in the dataset
    random_index = np.random.randint(0, len(torch_dataset))
    image, res = torch_dataset[random_index]
    plt.title(res['id'])
    plt.imshow(image.permute(1, 2, 0).numpy())
    axes = plt.gca()
    for b, l in zip(res['box'], res['label']):
        rect = plt_patches.Rectangle((b[0], b[1]),
                                        b[2], b[3],
                                        linewidth=1, edgecolor='r', facecolor='none')
        axes.add_patch(rect)
        axes.annotate(l, rect.get_xy())
    plt.show()
    

![../../_images/recipes_torch-dataset-examples_the_cache_field_names_argument_30_0.png](../../_images/recipes_torch-dataset-examples_the_cache_field_names_argument_30_0.png) And again, we can create dataloaders and work with the dataset during training.
    
    
    [15]:
    
    
    
    # utils.get_item_cached_quickstart is the same get_item_cached as above.
    fields_of_interest = [
        'id',
        'filepath',
        'ground_truth.detections.bounding_box',
        'ground_truth.detections.label'
    ]
    # Wrap our function with SimpleGetItem to specify which fields to cache
    get_item_wrapper = SimpleGetItem(utils.get_item_cached_quickstart, fields_of_interest)
    torch_dataset = some_interesting_view.to_torch(get_item_wrapper, vectorize=True)
    dataloader = utils.create_dataloader_simple(torch_dataset)
    
    
    
    [16]:
    
    
    
    ids_seen = utils.ids_in_dataloader(dataloader)
    
    
    
    [17]:
    
    
    
    # confirm we have seen each sample once
    from collections import Counter
    ids_with_counts = Counter(ids_seen)
    assert set(ids_with_counts.keys()) == set(some_interesting_view.values('id'))
    assert np.all(np.array(list(ids_with_counts.values())) == 1)
    
    
    
    [18]:
    
    
    
    # visualizing results, run this a couple of times to see different batches
    iterator = iter(dataloader)
    
    
    
    [19]:
    
    
    
    image, res = next(iterator)
    
    fig, axes = plt.subplots(1, len(image), figsize=(4 * len(image), 3))
    
    for i, img in enumerate(image):
        axes[i].set_title(res[i]['id'])
        axes[i].imshow(img.permute(1, 2, 0).numpy())
        for b, l in zip(res[i]['box'], res[i]['label']):
            rect = plt_patches.Rectangle((b[0], b[1]),
                                            b[2], b[3],
                                            linewidth=1, edgecolor='r', facecolor='none')
            axes[i].add_patch(rect)
            axes[i].annotate(l, rect.get_xy())
    
    plt.show()
    

![../../_images/recipes_torch-dataset-examples_the_cache_field_names_argument_36_0.png](../../_images/recipes_torch-dataset-examples_the_cache_field_names_argument_36_0.png) IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
