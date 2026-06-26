---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/phenobench.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/PhenoBench)

![pheno-bench-demo](https://huggingface.co/datasets/Voxel51/PhenoBench/resolve/main/./pheno-bench-demo.gif)

# Dataset Card for PhenoBench#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2,179 samples.

The images and original annotations are from [PhenoBench](https://www.phenobench.org/), a large UAV image dataset for semantic image interpretation in the agricultural domain (sugar beet crops and weeds), introduced by Weyler et al. in [_PhenoBench â A Large Dataset and Benchmarks for Semantic Image Interpretation in the Agricultural Domain_](https://arxiv.org/abs/2306.04557) (IEEE TPAMI, 2024). This release packages a subset of PhenoBench as a FiftyOne dataset and adds object-detection predictions and embeddings produced by Voxel51.

## Whatâs in this dataset#

  * **2,179 samples** (train: 1,407 / val: 386 / test: 386), each a 1024Ã1024 RGB UAV image of a sugar beet field

  * **Original PhenoBench annotations** (from phenobench.org):

    * `semantics` â semantic segmentation: background, crop, weed, partial-crop, partial-weed

    * `plant_instances` â per-plant instance segmentation

    * `leaf_instances` â per-leaf instance segmentation

    * `plant_visibility`, `leaf_visibility` â visibility heatmaps

  * **Voxel51-added detections and embeddings** :

    * `yolo11n`, `yolo11l` â YOLO11 (nano and large) object detection predictions for plants, with per-detection true-positive / false-positive / false-negative matches against the ground-truth instance masks

    * Brain runs in `brain/`: CLIP and DINOv2 embeddings + similarity indexes for sample-level and patch-level visual search




For the full original PhenoBench dataset (train/val/test = 1,407 / 772 / 693) and the canonical annotation specification, see [phenobench.org](https://www.phenobench.org/).

## License#

CC BY-SA 4.0, inherited from the upstream PhenoBench release.

## Installation#
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    dataset = load_from_hub("Voxel51/PhenoBench")
    
    # Launch the FiftyOne App
    session = fo.launch_app(dataset)
    

## Citation#

If you use this dataset, please cite the original PhenoBench paper:
    
    
    @article{weyler2024phenobench,
      title={PhenoBench: A Large Dataset and Benchmarks for Semantic Image Interpretation in the Agricultural Domain},
      author={Weyler, Jan and Magistri, Federico and Marks, Elias and Chong, Yue Linn and Sodano, Matteo and Roggiolani, Gianmarco and Chebrolu, Nived and Stachniss, Cyrill and Behley, Jens},
      journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
      year={2024},
      url={https://arxiv.org/abs/2306.04557}
    }
    

Please refer to [phenobench.org](https://www.phenobench.org/) for the authoritative citation and licensing terms.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
