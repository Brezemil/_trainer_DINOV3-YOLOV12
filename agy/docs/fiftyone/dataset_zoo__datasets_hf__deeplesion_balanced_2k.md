---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/deeplesion_balanced_2k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/deeplesion-balanced-2k)

# DeepLesion Benchmark Subset (Balanced 2K)#

This dataset is a curated subset of the [DeepLesion dataset](https://nihcc.app.box.com/v/DeepLesion), prepared for demonstration and benchmarking purposes. It consists of 2,000 CT lesion samples, balanced across 8 coarse lesion types, and filtered to include lesions with a short diameter > 10mm.

## Dataset Details#

  * **Source** : [DeepLesion](https://nihcc.app.box.com/v/DeepLesion)

  * **Institution** : National Institutes of Health (NIH) Clinical Center

  * **Subset size** : 2,000 images

  * **Lesion types** : lung, abdomen, mediastinum, liver, pelvis, soft tissue, kidney, bone

  * **Selection criteria** :

    * Short diameter > 10mm

    * Balanced sampling across all types

  * **Windowing** : All slices were windowed using DICOM parameters and converted to 8-bit PNG format




## License#

This dataset is shared under the **[CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)** , as specified by the NIH DeepLesion dataset creators.

> This dataset is intended **only for non-commercial research and educational use**.  
>  You must credit the original authors and the NIH Clinical Center when using this data.

## Citation#

If you use this data, please cite:
    
    
    @article{yan2018deeplesion,
    title={DeepLesion: automated mining of large-scale lesion annotations and universal lesion detection with deep learning},
    author={Yan, Ke and Zhang, Yao and Wang, Le Lu and Huang, Xuejun and Summers, Ronald M},
    journal={Journal of medical imaging},
    volume={5},
    number={3},
    pages={036501},
    year={2018},
    publisher={SPIE}
    }
    
    Curation done by FiftyOne.
    @article{moore2020fiftyone,
      title={FiftyOne},
      author={Moore, B. E. and Corso, J. J.},
      journal={GitHub. Note: https://github.com/voxel51/fiftyone},
      year={2020}
    }
    

## Intended Uses#

  * Embedding demos

  * Lesion similarity and retrieval

  * Benchmarking medical image models

  * Few-shot learning on lesion types




## Limitations#

  * This is a small subset of the full DeepLesion dataset

  * Not suitable for training full detection models

  * Labels are coarse and may contain inconsistencies




## Contact#

Created by Paula Ramos for demo purposes using FiftyOne and the DeepLesion public metadata.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
