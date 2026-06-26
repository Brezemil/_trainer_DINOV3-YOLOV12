---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/arcade_fo.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ARCADE_FO)

# Dataset Card for arcade_combined_export#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 3000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("pjramg/arcade_fiftyone")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# ARCADE Combined Dataset (FiftyOne Format)#

The **ARCADE Combined Dataset** is a curated collection of coronary angiography images and annotations designed to evaluate coronary artery stenosis. This version has been processed and exported using [FiftyOne](https://voxel51.com/fiftyone), and includes cleaned segmentation data, metadata fields for clinical context, and embedded visual labels.

## Dataset Structure#

  * `segmentations`: COCO-style detection masks per coronary artery segment.

  * `phase`: The acquisition phase of the angiography video.

  * `task`: A specific labeling task (segmentation or regression) is used.

  * `subset_name`: Subdivision info (train, val, test).

  * `coco_id`: Corresponding COCO ID for alignment with original sources.

  * `filepath`: Path to the image file.

  * `metadata`: Image metadata including dimensions and pixel spacing.




## Format#

This dataset is stored in **FiftyOneDataset format** , which consists of:

  * `data.json`: Metadata and label references

  * `data/`: Folder containing all image samples

  * Optional: auxiliary files (e.g., `README.md`, config, JSON index)




To load it in Python:
    
    
    import fiftyone as fo
    dataset = fo.Dataset.from_dir(
        dataset_dir="arcade_combined_fiftyone",
        dataset_type=fo.types.FiftyOneDataset,
    )
    

## Source#

The original ARCADE dataset was introduced in the paper:

Labrecque Langlais et al. (2023) â Evaluation of Stenoses Using AI Video Models Applied to Coronary Angiographies. https://doi.org/10.21203/rs.3.rs-3610879/v1

This combined version aggregates and restructures subsets across tasks and phases, harmonized with FiftyOne tooling for streamlined model training and evaluation.

## License#

This dataset is shared for research and academic use only. Please consult the original dataset license for clinical or commercial applications.

## Citation#
    
    
    @article{avram2023evaluation,
      title={Evaluation of Stenoses Using AI Video Models Applied to Coronary Angiographies},
      author={Labrecque Langlais, E. and Corbin, D. and Tastet, O. and Hayek, A. and Doolub, G. and Mrad, S. and Tardif, J.-C. and Tanguay, J.-F. and Marquis-Gravel, G. and Tison, G. and Kadoury, S. and Le, W. and Gallo, R. and Lesage, F. and Avram, R.},
      year={2023}
    }
    

## Dataset Card Contact#

[Paula Ramos](https://huggingface.co/datasets/pjramg)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
