---
source_url: https://docs.voxel51.com/model_zoo/models/efficientdet_d4_coco_tf1.html
---

# efficientdet-d4-coco-tf1#

Legacy high-accuracy object detector ensuring backward compatibility with TensorFlow 1.

**Details**

  * Model name: `efficientdet-d4-coco-tf1`

  * Model source: [voxel51/automl](https://github.com/voxel51/automl/tree/master/efficientdet)

  * Model author: Mingxing Tan, et al.

  * Model license: Apache 2.0

  * Model size: 175.33 MB

  * Exposes embeddings? no

  * Tags: `detection, coco, tf1, efficientdet, legacy`




**Requirements**

  * CPU support

    * yes

    * Packages: `tensorflow>=1.14,<2`

  * GPU support

    * yes

    * Packages: `tensorflow-gpu>=1.14,<2`




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
    12model = foz.load_zoo_model("efficientdet-d4-coco-tf1")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
