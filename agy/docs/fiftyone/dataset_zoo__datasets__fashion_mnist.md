---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/fashion_mnist.html
---

# Fashion MNIST#

The Fashion-MNIST database of Zalandoâs fashion article images.

The dataset consists of 70,000 28 x 28 grayscale images in 10 classes. There are 60,000 training images and 10,000 test images.

**Details**

  * Dataset name: `fashion-mnist`

  * Dataset source: [zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)

  * Dataset license: MIT

  * Dataset size: 36.42 MB

  * Tags: `image, classification`

  * Supported splits: `train, test`

  * ZooDataset classes:

    * [`FashionMNISTDataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.FashionMNISTDataset "fiftyone.zoo.datasets.tf.FashionMNISTDataset") (TF backend)

    * [`FashionMNISTDataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.FashionMNISTDataset "fiftyone.zoo.datasets.torch.FashionMNISTDataset") (Torch backend)




Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("fashion-mnist", split="test")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load fashion-mnist --split test
    
    fiftyone app launch fashion-mnist-test
    

![fashion-mnist-test](../../_images/fashion-mnist-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
