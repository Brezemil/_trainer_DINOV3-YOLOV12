---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/ris_lad.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/RIS-LAD)

# Dataset Card for RIS-LAD#

![image/png](https://huggingface.co/datasets/Voxel51/RIS-LAD/resolve/main/ris-lad.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2103 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/RIS-LAD")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

**RIS-LAD** (Referring Low-Altitude Drone Image Segmentation) is the first fine-grained Referring Image Segmentation benchmark specifically designed for low-altitude drone (LAD) scenarios.

The dataset contains **13,871** meticulously annotated image-text-mask triplets collected from real-world drone footage captured at altitudes of approximately 30-100 meters with oblique viewing angles (30Â°-60Â°).

Unlike existing remote sensing RIS datasets that focus on high-altitude satellite or fixed-angle imagery, RIS-LAD addresses unique challenges of low-altitude drone perception including:

  * Strong perspective changes and foreshortening from oblique views

  * Tiny and densely packed objects

  * Variable illumination conditions including nighttime scenes

  * Category drift (tiny targets causing confusion with larger, semantically similar objects)

  * Object drift (difficulty distinguishing among crowded same-class instances)




The dataset was constructed using a semi-automatic pipeline combining SAM-2 for high-quality instance masks and multimodal LLM-generated referring expressions, followed by human refinement and verification.

  * **Curated by:** Kai Ye, Yingshi Luan, Zhudi Chen, Guangyue Meng, Pingyang Dai, Liujuan Cao (Xiamen University)

  * **Language(s) (NLP):** English

  * **License:** CC BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike 4.0)




