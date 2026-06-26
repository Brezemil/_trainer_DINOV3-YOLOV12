---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/uco3d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/uco3d)

# Dataset Card for UnCommon Objects in 3D#

![image/png](https://huggingface.co/datasets/Voxel51/uco3d/resolve/main/uco3d.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 52 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/uco3d")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Details#

## Dataset Description#

uCO3D (UnCommon Objects in 3D) is a large-scale dataset of high-quality 360Â° videos of real-life objects with comprehensive 3D annotations.

It contains 170,000 objects across more than 1,000 diverse object categories derived from the LVIS taxonomy. Each object is captured in a turntable-like video with full 360Â° coverage, ensuring all sides of the object are visible. The dataset provides accurate 3D annotations including camera parameters, point clouds, and complete 3D Gaussian Splatting reconstructions. All objects are normalized to a canonical reference frame, facilitating training of generative models.

With its combination of scale, diversity, and quality, uCO3D addresses limitations in existing datasets, providing a superior resource for 3D deep learning research and applications.

  * **Curated by:** Xingchen Liu, Piyush Tayal, Jianyuan Wang, Jesus Zarzar, Tom Monnier, Konstantinos Tertikas, Jiali Duan, Antoine Toisoul, Jason Y. Zhang, Natalia Neverova, Andrea Vedaldi, Roman Shapovalov, David Novotny (Meta AI and collaborating institutions)

  * **Funded by:** Meta AI

  * **Shared by:** Meta AI

  * **Language(s) (NLP):** en

  * **License:** Not explicitly stated in the paper (likely Meta AI research license)




## Dataset Sources#

  * **Repository:** https://github.com/facebookresearch/uco3d

  * **Hugging Face Dataset Repo:** https://huggingface.co/datasets/facebook/uco3d

  * **Paper:** arXiv:2501.07574v1 [cs.CV] (Jan 13, 2025)

  * **Demo:** https://uco3d.github.io




# Uses#

## Direct Use#

The uCO3D dataset is specifically designed for:

  * Training feedforward few-view 3D reconstruction models (like LightplaneLRM)

  * Novel view synthesis using diffusion models (CAT3D-like approaches)

  * Text-to-3D generation (Instant3D-like pipelines)

  * Training large 3D generative models

  * Digital twinning applications (creating 3D models of real-life objects)

  * Research in 3D representation learning

  * Transfer learning for 3D vision tasks

  * Benchmarking 3D reconstruction algorithms




## Out-of-Scope Use#

The dataset is not intended for:

  * Real-time applications without appropriate downstream models

  * Human activity or behavioral analysis

  * Surveillance or security applications

  * Generating photorealistic synthetic human identities

  * Classes not represented in the 1,070 LVIS categories

  * Medical or safety-critical applications

  * Applications requiring perfect geometric accuracy (as SfM reconstructions have inherent limitations)




# Dataset Structure#

The full dataset consists of 170,000 video sequences organized by object category. Each sequence contains:

  * High-resolution video (60%+ at 1080p+) with full 360Â° coverage of a single object

  * 200 uniformly sampled frames with corresponding camera parameters (intrinsics and extrinsics)

  * Object segmentation masks for each frame

  * Sparse and dense SfM point clouds

  * Complete 3D Gaussian Splat reconstruction

  * Textual caption describing the object

  * Normalized object-centric coordinate system alignment




**Preview Subset:** Users can download a small 52-video subset of uCO3D for preview and debugging purposes. This subset represents a random sample of categories and takes approximately 9.6 GB, which is more than 1000x smaller than the full dataset. This preview subset is ideal for initial experimentation and workflow development before committing to the full dataset.

The 1,070 object categories are organized into 50 super-categories, with approximately 20 subcategories per super-category.

## Dataset Creation#

### Curation Rationale#

uCO3D was created to address limitations in existing 3D datasets:

  * CO3Dv2 has limited diversity (only 50 categories) and variable quality

  * MVImgNet lacks full 360Â° coverage of objects

  * High-quality 3D scan datasets like OmniObject3D have very limited scale

  * Synthetic datasets like Objaverse lack realism




uCO3D aims to provide the optimal balance between quality, scale, and diversity for real object-centric 3D learning.

### Source Data#

#### Data Collection and Processing#

  * Videos were captured by workers on Amazon Mechanical Turk

  * Workers followed a sine-wave trajectory (varying elevation) instead of a simple circular path

  * Each video was manually assessed for quality

  * Object segmentation used text-conditioned Segment-Anything (langSAM) with XMem for temporal consistency

  * 3D reconstruction used VGGSfM (more accurate than COLMAP used in previous datasets)

  * Scene alignment procedure normalized objects to canonical reference frames

  * 3D Gaussian Splat reconstruction was performed for each object using gsplat

  * Captioning used a vision-language model for per-view captions, summarized with LLAMA3




#### Who are the source data producers?#

Amazon Mechanical Turk workers captured the videos using consumer cameras. The workers were tasked with recording full 360Â° turntable-like videos of various objects, ensuring high resolution and complete coverage.

### Annotations#

#### Annotation process#

  * Camera parameters: VGGSfM estimated intrinsic and extrinsic parameters for 200 frames per video

  * Point clouds: VGGSfM generated sparse and dense point clouds

  * Segmentation: langSAM provided initial segmentations, refined by XMem for temporal consistency

  * 3D reconstruction: Each scene was reconstructed using 3D Gaussian Splatting

  * Alignment: Objects were aligned to canonical reference frames through a multi-step procedure

  * Captioning: Vision-language models generated per-view captions, synthesized by LLAMA3




The annotation quality was validated through both automated metrics and manual verification.

#### Who are the annotators?#

A combination of:

  * Automated systems (VGGSfM, langSAM, XMem, 3D Gaussian Splatting, vision-language models)

  * Meta AI research team (for quality control and validation)

  * Amazon Mechanical Turk workers (for initial video capture)




#### Personal and Sensitive Information#

The dataset focuses on object-centric videos and does not explicitly contain personal information. The objects captured are everyday items, and care was taken during the collection process to focus solely on the objects themselves.

## Bias, Risks, and Limitations#

  * Category distribution may not be perfectly balanced

  * Quality variations may exist across different object categories

  * Object selection may reflect cultural biases of the data collectors

  * SfM and 3DGS reconstructions have inherent technical limitations

  * Some complex object materials (transparent, reflective) may have lower quality reconstructions

  * The dataset is limited to static objects and does not include articulated or deformable objects

  * Training on this dataset alone may not generalize to all real-world scenarios




### Recommendations#

  * Consider the distribution of categories when training models

  * Evaluate models on diverse test sets beyond this dataset

  * Combine with synthetic data for categories underrepresented in this dataset

  * Be aware of potential biases in object representation

  * For highest quality results, filter by reconstruction quality metrics

  * For generative models, consider augmenting with other datasets for improved diversity




## Dataset Card Authors#

The dataset card is based on information from the paper âUnCommon Objects in 3Dâ by Xingchen Liu et al.

## Dataset Card Contact#

For more information, contact the authors via the GitHub repository: https://github.com/facebookresearch/uco3d

# Citation#
    
    
    @inproceedings{liu24uco3d,
        Author = {Liu, Xingchen and Tayal, Piyush and Wang, Jianyuan
                    and Zarzar, Jesus and Monnier, Tom and Tertikas, Konstantinos
                    and Duan, Jiali and Toisoul, Antoine and Zhang, Jason Y.
                    and Neverova, Natalia and Vedaldi, Andrea
                    and Shapovalov, Roman and Novotny, David},
        Booktitle = {arXiv},
        Title = {UnCommon Objects in 3D},
        Year = {2024},
    }
    

**APA:** Liu, X., Tayal, P., Wang, J., Zarzar, J., Monnier, T., Tertikas, K., Duan, J., Toisoul, A., Zhang, J. Y., Neverova, N., Vedaldi, A., Shapovalov, R., & Novotny, D. (2025). UnCommon Objects in 3D. arXiv preprint arXiv:2501.07574.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
