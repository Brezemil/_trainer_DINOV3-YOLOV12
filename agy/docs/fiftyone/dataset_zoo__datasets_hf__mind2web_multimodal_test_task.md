---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/mind2web_multimodal_test_task.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/mind2web_multimodal_test_task)

# Dataset Card for Multimodal Mind2Web âCross-Taskâ Test Split#

**Note** : This dataset is the test split of the Cross-Task dataset introduced in the paper.

![image/png](https://huggingface.co/datasets/Voxel51/mind2web_multimodal_test_task/resolve/main/m2w_tt.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1338 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/mind2web_multimodal_test_task")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Description#

**Curated by:** The Ohio State University NLP Group (OSU-NLP-Group)  
**Shared by:** OSU-NLP-Group on Hugging Face  
**Language(s) (NLP):** en  
**License:** OPEN-RAIL License

## Dataset Source#

**Repository:** https://github.com/OSU-NLP-Group/SeeAct and https://huggingface.co/datasets/osunlp/Multimodal-Mind2Web  
**Paper:** âGPT-4V(ision) is a Generalist Web Agent, if Groundedâ by Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, Yu Su  
**Demo:** https://osu-nlp-group.github.io/SeeAct

## Uses#

### Direct Use#

  * Evaluating web agentsâ ability to generalize to new tasks on familiar websites

  * Benchmarking LMMs and LLMs on web navigation tasks

  * Training and fine-tuning models for web navigation

  * Testing model performance on tasks that require following multi-step instructions




### Out-of-Scope Use#

  * Developing web agents for harmful purposes (as stated in the paperâs impact statement)

  * Automating actions that could violate website terms of service

  * Creating agents that access usersâ personal profiles or perform sensitive operations without consent




## Dataset Structure#

  * Contains 177 tasks across 17 domains and 64 websites

  * Tasks average 7.6 actions each

  * Average 4,172 visual tokens per task

  * Average 607 HTML elements per task

  * Average 123,274 HTML tokens per task

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

The Cross-Task split was specifically designed to evaluate an agentâs ability to generalize to new tasks on websites and domains it has already encountered during training.

### Source Data#

#### Data Collection and Processing#

  * Based on the original MIND2WEB dataset

  * Each HTML document is aligned with its corresponding webpage screenshot image

  * Underwent human verification to confirm element visibility and correct rendering for action prediction




#### Who are the source data producers?#

Web screenshots and HTML were collected from 64 websites across 17 domains that were also represented in the training data.

### Annotations#

#### Annotation process#

Each task includes annotated action sequences showing the correct steps to complete the task. These were likely captured through a tool that records user actions on websites.

#### Who are the annotators?#

Researchers from The Ohio State University NLP Group or hired annotators, though specific details arenât provided in the paper.

### Personal and Sensitive Information#

The dataset focuses on non-login tasks to comply with user agreements and avoid privacy issues.

## Bias, Risks, and Limitations#

  * Performance on this split is generally better than Cross-Website and Cross-Domain, as models can leverage knowledge of website structures

  * Supervised fine-tuning methods show advantages on this split compared to in-context learning

  * The dataset may contain biases present in the original websites

  * Website layouts and functionality may change over time, affecting the validity of the dataset




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
