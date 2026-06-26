---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/dancetrack.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/DanceTrack)

# Dataset Card for DanceTrack#

DanceTrack is a multi-human tracking dataset with two emphasized properties, (1) uniform appearance: humans are in highly similar and almost undistinguished appearance, (2) diverse motion: humans are in complicated motion pattern and their relative positions exchange frequently. We expect the combination of uniform appearance and complicated motion pattern makes DanceTrack a platform to encourage more comprehensive and intelligent multi-object tracking algorithms.

![image/png](https://huggingface.co/datasets/Voxel51/DanceTrack/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 33 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'split', 'max_samples', etc
    dataset = fouh.load_from_hub("dgural/DanceTrack")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

From _Multi-Object Tracking in Uniform Appearance and Diverse Motion_ :

A typical pipeline for multi-object tracking (MOT) is to use a detector for object localization, and following re-identification (re-ID) for object association. This pipeline is partially motivated by recent progress in both object detec- tion and re-ID, and partially motivated by biases in existing tracking datasets, where most objects tend to have distin- guishing appearance and re-ID models are sufficient for es- tablishing associations. In response to such bias, we would like to re-emphasize that methods for multi-object tracking should also work when object appearance is not sufficiently discriminative. To this end, we propose a large-scale dataset for multi-human tracking, where humans have similar appearance, diverse motion and extreme articulation. As the dataset contains mostly group dancing videos, we name it âDanceTrackâ. We expect DanceTrack to provide a better platform to develop more MOT algorithms that rely less on visual discrimination and depend more on motion analysis. We benchmark several state-of-the-art trackers on our dataset and observe a significant performance drop on DanceTrack when compared against existing benchmarks.

  * **Language(s) (NLP):** en

  * **License:** cc-by-4.0




### Dataset Sources#

  * **Repository:** https://dancetrack.github.io/

  * **Paper [optional]:** https://arxiv.org/abs/2111.14690

  * **Demo [optional]:** https://dancetrack.github.io/




## Uses#

This dataset is great for tracking use cases in computer vision is a common benchmark dataset.

## Citation#

@inproceedings{sun2022dance, title={DanceTrack: Multi-Object Tracking in Uniform Appearance and Diverse Motion}, author={Sun, Peize and Cao, Jinkun and Jiang, Yi and Yuan, Zehuan and Bai, Song and Kitani, Kris and Luo, Ping}, booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}, year={2022} }

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
