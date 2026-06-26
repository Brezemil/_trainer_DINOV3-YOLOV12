---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/webuot_238_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/WebUOT-238-Test)

# Dataset Card for WebUOT-238-Test#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 238 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/WebUOT-238-Test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Description#

WebUOT-1M is the largest million-scale benchmark for underwater object tracking (UOT), designed to address limitations in existing datasets by providing diverse underwater scenarios, rich annotations, and language prompts. It comprises **1.1 million frames** across **1,500 underwater videos** , covering **408 target categories** categorized into 12 superclasses (e.g., fish, molluscs, inanimate objects). The dataset includes high-quality bounding box annotations, 23 tracking attributes (e.g., illumination variation, camouflage), and language descriptions for multimodal tracking research.

**Note:** This dataset, which has been parsed into FiftyOne format, comprises 238 randomly selected videos from the WebUOT-1M test set for a total of 192,000+ frames.

### Dataset Details#

  * **Curated by:**  
Chunhui Zhang (Shanghai Jiao Tong University), Li Liu (HKUST-Guangzhou), Guanjie Huang (HKUST-Guangzhou), Hao Wen (CloudWalk), Xi Zhou (CloudWalk), Yanfeng Wang (Shanghai Jiao Tong University).

  * **Funded by:**  
National Natural Science Foundation of China (No. 62101351), Key R&D Program of Chongqing (cstc2021jscx-gksbX0032).

  * **Language(s):**  
English (annotations and language prompts).

  * **License:**  
[Creative Commons (intended for academic research).](https://creativecommons.org/licenses/by/4.0/)

  * **Shared by:** [Harpreet Sahota, Hacker-in-Residence @ Voxel51](https://huggingface.co/harpreetsahota)




### Dataset Sources#

  * **Repository:** https://github.com/983632847/Awesome-Multimodal-Object-Tracking/tree/main/WebUOT-1M

  * **Paper:** https://arxiv.org/abs/2405.19818




## Uses#

### Direct Use#

  * Training/evaluating UOT algorithms.

  * Multimodal tracking (vision + language prompts).

  * Studying domain adaptation (underwater vs. open-air environments).

  * Marine conservation, underwater robotics, and search/rescue applications.




### Out-of-Scope Use#

  * Non-underwater tracking tasks (e.g., aerial/terrestrial tracking).

  * Commercial applications without proper licensing.

  * Non-visual tasks (e.g., audio analysis).




## Dataset Structure#

  * **Fields:**

    * Videos: 1,500 clips (1,020 train / 480 test).

    * Annotations: Bounding boxes, absent labels, 23 attributes (e.g., low visibility, similar distractors).

    * Language Prompts: Text descriptions of targets (e.g., âred clownfish in yellow coralâ).

    * Metadata: Object categories (408), superclasses (12), resolution, duration.

  * **Splits:**  
Train/Test sets divided by videos, ensuring no overlap in categories or scenarios.




## Dataset Creation#

### Curation Rationale#

To bridge the gap in UOT research caused by small-scale datasets, WebUOT-1M was created to enable robust model training/evaluation, domain adaptation, and multimodal tracking in complex underwater environments.

### Source Data#

#### Data Collection and Processing#

  * **Sources:** YouTube, Bilibili (filtered for diversity).

  * **Processing:**

    * Manual selection of moving targets.

    * Semi-supervised enhancement for blurry/low-visibility frames.

    * Professional annotation team for bounding boxes and attributes.

    * Final verification by authors.




#### Who are the source data producers?#

Videos were captured by divers, underwater robots, and hobbyists using varied devices (cameras, phones).

### Annotations#

#### Annotation Process#

  * **Tools:** In-house annotation tools; enhanced frames for challenging cases.

  * **Guidelines:** Focus on target motion, bounding box accuracy, and attribute labeling (23 attributes).

  * **Validation:** Multiple rounds of correction by authors.




#### Who are the annotators?#

A professional labeling team and the authors performed verification.

## Citation#

**BibTeX:**
    
    
    @article{zhang2024webuot,
      title={WebUOT-1M: Advancing Deep Underwater Object Tracking with A Million-Scale Benchmark},
      author={Zhang, Chunhui and Liu, Li and Huang, Guanjie and Wen, Hao and Zhou, Xi and Wang, Yanfeng},
      journal={arXiv preprint arXiv:2405.19818},
      year={2024}
    }
    

## Glossary#

The following glossary details the attributes of each video.

Hereâs the content parsed as a markdown table:

Attribute | Definition  
---|---  
01\. LR | If the size of the bounding box of the target in one frame is less than 400 pixels.  
02\. FM | The center position of the target in two consecutive frames exceeds 20 pixels.  
03\. SV | The ratio of the target bounding box is not within the range [0.5, 2].  
04\. ARV | The aspect ratio of the target bounding box is not in the range [0.5, 2].  
05\. CM | There is severe camera movement in the video frame.  
06\. VC | Viewpoint changes significantly affect the appearance of the target.  
07\. PO | If the target appears partially occluded in one frame.  
08\. FO | As long as the target is completely occluded in one frame.  
09\. OV | There is one frame where the target completely leaves the video frame.  
10\. ROT | The target rotates in the video frame.  
11\. DEF | The target appears deformation in the video frame.  
12\. SD | Similarity interference appears around the target.  
13\. IV | The illumination of the target area changes significantly.  
14\. MB | The target area becomes blurred due to target motion or camera motion.  
15\. PTI | In the initial frame only partial information about the target is visible.  
16\. NAO | The target belongs to a natural or artificial object.  
17\. CAM | The target is camouflaging in the video frame.  
18\. UV | The underwater visibility of the target area (low, medium, or high visibility).  
19\. WCV | The color of the water of the target area.  
20\. US | Different underwater scenarios where the target is located.  
21\. SP | Different shooting perspectives (underwater, outside-water, and fish-eye views).  
22\. SIZ | The size s = â(w Ã h) of the video is small (s < â(640 Ã 480)), medium (â(640 Ã 480) â¤ s < â(1280 Ã 720)), or large (s â¥ â(1280 Ã 720)).  
23\. LEN | The length l of the video is short (l â¤ 600 frames), medium (600 frames < l â¤ 1800 frames), or long (l > 1800 frames).  
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