### Dataset Sources#

  * **Repository:** https://github.com/AHideoKuzeA/RIS-LAD-A-Benchmark-and-Model-for-Referring-Low-Altitude-Drone-Image-Segmentation

  * **Paper:** [RIS-LAD: A Benchmark and Model for Referring Low-Altitude Drone Image Segmentation](https://arxiv.org/abs/2507.20920)

  * **Dataset Download:** [Google Drive](https://drive.google.com/file/d/1PmtaQH_F0AUoGWgpmDSpPu27E2XSdGd4/view?usp=sharing)




## Uses#

### Direct Use#

This dataset is intended for:

  * **Referring Image Segmentation (RIS)** : Training and evaluating models that segment objects based on natural language descriptions

  * **Vision-Language Research** : Multi-modal learning combining computer vision and natural language processing

  * **Low-Altitude Drone Perception** : Developing perception systems for drone applications operating at 30-100m altitude

  * **Visual Grounding** : Research on grounding natural language expressions to visual regions

  * **Benchmark Evaluation** : Comparing RIS methods specifically under challenging low-altitude drone conditions with tiny, dense objects and variable illumination




### Out-of-Scope Use#

  * **Commercial Applications** : The dataset is licensed under CC BY-NC-SA 4.0, restricting commercial use

  * **High-Altitude Remote Sensing** : The dataset is specifically designed for low-altitude (30-100m) oblique views and may not generalize well to satellite or high-altitude imagery

  * **Ground-Level Scene Understanding** : The oblique drone perspective differs substantially from conventional ground-view datasets

  * **Privacy-Sensitive Applications** : Users should be aware that drone imagery may contain identifiable individuals or private property




## Dataset Structure#

### FiftyOne Format#

When converted to FiftyOne using the provided conversion script, each sample contains:

  * **`filepath`** : Path to the image file

  * **`tags`** : Dataset split as a tag (`train`, `val`, or `test`)

  * **`prompts`** : List of all referring expression strings for that image

  * **`ground_truth`** : FiftyOne Detections object containing:

    * `label`: Object category name

    * `bounding_box`: Normalized bounding box coordinates [x, y, width, height] in range [0, 1]

    * `mask`: Binary segmentation mask (cropped to bounding box region)

    * `ref_id`: Unique reference ID

    * `ann_id`: Annotation ID linking to the original data

    * `referring_expression`: The natural language description for this specific object




### Object Categories#

The dataset includes 8 object categories commonly found in low-altitude drone imagery:

Category | Count | Description  
---|---|---  
car | 4,365 | Most common category  
people | 2,910 | Pedestrians and individuals  
motor | 2,803 | Motorcycles and motorized two-wheelers  
truck | 1,648 | Trucks and large vehicles  
bus | 732 | Buses  
bicycle | 640 | Bicycles  
tricycle | 528 | Tricycles  
boat | 245 | Boats and watercraft  
  
## Dataset Creation#

### Curation Rationale#

Existing referring image segmentation (RIS) datasets focus primarily on conventional ground-view scenes or high-altitude remote sensing imagery. These settings differ substantially from low-altitude drone (LAD) views where:

  * Perspectives are oblique (30Â°-60Â° angles) rather than top-down or horizontal

  * Objects are tiny and densely packed

  * Illumination varies widely, including nighttime scenes

  * Altitude is much lower (30-100m) compared to satellite imagery (>1000m)




RIS-LAD was created to bridge this gap and enable research on referring image segmentation specifically for low-altitude drone applications, which are increasingly deployed in real-world perception systems due to their flexibility and cost-effectiveness.

### Source Data#

#### Data Collection and Processing#

**Image Collection:**

  * Source: Real-world drone footage captured at altitudes of 30-100 meters

  * Viewing angles: Oblique perspectives at 30Â°-60Â° angles

  * Resolution: 1080Ã1080 pixels

  * Conditions: Various illumination including daytime and nighttime scenes

  * Total images: 2,104 unique images




**Annotation Pipeline (Semi-Automatic):**

  1. **Instance Segmentation** : High-quality instance masks generated using SAM-2 (Segment Anything Model 2) with prompting

  2. **Referring Expression Generation** : Initial expressions generated by multimodal LLMs given:

     * Cropped instance images

     * Location cues

     * Category information

  3. **Human Refinement** : Manual verification and refinement of both masks and expressions

  4. **Quality Control** : Careful verification of all 13,871 image-text-mask triplets




#### Who are the source data producers?#

The source data was collected from real-world drone operations. The specific locations and operators are not disclosed in the publicly available information. The dataset was curated and annotated by researchers at Xiamen University.

### Annotations#

#### Annotation process#

The dataset uses a semi-automatic annotation pipeline:

  1. **Segmentation Masks** : Generated using SAM-2 with human-in-the-loop prompting and verification

  2. **Referring Expressions** :

     * Initially generated by multimodal LLMs

     * Provided with cropped object images and spatial location information

     * Manually refined by human annotators

     * Verified for accuracy and naturalness




The annotations include:

  * Binary segmentation masks (RLE format)

  * Bounding boxes

  * Natural language referring expressions

  * Object category labels

  * Tokenized text




#### Who are the annotators?#

The annotation team consisted of researchers from Xiamen University who performed the human refinement and verification steps of the semi-automatic pipeline. Specific demographic information about annotators is not provided.

#### Personal and Sensitive Information#

The dataset contains drone imagery captured from low altitudes (30-100m) which may include:

  * **Identifiable individuals** : People visible in public spaces

  * **Vehicles** : Cars, motorcycles, trucks, buses with potentially visible license plates

  * **Location information** : Urban and outdoor scenes




**Privacy Considerations:**

  * Images are from real-world drone footage

  * No explicit anonymization process is described

  * Users should be aware of potential privacy implications

  * The non-commercial license (CC BY-NC-SA 4.0) provides some restrictions on use




### Dataset-Specific Challenges#

The paper identifies two key failure modes that are prevalent in this dataset:

  1. **Category Drift** : Tiny targets can cause models to incorrectly segment larger, semantically similar objects

  2. **Object Drift** : Dense crowds of same-class instances make it difficult to distinguish which specific instance is being referred to




### Potential Biases#

  * **Domain Bias** : Focused on urban/outdoor surveillance scenarios typical of drone operations

  * **Category Distribution** : Heavily skewed toward vehicles (cars: 31%, motor: 20%, truck: 12%) vs. other categories

  * **Illumination Bias** : While nighttime scenes are included, the distribution between day/night is not specified

  * **Expression Style** : Referring expressions generated by LLMs may have stylistic patterns that differ from purely human-generated descriptions




## Citation#

**BibTeX:**
    
    
    @misc{ye2025risladbenchmarkmodelreferring,
      title        = {RIS-LAD: A Benchmark and Model for Referring Low-Altitude Drone Image Segmentation}, 
      author       = {Kai Ye and YingShi Luan and Zhudi Chen and Guangyue Meng and Pingyang Dai and Liujuan Cao},
      year         = {2025},
      eprint       = {2507.20920},
      archivePrefix= {arXiv},
      primaryClass = {cs.CV},
      url          = {https://arxiv.org/abs/2507.20920}
    }
    

**APA:**

Ye, K., Luan, Y., Chen, Z., Meng, G., Dai, P., & Cao, L. (2025). RIS-LAD: A Benchmark and Model for Referring Low-Altitude Drone Image Segmentation. _arXiv preprint arXiv:2507.20920_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
