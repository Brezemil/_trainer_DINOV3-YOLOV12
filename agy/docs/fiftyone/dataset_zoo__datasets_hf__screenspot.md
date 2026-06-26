---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/screenspot.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ScreenSpot)

# Dataset Card for ScreenSpot#

![image/png](https://huggingface.co/datasets/Voxel51/ScreenSpot/resolve/main/ScreenSpot.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1272 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/ScreenSpot")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

Note: Dataset card details taken from [rootsautomation/ScreenSpot](https://huggingface.co/datasets/rootsautomation/ScreenSpot). GUI Grounding Benchmark: ScreenSpot.

Created researchers at Nanjing University and Shanghai AI Laboratory for evaluating large multimodal models (LMMs) on GUI grounding tasks on screens given a text-based instruction.

### Dataset Description#

ScreenSpot is an evaluation benchmark for GUI grounding, comprising over 1200 instructions from iOS, Android, macOS, Windows and Web environments, along with annotated element types (Text or Icon/Widget). See details and more examples in the paper.

  * **Curated by:** NJU, Shanghai AI Lab

  * **Language(s) (NLP):** EN

  * **License:** Apache 2.0




### Dataset Sources#

  * **Repository:** [GitHub](https://github.com/njucckevin/SeeClick)

  * **Paper:** [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935)




## Uses#

This dataset is a benchmarking dataset. It is not used for training. It is used to zero-shot evaluate a multimodal modelâs ability to locally ground on screens.

## Dataset Structure#

Each test sample contains:

  * `image`: Raw pixels of the screenshot

  * `file_name`: the interface screenshot filename

  * `instruction`: human instruction to prompt localization

  * `bbox`: the bounding box of the target element corresponding to instruction. While the original dataset had this in the form of a 4-tuple of (top-left x, top-left y, width, height), we first transform this to (top-left x, top-left y, bottom-right x, bottom-right y) for compatibility with other datasets.

  * `data_type`: âiconâ/âtextâ, indicates the type of the target element

  * `data_souce`: interface platform, including iOS, Android, macOS, Windows and Web (Gitlab, Shop, Forum and Tool)




## Dataset Creation#

### Curation Rationale#

This dataset was created to benchmark multimodal models on screens. Specifically, to assess a modelâs ability to translate text into a local reference within the image.

### Source Data#

Screenshot data spanning dekstop screens (Windows, macOS), mobile screens (iPhone, iPad, Android), and web screens.

#### Data Collection and Processing#

Sceenshots were selected by annotators based on their typical daily usage of their device. After collecting a screen, annotators would provide annotations for important clickable regions. Finally, annotators then write an instruction to prompt a model to interact with a particular annotated element.

#### Who are the source data producers?#

PhD and Master students in Comptuer Science at NJU. All are proficient in the usage of both mobile and desktop devices.

## Citation#

**BibTeX:**
    
    
    @misc{cheng2024seeclick,
          title={SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents}, 
          author={Kanzhi Cheng and Qiushi Sun and Yougang Chu and Fangzhi Xu and Yantao Li and Jianbing Zhang and Zhiyong Wu},
          year={2024},
          eprint={2401.10935},
          archivePrefix={arXiv},
          primaryClass={cs.HC}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
