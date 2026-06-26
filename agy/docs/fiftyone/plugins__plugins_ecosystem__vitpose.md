---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/vitpose.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/vitpose-plugin)

# ViTPose Plugin#

This plugin essentially makes it easy to add human pose estimation capabilities to any FiftyOne dataset that already has person detections.

## Plugin Overview#

This plugin integrates ViTPose (a Vision Transformer-based pose estimation model) into FiftyOne, allowing users to detect human body keypoints in images that already have person bounding boxes detected.

  * Supports multiple ViTPose architectures

  * Hardware acceleration (CUDA/MPS) when available

  * Confidence threshold filtering

  * Delegation support for distributed processing

  * Handles normalized coordinate conversions

  * Integrates with FiftyOneâs Dataset and UI




## Note: This plugin makes assumptions.#

### It assumes you have bounding box detections on your dataset already.#

If you do not have bounding boxes on your Dataset already, you can add them quite easily, for example:
    
    
    from ultralytics import YOLO
    
    yolo_world_model = YOLO("yolov8x-worldv2.pt")  # or choose yolov8m/l-world.pt
    
    # Define custom classes
    yolo_world_model.set_classes(["person"])
    
    dataset.apply_model(
        yolo_world_model,
        label_field="bbox_detections"
    )
    

### It assumes you already have metadata computed on your dataset.#

If you donât already have metadata computed, you can do so as follows:
    
    
    dataset.compute_metadata()
    

### Supported Models#

This plugin supports all [currently available checkpoints](https://huggingface.co/collections/usyd-community/vitpose-677fcfd0a0b2b5c8f79c4335) (as of Jan 2025).

  * `usyd-community/vitpose-plus-small`

  * `usyd-community/vitpose-base`

  * `usyd-community/vitpose-base-simple`

  * `usyd-community/vitpose-plus-base`

  * `usyd-community/vitpose-plus-large`

  * `usyd-community/vitpose-plus-huge`

  * `usyd-community/vitpose-base-coco-aic-mpii`




## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone transformers
    

Then, install the plugin:
    
    
    fiftyone plugins download https://github.com/harpreetsahota204/vitpose-plugin
    

## Usage in FiftyOne App#

You can estimate poses using ViTPose directly through the FiftyOne App:

  1. Launch the FiftyOne App with your dataset

  2. Open the âOperators Browserâ by clicking on the Operator Browser icon above the sample grid or by typing backtick (`)

  3. Type âVitPose Human Pose Estimatorâ

  4. Configure the following parameters:

     * **ViTPose Model** : Select one of the supported models

     * **Bounding Box Field** : The field where your bounding box detections are

     * **Output Field** : Enter the name for the field to store key points

     * **Confidence Threshold** : Confidence threshold for keypoint detection

  5. Click âExecuteâ to compute keypoints for your dataset




## Operators#

### `vitpose_keypoint_estimator`#

Estimate keypoints for human pose estimation with VitPose

## Operator usage via SDK#

Once the plugin has been installed, you can instantiate the operator as follows:
    
    
    import fiftyone.operators as foo
    
    vitpose_operator = foo.get_operator("@harpreetsahota/vitpose/vitpose_keypoint_estimator")
    
    

You can then estimate poses on your dataset by running the operator with your desired parameters:
    
    
    # Run the operator on your dataset
    vitpose_operator(
        dataset,
        model_name="usyd-community/vitpose-plus-small",  # Select from one of the supported models
        bbox_field="bbox_field", # Name of the field where your bounding box detections are stored.
        output_field="vitpose_estimates",  # Name of the field to store the Keypoints in.
        confidence_threshold= 0.55 #Confidence threshold for keypoint detection
    )
    

If youâre running in a notebook, itâs recommended to launch a [Delegated operation](https://docs.voxel51.com/plugins/using_plugins.html#delegated-operations) by running `fiftyone delegated launch` in terminal, then run as follows:
    
    
    await vitpose_operator(
        dataset,
        model_name="usyd-community/vitpose-plus-small",
        bbox_field="bbox_field", 
        output_field="vitpose_estimates",
        confidence_threshold= 0.55
    )
    

# Citation#

You can read the paper here.
    
    
    @article{xu2022vitposesimplevisiontransformer,
      title={ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation},
      author={Yufei Xu and Jing Zhang and Qiming Zhang and Dacheng Tao},
      year={2022},
      eprint={2204.12484},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2204.12484}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
