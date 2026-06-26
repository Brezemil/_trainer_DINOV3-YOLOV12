---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/quickstart_groups.html
---

# Quickstart Groups#

A small dataset with grouped image and point cloud data.

The dataset consists of 200 scenes from the train split of the KITTI dataset, each containing left camera, right camera, point cloud, and 2D/3D object annotation data.

**Details**

  * Dataset name: `quickstart-groups`

  * Dataset size: 516.3 MB

  * Dataset license: CC-BY-NC-SA-3.0

  * Tags: `image, point-cloud, quickstart`

  * Supported splits: `N/A`

  * ZooDataset class: [`QuickstartGroupsDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.QuickstartGroupsDataset "fiftyone.zoo.datasets.base.QuickstartGroupsDataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("quickstart-groups")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load quickstart-groups
    
    fiftyone app launch quickstart-groups
    

![quickstart-groups](../../_images/quickstart-groups.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
