---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/ucf101.html
---

# UCF101#

UCF101 is an action recognition data set of realistic action videos, collected from YouTube, having 101 action categories. This data set is an extension of UCF50 data set which has 50 action categories.

With 13,320 videos from 101 action categories, UCF101 gives the largest diversity in terms of actions and with the presence of large variations in camera motion, object appearance and pose, object scale, viewpoint, cluttered background, illumination conditions, etc, it is the most challenging data set to date. As most of the available action recognition data sets are not realistic and are staged by actors, UCF101 aims to encourage further research into action recognition by learning and exploring new realistic action categories.

The videos in 101 action categories are grouped into 25 groups, where each group can consist of 4-7 videos of an action. The videos from the same group may share some common features, such as similar background, similar viewpoint, etc.

**Details**

  * Dataset name: `ucf101`

  * Dataset source: <https://www.crcv.ucf.edu/research/data-sets/ucf101>

  * Dataset license: CC0-1.0

  * Dataset size: 6.48 GB

  * Tags: `video, action-recognition`

  * Supported splits: `train, test`

  * ZooDataset class: [`UCF101Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.UCF101Dataset "fiftyone.zoo.datasets.base.UCF101Dataset")




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3import fiftyone.utils.video as fouv
     4
     5dataset = foz.load_zoo_dataset("ucf101", split="test")
     6
     7# Re-encode source videos as H.264 MP4s so they can be viewed in the App
     8fouv.reencode_videos(dataset)
     9
    10session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load ucf101 --split test
    
    # Re-encode source videos as H.264 MP4s so they can be viewed in the App
    fiftyone utils transform-videos ucf101-test --reencode
    
    fiftyone app launch ucf101-test
    

Note

In order to work with video datasets, youâll need to have [ffmpeg installed](installation__troubleshooting.md#troubleshooting-video).

Also, if you donât already have a utility to uncompress `.rar` archives, you may need to install one. For example, on macOS:
    
    
    brew install rar
    

![ucf101-test](../../_images/ucf101-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
