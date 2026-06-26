---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/cifar100.html
---

# CIFAR-100#

The CIFAR-100 dataset of images.

The dataset consists of 60,000 32 x 32 color images in 100 classes, with 600 images per class. There are 50,000 training images and 10,000 test images.

**Details**

  * Dataset name: `cifar100`

  * Dataset source: <https://www.cs.toronto.edu/~kriz/cifar.html>

  * Dataset size: 132.03 MB

  * Tags: `image, classification`

  * Supported splits: `train, test`

  * ZooDataset classes:

    * [`CIFAR100Dataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.CIFAR100Dataset "fiftyone.zoo.datasets.tf.CIFAR100Dataset") (TF backend)

    * [`CIFAR100Dataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.CIFAR100Dataset "fiftyone.zoo.datasets.torch.CIFAR100Dataset") (Torch backend)




Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("cifar100", split="test")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load cifar100 --split test
    
    fiftyone app launch cifar100-test
    

![cifar100-test](../../_images/cifar100-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
