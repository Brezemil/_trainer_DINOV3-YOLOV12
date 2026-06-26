---
source_url: https://docs.voxel51.com/recipes/torch-dataset-examples/simple_training_example.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/recipes/torch-dataset-examples/simple_training_example.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/recipes/torch-dataset-examples/simple_training_example.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/recipes/torch-dataset-examples/simple_training_example.ipynb)

# How to Train a Model on MNIST with FiftyOne and Torch#

This recipe demonstrates how to train a PyTorch model on the **MNIST** dataset using `FiftyOneTorchDataset`. This is useful when you want to build and evaluate models in Torch while managing your data pipeline directly from FiftyOne. Specifically, it covers:

  * Loading the MNIST dataset from the [Dataset Zoo](https://voxel51.com/docs/fiftyone/user_guide/dataset_zoo/index.html)
  * Creating train/validation/test splits with FiftyOneâs tagging and random splitting utilities
  * Building a subset of the dataset for faster experimentation
  * Running a simple training loop via an external script (`mnist_training.py`)
  * Saving model weights for later evaluation or reuse



## Setup#

If you havenât already, install FiftyOne:
    
    
    [ ]:
    
    
    
    !pip install fiftyone
    

In this tutorial, weâll use [PyTorch](https://pytorch.org/) for working with tensors and inspecting sample data. To follow along, youâll need to install `torch` and `torchvision`, if necessary:
    
    
    [ ]:
    
    
    
    !pip install torch torchvision
    

## Import Libraries#
    
    
    [1]:
    
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.random as four
    
    
    
    [2]:
    
    
    
    import torch
    from torch.utils.data import DataLoader
    import numpy as np
    import torchvision.transforms.v2 as transforms
    from torchvision import tv_tensors
    import matplotlib.pyplot as plt
    import matplotlib.patches as plt_patches
    from PIL import Image
    import urllib.request
    

To run this recipe, youâll need the mnist_training.py script, which contains a simple PyTorch training loop. The following cell will automatically download the file into your working directory so it can be imported directly.
    
    
    [ ]:
    
    
    
    url = "https://cdn.voxel51.com/tutorials_torch_dataset_examples/notebook_simple_training_example/mnist_training.py"
    urllib.request.urlretrieve(url, "mnist_training.py")
    
    
    
    [ ]:
    
    
    
    url = "https://cdn.voxel51.com/tutorials_torch_dataset_examples/notebook_the_cache_field_names_argument/utils.py"
    urllib.request.urlretrieve(url, "utils.py")
    
    
    
    [3]:
    
    
    
    import mnist_training
    
    
    
    [4]:
    
    
    
    torch.multiprocessing.set_start_method('forkserver')
    torch.multiprocessing.set_forkserver_preload(['torch', 'fiftyone'])
    

## Basic Training Example on MNIST#

Now we will look at an actual training script with `FiftyOneTorchDataset`
    
    
    [5]:
    
    
    
    mnist = foz.load_zoo_dataset("mnist")
    mnist.persistent = True
    
    
    
    Split 'train' already downloaded
    Split 'test' already downloaded
    Loading existing dataset 'mnist'. To reload from disk, either delete the existing dataset or provide a custom `dataset_name` to use
    
    
    
    [6]:
    
    
    
    fo.launch_app(mnist, auto=False)
    
    
    
    Session launched. Run `session.show()` to open the App in a cell output.
    
    
    
    [6]:
    
    
    
    Dataset:          mnist
    Media type:       image
    Num samples:      70000
    Selected samples: 0
    Selected labels:  0
    Session URL:      http://localhost:5151/
    

Now letâs say that for our training, we want to define some random subset of our trainset to be a validation set. We can easily do this with FiftyOne.
    
    
    [7]:
    
    
    
    # remove existing 'train' or 'validation' tags if they exist
    mnist.untag_samples(['train', 'validation'])
    
    # create a random split, just on the samples not tagged 'test'
    not_test = mnist.match_tags('test', bool=False)
    four.random_split(not_test, {'train' : 0.9, 'validation' : 0.1})
    print(mnist.count_sample_tags())
    
    
    
    {'train': 54000, 'validation': 6000, 'test': 10000}
    
    
    
    [8]:
    
    
    
    # subset if we want it
    samples = []
    samples += mnist.match_tags('train').take(1000).values('id')
    for tag in ['test', 'validation']:
        samples += mnist.match_tags(tag).values('id')
    
    subset = mnist.select(samples)
    
    
    
    [ ]:
    
    
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    path_to_save_weights = '/path/to/save/weights'
    mnist_training.main(subset, 10, 10, device, path_to_save_weights)
    
    
    
    Average Train Loss =   3.999074: 100%|ââââââââââ| 63/63 [00:01<00:00, 58.45it/s]
    Average Validation Loss =   2.811698: 100%|ââââââââââ| 375/375 [00:02<00:00, 149.01it/s]
    
    
    
    New best lost achieved : 2.801392190893491. Saving model...
    
    
    
    Average Train Loss =   1.072026: 100%|ââââââââââ| 63/63 [00:00<00:00, 119.78it/s]
    Average Validation Loss =   0.396746: 100%|ââââââââââ| 375/375 [00:01<00:00, 215.10it/s]
    
    
    
    New best lost achieved : 0.39641891201337176. Saving model...
    
    
    
    Average Train Loss =   0.148484: 100%|ââââââââââ| 63/63 [00:00<00:00, 120.53it/s]
    Average Validation Loss =   0.319500: 100%|ââââââââââ| 375/375 [00:01<00:00, 211.25it/s]
    
    
    
    New best lost achieved : 0.3149221637323499. Saving model...
    
    
    
    Average Train Loss =   0.627752: 100%|ââââââââââ| 63/63 [00:00<00:00, 97.89it/s]
    Average Validation Loss =   0.304854: 100%|ââââââââââ| 375/375 [00:01<00:00, 207.17it/s]
    
    
    
    New best lost achieved : 0.2977131818582614. Saving model...
    
    
    
    Average Train Loss =   0.204026: 100%|ââââââââââ| 63/63 [00:00<00:00, 119.48it/s]
    Average Validation Loss =   0.210062: 100%|ââââââââââ| 375/375 [00:01<00:00, 214.69it/s]
    
    
    
    New best lost achieved : 0.2064167803612848. Saving model...
    
    
    
    Average Train Loss =   0.070824: 100%|ââââââââââ| 63/63 [00:00<00:00, 106.55it/s]
    Average Validation Loss =   1.467735: 100%|ââââââââââ| 375/375 [00:02<00:00, 173.34it/s]
    Average Train Loss =   0.509837: 100%|ââââââââââ| 63/63 [00:00<00:00, 112.51it/s]
    Average Validation Loss =   0.387830: 100%|ââââââââââ| 375/375 [00:02<00:00, 163.92it/s]
    Average Train Loss =   0.236021: 100%|ââââââââââ| 63/63 [00:00<00:00, 116.83it/s]
    Average Validation Loss =   0.287110: 100%|ââââââââââ| 375/375 [00:01<00:00, 211.45it/s]
    Average Train Loss =   0.047093: 100%|ââââââââââ| 63/63 [00:00<00:00, 99.11it/s]
    Average Validation Loss =   0.156705: 100%|ââââââââââ| 375/375 [00:01<00:00, 213.70it/s]
    
    
    
    New best lost achieved : 0.14917240004179377. Saving model...
    
    
    
    Average Train Loss =   0.009842: 100%|ââââââââââ| 63/63 [00:00<00:00, 97.05it/s]
    Average Validation Loss =   0.138089: 100%|ââââââââââ| 375/375 [00:01<00:00, 211.95it/s]
    
    
    
    New best lost achieved : 0.13520573990046977. Saving model...
    
    
    
    Average Validation Loss =   0.113355: 100%|ââââââââââ| 625/625 [00:10<00:00, 61.62it/s]
    
    
    
    Final Test Results:
    Loss = 0.11413920720983296
                  precision    recall  f1-score   support
    
        0 - zero       0.98      0.97      0.98       980
         1 - one       0.98      0.99      0.99      1135
         2 - two       0.96      0.97      0.96      1032
       3 - three       0.95      0.97      0.96      1010
        4 - four       0.96      0.97      0.96       982
        5 - five       0.95      0.96      0.95       892
         6 - six       0.96      0.97      0.96       958
       7 - seven       0.97      0.93      0.95      1028
       8 - eight       0.98      0.94      0.96       974
        9 - nine       0.95      0.96      0.96      1009
    
        accuracy                           0.96     10000
       macro avg       0.96      0.96      0.96     10000
    weighted avg       0.96      0.96      0.96     10000
    
    

This recipe showed how to train a PyTorch model on MNIST using `FiftyOneTorchDataset`, with dataset splits, subsets, and a simple training loop. IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
