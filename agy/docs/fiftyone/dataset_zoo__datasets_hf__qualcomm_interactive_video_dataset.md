---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/qualcomm_interactive_video_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/qualcomm-interactive-video-dataset)

# Dataset Card for Qualcomm Interactive Video Dataset#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2900 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/qualcomm-interactive-video-dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Description#

![image/png](https://huggingface.co/datasets/Voxel51/qualcomm-interactive-video-dataset/resolve/main/qivd.gif)

QIVD (Qualcomm Interactive Video Dataset) is a comprehensive video question-answering dataset designed for evaluating multimodal AI models on their ability to understand and reason about video content. The dataset contains 2,900 video samples with associated questions, answers, and temporal annotations. Each sample includes a question about the video content, a detailed answer, a short answer, and a timestamp indicating when the answer can be found in the video.

The dataset covers 13 distinct categories of video understanding tasks, including object referencing, action detection, object attributes, action counting, object counting, and more specialized tasks like audio-visual reasoning and OCR in videos.

  * **Curated by:** Qualcomm AI Research

  * **Funded by:** Qualcomm Technologies, Inc.

  * **Shared by:** Qualcomm AI Research Team

  * **Language(s) (NLP):** en

  * **License:** [Data Research License](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/qvid-dataset-research-license-mar-27-2025.pdf)




### Dataset Sources#

  * **Paper :** [arXiv:2503.19356v1](https://arxiv.org/pdf/2503.19356)

  * **Website:** https://www.qualcomm.com/developer/software/qualcomm-interactive-video-dataset-qivd




## Uses#

### Direct Use#

This dataset is intended for:

  * Training and evaluating video question-answering (VideoQA) models

  * Benchmarking multimodal AI systems on video understanding tasks

  * Research in temporal reasoning and visual-language understanding

  * Developing models that can answer questions about specific moments in videos

  * Fine-tuning large language models with video understanding capabilities

  * Evaluating model performance across different categories of video understanding (object detection, action recognition, counting, etc.)




### Out-of-Scope Use#

This dataset should not be used for:

  * Real-time surveillance or monitoring applications

  * Making decisions about individuals based on video content

  * Any application that could infringe on privacy rights

  * Training models for malicious deepfake generation

  * Commercial applications without proper licensing consideration




## Dataset Structure#

The dataset contains 2,900 video samples with the following structure:

### Fields#

Each sample in the dataset contains:

  * **video** : Path to the video file (MP4 format, H.264 codec)

  * **question** : A natural language question about the video content

  * **answer** : A detailed, complete answer to the question

  * **short_answer** : A concise version of the answer

  * **answer_timestamp** : Temporal location in the video where the answer can be found (format: MM:SS.S)

  * **category** : Classification label indicating the type of question/task

  * **id** : Unique identifier for each sample




### Category Distribution#

The dataset includes 13 categories with the following distribution:

  * **object referencing** (706 samples): Questions about identifying or locating specific objects

  * **object attributes** (562 samples): Questions about properties of objects (color, size, shape, etc.)

  * **action detection** (440 samples): Questions about whether specific actions occurred

  * **object counting** (286 samples): Questions requiring counting objects in the video

  * **action counting** (224 samples): Questions requiring counting occurrences of actions

  * **object detection** (211 samples): Questions about the presence of objects

  * **action attributes** (155 samples): Questions about properties of actions

  * **action understanding** (110 samples): Questions requiring comprehension of actions

  * **object understanding** (79 samples): Questions requiring deeper object comprehension

  * **subjective** (43 samples): Questions requiring subjective judgment

  * **scene understanding** (38 samples): Questions about overall scene context

  * **audio-visual** (23 samples): Questions requiring both audio and visual information

  * **ocr** (23 samples): Questions requiring reading text in videos




### Video Format#

All videos are encoded in H.264 format, compatible with FiftyOne and standard video processing libraries.

## Dataset Creation#

### Curation Rationale#

The QIVD dataset was created to address the need for comprehensive video question-answering benchmarks that test various aspects of video understanding. The dataset was designed to evaluate models on:

  1. Temporal reasoning - understanding when events occur in videos

  2. Multi-category understanding - covering diverse types of visual reasoning tasks

  3. Fine-grained video comprehension - requiring attention to specific moments and details

  4. Practical video QA scenarios - reflecting real-world use cases




The inclusion of precise timestamps for answers enables evaluation of temporal grounding capabilities, while the diverse category distribution ensures comprehensive assessment of video understanding abilities.

### Source Data#

#### Data Collection and Processing#

The dataset consists of video clips collected from various sources and annotated with question-answer pairs. Each video was:

  1. Encoded in H.264 format for compatibility and efficient storage

  2. Annotated with questions spanning 13 different categories

  3. Labeled with precise timestamps indicating when answers can be found

  4. Provided with both detailed and short-form answers for flexibility




Quality control measures were implemented to ensure:

  * Temporal accuracy of timestamp annotations

  * Clarity and answerability of questions

  * Consistency in answer formatting

  * Balanced distribution across categories




#### Who are the source data producers?#

The dataset was produced by the Qualcomm AI Research team, with video content sourced from publicly available video datasets and annotated by trained annotators following detailed guidelines. The annotation process involved multiple rounds of review to ensure quality and consistency.

### Annotations#

#### Annotation process#

The annotation process involved:

  1. **Question Generation** : Annotators watched videos and created questions covering different aspects of video understanding

  2. **Answer Creation** : Both detailed and concise answers were provided for each question

  3. **Temporal Annotation** : Precise timestamps were marked indicating when the answer could be found in the video

  4. **Category Assignment** : Each question-answer pair was classified into one of 13 predefined categories

  5. **Quality Assurance** : Multiple rounds of review ensured consistency and accuracy




### Recommendations#

Users should:

  * Be aware of the category imbalance when training models and consider appropriate sampling strategies

  * Validate model performance on held-out test sets from different video sources

  * Consider the limited size of underrepresented categories when drawing conclusions about model capabilities

  * Use appropriate evaluation metrics that account for both answer accuracy and temporal grounding

  * Be cautious when deploying models trained on this dataset in production environments without additional validation

  * Consider combining this dataset with other video QA datasets for more robust training

  * Implement fairness checks to ensure models donât perpetuate biases present in the data




## Citation#

**BibTeX:**
    
    
    @misc{pourreza2025visionlanguagemodelsanswerface,
        title={Can Vision-Language Models Answer Face to Face Questions in the Real-World?},
        author={Reza Pourreza and Rishit Dagli and Apratim Bhattacharyya and Sunny Panchal and Guillaume Berger and Roland Memisevic},
        year={2025},
        eprint={2503.19356},
        archivePrefix={arXiv},
        primaryClass={cs.CV},
        url={https://arxiv.org/abs/2503.19356},
    }
    

**APA:**

Qualcomm AI Research Team. (2025). QIVD: Qualcomm Interactive Video Dataset for Video Question Answering. arXiv preprint arXiv:2503.19356.

## Dataset Card Contact#

For questions, issues, or contributions, please contact:

  * Qualcomm AI Research: ai-research@qualcomm.com

  * GitHub Issues: https://github.com/qualcomm/qivd-dataset/issues




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
