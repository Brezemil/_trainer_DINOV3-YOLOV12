---
source_url: https://docs.voxel51.com/model_zoo/models/pose_estimation_transformer_torch.html
---

# pose-estimation-transformer-torch#

Vision Transformer for pose estimation with 90M parameters removing complex decoder components..

**Details**

  * Model name: `pose-estimation-transformer-torch`

  * Model source: [ViTAE-Transformer/ViTPose](https://github.com/ViTAE-Transformer/ViTPose)

  * Model license: Apache 2.0

  * Exposes embeddings? no

  * Tags: `keypoints, coco, torch, transformers, pose-estimation`




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
    12model = foz.load_zoo_model("pose-estimation-transformer-torch")
    13
    14dataset.apply_model(model, prompt_field="ground_truth", label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
