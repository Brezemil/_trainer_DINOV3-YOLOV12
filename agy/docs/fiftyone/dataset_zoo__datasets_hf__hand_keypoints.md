---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/hand_keypoints.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/hand-keypoints)

# Dataset Card for Image Hand Keypoint Detection#

![image/png](https://huggingface.co/datasets/Voxel51/hand-keypoints/resolve/main/hands-dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 846 samples.

**Note:** The images here are from the test set of the [original dataset](http://domedb.perception.cs.cmu.edu/panopticDB/hands/hand_labels.zip) and parsed into FiftyOne format.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("voxel51/hand-keypoints")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

As part of their research, the authors created a dataset by manually annotating two publicly available image sets: the MPII Human Pose dataset and images from the New Zealand Sign Language (NZSL) Exercises.

To date, they collected annotations for 1300 hands on the MPII set and 1500 on NZSL.

This combined dataset was split into a training set (2000 hands) and a testing set (800 hands)

### Dataset Description#

The dataset created in this research is a collection of manually annotated RGB images of hands sourced from the MPII Human Pose dataset and the New Zealand Sign Language (NZSL) Exercises.

It contains 2D locations for 21 keypoints on 2800 hands, split into a training set of 2000 hands and a testing set of 800 hands.

This dataset was used to train and evaluate their hand keypoint detection methods for single images.

  * **Paper:** https://arxiv.org/abs/1704.07809

  * **Demo:** http://domedb.perception.cs.cmu.edu/handdb.html

  * **Curated by:** Tomas Simon, Hanbyul Joo, Iain Matthews, Yaser Sheikh

  * **Funded by:** Carnegie Mellon University

  * **Shared by:** [Harpreet Sahota](https://huggingface.co/harpreetsahota), Hacker-in-Residence at Voxel51

  * **License:** This dataset contains images from:

    1. MPII Huaman Pose dataset, which is under the [BSD License](https://github.com/YuliangXiu/MobilePose/blob/master/pose_dataset/mpii/mpii_human_pose_v1_u12_2/bsd.txt)

    2. New Zealand Sign Language Dictionary Dataste, which is under the [CC BY-NC-SA 3.0 License](https://creativecommons.org/licenses/by-nc-sa/3.0/)




## Uses#

### Direct Use#

This manually annotated dataset was directly used to train and evaluate their hand keypoint detection methods.

The dataset serves as a benchmark to assess the accuracy of their single image 2D hand keypoint detector.

It enabled them to train an initial detector and evaluate the improvements gained through their proposed multiview bootstrapping technique.

The dataset contains images extracted from YouTube videos depicting everyday human activities (MPII) and images showing a variety of hand poses from people using New Zealand Sign Language (NZSL).

These diverse sets of images allowed the researchers to evaluate the generalization capabilities of their detector.

## Dataset Structure#
    
    
    Name:        hand_keypoints
    Media type:  image
    Num samples: 846
    Persistent:  True
    Tags:        []
    Sample fields:
        id:               fiftyone.core.fields.ObjectIdField
        filepath:         fiftyone.core.fields.StringField
        tags:             fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:         fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        created_at:       fiftyone.core.fields.DateTimeField
        last_modified_at: fiftyone.core.fields.DateTimeField
        right_hand:       fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
        body:             fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
        left_hand:        fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
    

### Dataset Sources#

#### Source Data#

[**MPII Human Pose dataset:**](https://github.com/YuliangXiu/MobilePose/blob/master/pose_dataset/mpii/mpii_human_pose_v1_u12_2/README.md) Contains images from YouTube videos depicting a wide range of everyday human activities. These images vary in quality, resolution, and hand appearance, and include various types of occlusions and hand-object/hand-hand interactions.

[ **New Zealand Sign Language (NZSL) Exercises:**](https://github.com/Bluebie/NZSL-Dictionary) Features images of people making visible hand gestures for communication. This subset provides a variety of hand poses commonly found in conversational contexts

#### Data Collection and Processing#

The dataset is composed of manually annotated RGB images of hands sourced from two existing datasets: MPII and NZSL.

â¢ **Annotations:** Each annotated image includes 2D locations for 21 keypoints on the hand (see Fig. 4a for an example). These keypoints represent different landmarks on the hand, such as finger tips and joints.

â¢ **Splits:** The combined dataset of 2800 annotated hands was divided into a training set of 2000 hands and a testing set of 800 hands. The criteria for this split are not explicitly detailed in the provided excerpts.

### Annotations#

#### Annotation process#

This manually annotated dataset was directly used to train and evaluate their hand keypoint detection methods.

The dataset serves as a benchmark to assess the accuracy of their single image 2D hand keypoint detector. It enabled them to train an initial detector and evaluate the improvements gained through their proposed multiview bootstrapping technique.

The dataset contains images extracted from YouTube videos depicting everyday human activities (MPII) and images showing a variety of hand poses from people using New Zealand Sign Language (NZSL).

These diverse sets of images allowed the researchers to evaluate the generalization capabilities of their detector.

The process of manually annotating hand keypoints in single images was challenging due to frequent occlusions caused by hand articulation, viewpoint, and grasped objects.

In many cases, annotators had to estimate the locations of occluded keypoints, potentially reducing the accuracy of these annotations

## Citation#
    
    
    @inproceedings{simon2017hand,
      author = {Tomas Simon and Hanbyul Joo and Iain Matthews and Yaser Sheikh},
      booktitle = {CVPR},
      title = {Hand Keypoint Detection in Single Images using Multiview Bootstrapping},
      year = {2017}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
