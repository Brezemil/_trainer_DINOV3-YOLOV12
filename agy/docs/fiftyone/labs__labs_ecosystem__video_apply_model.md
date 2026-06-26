---
source_url: https://docs.voxel51.com/labs/labs_ecosystem/video_apply_model.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-labs/tree/main/plugins/video_apply_model)

# Apply image model to video frames#

The `video_apply_model` operator offers a torch dataloader for loading videos frames from a FiftyOne video dataset and applying the image model to each video frame.

This Labs feature supports reading videos from a FiftyOne video dataset via `model_inference.TorchVideoFramesDataset` which uses FFmpeg decoder and loads chunks of frames from each video.

## Usage#

### Via FiftyOne App#
    
    
    import fiftyone.zoo as foz
    import fiftyone as fo
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    session = fo.launch_app(dataset)
    

![Operators panel](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/video_apply_model/assets/operators_list_screenshot.png)

_Select video_apply_model operator_

![Apply model parameters](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/video_apply_model/assets/operator_screenshot.png)

### Via code#
    
    
    import fiftyone.zoo as foz
    from labs.plugins.video_apply_model import model_inference
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    model = foz.load_zoo_model("clip-vit-base32-torch")
    
    model_inference.apply_image_model_to_video_frames(
        dataset,
        model,
        label_field="predictions",
        frames_chunk_size=64,
        num_workers=8,
        confidence_thresh=0.5,
        skip_failures=True,
        parse_type="sequential",
    )
    

## TODOs#

  * Add support for model class filtering




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
