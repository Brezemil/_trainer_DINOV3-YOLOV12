---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/showui_desktop.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ShowUI_desktop)

# Desktop Dataset from ShowUI#

![image/png](https://huggingface.co/datasets/Voxel51/ShowUI_desktop/resolve/main/showui_desktop.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7496 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/ShowUI_desktop")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Desktop dataset is an augmented version of OmniAct Desktop data, containing UI elements from desktop software applications. It features 100 screenshots with originally 2,000 raw element annotations from 15 different software applications across iOS, Windows, and Linux desktop environments. The original dataset contained only basic element names (e.g., âmessage_ashâ), but was enhanced through GPT-4o-assisted annotation to generate three distinct query types for each element: appearance descriptions, spatial relationship descriptions, and intentional queries. This augmentation expanded the dataset from 2,000 to 8,000 elements without requiring additional screenshots.

  * **Curated by:** Show Lab, National University of Singapore and Microsoft

  * **Language(s) (NLP):** en

  * **License:** Apache-2.0




### Dataset Sources#

  * **GitHub Repo:** https://github.com/showlab/ShowUI/

  * **HF Dataset Repo:** https://huggingface.co/datasets/showlab/ShowUI-desktop




## Uses#

### Direct Use#

The dataset is designed for training vision-language-action models for GUI visual agents, specifically to improve UI element grounding capabilities across desktop platforms. It can be used for training models to:

  * Visually identify UI elements based on appearance descriptions

  * Locate elements based on their spatial relationships with other elements

  * Understand user intent and map it to the appropriate UI element




### Out-of-Scope Use#

While the paper doesnât explicitly mention out-of-scope uses, this dataset is likely not suitable for:

  * Training models for web or mobile interfaces exclusively (without combining with appropriate datasets for those platforms)

  * General visual understanding tasks unrelated to UI navigation

  * Training models for non-English interface navigation




## Dataset Structure#

The dataset contains ~8,000 element annotations across 100 desktop screenshots from 15 different applications. Each element annotation includes:

  1. Original element name from OmniAct

  2. Bounding box coordinates

  3. Three types of descriptive queries per element:

     * Appearance description (visual characteristics like color, shape, text)

     * Spatial relationship description (position relative to other UI elements)

     * Intentional query (purpose or user intent related to the element)




# FiftyOne Dataset Structure#

**Basic Info:** 7,496 desktop UI screenshots with interaction annotations

**Core Fields:**

  * `instruction`: StringField - Task description in structured format

  * `action_detections`: EmbeddedDocumentField(Detection) containing target element:

    * `label`: Action type (e.g., âactionâ)

    * `bounding_box`: A list of relative bounding box coordinates in [0, 1] in the following format: `[<top-left-x>, <top-left-y>, <width>, <height>]`

  * `action_keypoints`: EmbeddedDocumentField(Keypoints) containing interaction points:

    * `label`: Action type (e.g., âactionâ)

    * `points`: A list of `(x, y)` keypoints in `[0, 1] x [0, 1]`

  * `query_type`: EmbeddedDocumentField(Classification) - Type of instruction query (e.g., âoriginalâ)

  * `interfaces`: EmbeddedDocumentField(Classification) - Interface application type (e.g., âaudibleâ)




The dataset captures desktop application interactions with detailed UI element annotations and action points for interface interaction research across different desktop applications.

## Dataset Creation#

### Curation Rationale#

The authors identified desktop data as particularly valuable but challenging to collect automatically. The original OmniAct dataset provided manually annotated elements, but with limited annotation diversity (only element names). To improve model training for desktop UI navigation, they needed more diverse query types that reflected how users might describe or search for UI elements.

### Source Data#

#### Data Collection and Processing#

The team started with the existing OmniAct Desktop dataset (100 screenshots, 2,000 elements). They employed âreverse engineeringâ techniques using the ground-truth bounding boxes and text elements from the original dataset. For augmentation, they:

  1. Identified the original elements and their bounding boxes

  2. Created visual prompts with red bounding boxes highlighting target elements

  3. Used GPT-4o with a specific prompt template (detailed in Appendix B.2 of the paper)

  4. Generated three distinct query types per element

  5. This process expanded the dataset to 8,000 elements without requiring additional screenshots




#### Who are the source data producers?#

The original data came from OmniAct, while the augmentation was performed by the authors of the ShowUI paper (Show Lab, National University of Singapore and Microsoft).

### Annotations#

#### Annotation process#

The annotation process involved:

  1. Extracting original element names from OmniAct

  2. Prompting GPT-4o with screenshots containing highlighted target elements

  3. Using a specific prompt template that requests three types of descriptions:

     * Appearance-based (15 words or fewer)

     * Spatial relationship-based (15 words or fewer)

     * Situation/intention-based (15 words or fewer)

  4. Formatting responses in JSON structure




#### Who are the annotators?#

The annotations were produced using GPT-4o, prompted by the authors of the ShowUI paper.

### Recommendations#

Users should be aware that this is a relatively small dataset augmented with AI-generated descriptions. While the authors demonstrate its effectiveness when combined with other data sources, it may not be comprehensive enough on its own for training robust GUI agents. It would be most effective when used as part of a balanced training regime alongside web and mobile UI datasets.

## Citation#

**BibTeX:**
    
    
    @misc{lin2024showui,
          title={ShowUI: One Vision-Language-Action Model for GUI Visual Agent}, 
          author={Kevin Qinghong Lin and Linjie Li and Difei Gao and Zhengyuan Yang and Shiwei Wu and Zechen Bai and Weixian Lei and Lijuan Wang and Mike Zheng Shou},
          year={2024},
          eprint={2411.17465},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2411.17465}, 
    }
    

**APA:** Lin, K. Q., Li, L., Gao, D., Yang, Z., Wu, S., Bai, Z., Lei, S. W., Wang, L., & Shou, M. Z. (2024). ShowUI: One Vision-Language-Action Model for GUI Visual Agent. arXiv preprint arXiv:2411.17465.

## Dataset Card Contact#

GitHub: https://github.com/showlab/ShowUI

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
