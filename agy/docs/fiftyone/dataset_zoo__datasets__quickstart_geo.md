---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/quickstart_geo.html
---

# Quickstart Geo#

A small dataset with geolocation data.

The dataset consists of 500 images from the validation split of the BDD100K dataset in the New York City area with object detections and GPS timestamps.

**Details**

  * Dataset name: `quickstart-geo`

  * Dataset size: 33.50 MB

  * Tags: `image, location, quickstart`

  * Supported splits: `N/A`

  * ZooDataset class: [`QuickstartGeoDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.QuickstartGeoDataset "fiftyone.zoo.datasets.base.QuickstartGeoDataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("quickstart-geo")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load quickstart-geo
    
    fiftyone app launch quickstart-geo
    

![quickstart-geo](../../_images/quickstart-geo.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
