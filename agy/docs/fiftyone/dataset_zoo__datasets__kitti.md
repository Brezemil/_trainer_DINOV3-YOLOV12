---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/kitti.html
---

# KITTI#

KITTI contains a suite of vision tasks built using an autonomous driving platform.

This dataset contains the left camera images and the associated 2D object detections.

The training split contains 7,481 annotated images, and the test split contains 7,518 unlabeled images.

A full description of the annotations can be found in the README of the object development kit on the KITTI homepage.

**Details**

  * Dataset name: `kitti`

  * Dataset source: <http://www.cvlibs.net/datasets/kitti>

  * Dataset license: CC-BY-NC-SA-3.0

  * Dataset size: 12.57 GB

  * Tags: `image, detection`

  * Supported splits: `train, test`

  * ZooDataset class: [`KITTIDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.KITTIDataset "fiftyone.zoo.datasets.base.KITTIDataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("kitti", split="train")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load kitti --split train
    
    fiftyone app launch kitti-train
    

![kitti-train](../../_images/kitti-train.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
