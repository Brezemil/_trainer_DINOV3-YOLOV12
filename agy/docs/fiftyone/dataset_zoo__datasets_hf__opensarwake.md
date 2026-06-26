---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/opensarwake.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/OpenSARWake)

# Dataset Card for OpenSARWake#

OpenSARWake is a benchmark dataset built for ship wake detection. This collection provides 3,973 images containing two polarization modes and 4,096 instances. Most importantly, it encompasses SAR images in the L-, C-, and X-bands, which have not been provided by previous datasets. The images in the dataset have spatial resolutions of 1.25 m to 12.5 m. The image size is 1024Ã 1024 pixels.

![preview](https://huggingface.co/datasets/Voxel51/OpenSARWake/resolve/main/./preview.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2383 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("dgural/OpenSARWake")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Sources#

  * **Repository:** https://github.com/libzzluo/OpenSARWake?tab=readme-ov-file




## Dataset Structure#

The dataset includes `ground_truth` field as well as clip embeddings for visualization

### Source Data#

[Google Drive Link](https://drive.google.com/file/d/14VkPYnb1BsmOvw_JTwtVFM-_qVpc4Udu/view?usp=sharing)

#### Who are the source data producers?#

Xu, Chengji and Wang, Xiaoqing

## Citation [optional]#

@ARTICLE{10507047, author={Xu, Chengji and Wang, Xiaoqing}, journal={IEEE Geoscience and Remote Sensing Letters}, title={OpenSARWake: A Large-Scale SAR Dataset for Ship Wake Recognition with a Feature Refinement Oriented Detector}, year={2024}, doi={10.1109/LGRS.2024.3392681}}

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
