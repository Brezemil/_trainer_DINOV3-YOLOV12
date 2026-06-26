---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/quickstart_3d.html
---

# Quickstart 3D#

A small 3D dataset with meshes, point clouds, and oriented bounding boxes.

The dataset consists of 200 3D mesh samples from the test split of the [ModelNet40](https://modelnet.cs.princeton.edu) dataset, with point clouds generated using a Poisson disk sampling method, and oriented bounding boxes generated based on the convex hull.

Objects have been rescaled and recentered from the original dataset.

**Details**

  * Dataset name: `quickstart-3d`

  * Dataset size: 215.7 MB

  * Dataset license: <https://modelnet.cs.princeton.edu>

  * Tags: `3d, point-cloud, mesh, quickstart`

  * Supported splits: `N/A`

  * ZooDataset class: [`Quickstart3DDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.Quickstart3DDataset "fiftyone.zoo.datasets.base.Quickstart3DDataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("quickstart-3d")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load quickstart-3d
    
    fiftyone app launch quickstart-3d
    

![quickstart-3d](../../_images/quickstart-3d.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
