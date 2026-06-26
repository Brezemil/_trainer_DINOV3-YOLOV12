---
source_url: https://docs.voxel51.com/model_zoo/models/segment_anything_2_1_hiera_small_image_torch.html
---

# segment-anything-2.1-hiera-small-image-torch#

Balanced updated segmenter combining speed and accuracy for edge device image processing.

**Details**

  * Model name: `segment-anything-2.1-hiera-small-image-torch`

  * Model source: <https://ai.meta.com/sam2/>

  * Model author: Nikhila Ravi, et al.

  * Model license: Apache 2.0, BSD 3-Clause

  * Model size: 175.87 MB

  * Exposes embeddings? no

  * Tags: `segment-anything, torch, zero-shot, transformer, official`




**Requirements**

  * Packages: `torch, torchvision, sam2`

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
    12model = foz.load_zoo_model("segment-anything-2.1-hiera-small-image-torch")
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
