---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/voc_2012.html
---

# VOC-2012#

The dataset for the PASCAL Visual Object Classes Challenge 2012 (VOC2012) for the detection competition.

A total of 11540 images are included in this dataset, where each image contains a set of objects, out of 20 different classes, making a total of 27450 annotated objects.

Note that, as per the official dataset, the test set of VOC2012 does not contain annotations.

**Details**

  * Dataset name: `voc-2012`

  * Dataset source: <http://host.robots.ox.ac.uk/pascal/VOC/voc2012>

  * Dataset size: 3.59 GB

  * Tags: `image, detection`

  * Supported splits: `train, validation, test`

  * ZooDataset classes:

    * [`VOC2012Dataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.VOC2012Dataset "fiftyone.zoo.datasets.tf.VOC2012Dataset") (TF backend)

    * [`VOC2012Dataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.VOC2012Dataset "fiftyone.zoo.datasets.torch.VOC2012Dataset") (Torch backend)




Note

The `test` split is only available via the [TensorFlow backend](dataset_zoo__api.md#dataset-zoo-ml-backend).

Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("voc-2012", split="validation")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load voc-2012 --split validation
    
    fiftyone app launch voc-2012-validation
    

![voc-2012-validation](../../_images/voc-2012-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
