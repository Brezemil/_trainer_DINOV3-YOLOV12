---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/pidray.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/PIDray)

# Dataset Card for pidray#

PIDray is a large-scale dataset which covers various cases in real-world scenarios for prohibited item detection, especially for deliberately hidden items. The dataset contains 12 categories of prohibited items in 47, 677 X-ray images with high-quality annotated segmentation masks and bounding boxes.

![image/png](https://huggingface.co/datasets/Voxel51/PIDray/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 9482 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("voxel51/PIDray")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

From _Towards Real-World Prohibited Item Detection: A Large-Scale X-ray Benchmark_ : Automatic security inspection using computer vision technology is a challenging task in real-world scenarios due to various factors, including intra-class variance, class imbalance, and occlusion. Most of the previous methods rarely solve the cases that the prohibited items are deliberately hidden in messy objects due to the lack of large-scale datasets, restricted their applications in real-world scenarios. Towards real-world prohibited item detection, we collect a large-scale dataset, named as PIDray, which covers various cases in real-world scenarios for prohibited item detection, especially for deliberately hidden items. With an intensive amount of effort, our dataset contains categories of prohibited items in X-ray images with high-quality annotated segmentation masks and bounding boxes. To the best of our knowledge, it is the largest prohibited items detection dataset to date. Meanwhile, we design the selective dense attention network (SDANet) to construct a strong baseline, which consists of the dense attention module and the dependency refinement module. The dense attention module formed by the spatial and channel-wise dense attentions, is designed to learn the discriminative features to boost the performance. The dependency refinement module is used to exploit the dependencies of multi-scale features. Extensive experiments conducted on the collected PIDray dataset demonstrate that the proposed method performs favorably against the state-of-the-art methods, especially for detecting the deliberately hidden items.

  * **Language(s) (NLP):** en

  * **License:** apache-2.0 The images and the corresponding annotations in PIDray Dataset can be used ONLY for academic purposes, NOT for commercial purposes.




Copyright Â© 2021 Institute of Software Chinese Academy of Sciences, University of Chinese Academy of Sciences

All rights reserved.

### Dataset Sources#

  * **Repository:** https://github.com/bywang2018/security-dataset

  * **Paper [optional]:** https://arxiv.org/abs/2108.07020




## Uses#

This used for academic research on airport security screening machines and the detection of objects being scanned.

### Out-of-Scope Use#

Any non-academic work is out of scope and prohibited.

## Citation#

@inproceedings{wang2021towards, title={Towards Real-World Prohibited Item Detection: A Large-Scale X-ray Benchmark}, author={Wang, Boying and Zhang, Libo and Wen, Longyin and Liu, Xianglong and Wu, Yanjun}, booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision}, pages={5412â5421}, year={2021} }

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
