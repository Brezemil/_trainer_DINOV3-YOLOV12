---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/total_text_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Total-Text-Dataset)

# Dataset Card for Total-Text-Dataset#

The Total-Text consists of 1555 images with more than 3 different text orientations: Horizontal, Multi-Oriented, and Curved

![image/png](https://huggingface.co/datasets/Voxel51/Total-Text-Dataset/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1555 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Total-Text-Dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by :** Chee-Kheng Châng, Chee Seng Chan, Cheng-Lin Liu

  * **Funded by :** Fundamental Research Grant Scheme (FRGS) MoHE (Grant No. FP004-2016) and Postgraduate Research Grant (PPP) (Grant No. PG350-2016A).

  * **Language(s) (NLP):** en

  * **License:** bsd-3-clause




### Dataset Sources#

  * **Repository :** https://github.com/cs-chan/Total-Text-Dataset

  * **Paper :** https://arxiv.org/abs/1710.10400




## Uses#

  * curved text detection problems




## Dataset Structure#
    
    
    Name:        Total-Text-Dataset
    Media type:  image
    Num samples: 1555
    Persistent:  False
    Tags:        []
    Sample fields:
        id:                     fiftyone.core.fields.ObjectIdField
        filepath:               fiftyone.core.fields.StringField
        tags:                   fiftyone.core.fields.ListField(fiftyone.core.fields.StringField)
        metadata:               fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.metadata.ImageMetadata)
        ground_truth_polylines: fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Polylines)
        ground_truth:           fiftyone.core.fields.EmbeddedDocumentField(fiftyone.core.labels.Detections)
    

The dataset has 2 splits: âTrainâ and âTestâ. Samples are tagged with their split.

## Dataset Creation#

### Curation Rationale#

At present, text orientation is not diverse enough in the existing scene text datasets. Specifically, curve-orientated text is largely out-numbered by horizontal and multi-oriented text, hence, it has received minimal attention from the community so far. Motivated by this phenomenon, the authors collected a new scene text dataset, Total-Text, which emphasized on text orientations diversity. It is the first relatively large scale scene text dataset that features three different text orientations: horizontal, multioriented, and curve-oriented.

#### Annotation process#

Initial version of Total-Textâs polygon annotation was carried out with the mindset of covering text instances tightly with the least amount of vertices. As a result, the uncontrolled length of polygon vertices is not practical to train a regression network. The authors refined the Total-Text annotation using the following scheme. Apart from setting the number of polygon vertices to 10 (empirically, 10 vertices are found to be sufficient in covering all the word-level text instances tightly in our dataset), they used a guidance concept inspired by Curved scene text detection via transverse and longitudinal sequence connection paper by Liu, et al. which was introduced to remove human annotatorsâ bias and in turn producing a more consistent ground truth. The process for other annotations can be referred from paper.

The authors have mentioned in the paper that the human annotator was given the freedom to take a break whenever he feels like to, ensuring that he will not suffer from fatigue which in turn introduces bias to the experiment. Both time and annotation quality were measured internally (within the script) and individually to each image.

The authors have also proposed aided scene text detection annotation tool, T3, could help in providing a better scene text dataset in terms of quality and scale.

#### Who are the annotators?#

Chee-Kheng Châng, Chee Seng Chan, Cheng-Lin Liu and Chun Chet Ng

## Citation#

**BibTeX:**
    
    
    @article{CK2019,
      author    = {Chee Kheng Châng and
                   Chee Seng Chan and
                   Chenglin Liu},
      title     = {Total-Text: Towards Orientation Robustness in Scene Text Detection},
      journal   = {International Journal on Document Analysis and Recognition (IJDAR)},
      volume    = {23},
      pages     = {31-52},
      year      = {2020},
      doi       = {10.1007/s10032-019-00334-z},
    }
    

## Dataset Card Authors#

[Kishan Savant](https://huggingface.co/NeoKish)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
