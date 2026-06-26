---
source_url: https://docs.voxel51.com/model_zoo/models/yoloev8m_seg_torch.html
---

# yoloev8m-seg-torch#

Model creating masks for any object type you name in text.

**Details**

  * Model name: `yoloev8m-seg-torch`

  * Model source: <https://docs.ultralytics.com/models/yoloe>

  * Model author: Glenn Jocher, et al.

  * Model license: AGPL-3.0

  * Model size: 62.75 MB

  * Exposes embeddings? no

  * Tags: `instances, torch, yolo, zero-shot, official`




**Requirements**

  * Packages: `torch>=1.7.0, torchvision>=0.8.1, ultralytics>=8.3.99`

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
    12model = foz.load_zoo_model("yoloev8m-seg-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    17
    18#
    19# Make zero-shot predictions with custom classes
    20#
    21
    22model = foz.load_zoo_model(
    23    "yoloev8m-seg-torch",
    24    classes=["person", "dog", "cat", "bird", "car", "tree", "chair"],
    25)
    26
    27dataset.apply_model(model, label_field="predictions")
    28session.refresh()
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
