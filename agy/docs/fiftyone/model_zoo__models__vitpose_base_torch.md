---
source_url: https://docs.voxel51.com/model_zoo/models/vitpose_base_torch.html
---

# vitpose-base-torch#

Vision Transformer for pose estimation with 90M parameters using standard ViT backbone. Detects 17 human keypoints through heatmap regression achieving 75.8 AP on COCO. Processes 256x192 images with hierarchical features for accurate joint localization..

**Details**

  * Model name: `vitpose-base-torch`

  * Model source: [ViTAE-Transformer/ViTPose](https://github.com/ViTAE-Transformer/ViTPose)

  * Model author: Yufei Xu, et al.

  * Model license: Apache 2.0

  * Model size: 343.33 MB

  * Exposes embeddings? no

  * Tags: `keypoints, coco, torch, transformers, pose-estimation, official`




**Requirements**

  * Packages: `torch, torchvision, transformers`

  * CPU support

    * yes

  * GPU support

    * yes




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
    12model = foz.load_zoo_model("vitpose-base-torch")
    13
    14dataset.apply_model(model, prompt_field="ground_truth", label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
