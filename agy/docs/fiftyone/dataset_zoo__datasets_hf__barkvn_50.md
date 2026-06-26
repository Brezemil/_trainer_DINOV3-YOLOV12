---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/barkvn_50.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/BarkVN-50)

# Dataset Card for BarkVN-50: Tree Species Identification from Bark Texture#

![image/png](https://huggingface.co/datasets/Voxel51/BarkVN-50/resolve/main/barkvn50.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5578 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/BarkVN-50")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

BarkVN-50 is a comprehensive tree bark texture classification dataset containing 5,678 images of 303Ã404 pixels across 50 different tree species. This dataset represents the maximum number of tree species considered for bark classification research at the time of its creation. The dataset was specifically designed for automated tree species identification using computer vision and deep learning techniques.

Bark texture provides a reliable characteristic for tree identification as it remains present despite seasonal variations, unlike leaves, fruits, or flowers. This makes the dataset particularly valuable for year-round forestry applications including forest conservation, disease diagnosis, and plant production.

  * **Curated by:** Truong Hoang, Vinh

  * **Original Dataset:** [BarkVN-50 on Mendeley Data](https://data.mendeley.com/datasets/gbt4tdmttn/1)

  * **Paper:** [Automated Identification of Tree Species by Bark Texture Classification Using Convolutional Neural Networks](https://arxiv.org/abs/2210.09290v1) by Sahil Faizal

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Repository:** https://data.mendeley.com/datasets/gbt4tdmttn/1

  * **Paper:** https://arxiv.org/abs/2210.09290v1

  * **DOI:** 10.17632/gbt4tdmttn.1




## Dataset Structure#

### Original Dataset#

The original BarkVN-50 dataset consists of:

  * **Total Images:** 5,678 (5,578 after processing)

  * **Image Dimensions:** 303Ã404 pixels (original), resized to 160Ã160 pixels for training

  * **Color Depth:** 24 bits/pixel

  * **Number of Classes:** 50 tree species

  * **Format:** Image classification directory tree structure




### FiftyOne Dataset Structure#

This dataset has been enhanced using FiftyOne with additional computed fields:

**Sample Fields:**

  * `id`: Unique sample identifier (ObjectIdField)

  * `filepath`: Path to the image file (StringField)

  * `tags`: Custom tags for organizing samples (ListField)

  * `metadata`: Image metadata including dimensions and size (ImageMetadata)

  * `created_at`: Timestamp of sample creation (DateTimeField)

  * `last_modified_at`: Timestamp of last modification (DateTimeField)

  * `ground_truth`: Original tree species label (Classification)

  * `radio_embeddings`: Feature embeddings from NVIDIA RADIO v3-h model (VectorField)

  * `radio_heatmap`: Spatial attention heatmaps from RADIO model (Heatmap)

  * `siglip2_predictions`: Zero-shot predictions from SigLIP2 model (Classification)

  * `eval_simple`: Evaluation results comparing predictions to ground truth (BooleanField)




### Data Splits#

The dataset is typically split as:

  * **Training set:** 80% of samples (approximately 4,462 images)

  * **Testing set:** 20% of samples (approximately 1,116 images)




K-Fold Cross Validation with k=5 has been used for robust performance evaluation.

## Dataset Creation#

### Curation Rationale#

This dataset was created to address the need for automated tree species identification in forestry applications. Traditional manual identification methods are:

  * Expensive and time-consuming

  * Require expert knowledge and years of experience

  * Inconsistent in accuracy (previous studies showed expert accuracy ranging from 56.6% to 77.8%)

  * Risky, requiring experts to venture into forested areas




The dataset focuses on bark texture because:

  1. Bark remains present throughout all seasons, unlike leaves, flowers, or fruits

  2. Bark provides characteristic identity through structural variations

  3. Bark texture is suitable for computer vision analysis

  4. Commercial and medicinal products are often derived from tree bark




With 50 tree species, this represents the largest bark classification dataset at the time of creation, addressing the lack of diverse, multi-class datasets in this domain.

### Source Data#

#### Data Collection and Processing#

The images in BarkVN-50 were collected and curated by Truong Hoang, Vinh. The dataset contains bark texture images from 50 different tree species.

**Processing steps include:**

  * Original images: 303Ã404 pixels, 24 bits/pixel color depth

  * Images stored in numpy arrays after resampling and preprocessing

  * For model training, images are typically resized to 160Ã160 pixels

  * Data augmentation techniques are commonly applied during training




**Enhanced Processing (FiftyOne version):**

  * Computed embeddings using NVIDIA RADIO v3-h model for similarity search and visualization

  * Generated spatial attention heatmaps to identify discriminative bark regions

  * Applied zero-shot classification using SigLIP2 model

  * Created UMAP visualizations for embedding space exploration




#### Who are the source data producers?#

The original dataset was curated by **Truong Hoang, Vinh** and published on Mendeley Data. The research paper utilizing this dataset was authored by **Sahil Faizal** from the School of Computer Science and Engineering at Vellore Institute of Technology, Chennai.

### Annotations#

#### Annotation process#

The dataset is organized in an image classification directory tree structure, where each subdirectory represents a tree species class. Images are labeled by their directory placement, with 50 distinct species classes.

**Enhanced Annotations (FiftyOne version):**

  * **Ground truth labels:** Original species classifications from directory structure

  * **RADIO embeddings:** 1024-dimensional feature vectors computed using NVIDIAâs RADIO v3-h model

  * **Attention heatmaps:** Spatial feature maps showing which bark regions are most discriminative

  * **SigLIP2 predictions:** Zero-shot classification predictions using the prompt âA picture of a tree bark from the species [species_name]â

  * **Evaluation metrics:** Binary correctness indicators comparing predictions to ground truth




#### Who are the annotators?#

The original species labels were assigned by the dataset curator, Truong Hoang, Vinh, presumably based on expert botanical knowledge. The enhanced annotations (embeddings, heatmaps, predictions) were computed algorithmically using pre-trained foundation models.

## Citation#

**Dataset Citation (BibTeX):**
    
    
    @data{gbt4tdmttn-1,
      author = {Truong Hoang, Vinh},
      title = {BarkVN-50},
      year = {2020},
      publisher = {Mendeley Data},
      version = {V1},
      doi = {10.17632/gbt4tdmttn.1},
      url = {https://data.mendeley.com/datasets/gbt4tdmttn/1}
    }
    

**Research Paper Citation (BibTeX):**
    
    
    @article{faizal2022automated,
      title={Automated Identification of Tree Species by Bark Texture Classification Using Convolutional Neural Networks},
      author={Faizal, Sahil},
      journal={arXiv preprint arXiv:2210.09290},
      year={2022},
      url={https://arxiv.org/abs/2210.09290v1}
    }
    

**APA:**

Truong Hoang, V. (2020). _BarkVN-50_ (Version 1) [Data set]. Mendeley Data. https://doi.org/10.17632/gbt4tdmttn.1

Faizal, S. (2022). Automated Identification of Tree Species by Bark Texture Classification Using Convolutional Neural Networks. _arXiv preprint arXiv:2210.09290_.

## Dataset Card Contact#

For questions about the original dataset, please refer to the [Mendeley Data repository](https://data.mendeley.com/datasets/gbt4tdmttn/1).

For questions about the research paper, contact: Sahil Faizal, Vellore Institute of Technology, Chennai.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
