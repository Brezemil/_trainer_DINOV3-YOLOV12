---
source_url: https://docs.voxel51.com/model_zoo/models/yolov8s_oiv7_torch.html
---

# yolov8s-oiv7-torch#

Compact detector recognizing diverse object types across many different image categories.

**Details**

  * Model name: `yolov8s-oiv7-torch`

  * Model source: <https://docs.ultralytics.com/datasets/detect/open-images-v7>

  * Model author: Glenn Jocher, et al.

  * Model license: AGPL-3.0

  * Model size: 21.92 MB

  * Exposes embeddings? no

  * Tags: `detection, oiv7, torch, yolo, official`




**Requirements**

  * Packages: `torch>=1.7.0, torchvision>=0.8.1, ultralytics`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset(
     5    "coco-2017",
     6    split="validation",
     7    dataset_name=fo.get_default_dataset_name(),
     8    max_samples=50,
     9    shuffle=True,
    10)
    11
    12model = foz.load_zoo_model("yolov8s-oiv7-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
