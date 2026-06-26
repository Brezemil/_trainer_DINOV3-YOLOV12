---
source_url: https://docs.voxel51.com/integrations/v7.html
---

# V7 Integration#

[V7](https://www.v7labs.com) is one of the leading image and video annotation tools available, and weâve made it easy to upload your data directly from FiftyOne to V7 for labeling.

Create a [V7 account](https://www.v7labs.com/sign-up) and follow these simple setup instructions to get up and running.

Note

Did you know? You can request, manage, and import annotations from within the FiftyOne App by installing the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation) plugin!

FiftyOne provides an API to upload data, define label schemas, and download annotations using V7, all programmatically in Python. All of the following label types are supported, for both image and video datasets:

  * [Classifications](https://docs.voxel51.com/user_guide/using_datasets.html#classification)

  * [Detections](https://docs.voxel51.com/user_guide/using_datasets.html#object-detection)

  * [Polygons](https://docs.voxel51.com/user_guide/using_datasets.html#polylines)

  * [Keypoints](https://docs.voxel51.com/user_guide/using_datasets.html#keypoints)


![v7-hero](../_images/v7-hero.jpg)

## Basic recipe#

The basic workflow to use V7 to add or edit labels on your FiftyOne datasets is as follows:

  1. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Explore the dataset using the [App](user_guide__app.md#fiftyone-app) or [dataset views](https://docs.voxel51.com/user_guide/using_views.html#using-views) to locate either unlabeled samples that you wish to annotate or labeled samples whose annotations you want to edit

  3. Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method on your dataset or view to upload the samples and optionally their existing labels to V7 by setting the parameter `backend="darwin"`

  4. In V7, perform the necessary annotation work

  5. Back in FiftyOne, load your dataset and use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to merge the annotations back into your FiftyOne dataset

  6. If desired, delete the V7 project and the record of the annotation run from your FiftyOne dataset




  
The example below demonstrates this workflow.

Note

You must create an account at <https://www.v7labs.com/sign-up> and follow the simple setup instructions in this section in order to run this example.

First, we create the annotation tasks in V7:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5# Step 1: Load your data into FiftyOne
     6
     7dataset = foz.load_zoo_dataset(
     8    "quickstart", dataset_name="v7-annotation-example"
     9)
    10dataset.persistent = True
    11
    12dataset.evaluate_detections(
    13    "predictions", gt_field="ground_truth", eval_key="eval"
    14)
    15
    16# Step 2: Locate a subset of your data requiring annotation
    17
    18# Create a view that contains only high confidence false positive model
    19# predictions, with samples containing the most false positives first
    20most_fp_view = (
    21    dataset
    22    .filter_labels("predictions", (F("confidence") > 0.8) & (F("eval") == "fp"))
    23    .sort_by(F("predictions.detections").length(), reverse=True)
    24)
    25
    26# Retrieve the sample with the most high confidence false positives
    27sample_id = most_fp_view.first().id
    28view = dataset.select(sample_id)
    29
    30# Step 3: Send samples to V7
    31
    32# A unique identifier for this run
    33anno_key = "v7_basic_recipe"
    34
    35label_schema = {
    36    "new_ground_truth": {
    37        "type": "detections",
    38        "classes": dataset.distinct("ground_truth.detections.label"),
    39    },
    40}
    41
    42view.annotate(
    43    anno_key,
    44    backend="darwin",
    45    label_schema=label_schema,
    46    launch_editor=True,
    47    dataset_slug=anno_key,
    48)
    49print(dataset.get_annotation_info(anno_key))
    50
    51# Step 4: Perform annotation in V7 and save the tasks
    

Then, once the annotation work is complete, we merge the annotations back into FiftyOne:
    
    
     1import fiftyone as fo
     2
     3anno_key = "v7_basic_recipe"
     4
     5# Step 5: Merge annotations back into FiftyOne dataset
     6
     7dataset = fo.load_dataset("v7-annotation-example")
     8dataset.load_annotations(anno_key)
     9
    10# Load the view that was annotated in the App
    11view = dataset.load_annotation_view(anno_key)
    12session = fo.launch_app(view=view)
    13
    14# Step 6: Cleanup
    15
    16# Delete tasks from V7
    17results = dataset.load_annotation_results(anno_key)
    18results.cleanup()
    19
    20# Delete run record (not the labels) from FiftyOne
    21dataset.delete_annotation_run(anno_key)
    

Note

See this section to see a variety of common V7 annotation patterns.

## Setup#

You can get started with V7 by [creating an account](https://www.v7labs.com/sign-up) and downloading an API key.

### Installing the V7 backend#

In order to use the V7 backend, you must install the `darwin_fiftyone` Python package:
    
    
    pip install darwin_fiftyone
    

and register the `darwin` backend with FiftyOne, which you can do either by setting the following environment variables:
    
    
    export FIFTYONE_ANNOTATION_BACKENDS=*,darwin
    export FIFTYONE_DARWIN_CONFIG_CLS=darwin_fiftyone.DarwinBackendConfig
    export FIFTYONE_DARWIN_API_KEY=XXXXXXXXX
    

or by adding the following parameters to your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "backends": {
            "darwin": {
                "config_cls": "darwin_fiftyone.DarwinBackendConfig",
                "api_key": "XXXXXXXXX"
            }
        }
    }
    

Note that this file may not exist if you havenât previously customized your annotation backends.

### Using the V7 backend#

By default, calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will use the [CVAT backend](integrations__cvat.md#cvat-integration).

To use the V7 backend, simply set the optional `backend` parameter of [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to `"darwin"`:
    
    
    1view.annotate(anno_key, backend="darwin", ...)
    

Alternatively, you can permanently configure FiftyOne to use the V7 backend by setting the `FIFTYONE_ANNOTATION_DEFAULT_BACKEND` environment variable:
    
    
    export FIFTYONE_ANNOTATION_DEFAULT_BACKEND=darwin
    

or by setting the `default_backend` parameter of your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "default_backend": "darwin"
    }
    

### Authentication#

In order to connect to V7, you must provide your API key, which can be done in a variety of ways.

**Environment variables (recommended)**

The recommended way to configure your V7 API key is to store it in the `FIFTYONE_DARWIN_API_KEY` environment variable. This is automatically accessed by FiftyOne whenever a connection to V7 is made.
    
    
    export FIFTYONE_DARWIN_API_KEY=...
    

**FiftyOne annotation config**

You can also store your credentials in your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "backends": {
            "darwin": {
                "api_key": ...,
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide your API key as a keyword argument each time you call methods like [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") and [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") that require connections to V7:
    
    
    1view.annotate(
    2    anno_key,
    3    backend="darwin",
    4    label_field="ground_truth",
    5    dataset_slug=anno_key,
    6    api_key=...,
    7)
    

## Requesting annotations#

Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method to send the samples and optionally existing labels in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to V7 for annotation.

The basic syntax is:
    
    
    1anno_key = "..."
    2view.annotate(anno_key, backend="darwin", ...)
    

The `anno_key` argument defines a unique identifier for the annotation run, and you will provide it to methods like [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`get_annotation_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`load_annotation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotation_results "fiftyone.core.collections.SampleCollection.load_annotation_results"), [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run"), and [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to manage the run in the future.

Note

Calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will upload the source media files to the V7 server.

In addition, [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") provides various parameters that you can use to customize the annotation tasks that you wish to be performed.

The following parameters are supported by all annotation backends:

  * **backend** (_None_): the annotation backend to use. Use `"darwin"` for the V7 backend. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * **media_field** (_âfilepathâ_): the sample field containing the path to the source media to upload

  * **launch_editor** (_False_): whether to launch the annotation backendâs editor after uploading the samples




The following parameters allow you to configure the labeling schema to use for your annotation tasks. See this section for more details:

  * **label_schema** (_None_): a dictionary defining the label schema to use. If this argument is provided, it takes precedence over `label_field` and `label_type`

  * **label_field** (_None_): a string indicating a new or existing label field to annotate

  * **label_type** (_None_): a string indicating the type of labels to annotate. The possible label types are:

    * `"classification"`: a single classification stored in [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") fields

    * `"classifications"`: multilabel classifications stored in [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields

    * `"detections"`: object detections stored in [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields

    * `"polygons"`: polygons stored in [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `True`

    * `"keypoints"`: keypoints stored in [`Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") fields

All new label fields must have their type specified via this argument or in `label_schema`

  * **classes** (_None_): a list of strings indicating the class options for `label_field` or all fields in `label_schema` without classes specified. All new label fields must have a class list provided via one of the supported methods. For existing label fields, if classes are not provided by this argument nor `label_schema`, the observed labels on your dataset are used

  * **allow_additions** (_True_): whether to allow new labels to be added. Only applicable when editing existing label fields

  * **allow_deletions** (_True_): whether to allow labels to be deleted. Only applicable when editing existing label fields

  * **allow_label_edits** (_True_): whether to allow the `label` attribute of existing labels to be modified. Only applicable when editing existing fields with `label` attributes

  * **allow_spatial_edits** (_True_): whether to allow edits to the spatial properties (bounding boxes, vertices, keypoints, etc) of labels. Only applicable when editing existing spatial label fields




  
In addition, the following V7-specific parameters can also be provided:

  * **dataset_slug** (_None_): the name of the dataset to use or create in Darwin. This is currently mandatory

  * **external_storage** (_None_): the sluggified name of a Darwin external storage to use. If provided, indicates that all files should be treated as external storage




### Label schema#

The `label_schema`, `label_field`, `label_type`, and `classes` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") allow you to define the annotation schema that you wish to be used.

The label schema may define new label field(s) that you wish to populate, and it may also include existing label field(s), in which case you can add, delete, or edit the existing labels on your FiftyOne dataset.

The `label_schema` argument is the most flexible way to define how to construct tasks in V7. In its most verbose form, it is a dictionary that defines the label type, annotation type, and possible classes for each label field:
    
    
     1anno_key = "..."
     2
     3label_schema = {
     4    "new_field": {
     5        "type": "classifications",
     6        "classes": ["class1", "class2"],
     7    },
     8}
     9
    10dataset.annotate(
    11    anno_key,
    12    backend="darwin",
    13    label_schema=label_schema,
    14    dataset_slug="dataset_slug",
    15)
    

Alternatively, if you are only editing or creating a single label field, you can use the `label_field`, `label_type`, and `classes` parameters to specify the components of the label schema individually:
    
    
     1anno_key = "..."
     2
     3label_field = "new_field",
     4label_type = "classifications"
     5classes = ["class1", "class2"]
     6
     7dataset.annotate(
     8    anno_key,
     9    backend="darwin",
    10    label_field=label_field,
    11    label_type=label_type,
    12    classes=classes,
    13    dataset_slug="dataset_slug",
    14)
    

When you are annotating existing label fields, you can omit some of these parameters from [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), as FiftyOne can infer the appropriate values to use:

  * **label_type** : if omitted, the [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type of the field will be used to infer the appropriate value for this parameter

  * **classes** : if omitted, the observed labels on your dataset will be used to construct a classes list




Warning

Annotating multiple fields is not yet supported by the `darwin` backend. Please check back soon!

### Label attributes#

Warning

Label attributes are not yet supported by the `darwin` backend. Please check back soon!

## Loading annotations#

After your annotations tasks in the annotation backend are complete, you can use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to download them and merge them back into your FiftyOne dataset.
    
    
    1view.load_annotations(anno_key)
    

The `anno_key` parameter is the unique identifier for the annotation run that you provided when calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"). You can use [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs") to see the available keys on a dataset.

Note

By default, calling [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") will not delete any information for the run from the annotation backend.

However, you can pass `cleanup=True` to delete the V7 dataset associated with the run after the annotations are downloaded.

Warning

The `dest_field` parameter of [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") is not yet supported by the `darwin` backend. Check back soon!

## Managing annotation runs#

FiftyOne provides a variety of methods that you can use to manage in-progress or completed annotation runs.

For example, you can call [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs") to see the available annotation keys on a dataset:
    
    
    1dataset.list_annotation_runs()
    

Or, you can use [`get_annotation_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_annotation_info "fiftyone.core.collections.SampleCollection.get_annotation_info") to retrieve information about the configuration of an annotation run:
    
    
    1info = dataset.get_annotation_info(anno_key)
    2print(info)
    

Use [`load_annotation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotation_results "fiftyone.core.collections.SampleCollection.load_annotation_results") to load the [`AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults") instance for an annotation run.

All results objects provide a [`cleanup()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults.cleanup "fiftyone.utils.annotations.AnnotationResults.cleanup") method that you can use to delete all information associated with a run from the annotation backend.
    
    
    1results = dataset.load_annotation_results(anno_key)
    2results.cleanup()
    

You can use [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run") to rename the annotation key associated with an existing annotation run:
    
    
    1dataset.rename_annotation_run(anno_key, new_anno_key)
    

Finally, you can use [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to delete the record of an annotation run from your FiftyOne dataset:
    
    
    1dataset.delete_annotation_run(anno_key)
    

Note

Calling [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") only deletes the **record** of the annotation run from your FiftyOne dataset; it will not delete any annotations loaded onto your dataset via [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), nor will it delete any associated information from the annotation backend.

## Examples#

This section demonstrates how to perform some common annotation workflows on a FiftyOne dataset using the V7 backend.

Note

All of the examples below assume you have configured your V7 backend as described in this section.

### Adding new label fields#

In order to annotate a new label field, you can provide the `label_field`, `label_type`, and `classes` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to define the annotation schema for the field:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "v7_new_field"
     8
     9view.annotate(
    10    anno_key,
    11    backend="darwin",
    12    label_field="new_classifications",
    13    label_type="classifications",
    14    classes=["dog", "cat", "person"],
    15    dataset_slug=anno_key,
    16    launch_editor=True,
    17)
    18print(dataset.get_annotation_info(anno_key))
    19
    20# Create annotations in V7
    21
    22dataset.load_annotations(anno_key, cleanup=True)
    23dataset.delete_annotation_run(anno_key)
    

Alternatively, you can use the `label_schema` argument to define the same labeling task:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "v7_new_field"
     8
     9label_schema = {
    10    "new_classifications": {
    11        "type": "classifications",
    12        "classes": ["dog", "cat", "person"],
    13    }
    14}
    15
    16view.annotate(
    17    anno_key,
    18    backend="darwin",
    19    label_schema=label_schema,
    20    dataset_slug=anno_key,
    21    launch_editor=True,
    22)
    23print(dataset.get_annotation_info(anno_key))
    24
    25# Create annotations in V7
    26
    27dataset.load_annotations(anno_key, cleanup=True)
    28dataset.delete_annotation_run(anno_key)
    

### Editing existing labels#

A common use case is to fix annotation mistakes that you discovered in your datasets through FiftyOne.

You can easily edit the labels in an existing field of your FiftyOne dataset by simply passing the name of the field via the `label_field` parameter of [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "v7_existing_field"
     8
     9view.annotate(
    10    anno_key,
    11    backend="darwin",
    12    label_field="ground_truth",
    13    dataset_slug=anno_key,
    14    launch_editor=True,
    15)
    16print(dataset.get_annotation_info(anno_key))
    17
    18# Modify/add/delete bounding boxes and their attributes in V7
    19
    20dataset.load_annotations(anno_key, cleanup=True)
    21dataset.delete_annotation_run(anno_key)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
