---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/motif_1k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/motif-1k)

# Dataset Card for MotIF-1K#

![image/png](https://huggingface.co/datasets/Voxel51/motif-1k/resolve/main/motif1k.gif)

MotIF-1K is a robotics motion dataset containing 1,022 demonstrations across 13 task categories, used to benchmark and fine-tune vision-language models (VLMs) for motion-based success detection. Each demonstration includes a video of the motion, multiple pre-rendered trajectory visualizations, task instructions, and motion descriptions.

The FiftyOne dataset is a **grouped dataset** where each group represents one trajectory and each group slice represents a different visual representation of that trajectory â mirroring the exact input formats used in the paper.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1023 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/motif-1k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Sources#

  * **HuggingFace repository:** https://huggingface.co/datasets/myconnects/motif

  * **Paper:** https://arxiv.org/abs/2409.10683

  * **Code / collection scripts:** https://github.com/Minyoung1005/motif

  * **Paper:** [MotIF: Motion Instruction Fine-tuning](https://arxiv.org/abs/2409.10683) (Hwang et al., 2024)

  * **Project page:** https://motif-1k.github.io

  * **License:** MIT




* * *

## FiftyOne Dataset Structure#

### Grouped Dataset Overview#
    
    
    Dataset name:   motif-1k
    Media type:     group
    Default slice:  video_trajviz
    Groups:         1,022  (653 human_motion + 369 stretch_motion)
    

### Group Slices#

Every trajectory group contains up to 13 slices. Each slice is a separate `fo.Sample` with its own media file and labels. Not all slices are present for every group â see the **Incomplete samples** note below.

Slice name | Media type | Description | Always present?  
---|---|---|---  
`video_trajviz` | video | Raw video with the trajectory overlaid â the **default slice** and the paperâs primary representation | No (absent for 182 incomplete stretch samples)  
`video_raw` | video | Clean video without any trajectory overlay; carries the interactive per-frame trajectory Polyline | Yes  
`last_frame_trajviz` | image | Final video frame with trajectory overlay â **the exact image input used by the paperâs VLM** | No  
`last_frame_raw` | image | Final video frame, no overlay | No  
`opticalflow` | image | Full optical-flow visualization of all keypoints | No  
`storyboard_key2` | image | 2-keyframe storyboard, clean | No  
`storyboard_key2_trajviz` | image | 2-keyframe storyboard with trajectory overlay | No  
`storyboard_key4` | image | 4-keyframe storyboard, clean | No  
`storyboard_key4_trajviz` | image | 4-keyframe storyboard with trajectory overlay | No  
`storyboard_key9` | image | 9-keyframe storyboard, clean | No  
`storyboard_key9_trajviz` | image | 9-keyframe storyboard with trajectory overlay | No  
`storyboard_key16` | image | 16-keyframe storyboard, clean | No  
`storyboard_key16_trajviz` | image | 16-keyframe storyboard with trajectory overlay | No  
  
### Sample-Level Fields#

All fields below are present on every slice of every group.

Field | Type | Description  
---|---|---  
`group` | `Group` | FiftyOne group handle; `group.id` is the trajectory identifier, `group.name` is the slice name  
`config` | `str` | Source config: `"human_motion"` or `"stretch_motion"`  
`traj_idx` | `int` | Trajectory index within its config (0-based)  
`task_instruction` | `str` | High-level task goal, e.g. `"shake the boba"`  
`motion_description` | `str` | Fine-grained motion specification, e.g. `"move to the right and to the left, repeating this sequence 3 times"`  
`num_steps` | `int` | Number of steps as stored in the source (may differ from `trajectory_length`; see notes)  
`trajectory_length` | `int` | Actual number of trajectory points (`len(trajectory)`) â the reliable count  
`has_source_artifacts` | `bool` | Whether this sampleâs group has all pre-rendered visualizations. `False` for 182 incomplete stretch_motion groups  
`tags` | `list[str]` | Always includes the config name; incomplete groups are also tagged `"incomplete"`  
  
### Label Fields#

#### `video_raw` slice â `frames.trajectory` (per-frame Polyline)#

The `video_raw` slice carries a frame-level progressive trajectory annotation. At frame N, the Polyline contains the first N trajectory points, so the path draws itself out as the video plays.

  * Frame 1: a zero-length degenerate segment marking the trajectory start position (renders as a dot)

  * Frame N: the full trajectory path accumulated to that point




Each Polyline carries these label attributes:

Attribute | Type | Description  
---|---|---  
`coord_space` | `str` | Coordinate convention used: `video_pixels`, `video_pixels_offset`, or `realsense_native`  
`has_source_artifacts` | `bool` | Whether the source provided a `last_frame_trajviz` for offset detection  
`correction_method` | `str` | How the trajectory was corrected: `identity`, `detected`, `resolution_median_fallback`, `default_fallback`, or `realsense_heuristic`  
`offset_x` | `float` | Pixel offset applied in x (0 for identity and realsense_heuristic)  
`offset_y` | `float` | Pixel offset applied in y (0 for identity and realsense_heuristic)  
  
All Polyline coordinates are normalized to `[0, 1] Ã [0, 1]` relative to the video frame.

* * *

## Dataset Composition#

Config | Agent | Trajectories | Has all slices?  
---|---|---|---  
`human_motion` | Human (6 different people) | 653 | Yes â all 13 slices  
`stretch_motion` (with artifacts) | Hello Robot Stretch 2 | 188 | Yes â all 13 slices  
`stretch_motion` (incomplete) | Hello Robot Stretch 2 | 182 | `video_raw` only; tagged `"incomplete"`  
**Total** |  | **1,022** |   
  
### Task Categories#

13 categories spanning non-interactive, object-interactive, and user-interactive motions:

Category | Tasks  
---|---  
Non-interactive | Outdoor Navigation, Indoor Navigation, Draw Path  
Object-interactive | Shake, Pick and Place, Stir, Wipe, Open/Close Cabinet, Spread Condiment  
User-interactive | Handover, Brush Hair, Tidy Hair, Style Hair  
  
* * *

## Trajectory Coordinate System#

The `trajectory` field in the source data stores 2D pixel coordinates `[x, y]` per timestep. The coordinate space differs by config â this is a known source-side inconsistency, not a parsing bug:

`coord_space` value | Applies to | Correction applied  
---|---|---  
`video_pixels` | All `human_motion` (653) | Identity â MediaPipe hand detection runs on the cropped video frame, so coordinates match the stored video dimensions directly  
`video_pixels_offset` | `stretch_motion` with artifacts (188) | Per-sample pixel translation detected from the red endpoint marker in `last_frame_trajviz`; confirmed pixel-accurate  
`realsense_native` | `stretch_motion` without artifacts (182) | Best-effort: coordinates divided by 1280Ã720 (the RealSense D435i native capture resolution per the collection script). No source ground truth is available for this subset.  
  
* * *

## Known Data Quality Issues#

The following issues were identified during import and are preserved in the data:

  1. **Incomplete stretch_motion subset (182 groups):** These groups have no pre-rendered visualizations (`video_trajviz`, `last_frame_trajviz`, `opticalflow`, storyboards are all absent). Only `video_raw` is available. These samples cannot be used with the paperâs VLM evaluation methodology without regenerating the visualizations. Identified by `has_source_artifacts == False` or the `"incomplete"` tag.

  2. **`num_steps` vs `trajectory_length` disagreement (~160 rows):** The sourceâs `num_steps` field reflects the original capture length before some post-processing trimmed the trajectory. `trajectory_length` (= `len(trajectory)`) is the reliable count and is used for all frame-level annotations.

  3. **Trajectory partially outside frame:** Some trajectories extend into negative coordinates or past the video edges. FiftyOne clips these gracefully at the frame border; no values are modified.

  4. **Variable video resolutions:** Human demos span 14 different square resolutions (208Ã208 to 480Ã480 plus one 640Ã480). Stretch demos with artifacts use three resolutions (320Ã320, 352Ã352, 480Ã480). The incomplete stretch subset uses eight different resolutions (192Ã192 to 720Ã720).




* * *

## Citation#
    
    
    @article{hwang2024motif,
      title={MotIF: Motion Instruction Fine-tuning},
      author={Hwang, Minyoung and Hejna, Joey and Sadigh, Dorsa and Bisk, Yonatan},
      journal={arXiv preprint arXiv:2409.10683},
      year={2024}
    }
    

**APA:** Hwang, M., Hejna, J., Sadigh, D., & Bisk, Y. (2024). MotIF: Motion Instruction Fine-tuning. _arXiv preprint arXiv:2409.10683_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
