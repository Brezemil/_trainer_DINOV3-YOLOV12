---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/cityscapes.html
---

# Cityscapes#

Cityscapes is a large-scale dataset that contains a diverse set of stereo video sequences recorded in street scenes from 50 different cities, with high quality pixel-level annotations of 5,000 frames in addition to a larger set of 20,000 weakly annotated frames.

The dataset is intended for:

  * Assessing the performance of vision algorithms for major tasks of semantic urban scene understanding: pixel-level, instance-level, and panoptic semantic labeling

  * Supporting research that aims to exploit large volumes of (weakly) annotated data, e.g. for training deep neural networks




Note

In order to load the Cityscapes dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        leftImg8bit_trainvaltest.zip
        gtFine_trainvaltest.zip             # optional
        gtCoarse.zip                        # optional
        gtBbox_cityPersons_trainval.zip     # optional
    

You can register at <https://www.cityscapes-dataset.com/register> in order to get links to download the data.

**Details**

  * Dataset name: `cityscapes`

  * Dataset source: <https://www.cityscapes-dataset.com>

  * Dataset license: <https://www.cityscapes-dataset.com/license>

  * Dataset size: 11.80 GB

  * Tags: `image, multilabel, automotive, manual`

  * Supported splits: `train, validation, test`

  * ZooDataset class: [`CityscapesDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.CityscapesDataset "fiftyone.zoo.datasets.base.CityscapesDataset")




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4# The path to the source files that you manually downloaded
     5source_dir = "/path/to/dir-with-cityscapes-files"
     6
     7dataset = foz.load_zoo_dataset(
     8    "cityscapes",
     9    split="validation",
    10    source_dir=source_dir,
    11)
    12
    13session = fo.launch_app(dataset)
    
    
    
    # The path to the source files that you manually downloaded
    SOURCE_DIR="/path/to/dir-with-cityscapes-files"
    
    fiftyone zoo datasets load cityscapes --split validation \
        --kwargs "source_dir=${SOURCE_DIR}"
    
    fiftyone app launch cityscapes-validation
    

![cityscapes-validation](../../_images/cityscapes-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
