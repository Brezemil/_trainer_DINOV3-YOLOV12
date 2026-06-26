---
source_url: https://docs.voxel51.com/integrations/open_images.html
---

# Open Images Integration#

Weâve collaborated with the team behind the [Open Images Dataset](https://storage.googleapis.com/openimages/web/download.html) to make it easy to download, visualize, and evaluate on the Open Images dataset natively in FiftyOne!

Note

Check out [this tutorial](tutorials__open_images.md) to see how you can use FiftyOne to download and evaluate models on Open Images.

![open-images-v6](../_images/open-images-v6.png)

## Loading Open Images#

The FiftyOne Dataset Zoo provides support for loading the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) and [Open Images V7](dataset_zoo__datasets__open_images_v7.md#dataset-zoo-open-images-v7) datasets.

Like all other zoo datasets, you can use [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") to download and load an Open Images V7 split into FiftyOne:
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4# Download and load the validation split of Open Images V7
    5dataset = foz.load_zoo_dataset("open-images-v7", split="validation")
    6
    7session = fo.launch_app(dataset)
    

Note

FiftyOne supports loading annotations for classification, detection, segmentation, and visual relationship tasks for the 600 boxable classes ([cf. dataset overview](https://storage.googleapis.com/openimages/web/factsfigures.html)).

By default, all label types are loaded, but you can customize this via the optional `label_types` argument (see below for details).

In addition, FiftyOne provides parameters that can be used to efficiently download specific subsets of the Open Images dataset, allowing you to quickly explore different slices of the dataset without downloading the entire split.

When performing partial downloads, FiftyOne will use existing downloaded data first if possible before resorting to downloading additional data from the web.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4#
     5# Load 50 random samples from the validation split of Open Images V7.
     6#
     7# Only the required images will be downloaded (if necessary).
     8# By default, all label types are loaded
     9#
    10
    11dataset = foz.load_zoo_dataset(
    12    "open-images-v7",
    13    split="validation",
    14    max_samples=50,
    15    shuffle=True,
    16)
    17
    18session = fo.launch_app(dataset)
    19
    20#
    21# Load detections and classifications for 25 samples from the
    22# validation split of Open Images V6 that contain fedoras and pianos
    23#
    24# Images that contain all `label_types` and `classes` will be
    25# prioritized first, followed by images that contain at least one of
    26# the required `classes`. If there are not enough images matching
    27# `classes` in the split to meet `max_samples`, only the available
    28# images will be loaded.
    29#
    30# Images will only be downloaded if necessary
    31#
    32
    33dataset = foz.load_zoo_dataset(
    34    "open-images-v6",
    35    split="validation",
    36    label_types=["detections", "classifications"],
    37    classes=["Fedora", "Piano"],
    38    max_samples=25,
    39)
    40
    41session.dataset = dataset
    42
    43#
    44# Load classifications and point labels for all samples from the
    45# validation split of Open Images V7 with class "Turtle" or "Tortoise".
    46#
    47# If there are not enough images matching classes` in the split to
    48# meet `max_samples`, only the available images will be loaded.
    49#
    50# Images will only be downloaded if necessary
    51#
    52
    53dataset = foz.load_zoo_dataset(
    54    "open-images-v7",
    55    split="validation",
    56    label_types=["points", "classifications"],
    57    classes=["Turtle", "Tortoise"],
    58)
    59
    60session.dataset = dataset
    

The following parameters are available to configure a partial download of Open Images V6 or Open Images V7 by passing them to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset"):

  * **split** (_None_) and **splits** (_None_): a string or list of strings, respectively, specifying the splits to load. Supported values are `("train", "test", "validation")`. If neither is provided, all available splits are loaded

  * **label_types** (_None_): a label type or list of label types to load. Supported values for Open Images V6 are `("detections", "classifications", "relationships", "segmentations")`. Open Images V7 also supports `"points"` labels. By default, all labels types are loaded

  * **classes** (_None_): a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded. You can use [`get_classes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_classes "fiftyone.utils.openimages.get_classes") and [`get_segmentation_classes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_segmentation_classes "fiftyone.utils.openimages.get_segmentation_classes") to see the available classes and segmentation classes, respectively

  * **attrs** (_None_): a string or list of strings specifying required relationship attributes to load. This parameter is only applicable if `label_types` contains `"relationships"`. If provided, only samples containing at least one instance of a specified attribute will be loaded. You can use [`get_attributes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_attributes "fiftyone.utils.openimages.get_attributes") to see the available attributes

  * **image_ids** (_None_): a list of specific image IDs to load. The IDs can be specified either as `<split>/<image-id>` or `<image-id>` strings. Alternatively, you can provide the path to a TXT (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_True_): whether to include the Open Images ID of each sample in the loaded labels

  * **only_matching** (_False_): whether to only load labels that match the `classes` or `attrs` requirements that you provide (True), or to load all labels for samples that match the requirements (False)

  * **num_workers** (_None_): the number of processes to use when downloading individual images. By default, `multiprocessing.cpu_count()` is used

  * **shuffle** (_False_): whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_): a random seed to use when shuffling

  * **max_samples** (_None_): a maximum number of samples to load per split. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements




Note

See [`OpenImagesV7Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.OpenImagesV6Dataset "fiftyone.zoo.datasets.base.OpenImagesV6Dataset") , [`OpenImagesV7Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.OpenImagesV7Dataset "fiftyone.zoo.datasets.base.OpenImagesV7Dataset") and [`OpenImagesDatasetImporter`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.OpenImagesDatasetImporter "fiftyone.utils.openimages.OpenImagesDatasetImporter") for complete descriptions of the optional keyword arguments that you can pass to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

## Open Images-style evaluation#

The [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") method provides builtin support for running [Open Images-style evaluation](https://storage.googleapis.com/openimages/web/evaluation.html).

In order to run Open Images-style evaluation, simply set the `method` parameter to `"open-images"`.

Note

FiftyOneâs implementation of Open Images-style evaluation matches the reference implementation available via the [TF Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).

### Overview#

Open Images-style evaluation provides additional features not found in [COCO-style evaluation](user_guide__evaluation.md#evaluating-detections-coco) that you may find useful when evaluating your custom datasets.

The two primary differences are:

  * **Non-exhaustive image labeling:** positive and negative sample-level [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields can be provided to indicate which object classes were considered when annotating the image. Predicted objects whose classes are not included in the sample-level labels for a sample are ignored. The names of these fields can be specified via the `pos_label_field` and `neg_label_field` parameters

  * **Class hierarchies:** If your dataset includes a [class hierarchy](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html), you can configure this evaluation protocol to automatically expand ground truth and/or predicted leaf classes so that all levels of the hierarchy can be [correctly evaluated](https://storage.googleapis.com/openimages/web/evaluation.html). You can provide a label hierarchy via the `hierarchy` parameter. By default, if you provide a hierarchy, then image-level label fields and ground truth detections will be expanded to incorporate parent classes (child classes for negative image-level labels). You can disable this feature by setting the `expand_gt_hierarchy` parameter to `False`. Alternatively, you can expand predictions by setting the `expand_pred_hierarchy` parameter to `True`




In addition, note that:

  * Like [VOC-style evaluation](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/devkit_doc_08-May-2010.pdf), only one IoU (default = 0.5) is used to calculate mAP. You can customize this value via the `iou` parameter

  * When dealing with crowd objects, Open Images-style evaluation dictates that if a crowd is matched with multiple predictions, each counts as one true positive when computing mAP




When you specify an `eval_key` parameter, a number of helpful fields will be populated on each sample and its predicted/ground truth objects:

  * True positive (TP), false positive (FP), and false negative (FN) counts for each sample are saved in top-level fields of each sample:
        
        TP: sample.<eval_key>_tp
        FP: sample.<eval_key>_fp
        FN: sample.<eval_key>_fn
        

  * The fields listed below are populated on each individual object instance; these fields tabulate the TP/FP/FN status of the object, the ID of the matching object (if any), and the matching IoU:
        
        TP/FP/FN: object.<eval_key>
              ID: object.<eval_key>_id
             IoU: object.<eval_key>_iou
        




Note

See [`OpenImagesEvaluationConfig`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig "fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig") for complete descriptions of the optional keyword arguments that you can pass to [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") when running Open Images-style evaluation.

### Example evaluation#

The example below demonstrates Open Images-style detection evaluation on the [quickstart dataset](dataset_zoo__datasets__quickstart.md#dataset-zoo-quickstart) from the Dataset Zoo:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6print(dataset)
     7
     8# Evaluate the objects in the `predictions` field with respect to the
     9# objects in the `ground_truth` field
    10results = dataset.evaluate_detections(
    11    "predictions",
    12    gt_field="ground_truth",
    13    method="open-images",
    14    eval_key="eval",
    15)
    16
    17# Get the 10 most common classes in the dataset
    18counts = dataset.count_values("ground_truth.detections.label")
    19classes = sorted(counts, key=counts.get, reverse=True)[:10]
    20
    21# Print a classification report for the top-10 classes
    22results.print_report(classes=classes)
    23
    24# Print some statistics about the total TP/FP/FN counts
    25print("TP: %d" % dataset.sum("eval_tp"))
    26print("FP: %d" % dataset.sum("eval_fp"))
    27print("FN: %d" % dataset.sum("eval_fn"))
    28
    29# Create a view that has samples with the most false positives first, and
    30# only includes false positive boxes in the `predictions` field
    31view = (
    32    dataset
    33    .sort_by("eval_fp", reverse=True)
    34    .filter_labels("predictions", F("eval") == "fp")
    35)
    36
    37# Visualize results in the App
    38session = fo.launch_app(view=view)
    
    
    
                   precision    recall  f1-score   support
    
           person       0.25      0.86      0.39       378
             kite       0.27      0.75      0.40        75
              car       0.18      0.80      0.29        61
             bird       0.20      0.51      0.28        51
           carrot       0.09      0.74      0.16        47
             boat       0.09      0.46      0.16        37
        surfboard       0.17      0.73      0.28        30
         airplane       0.36      0.83      0.50        24
    traffic light       0.32      0.79      0.45        24
          giraffe       0.36      0.91      0.52        23
    
        micro avg       0.21      0.79      0.34       750
        macro avg       0.23      0.74      0.34       750
     weighted avg       0.23      0.79      0.36       750
    

![quickstart-evaluate-detections-oi](../_images/quickstart_evaluate_detections_oi.png)

### mAP and PR curves#

You can easily compute mean average precision (mAP) and precision-recall (PR) curves using the results object returned by [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections"):

Note

FiftyOneâs implementation of Open Images-style evaluation matches the reference implementation available via the [TF Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5print(dataset)
     6
     7results = dataset.evaluate_detections(
     8    "predictions",
     9    gt_field="ground_truth",
    10    method="open-images",
    11)
    12
    13print(results.mAP())
    14# 0.599
    15
    16plot = results.plot_pr_curves(classes=["person", "dog", "car"])
    17plot.show()
    

![oi-pr-curve](../_images/oi_pr_curve.png)

### Confusion matrices#

You can also easily generate [confusion matrices](user_guide__evaluation.md#confusion-matrices) for the results of Open Images-style evaluations.

In order for the confusion matrix to capture anything other than false positive/negative counts, you will likely want to set the [`classwise`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig "fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig") parameter to `False` during evaluation so that predicted objects can be matched with ground truth objects of different classes.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5
     6# Perform evaluation, allowing objects to be matched between classes
     7results = dataset.evaluate_detections(
     8    "predictions",
     9    gt_field="ground_truth",
    10    method="open-images",
    11    classwise=False,
    12)
    13
    14# Generate a confusion matrix for the specified classes
    15plot = results.plot_confusion_matrix(classes=["car", "truck", "motorcycle"])
    16plot.show()
    

![oi-confusion-matrix](../_images/oi_confusion_matrix.png)

Note

Did you know? [Confusion matrices](user_guide__evaluation.md#confusion-matrices) can be attached to your [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") object and dynamically explored using FiftyOneâs [interactive plotting features](user_guide__plots.md#interactive-plots)!

## Open Images Challenge#

Since FiftyOneâs implementation of Open Images-style evaluation matches the reference implementation from the [TF Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) used in the [Open Images detection challenges](https://storage.googleapis.com/openimages/web/evaluation.html). you can use it to compute the official mAP for your model while also enjoying the benefits of working in the FiftyOne ecosystem, including [using views](https://docs.voxel51.com/user_guide/using_views.html#using-views) to manipulate your dataset and visually exploring your modelâs predictions in the [FiftyOne App](user_guide__app.md#fiftyone-app)!

In order to compute the official Open Images mAP for a model, your dataset **must** include the appropriate positive and negative sample-level labels, and you must provide the class hierarchy. Fortunately, when you load the Open Images dataset [from the FiftyOne Dataset Zoo](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6), all of the necessary information is automatically loaded for you!

The example snippet below loads the [Open Images V6](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) dataset and runs the official Open Images evaluation protocol on some mock model predictions:
    
    
     1import random
     2
     3import fiftyone as fo
     4import fiftyone.zoo as foz
     5
     6# Load some samples from the Open Images V6 dataset from the zoo
     7dataset = foz.load_zoo_dataset(
     8    "open-images-v6",
     9    "validation",
    10    max_samples=100,
    11    label_types=["detections", "classifications"],
    12)
    13
    14# Generate some fake predictions
    15for sample in dataset:
    16    predictions = sample["detections"].copy()
    17    for detection in predictions.detections:
    18        detection.confidence = random.random()
    19
    20    sample["predictions"] = predictions
    21    sample.save()
    22
    23# Evaluate your predictions via the official Open Images protocol
    24results = dataset.evaluate_detections(
    25    "predictions",
    26    gt_field="detections",
    27    method="open-images",
    28    pos_label_field="positive_labels",
    29    neg_label_field="negative_labels",
    30    hierarchy=dataset.info["hierarchy"],
    31
    32)
    33
    34# The official mAP for the results
    35print(results.mAP())
    

Most models trained on Open Images return the predictions for every class in the hierarchy. However, if your model does not, then you can set the [`expand_pred_hierarchy`](api__fiftyone.utils.eval.openimages.md#fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig "fiftyone.utils.eval.openimages.OpenImagesEvaluationConfig") parameter to `False` to automatically generate predictions for parent classes in the hierarchy for evaluation purposes.

Note

Check out [this recipe](recipes__adding_detections.md) to learn how to add your modelâs predictions to a FiftyOne Dataset.

## mAP protocol#

The Open Images mAP protocol is similar to [COCO-style mAP](integrations__coco.md#coco-map), with the primary differences being support for image-level labels, class hierarchies, and differences in the way that objects are matched to crowds.

The steps to compute Open Images-style mAP are detailed below.

**Preprocessing**

  * Filter ground truth and predicted objects by class (unless `classwise=False`)

  * Expand the ground truth predictions by duplicating every object and positive image-level label and modifying the class to include all parent classes in the class hierarchy. Negative image-level labels are expanded to include all child classes in the hierarchy for every label in the image

  * Sort predicted objects by confidence so that high confidence objects are matched first

  * Sort ground truth objects so that objects with `IsGroupOf=True` (the name of this attribute can be customized via the `iscrowd` parameter) are matched last

  * Compute IoU between every ground truth and predicted object within the same class (and between classes if `classwise=False`) in each image

  * Compute IoU between predictions and crowd objects as the intersection of both boxes divided by the area of the prediction only. A prediction fully inside the crowd box has an IoU of 1




**Matching**

Once IoUs have been computed, predictions and ground truth objects are matched to compute true positives, false positives, and false negatives:

  * For each class, start with the highest confidence prediction, match it to the ground truth object that it overlaps with the highest IoU. A prediction only matches if the IoU is above the specified `iou` threshold (default = 0.5)

  * If a prediction matched to a non-crowd gt object, it will not match to a crowd even if the IoU is higher

  * Multiple predictions can match to the same crowd ground truth object, but only one counts as a true positive, the others are ignored (unlike COCO). If the crowd is not matched by any prediction, it is a false negative

  * (Unlike COCO) If a prediction maximally overlaps with a non-crowd ground truth object that has already been matched with a higher confidence prediction, the prediction is marked as a false positive

  * If `classwise=False`, predictions can only match to crowds if they are of the same class




**Computing mAP**

  * (Unlike COCO) Only one IoU threshold (default = 0.5) is used to compute mAP

  * The next 6 steps are computed separately for each class:

  * Construct an array of true positives and false positives, sorted by confidence

  * Compute the cumulative sum of this TP FP array

  * Compute precision array by elementwise dividing the TP-FP-sum array by the total number of predictions up to that point

  * Compute recall array by elementwise dividing the TP-FP-sum array with the total number of ground truth objects for the class

  * Ensure that precision is a non-increasing array

  * Add values `0` and `1` to precision and recall arrays

  * (Unlike COCO) Precision values are not interpolated and all recall values are used to compute AP. This means that every class will produce a different number of precision and recall values depending on the number of true and false positives existing for that class

  * For every class that contains at least one ground truth object, compute the AP by averaging the precision values. Then compute mAP by averaging the AP values for each class




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
