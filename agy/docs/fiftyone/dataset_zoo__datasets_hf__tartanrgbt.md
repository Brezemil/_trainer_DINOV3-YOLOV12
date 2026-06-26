---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/tartanrgbt.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/TartanRGBT)

# TartanRGBT Dataset Card#

![image/png](https://huggingface.co/datasets/Voxel51/TartanRGBT/resolve/main/tartanrgbt.gif)

TartanRGBT is a hardware-synchronized **RGBâthermal** robotics dataset from CMU AirLabâs [AnyThermal](https://anythermal.github.io/) project (ICRA 2026). Features co-registered stereo RGB and thermal images across indoor, urban, park, and off-road environments.

**This subset:**

  * 15 trajectories

  * 5,952 timesteps

  * 1 Hz sampling

  * 23,808 FiftyOne samples




This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5952 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/TartanRGBT")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Sources#

  * **Source:** [theairlabcmu/TartanRGBT](https://huggingface.co/datasets/theairlabcmu/TartanRGBT)

  * **Paper:** [arXiv:2602.06203](https://arxiv.org/abs/2602.06203)

  * **License:** BSD-3-Clause-Clear




## Data Streams#

Each timestep provides 4 synchronized camera streams:

Stream | Resolution | Notes  
---|---|---  
**RGB in thermal frame** | 640 Ã 512 | ZED RGB reprojected to thermal grid. Pixel-aligned with left thermal. **Primary RGBâthermal pair.**  
Left thermal | 640 Ã 512 | FLIR Boson 640+, 8-bit grayscale  
Right thermal | 640 Ã 512 | FLIR Boson 640+, 8-bit grayscale  
ZED left RGB | 960 Ã 540 | Native rectified stereo  
ZED right RGB | 960 Ã 540 | Native rectified stereo  
Stereo depth | 960 Ã 540 | Dense depth map (meters), aligned with ZED left  
  
## Scenes#

15 scenes across 5 collection days covering indoor, urban, park, and off-road terrain.

## FiftyOne Structure#

  * **Type:** Grouped dataset

  * **Default slice:** `rgb_in_thermal`

  * **Groups:** 5,952




### Key Fields#

Field | Type | Description  
---|---|---  
`day` | str | `"day1"` â `"day5"`  
`scene_name` | str | e.g. `"park_frick_seq_1_riverview_trail"`  
`frame_id` | int | Frame index (0, 10, 20, â¦)  
`timestamp` | float | Unix time (seconds)  
`ffc_dropped` | bool | **Exclude from training if` True`** (thermal calibration event)  
`pose_x/y/z` | float | Position (meters, from stereo odometry)  
`pose_qx/qy/qz/qw` | float | Orientation (quaternion)  
  
### Labels#

  * **`thermal`** (`rgb_in_thermal` slice): Heatmap overlay of thermal intensity on RGB

  * **`depth`** (`zed_left` slice): Display-optimized depth (masked, percentile-normalized)

  * **`depth_gt`** (`zed_left` slice): Raw depth visualization (min/max normalized)




## Use Cases#

**Intended:**

  * RGBâthermal representation learning & knowledge distillation

  * Cross-modal place recognition

  * Monocular thermal depth estimation

  * Multi-environment thermal features




**Out of scope:**

  * Odometry or metric depth benchmarking (stereo-derived, not ground truth)

  * GPS-based localization




## Citation#
    
    
    @misc{maheshwari2026anythermallearninguniversalrepresentations,
      title={AnyThermal: Towards Learning Universal Representations for Thermal Perception},
      author={Parv Maheshwari and Jay Karhade and Yogesh Chawla and Isaiah Adu and Florian Heisen
              and Andrew Porco and Andrew Jong and Yifei Liu and Santosh Pitla
              and Sebastian Scherer and Wenshan Wang},
      year={2026},
      eprint={2602.06203},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
