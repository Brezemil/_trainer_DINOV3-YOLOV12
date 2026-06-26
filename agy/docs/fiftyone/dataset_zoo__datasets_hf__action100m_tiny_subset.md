---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/action100m_tiny_subset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/action100m_tiny_subset)

# Dataset Card for action100m#

![image/png](https://huggingface.co/datasets/Voxel51/action100m_tiny_subset/resolve/main/action100m.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1144 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/action100m_tiny_subset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card for Action100M Preview#

## Dataset Description#

This is a FiftyOne-formatted preview of Action100M, a large-scale video action dataset containing ~100 million temporally localized segments with open-vocabulary action supervision and rich captions.

The full dataset is constructed from 1.2 million Internet instructional videos (14.6 years of duration) sourced from HowTo100M.

### This preview contains 1,144 videos clipped to 90 seconds at 480p resolution.#

Each video is annotated with a hierarchical Tree-of-Captions structure produced by a fully automated three-stage pipeline: (1) hierarchical temporal segmentation using V-JEPA 2 embeddings, (2) multi-level caption generation using PerceptionLM-3B and Llama-3.2-Vision-11B, and (3) structured annotation extraction via GPT-OSS-120B with multi-round Self-Refine. The final annotations include brief and detailed action descriptions, actor identification, and brief and detailed video captions for each temporal segment.

  * **Curated by:** Delong Chen, Tejaswi Kasarla, Yejin Bang, Mustafa Shukor, Willy Chung, Jade Yu, Allen Bolourchi, ThÃ©o Moutakanni, Pascale Fung â Meta FAIR, HKUST, University of Amsterdam, Sorbonne UniversitÃ©

  * **Shared by:** Voxel51 (FiftyOne format conversion)

  * **Language(s) (NLP):** en

  * **License:** FAIR Noncommercial Research License (no commercial use, no redistribution)




## Dataset Sources#

  * **Repository:** https://github.com/facebookresearch/Action100M

  * **Original Dataset:** https://huggingface.co/datasets/facebook/action100m-preview

  * **Paper:** https://arxiv.org/abs/2601.10592




## Uses#

### Direct Use#

This preview is suitable for exploring the Action100M annotation structure, prototyping video understanding pipelines, and evaluating the hierarchical Tree-of-Captions annotation format. The full Action100M dataset is designed for training open-vocabulary video action recognizers, text-to-video retrieval models, and vision-language models for action-centric video understanding. Downstream applications include embodied AI, wearable assistive technology, action-conditioned world modeling, and procedural activity understanding.

### Out-of-Scope Use#

This preview subset (1,144 samples) is not sufficient for model training â the paperâs scaling results require millions of samples. Commercial use is prohibited under the FAIR Noncommercial Research License. The dataset is biased toward instructional and procedural content (cooking, DIY, home improvement) drawn from 12 WikiHow categories, and is not representative of all human activities. The source videos contain faces that have been blurred by Meta, but other personally identifiable information (voices, locations, usernames) may still be present.

## Dataset Structure#

Each sample in this FiftyOne format dataset is a video with the following fields:

**Video metadata:**

  * `title` (string): Original YouTube video title.

  * `description` (string): Original YouTube video description.

  * `full_video_url` (string): YouTube URL for the source video.

  * `upload_date` (datetime): Video upload date.

  * `view_count`, `like_count` (int): Engagement metrics.

  * `full_video_duration` (float): Duration of the original unclipped video in seconds.

  * `transcript` (string): Concatenated ASR transcript text.

  * `tree_depth` (int): Maximum hierarchy depth for this videoâs Tree-of-Captions.




**GPT-refined annotations (Stage 3)** â stored as `TemporalDetections`, each detection carrying `node_id`, `parent_id`, and `level` attributes for hierarchy reconstruction:

  * `gpt_summary_brief`: One-sentence concise caption per segment.

  * `gpt_summary_detailed`: Longer, comprehensive description per segment.

  * `gpt_action_brief`: Short verb phrase naming the action step (e.g., âstir mixtureâ, âpour batterâ). Segments with âN/Aâ actions (intros, ads, non-action content â ~3.23% of segments) are excluded.

  * `gpt_action_detailed`: Imperative-style instruction describing how the action is performed.

  * `gpt_action_actor`: Noun phrase identifying who or what performs the action.




**Transcript segments:**

  * `transcript_segments`: ASR transcript entries as temporal detections aligned to video time.




Annotations at different hierarchy levels overlap temporally â a parent nodeâs time span contains all of its childrenâs spans. The `level` attribute (0 = root/coarsest, higher = finer) and `parent_id` linkage allow filtering to a single granularity or reconstructing the full tree. Segments shorter than 4 seconds do not have GPT-refined annotations.

### Understanding the annotations:#

  * **gpt_summary_brief** â Whatâs happening in this clip, in one sentence. (âA woman spreads almonds on a parchment-lined tray.â)

  * **gpt_summary_detailed** â The full play-by-play of everything visible in the clip. (âThe presenter stands in a bright kitchen, pours raw almonds from a bag onto a parchment-lined baking tray, spreads them evenly with her hands, then slides the tray into a preheated oven.â)

  * **gpt_action_brief** â The verb phrase youâd use as a label. (âSpread almonds on trayâ)

  * **gpt_action_detailed** â The instruction manual version of that action. (âSpread raw almonds evenly across a parchment-lined baking tray using both hands.â)

  * **gpt_action_actor** â Whoâs doing it. (âA woman in a white apronâ)




## Dataset Creation#

### Curation Rationale#

Existing video action datasets are developed for narrow domains (e.g., cooking, toy assembly) and remain limited in scale (less than 1 million action instances). Action understanding lags behind object and scene recognition due to the absence of large-scale, open-vocabulary action data. Action100M was created to address this gap by providing dense, temporally localized action annotations at unprecedented scale to enable open-domain and open-vocabulary video action recognition, embodied learning, and physical world modeling.

### Source Data#

#### Data Collection and Processing#

Source videos are 1,199,096 face-blurred videos from HowTo100M, an instructional video dataset curated from 12 WikiHow categories (e.g., Food & Entertaining, Home & Garden, Hobbies & Crafts). ASR transcripts were successfully retrieved for 72% of these videos. Many original HowTo100M videos have become unavailable since the datasetâs release in June 2019.

For this FiftyOne preview, videos are clipped to the first 90 seconds and provided at 480p resolution. The preview represents approximately 10% of the full Action100M dataset by video count.

#### Who are the source data producers?#

YouTube content creators who uploaded instructional and how-to videos. The videos were originally collected by the HowTo100M project (Miech et al., 2019).

### Annotations#

#### Annotation process#

Annotations are fully automated with no manual labeling, produced through a three-stage pipeline:

**Stage 1 â Temporal Segmentation:** V-JEPA 2 (ViT-g-384) extracts dense per-frame visual embeddings. Hierarchical agglomerative clustering with Ward linkage and a local temporal connectivity constraint decomposes each video into a tree of contiguous, semantically coherent segments at multiple temporal scales. Segments shorter than 0.5 seconds are discarded.

**Stage 2 â Caption Generation (Tree-of-Captions):** Leaf nodes receive mid-frame captions from Llama-3.2-Vision-11B. Non-leaf nodes receive video-segment captions from PerceptionLM-3B processing 32 evenly sampled frames at 320Â² resolution. Both models are limited to 1024 generation tokens.

**Stage 3 â LLM Aggregation:** GPT-OSS-120B receives each nodeâs caption, its childrenâs captions in depth-first order, root-level captions, and video metadata (title, description, ASR transcript). It extracts five structured fields (brief/detailed summary, brief/detailed action, actor) through three rounds of Self-Refine. Segments shorter than 4 seconds are discarded at this stage.

The full pipeline consumed approximately 1.3 million V100 GPU hours for segmentation and captioning, and 0.3 million H100/H200 GPU hours for LLM aggregation, producing 147 million segment-level annotations totaling 21.3 billion English words.

#### Who are the annotators?#

All annotations are machine-generated by V-JEPA 2, PerceptionLM-3B, Llama-3.2-Vision-11B, and GPT-OSS-120B. No human annotators were involved.

#### Personal and Sensitive Information#

Source videos are face-blurred by Meta. However, other personally identifiable information may remain, including voices, speech content in ASR transcripts, YouTube usernames in video metadata, and identifiable locations or personal spaces visible in instructional videos.

## Bias, Risks, and Limitations#

The dataset is heavily biased toward instructional and procedural content. The most frequent action is âspeak to cameraâ (2.13M instances in the full dataset), and cooking-related actions dominate. Abstract categories such as Relationships or Finance were excluded from the WikiHow source categories. The action label distribution is severely long-tailed â 7.58 million duplicate action description groups account for 141.8 million duplicate instances. The dataset is English-only, reflecting the English-language bias of HowTo100M.

Approximately 3.23% of segments receive âN/Aâ action labels, corresponding to non-action content such as video introductions, advertisements, or subscription reminders. Stage 2 captions (from PerceptionLM-3B and Llama-3.2-Vision-11B) may contain hallucinations; the Stage 3 GPT-refined annotations are more reliable but not error-free.

### Recommendations#

Users should rely on the GPT-refined annotations (`gpt_*` fields) rather than raw Stage 2 outputs for downstream applications. The semantic resampling strategy described in the paper (Section 5.4) is recommended for training to mitigate long-tail action imbalance. Users should be aware that this preview subset is not representative of the full datasetâs scale and should not be used for drawing conclusions about model training dynamics.

## Citation#

**BibTeX:**
    
    
    @article{chen2026action100m,
      title={Action100M: A Large-scale Video Action Dataset},
      author={Chen, Delong and Kasarla, Tejaswi and Bang, Yejin and Shukor, Mustafa and Chung, Willy and Yu, Jade and Bolourchi, Allen and Moutakanni, Th{\'e}o and Fung, Pascale},
      journal={arXiv preprint arXiv:2601.10592},
      year={2026}
    }
    

**APA:** Chen, D., Kasarla, T., Bang, Y., Shukor, M., Chung, W., Yu, J., Bolourchi, A., Moutakanni, T., & Fung, P. (2026). Action100M: A Large-scale Video Action Dataset. _arXiv preprint arXiv:2601.10592_.

## More Information#

The full Action100M dataset contains 147 million annotated segments across 1.2 million videos. This preview contains 1,144 videos. Additional code for visualization and data loading is available at the GitHub repository.

The paper demonstrates that training VL-JEPA on Action100M yields consistent data-scaling improvements and strong zero-shot performance across eight action recognition benchmarks and eight text-to-video retrieval benchmarks, outperforming CLIP, SigLIP2, and Perception Encoder despite seeing significantly fewer training samples.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
