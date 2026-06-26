---
source_url: https://docs.voxel51.com/model_zoo/models/mobilenet_v2_imagenet_tf1.html
---

# mobilenet-v2-imagenet-tf1#

Efficient mobile classifier using specialized architecture for fast image recognition on phones.

**Details**

  * Model name: `mobilenet-v2-imagenet-tf1`

  * Model source: [tensorflow/models](https://github.com/tensorflow/models/tree/archive/research/slim#pre-trained-models)

  * Model author: Mark Sandler, et al.

  * Model license: Apache 2.0

  * Model size: 13.64 MB

  * Exposes embeddings? yes

  * Tags: `classification, embeddings, logits, imagenet, tf1, mobilenet`




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
    11model = foz.load_zoo_model("mobilenet-v2-imagenet-tf1")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
