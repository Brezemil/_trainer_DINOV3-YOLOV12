---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/caltech101.html
---

# Caltech-101#

The Caltech-101 dataset of images.

The dataset consists of pictures of objects belonging to 101 classes, plus one background clutter class (`BACKGROUND_Google`). Each image is labelled with a single object.

Each class contains roughly 40 to 800 images, totalling around 9,000 images. Images are of variable sizes, with typical edge lengths of 200-300 pixels. This version contains image-level labels only.

**Details**

  * Dataset name: `caltech101`

  * Dataset source: <https://data.caltech.edu/records/mzrjq-6wc02>

  * Dataset license: CC-BY-4.0

  * Dataset size: 138.60 MB

  * Tags: `image, classification`

  * Supported splits: `N/A`

  * ZooDataset class: [`Caltech101Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.Caltech101Dataset "fiftyone.zoo.datasets.base.Caltech101Dataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("caltech101")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load caltech101
    
    fiftyone app launch caltech101
    

![caltech101](../../_images/caltech101.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
