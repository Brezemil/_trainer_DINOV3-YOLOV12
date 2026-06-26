---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/iam_handwriting_finevision.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/iam_handwriting_finevision)

# Dataset Card for finevision_iam#

![image/png](https://huggingface.co/datasets/Voxel51/iam_handwriting_finevision/resolve/main/iam_handwriting.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5663 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/iam_handwriting_finevision")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is a subset of the [FineVision](https://huggingface.co/spaces/HuggingFaceM4/FineVision) dataset, derived from the [IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database). It contains images of handwritten English text paired with question-answer style annotations for OCR and vision-language model training.

The IAM Handwriting Database contains forms of unconstrained handwritten English text, scanned at 300dpi and saved as grayscale PNG images. The original database was created using sentences from the LOB (Lancaster-Oslo/Bergen) Corpus of British English.

  * **Curated by:** Original IAM database by U. Marti and H. Bunke (University of Bern); FineVision subset by HuggingFaceM4

  * **Shared by [optional]:** HuggingFaceM4

  * **Language(s) (NLP):** English

  * **License:** The original IAM Handwriting Database may be used for non-commercial research purposes only




### Dataset Sources#

  * **Original Database:** [IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)

  * **FineVision Source:** [HuggingFaceM4/FineVision](https://huggingface.co/spaces/HuggingFaceM4/FineVision)

  * **Paper:** U. Marti and H. Bunke. The IAM-database: An English Sentence Database for Off-line Handwriting Recognition. Int. Journal on Document Analysis and Recognition, Volume 5, pages 39-46, 2002.




## Uses#

### Direct Use#

  * Training and evaluating handwritten text recognition (HTR) systems

  * Fine-tuning vision-language models (VLMs) for OCR tasks

  * Training models to transcribe handwritten English text from images




### Out-of-Scope Use#

  * Commercial applications (prohibited by original IAM database license)

  * Writer identification or verification without appropriate consent considerations




## Dataset Structure#

This subset contains **1,888 samples** with the following fields:

Field | Type | Description  
---|---|---  
`filepath` | string | Path to the handwritten text image (PNG format)  
`user` | string | A question prompt asking about the handwriting content  
`assistant` | string | The transcription of the handwritten text  
  
Example:

  * **user** : âWhat does the handwriting in this picture say?â

  * **assistant** : âA MOVE to stop Mr. Gaitskell from nominating any more Labour life Peers is to be made at a meeting of Labour MPs tomorrow.â




## Dataset Creation#

### Curation Rationale#

This dataset was created to provide a FiftyOne-compatible format of handwriting OCR data for training and evaluating vision-language models on handwritten text recognition tasks.

### Source Data#

#### Data Collection and Processing#

The original IAM Handwriting Database was collected by scanning handwritten forms at 300dpi resolution and saving them as grayscale PNG images. The text content was sourced from the LOB (Lancaster-Oslo/Bergen) Corpus of British English.

This subset was obtained from the FineVision dataset (HuggingFaceM4), which reformatted the data into a question-answer format suitable for VLM fine-tuning.

#### Who are the source data producers?#

The original handwriting samples in the IAM database were contributed by 657 writers. The text content originates from the LOB Corpus.

### Annotations#

#### Annotation process#

The original IAM database used automatic segmentation with manual verification for word extraction. The question-answer format annotations in FineVision were added to convert the transcriptions into a conversational VLM training format.

#### Who are the annotators?#

Original transcription annotations were created as part of the IAM Handwriting Database project at the University of Bern.

#### Personal and Sensitive Information#

The text content is sourced from the LOB Corpus (published news and written English). The handwriting samples were contributed by volunteer writers for research purposes.

## Bias, Risks, and Limitations#

  * The dataset contains only English handwriting samples

  * Writers were primarily from an academic/research context, which may not represent the full diversity of handwriting styles

  * The text content is from British English sources (LOB Corpus), which may have regional language patterns




### Recommendations#

  * Users should verify the license terms of the original IAM Handwriting Database before use

  * This dataset is intended for non-commercial research purposes only

  * Models trained on this data may not generalize well to handwriting styles or languages not represented in the dataset




## Citation#

If you use this dataset, please cite the original IAM Handwriting Database paper:

**BibTeX:**
    
    
    @article{marti2002iam,
      title={The IAM-database: An English Sentence Database for Off-line Handwriting Recognition},
      author={Marti, U. and Bunke, H.},
      journal={International Journal on Document Analysis and Recognition},
      volume={5},
      pages={39--46},
      year={2002}
    }
    

**APA:**

Marti, U., & Bunke, H. (2002). The IAM-database: An English Sentence Database for Off-line Handwriting Recognition. _International Journal on Document Analysis and Recognition_ , 5, 39-46.

## More Information#

  * [IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database)

  * [FineVision Space](https://huggingface.co/spaces/HuggingFaceM4/FineVision)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
