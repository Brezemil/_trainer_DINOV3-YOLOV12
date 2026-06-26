---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/football_player_segmentation.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Football-Player-Segmentation)

# Dataset Card for football-player-segmentation#

This dataset is specifically designed for computer vision tasks related to player detection and segmentation in foot goalkeeperders, and forwards, captured from various angles and distances.

![image/png](https://huggingface.co/datasets/Voxel51/Football-Player-Segmentation/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 512 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Football-Player-Segmentation")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is specifically designed for computer vision tasks related to player detection and segmentation in football matches. The dataset contains images of players in different playing positions, such as goalkeepers, defenders, midfielders, and forwards, captured from various angles and distances. The images are annotated with pixel-level masks that indicate the playerâs location and segmentation boundaries, making it ideal for training deep learning models for player segmentation. The dataset is suitable for researchers and developers working on football-related computer vision applications, such as tracking players during a match or analysing player movements and behaviours. It is also useful for sports analysts and enthusiasts who want to explore player performance metrics and trends based on positional data. Overall, this football player segmentation dataset is a valuable resource for anyone interested in advancing computer vision techniques for sports analysis and tracking.

  * **Language(s) (NLP):** en

  * **License:** cc0-1.0




### Dataset Sources#

  * **Original Source:** [kaggle](https://www.kaggle.com/datasets/ihelon/football-player-segmentation)




## Uses#

  * Object Detection

  * Segmentation




## Dataset Structure#

The dataset contains two fields, `detections` and `segmentations` across 512 different samples

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
