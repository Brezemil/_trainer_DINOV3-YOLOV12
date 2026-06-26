---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/guiact_smartphone_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/guiact_smartphone_test)

# GUIAct Smartphone Dataset - Test Split#

![image/png](https://huggingface.co/datasets/Voxel51/guiact_smartphone_test/resolve/main/guiact_smartphone.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2079 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/guiact_smartphone_test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The GUIAct Smartphone dataset is a collection of multi-step action instructions for smartphone GUI navigation tasks. It was created by converting and adapting a subset of the AITW ([Androids in the Wild](https://arxiv.org/abs/2307.10088)) dataset, specifically focusing on data with the âGeneralâ tag. The dataset contains sequences of actions (such as tap, swipe, input) paired with smartphone screenshots, designed to train vision language models to navigate smartphone interfaces. Each instruction requires multiple actions to complete the task, with actions mapped to a standardized format that includes position information. The dataset serves as a crucial component of the larger GUICourse collection for training versatile GUI agents.

  * **Curated by:** Wentong Chen, Junbo Cui, Jinyi Hu, and other researchers from Tsinghua University, Renmin University of China, and other institutions as listed in the GUICourse paper

  * **Shared by:** The authors of the GUICourse paper

  * **Language(s) (NLP):** en

  * **License:** CC BY 4.0




### Dataset Sources#

  * **Repository:** https://github.com/yiye3/GUICourse and https://huggingface.co/datasets/yiye2023/GUIAct

  * **Paper:** âGUICourse: From General Vision Language Model to Versatile GUI Agentâ (arXiv:2406.11317v1)




## Uses#

### Direct Use#

The GUIAct Smartphone dataset is intended to be used for training and evaluating GUI agents that can navigate smartphone interfaces using visual inputs. Specific use cases include:

  1. Training vision language models to understand smartphone interface elements and their functions

  2. Teaching models to execute multi-step operations on smartphones based on natural language instructions

  3. Developing assistive technologies that can help users navigate smartphone interfaces

  4. Benchmarking the performance of GUI agents on smartphone navigation tasks




### Out-of-Scope Use#

The dataset is not intended to:

  1. Train models to access private user data on smartphones

  2. Enable unauthorized access to smartphone systems

  3. Replace human decision-making for critical smartphone operations

  4. Train agents to perform tasks beyond the scope of normal smartphone interface interactions

  5. Work with smartphone operating systems or applications not represented in the dataset




## Dataset Structure#

The GUIAct Smartphone dataset contains 9,157 multi-step action instructions which correspond to approximately 67,000 training samples. Each sample consists of:

  1. A smartphone screenshot (image)

  2. One or more actions to be performed on that screenshot

  3. Natural language instruction describing the task to be accomplished




The action space includes standardized actions such as:

  * **tap** : Single-point touch on the screen with position coordinates

  * **swipe** : Multi-point gesture with start and end coordinates

  * **input** : Text entry with content specified

  * **enter** : Submission action

  * **answer** : Task completion indication with text output




Actions include position information represented in either absolute pixel coordinates or relative position format (normalized to a range of 0-1 or 0-1000).

## FiftyOne Dataset Structure#

# GUIAct Smartphone Test Dataset Structure#

**Basic Info:** 2,079 mobile UI screenshots with interaction annotations

**Core Fields:**

  * `id`: ObjectIdField - Unique identifier

  * `filepath`: StringField - Image path

  * `tags`: ListField(StringField) - Sample categories

  * `metadata`: EmbeddedDocumentField - Image properties (size, dimensions)

  * `episode`: StringField - Unique identifier for interaction sequence

  * `step`: IntField - Sequential position within episode

  * `question`: StringField - Natural language task description

  * `current_action`: StringField - Current action to perform

  * `structured_history`: ListField - Previous actions in sequence

  * `ui_elements`: EmbeddedDocumentField(Detections) containing multiple Detection objects:

    * `label`: Element type (ICON_*, TEXT)

    * `bounding_box`: a list of relative bounding box coordinates in [0, 1] in the following format: `[<top-left-x>, <top-left-y>, <width>, <height>]`

    * `text`: Text content of element if present

  * `action`: EmbeddedDocumentField(Keypoints) containing interaction points:

    * `label`: Action type (tap, swipe)

    * `points`: A list of `(x, y)` keypoints in `[0, 1] x [0, 1]`, `[[x, y]]` for tap or `[[x1, y1], [x2, y2]]` for swipe




The dataset captures smartphone screen interactions with detailed UI element annotations and action sequences for mobile interaction research.

## Dataset Creation#

### Curation Rationale#

The GUIAct Smartphone dataset was created to provide training data for visual-based GUI agents that can navigate smartphone interfaces. The authors identified limitations in existing datasets for training such agents, including scenarios that were too simplistic, too narrow in domain focus, or too small in size. By adapting data from the larger AITW dataset, they aimed to provide a substantial collection of realistic smartphone navigation tasks for training robust GUI agents.

### Source Data#

#### Data Collection and Processing#

The GUIAct Smartphone dataset was derived from the AITW dataset by:

  1. Selecting data with the âGeneralâ tag from AITW

  2. Filtering out screenshots that did not include the bottom navigation bar

  3. Converting the original AITW action format to the unified action space defined for GUICourse:

     * âdual-point gestureâ actions were split into âtapâ and âswipeâ based on distance

     * âtypeâ actions were renamed to âinputâ actions

     * âenterâ actions were preserved

     * âgo back/homeâ actions were converted to âtapâ actions on the bottom navigation bar

     * âtask complete/impossibleâ actions were converted to âanswerâ actions




#### Personal and Sensitive Information#

The paper does not explicitly address whether the smartphone screenshots contain personal or sensitive information. However, since the dataset is derived from AITW and intended for research purposes, it likely avoids including personally identifiable information in the screenshots.

## Bias, Risks, and Limitations#

  * The dataset may reflect biases present in smartphone interface design

  * The tasks represented may not cover the full diversity of smartphone usage patterns across different user demographics

  * The dataset is likely limited to specific smartphone operating systems and applications

  * Performance of models trained on this data may not generalize to significantly different smartphone interfaces or to future interface designs

  * The action space simplification (e.g., converting dual-point gestures to tap/swipe) may not capture the full complexity of human smartphone interaction




### Recommendations#

Users should be aware that:

  * Models trained on this dataset may perform differently across different smartphone operating systems or UI designs

  * The simplified action space may limit the range of interactions possible with trained models

  * Evaluation should consider both action accuracy and overall task completion

  * For deployment in assistive technologies, additional safety measures and user feedback mechanisms are advisable

  * The dataset should be used as part of a broader training approach that includes ethical considerations for AI assistance




## Citation#

**BibTeX:**
    
    
    @article{chen2024guicourse,
      title={GUICourse: From General Vision Language Model to Versatile GUI Agent},
      author={Chen, Wentong and Cui, Junbo and Hu, Jinyi and Qin, Yujia and Fang, Junjie and Zhao, Yue and Wang, Chongyi and Liu, Jun and Chen, Guirong and Huo, Yupeng and Yao, Yuan and Lin, Yankai and Liu, Zhiyuan and Sun, Maosong},
      journal={arXiv preprint arXiv:2406.11317},
      year={2024}
    }
    

**APA:** Chen, W., Cui, J., Hu, J., Qin, Y., Fang, J., Zhao, Y., Wang, C., Liu, J., Chen, G., Huo, Y., Yao, Y., Lin, Y., Liu, Z., & Sun, M. (2024). GUICourse: From General Vision Language Model to Versatile GUI Agent. arXiv preprint arXiv:2406.11317.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
