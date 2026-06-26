---
source_url: https://docs.voxel51.com/model_zoo/models/faster_rcnn_resnet101_lowproposals_coco_tf.html
---

# faster-rcnn-resnet101-lowproposals-coco-tf#

Accelerated deep detector that processes fewer regions for faster results with minimal accuracy loss.

**Details**

  * Model name: `faster-rcnn-resnet101-lowproposals-coco-tf`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/blob/archive/research/object_detection/g3doc/tf1_detection_zoo.md)

  * Model author: Shaoqing Ren, et al.

  * Model license: Apache 2.0

  * Model size: 186.41 MB

  * Exposes embeddings? no

  * Tags: `detection, coco, tf, faster-rcnn, resnet, legacy`




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
    12model = foz.load_zoo_model("faster-rcnn-resnet101-lowproposals-coco-tf")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
