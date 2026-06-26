---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/qwen3_5_vl.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/qwen3_5_vl)

# Qwen3.5-VL FiftyOne Zoo Model#

A FiftyOne remote zoo model integration for [Qwen3.5](https://huggingface.co/Qwen/Qwen3.5-9B), a multimodal vision-language model that supports both **image** and **video** understanding in a single model instance.

## Quick Start#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # Register and download
    foz.register_zoo_model_source(
        "https://github.com/harpreetsahota204/qwen3_5_vl",
        overwrite=True
    )
    
    foz.download_zoo_model(
        "https://github.com/harpreetsahota204/qwen3_5_vl",
        model_name="Qwen/Qwen3.5-9B",
    )
    
    # Load for image tasks
    dataset = foz.load_zoo_dataset("quickstart")
    
    model = foz.load_zoo_model(
        "Qwen/Qwen3.5-9B",
        media_type="image",
        operation="vqa",
    )
    
    model.prompt = "Describe what is happening in this image."
    dataset.apply_model(model, label_field="description", batch_size=8)
    
    session = fo.launch_app(dataset)
    

## Features#

  * **5 image operations** : VQA, object detection, keypoint detection, image classification, and 3D bounding box detection

  * **6 video operations** : description, temporal localization, object tracking, OCR, comprehensive analysis, and custom prompts

  * **True GPU batching** : multiple images processed in a single `model.generate()` call using left-padded batch inference

  * **Thinking mode support** : reasoning chains (text before `</think>`) stored as a `reasoning` attribute on each label

  * **Per-sample prompts** : pass a dataset field as the prompt source via `prompt_field`

  * **3D bounding boxes** : projects 3D detections to 2D using real or auto-generated camera intrinsics

  * **bfloat16** on Ampere+ GPUs (compute capability â¥ 8.0), `auto` dtype otherwise




* * *

## Installation#
    
    
    pip install fiftyone qwen-vl-utils decord accelerate
    

* * *

## Supported Models#

Model | VRAM  
---|---  
`Qwen/Qwen3.5-9B` | ~18 GB  
  
* * *

## Image Operations#

Load the model with `media_type="image"` to work on image datasets. Switch operations by setting `model.operation` â each operation has a built-in system prompt you can inspect with `print(model.system_prompt)`.

### Visual Question Answering#
    
    
    model = foz.load_zoo_model("Qwen/Qwen3.5-9B", media_type="image")
    
    model.operation = "vqa"
    model.prompt = "List all objects in this image separated by commas."
    
    dataset.apply_model(model, label_field="q_vqa", batch_size=8, num_workers=4)
    
    dataset.first().q_vqa  # str
    

**Output** : `str`

### Object Detection#
    
    
    model.operation = "detect"
    
    print(model.system_prompt)  # inspect the default system prompt
    
    model.prompt = "Detect any person, animal, or vehicle in this image."
    
    dataset.apply_model(model, label_field="qdets", batch_size=8, num_workers=4)
    

**Output** : `fo.Detections` â bounding boxes normalized to `[0, 1]`, coordinates derived from 0â1000 model output scale.

### Keypoint Detection#
    
    
    model.operation = "point"
    model.prompt = "Locate the face of each person in this image."
    
    dataset.apply_model(model, label_field="qpts", batch_size=8, num_workers=4)
    

**Output** : `fo.Keypoints` â point coordinates normalized to `[0, 1]`.

### Image Classification#
    
    
    model.operation = "classify"
    model.prompt = "List the potential image quality issues in this image which would make it unsuitable for training a vision model."
    
    print(model.system_prompt)
    
    dataset.apply_model(model, label_field="q_cls", batch_size=8, num_workers=4)
    

**Output** : `fo.Classifications` â multi-label classification results.

### Grounded Operations#

Use a previously computed VQA field as the per-sample prompt to ground detection or pointing to specific objects:
    
    
    # First run VQA to generate per-sample descriptions
    model.operation = "vqa"
    model.prompt = "List all objects in this image."
    dataset.apply_model(model, label_field="q_vqa")
    
    # Use the VQA output as a per-sample prompt for detection
    model.operation = "detect"
    dataset.apply_model(
        model,
        label_field="grounded_qdets",
        prompt_field="q_vqa",  # each sample uses its own VQA output as the prompt
    )
    
    # Same for keypoint detection
    model.operation = "point"
    dataset.apply_model(
        model,
        label_field="grounded_kpts",
        prompt_field="q_vqa",
    )
    

* * *

## Video Operations#

Load the model with `media_type="video"` to work on video datasets. Operations that produce temporal or frame-level labels require `dataset.compute_metadata()` to be run first.
    
    
    video_dataset = foz.load_zoo_dataset("quickstart-video")
    video_dataset.compute_metadata()  # required for all operations except description
    
    model = foz.load_zoo_model("Qwen/Qwen3.5-9B", media_type="video")
    

### Description#

Plain-text summary of video content. Does not require metadata.
    
    
    model.operation = "description"
    
    video_dataset.apply_model(model, label_field="desc")
    # result stored in sample.desc_summary (str)
    

### Temporal Localization#

Detects activity events with precise start/end timestamps.
    
    
    model.operation = "temporal_localization"
    
    video_dataset.apply_model(model, label_field="events")
    # result stored in sample.events (fo.TemporalDetections)
    

### Object Tracking#

Tracks objects across frames with per-frame bounding boxes.
    
    
    model.operation = "tracking"
    
    video_dataset.apply_model(model, label_field="tracking")
    # result stored in sample.frames[N].objects (fo.Detections)
    

### Video OCR#

Extracts text appearing in frames with bounding boxes.
    
    
    model.operation = "ocr"
    
    video_dataset.apply_model(model, label_field="ocr")
    # result stored in sample.frames[N].text_content (fo.Detections)
    

### Comprehensive Analysis#

Performs all analyses in a single pass: description, temporal events, object appearances, scene metadata, and activities.
    
    
    model.operation = "comprehensive"
    
    video_dataset.apply_model(model, label_field="analysis")
    

**Output fields** (all prefixed with `label_field`):

  * `analysis_summary` â plain text description

  * `analysis_events` â `fo.TemporalDetections`

  * `analysis_objects` â `fo.TemporalDetections` (object appearances)

  * `analysis_scene_info_*` â `fo.Classification` per scene attribute

  * `analysis_activities_*` â `fo.Classifications`

  * `sample.frames[N].objects` â frame-level `fo.Detections`

  * `sample.frames[N].text_content` â frame-level OCR `fo.Detections`




### Custom Prompts#

Full control over the prompt for domain-specific analysis. Returns raw text in `label_field_result`.
    
    
    model.operation = "custom"
    model.custom_prompt = """Analyze this video and describe:
    - Any safety hazards visible
    - Compliance with PPE requirements
    
    Output JSON: {"hazards": [...], "ppe_compliance": "compliant/non-compliant"}
    """
    
    video_dataset.apply_model(model, label_field="safety_analysis")
    # raw text in sample.safety_analysis_result
    

* * *

## Thinking Mode and Reasoning#

Qwen3.5 may prefix its response with an internal reasoning chain ending with `</think>`. The model automatically strips this before parsing labels, and stores it as a `"reasoning"` dynamic attribute on each label if present:
    
    
    det = dataset.first().qdets.detections[0]
    print(det.label)
    print(det["reasoning"])  # the model's thinking chain, if any
    

* * *

## Output Format Reference#

Operation | Output type | FiftyOne label  
---|---|---  
`vqa` | `str` | Plain string field  
`detect` | `fo.Detections` | Normalized `[x, y, w, h]` bounding boxes  
`point` | `fo.Keypoints` | Normalized `[x, y]` points  
`classify` | `fo.Classifications` | Multi-label list  
`description` | `str` in `_summary` field | Plain string  
`temporal_localization` | `fo.TemporalDetections` in `_events` field | Frame-range detections  
`tracking` | Frame-level `fo.Detections` in `frames.objects` | Per-frame bounding boxes  
`ocr` | Frame-level `fo.Detections` in `frames.text_content` | Per-frame text boxes  
`comprehensive` | Mixed â see above | Multiple fields  
`custom` | `str` in `_result` field | Raw text  
  
* * *

## Technical Details#

  * **Batch inference** : images are processed as a true GPU batch (left-padded, single `generate()` call). Video inference is sequential per sample due to variable frame counts.

  * **Coordinate system** : all 2D coordinates from the model are in 0â1000 scale, normalized to `[0, 1]` on output.

  * **3D rotation angles** : the model outputs rotation values as fractions of Ï. The implementation converts to radians as `model_value Ã Ï`.

  * **dtype** : `bfloat16` on Ampere+ GPUs (CUDA compute capability â¥ 8.0), `torch_dtype="auto"` otherwise.

  * **Metadata requirement** : video operations that produce temporal or frame-level labels require `dataset.compute_metadata()` to be called first.




* * *

## Citation#
    
    
    @misc{qwen3,
      title  = {Qwen3 Technical Report},
      author = {Qwen Team},
      year   = {2025},
      url    = {https://huggingface.co/Qwen/Qwen3.5-9B}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
