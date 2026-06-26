---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/imagenet_a.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ImageNet-A)

# Dataset Card for ImageNet-A#

![image](https://huggingface.co/datasets/Voxel51/ImageNet-A/resolve/main/ImageNet-A.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7450 samples.

The recipe notebook for creating this FiftyOne Dataset can be found [here](https://colab.research.google.com/drive/1GpM0AEr8YolZxVF5tp0L94YIuT1WP-I7?usp=sharing).

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/ImageNet-A")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

ImageNet-A is a dataset of adversarially filtered images that reliably fool current ImageNet classifiers.

It contains natural, unmodified real-world examples that transfer to various unseen ImageNet models, demonstrating that these models share weaknesses with adversarially selected images. These images cause consistent classification mistakes across various models.

To create ImageNet-A, the authors first downloaded numerous images related to an ImageNet class. They then deleted the images that fixed ResNet-50 classifiers correctly predicted.

With the remaining incorrectly classified images, the authors manually selected visually clear images.

The resulting ImageNet-A dataset has ~7,500 adversarially filtered images.

The ImageNet-A dataset enables testing image classification performance when the input data distribution shifts[1]. ImageNet-A can be used to measure model robustness to distribution shift using challenging natural images.

  * The images belong to 200 ImageNet classes selected to avoid overly fine-grained classes and classes with substantial overlap[1]. The classes span the most broad categories in ImageNet-1K.

  * To create ImageNet-A, the authors downloaded images related to the 200 classes from sources like iNaturalist, Flickr, and DuckDuckGo[1].

  * They then filtered out images that fixed ResNet-50 classifiers could correctly predict[1]. Images that fooled the classifiers were kept.

  * The authors manually selected visually clear, single-class images from the remaining incorrectly classified images to include in the final dataset[1].

  * The resulting dataset contains 7,500 natural, unmodified images that reliably transfer to and fool unseen models[1].




Citations: [1] https://ar5iv.labs.arxiv.org/html/1907.07174

  * **Curated by:** Jacob Steinhardt, Dawn Song

  * **Funded by:** UC Berkeley

  * **Shared by:** [Harpreet Sahota](https://twitter.com/DataScienceHarp), Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:** MIT




### Dataset Sources [optional]#

  * **Repository:** https://github.com/hendrycks/natural-adv-examples

  * **Paper:** https://ar5iv.labs.arxiv.org/html/1907.07174




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
