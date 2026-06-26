---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/skyscenes.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/SkyScenes)

# Dataset Card for SkyScenes#

![image](https://huggingface.co/datasets/Voxel51/SkyScenes/resolve/main/skyscene-fo.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 280 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/SkyScenes")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

SkyScenes is a comprehensive synthetic dataset for aerial scene understanding that was recently accepted to ECCV 2024. The dataset contains 33,600 aerial images captured from UAV perspectives using the CARLA simulator.

The original repo on the Hub can be found [here](https://huggingface.co/datasets/hoffman-lab/SkyScenes).

  * **Curated by:** [Sahil Khose](https://sahilkhose.github.io/), Anisha Pal, Aayushi Agarwal, Deepanshi, Judy Hoffman, Prithvijit Chattopadhyay

  * **Funded by:** Georgia Institute of Technology

  * **Shared by:** [Harpreet Sahota](https://huggingface.co/harpreetsahota), Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:** MIT License




### Dataset Structure#

  * **Images** : RGB images captured across multiple variations:

    * 8 different town layouts (7 urban + 1 rural)

    * 5 weather/time conditions (ClearNoon, ClearSunset, ClearNight, CloudyNoon, MidRainyNoon)

    * 12 viewpoint combinations (3 heights Ã 4 pitch angles)




### Annotations#

Each image comes with dense pixel-level annotations for:

  * Semantic segmentation (28 classes)

  * Instance segmentation

  * Depth information




### Key Variations#

  * **Heights** : 15m, 35m, 60m

  * **Pitch Angles** : 0Â°, 45Â°, 60Â°, 90Â°

  * **Weather/Time** : Various conditions to test robustness

  * **Layouts** : Different urban and rural environments




### NOTE: This repo contains only a subset of the full dataset:#

  * **Heights & Pitch Angles**:

    * H_15_P_0 (15m height, 0Â° pitch)

    * H_35_P_0 (35m height, 0Â° pitch)

    * H_60_P_0 (60m height, 0Â° pitch)

  * **Weather Condition** : ClearNoon only

  * **Town Layouts** : Town01, Town02, Town05, Town07

  * **Data Modalities** :

    * RGB Images

    * Depth Maps

    * Semantic Segmentation




If you wish to work with the full dataset in FiftyOne format, you can use the [following repo](https://github.com/harpreetsahota204/skyscenes-to-fiftyone).

### Dataset Sources#

  * **Repository:** https://github.com/hoffman-group/SkyScenes

  * **Paper:** https://arxiv.org/abs/2312.06719

  * **Demo:** https://hoffman-group.github.io/SkyScenes/




# Uses#

The dataset contains 33.6k densely annotated synthetic aerial images with comprehensive metadata and annotations, making it suitable for both training and systematic evaluation of aerial scene understanding models.

## Training and Pre-training#

  * Functions as a pre-training dataset for real-world aerial scene understanding models

  * Models trained on SkyScenes demonstrate strong generalization to real-world scenarios

  * Can effectively augment real-world training data to improve overall model performance




## Model Evaluation and Testing#

**Diagnostic Testing**

  * Serves as a test bed for assessing model sensitivity to various conditions including:

    * Weather changes

    * Time of day variations

    * Different pitch angles

    * Various altitudes

    * Different layout types




**Multi-modal Development**

  * Enables development of multi-modal segmentation models by incorporating depth information alongside visual data

  * Supports testing how additional sensor modalities can improve aerial scene recognition capabilities




## Research Applications#

  * Enables studying synthetic-to-real domain adaptation for aerial imagery

  * Provides controlled variations for analyzing model behavior under different viewing conditions

  * Supports development of models for:

    * Semantic segmentation

    * Instance segmentation

    * Depth estimation




## References#

  * [SkyScenes Dataset on HuggingFace](https://huggingface.co/datasets/hoffman-lab/SkyScenes)

  * [SkyScenes Official Website](https://hoffman-group.github.io/SkyScenes/)




## Citation#
    
    
    @misc{khose2023skyscenes,
          title={SkyScenes: A Synthetic Dataset for Aerial Scene Understanding}, 
          author={Sahil Khose and Anisha Pal and Aayushi Agarwal and Deepanshi and Judy Hoffman and Prithvijit Chattopadhyay},
          year={2023},
          eprint={2312.06719},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
