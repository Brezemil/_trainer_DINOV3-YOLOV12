---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/imagenet_2012.html
---

# ImageNet 2012#

The ImageNet 2012 dataset.

ImageNet, as known as ILSVRC 2012, is an image dataset organized according to the WordNet hierarchy. Each meaningful concept in WordNet, possibly described by multiple words or word phrases, is called a âsynonym setâ or âsynsetâ. There are more than 100,000 synsets in WordNet, majority of them are nouns (80,000+). ImageNet provides on average 1,000 images to illustrate each synset. Images of each concept are quality-controlled and human-annotated. In its completion, we hope ImageNet will offer tens of millions of cleanly sorted images for most of the concepts in the WordNet hierarchy.

Note that labels were never publicly released for the test set, so only the training and validation sets are provided.

Note

In order to load the ImageNet dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        ILSVRC2012_devkit_t12.tar.gz    # both splits
        ILSVRC2012_img_train.tar        # train split
        ILSVRC2012_img_val.tar          # validation split
    

You can register at <http://www.image-net.org/download-images> in order to get links to download the data.

**Details**

  * Dataset name: `imagenet-2012`

  * Dataset source: <http://image-net.org>

  * Dataset license: <https://image-net.org/download>

  * Dataset size: 144.02 GB

  * Tags: `image, classification, manual`

  * Supported splits: `train, validation`

  * ZooDataset classes:

    * [`ImageNet2012Dataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.ImageNet2012Dataset "fiftyone.zoo.datasets.tf.ImageNet2012Dataset") (TF backend)

    * [`ImageNet2012Dataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.ImageNet2012Dataset "fiftyone.zoo.datasets.torch.ImageNet2012Dataset") (Torch backend)




Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4# The path to the source files that you manually downloaded
     5source_dir = "/path/to/dir-with-imagenet-files"
     6
     7dataset = foz.load_zoo_dataset(
     8    "imagenet-2012",
     9    split="validation",
    10    source_dir=source_dir,
    11)
    12
    13session = fo.launch_app(dataset)
    
    
    
    # The path to the source files that you manually downloaded
    SOURCE_DIR="/path/to/dir-with-imagenet-files"
    
    fiftyone zoo datasets load imagenet-2012 --split validation \
        --kwargs "source_dir=${SOURCE_DIR}"
    
    fiftyone app launch imagenet-2012-validation
    

![imagenet-2012-validation](../../_images/imagenet-2012-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
