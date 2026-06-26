---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/cholect50.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/cholect50)

# CholecT50 Dataset (FiftyOne Format)#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset version of the [CholecT50 dataset](https://github.com/CAMMA-public/cholect50).

CholecT50 is a dataset of laparoscopic cholecystectomy surgeries, annotated with surgical action triplets. It is the first public dataset to provide action triplet annotations for surgical videos, enabling research in fine-grained surgical activity recognition.

![cholect50](https://cdn-uploads.huggingface.co/production/uploads/690ba27044e8ef52338d87f5/_DSnB6L4IDIQ1Fmc5RTqH.gif)

## Dataset Description#

  * **Repository:** [CAMMA-public/cholect50](https://github.com/CAMMA-public/cholect50)

  * **Paper:** [Rendition of CholecT50: A dataset for surgical action triplet recognition](https://arxiv.org/abs/2202.05324)

  * **Point of Contact:** [Chinedu Innocent Nwoye](mailto:nwoye%40unistra.fr)




### Dataset Summary#

CholecT50 consists of 50 videos of laparoscopic cholecystectomy surgeries. Each frame is annotated with action triplets of the form `<Instrument, Verb, Target>`.

  * **Instruments:** 7 categories (e.g., grasper, bipolar, hook)

  * **Verbs:** 10 categories (e.g., grasp, retract, cauterize)

  * **Targets:** 15 categories (e.g., gallbladder, cystic duct, liver)




The dataset contains approximately 100,000 annotated frames, providing a rich source for training and evaluating models for surgical video understanding.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#

You can load the dataset from the Hugging Face Hub using FiftyOne:
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/cholect50")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Structure#

The dataset is organized as a FiftyOne dataset. Each sample represents a video frame and includes the following fields:

  * `filepath`: The path to the frame image.

  * `video_id`: The ID of the video the frame belongs to.

  * `frame_number`: The frame number within the video.

  * `instruments`: Classifications for the instruments present in the frame.

  * `verbs`: Classifications for the verbs (actions) being performed.

  * `targets`: Classifications for the targets of the actions.

  * `triplets`: The full action triplet annotations.

  * `clip_embeddings`: 512-dimensional embeddings generated using a CLIP model (ViT-B/32).




## Citation#

If you use the CholecT50 dataset in your research, please cite the following paper:
    
    
    @article{nwoye2022rendition,
      title={Rendition of CholecT50: A dataset for surgical action triplet recognition},
      author={Nwoye, Chinedu Innocent and Yu, Tong and Zahid, Anwar and Al Hajj, Hassan and Mutschler, Cristopher and Padoy, Nicolas},
      journal={arXiv preprint arXiv:2202.05324},
      year={2022}
    }
    

## License#

The CholecT50 dataset is released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
