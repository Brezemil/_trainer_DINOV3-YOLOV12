---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/usps.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/USPS)

# Dataset Card for usps#

![image/png](https://huggingface.co/datasets/Voxel51/USPS/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 9298 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/USPS")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** Introduced by Jonathan J. Hull in [A Database for Handwritten Text Recognition Research](https://ieeexplore.ieee.org/document/291440) and available at <https://paperswithcode.com/dataset/usps>.

  * **Language(s) (NLP):** en

  * **License:** unknown




### Dataset Sources [optional]#

  * **Repository:** https://paperswithcode.com/dataset/usps

  * **Paper:** [A Database for Handwritten Text Recognition Research](https://ieeexplore.ieee.org/document/291440)




## Dataset Structure#
    
    
    Name:        usps
    Media type:  image
    Num samples: 9298
    Persistent:  False
    Tags:        []
    Sample fields:
        id:           fiftyone.core.fields.ObjectIdField
        filepath:     fiftyone.core.fields.StringField
        tags:         fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:     fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        ground_truth: fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Classification)
    

The dataset has 2 splits: âtrainâ and âtestâ. Samples are tagged with their split.

## Dataset Creation#

Introduced by Jonathan J. Hull in [A Database for Handwritten Text Recognition Research](https://ieeexplore.ieee.org/document/291440)

## Citation#

**BibTeX:**
    
    
    @ARTICLE{291440,
      author={Hull, J.J.},
      journal={IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
      title={A database for handwritten text recognition research}, 
      year={1994},
      volume={16},
      number={5},
      pages={550-554},
      keywords={Text recognition;Image databases;Testing;Cities and towns;Handwriting recognition;Gray-scale;Performance analysis;Writing;Digital images;Postal services},
      doi={10.1109/34.291440}}
    

## More Information#

Dataset conversion and data card contributed by [Rohith Raj Srinivasan](https://huggingface.co/rohis).

## Dataset Card Authors#

[Rohith Raj Srinivasan](https://huggingface.co/rohis)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
