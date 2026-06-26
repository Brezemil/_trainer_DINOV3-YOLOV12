---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/hmdb51.html
---

# HMDB51#

HMDB51 is an action recognition dataset containing a total of 6,766 clips distributed across 51 action classes.

**Details**

  * Dataset name: `hmdb51`

  * Dataset source: <https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database>

  * Dataset license: CC-BY-4.0

  * Dataset size: 2.16 GB

  * Tags: `video, action-recognition`

  * Supported splits: `train, test, other`

  * ZooDataset class: [`HMDB51Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.HMDB51Dataset "fiftyone.zoo.datasets.base.HMDB51Dataset")




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3import fiftyone.utils.video as fouv
     4
     5dataset = foz.load_zoo_dataset("hmdb51", split="test")
     6
     7# Re-encode source videos as H.264 MP4s so they can be viewed in the App
     8fouv.reencode_videos(dataset)
     9
    10session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load hmdb51 --split test
    
    # Re-encode source videos as H.264 MP4s so they can be viewed in the App
    fiftyone utils transform-videos hmdb51-test --reencode
    
    fiftyone app launch hmdb51-test
    

Note

In order to work with video datasets, youâll need to have [ffmpeg installed](installation__troubleshooting.md#troubleshooting-video).

![hmdb51-test](../../_images/hmdb51-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
