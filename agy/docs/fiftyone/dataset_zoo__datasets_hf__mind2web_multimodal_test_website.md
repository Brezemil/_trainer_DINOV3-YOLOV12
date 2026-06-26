---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/mind2web_multimodal_test_website.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/mind2web_multimodal_test_website)

# Dataset Card for Multimodal Mind2Web âCross-Websiteâ Test Split#

**Note** : This dataset is the test split of the Cross-Website dataset introduced in the paper.

![image/png](https://huggingface.co/datasets/Voxel51/mind2web_multimodal_test_website/resolve/main/m2w_tw.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1019 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/mind2web_multimodal_test_website")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Details for âCross-Websiteâ Split in Multimodal Mind2Web#

## Dataset Description#

**Curated by:** The Ohio State University NLP Group (OSU-NLP-Group)  
**Shared by:** OSU-NLP-Group on Hugging Face  
**Language(s) (NLP):** en  
**License:** OPEN-RAIL License (mentioned in the Impact Statements section)

## Dataset Sources#

**Repository:** https://github.com/OSU-NLP-Group/SeeAct and https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web  
**Paper:** âGPT-4V(ision) is a Generalist Web Agent, if Groundedâ by Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su  
**Demo:** https://osu-nlp-group.github.io/SeeAct

## Uses#

### Direct Use#

  * Evaluating web agentsâ ability to generalize to new websites within familiar domains

  * Testing website-level transfer capabilities of models

  * Benchmarking adaptability to new website interfaces with similar functionality

  * Assessing how models handle design variations within the same domain category




### Out-of-Scope Use#

  * Developing web agents for harmful purposes (as stated in the paperâs impact statement)

  * Automating actions that could violate website terms of service

  * Creating agents that access usersâ personal profiles or perform sensitive operations without consent




## Dataset Structure#

  * Contains 142 tasks across 9 domains and 10 websites

  * Tasks average 7.2 actions each

  * Average 4,653 visual tokens per task (highest among the three splits)

  * Average 612 HTML elements per task (most complex pages among the splits)

  * Average 114,358 HTML tokens per task

  * Each example includes task descriptions, HTML structure, operations (CLICK, TYPE, SELECT), target elements with attributes, and action histories




### FiftyOne Dataset Structure#

**Basic Info:** 1,338 web UI screenshots with task-based annotations

**Core Fields:**

  * `action_uid`: StringField - Unique action identifier

  * `annotation_id`: StringField - Annotation identifier

  * `target_action_index`: IntField - Index of target action in sequence

  * `ground_truth`: EmbeddedDocumentField(Detection) - Element to interact with:

    * `label`: Action type (TYPE, CLICK)

    * `bounding_box`: a list of relative bounding box coordinates in [0, 1] in the following format: `<top-left-x>, <top-left-y>, <width>, <height>]`

    * `target_action_reprs`: String representation of target action

  * `website`: EmbeddedDocumentField(Classification) - Website name

  * `domain`: EmbeddedDocumentField(Classification) - Website domain category

  * `subdomain`: EmbeddedDocumentField(Classification) - Website subdomain category

  * `task_description`: StringField - Natural language description of the task

  * `full_sequence`: ListField(StringField) - Complete sequence of actions for the task

  * `previous_actions`: ListField - Actions already performed in the sequence

  * `current_action`: StringField - Action to be performed

  * `alternative_candidates`: EmbeddedDocumentField(Detections) - Other possible elements




## Dataset Creation#

### Curation Rationale#

The Cross-Website split was specifically designed to evaluate an agentâs ability to generalize to new websites within domains it has encountered during training, representing a medium difficulty generalization scenario.

### Source Data#

#### Data Collection and Processing#

  * Based on the original MIND2WEB dataset

  * Each HTML document is aligned with its corresponding webpage screenshot image

  * Underwent human verification to confirm element visibility and correct rendering for action prediction

  * Specifically includes 10 new websites from the top-level domains represented in the training data




#### Who are the source data producers?#

Web screenshots and HTML were collected from 10 websites across 9 domains that were represented in the training data, but the specific websites were held out.

### Annotations#

#### Annotation process#

Each task includes annotated action sequences showing the correct steps to complete the task. These were likely captured through a tool that records user actions on websites.

#### Who are the annotators?#

Researchers from The Ohio State University NLP Group or hired annotators, though specific details arenât provided in the paper.

### Personal and Sensitive Information#

The dataset focuses on non-login tasks to comply with user agreements and avoid privacy issues.

## Bias, Risks, and Limitations#

  * This split presents a medium difficulty generalization scenario, testing adaptation to new interfaces within familiar domains

  * In-context learning methods show advantages over supervised fine-tuning on this split

  * The pages in this split are the most complex in terms of HTML elements and have the highest average visual tokens

  * Website layouts and functionality may change over time, affecting the validity of the dataset

  * Limited to only 10 websites across 9 domains, may not capture the full diversity of websites within those domains




## Citation#

### BibTeX:#
    
    
    @article{zheng2024seeact,
      title={GPT-4V(ision) is a Generalist Web Agent, if Grounded},
      author={Boyuan Zheng and Boyu Gou and Jihyung Kil and Huan Sun and Yu Su},
      booktitle={Forty-first International Conference on Machine Learning},
      year={2024},
      url={https://openreview.net/forum?id=piecKJ2DlB},
    }
    
    @inproceedings{deng2023mindweb,
      title={Mind2Web: Towards a Generalist Agent for the Web},
      author={Xiang Deng and Yu Gu and Boyuan Zheng and Shijie Chen and Samuel Stevens and Boshi Wang and Huan Sun and Yu Su},
      booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
      year={2023},
      url={https://openreview.net/forum?id=kiYqbO3wqw}
    }
    

### APA:#

Zheng, B., Gou, B., Kil, J., Sun, H., & Su, Y. (2024). GPT-4V(ision) is a Generalist Web Agent, if Grounded. arXiv preprint arXiv:2401.01614.

## Dataset Card Contact#

GitHub: https://github.com/OSU-NLP-Group/SeeAct

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
