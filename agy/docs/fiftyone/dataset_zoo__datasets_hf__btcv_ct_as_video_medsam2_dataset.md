---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/btcv_ct_as_video_medsam2_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/BTCV-CT-as-video-MedSAM2-dataset)

# Dataset Card for btcv#

![image/png](https://huggingface.co/datasets/Voxel51/BTCV-CT-as-video-MedSAM2-dataset/resolve/main/dataset_preview.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 30 video samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/BTCV-CT-as-video-MedSAM2-dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is the âBeyond the Cranial Vaultâ (BTCV) dataset used by Medical-SAM2 paper. Med-SAM2 fine-tunes the Segment Anything Model 2 on to accurately segment CT-scan imagery. The paper âadopts the philosophy of taking medical images as videosâ; so, the images have been converted into videos, and maybe easily resampled into frames using `dataset.to_frames(sample_frames=True)`.

  * **Curated by:** [Synapse](https://www.synapse.org/Synapse:syn3193805/wiki/89480)

  * **Shared by [optional]:** [Jiayuan Zhu](https://huggingface.co/datasets/jiayuanz3/btcv/tree/main) and [Med-SAM2 Authors](https://github.com/MedicineToken/Medical-SAM2)




### Dataset Sources [optional]#

  * **Med-SAM2 Github Repository:** [MedicineToken/Medical-SAM2](https://github.com/MedicineToken/Medical-SAM2)

  * **Paper:** [Medical SAM 2: Segment medical images as video via Segment Anything Model 2](https://arxiv.org/abs/2408.00874)

  * **Data Repository:** [Med-SAM2 preprocessed dataset on HF](https://huggingface.co/datasets/jiayuanz3/btcv/tree/main)

  * **Demo [optional]:** [Coming Soonâ¦]




## Uses#

### Direct Use#

[More Information Needed]

### Out-of-Scope Use#

[More Information Needed]

## Dataset Structure#

[More Information Needed]

## Dataset Creation#

### Curation Rationale#

[More Information Needed]

### Source Data#

#### Data Collection and Processing#

[More Information Needed]

#### Who are the source data producers?#

[More Information Needed]

### Annotations [optional]#

#### Annotation process#

[More Information Needed]

#### Who are the annotators?#

[More Information Needed]

#### Personal and Sensitive Information#

[More Information Needed]

## Bias, Risks, and Limitations#

[More Information Needed]

### Recommendations#

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]#

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]#

[More Information Needed]

## Dataset Card Authors#

  * [Evatt Harvey-Salinger](https://huggingface.co/evatt-harvey-salinger)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
