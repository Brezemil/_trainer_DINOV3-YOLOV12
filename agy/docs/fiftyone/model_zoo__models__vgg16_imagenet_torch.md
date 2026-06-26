---
source_url: https://docs.voxel51.com/model_zoo/models/vgg16_imagenet_torch.html
---

# vgg16-imagenet-torch#

PyTorch version of the popular classifier ready for modern deep learning workflows.

**Details**

  * Model name: `vgg16-imagenet-torch`

  * Model source: <https://pytorch.org/vision/main/models.html>

  * Model author: Karen Simonyan, et al.

  * Model license: BSD 3-Clause

  * Model size: 527.80 MB

  * Exposes embeddings? yes

  * Tags: `classification, embeddings, logits, imagenet, torch, vgg, official`




**Requirements**

  * Packages: `torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




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
    11model = foz.load_zoo_model("vgg16-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
