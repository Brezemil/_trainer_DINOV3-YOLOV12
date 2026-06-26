---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/crops3d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/crops3d)

# Dataset Card for crops3d#

![image/png](https://huggingface.co/datasets/Voxel51/crops3d/resolve/main/crops3d-mq.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1180 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import json
    import os
    import fiftyone as fo
    
    from huggingface_hub import snapshot_download
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(repo_id="Voxel51/crops3d", local_dir=".", repo_type="dataset")
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="crops3d"  # Assign a name to the dataset for identification
    )
    
    def update_dataset_ply_paths(dataset):
        """
        Update PLY file paths in FiftyOne 3D dataset to use absolute paths.
        
        This function iterates through all samples in a FiftyOne dataset and modifies
        any PLY mesh file paths found in the JSON metadata to be absolute paths
        relative to the sample's directory location.
        
        Args:
            dataset (fiftyone.Dataset): A FiftyOne dataset containing 3D samples
                                       with JSON metadata files that may reference
                                       PLY mesh files with relative paths.
        
        Returns:
            None: The function modifies the JSON files in-place on disk.
        
        Note:
            - This function assumes each sample's filepath points to a JSON file
            - The JSON structure should contain a 'children' array with objects
            - PLY mesh objects are identified by '_type': 'PlyMesh'
            - Only objects with a 'plyPath' field will be updated
        """
        # Iterate through each sample in the dataset
        for sample in dataset:
            # Get the file path of the current sample (JSON metadata file)
            fo3d_filepath = sample.filepath
            
            # Extract the directory containing the sample file
            fo3d_directory = os.path.dirname(fo3d_filepath)
            
            # Read and parse the JSON metadata file
            with open(fo3d_filepath, 'r') as f:
                fo3d_data = json.load(f)
            
            # Process each child object in the JSON structure
            for child in fo3d_data.get('children', []):
                # Check if this child is a PLY mesh object with a path reference
                if child.get('_type') == 'PlyMesh' and 'plyPath' in child:
                    # Convert relative PLY path to absolute path
                    # by joining it with the sample's directory
                    child['plyPath'] = os.path.join(fo3d_directory, child['plyPath'])
            
            # Write the updated JSON data back to the file
            with open(fo3d_filepath, 'w') as f:
                json.dump(fo3d_data, f, indent=2)  # Pretty-print with 2-space indentation
    
    # Execute the path update function on the loaded dataset
    update_dataset_ply_paths(dataset)
    

# Dataset Details#

## Dataset Description#

**Curated by:** Jianzhong Zhu, Ruifang Zhai, He Ren, Kai Xie, Aobo Du, Xinwei He, Chenxi Cui, Yinghua Wang, Junli Ye, Jiashi Wang, Xue Jiang, Yulong Wang, Chenglong Huang, Wanneng Yang (Huazhong Agricultural University, China)

**Funded by:** National Natural Science Foundation of China, National Key Research and Development Program of China

**Shared by:** Huazhong Agricultural University, National Key Laboratory of Crop Genetic Improvement

**Language(s) (NLP):** Not applicable (3D point cloud dataset)

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Dataset Sources [optional]#

**Repository:** https://github.com/clawCa/Crops3D

**Paper:** https://doi.org/10.1038/s41597-024-04290-0

**Demo:** Available through FiftyOne visualization after processing with provided scripts

