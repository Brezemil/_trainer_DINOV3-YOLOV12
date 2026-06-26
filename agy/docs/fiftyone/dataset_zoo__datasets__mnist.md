---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/mnist.html
---

# MNIST#

The MNIST database of handwritten digits.

The dataset consists of 70,000 28 x 28 grayscale images in 10 classes. There are 60,000 training images and 10,000 test images.

**Details**

  * Dataset name: `mnist`

  * Dataset source: <http://yann.lecun.com/exdb/mnist>

  * Dataset license: CC-BY-SA-3.0

  * Dataset size: 21.00 MB

  * Tags: `image, classification`

  * Supported splits: `train, test`

  * ZooDataset classes:

    * [`MNISTDataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.MNISTDataset "fiftyone.zoo.datasets.tf.MNISTDataset") (TF backend)

    * [`MNISTDataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.MNISTDataset "fiftyone.zoo.datasets.torch.MNISTDataset") (Torch backend)




Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("mnist", split="test")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load mnist --split test
    
    fiftyone app launch mnist-test
    

![mnist-test](../../_images/mnist-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
