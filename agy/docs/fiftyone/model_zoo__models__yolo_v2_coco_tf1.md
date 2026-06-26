---
source_url: https://docs.voxel51.com/model_zoo/models/yolo_v2_coco_tf1.html
---

# yolo-v2-coco-tf1#

Classic real-time detector finding eighty object types quickly for video analysis applications.

**Details**

  * Model name: `yolo-v2-coco-tf1`

  * Model source: [thtrieu/darkflow](https://github.com/thtrieu/darkflow)

  * Model author: Joseph Redmon, et al.

  * Model license: GPL-3.0

  * Model size: 194.49 MB

  * Exposes embeddings? no

  * Tags: `detection, coco, tf1, yolo, legacy`




**Requirements**

  * CPU support

    * yes

    * Packages: `tensorflow<2`

  * GPU support

    * yes

    * Packages: `tensorflow-gpu<2`




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
    12model = foz.load_zoo_model("yolo-v2-coco-tf1")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
