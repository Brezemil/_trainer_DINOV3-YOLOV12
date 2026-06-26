---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/rcs_utn_green_box.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/rcs_utn_green_box)

# Dataset Card for RCS UTN Green Box (FiftyOne)#

![FiftyOne](https://img.shields.io/badge/FiftyOne-grouped%20video-orange)

![image/png](https://huggingface.co/datasets/Voxel51/rcs_utn_green_box/resolve/main/rsc_green_box.gif)

**rcs_utn_green_box** is a grouped FiftyOne video dataset of a multi-view robot manipulation task â _âpick the green boxâ_ â collected with the **Robot Control Stack (RCS)** ecosystem from the University of Technology Nuremberg. Each episode is a group with one synchronized video per camera, plus dense robot proprioception and action data on every frame.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    dataset = load_from_hub("Voxel51/rcs_utn_green_box")
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Robot Control Stack (RCS) is a lean, modular ecosystem for robot learning at scale, with a unified interface for simulated and physical robots to facilitate sim-to-real transfer. This dataset captures a single cube-picking task recorded from five camera perspectives, with per-frame joint states, end-effector poses, gripper state, actions, and the tracked cube pose â the kind of multi-view, multi-modal trajectory data used to train and evaluate Vision-Language-Action (VLA) policies.

This FiftyOne version is a **grouped video dataset** : each episode links the five camera streams so they can be scrubbed together in the App, with robot state and actions rendered as per-frame numeric fields.

  * **Project page:** [robotcontrolstack.github.io](https://robotcontrolstack.github.io)

  * **Paper:** [Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale](https://arxiv.org/abs/2509.14932) (JÃ¼lg, Krack, Bien et al., UTN)

  * **License:** Apache-2.0 (RCS project license)




* * *

## FiftyOne Dataset Structure#

**Dataset name:** `rcs_utn_green_box`

**Media type:** `group`

**Default group slice:** `side_wide`

### Summary#

Property | Value  
---|---  
Groups (episodes) | 143  
Video samples (total) | 715  
Group slices | `side_wide`, `wrist`, `side_right`, `bird_eye`, `side`  
Language instruction | `pick the green box`  
  
### Groups and slices#

Each episode is one demonstration. The five linked slices are the camera perspectives recorded during that episode:

Slice | Description  
---|---  
`side_wide` | Wide side view (default slice)  
`wrist` | Wrist-mounted camera  
`side_right` | Right-side view  
`bird_eye` | Top-down birdâs-eye view  
`side` | Side view  
  
Videos are encoded as H.264 / `yuv420p` (30 fps) from the source JPEG frames for in-App playback.

### Sample-level fields#

Field | Type | Description  
---|---|---  
`episode_id` | string | Episode identifier (from the source parquet shard)  
`camera` | string | Camera/slice name for this sample  
`language_instruction` | string | Natural-language task description  
`intrinsics` | list | Camera intrinsics for this view  
`extrinsics` | list | Camera extrinsics for this view  
  
### Frame-level fields#

Field | Type | Description  
---|---|---  
`step` | int | Step index within the episode  
`timestamp` | float | Frame timestamp  
`reward` | float | Per-step reward  
`success` | bool | Success flag  
`joints` | list(float) | Robot joint positions  
`tquat` | list(float) | End-effector pose (translation + quaternion)  
`xyzrpy` | list(float) | End-effector pose (xyz + roll/pitch/yaw)  
`gripper` | float | Gripper state  
`action_tquat` | list(float) | Commanded end-effector action (translation + quaternion)  
`action_gripper` | float | Commanded gripper action  
`cube_pos_tquat` | list(float) | Tracked green-cube pose (translation + quaternion)  
  
## Citation#
    
    
    @article{juelg2025rcs,
      title   = {Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale},
      author  = {J\"ulg, Tobias and Krack, Pierre and Bien, Seongjin and Blei, Yannik and Gamal, Khaled and Nakahara, Ken and Hechtl, Johannes and Calandra, Roberto and Burgard, Wolfram and Walter, Florian},
      journal = {arXiv preprint arXiv:2509.14932},
      year    = {2025}
    }
    

## License#

The source Robot Control Stack project is released under the Apache-2.0 License.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
