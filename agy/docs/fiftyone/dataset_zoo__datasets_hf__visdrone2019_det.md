---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/visdrone2019_det.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/VisDrone2019-DET)

# Dataset Card for VisDrone2019-DET#

![image/png](https://huggingface.co/datasets/Voxel51/VisDrone2019-DET/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) version of the VisDrone2019-DET dataset with 8629 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', 'persistent`, 'overwrite' etc
    dataset = fouh.load_from_hub("Voxel51/VisDrone2019-DET")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University, China

  * **Language(s) (NLP):** en

  * **License:** cc-by-sa-3.0




### Dataset Sources#

  * **Repository:** https://github.com/VisDrone/VisDrone-Dataset

  * **Paper:** [Detection and Tracking Meet Drones Challenge](https://arxiv.org/abs/2001.06303)




## Dataset Structure#
    
    
    Name:        VisDrone2019-DET
    Media type:  image
    Num samples: 8629
    Persistent:  False
    Tags:        []
    Sample fields:
        id:           fiftyone.core.fields.ObjectIdField
        filepath:     fiftyone.core.fields.StringField
        tags:         fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        ground_truth: fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
    

The dataset has 3 splits: âtrainâ, âvalâ, and âtestâ. Samples are tagged with their split.

## Dataset Creation#

Created by the AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University, China.

### Source Data#

#### Who are the source data producers?#

The VisDrone Dataset is a large-scale benchmark created by the AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University, China. It contains carefully annotated ground truth data for various computer vision tasks related to drone-based image and video analysis.

#### Personal and Sensitive Information#

The authors of the dataset have done their best to exclude identifiable information from the data to protect privacy. If you find your vehicle or personal information in this dataset, please contact them and they will remove the corresponding information from their dataset. They are not responsible for any actual or potential harm as the result of using this dataset.

## Citation#

**BibTeX:**
    
    
    @ARTICLE{9573394,
      author={Zhu, Pengfei and Wen, Longyin and Du, Dawei and Bian, Xiao and Fan, Heng and Hu, Qinghua and Ling, Haibin},
      journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
      title={Detection and Tracking Meet Drones Challenge},
      year={2021},
      volume={},
      number={},
      pages={1-1},
      doi={10.1109/TPAMI.2021.3119563}}
    

## Copyright Information#

The copyright of the [VisDrone dataset](https://github.com/VisDrone/VisDrone-Dataset) is reserved by the AISKYEYE team at Lab of Machine Learning and Data Mining, Tianjin University, China. The dataset described on this page is distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License, which implies that you must: (1) attribute the work as specified by the original authors; (2) may not use this work for commercial purposes ; (3) if you alter, transform, or build upon this work, you may distribute the resulting work only under the same license. The dataset is provided âas it isâ and we are not responsible for any subsequence from using this dataset.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
