---
source_url: https://docs.voxel51.com/model_zoo/models/deeplabv3_cityscapes_tf.html
---

# deeplabv3-cityscapes-tf#

Creates detailed pixel-by-pixel labels for urban scenes, helping autonomous vehicles understand their surroundings.

**Details**

  * Model name: `deeplabv3-cityscapes-tf`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/model_zoo.md)

  * Model author: Liang-Chieh Chen, et al.

  * Model license: Apache 2.0

  * Model size: 158.04 MB

  * Exposes embeddings? no

  * Tags: `segmentation, cityscapes, tf, deeplabv3, legacy`




**Requirements**

  * CPU support

    * yes

    * Packages: `tensorflow|tensorflow-macos`

  * GPU support

    * yes

    * Packages: `tensorflow-gpu|tensorflow>=2|tensorflow-macos`




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
    12model = foz.load_zoo_model("deeplabv3-cityscapes-tf")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
