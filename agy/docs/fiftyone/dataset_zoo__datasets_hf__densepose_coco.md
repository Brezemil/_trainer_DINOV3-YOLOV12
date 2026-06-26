---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/densepose_coco.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/DensePose-COCO)

# Dataset Card for DensePose-COCO#

DensePose-COCO is a large-scale ground-truth dataset with image-to-surface correspondences manually annotated on COCO images.

![image/png](https://huggingface.co/datasets/Voxel51/DensePose-COCO/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 33929 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/DensePose-COCO")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** RÄ±za Alp GÃ¼ler, Natalia Neverova, Iasonas Kokkinos

  * **Language(s) (NLP):** en

  * **License:** cc-by-nc-2.0




### Dataset Sources#

  * **Repository:** https://github.com/facebookresearch/Densepose

  * **Paper :** https://arxiv.org/abs/1802.00434

  * **Homepage:** http://densepose.org/




## Uses#

Dense human pose estimation

## Dataset Structure#
    
    
    Name:        DensePoseCOCO
    Media type:  image
    Num samples: 33929
    Persistent:  False
    Tags:        []
    Sample fields:
        id:            fiftyone.core.fields.ObjectIdField
        filepath:      fiftyone.core.fields.StringField
        tags:          fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:      fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        detections:    fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
        segmentations: fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
        keypoints:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Keypoints)
    

The dataset has 2 splits: âtrainâ and âvalâ. Samples are tagged with their split.

## Dataset Creation#

### Curation Rationale#

Please refer the homepage and the paper for the curation rationale.

#### Annotation process#

Please refer the github repo for the annotation process.

## Citation#

**BibTeX:**
    
    
      @InProceedings{Guler2018DensePose,
      title={DensePose: Dense Human Pose Estimation In The Wild},
      author={R\{i}za Alp G\"uler, Natalia Neverova, Iasonas Kokkinos},
      journal={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
      year={2018}
      }
    

## Dataset Card Authors#

[Kishan Savant](https://huggingface.co/NeoKish)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
