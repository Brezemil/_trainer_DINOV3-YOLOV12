---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/larch_tree_damage.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Larch_Tree_Damage)

# Dataset Card for Forest Damages - Larch Casebearer#

![image/png](https://huggingface.co/datasets/Voxel51/Larch_Tree_Damage/resolve/main/larch_casebarer.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1536 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/Larch_Tree_Damage")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Forest Damages - Larch Casebearer#

## Dataset Details#

### Dataset Description#

The Forest Damages - Larch Casebearer dataset contains aerial drone imagery of forests in VÃ¤stergÃ¶tland, Sweden, captured to support AI-based detection and monitoring of tree damage caused by the larch casebearer moth (_Coleophora laricella_). The dataset was created as part of a project to help forest caretakers quickly identify pest threats and respond to prevent further forest damage.

The dataset consists of 1,543 high-resolution RGB images collected during two drone flight campaigns over five affected forest areas. Images are organized into 10 batches and contain approximately 101,878 bounding box annotations identifying individual trees. Trees are categorized by species (Larch or Other), and batches 1-5 additionally include damage severity annotations across four categories: Healthy (H), Light Damage (LD), High Damage (HD), and Other.

  * **Curated by:** Swedish Forest Agency (Skogsstyrelsen)

  * **Funded by:** Microsoft AI for Earth program (supporting partner)

  * **Shared by:** National Forest Data Lab (Skogsdatalabbet), LILA BC

  * **Language(s) (NLP):** N/A (image dataset)

  * **License:** Community Data License Agreement - Permissive (CDLA-Permissive)




### Dataset Sources#

  * **Repository:** [LILA BC](https://lila.science/datasets/forest-damages-larch-casebearer/)

  * **Download:** [Google Cloud Storage](https://storage.googleapis.com/public-datasets-lila/larch-casebearer/Data_Set_Larch_Casebearer.zip)

  * **Paper:** N/A

  * **Demo:** N/A




## Uses#

### Direct Use#

This dataset is suitable for:

  * Training and evaluating object detection models for individual tree detection from aerial/drone imagery

  * Developing tree species classification systems (Larch vs. Other)

  * Building damage assessment models to classify tree health status from aerial imagery

  * Research on automated forest health monitoring and pest damage detection

  * Benchmarking remote sensing approaches for forestry applications




### Out-of-Scope Use#

This dataset may not be suitable for:

  * Detection of forest damages from pests other than larch casebearer, as damage patterns may differ significantly

  * Application to forest types or geographic regions substantially different from Swedish larch stands

  * High-altitude satellite imagery analysis (dataset uses low-altitude drone imagery)

  * Real-time operational deployment without additional validation on local forest conditions




## Dataset Structure#

### Original Format#

The original dataset is structured into 10 batches with images and annotations in Pascal VOC XML format. All batches contain tree species labels (Larch, Other), while batches 1-5 also include damage severity labels (H, LD, HD, Other).

### FiftyOne Format#

The dataset has been parsed into FiftyOne format with the following structure:

Field | Type | Description  
---|---|---  
`id` | ObjectIdField | Unique sample identifier  
`filepath` | StringField | Path to the image file  
`tags` | ListField(StringField) | Sample-level tags  
`metadata` | ImageMetadata | Image dimensions, format, etc.  
`created_at` | DateTimeField | Sample creation timestamp  
`last_modified_at` | DateTimeField | Last modification timestamp  
`location` | Classification | Geographic location identifier  
`capture_date` | DateTimeField | Date the image was captured  
`ground_truth` | Detections | Original bounding box annotations with species and damage labels  
`visual_segmentation` | Detections | Instance segmentation masks (model-generated)  
`radio_embeddings` | VectorField | Dense image embeddings (model-generated)  
`radio_heatmap` | Heatmap | Spatial feature heatmaps (model-generated)  
  
**Statistics:**

  * Total samples: 1,536 images

  * Total tree annotations: ~101,878 bounding boxes

  * Annotations with damage labels: ~44,500 (batches 1-5)




**Label Classes:**

  * Species: `Larch`, `Other`

  * Damage (batches 1-5 only): `Healthy (H)`, `Light Damage (LD)`, `High Damage (HD)`, `Other`




## Dataset Creation#

### Curation Rationale#

The larch casebearer is an invasive moth species that has caused significant damage to larch stands in VÃ¤stergÃ¶tland, Sweden. The Swedish Forest Agency initiated this project to develop AI-powered tools for identifying, inventorying, mapping, and monitoring affected forest areas. The primary motivation was to enable forest caretakers to rapidly identify pest threats and take preventive action before damage spreads.

### Source Data#

#### Data Collection and Processing#

Images were captured using drones during two separate flight campaigns over five forest areas affected by larch casebearer in VÃ¤stergÃ¶tland, Sweden. The Swedish Forest Agency secured permits for dissemination of geographical data from LantmÃ¤teriet (Swedish Land Survey).

#### Who are the source data producers?#

The drone imagery was collected by the Swedish Forest Agency as part of their forest monitoring program.

### Annotations#

#### Annotation process#

Annotations were created manually, with each tree marked using a bounding box and labeled with tree type (Larch or Other). A subset of annotations (batches 1-5) also includes damage severity classifications. Annotations are provided in Pascal VOC XML format.

#### Who are the annotators?#

Annotations were created by personnel at the Swedish Forest Agency.

## Citation#

**BibTeX:**
    
    
    @dataset{swedish_forest_agency_2021,
      author       = {{Swedish Forest Agency}},
      title        = {{Forest Damages â Larch Casebearer 1.0}},
      year         = {2021},
      publisher    = {National Forest Data Lab},
      url          = {https://lila.science/datasets/forest-damages-larch-casebearer/}
    }
    

**APA:** Swedish Forest Agency. (2021). _Forest Damages â Larch Casebearer 1.0_ [Dataset]. National Forest Data Lab. https://lila.science/datasets/forest-damages-larch-casebearer/

## Dataset Card Contact#

  * **Original Dataset Contact:** Halil Radogoshi, Swedish Forest Agency (halil.radogoshi@skogsstyrelsen.se)

  * **LILA BC:** https://lila.science/




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
