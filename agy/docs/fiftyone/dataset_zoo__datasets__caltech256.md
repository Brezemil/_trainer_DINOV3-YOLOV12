---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/caltech256.html
---

# Caltech-256#

The Caltech-256 dataset of images.

The dataset consists of pictures of objects belonging to 256 classes, plus one background clutter class (`clutter`). Each image is labelled with a single object.

Each class contains between 80 and 827 images, totalling 30,607 images. Images are of variable sizes, with typical edge lengths of 80-800 pixels.

**Details**

  * Dataset name: `caltech256`

  * Dataset source: <https://data.caltech.edu/records/nyy15-4j048>

  * Dataset license: CC-BY-4.0

  * Dataset size: 1.16 GB

  * Tags: `image, classification`

  * Supported splits: `N/A`

  * ZooDataset class: [`Caltech256Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.Caltech256Dataset "fiftyone.zoo.datasets.base.Caltech256Dataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("caltech256")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load caltech256
    
    fiftyone app launch caltech256
    

![caltech256](../../_images/caltech256.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
