---
source_url: https://docs.voxel51.com/model_zoo/models/segment_anything_2_1_hiera_small_video_torch.html
---

# segment-anything-2.1-hiera-small-video-torch#

Improved video segmenter maintaining quick performance on compact hardware while enhancing mask quality.

**Details**

  * Model name: `segment-anything-2.1-hiera-small-video-torch`

  * Model source: <https://ai.meta.com/sam2/>

  * Model author: Nikhila Ravi, et al.

  * Model license: Apache 2.0, BSD 3-Clause

  * Model size: 175.87 MB

  * Exposes embeddings? no

  * Tags: `segment-anything, torch, zero-shot, video, transformer, official`




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
     4
     5dataset = foz.load_zoo_dataset("quickstart-video", max_samples=2)
     6
     7# Only retain detections in the first frame
     8(
     9    dataset
    10    .match_frames(F("frame_number") > 1)
    11    .set_field("frames.detections", None)
    12    .save()
    13)
    14
    15model = foz.load_zoo_model("segment-anything-2.1-hiera-small-video-torch")
    16
    17# Segment inside boxes and propagate to all frames
    18dataset.apply_model(
    19    model,
    20    label_field="segmentations",
    21    prompt_field="frames.detections",  # can contain Detections or Keypoints
    22)
    23
    24session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
