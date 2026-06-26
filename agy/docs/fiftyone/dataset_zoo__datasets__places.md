---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/places.html
---

# Places#

Places is a scene recognition dataset of 10 million images comprising ~400 unique scene categories.

The images are labeled with scene semantic categories, comprising a large and diverse list of the types of environments encountered in the world.

**Details**

  * Dataset name: `places`

  * Dataset source: <http://places2.csail.mit.edu/download-private.html>

  * Dataset size: 29 GB

  * Tags: `image, classification`

  * Supported splits: `train, validation, test`

  * ZooDataset classes: [`PlacesDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.PlacesDataset "fiftyone.zoo.datasets.base.PlacesDataset")




**Full split stats**

  * Train split: 1,803,460 images, with between 3,068 and 5,000 per category

  * Test split: 328,500 images, with 900 images per category

  * Validation split: 36,500 images, with 100 images per category




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("places", split="validation")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load places --split validation
    
    fiftyone app launch places-validation
    

![places-validation](../../_images/places-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
