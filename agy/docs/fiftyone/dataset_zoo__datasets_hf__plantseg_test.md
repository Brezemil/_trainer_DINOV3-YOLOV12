---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/plantseg_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/PlantSeg-Test)

# Dataset Card for PlantSeg_Test#

![image/png](https://huggingface.co/datasets/Voxel51/PlantSeg-Test/resolve/main/plantseg.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1200 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/PlantSeg-Test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card for PlantSeg#

## Dataset Details#

### Dataset Description#

PlantSeg is a large-scale in-the-wild dataset for plant disease segmentation, containing 11,458 images with high-quality segmentation masks across 115 disease categories and 34 plant types. Unlike existing plant disease datasets that are collected in controlled laboratory settings, PlantSeg primarily comprises real-world field images with complex backgrounds, various viewpoints, and different lighting conditions. The dataset also includes an additional 8,000 healthy plant images categorized by plant type.

  * **Curated by:** Tianqi Wei, Zhi Chen, Xin Yu, Scott Chapman, Paul Melloy, and Zi Huang

  * **Shared by:** The University of Queensland; CSIRO Agriculture and Food

  * **Language(s) (NLP):** en

  * **License:** CC BY-NC-ND 4.0




### Dataset Sources [optional]#

  * **Repository:** https://doi.org/10.5281/zenodo.13293891

  * **Paper [optional]:** arXiv:2409.04038




## Uses#

### Direct Use#

  * Training and benchmarking semantic segmentation models for plant disease detection

  * Developing automated disease diagnosis systems for precision agriculture

  * Image classification for plant disease identification

  * Evaluating segmentation algorithms on in-the-wild agricultural imagery

  * Supporting integrated disease management (IDM) decision-making tools




## Dataset Structure#

The dataset is organized as follows:

  * **images/** : Plant disease images in JPEG format

  * **annotations/** : Segmentation labels in PNG format (grayscale, where diseased pixels have class index values and background is zero)

  * **json/** : Original LabelMe annotation files in JSON format

  * **PlantSeg-Meta.csv** : Metadata file containing image name, plant type, disease type, resolution, label file path, mask ratio, source URL, and train/test split assignment




**Statistics:**

  * Total images: 11,458 diseased plant images + 8,000 healthy plant images

  * Disease categories: 115

  * Plant types: 34

  * Train/test split: 80/20 (stratified by disease type)




**Plant categories are organized into four socioeconomic groups:**

  * Profit crops (e.g., Coffee, Tobacco): 9 diseases across 3 plants

  * Staple crops (e.g., wheat, corn, potatoes)

  * Fruits (e.g., apples, oranges): 39 diseases across 10 plants

  * Vegetables (e.g., tomatoes): 45 diseases across 15 plants




## Dataset Creation#

### Curation Rationale#

Existing plant disease datasets are insufficient for developing robust segmentation models due to three key limitations:

  1. **Annotation Type:** Most datasets only contain class labels or bounding boxes, lacking pixel-level segmentation masks

  2. **Image Source:** Many datasets contain images from controlled laboratory settings with uniform backgrounds, which do not reflect real-world field conditions

  3. **Scale:** Existing segmentation datasets are small and cover limited host-pathogen relationships




PlantSeg addresses these gaps by providing the largest in-the-wild plant disease segmentation dataset with expert-validated annotations.

### Source Data#

#### Data Collection and Processing#

Images were collected using plant disease names as keywords from multiple internet sources:

  * Google Images

  * Bing Images

  * Baidu Images




This multi-source collection strategy ensured geographic diversity, with images sourced from websites worldwide. After collection, a rigorous data cleaning process was conducted where annotators reviewed each image and removed incorrect or ambiguous images, with cross-validation by at least two annotators and expert review for discrepancies.

#### Who are the source data producers?#

Images were sourced from websites globally, representing diverse geographic regions, environmental conditions, and imaging setups. The original photographers/sources are not individually identified, but source URLs are preserved in the metadata for reproducibility and copyright compliance.

### Annotations [optional]#

#### Annotation process#

  1. **Standard establishment:** A segmentation annotation standard was created to ensure consistent labeling of disease-affected areas

  2. **Annotator training:** Annotators were trained on the standard and required to annotate 10 test images for evaluation before proceeding

  3. **Annotation tool:** LabelMe (V5.5.0) was used for polygon annotation

  4. **Annotation guidelines:**

     * Distinct lesions: annotated with individual polygons

     * Overlapping lesions: annotated as combined affected areas

     * Small clustered symptoms (rust, powdery mildew): meticulously annotated to reflect disease distribution

     * Disease-induced deformities: also annotated

  5. **Quality control:** Each image subset was annotated by one annotator, then reviewed by another annotator, with final review by expert plant pathologists




#### Who are the annotators?#

  * 10 trained annotators who passed qualification evaluations

  * Supervised by two expert plant pathologists who established standards, evaluated annotator work, and performed final reviews




## Citation#

**BibTeX:**
    
    
    @article{wei2024plantseg,
      title={PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation},
      author={Wei, Tianqi and Chen, Zhi and Yu, Xin and Chapman, Scott and Melloy, Paul and Huang, Zi},
      journal={arXiv preprint arXiv:2409.04038},
      year={2024}
    }
    

**APA:** Wei, T., Chen, Z., Yu, X., Chapman, S., Melloy, P., & Huang, Z. (2024). PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation. arXiv preprint arXiv:2409.04038.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
