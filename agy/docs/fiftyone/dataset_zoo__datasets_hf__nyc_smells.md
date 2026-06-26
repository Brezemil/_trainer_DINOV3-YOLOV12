---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/nyc_smells.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/NYC_Smells)

# Dataset Card for New York Smells#

![image/png](https://huggingface.co/datasets/Voxel51/NYC_Smells/resolve/main/nyc_smells_dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 20000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/NYC_Smells")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

New York Smells is a large-scale multimodal dataset pairing visual imagery with electronic nose (e-nose) olfactory signals captured âin the wildâ throughout New York City. The dataset enables cross-modal learning between smell and sight, addressing a critical gap in machine perception research where olfaction remains largely inaccessible to machines compared to vision, sound, and touch.

The dataset contains 7,000 smell-image pairs from 3,500 distinct objects across 60 recording sessions in diverse indoor and outdoor environmentsâapproximately 70Ã more objects than existing olfactory datasets.

  * **Curated by:** Ege Ozguroglu, Junbang Liang, Ruoshi Liu, Mia Chiquier, Michael DeTienne, Wesley Wei Qian, Alexandra Horowitz, Andrew Owens, Carl Vondrick

  * **Institutions:** Columbia University, Cornell University, Osmo Labs

  * **Funded by:** Not specified

  * **License:** Not specified (check project website for updates)




### Dataset Sources#

  * **Repository:** https://smell.cs.columbia.edu/

  * **Paper:** https://arxiv.org/abs/2511.20544

  * **Data Download:** https://smell.cs.columbia.edu/static/smell-dataset.tar.gz (27 GB)

  * **Hardware Rig Specs:** https://smell.cs.columbia.edu/static/hardware.zip




## Uses#

### Direct Use#

  * **Cross-modal smell-to-image retrieval:** Given a query smell, retrieve matching images in embedding space

  * **Scene/object/material recognition from smell alone:** Classify scenes, objects, and materials using only olfactory signals

  * **Fine-grained olfactory discrimination:** Distinguish between similar objects (e.g., different grass species)

  * **Olfactory representation learning:** Train general-purpose smell embeddings using visual supervision

  * **Multimodal sensor fusion research:** Combine RGB, depth, and chemical sensor modalities




### Out-of-Scope Use#

  * Medical diagnosis or health-related smell detection (dataset not collected for clinical purposes)

  * Hazardous material detection (not designed for safety-critical applications)

  * Individual identification or tracking via smell

  * Production deployment without additional validation on target domain




## Dataset Structure#

### FiftyOne Dataset Organization#

The dataset is loaded as a **grouped dataset** with three slices per sample:

Slice | Description  
---|---  
`rs_rgb` (default) | RealSense RGB image with depth heatmap overlay  
`rgb` | iPhone RGB image  
`olfaction` | Olfaction diff visualization (sample â baseline heatmap)  
  
### Sample Fields#

Field | Type | Description  
---|---|---  
`clip_features` | VectorField (768,) | Pre-computed CLIP embeddings  
`smellprint_vector` | VectorField (32,) | Normalized 32-channel smell signature  
`olfaction_diff` | VectorField (32,) | Max-pooled olfaction diff (sample â baseline)  
`baseline_max` | VectorField (32,) | Max-pooled baseline (ambient) readings  
`sample_max` | VectorField (32,) | Max-pooled sample (object) readings  
`baseline_raw` | ArrayField (~17, 32) | Raw olfactory baseline time series  
`sample_raw` | ArrayField (~17, 32) | Raw olfactory object time series  
`location` | Classification | Recording location (e.g., âCV Lab Loungeâ)  
`object_class` | Classification | Object index (numeric ID, no human-readable mapping yet)  
`timestamp` | DateTimeField | Session timestamp  
`session_id` | StringField | Session identifier (e.g., â2025-04-12_16-59-24â)  
`global_id` | StringField | Unique sample identifier  
`temperature` | FloatField | Ambient temperature (Â°C)  
`humidity` | FloatField | Ambient humidity (%)  
`pid` | StringField | VOC concentration (PID sensor reading)  
`depth_heatmap` | Heatmap | 16-bit depth map overlay (rs_rgb slice only)  
  
### Pre-computed Visualizations (Brain Keys)#

Brain Key | Embeddings | Description  
---|---|---  
`clip_viz` | `clip_features` | UMAP of visual CLIP embeddings  
`smellprint_viz` | `smellprint_vector` | UMAP of pre-computed smell fingerprints  
`olfaction_diff_viz` | `olfaction_diff` | UMAP of objectâs unique smell signature  
`baseline_max_viz` | `baseline_max` | UMAP of ambient environment smell  
`sample_max_viz` | `sample_max` | UMAP of object + environment smell  
  
## Dataset Creation#

### Curation Rationale#

While olfaction is central to how animals perceive the world, this sensory modality remains largely inaccessible to machines. A key bottleneck is the lack of diverse, multimodal olfactory training data collected in natural settings. Existing olfactory datasets are small and captured in controlled lab environments. New York Smells addresses this gap by providing large-scale, in-the-wild paired vision-olfaction data.

### Source Data#

#### Data Collection and Processing#

  * **Sensor Hardware:** Cyranose 320 electronic nose with 32 polymer-composite chemoresistive sensors, mounted on a custom 3D-printed rig with an iPhone camera and Intel RealSense depth sensor

  * **Collection Method:** Researchers walked through various NYC locations capturing synchronized images and e-nose readings of odorant objects

  * **Locations:** Parks, gyms, dining halls, libraries, streets, and other indoor/outdoor environments across New York City

  * **Sessions:** 60 recording sessions

  * **Samples:** 7,000 smell-image pairs from 3,500 distinct objects

  * **Additional Sensors:** RGB-D, temperature, humidity, volatile organic compound (VOC) concentration




#### Olfactory Signal Format#

  * **Baseline:** ~17 timesteps Ã 32 sensors â ambient air reading before approaching object

  * **Sample:** ~17 timesteps Ã 32 sensors â reading while near object

  * **Smellprint:** 32-element vector â pre-computed time-collapsed fingerprint

  * **Values:** Normalized resistance ratios (ÎR/Râ)




#### Who are the source data producers?#

Research team from Columbia University, Cornell University, and Osmo Labs collected all data in New York City.

### Annotations#

#### Annotation process#

  * **Location labels:** Manually recorded during collection sessions

  * **Object indices:** Assigned during collection (human-readable labels pending release)

  * **Scene/object/material labels:** Generated via GPT-4o (release pending per authors)

  * **CLIP features:** Pre-computed using CLIP model on RGB images




#### Who are the annotators?#

The research team annotated location and object information. GPT-4o was used for scene/object/material labeling (pending release).

## Citation#

### BibTeX#
    
    
    @article{ozguroglu2025smell,
      title={New York Smells: A Large Multimodal Dataset for Olfaction},
      author={Ozguroglu, Ege and Liang, Junbang and Liu, Ruoshi and Chiquier, Mia and DeTienne, Michael and Qian, Wesley Wei and Horowitz, Alexandra and Owens, Andrew and Vondrick, Carl},
      journal={arXiv preprint arXiv:2511.20544},
      year={2025}
    }
    

### APA#

Ozguroglu, E., Liang, J., Liu, R., Chiquier, M., DeTienne, M., Qian, W. W., Horowitz, A., Owens, A., & Vondrick, C. (2025). New York Smells: A Large Multimodal Dataset for Olfaction. _arXiv preprint arXiv:2511.20544_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
