---
source_url: https://docs.voxel51.com/model_zoo/models/inception_resnet_v2_imagenet_tf1.html
---

# inception-resnet-v2-imagenet-tf1#

High-accuracy image classifier with advanced architecture for precise categorization and feature extraction.

**Details**

  * Model name: `inception-resnet-v2-imagenet-tf1`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/tree/archive/research/slim#pre-trained-models)

  * Model author: Christian Szegedy, et al.

  * Model license: Apache 2.0

  * Model size: 213.81 MB

  * Exposes embeddings? yes

  * Tags: `classification, embeddings, logits, imagenet, tf1, inception, resnet`




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
     5    "imagenet-sample",
     6    dataset_name=fo.get_default_dataset_name(),
     7    max_samples=50,
     8    shuffle=True,
     9)
    10
    11model = foz.load_zoo_model("inception-resnet-v2-imagenet-tf1")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