You can see how the dataset was parsed [here](https://github.com/harpreetsahota204/crops3d_to_fiftyone)

## Uses#

### Direct Use#

  * **3D crop phenotyping research** : Analysis of plant morphology and structure

  * **Instance segmentation** : Segmenting individual plants in agricultural plots

  * **Plant classification** : Identifying and classifying different crop types from 3D data

  * **Organ segmentation** : Fine-grained segmentation of plant organs (leaves, stems, etc.)

  * **Agricultural robotics** : Training perception models for autonomous agricultural systems

  * **Precision agriculture** : Development of crop monitoring and assessment tools

  * **Computer vision research** : Benchmarking 3D segmentation and classification algorithms




## Dataset Structure#

The dataset contains 1,180 high-quality 3D point cloud samples in PLY format with RGB color information:

  * **File format** : PLY (Polygon File Format) with XYZ coordinates and RGB colors

  * **Total samples** : 1,180 point clouds

  * **Crop types** : 8 (Maize: 225, Cabbage: 196, Cotton: 176, Rapeseed: 150, Wheat: 148, Potato: 118, Rice: 84, Tomato: 83)

  * **Acquisition methods** : Multi-view stereo (mvs) and structured light (sl)

  * **File naming** : `{CropType}-{identifier}.ply` (e.g., `Cabbage-mvs_1005_01.ply`)

  * **Point density** : Varies by acquisition method and crop complexity

  * **Additional variants** :

    * Crops3D_10k: Subsampled to 10,000 points using Farthest Point Sampling

    * Crops3D_10k-C: Corruption robustness test sets with 7 corruption types at 5 severity levels

    * Crops3D_IS: Instance segmentation data for plot-level analysis




## Dataset Creation#

### Curation Rationale#

The dataset was created to address the lack of comprehensive 3D agricultural datasets for developing and benchmarking computer vision algorithms in precision agriculture. Existing datasets were limited in diversity, realism, and complexity, hindering the development of robust agricultural perception systems. Crops3D fills this gap by providing authentic, diverse, and complex 3D point cloud data from real agricultural environments.

### Source Data#

#### Data Collection and Processing#

  * **Collection period** : Multiple growth stages across agricultural seasons

  * **Location** : Agricultural research fields in China

  * **Equipment** : Professional 3D scanning devices using multi-view stereo and structured light technologies

  * **Processing** :

    * Raw point clouds captured from multiple viewpoints

    * Registration and fusion to create complete 3D models

    * Color information preserved from RGB cameras

    * Quality control to ensure accurate geometry and color




#### Who are the source data producers?#

The data was produced by researchers at:

  * Huazhong Agricultural University

  * National Key Laboratory of Crop Genetic Improvement

  * Collaborative teams from agricultural and computer vision research groups




### Annotations#

#### Annotation process#

  * **Plant-level labels** : Each point cloud is labeled with its crop type

  * **Instance segmentation** : Plot-level data includes individual plant boundaries

  * **Organ segmentation** : Selected samples include organ-level annotations (leaves, stems)

  * **Quality assurance** : Multiple rounds of verification by agricultural experts




#### Who are the annotators?#

  * Agricultural researchers and graduate students from Huazhong Agricultural University

  * Domain experts in crop phenotyping and plant science

  * Computer vision researchers familiar with 3D data annotation




## Personal and Sensitive Information#

The dataset contains no personal or sensitive information. All data consists of 3D scans of agricultural crops in research fields with no human subjects or private information included.

## Bias, Risks, and Limitations#

**Biases:**

  * **Geographic bias** : Data collected primarily from agricultural fields in China, may not represent all global agricultural conditions

  * **Crop selection bias** : Limited to 8 major crop types, doesnât cover all agricultural species

  * **Growth stage bias** : May not equally represent all growth stages for each crop




**Risks:**

  * **Generalization** : Models trained on this data may not perform well on crops grown in significantly different climates or conditions

  * **Scale limitations** : Individual plant models may not scale directly to large field applications




**Limitations:**

  * **Point cloud density variations** : Different acquisition methods produce varying point densities

  * **Occlusion** : Natural self-occlusion in dense crop canopies may limit visibility of internal structures

  * **Weather conditions** : Data collected under specific weather conditions may not represent all scenarios

  * **File size** : Large PLY files (~9GB total) require significant storage and processing resources




## Recommendations#

Users should be made aware of the following recommendations:

  1. **Preprocessing** : Consider subsampling large point clouds for efficiency (Crops3D_10k variant available)

  2. **Validation** : Test model generalization on crops from different geographic regions

  3. **Augmentation** : Apply appropriate 3D augmentations to improve model robustness

  4. **Multi-modal approaches** : Consider combining with 2D imagery or other sensor data for comprehensive analysis

  5. **Computational resources** : Ensure adequate GPU memory and storage for processing large point clouds

  6. **Domain adaptation** : May require fine-tuning for specific agricultural environments or crop varieties




## Citation#

**BibTeX:**
    
    
    @article{zhu2024crops3d,
      title={Crops3D: a diverse 3D crop dataset for realistic perception and segmentation toward agricultural applications},
      author={Zhu, Jianzhong and Zhai, Ruifang and Ren, He and Xie, Kai and Du, Aobo and He, Xinwei and Cui, Chenxi and Wang, Yinghua and Ye, Junli and Wang, Jiashi and Jiang, Xue and Wang, Yulong and Huang, Chenglong and Yang, Wanneng},
      journal={Scientific Data},
      volume={11},
      number={1438},
      year={2024},
      doi={10.1038/s41597-024-04290-0},
      publisher={Nature Publishing Group}
    }
    

**APA:**

Zhu, J., Zhai, R., Ren, H., Xie, K., Du, A., He, X., Cui, C., Wang, Y., Ye, J., Wang, J., Jiang, X., Wang, Y., Huang, C., & Yang, W. (2024). Crops3D: a diverse 3D crop dataset for realistic perception and segmentation toward agricultural applications. _Scientific Data_ , 11, 1438. https://doi.org/10.1038/s41597-024-04290-0

## Glossary#

  * **PLY** : Polygon File Format, a file format for storing 3D data

  * **Point Cloud** : A collection of 3D points representing the external surface of an object

  * **FPS** : Farthest Point Sampling, a method for subsampling point clouds

  * **Instance Segmentation** : Identifying and separating individual objects (plants) in a scene

  * **Organ Segmentation** : Identifying different parts of a plant (leaves, stems, fruits)

  * **Multi-view Stereo (MVS)** : 3D reconstruction technique using multiple 2D images

  * **Structured Light (SL)** : 3D scanning method using projected light patterns

  * **Phenotyping** : Measuring observable plant characteristics




## More Information#

  * **Dataset website** : https://figshare.com/articles/dataset/Crops3D_a_diverse_3D_crop_dataset_for_realistic_perception_and_segmentation_toward_agricultural_applications/27313272

  * **Download link** : https://springernature.figshare.com/ndownloader/files/50027964

  * **Related datasets** : PlantNet, AgriNet, Leaf Counting Challenge datasets

  * **Applications** : Yield prediction, disease detection, growth monitoring, harvesting automation




## Dataset Card Authors#

  * Original dataset: Jianzhong Zhu et al., Huazhong Agricultural University

  * Dataset card: Prepared for Hugging Face distribution




## Dataset Card Contact#

  * **Primary contact** : Wanneng Yang (yangwn@mail.hzau.edu.cn)

  * **Institution** : National Key Laboratory of Crop Genetic Improvement, Huazhong Agricultural University

  * **GitHub Issues** : https://github.com/clawCa/Crops3D/issues




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
