---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/voc_2007.html
---

# VOC-2007#

The dataset for the PASCAL Visual Object Classes Challenge 2007 (VOC2007) for the detection competition.

A total of 9,963 images are included in this dataset, where each image contains a set of objects, out of 20 different classes, making a total of 24,640 annotated objects.

Note that, as per the official dataset, the test set of VOC2007 does not contain annotations.

**Details**

  * Dataset name: `voc-2007`

  * Dataset source: <http://host.robots.ox.ac.uk/pascal/VOC/voc2007>

  * Dataset size: 868.85 MB

  * Tags: `image, detection`

  * Supported splits: `train, validation, test`

  * ZooDataset classes:

    * [`VOC2007Dataset`](api__fiftyone.zoo.datasets.tf.md#fiftyone.zoo.datasets.tf.VOC2007Dataset "fiftyone.zoo.datasets.tf.VOC2007Dataset") (TF backend)

    * [`VOC2007Dataset`](api__fiftyone.zoo.datasets.torch.md#fiftyone.zoo.datasets.torch.VOC2007Dataset "fiftyone.zoo.datasets.torch.VOC2007Dataset") (Torch backend)




Note

The `test` split is only available via the [TensorFlow backend](dataset_zoo__api.md#dataset-zoo-ml-backend).

Note

You must have the [Torch or TensorFlow backend(s)](dataset_zoo__api.md#dataset-zoo-ml-backend) installed to load this dataset.

**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("voc-2007", split="validation")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load voc-2007 --split validation
    
    fiftyone app launch voc-2007-validation
    

![voc-2007-validation](../../_images/voc-2007-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
