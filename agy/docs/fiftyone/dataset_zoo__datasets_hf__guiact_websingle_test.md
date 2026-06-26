---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/guiact_websingle_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/guiact_websingle_test)

# Dataset Card for GUIAct Web-Single Dataset - Test Set#

![image/png](https://huggingface.co/datasets/Voxel51/guiact_websingle_test/resolve/main/guiact_websingle.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1410 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/guiact_websingle_test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The GUIAct Web-Single dataset is a comprehensive collection of single-step action instructions for website GUI navigation tasks. It contains approximately 67,000 instruction-action pairs, each consisting of a natural language instruction and a corresponding action to be performed on a website screenshot. The dataset is designed to train vision language models to understand and interact with web interfaces through actions such as clicking, inputting text, scrolling, and other common web interactions. Each instruction is paired with a single action to be performed on the visual content of a website, making it an ideal resource for teaching models the fundamental operations of web navigation.

  * **Curated by:** Wentong Chen, Junbo Cui, Jinyi Hu, and other researchers from Tsinghua University, Renmin University of China, and other institutions as listed in the GUICourse paper

  * **Shared by:** The authors of the GUICourse paper

  * **Language(s) (NLP):** en

  * **License:** CC BY 4.0




### Dataset Sources#

  * **Repository:** https://github.com/yiye3/GUICourse and https://huggingface.co/datasets/yiye2023/GUIAct

  * **Paper:** âGUICourse: From General Vision Language Model to Versatile GUI Agentâ (arXiv:2406.11317v1)




## Uses#

### Direct Use#

The GUIAct Web-Single dataset is intended to be used for:

  1. Training vision language models to recognize and interact with website elements

  2. Teaching models to map natural language instructions to appropriate GUI actions

  3. Developing assistive technologies that can help users navigate websites

  4. Benchmarking the performance of GUI agents on basic website navigation tasks

  5. Enabling research on vision-based web automation and navigation




### Out-of-Scope Use#

The dataset is not intended to:

  1. Train models to access private user data on websites

  2. Enable unauthorized access to website systems or bypass security measures

  3. Generate adversarial examples to manipulate website behavior

  4. Train agents to perform harmful actions on websites

  5. Replace human decision-making for critical web operations




## Dataset Structure#

The GUIAct Web-Single dataset contains approximately 67,000 instruction-action pairs derived from around 13,000 website screenshots. Each sample consists of:

  1. A website screenshot (image)

  2. A natural language instruction describing a task to be performed

  3. A single action to be performed on that screenshot




The action space includes standardized actions such as:

  * **click** : Selecting an element on the page with position coordinates

  * **input** : Text entry with content specified

  * **select:** Choose a specific value from a drop-down menu.

  * **scroll** : Page navigation with direction and amount information

  * **enter** : Submission action

  * **answer** : Information extraction response with text output




Actions include position information represented in either absolute pixel coordinates or relative position format (normalized to a range of 0-1).

## FiftyOne Dataset Structure#

# GUIAct WebSingle Test Dataset Structure#

**Basic Info:** 1,410 web UI screenshots with interaction annotations

**Core Fields:**

  * `uid`: StringField - Unique identifier for the task instance

  * `question`: StringField - Natural language task description

  * `ui_elements`: EmbeddedDocumentField(Detections) containing multiple Detection objects:

    * `label`: Sequential numeric ID for element (e.g., â1â, â2â)

    * `bounding_box`: Coordinates as [x, y, width, height] in normalized format (0-1)

    * `text`: Text content of element if present

  * `action_detections`: EmbeddedDocumentField(Detections) containing target interaction elements:

    * `label`: Action type (e.g., âclickâ, âinputâ, etc)

    * `bounding_box`: A list of relative bounding box coordinates in [0, 1] in the following format: `[<top-left-x>, <top-left-y>, <width>, <height>]`

    * `order`: Sequential order of action

  * `structured_history`: ListField(StringField) - Previous actions in structured text format

  * `action_keypoints`: EmbeddedDocumentField(Keypoints) - A list of `(x, y)` keypoints in `[0, 1] x [0, 1]`

  * `action_classifications`: EmbeddedDocumentField(Classifications) - Action classification information (if used)




The dataset captures web interface interactions with detailed UI element annotations and action specifications for web-based task completion research.

## Dataset Creation#

### Curation Rationale#

The GUIAct Web-Single dataset was created to address the limitations of existing GUI navigation datasets, which often featured simplified environments, narrow domains, or insufficient size for effectively training visual-based GUI agents. The authors aimed to create a large-scale dataset of realistic web navigation tasks that could teach models the fundamental knowledge of GUI functions and control methods.

### Source Data#

#### Data Collection and Processing#

The GUIAct Web-Single dataset was created through a four-step process:

  1. **Websites selection** : GPT-4 was used to gather diverse scenarios (e.g., online shopping, E-learning) and URLs. These URLs served as seeds to expand to new websites via hyperlinks, resulting in 50 domains and 13,000 websites.

  2. **Captures acquisition** : Web snapshot tools were used to capture website HTML, interactive elements, and screenshots based on the collected URLs.

  3. **LLM-Auto Annotation** : GPT-4V was employed to generate single-step instruction-action pairs for each website. For each request, two images were provided to GPT-4V: an original screenshot and a revised screenshot with interactive element identification. This process yielded approximately 70,000 instruction-action pairs.

  4. **Data checking** : Human annotators reviewed the automatically generated instruction-action pairs, revising inaccurate items or abandoning those difficult to revise. This quality control step improved the accuracy of the data from 55% to 92%, resulting in the final dataset of approximately 67,000 high-quality instruction-action pairs.




#### Who are the source data producers?#

The source data combines:

  1. Websites created by various web developers and organizations across 50 different domains

  2. Instruction-action pairs initially generated by GPT-4V (an AI system)

  3. Human annotators who verified and corrected the automatically generated data




The demographic information of the human annotators is not specified in detail, though the paper mentions they were paid 0.6 RMB per item, with an hourly salary of approximately 54 RMB.

### Annotations#

#### Annotation process#

The annotation process consisted of two major phases:

  1. **Automatic annotation** : GPT-4V was provided with two images per website - an original screenshot and a version with element identification markers. GPT-4V generated instruction-action pairs based on these inputs.

  2. **Human verification** : Annotators checked the quality of the automatically generated instruction-action pairs. They were instructed to:

     * Revise inaccurate items

     * Abandon items that were difficult to revise

     * Ensure the accuracy of element positions and action parameters




The verification process improved the accuracy of the dataset from 55% to 92% based on sampled evaluation results. Each item took approximately 40 seconds to check.

#### Personal and Sensitive Information#

The paper does not explicitly address whether the web screenshots contain personal or sensitive information. However, since the dataset is derived from public websites and intended for research purposes, it likely avoids including personally identifiable information in the screenshots. The authors note in the Ethical Considerations section that they âcanât guarantee there is no offensive content in these website screenshotsâ from the broader GUIEnv dataset, which suggests some level of awareness about content concerns.

## Bias, Risks, and Limitations#

  * The dataset may reflect biases present in website design and content

  * The 50 domains represented may not cover the full diversity of web interfaces and functionalities

  * Performance of models trained on this data may not generalize to significantly different website designs or to web applications with complex interaction patterns

  * The single-step nature of the instructions limits the complexity of tasks that can be learned

  * The action space simplification may not capture some nuanced web interactions

  * The effectiveness of the dataset depends partly on the quality of GPT-4Vâs initial annotations




### Recommendations#

Users should be aware that:

  * Models trained on this dataset will be limited to the types of web interfaces represented in the data

  * The single-step nature of the instructions makes this dataset most suitable for learning basic web interactions, not complex multi-step tasks

  * For deployment in assistive technologies, additional safety measures should be implemented

  * The dataset should be used as part of a broader training approach that includes ethical considerations

  * Evaluation should consider both action accuracy and the appropriateness of the action given the instruction




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
