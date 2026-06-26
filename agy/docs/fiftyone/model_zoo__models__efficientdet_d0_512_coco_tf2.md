---
source_url: https://docs.voxel51.com/model_zoo/models/efficientdet_d0_512_coco_tf2.html
---

# efficientdet-d0-512-coco-tf2#

Tiny object detector optimized for phones and embedded systems working with smaller images.

**Details**

  * Model name: `efficientdet-d0-512-coco-tf2`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/blob/archive/research/object_detection/g3doc/tf2_detection_zoo.md)

  * Model author: Mingxing Tan, et al.

  * Model license: Apache 2.0

  * Model size: 29.31 MB

  * Exposes embeddings? no

  * Tags: `detection, coco, tf2, efficientdet`




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
    12model = foz.load_zoo_model("efficientdet-d0-512-coco-tf2")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
