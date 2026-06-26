---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/afo_aerial_floating_objects.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/AFO-Aerial_Floating_Objects)

# Dataset Card for AFO - Aerial Floating Objects#

AFO dataset is the first free dataset for training machine learning and deep learning models for maritime Search and Rescue applications. It contains aerial-drone videos with 40,000 hand-annotated persons and objects floating in the water, many of small size, which makes them difficult to detect.

![preview](https://huggingface.co/datasets/Voxel51/AFO-Aerial_Floating_Objects/resolve/main/./preview.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1014 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("dgural/AFO-Aerial_Floating_Objects")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The AFO dataset contains images taken from fifty video clips containing objects floating on the water surface, captured by the various drone-mounted cameras (from 1280x720 to 3840x2160 resolutions), which have been used to create AFO. From these videos, we have extracted and manually annotated 3647 images that contain 39991 objects. These have been then split into three parts: the training (67,4% of objects), the test (19,12% of objects), and the validation set (13,48% of objects). In order to prevent overfitting of the model to the given data, the test set contains selected frames from nine videos that were not used in either the training or validation sets. Dataset is prepared in Darknet YOLO format -> https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects

  * **Funded by [optional]:** Polish National Science Center

  * **Language(s) (NLP):** en

  * **License:** Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License




### Dataset Sources#

  * **Repository:** https://www.kaggle.com/datasets/jangsienicajzkowy/afo-aerial-dataset-of-floating-objects

  * **Paper:** An ensemble deep learning method with optimized weights for drone-based water rescue and surveillance




## Uses#

The datasets provided on this page are published under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License. This means that you must attribute the work in the manner specified by the authors, you may not use this work for commercial purposes and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license. If you are interested in commercial usage you can contact authors for further options.

## Dataset Structure#

Ground_truth field plus clip embeddings are included!

## Citation#

**BibTeX:**

@article{article, author = {GÄ sienica-JÃ³zkowy, Jan and Knapik, Mateusz and Cyganek, Boguslaw}, year = {2021}, month = {01}, pages = {1-15}, title = {An ensemble deep learning method with optimized weights for drone-based water rescue and surveillance}, journal = {Integrated Computer-Aided Engineering}, doi = {10.3233/ICA-210649} }

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
