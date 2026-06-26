---
source_url: https://docs.voxel51.com/labs/labs_ecosystem/box_combine.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-labs/tree/main/plugins/box_combine)

# Weighted Boxes Fusion#

A plugin that provides methods for ensembling bounding boxes from different object detection models directly within the [FiftyOne App](https://docs.voxel51.com), using [Weighted Boxes Fusion (WBF)](https://arxiv.org/abs/1910.13302).

Based on [ZFTurboâs Weighted-Boxes-Fusion](https://github.com/ZFTurbo/Weighted-Boxes-Fusion).

## Installation#
    
    
    fiftyone labs install @51labs/box_combine
    

## Usage#

  1. Launch the App:



    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

  1. Click the `Browse operations` action to open the Operators list

  2. Select the `box_combine` operator.




### Example workflow#

A common workflow is to run multiple object detection models on a dataset and then combine their predictions:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    # Run multiple detection models
    model1 = foz.load_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
    model2 = foz.load_zoo_model("retinanet-resnet50-fpn-coco-torch")
    
    dataset.apply_model(model1, label_field="det_faster_rcnn")
    dataset.apply_model(model2, label_field="det_retinanet")
    
    session = fo.launch_app(dataset)
    

In the app, select `det_faster_rcnn` and `det_retinanet` labels in the panel on the left. Open `box_combine` operator to fuse the predictions from the selected label into a single field using weighted boxes fusion method.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
