---
source_url: https://docs.voxel51.com/integrations/labelstudio.html
---

# Label Studio Integration#

[Label Studio](https://labelstud.io/) is a popular open-source data labeling tool with a friendly UI. The integration between FiftyOne and Label Studio allows you to easily upload your data directly from FiftyOne to Label Studio for labeling.

You can get started with Label Studio through a simple pip install to get a local server up and running. FiftyOne provides simple setup instructions that you can use to specify the necessary account credentials and server endpoint to use.

Note

Did you know? You can request, manage, and import annotations from within the FiftyOne App by installing the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation) plugin!

FiftyOne provides an API to create projects, upload data, define label schemas, and download annotations using Label Studio, all programmatically in Python. All of the following label types are supported for image datasets:

  * [Classification](https://docs.voxel51.com/user_guide/using_datasets.html#classification)

  * [Multilabel classification](https://docs.voxel51.com/user_guide/using_datasets.html#multilabel-classification)

  * [Detections](https://docs.voxel51.com/user_guide/using_datasets.html#object-detection)

  * [Instance segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#instance-segmentation)

  * [Polygons and polylines](https://docs.voxel51.com/user_guide/using_datasets.html#polylines)

  * [Keypoints](https://docs.voxel51.com/user_guide/using_datasets.html#keypoints)

  * [Scalar fields](https://docs.voxel51.com/user_guide/using_datasets.html#adding-sample-fields)

  * [Semantic segmentation](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation)




## Basic recipe#

The basic workflow to use Label Studio to add or edit labels on your FiftyOne datasets is as follows:

  1. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Explore the dataset using the [App](user_guide__app.md#fiftyone-app) or [dataset views](https://docs.voxel51.com/user_guide/using_views.html#using-views) to locate either unlabeled samples that you wish to annotate or labeled samples whose annotations you want to edit

  3. Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method on your dataset or view to upload the samples and optionally their existing labels to Label Studio by setting the parameter `backend="labelstudio"`

  4. In Label Studio, perform the necessary annotation work

  5. Back in FiftyOne, load your dataset and use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to merge the annotations back into your FiftyOne dataset

  6. If desired, delete the Label Studio tasks and the record of the annotation run from your FiftyOne dataset




  
The example below demonstrates this workflow.

Note

You must start by installing and setting up Label Studio as described in this section.

Note that you can also store your credentials to avoid entering them manually each time you interact with Label Studio.

First, we create the annotation tasks in Label Studio:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5# Step 1: Load your data into FiftyOne
     6
     7dataset = foz.load_zoo_dataset(
     8    "quickstart", dataset_name="ls-annotation-example"
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
    30# Step 3: Send samples to Label Studio
    31
    32# A unique identifier for this run
    33anno_key = "labelstudio_basic_recipe"
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
    44    backend="labelstudio",
    45    label_schema=label_schema,
    46    launch_editor=True,
    47)
    48print(dataset.get_annotation_info(anno_key))
    49
    50# Step 4: Perform annotation in Label Studio and save the tasks
    

Then, once the annotation work is complete, we merge the annotations back into FiftyOne:
    
    
     1import fiftyone as fo
     2
     3anno_key = "labelstudio_basic_recipe"
     4
     5# Step 5: Merge annotations back into FiftyOne dataset
     6
     7dataset = fo.load_dataset("ls-annotation-example")
     8dataset.load_annotations(anno_key)
     9
    10# Load the view that was annotated in the App
    11view = dataset.load_annotation_view(anno_key)
    12session = fo.launch_app(view=view)
    13
    14# Step 6: Cleanup
    15
    16# Delete tasks from Label Studio
    17results = dataset.load_annotation_results(anno_key)
    18results.cleanup()
    19
    20# Delete run record (not the labels) from FiftyOne
    21dataset.delete_annotation_run(anno_key)
    

## Setup#

The easiest way to get started with [Label Studio](https://github.com/heartexlabs/label-studio) is to install it locally and create an account.
    
    
    pip install label-studio
    
    # Launch it!
    label-studio
    

### Installing the Label Studio client#

In order to use the Label Studio backend, you must install the [Label Studio Python SDK](https://github.com/heartexlabs/label-studio-sdk):
    
    
    pip install label-studio-sdk
    

### Using the Label Studio backend#

By default, calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will use the [CVAT backend](integrations__cvat.md#cvat-integration).

To use the Label Studio backend, simply set the optional `backend` parameter of [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to `"labelstudio"`:
    
    
    1view.annotate(anno_key, backend="labelstudio", ...)
    

Alternatively, you can permanently configure FiftyOne to use the Label Studio backend by setting the `FIFTYONE_ANNOTATION_DEFAULT_BACKEND` environment variable:
    
    
    export FIFTYONE_ANNOTATION_DEFAULT_BACKEND=labelstudio
    

or by setting the `default_backend` parameter of your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "default_backend": "labelstudio"
    }
    

### Authentication#

In order to connect to a Label Studio server, you must provide your API key, which can be done in a variety of ways.

**Environment variables (recommended)**

The recommended way to configure your Label Studio API key is to store it in the `FIFTYONE_LABELSTUDIO_API_KEY` environment variable. This is automatically accessed by FiftyOne whenever a connection to Label Studio is made.
    
    
    export FIFTYONE_LABELSTUDIO_API_KEY=...
    

**FiftyOne annotation config**

You can also store your credentials in your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "backends": {
            "labelstudio": {
                "api_key": ...,
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide your API key as a keyword argument each time you call methods like [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") and [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") that require connections to Label Studio:
    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelstudio",
    4    label_field="ground_truth",
    5    api_key=...,
    6)
    

**Command line prompt**

If you have not stored your API key via another method, you will be prompted to enter it interactively in your shell each time you call a method that requires a connection to Label Studio:
    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelstudio",
    4    label_field="ground_truth",
    5    launch_editor=True,
    6)
    
    
    
    Please enter your API key.
    You can avoid this in the future by setting your `FIFTYONE_LABELSTUDIO_API_KEY` environment variable.
    API key: ...
    

### Server URL#

You can configure the URL to the desired Label Studio server in any of the following ways:

  * Set the `FIFTYONE_LABELSTUDIO_URL` environment variable:



    
    
    export FIFTYONE_LABELSTUDIO_URL=http://localhost:8080
    

  * Store the `url` of your server in your [annotation config](integrations__annotation.md#annotation-config) at `~/.fiftyone/annotation_config.json`:



    
    
    {
        "backends": {
            "labelstudio": {
                "url": "http://localhost:8080"
            }
        }
    }
    

  * Pass the `url` parameter manually each time you call [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):



    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelstudio",
    4    label_field="ground_truth",
    5    url="http://localhost:8080",
    6    api_key=...,
    7)
    

### Configuring local file storage#

If you are using FiftyOne on the same machine that is hosting Label Studio, then you can make use of the [local storage feature](https://labelstud.io/guide/storage#Local-storage) of Label Studio to avoid needing to copy your media.

To enable this, you just need to configure the `LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT` and `LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED` environment variables as defined in [the documentation](https://labelstud.io/guide/storage#Prerequisites-2).

Then when you request annotations, if all of the samples in your [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") reside in a subdirectory of the `LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT`, the media will not be copied over and only filepaths for you media will be used to create the Label Studio project.

## Requesting annotations#

Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method to send the samples and optionally existing labels in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to Label Studio for annotation.

The basic syntax is:
    
    
    1anno_key = "..."
    2view.annotate(anno_key, backend="labelstudio", ...)
    

The `anno_key` argument defines a unique identifier for the annotation run, and you will provide it to methods like [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`get_annotation_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`load_annotation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotation_results "fiftyone.core.collections.SampleCollection.load_annotation_results"), [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run"), and [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to manage the run in the future.

Note

Calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will upload the source media files to the Label Studio server.

In addition, [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") provides various parameters that you can use to customize the annotation tasks that you wish to be performed.

The following parameters are supported by all annotation backends:

  * **backend** (_None_): the annotation backend to use. Use `"labelstudio"` for the Label Studio backend. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * **media_field** (_âfilepathâ_): the sample field containing the path to the source media to upload

  * **launch_editor** (_False_): whether to launch the annotation backendâs editor after uploading the samples




The following parameters allow you to configure the labeling schema to use for your annotation tasks. See this section for more details:

  * **label_schema** (_None_): a dictionary defining the label schema to use. If this argument is provided, it takes precedence over `label_field` and `label_type`

  * **label_field** (_None_): a string indicating a new or existing label field to annotate

  * **label_type** (_None_): a string indicating the type of labels to annotate. The possible label types are:

    * `"classification"`: a single classification stored in [`Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") fields

    * `"classifications"`: multilabel classifications stored in [`Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields

    * `"detections"`: object detections stored in [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields

    * `"instances"`: instance segmentations stored in [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields with their [`mask`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection.mask "fiftyone.core.labels.Detection.mask") attributes populated

    * `"polylines"`: polylines stored in [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `False`

    * `"polygons"`: polygons stored in [`Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `True`

    * `"keypoints"`: keypoints stored in [`Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") fields

    * `"segmentation"`: semantic segmentations stored in [`Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") fields

All new label fields must have their type specified via this argument or in `label_schema`

  * **classes** (_None_): a list of strings indicating the class options for `label_field` or all fields in `label_schema` without classes specified. All new label fields must have a class list provided via one of the supported methods. For existing label fields, if classes are not provided by this argument nor `label_schema`, they are parsed from [`Dataset.classes`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.classes "fiftyone.core.dataset.Dataset.classes") or [`Dataset.default_classes`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_classes "fiftyone.core.dataset.Dataset.default_classes")

  * **mask_targets** (_None_): a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to semantic label strings. Only applicable when annotating semantic segmentations. All new label fields must have mask targets provided via one of the supported methods. For existing label fields, if mask targets are not provided by this argument nor `label_schema`, any applicable mask targets stored on your dataset will be used, if available




  
In addition, the following Label Studio-specific parameters from [`LabelStudioBackendConfig`](api__fiftyone.utils.labelstudio.md#fiftyone.utils.labelstudio.LabelStudioBackendConfig "fiftyone.utils.labelstudio.LabelStudioBackendConfig") can also be provided:

  * **project_name** (_None_): a name for the Label Studio project that will be created. The default is `"FiftyOne_<dataset_name>"`




### Label schema#

The `label_schema`, `label_field`, `label_type`, `classes`, and `mask_targets` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") allow you to define the annotation schema that you wish to be used.

The label schema may define new label field(s) that you wish to populate, and it may also include existing label field(s), in which case you can add, delete, or edit the existing labels on your FiftyOne dataset.

The `label_schema` argument is the most flexible way to define how to construct tasks in Label Studio. In its most verbose form, it is a dictionary that defines the label type, annotation type, and possible classes for each label field:
    
    
     1anno_key = "..."
     2
     3label_schema = {
     4    "new_field": {
     5        "type": "detections",
     6        "classes": ["class1", "class2"],
     7    },
     8    "existing_field": {
     9        "classes": ["class3", "class4"],
    10    },
    11}
    12
    13dataset.annotate(anno_key, backend="labelstudio", label_schema=label_schema)
    

Alternatively, if you are only editing or creating a single label field, you can use the `label_field`, `label_type`, `classes`, and `mask_targets` parameters to specify the components of the label schema individually:
    
    
     1anno_key = "..."
     2
     3label_field = "new_field",
     4label_type = "detections"
     5classes = ["class1", "class2"]
     6
     7dataset.annotate(
     8    anno_key,
     9    backend="labelstudio",
    10    label_field=label_field,
    11    label_type=label_type,
    12    classes=classes,
    13)
    

When you are annotating existing label fields, you can omit some of these parameters from [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), as FiftyOne can infer the appropriate values to use:

  * **label_type** : if omitted, the [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type of the field will be used to infer the appropriate value for this parameter

  * **classes** : if omitted, the observed labels on your dataset will be used to construct a classes list

  * **mask_targets** : if omitted for a semantic segmentation field, the mask targets from the [`mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") or [`default_mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") properties of your dataset will be used, if available




### Label attributes#

Warning

The Label Studio integration does not yet support [annotating label attributes](integrations__annotation.md#annotation-label-attributes).

## Loading annotations#

After your annotations tasks in the annotation backend are complete, you can use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to download them and merge them back into your FiftyOne dataset.
    
    
    1view.load_annotations(anno_key)
    

The `anno_key` parameter is the unique identifier for the annotation run that you provided when calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"). You can use [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs") to see the available keys on a dataset.

Note

By default, calling [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") will not delete any information for the run from the annotation backend.

However, you can pass `cleanup=True` to delete all information associated with the run from the backend after the annotations are downloaded.

You can use the optional `dest_field` parameter to override the taskâs label schema and instead load annotations into different field name(s) of your dataset. This can be useful, for example, when editing existing annotations, if you would like to do a before/after comparison of the edits that you import. If the annotation run involves multiple fields, `dest_field` should be a dictionary mapping label schema field names to destination field names.

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
    

In addition, the [`AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults") subclasses for each backend may provide additional utilities such as support for programmatically monitoring the status of the annotation tasks in the run.

You can use [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run") to rename the annotation key associated with an existing annotation run:
    
    
    1dataset.rename_annotation_run(anno_key, new_anno_key)
    

Finally, you can use [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to delete the record of an annotation run from your FiftyOne dataset:
    
    
    1dataset.delete_annotation_run(anno_key)
    

Note

Calling [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") only deletes the **record** of the annotation run from your FiftyOne dataset; it will not delete any annotations loaded onto your dataset via [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), nor will it delete any associated information from the annotation backend.

## Annotating videos#

Warning

The Label Studio integration does not currently support annotating videos.

## Acknowledgements#

Note

Special thanks to [Rustem Galiullin](https://github.com/Rusteam), [Ganesh Tata](https://github.com/tataganesh), and [Emil Zakirov](https://github.com/bonlime) for building this integration!

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
