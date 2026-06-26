---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/bdd100k.html
---

# BDD100K#

The Berkeley Deep Drive (BDD) dataset is one of the largest and most diverse video datasets for autonomous vehicles.

The BDD100K dataset contains 100,000 video clips collected from more than 50,000 rides covering New York, San Francisco Bay Area, and other regions. The dataset contains diverse scene types such as city streets, residential areas, and highways. Furthermore, the videos were recorded in diverse weather conditions at different times of the day.

The videos are split into training (70K), validation (10K) and testing (20K) sets. Each video is 40 seconds long with 720p resolution and a frame rate of 30fps. The frame at the 10th second of each video is annotated for image classification, detection, and segmentation tasks.

This version of the dataset contains only the 100K images extracted from the videos as described above, together with the image classification, detection, and segmentation labels.

Note

In order to load the BDD100K dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        labels/
            bdd100k_labels_images_train.json
            bdd100k_labels_images_val.json
        images/
            100k/
                train/
                test/
                val/
    

You can register at <http://bdd-data.berkeley.edu> in order to get links to download the data.

**Details**

  * Dataset name: `bdd100k`

  * Dataset source: <http://bdd-data.berkeley.edu>

  * Dataset license: <http://bdd-data.berkeley.edu/download.html>

  * Dataset size: 7.10 GB

  * Tags: `image, multilabel, automotive, manual`

  * Supported splits: `train, validation, test`

  * ZooDataset class: [`BDD100KDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.BDD100KDataset "fiftyone.zoo.datasets.base.BDD100KDataset")




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4# The path to the source files that you manually downloaded
     5source_dir = "/path/to/dir-with-bdd100k-files"
     6
     7dataset = foz.load_zoo_dataset(
     8    "bdd100k",
     9    split="validation",
    10    source_dir=source_dir,
    11)
    12
    13session = fo.launch_app(dataset)
    
    
    
    # The path to the source files that you manually downloaded
    SOURCE_DIR="/path/to/dir-with-bdd100k-files"
    
    fiftyone zoo datasets load bdd100k --split validation \
        --kwargs "source_dir=${SOURCE_DIR}"
    
    fiftyone app launch bdd100k-validation
    

![bdd100k-validation](../../_images/bdd100k-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
