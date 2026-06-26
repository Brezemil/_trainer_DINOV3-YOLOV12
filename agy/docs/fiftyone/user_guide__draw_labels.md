---
source_url: https://docs.voxel51.com/user_guide/draw_labels.html
---

# Drawing Labels on Samples#

FiftyOne provides native support for rendering annotated versions of image and video samples with [label fields](https://docs.voxel51.com/user_guide/using_datasets.html#using-labels) overlaid on the source media.

## Basic recipe#

The interface for drawing labels on samples is exposed via the Python library and the CLI. You can easily annotate one or more [label fields](https://docs.voxel51.com/user_guide/using_datasets.html#using-labels) on entire datasets or arbitrary subsets of your datasets that you have identified by constructing a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

You can draw labels on a collection of samples via the [`Dataset.draw_labels()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.draw_labels "fiftyone.core.dataset.Dataset.draw_labels") and [`DatasetView.draw_labels()`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView.draw_labels "fiftyone.core.view.DatasetView.draw_labels") methods:
    
    
     1import fiftyone as fo
     2
     3# The Dataset or DatasetView containing the samples you wish to draw
     4dataset_or_view = fo.load_dataset(...)
     5
     6# The directory to which to write the annotated media
     7output_dir = "/path/for/output"
     8
     9# The list of `Label` fields containing the labels that you wish to render on
    10# the source media (e.g., classifications or detections)
    11label_fields = ["ground_truth", "predictions"]  # for example
    12
    13# Render the labels!
    14dataset_or_view.draw_labels(output_dir, label_fields=label_fields)
    

You can rendered annotated media for an entire FiftyOne dataset [via the CLI](https://docs.voxel51.com/cli/index.html):
    
    
    # The name of the FiftyOne dataset to annotate
    NAME="your-dataset"
    
    # The directory to which to write the annotated files
    OUTPUT_DIR=/path/for/output
    
    # A comma-separated list of `Label` fields containing the labels that you wish
    # to render on the source media (e.g., classifications or detections)
    LABEL_FIELDS=ground_truth,predictions  # for example
    
    # Render the labels!
    fiftyone datasets draw $NAME --output-dir $OUTPUT_DIR --label-fields $LABEL_FIELDS
    

## Examples#

### Drawing labels on images#

The following snippet renders the ground truth and predicted labels on a few samples from the [quickstart dataset](dataset_zoo__datasets__quickstart.md#dataset-zoo-quickstart):
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart", max_samples=10)
     5
     6anno_image_paths = dataset.draw_labels(
     7    "/tmp/quickstart/draw-labels",
     8    label_fields=None,                  # all label fields
     9    # label_fields=["predictions"],     # only predictions
    10)
    11print(anno_image_paths)
    

### Drawing labels on videos#

The following snippet renders both sample-level and frame-level labels on a few videos from the [quickstart-video dataset](dataset_zoo__datasets__quickstart_video.md#dataset-zoo-quickstart-video):
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart-video", max_samples=2).clone()
     5
     6# Add some temporal detections
     7sample1 = dataset.first()
     8sample1["events"] = fo.TemporalDetections(
     9    detections=[
    10        fo.TemporalDetection(label="first", support=[31, 60]),
    11        fo.TemporalDetection(label="second", support=[90, 120]),
    12    ]
    13)
    14sample1.save()
    15
    16sample2 = dataset.last()
    17sample2["events"] = fo.TemporalDetections(
    18    detections=[
    19        fo.TemporalDetection(label="first", support=[16, 45]),
    20        fo.TemporalDetection(label="second", support=[75, 104]),
    21    ]
    22)
    23sample2.save()
    24
    25anno_video_paths = dataset.draw_labels(
    26    "/tmp/quickstart-video/draw-labels",
    27    label_fields=None,                      # all sample and frame labels
    28    # label_fields=["events"],              # only sample-level labels
    29    # label_fields=["frames.detections"],   # only frame-level labels
    30)
    31print(anno_video_paths)
    

## Individual samples#

You can also render annotated versions of individual samples directly by using the various methods exposed in the [`fiftyone.utils.annotations`](api__fiftyone.utils.annotations.md#module-fiftyone.utils.annotations "fiftyone.utils.annotations") module.

For example, you can render an annotated version of an image sample with [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") and [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") labels overlaid via [`draw_labeled_image()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.draw_labeled_image "fiftyone.utils.annotations.draw_labeled_image"):
    
    
     1import fiftyone as fo
     2import fiftyone.utils.annotations as foua
     3
     4# Example data
     5sample = fo.Sample(
     6    filepath="~/fiftyone/coco-2017/validation/data/000000000632.jpg",
     7    gt_label=fo.Classification(label="bedroom"),
     8    pred_label=fo.Classification(label="house", confidence=0.95),
     9    gt_objects=fo.Detections(
    10        detections=[
    11            fo.Detection(
    12                label="bed",
    13                bounding_box=[0.00510938, 0.55248447, 0.62692188, 0.43115942],
    14            ),
    15            fo.Detection(
    16                label="chair",
    17                bounding_box=[0.38253125, 0.47712215, 0.16362500, 0.18155280],
    18            ),
    19        ]
    20    ),
    21    pred_objects=fo.Detections(
    22        detections=[
    23            fo.Detection(
    24                label="bed",
    25                bounding_box=[0.10, 0.63, 0.50, 0.35],
    26                confidence=0.74,
    27            ),
    28            fo.Detection(
    29                label="chair",
    30                bounding_box=[0.39, 0.53, 0.15, 0.13],
    31                confidence=0.92,
    32            ),
    33        ]
    34    ),
    35)
    36
    37# The path to write the annotated image
    38outpath = "/path/for/image-annotated.jpg"
    39
    40# Render the annotated image
    41foua.draw_labeled_image(sample, outpath)
    

![image-annotated.jpg](../_images/example1.jpg)

  
Similarly, you can draw an annotated version of a video sample with its frame labels overlaid via [`draw_labeled_video()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.draw_labeled_video "fiftyone.utils.annotations.draw_labeled_video").

## Customizing label rendering#

You can customize the look-and-feel of the labels rendered by FiftyOne by providing a custom [`DrawConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.DrawConfig "fiftyone.utils.annotations.DrawConfig") to the relevant drawing method, such as [`SampleCollection.draw_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.draw_labels "fiftyone.core.collections.SampleCollection.draw_labels") or the underlying methods in the [`fiftyone.utils.annotations`](api__fiftyone.utils.annotations.md#module-fiftyone.utils.annotations "fiftyone.utils.annotations") module.

Consult the [`DrawConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.DrawConfig "fiftyone.utils.annotations.DrawConfig") docs for a complete description of the available parameters.

For example, the snippet below increases the font size and line thickness of the labels in the example above and includes the confidence of the predictions:
    
    
     1# Continuing from example above...
     2
     3# Customize annotation rendering
     4config = foua.DrawConfig(
     5    {
     6        "font_size": 24,
     7        "bbox_linewidth": 5,
     8        "show_all_confidences": True,
     9        "per_object_label_colors": False,
    10    }
    11)
    12
    13# Render the annotated image
    14foua.draw_labeled_image(sample, outpath, config=config)
    

![image-annotated.jpg](../_images/example2.jpg)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
