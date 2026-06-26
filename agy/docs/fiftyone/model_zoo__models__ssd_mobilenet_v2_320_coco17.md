---
source_url: https://docs.voxel51.com/model_zoo/models/ssd_mobilenet_v2_320_coco17.html
---

# ssd-mobilenet-v2-320-coco17#

Fast object finder optimized for quick GPU processing of smaller input images.

**Details**

  * Model name: `ssd-mobilenet-v2-320-coco17`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/blob/archive/research/object_detection/g3doc/tf2_detection_zoo.md)

  * Model author: Mark Sandler, et al.

  * Model license: Apache 2.0

  * Model size: 43.91 MB

  * Exposes embeddings? no

  * Tags: `detection, coco, tf2, ssd, mobilenet`




**Requirements**

  * CPU support

    * yes

    * Packages: `tensorflow>=2|tensorflow-macos`

  * GPU support

    * yes

    * Packages: `tensorflow-gpu>=2|tensorflow>=2|tensorflow-macos`




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
    12model = foz.load_zoo_model("ssd-mobilenet-v2-320-coco17")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
