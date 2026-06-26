---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/mpii_human_pose_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/MPII_Human_Pose_Dataset)

# Dataset Card for MPII Human Pose#

MPII Human Pose dataset is a state of the art benchmark for evaluation of articulated human pose estimation.

The dataset includes around **25K images** containing over **40K people with annotated body joints**.

The images were systematically collected using an established **taxonomy of every day human activities**.

Overall the dataset covers **410 human activities** and each image is provided with an activity label.

Each image was extracted from a **YouTube video** and provided with preceding and following un-annotated frames.

In addition, for the test set, richer annotations were obtained including body part occlusions and 3D torso and head orientations.

Following the best practices for the performance evaluation benchmarks in the literature we withhold the test annotations to prevent overfitting and tuning on the test set. We are working on an automatic evaluation server and performance analysis tools based on rich test set annotations.

![image/png](https://huggingface.co/datasets/Voxel51/MPII_Human_Pose_Dataset/resolve/main/dataset_preview.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 24984 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/MPII_Human_Pose_Dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

> MPII Human Pose Dataset, Version 1.0 Copyright 2015 Max Planck Institute for Informatics Licensed under the Simplified BSD License Annotations and the corresponding are freely available for research purposes. Commercial use is not allowed due to the fact that the authors do not have the copyright for the images themselves.

  * **License:** bsd-2-clause




### Dataset Sources#

  * **Website:** http://human-pose.mpi-inf.mpg.de/#

  * **Paper:** http://human-pose.mpi-inf.mpg.de/contents/andriluka14cvpr.pdf




## Uses#

At the time when dataset was released **(2014)** , dataset was evaluated on 2 main tasks:

  * Multi-Person Pose Estimation

  * Single Person Pose Estimation




## Dataset Structure#
    
    
    Name:        MPII Human Pose
    Media type:  image
    Num samples: 24984
    Persistent:  True
    Tags:        ['version1', 'MPII Human Pose']
    Sample fields:
        id:           fiftyone.core.fields.ObjectIdField
        filepath:     fiftyone.core.fields.StringField
        tags:         fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        rectangle_id: fiftyone.core.fields.ListField(fiftyone.core.fields.IntField)
        activity:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Classifications)
        head_rect:    fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
        objpos:       fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
        scale:        fiftyone.core.fields.VectorField
        annopoints:   fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
        video_id:     fiftyone.core.fields.StringField
        frame_sec:    fiftyone.core.fields.IntField
    

## Dataset Creation#

### Source Data#

#### Data Collection and Processing#

See **Section 2. Dataset - Data collection paragraph** of this [paper](http://human-pose.mpi-inf.mpg.de/contents/andriluka14cvpr.pdf)

#### Who are the source data producers?#

[Source data producers](http://human-pose.mpi-inf.mpg.de/#contact)

### Annotations#

Annotation description

Annotations are stored in a matlab structure **RELEASE** having following fields
    
    
    .annolist(imgidx) - annotations for image imgidx
        .image.name - image filename
        .annorect(ridx) - body annotations for a person ridx
            .x1, .y1, .x2, .y2 - coordinates of the head rectangle
            .scale - person scale w.r.t. 200 px height
            .objpos - rough human position in the image
            .annopoints.point - person-centric body joint annotations
                .x, .y - coordinates of a joint
                id - joint id (0 - r ankle, 1 - r knee, 2 - r hip, 3 - l hip, 4 - l knee, 5 - l ankle, 6 - pelvis, 7 - thorax, 8 - upper neck, 9 - head top, 10 - r wrist, 11 - r elbow, 12 - r shoulder, 13 - l shoulder, 14 - l elbow, 15 - l wrist)
                is_visible - joint visibility
        .vidx - video index in video_list
        .frame_sec - image position in video, in seconds
    
    img_train(imgidx) - training/testing image assignment
    
    single_person(imgidx) - contains rectangle id ridx of sufficiently separated individuals
    
    act(imgidx) - activity/category label for image imgidx
        act_name - activity name
        cat_name - category name
        act_id - activity id
    
    video_list(videoidx) - specifies video id as is provided by YouTube. To watch video on youtube go to https://www.youtube.com/watch?v=video_list(videoidx)
    
    

#### Annotation process#

See **Section 2. Dataset - Data annotation paragraph** of this [paper](http://human-pose.mpi-inf.mpg.de/contents/andriluka14cvpr.pdf)

## Citation#

**BibTeX:**
    
    
    @inproceedings{andriluka14cvpr,
                   author = {Mykhaylo Andriluka and Leonid Pishchulin and Peter Gehler and Schiele, Bernt}
                   title = {2D Human Pose Estimation: New Benchmark and State of the Art Analysis},
                   booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
                   year = {2014},
                   month = {June}
    }
    

## More Information#

The following [**Github repo**](https://github.com/loloMD/51_contribution/tree/mpii_human_pose/mpii_human_pose) contains code to parse the raw data (in MATLAB format) and convert it into a FiftyOne Dataset

Dataset conversion and data card contributed by [Loic Mandine](https://lolomd.github.io/)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
