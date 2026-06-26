---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/parkseg12k_train.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/parkseg12k_train)

# **Dataset Card for ParkSeg12k: Parking Lot Segmentation Dataset**#

![image/png](https://huggingface.co/datasets/Voxel51/parkseg12k_train/resolve/main/parkseg12k-mq.gif)

This is a **FiftyOne** dataset with 11,355 samples from the ParkSeg12k dataset, enhanced with NDVI calculations for parking lot segmentation.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/parkseg12k_train")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** UTEL-UIUC (Urban Traffic & Economics Lab, University of Illinois at Urbana-Champaign)

  * **Enhanced by:** Harpreet Sahota (FiftyOne conversion and NDVI calculations)

  * **Language(s) (NLP):** en

  * **License:** See original dataset for license information




### Dataset Sources#

  * **Original Dataset:** https://huggingface.co/datasets/UTEL-UIUC/parkseg12k

  * **Paper:** [A Pipeline and NIR-Enhanced Dataset for Parking Lot Segmentation](https://arxiv.org/pdf/2412.13179)

  * **GitHub Repository:** https://github.com/UTEL-UIUC/ParkSeg12k




## Uses#

### Direct Use#

  * Training semantic segmentation models for parking lot detection

  * Urban planning and policy analysis

  * Analyzing land use patterns in US cities

  * Supporting parking reform policy discussions




### Out-of-Scope Use#

  * This dataset is specific to US cities and may not generalize to other countries

  * Not suitable for real-time parking occupancy detection (detects lot boundaries, not individual spaces)




## Dataset Structure#

### FiftyOne Fields#

Each sample contains:

  * **filepath** : Path to RGB image (512x512 pixels, 30 cm/pixel resolution)

  * **segmentation** : Binary segmentation mask for parking lots (0=background, 1=parking)

  * **nir** : Near-infrared channel as heatmap (upsampled from NAIP imagery)

  * **ndvi** : Normalized Difference Vegetation Index heatmap (range: -1 to 1)

  * **ndvi_mean** : Mean NDVI value for the image

  * **ndvi_std** : Standard deviation of NDVI values

  * **ndvi_min** : Minimum NDVI value

  * **ndvi_max** : Maximum NDVI value




### NDVI Calculation#

NDVI was computed using: `(NIR - Red) / (NIR + Red)`

  * Values near 1: Dense vegetation

  * Values near 0: Bare soil/pavement

  * Negative values: Water bodies




This helps identify parking lot boundaries since many are surrounded by grass/vegetation.

## Dataset Creation#

### Curation Rationale#

Created to automate parking lot detection for urban planning discussions around minimum parking requirements (MPRs) and land use policy.

### Source Data#

#### Data Collection and Processing#

  * RGB imagery: Google Maps satellite tiles (30 cm/pixel)

  * NIR imagery: National Agriculture Imagery Program (NAIP) - upsampled from 1m/pixel to 30cm/pixel

  * Covers 45 US cities with ~35,000 annotated parking lots

  * Total area: 297.7 kmÂ² with 62.5 kmÂ² of labeled parking




#### Who are the source data producers?#

  * Google Maps (RGB imagery)

  * NAIP/USDA (NIR imagery)

  * Parking Reform Network (initial annotations for 42 cities)

  * OpenStreetMap (additional annotations for 3 cities)




### Annotations#

#### Annotation process#

Manual refinement of initial annotations in QGIS, ensuring boundaries align with pavement edges rather than property lines.

#### Who are the annotators?#

Students from the Urban Traffic & Economics Lab at UIUC, supervised by the paper authors.

## Personal and Sensitive Information#

Satellite imagery may incidentally capture vehicles and structures but no personally identifiable information is included.

## Bias, Risks, and Limitations#

  * Dataset focuses on US cities; parking lot designs may differ internationally

  * NIR channel contains tiling/mosaicking artifacts from orthorectification

  * Temporal misalignment possible between RGB and NIR sources

  * Urban-focused; may not generalize well to rural areas




## Recommendations#

  * Be aware of NIR artifacts when training models

  * Consider using NDVI statistics to filter samples by vegetation content

  * Post-processing steps (edge simplification, building/road removal) recommended for deployment




## Citation#

**BibTeX:**
    
    
    @article{qiam2024,
      title={A Pipeline and NIR-Enhanced Dataset for Parking Lot Segmentation},
      author={Shirin Qiam and Saipraneeth Devunuri and Lewis J. Lehe},
      journal={arXiv preprint arXiv:2412.13179},
      year={2024},
      url={https://arxiv.org/pdf/2412.13179}
    }
    

**APA:** Qiam, S., Devunuri, S., & Lehe, L. J. (2024). A Pipeline and NIR-Enhanced Dataset for Parking Lot Segmentation. _arXiv preprint arXiv:2412.13179_.

## Dataset Card Contact#

For questions about the original dataset: {sqiam2, sd37, lehe}@illinois.edu

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
