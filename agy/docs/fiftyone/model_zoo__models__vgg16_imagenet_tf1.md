---
source_url: https://docs.voxel51.com/model_zoo/models/vgg16_imagenet_tf1.html
---

# vgg16-imagenet-tf1#

TensorFlow version of the classic image classifier supporting legacy production systems.

**Details**

  * Model name: `vgg16-imagenet-tf1`

  * Model source: <https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md>

  * Model author: Karen Simonyan, et al.

  * Model license: CC-BY-4.0

  * Model size: 527.80 MB

  * Exposes embeddings? yes

  * Tags: `classification, embeddings, logits, imagenet, tf1, vgg, legacy`




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
    11model = foz.load_zoo_model("vgg16-imagenet-tf1")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
