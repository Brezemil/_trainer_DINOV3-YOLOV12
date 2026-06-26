---
source_url: https://docs.voxel51.com/model_zoo/models/med_sam_2_video_torch.html
---

# med-sam-2-video-torch#

Medical segmentation tool that outlines organs and structures in medical videos and 3D scans.

**Details**

  * Model name: `med-sam-2-video-torch`

  * Model source: [MedicineToken/Medical-SAM2](https://github.com/MedicineToken/Medical-SAM2)

  * Model author: Jiayuan Zhu, et al.

  * Model license: Apache 2.0

  * Model size: 74.46 MB

  * Exposes embeddings? no

  * Tags: `segment-anything, torch, zero-shot, video, med-SAM, transformer, official`




**Requirements**

  * Packages: `torch, torchvision, sam2`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4from fiftyone.utils.huggingface import load_from_hub
     5
     6dataset = load_from_hub("Voxel51/BTCV-CT-as-video-MedSAM2-dataset")[:2]
     7
     8# Retaining detections from a single frame in the middle
     9# Note that SAM2 only propagates segmentation masks forward in a video
    10(
    11    dataset
    12    .match_frames(F("frame_number") != 100)
    13    .set_field("frames.gt_detections", None)
    14    .save()
    15)
    16
    17model = foz.load_zoo_model("med-sam-2-video-torch")
    18
    19# Segment inside boxes and propagate to all frames
    20dataset.apply_model(
    21    model,
    22    label_field="pred_segmentations",
    23    prompt_field="frames.gt_detections",
    24)
    25
    26session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
