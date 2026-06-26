---
source_url: https://docs.voxel51.com/labs/labs_ecosystem/click_segmentation.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-labs/tree/main/plugins/click_segmentation)

# Image segmentation via point prompts#

Image segmentation via point prompts is a `fiftyone-labs` features that lets users interactively add keypoints to an image and use these keypoints for generating segmentation masks via a promptable segmentation model. There are two main components in this feaure:

  1. The `click_segmentation` panel is an interactive tool for generating point prompts via clicks on the `Sample` modal. These point prompts can be input to a promptable segmentation model (such as Segment Anything Model) to create segmentation masks.

  2. The `segment_with_prompts` operator is a standalone operator that can be used to run a promptable segmentation model with either box or keypoint prompts saved in a sample field. The operator may be applied to the entire dataset or a subset of the dataset.




## Usage#

### Click To Segment Panel#
    
    
    import fiftyone.zoo as foz
    import fiftyone as fo
    
    dataset = foz.load_zoo_dataset("quickstart")
    # For a smoother experience, ensure that samples have metadata.
    if dataset.count("metadata") != len(dataset):
        dataset.compute_metadata()
    
    session = fo.launch_app(dataset)
    

_Select a sample and open Click To Segment panel_

![Open panel](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/open_panel.png)

_Enable capture mode by checking the box_

![Click-To-Segment panel](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/click_capture_enabled.png)

The panel has two modes of operation:

  * Multiple Click Capture: Users can save multiple sets of clicks and manually trigger segmentation.

  * Single Click Capture: Users can click on the sample modal and segmentation will auto-trigger.




#### Multiple Click Capture#

_In the Sample modal, add a set of clicks for airplane and save as keypoints_

![Keypoints for airplane](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/clicks_airplane.png)

_Add another set of clicks for sky and save as keypoints_

![Keypoints for sky](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/clicks_sky.png)

_Choose a segmentation model from FiftyOne model zoo and click on Segment with Keypoints button_

![Segmentation successful](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/seg_success_notification.png)

_Segmentation masks will be added to the Sample_

![Output segmentations for multiple clicks](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/output_multi_click_segmentation.png)

#### Single Click Capture#

_In the Click To Segment panel, enable single click segmentation by checking the box_

![Single Click Segmentation](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/single_click_mode.png)

_Add a click on the Sample modal to trigger auto-segmentation_

![Keypoints for sky](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/output_single_click_segmentation.png)

### Segment With Prompt Operator#

_Launch the Segment With Prompts operator from the dropdown operators menu_

![Segment-With-Prompts operator](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/open_seg_with_prompts_op.png)

_Add inputs and trigger execution_

![Segment-With-Prompts operator](https://raw.githubusercontent.com/voxel51/fiftyone-labs/main/plugins/click_segmentation/assets/seg_with_prompts_op.png)

**Delegated Operation** To run `Segment With Prompts` operator with delegated operation, see the instructions [here](https://docs.voxel51.com/plugins/using_plugins.html#delegated-operations). You can also enable delegated operation via _Click To Segment_ panel by checking the `Use delegated operation` checkbox next to _Segment With Keypoints_ button.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
