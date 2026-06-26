---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/screenparser.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/Burhan-Q/screenparser)

# ScreenParser for FiftyOne#

![ScreenSpot-Pro sample with ScreenParser inference results](https://github.com/user-attachments/assets/cc3f44db-a076-47b1-bd07-f309b831a9c9)   
Inference results in FiftyOne using ScreenParser on a sample from the [ScreenSpot-Pro dataset](https://huggingface.co/datasets/Voxel51/ScreenSpot). 

A [FiftyOne](https://docs.voxel51.com) remote model zoo source for [**ScreenParser**](https://huggingface.co/docling-project/ScreenParser), a YOLO11-L object detector fine-tuned by the [docling-project](https://huggingface.co/docling-project) on the [ScreenParse v2 dataset (~1.45M screenshots)](https://huggingface.co/datasets/docling-project/screenparse) to localize **55 UI element classes** (buttons, tables, navigation bars, text inputs, icons, etc.) in application and web screenshots.

ScreenParser is a standard Ultralytics YOLO model, so this integration uses FiftyOneâs built-in [`fiftyone.utils.ultralytics.FiftyOneYOLOModel`](https://docs.voxel51.com/integrations/ultralytics.html) wrapper, there is no custom inference code, only a `manifest.json` describing where to download the weights and how to deploy them.

## Requirements#
    
    
    pip install "fiftyone>=1.0" "ultralytics>=8.3.0"
    

## Usage#

Register this repository as a remote zoo model source, then load and apply the model like any other zoo model:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # 1. Register the remote source (one time)
    foz.register_zoo_model_source("https://github.com/Burhan-Q/screenparser")
    
    # 2. Download the weights (153 MB); load_zoo_model does this for you
    foz.download_zoo_model(
        "https://github.com/Burhan-Q/screenparser",
        model_name="docling-project/ScreenParser",
    )
    
    # 3. Load the model
    model = foz.load_zoo_model("docling-project/ScreenParser")
    
    # 4. Apply to a dataset of screenshots
    dataset = fo.Dataset.from_images_dir("/path/to/screenshots")
    dataset.apply_model(model, label_field="ui_elements")
    
    session = fo.launch_app(dataset)
    

Predictions are stored as `fiftyone.core.labels.Detections` in the `ui_elements` field.

### Inference settings#

The model was trained at **1280px** ; the manifest sets the recommended defaults of `imgsz=1280`, `conf=0.10`, `iou=0.10`. You can override the confidence threshold and other Ultralytics arguments at load time:
    
    
    model = foz.load_zoo_model(
        "docling-project/ScreenParser",
        confidence_thresh=0.25,
        overrides={"iou": 0.10, "imgsz": 1280},
    )
    

## Training Data & Detected Classes#

The current main checkpoint was trained on ScreenParse v2, which provides 1,447,100 high-quality training screenshots and 25,575,213 UI element annotations. The dataset uses filtered leaf-element annotations to reduce noisy nested boxes and includes multiple viewport resolutions.

### Limitations#

  * Produces bounding boxes and element labels only; it does not produce text content for detected elements. Pair it with OCR or ScreenVLM when text extraction is needed.

  * The model is trained on rendered web screenshots, so performance may vary on native desktop, mobile, or application screenshots outside the training distribution.


Expand for the full class list

  * Table

  * Column/Browser

  * Button

  * Utility Button

  * App Icon

  * Navigation Bar

  * Status Bar

  * Search Field

  * Toolbar

  * Tooltip

  * Video

  * Tab Bar

  * Side Bar

  * Slider

  * Picker

  * ContextMenu

  * DockMenu

  * EditMenu

  * Image

  * Scroll

  * Switch

  * File Icon

  * Chart

  * Window

  * Screen

  * List

  * List Item

  * PopUp Menu

  * Steppers

  * Toggles

  * Text Input

  * Rating Indicator

  * Checkbox

  * Radiobox

  * Select

  * Avatar

  * Badge

  * Alert

  * Progress bar

  * Bottom navigation

  * Breadcrumb

  * Page control

  * Link

  * Menu

  * Pagination

  * Tab

  * Search Bar

  * Date-Time picker

  * Calendar

  * Text

  * Heading

  * Code snippet

  * Carousel

  * Notification

  * Logo




## License#

The ScreenParser FiftyOne integration source is released under the **Apache-2.0** license. See the [model card](https://huggingface.co/docling-project/ScreenParser) for details about the docling-project license of the model weights.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
