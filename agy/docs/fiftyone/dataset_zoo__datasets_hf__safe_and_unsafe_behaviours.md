---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/safe_and_unsafe_behaviours.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Safe_and_Unsafe_Behaviours)

# Dataset Card for safe_unsafe_behaviours#

![image/png](https://huggingface.co/datasets/Voxel51/Safe_and_Unsafe_Behaviours/resolve/main/safe_unsafe.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 691 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/Safe_and_Unsafe_Behaviours")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

A high-resolution video dataset of safe and unsafe workplace behaviors collected from security cameras at a production facility, designed for occupational accident prevention research. The dataset contains 691 video clips capturing 8 behavior classes (4 safe, 4 unsafe) that represent common safety compliance scenarios in industrial environments including walkway violations, unauthorized equipment interventions, panel cover states, and forklift load compliance.

  * **Curated by:** OÄuzhan Ãnal and Emre DandÄ±l, Department of Computer Engineering, Faculty of Engineering, Bilecik Åeyh Edebali University, Bilecik, Turkey

  * **Shared by:** KafaoÄlu Metal Plastik Makine San. ve Tic. A.Å., EskiÅehir, Turkey

  * **Language(s) (NLP):** en

  * **License:** CC BY 4.0




### Dataset Sources#

  * **Repository:** https://data.mendeley.com/datasets/xjmtb22pff/1

  * **Paper:** https://www.sciencedirect.com/science/article/pii/S235234092400756X




## Uses#

### Direct Use#

  * Video classification for industrial safety monitoring systems

  * Action recognition and temporal behavior detection research

  * Training real-time unsafe behavior detection models

  * Benchmarking video understanding models on industrial surveillance footage

  * Computer vision research for occupational health and safety applications




### Out-of-Scope Use#

  * Deployment in environments significantly different from industrial manufacturing settings

  * Worker surveillance or performance monitoring without proper consent and ethical oversight

  * Applications requiring detection of safety behaviors not represented in the 8 defined classes




## Dataset Structure#

This dataset is formatted for [FiftyOne](https://github.com/voxel51/fiftyone), an open-source tool for building high-quality datasets and computer vision models.

**Dataset Info:**

  * **Name:** `safe_unsafe_behaviours`

  * **Media type:** video

  * **Num samples:** 691

  * **Splits:** `train` (566 samples), `test` (125 samples) â indicated via sample tags




**Sample Fields:**

Field | Type | Description  
---|---|---  
`id` | ObjectIdField | Unique sample identifier  
`filepath` | StringField | Path to video file  
`tags` | ListField(StringField) | Split tags: `train` or `test`  
`metadata` | EmbeddedDocumentField(VideoMetadata) | Video metadata (resolution, duration, fps, etc.)  
`ground_truth` | EmbeddedDocumentField(Classification) | Video-level behavior classification label  
  
**Frame Fields:**

Field | Type | Description  
---|---|---  
`id` | ObjectIdField | Unique frame identifier  
`frame_number` | FrameNumberField | Frame index within video  
  
**Classes (8 total):**

Class | Behavior Type | Description  
---|---|---  
`Safe Walkway Violation` | Unsafe | Worker goes beyond designated safe walkway boundaries  
`Unauthorized Intervention` | Unsafe | Worker intervenes on equipment without proper safety gear/authorization  
`Opened Panel Cover` | Unsafe | Panel cover left open after intervention  
`Carrying Overload with Forklift` | Unsafe | Forklift carrying 3+ blocks  
`Safe Walkway` | Safe | Worker stays within designated walkway  
`Authorized Intervention` | Safe | Worker properly equipped for equipment intervention  
`Closed Panel Cover` | Safe | Panel cover properly closed  
`Safe Carrying` | Safe | Forklift carrying 2 or fewer blocks  
  
**Video Specifications:**

  * Resolution: 1920Ã1080 pixels

  * Frame rate: 24 fps

  * Format: MP4

  * Duration: 1â20 seconds per clip




## Dataset Creation#

### Curation Rationale#

Unsafe behavior is a leading cause of workplace injuries and deaths. Despite regular safety inspections, accidents occur due to breaches of occupational health and safety protocols. This dataset was created to support the development of computer vision systems capable of real-time detection of unsafe behaviors before accidents occur, addressing the need for automated, continuous safety monitoring in industrial environments.

### Source Data#

#### Data Collection and Processing#

Video footage was collected from security cameras at KafaoÄlu Metal Plastik Makine San. ve Tic. A.Å., a production facility in an organized industrial zone in EskiÅehir, Turkey. Collection occurred between November 5, 2022 and December 13, 2022 (39 days) using two different IP cameras. After collection, domain experts reviewed the footage to identify segments containing the defined safe and unsafe behaviors, extracting clips of 1â20 seconds containing the target behaviors.

#### Who are the source data producers?#

Workers and employees at KafaoÄlu Metal Plastik Makine San. ve Tic. A.Å. performing normal production activities. Necessary permissions were obtained from company officials and employees prior to data collection.

### Annotations#

#### Annotation process#

After videos were collected, frames containing safe and unsafe behaviors were identified by domain experts including factory managers and occupational safety specialists. Video clips were then extracted from the full surveillance footage. Some videos contain a single behavior class while others may contain multiple behavior classes.

#### Who are the annotators?#

Domain experts including factory managers and the occupational safety specialist at the facility where the videos were collected, in collaboration with the research team.

#### Personal and Sensitive Information#

The dataset contains video footage of workers performing their duties in an industrial setting. Workersâ faces and bodies are visible in the footage. Proper permissions were obtained from company officials and employees for the use of video recordings and images in academic studies. The permission documentation is maintained at the Department of Computer Engineering, Faculty of Engineering, Bilecik Åeyh Edebali University.

## Bias, Risks, and Limitations#

  * **Single environment:** Data collected from one facility in Turkey, which may limit generalization to other industrial settings, equipment configurations, or geographic contexts

  * **Temporal scope:** 39-day collection period may not capture seasonal variations in behavior or clothing

  * **Class definitions:** Safety behaviors are specific to this facilityâs protocols and may not align with regulations in other jurisdictions

  * **Scale:** 691 videos is relatively small for training deep learning models; data augmentation may be necessary

  * **Camera perspectives:** Only two camera viewpoints represented




### Recommendations#

Users should consider domain adaptation techniques when applying models trained on this dataset to different industrial environments. The dataset is best suited for research and prototyping rather than direct production deployment without additional validation on target environments.

## Citation#

**BibTeX:**
    
    
    @article{ONAL2024110756,
      title = {Video dataset for the detection of safe and unsafe behaviours in workplaces},
      journal = {Data in Brief},
      volume = {56},
      pages = {110756},
      year = {2024},
      issn = {2352-3409},
      doi = {https://doi.org/10.1016/j.dib.2024.110756},
      url = {https://www.sciencedirect.com/science/article/pii/S235234092400756X},
      author = {OÄuzhan Ãnal and Emre DandÄ±l}
    }
    

**APA:**

Ãnal, O., & DandÄ±l, E. (2024). Video dataset for the detection of safe and unsafe behaviours in workplaces. Data in Brief, 56, 110756. https://doi.org/10.1016/j.dib.2024.110756

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
