---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/lfw.html
---

# Labeled Faces in the Wild#

Labeled Faces in the Wild is a public benchmark for face verification, also known as pair matching.

The dataset contains 13,233 images of 5,749 peopleâs faces collected from the web. Each face has been labeled with the name of the person pictured. 1,680 of the people pictured have two or more distinct photos in the data set. The only constraint on these faces is that they were detected by the Viola-Jones face detector.

**Details**

  * Dataset name: `lfw`

  * Dataset source: <http://vis-www.cs.umass.edu/lfw>

  * Dataset size: 173.00 MB

  * Tags: `image, classification, facial-recognition`

  * Supported splits: `test, train`

  * ZooDataset class: [`LabeledFacesInTheWildDataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.LabeledFacesInTheWildDataset "fiftyone.zoo.datasets.base.LabeledFacesInTheWildDataset")




**Example usage**
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset("lfw", split="test")
    5
    6session = fo.launch_app(dataset)
    
    
    
    fiftyone zoo datasets load lfw --split test
    
    fiftyone app launch lfw-test
    

![lfw-test](../../_images/lfw-test.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
