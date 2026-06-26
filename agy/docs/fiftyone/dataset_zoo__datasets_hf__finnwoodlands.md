---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/finnwoodlands.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/FinnWoodlands)

# Dataset Card for FinnWoodlands#

![image/png](https://huggingface.co/datasets/Voxel51/FinnWoodlands/resolve/main/finnwoodland.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 250 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/FinnWoodlands")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card for FinnWoodlands#

## Dataset Details#

### Dataset Description#

FinnWoodlands is a forest dataset designed for forestry and robotics applications. It consists of RGB stereo images, point clouds, and sparse depth maps, along with ground truth manual annotations for semantic, instance, and panoptic segmentation. The dataset comprises 4,226 manually annotated objects, with 2,562 objects (60.6%) corresponding to tree trunks classified into three instance categories: âSpruce Tree,â âBirch Tree,â and âPine Tree.â Additional annotations include âObstaclesâ as instance objects and semantic âstuffâ classes: âLake,â âGround,â and âTrack.â

  * **Curated by:** Juan Lagos, Urho LempiÃ¶, and Esa Rahtu (Tampere University, Finland)

  * **Shared by:** Tampere University

  * **Language(s) (NLP):** N/A (Computer Vision dataset)

  * **License:** Â© Springer Nature Switzerland (exclusive license) - see paper for full terms




### Dataset Sources#

  * **Repository:** https://github.com/juanb09111/FinnForest

  * **Paper:** https://link.springer.com/chapter/10.1007/978-3-031-31435-3_7

  * **ArXiv:** https://arxiv.org/abs/2304.00793

  * **Data Download (with annotations):** https://drive.google.com/file/d/1uf9QBv1j_VRjM6jWCp2cgw5ZQ5CUx9R7/view

  * **Data Download (full, no GT):** https://drive.google.com/drive/folders/1RhLxuHoxfB5C-Nz2_oyVAX1ima02Ddt8




## Uses#

### Direct Use#

  * Semantic segmentation in forest environments

  * Instance segmentation for tree trunk detection and species classification

  * Panoptic segmentation for holistic forest scene understanding

  * Depth completion from sparse depth maps

  * Autonomous forestry robotics and navigation

  * Development of data-driven methods for unstructured outdoor environments

  * Benchmarking perception models for forest-like scenarios




### Out-of-Scope Use#

  * Urban or indoor scene understanding (dataset is forest-specific)

  * Tree species classification beyond the three included species (Spruce, Birch, Pine)

  * Geographic generalization to forests outside Finland without domain adaptation

  * Real-time applications without appropriate model optimization (benchmark models may require tuning)




## Dataset Structure#

**Modalities:**

  * RGB stereo images




**Annotation Types:**

  * Panoptic segmentation annotations




**Classes:**

Category Type | Class Name | Description  
---|---|---  
Things (Instance) | Spruce Tree | Tree trunk instances  
Things (Instance) | Birch Tree | Tree trunk instances  
Things (Instance) | Pine Tree | Tree trunk instances  
Things (Instance) | Obstacles | Other countable objects  
Stuff (Semantic) | Lake | Water bodies  
Stuff (Semantic) | Ground | Forest floor  
Stuff (Semantic) | Track | Forest paths/roads  
  
## Dataset Creation#

### Curation Rationale#

Large and diverse datasets have driven breakthroughs in autonomous driving and indoor applications, but forestry applications lag behind due to a lack of suitable datasets. FinnWoodlands was created to address this gap and enable significant progress in developing data-driven methods for forest-like scenarios, particularly for applications requiring holistic environmental representation.

### Source Data#

#### Data Collection and Processing#

Data was collected in Finnish forest environments using stereo camera setups capable of capturing RGB stereo images, point clouds, and sparse depth maps. The dataset captures unstructured forest scenarios that present unique challenges compared to urban or indoor environments.

#### Who are the source data producers?#

Researchers at Tampere University, Finland, collected the data in Finnish woodland environments.

### Annotations#

#### Annotation process#

Manual annotations were created using CVAT (Computer Vision Annotation Tool) for semantic, instance, and panoptic segmentation. The annotation scheme follows the âstuffâ and âthingsâ paradigm from computer vision, where âstuffâ classes represent uncountable regions (Lake, Ground, Track) and âthingsâ classes represent countable objects (tree trunks, obstacles).

#### Who are the annotators?#

The research team at Tampere University performed the annotations.

## Citation#

### BibTeX#
    
    
    @InProceedings{10.1007/978-3-031-31435-3_7,
    author="Lagos, Juan
    and Lempi{\"o}, Urho
    and Rahtu, Esa",
    editor="Gade, Rikke
    and Felsberg, Michael
    and K{\"a}m{\"a}r{\"a}inen, Joni-Kristian",
    title="FinnWoodlands Dataset",
    booktitle="Image Analysis",
    year="2023",
    publisher="Springer Nature Switzerland",
    address="Cham",
    pages="95--110",
    }
    

### APA#

Lagos, J., LempiÃ¶, U., & Rahtu, E. (2023). FinnWoodlands Dataset. In R. Gade, M. Felsberg, & J.-K. KÃ¤mÃ¤rÃ¤inen (Eds.), _Image Analysis_ (pp. 95-110). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-31435-3_7

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
