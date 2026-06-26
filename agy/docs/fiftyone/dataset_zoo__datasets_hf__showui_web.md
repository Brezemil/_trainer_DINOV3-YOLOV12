---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/showui_web.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ShowUI_Web)

# Dataset Card for ShowUI_Web#

![image/png](https://huggingface.co/datasets/Voxel51/ShowUI_Web/resolve/main/showui_web.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 21988 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/ShowUI_Web")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Web Dataset from ShowUI#

## Dataset Details#

### Dataset Description#

The Web dataset is a custom-collected corpus of web interface screenshots and element annotations created specifically for training GUI visual agents. It focuses on visually rich UI elements across 22 representative website scenarios (including Airbnb, Booking, AMD, Apple, etc.), purposefully filtering out static text elements to concentrate on interactive components like buttons and checkboxes. This curation strategy was based on the observation that most Vision-Language Models already possess strong OCR capabilities, making visually interactive elements more valuable for training.

  * **Curated by:** Show Lab, National University of Singapore and Microsoft

  * **Language(s) (NLP):** en

  * **License:** Apache-2.0




### Dataset Sources#

  * **Repository:** https://github.com/showlab/ShowUI (main project repository) and https://huggingface.co/datasets/showlab/ShowUI-web

  * **Paper:** https://arxiv.org/abs/2411.17465




## Uses#

### Direct Use#

The dataset is designed for training vision-language-action models for GUI visual agents operating in web environments. It can be used for:

  * Training models to identify interactive UI elements visually

  * Web element grounding (mapping textual queries to visual elements)

  * Supporting web navigation tasks by providing high-quality visual element references

  * Learning to distinguish between different types of web UI components




### Out-of-Scope Use#

While not explicitly stated in the paper, this dataset would likely be unsuitable for:

  * Training models for desktop or mobile interfaces exclusively

  * General image understanding unrelated to UI navigation

  * Training models where text-based element identification is the primary goal

  * Applications requiring user data or personalized interfaces




## Dataset Structure#

The dataset contains:

  * 22,000 web screenshots across 22 representative website scenarios

  * 576,000 annotated UI elements (filtered from an original 926,000)

  * An average of 26 elements per screenshot

  * Element annotations focus on interactive visual components (buttons, checkboxes, etc.)

  * Annotations exclude static text elements (which comprised about 40% of the original data)




## FiftyOne Dataset Structure#

**Basic Info:** 21,988 web UI screenshots with interaction annotations

**Core Fields:**

  * `instructions`: ListField(StringField) - List of potential text instructions or UI element texts

  * `detections`: EmbeddedDocumentField(Detections) containing multiple Detection objects:

    * `label`: Element type (e.g., âListItemâ)

    * `bounding_box`: A list of relative bounding box coordinates in [0, 1] in the following format: `[<top-left-x>, <top-left-y>, <width>, <height>]`

    * `text`: Text content of element

  * `keypoints`: EmbeddedDocumentField(Keypoints) containing interaction points:

    * `label`: Element type (e.g., âListItemâ)

    * `points`: A list of `(x, y)` keypoints in `[0, 1] x [0, 1]`

    * `text`: Text content associated with the interaction point




The dataset captures web interface elements and interaction points with detailed text annotations for web interaction research. Each element has both its bounding box coordinates and a corresponding interaction point, allowing for both element detection and precise interaction targeting.

## Dataset Creation#

### Curation Rationale#

The authors identified that most existing web datasets contain a high proportion of static text elements (around 40%) that provide limited value for training visual GUI agents, since modern Vision-Language Models already possess strong OCR capabilities. Instead, they focused on collecting visually distinctive interactive elements that would better enable models to learn UI navigation skills. This selective approach prioritizes quality and relevance over raw quantity.

### Source Data#

#### Data Collection and Processing#

The authors:

  1. Developed a custom parser using PyAutoGUI

  2. Selected 22 representative website scenarios (including Airbnb, Booking, AMD, Apple, etc.)

  3. Collected multiple screenshots per scenario to maximize annotation coverage

  4. Initially gathered 926,000 element annotations across 22,000 screenshots

  5. Filtered out elements classified as static text, retaining 576,000 visually interactive elements

  6. Focused on elements tagged with categories like âButtonâ or âCheckboxâ




#### Who are the source data producers?#

The data was collected from 22 publicly accessible websites across various domains (e-commerce, technology, travel, etc.). The specific screenshots and annotations were produced by the authors of the ShowUI paper (Show Lab, National University of Singapore and Microsoft).

## Bias, Risks, and Limitations#

The paper doesnât explicitly discuss biases or limitations specific to this dataset, but potential limitations might include:

  * Limited to 22 website scenarios, which may not represent the full diversity of web interfaces

  * Filtering out static text could limit the modelâs ability to handle text-heavy interfaces

  * Potential overrepresentation of popular or mainstream websites compared to niche or specialized interfaces

  * May not capture the full range of web accessibility features or alternative UI designs




### Recommendations#

Users should be aware that this dataset deliberately excludes static text elements, which makes it complementary to text-focused datasets but potentially incomplete on its own. For comprehensive web navigation models, it should be used alongside datasets that include text recognition capabilities. Additionally, researchers may want to evaluate whether the 22 selected website scenarios adequately represent their target application domains.

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
