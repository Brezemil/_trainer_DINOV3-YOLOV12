---
source_url: https://docs.voxel51.com/model_zoo/models/segment_anything_vitl_torch.html
---

# segment-anything-vitl-torch#

Large segmentation model producing finer object outlines for professional editing and labeling workflows.

**Details**

  * Model name: `segment-anything-vitl-torch`

  * Model source: <https://segment-anything.com>

  * Model author: Alexander Kirillov, et al.

  * Model license: Apache 2.0

  * Model size: 1.16 GB

  * Exposes embeddings? no

  * Tags: `segment-anything, sa-1b, torch, zero-shot, transformer, official`




**Requirements**

  * Packages: `torch, torchvision, segment-anything`

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
    12model = foz.load_zoo_model("segment-anything-vitl-torch")
    13
    14# Segment inside boxes
    15dataset.apply_model(
    16    model,
    17    label_field="segmentations",
    18    prompt_field="ground_truth",  # can contain Detections or Keypoints
    19)
    20
    21# Full automatic segmentations
    22dataset.apply_model(model, label_field="auto")
    23
    24session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
