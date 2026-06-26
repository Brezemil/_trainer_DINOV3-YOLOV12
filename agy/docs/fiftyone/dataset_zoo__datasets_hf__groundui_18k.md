---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/groundui_18k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/GroundUI-18k)

# Dataset Card for GroundUI-18k Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/GroundUI-18k/resolve/main/groundui18k.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 18026 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/GroundUI-18k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# GroundUI-18K Dataset Details#

## Dataset Description#

**Curated by:** Longtao Zheng, Zhiyuan Huang, Zhenghai Xue, Xinrun Wang, Bo An, and Shuicheng Yan as part of the AgentStudio project team

**Funded by:** NTU, ETH Zurich, Skywork AI, NUS, and SMU (based on author affiliations)

**Shared by:** AgentStudio project team via their HF Dataset repository: https://huggingface.co/datasets/agent-studio/GroundUI-18K

**Language(s) (NLP):** en

**License:** Not explicitly stated in the paper, likely MIT License or another open-source license (as most research datasets)

## Dataset Sources#

**Repository:** https://ltzheng.github.io/agent-studio and https://huggingface.co/datasets/agent-studio/GroundUI-18K

**Paper [optional]:** âAgentStudio: A Toolkit for Building General Virtual Agentsâ (ICLR 2025)

## Uses#

### Direct Use#

  * Benchmarking UI grounding capabilities of virtual agents

  * Training and fine-tuning models for precise UI element localization

  * Evaluating cross-platform generalization of vision-language models

  * Developing more accurate GUI interaction systems




### Out-of-Scope Use#

  * Using the dataset for creating systems that automate malicious actions on user interfaces

  * Extracting personal or sensitive information that might be present in screenshots

  * Training models for surveillance or unauthorized monitoring of user activities

  * Developing systems that could compromise user privacy or security




## Dataset Structure#

The dataset contains 18,026 data entries with 13,522 unique screenshots across web, desktop, and mobile platforms. Each data entry is structured as:

  * Instruction: Text description of the action to perform

  * Screenshot: Image of the UI

  * Bounding Box: Coordinates (x1, y1, x2, y2) of the target UI element

  * Resolution: Screen resolution of the screenshot

  * Source: Origin dataset of the sample

  * Platform: Web, desktop, or mobile




The dataset is divided across platforms:

  * Web: Samples from websites and web applications

  * Desktop: Samples from desktop operating systems and applications

  * Mobile: Samples from mobile devices and applications




## FiftyOne Dataset Structure#

# GroundUI-18k Dataset Structure#

**Basic Info:** 18,026 UI screenshots with element annotations

**Core Fields:**

  * `instruction`: StringField - Task instruction or element description (e.g., âClick on âDaVinci Resolve - getââ)

  * `source`: StringField - Data origin source (e.g., âomniactâ)

  * `platform`: StringField - UI platform (web, mobile, desktop)

  * `detections`: EmbeddedDocumentField(Detection) - UI element detection information:

    * `label`: Element type (e.g., âgrounding_elementâ)

    * `bounding_box`: a list of relative bounding box coordinates in [0, 1] in the following format: `<top-left-x>, <top-left-y>, <width>, <height>]`




The dataset provides annotated UI elements with contextual instructions for performing specific actions across different platforms, primarily focused on grounding natural language instructions to UI elements.

## Dataset Creation#

### Curation Rationale#

The dataset was created to address limitations in existing UI grounding benchmarks:

  1. Previous datasets had ambiguous or incorrect instructions

  2. Existing datasets were platform-specific and used different formats

  3. Most datasets lacked standardized evaluation metrics

  4. There was a need for a comprehensive benchmark spanning multiple platforms and applications




The goal was to create a reliable benchmark for evaluating a fundamental capability of virtual agents - accurately locating and interacting with UI elements.

### Source Data#

#### Data Collection and Processing#

The dataset combines samples from several existing datasets:

  * 9,268 entries from Mind2Web test sets

  * 3,804 entries from OmniACT test sets

  * 3,455 entries from MoTIF test sets

  * 1,272 entries from ScreenSpot benchmark

  * 227 entries newly annotated using AgentStudioâs GUI annotation tool




For quality improvement, instructions were recaptioned using GPT-4o when the original instructions were ambiguous or incorrect. The process involved:

  1. Overlaying ground truth actions onto each screenshot

  2. Using GPT-4o to generate detailed descriptions of the plotted GUI elements

  3. Verifying the clarity and accuracy of the new instructions




Data without annotated bounding boxes was filtered out during processing.

#### Who are the source data producers?#

The source data comes from:

  * Mind2Web: Web interactions dataset

  * OmniACT: A dataset spanning multiple platforms

  * MoTIF: Mobile UI interactions dataset

  * ScreenSpot: Screenshots dataset with 610 screenshots and 1,272 instructions

  * AgentStudio: Additional samples collected by the authors using their annotation tools




### Annotations [optional]#

#### Annotation process#

The authors used the original bounding box annotations for existing datasets. For ambiguous or incorrect instructions, they performed recaptioning using GPT-4o.

For the 227 newly collected samples, the authors used the AgentStudio GUI annotation tool, which allows:

  1. Capturing screenshots

  2. Drawing bounding boxes around UI elements

  3. Writing step-level instructions

  4. Saving the annotations in a standardized format




#### Who are the annotators?#

For recaptioning, GPT-4o was used to generate improved instructions.

For the newly collected samples, likely the research team members served as annotators, though this is not explicitly stated in the paper.

### Personal and Sensitive Information#

The paper does not explicitly address potential personal information in screenshots. However, UI screenshots may contain:

  * User interface layouts

  * Application content

  * Potentially user data if present in the applications




Itâs likely the authors took steps to minimize personal information in the screenshots, but this isnât explicitly detailed in the paper.

## Bias, Risks, and Limitations#

  * **Platform bias** : Although the dataset covers multiple platforms, there may be imbalances in representation

  * **Application bias** : Some applications may be overrepresented compared to others

  * **Language bias** : Instructions are in English only

  * **Design bias** : UI designs change over time, making the dataset potentially less relevant as UI designs evolve

  * **Instruction quality** : Despite recaptioning efforts, some instructions may still be imperfect

  * **Bounding box precision** : Annotations may have different standards of precision across source datasets




## Recommendations#

Users should be aware of:

  * The datasetâs focus on single-step instructions rather than complex multi-step tasks

  * Potential biases in platform representation

  * The datasetâs value for benchmarking but potential limitations for real-world deployment

  * The need to consider user privacy when working with UI screenshots




When using this dataset, researchers should:

  * Report performance across different platforms separately

  * Consider element size when analyzing results (as noted in the paper, larger elements are easier to identify)

  * Be cautious about overfitting to this specific dataset




## Citation [optional]#

### BibTeX:#
    
    
    @inproceedings{zheng2025agentstudio,
      title={AgentStudio: A Toolkit for Building General Virtual Agents},
      author={Zheng, Longtao and Huang, Zhiyuan and Xue, Zhenghai and Wang, Xinrun and An, Bo and Yan, Shuicheng},
      booktitle={International Conference on Learning Representations},
      year={2025},
      url={https://ltzheng.github.io/agent-studio}
    }
    

### APA:#

Zheng, L., Huang, Z., Xue, Z., Wang, X., An, B., & Yan, S. (2025). AgentStudio: A Toolkit for Building General Virtual Agents. In the International Conference on Learning Representations (ICLR 2025).

## Dataset Card Contact#

For more information about the dataset, contact the authors through the project website: https://ltzheng.github.io/agent-studio

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
