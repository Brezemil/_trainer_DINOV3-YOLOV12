---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/imagenet_o.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ImageNet-O)

# Dataset Card for ImageNet-O#

![image](https://huggingface.co/datasets/Voxel51/ImageNet-O/resolve/main/ImageNet-O.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2000 samples.

The recipe notebook for creating this dataset can be found [here](https://colab.research.google.com/drive/1ScN-30Q-1ssAwuQYIbZ453h0vo0SAhz8).

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/ImageNet-O")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The ImageNet-O dataset consists of images from classes not found in the standard ImageNet-1k dataset. It tests the robustness and out-of-distribution detection capabilities of computer vision models trained on ImageNet-1k.

Key points about ImageNet-O:

  * Contains images from classes distinct from the 1,000 classes in ImageNet-1k

  * Enables testing model performance on out-of-distribution samples, i.e. images that are semantically different from the training data

  * Commonly used to evaluate out-of-distribution detection methods for models trained on ImageNet

  * Reported using the Area Under the Precision-Recall curve (AUPR) metric

  * Manually annotated, naturally diverse class distribution, and large scale

  * **Curated by:** Dan Hendrycks, Kevin Zhao, Steven Basart, Jacob Steinhardt, Dawn Song

  * **Shared by:** Harpreet Sahota, Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:** [MIT License](https://github.com/hendrycks/natural-adv-examples/blob/master/LICENSE)




### Dataset Sources [optional]#

  * **Repository:** https://github.com/hendrycks/natural-adv-examples

  * **Paper:** https://arxiv.org/abs/1907.07174




## Citation#

**BibTeX:**
    
    
    @article{hendrycks2021nae,
      title={Natural Adversarial Examples},
      author={Dan Hendrycks and Kevin Zhao and Steven Basart and Jacob Steinhardt and Dawn Song},
      journal={CVPR},
      year={2021}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
