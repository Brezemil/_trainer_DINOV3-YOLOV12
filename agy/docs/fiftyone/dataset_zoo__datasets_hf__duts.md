---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/duts.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/DUTS)

# Dataset Card for DUTS#

![image/png](https://huggingface.co/datasets/Voxel51/DUTS/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 15572 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/DUTS")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

DUTS is a saliency detection dataset containing 10,553 training images and 5,019 test images. All training images are collected from the ImageNet DET training/val sets, while test images are collected from the ImageNet DET test set and the SUN data set. Both the training and test set contain very challenging scenarios for saliency detection. Accurate pixel-level ground truths are manually annotated by 50 subjects.

  * **Curated by:** Lijun Wang, Huchuan Lu, Yifan Wang, Mengyang Feng, Dong Wang, Baocai Yin, and Xiang Ruan

  * **Language(s) (NLP):** en

  * **License:** unknown




## Dataset Structure#
    
    
    Name:        DUTS
    Media type:  image
    Num samples: 15572
    Persistent:  False
    Tags:        []
    Sample fields:
        id:           fiftyone.core.fields.ObjectIdField
        filepath:     fiftyone.core.fields.StringField
        tags:         fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        ground_truth: fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Segmentation)
    

The dataset has 2 splits: âtrainâ and âtestâ. Samples are tagged with their split.

## Dataset Creation#

Introduced by Wang et al. in [Learning to Detect Salient Objects With Image-Level Supervision](https://paperswithcode.com/paper/learning-to-detect-salient-objects-with-image)

## Citation#

**BibTeX:**
    
    
    @inproceedings{wang2017,
    title={Learning to Detect Salient Objects with Image-level Supervision},
    author={Wang, Lijun and Lu, Huchuan and Wang, Yifan and Feng, Mengyang 
    and Wang, Dong, and Yin, Baocai and Ruan, Xiang}, 
    booktitle={CVPR},
    year={2017}
    }
    

## Dataset Card Authors#

Dataset conversion and data card contributed by [Rohith Raj Srinivasan](https://huggingface.co/rohis).

## Dataset Card Contact#

[Rohith Raj Srinivasan](https://huggingface.co/rohis)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
