---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/colorswap.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ColorSwap)

# Dataset Card for colorswap#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2000 samples.

![image](https://huggingface.co/datasets/Voxel51/ColorSwap/resolve/main/colorswap.gif)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'split', 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/ColorSwap")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The ColorSwap dataset was designed to evaluate and improve the ability of multimodal models to match objects with their colors. It contains 2,000 unique image-caption pairs, grouped into 1,000 examples. Each example includes a caption-image pair and a âcolor-swappedâ pair, following the Winoground schema where the two captions have the same words but with color words rearranged to modify different objects[1].

The dataset was created using a combination of automated caption and image generation, along with human input to ensure naturalness and accuracy[1]. Various diffusion models like Stable Diffusion, Midjourney, and DALLE 3 were used for image generation[1].

Evaluations of image-text matching (ITM) and visual language models (VLMs) on ColorSwap reveal that even state-of-the-art models struggle with this task[1]. Contrastive ITM models like CLIP and SigLIP perform close to chance, while the non-contrastive BLIP ITM model is stronger. VLMs like GPT-4V and LLaVA also make genuine errors on this simple task.

However, fine-tuning these models on fewer than 2,000 examples from the ColorSwap training set yields significant performance gains on this out-of-distribution word-order understanding task[1]. After fine-tuning, CLIP and BLIP show substantial improvements across all metrics.

The ColorSwap dataset provides a targeted benchmark for evaluating and improving the compositional color comprehension abilities of multimodal models, revealing current limitations and the potential for improvement through fine-tuning on a small set of naturalistic data.

The samples in this FiftyOne dataset have been ungrouped, such that there is one sample per prompt.

Citations: [1] https://arxiv.org/html/2402.04492v1

  * **Curated by:** Jirayu Burapacheep, Ishan Gaur, Agam Bhatia, Tristan Thrush

  * **Funded by:** Stanford University

  * **Shared by:** [Harpreet Sahota](https://twitter.com/DataScienceHarp), Hacker-in-Residence @ Voxel51

  * **Language(s) (NLP):** en

  * **License:** MIT




### Dataset Sources [optional]#

  * **Repository:** https://huggingface.co/datasets/stanfordnlp/colorswap

  * **Paper:** https://arxiv.org/html/2402.04492v1




## Citation#

**BibTeX:**
    
    
    @article{burapacheep2024colorswap,
        author    = {Jirayu Burapacheep and Ishan Gaur and Agam Bhatia and Tristan Thrush},
        title     = {ColorSwap: A Color and Word Order Dataset for Multimodal Evaluation},
        journal   = {arXiv},
        year      = {2024},
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
