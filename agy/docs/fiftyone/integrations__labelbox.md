---
source_url: https://docs.voxel51.com/integrations/labelbox.html
---

# Labelbox Integration#

[Labelbox](https://labelbox.com/) is one of the most popular cloud-based image and video annotation tools available, and weâve made it easy to upload your data directly from FiftyOne to Labelbox for labeling.

You can create a [free Labelbox account](https://app.labelbox.com/signin) to upload and annotate raw data in the user-friendly Labelbox editor. FiftyOne provides simple setup instructions that you can use to specify the necessary API key and server endpoint to use.

Note

Did you know? You can request, manage, and import annotations from within the FiftyOne App by installing the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation) plugin!

FiftyOne provides an API to create projects, upload data, define label schemas, and download annotations using Labelbox, all programmatically in Python. All of the following label types are supported, for both image and video datasets:

  * [Classifications](https://docs.voxel51.com/user_guide/using_datasets.html#classification)

  * [Detections](https://docs.voxel51.com/user_guide/using_datasets.html#object-detection)

  * [Instance segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#instance-segmentation)

  * [Polygons and polylines](https://docs.voxel51.com/user_guide/using_datasets.html#polylines)

  * [Keypoints](https://docs.voxel51.com/user_guide/using_datasets.html#keypoints)

  * [Scalar fields](https://docs.voxel51.com/user_guide/using_datasets.html#adding-sample-fields)

  * [Semantic segmentation](https://docs.voxel51.com/user_guide/using_datasets.html#semantic-segmentation)


![labelbox-video](../_images/labelbox_video.png)

## Basic recipe#

The basic workflow to use Labelbox to add or edit labels on your FiftyOne datasets is as follows:

  1. [Load a dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Explore the dataset using the [App](user_guide__app.md#fiftyone-app) or [dataset views](https://docs.voxel51.com/user_guide/using_views.html#using-views) to locate either unlabeled samples that you wish to annotate or labeled samples whose annotations you want to edit

  3. Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method on your dataset or view to upload the samples and optionally their existing labels to Labelbox by setting the parameter `backend="labelbox"`

  4. In Labelbox, perform the necessary annotation work

  5. Back in FiftyOne, load your dataset and use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to merge the annotations back into your FiftyOne dataset

  6. If desired, delete the Labelbox tasks and the record of the annotation run from your FiftyOne dataset




  
The example below demonstrates this workflow.

Note

You must create an account at [labelbox.com](https://labelbox.com) in order to run this example.

Note that you can store your credentials as described in this section to avoid entering them manually each time you interact with Labelbox.

Youâll also need to install the [Labelbox Python client](https://github.com/Labelbox/labelbox-python):
    
    
    pip install labelbox
    

First, we create the annotation tasks in Labelbox:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5# Step 1: Load your data into FiftyOne
     6
     7dataset = foz.load_zoo_dataset(
     8    "quickstart", dataset_name="lb-annotation-example"
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
    30# Step 3: Send samples to Labelbox
    31
    32# A unique identifier for this run
    33anno_key = "labelbox_basic_recipe"
    34
    35label_schema = {
    36    "new_ground_truth": {
    37        "type": "detections",
    38        "classes": dataset.distinct("ground_truth.detections.label"),
    39        "attributes": {
    40            "iscrowd": {
    41                "type": "radio",
    42                "values": [True, False],
    43            },
    44        },
    45    },
    46}
    47
    48view.annotate(
    49    anno_key,
    50    backend="labelbox",
    51    label_schema=label_schema,
    52    launch_editor=True,
    53)
    54print(dataset.get_annotation_info(anno_key))
    55
    56# Step 4: Perform annotation in Labelbox and save the tasks
    

Then, once the annotation work is complete, we merge the annotations back into FiftyOne:
    
    
     1import fiftyone as fo
     2
     3anno_key = "labelbox_basic_recipe"
     4
     5# Step 5: Merge annotations back into FiftyOne dataset
     6
     7dataset = fo.load_dataset("lb-annotation-example")
     8dataset.load_annotations(anno_key)
     9
    10# Load the view that was annotated in the App
    11view = dataset.load_annotation_view(anno_key)
    12session = fo.launch_app(view=view)
    13
    14# Step 6: Cleanup
    15
    16# Delete tasks from Labelbox
    17results = dataset.load_annotation_results(anno_key)
    18results.cleanup()
    19
    20# Delete run record (not the labels) from FiftyOne
    21dataset.delete_annotation_run(anno_key)
    

Note

See this section to see a variety of common Labelbox annotation patterns.

## Setup#

FiftyOne supports both [standard Labelbox cloud accounts](https://app.labelbox.com/signin) and [on-premise Labelbox deployments](https://docs.labelbox.com/docs/labelbox-on-premises).

The easiest way to get started is to use [app.labelbox.com](https://app.labelbox.com), which simply requires creating an account and then providing your API key as shown below.

### Installing the Labelbox client#

In order to use the Labelbox backend, you must install the [Labelbox Python client](https://github.com/Labelbox/labelbox-python):
    
    
    pip install labelbox
    

### Using the Labelbox backend#

By default, calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will use the [CVAT backend](integrations__cvat.md#cvat-integration).

To use the Labelbox backend, simply set the optional `backend` parameter of [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to `"labelbox"`:
    
    
    1view.annotate(anno_key, backend="labelbox", ...)
    

Alternatively, you can permanently configure FiftyOne to use the Labelbox backend by setting the `FIFTYONE_ANNOTATION_DEFAULT_BACKEND` environment variable:
    
    
    export FIFTYONE_ANNOTATION_DEFAULT_BACKEND=labelbox
    

or by setting the `default_backend` parameter of your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "default_backend": "labelbox"
    }
    

### Authentication#

In order to connect to a Labelbox server, you must provide your API key, which can be done in a variety of ways.

**Environment variables (recommended)**

The recommended way to configure your Labelbox API key is to store it in the `FIFTYONE_LABELBOX_API_KEY` environment variable. This is automatically accessed by FiftyOne whenever a connection to Labelbox is made.
    
    
    export FIFTYONE_LABELBOX_API_KEY=...
    

**FiftyOne annotation config**

You can also store your credentials in your [annotation config](integrations__annotation.md#annotation-config) located at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "backends": {
            "labelbox": {
                "api_key": ...,
            }
        }
    }
    

Note that this file will not exist until you create it.

**Keyword arguments**

You can manually provide your API key as a keyword argument each time you call methods like [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") and [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") that require connections to Labelbox:
    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelbox",
    4    label_field="ground_truth",
    5    api_key=...,
    6)
    

**Command line prompt**

If you have not stored your API key via another method, you will be prompted to enter it interactively in your shell each time you call a method that requires a connection to Labelbox:
    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelbox",
    4    label_field="ground_truth",
    5    launch_editor=True,
    6)
    
    
    
    Please enter your API key.
    You can avoid this in the future by setting your `FIFTYONE_LABELBOX_API_KEY` environment variable.
    API key: ...
    

### On-premises servers#

If you have an [on-premises Labelbox server](https://docs.labelbox.com/docs/labelbox-on-premises), you can configure the URL of your server in any of the following ways:

  * Set the `FIFTYONE_LABELBOX_URL` environment variable:



    
    
    export FIFTYONE_LABELBOX_URL=http://localhost:8080
    

  * Store the `url` of your server in your [annotation config](integrations__annotation.md#annotation-config) at `~/.fiftyone/annotation_config.json`:



    
    
    {
        "backends": {
            "labelbox": {
                "url": "http://localhost:8080"
            }
        }
    }
    

  * Pass the `url` parameter manually each time you call [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):



    
    
    1view.annotate(
    2    anno_key,
    3    backend="labelbox",
    4    label_field="ground_truth",
    5    url="http://localhost:8080",
    6    api_key=...,
    7)
    

## Requesting annotations#

Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method to send the samples and optionally existing labels in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to Labelbox for annotation.

The basic syntax is:
    
    
    1anno_key = "..."
    2view.annotate(anno_key, backend="labelbox", ...)
    

The `anno_key` argument defines a unique identifier for the annotation run, and you will provide it to methods like [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`get_annotation_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`load_annotation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotation_results "fiftyone.core.collections.SampleCollection.load_annotation_results"), [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run"), and [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to manage the run in the future.

Note

Calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will upload the source media files to the Labelbox server.

In addition, [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") provides various parameters that you can use to customize the annotation tasks that you wish to be performed.

The following parameters are supported by all annotation backends:

  * **backend** (_None_): the annotation backend to use. Use `"labelbox"` for the Labelbox backend. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

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

    * `"scalar"`: scalar labels stored in [`IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField"), [`FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField"), [`StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField"), or [`BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") fields

All new label fields must have their type specified via this argument or in `label_schema`

  * **classes** (_None_): a list of strings indicating the class options for `label_field` or all fields in `label_schema` without classes specified. All new label fields must have a class list provided via one of the supported methods. For existing label fields, if classes are not provided by this argument nor `label_schema`, the observed labels on your dataset are used

  * **attributes** (_True_): specifies the label attributes of each label field to include (other than their `label`, which is always included) in the annotation export. Can be any of the following:

    * `True`: export all label attributes

    * `False`: donât export any custom label attributes

    * a list of label attributes to export

    * a dict mapping attribute names to dicts specifying the `type`, `values`, and `default` for each attribute

If a `label_schema` is also provided, this parameter determines which attributes are included for all fields that do not explicitly define their per-field attributes (in addition to any per-class attributes)

  * **mask_targets** (_None_): a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to semantic label strings. Only applicable when annotating semantic segmentations. All new label fields must have mask targets provided via one of the supported methods. For existing label fields, if mask targets are not provided by this argument nor `label_schema`, any applicable mask targets stored on your dataset will be used, if available

  * **allow_additions** (_True_): whether to allow new labels to be added. Only applicable when editing existing label fields

  * **allow_deletions** (_True_): whether to allow labels to be deleted. Only applicable when editing existing label fields

  * **allow_label_edits** (_True_): whether to allow the `label` attribute of existing labels to be modified. Only applicable when editing existing fields with `label` attributes

  * **allow_index_edits** (_True_): whether to allow the `index` attribute of existing video tracks to be modified. Only applicable when editing existing frame fields with `index` attributes

  * **allow_spatial_edits** (_True_): whether to allow edits to the spatial properties (bounding boxes, vertices, keypoints, masks, etc) of labels. Only applicable when editing existing spatial label fields




  
In addition, the following Labelbox-specific parameters from [`LabelboxBackendConfig`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxBackendConfig "fiftyone.utils.labelbox.LabelboxBackendConfig") can also be provided:

  * **project_name** (_None_): a name for the Labelbox project that will be created. The default is `"FiftyOne_<dataset_name>"`

  * **members** (None): an optional list of `(email, role)` tuples specifying the email addresses and roles of users to add to the project. If a user is not a member of the projectâs organization, an email invitation will be sent to them. The supported roles are `["LABELER", "REVIEWER", "TEAM_MANAGER", "ADMIN"]`

  * **classes_as_attrs** (_True_): whether to show every object class at the top level of the editor (False) or whether to show the label field at the top level and annotate the class as a required attribute of each object (True)

  * **export_version** (_âv2â_): the Labelbox export format and API version to use. Supported values are `("v1", "v2")`




Note

See this section for details about editing existing labels.

### Label schema#

The `label_schema`, `label_field`, `label_type`, `classes`, `attributes`, and `mask_targets` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") allow you to define the annotation schema that you wish to be used.

The label schema may define new label field(s) that you wish to populate, and it may also include existing label field(s), in which case you can add, delete, or edit the existing labels on your FiftyOne dataset.

The `label_schema` argument is the most flexible way to define how to construct tasks in Labelbox. In its most verbose form, it is a dictionary that defines the label type, annotation type, possible classes, and possible attributes for each label field:
    
    
     1anno_key = "..."
     2
     3label_schema = {
     4    "new_field": {
     5        "type": "classifications",
     6        "classes": ["class1", "class2"],
     7        "attributes": {
     8            "attr1": {
     9                "type": "checkbox",
    10                "values": ["val1", "val2"],
    11            },
    12            "attr2": {
    13                "type": "radio",
    14                "values": [True, False],
    15            }
    16        },
    17    },
    18    "existing_field": {
    19        "classes": ["class3", "class4"],
    20        "attributes": {
    21            "attr3": {
    22                "type": "text",
    23            }
    24        }
    25    },
    26}
    27
    28dataset.annotate(anno_key, backend="labelbox", label_schema=label_schema)
    

You can also define class-specific attributes by setting elements of the `classes` list to dicts that specify groups of `classes` and their corresponding `attributes`. For example, in the configuration below, `attr1` only applies to `class1` and `class2` while `attr2` applies to all classes:
    
    
     1anno_key = "..."
     2
     3label_schema = {
     4    "new_field": {
     5        "type": "detections",
     6        "classes": [
     7            {
     8                "classes": ["class1", "class2"],
     9                "attributes": {
    10                    "attr1": {
    11                        "type": "radio",
    12                        "values": ["val1", "val2"],
    13                    }
    14                 }
    15            },
    16            "class3",
    17            "class4",
    18        ],
    19        "attributes": {
    20            "attr2": {
    21                "type": "radio",
    22                "values": [True, False],
    23            }
    24        },
    25    },
    26}
    27
    28dataset.annotate(anno_key, backend="labelbox", label_schema=label_schema)
    

Alternatively, if you are only editing or creating a single label field, you can use the `label_field`, `label_type`, `classes`, `attributes`, and `mask_targets` parameters to specify the components of the label schema individually:
    
    
     1anno_key = "..."
     2
     3label_field = "new_field",
     4label_type = "classifications"
     5classes = ["class1", "class2"]
     6
     7# These are optional
     8attributes = {
     9    "attr1": {
    10        "type": "radio",
    11        "values": ["val1", "val2"],
    12    },
    13    "attr2": {
    14        "type": "radio",
    15        "values": [True, False],
    16    }
    17}
    18
    19dataset.annotate(
    20    anno_key,
    21    backend="labelbox",
    22    label_field=label_field,
    23    label_type=label_type,
    24    classes=classes,
    25    attributes=attributes,
    26)
    

When you are annotating existing label fields, you can omit some of these parameters from [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), as FiftyOne can infer the appropriate values to use:

  * **label_type** : if omitted, the [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type of the field will be used to infer the appropriate value for this parameter

  * **classes** : if omitted, the observed labels on your dataset will be used to construct a classes list

  * **mask_targets** : if omitted for a semantic segmentation field, the mask targets from the [`mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") or [`default_mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") properties of your dataset will be used, if available




Note

See this section for details about editing existing labels.

### Label attributes#

The `attributes` parameter allows you to configure whether [custom attributes](https://docs.voxel51.com/user_guide/using_datasets.html#using-labels) beyond the default `label` attribute are included in the annotation tasks.

When adding new label fields for which you want to include attributes, you must use the dictionary syntax demonstrated below to define the schema of each attribute that you wish to label:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "occluded": {
     5        "type": "radio",
     6        "values": [True, False],
     7    },
     8    "weather": {
     9        "type": "checkbox",
    10        "values": ["cloudy", "sunny", "overcast"],
    11    },
    12    "caption": {
    13        "type": "text",
    14    }
    15}
    16
    17view.annotate(
    18    anno_key,
    19    backend="labelbox",
    20    label_field="new_field",
    21    label_type="detections",
    22    classes=["dog", "cat", "person"],
    23    attributes=attributes,
    24)
    

You can always omit this parameter if you do not require attributes beyond the default `label`.

For Labelbox, the following `type` values are supported:

  * `text`: a free-form text box. In this case, `values` is unused

  * `radio`: a radio button list UI. In this case, `values` is required

  * `checkbox`: a list of checkboxes. In this case, `values` is required




When you are annotating existing label fields, the `attributes` parameter can take additional values:

  * `True` (default): export all custom attributes observed on the existing labels, using their observed values to determine the appropriate UI type and possible values, if applicable

  * `False`: do not include any custom attributes in the export

  * a list of custom attributes to include in the export

  * a full dictionary syntax described above




Note that only scalar-valued label attributes are supported. Other attribute types like lists, dictionaries, and arrays will be omitted.

Note

Labelbox does not support default values for attributes, so the `default` key [described here](integrations__annotation.md#annotation-label-attributes) will be ignored if included in label schemas provided when annotating with Labelbox.

### Video label attributes#

When annotating spatiotemporal objects in videos, each object attribute specification can include a `mutable` property that controls whether the attributeâs value can change between frames for each object:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "type": {
     5        "type": "checkbox",
     6        "values": ["sedan", "suv", "truck"],
     7        "mutable": False,
     8    },
     9    "occluded": {
    10        "type": "radio",
    11        "values": [True, False],
    12        "mutable": True,
    13    },
    14}
    15
    16view.annotate(
    17    anno_key,
    18    backend="labelbox",
    19    label_field="frames.new_field",
    20    label_type="detections",
    21    classes=["vehicle"],
    22    attributes=attributes,
    23)
    

The meaning of the `mutable` attribute is defined as follows:

  * `True` (default): the attribute is dynamic and can have a different value for every frame in which the object track appears

  * `False`: the attribute is static and is the same for every frame in which the object track appears (**Not yet supported**)




## Loading annotations#

After your annotations tasks in the annotation backend are complete, you can use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to download them and merge them back into your FiftyOne dataset.
    
    
    1view.load_annotations(anno_key)
    

The `anno_key` parameter is the unique identifier for the annotation run that you provided when calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"). You can use [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs") to see the available keys on a dataset.

Note

By default, calling [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") will not delete any information for the run from the annotation backend.

However, you can pass `cleanup=True` to delete all information associated with the run from the backend after the annotations are downloaded. Specifically, it will delete the project and ontology associated with this annotation run. Data rows are not deleted since they can be reused by other annotation runs.

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

## Examples#

This section demonstrates how to perform some common annotation workflows on a FiftyOne dataset using the Labelbox backend.

Note

All of the examples below assume you have configured your Labelbox server and API key as described in this section.

### Adding new label fields#

In order to annotate a new label field, you can provide the `label_field`, `label_type`, and `classes` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to define the annotation schema for the field:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_new_field"
     8
     9view.annotate(
    10    anno_key,
    11    backend="labelbox",
    12    label_field="new_classifications",
    13    label_type="classifications",
    14    classes=["dog", "cat", "person"],
    15    launch_editor=True,
    16)
    17print(dataset.get_annotation_info(anno_key))
    18
    19# Create annotations in Labelbox
    20
    21dataset.load_annotations(anno_key, cleanup=True)
    22dataset.delete_annotation_run(anno_key)
    

Alternatively, you can use the `label_schema` argument to define the same labeling task:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_new_field"
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
    18    backend="labelbox",
    19    label_schema=label_schema,
    20    launch_editor=True,
    21)
    22print(dataset.get_annotation_info(anno_key))
    23
    24# Create annotations in Labelbox
    25
    26dataset.load_annotations(anno_key, cleanup=True)
    27dataset.delete_annotation_run(anno_key)
    

![labelbox-tag](../_images/labelbox_tag.png)

### Editing labels with a free Labelbox account#

A common use case is to fix annotation mistakes that you discovered in your datasets through FiftyOne.

If you have a paid Labelbox account with access to Labelboxâs [Model Assisted Labeling](https://docs.labelbox.com/docs/model-assisted-labeling) feature, see this section for the recommended workflow for editing existing labels.

For free Labelbox users, one possible workflow for editing existing labels is the following:

  * [Tag the labels](user_guide__app.md#app-tagging) that need editing in FiftyOne

  * Use FiftyOne to construct the label schema for the existing label field

  * Upload the samples containing the tagged labels to Labelbox using [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") using a new (temporary) label field to hold the edited labels

  * Perform the annotation work in Labelbox, and download the results

  * Use the FiftyOne App to compare the newly loaded labels with the previously tagged labels to make sure youâre happy with the edits

  * Use [`merge_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.merge_labels "fiftyone.core.collections.SampleCollection.merge_labels") to merge edits into the original label field and then delete the tagged labels that you edited




The example snippet below demonstrates this workflow:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7session = fo.launch_app(view=view)
     8
     9# In the App, tag some ground truth labels with the "edit" tag...
    10
    11# Create view that only contains samples having labels with the "edit" tag
    12edit_view = view.match_labels(tags="edit")
    13
    14#
    15# Create an annotation run to reannotate the chosen samples in a new
    16# `ground_truth_edits` field
    17#
    18
    19anno_key = "labelbox_edit_labels"
    20
    21label_schema = {
    22    "ground_truth_edits": {
    23        "type": "detections",
    24        "classes": dataset.distinct("ground_truth.detections.label"),
    25        "attributes": {
    26            "iscrowd": {
    27                "type": "radio",
    28                "values": [True, False],
    29            }
    30        }
    31    }
    32}
    33
    34edit_view.annotate(
    35    anno_key,
    36    backend="labelbox",
    37    label_schema=label_schema,
    38    launch_editor=True,
    39)
    40
    41print(dataset.get_annotation_info(anno_key))
    42
    43# In Labelbox, re-annotate the relevant objects...
    44
    45# Download the results
    46dataset.load_annotations(anno_key, cleanup=True)
    47dataset.delete_annotation_run(anno_key)
    48
    49# In the App, compare the tagged and re-annotated labels
    50session.view = edit_view
    51
    52# If the edits look good, merge them into the `ground_truth` field
    53# and delete the previously tagged labels
    54dataset.merge_labels("ground_truth_edits", "ground_truth")
    55dataset.delete_labels(tags="edit")
    

![labelbox-example](../_images/labelbox_example.png) ![labelbox-new-class](../_images/labelbox_new_class.png)

### Editing existing labels#

Warning

Uploading existing labels is not yet implemented for the Labelbox backend.

See this section for one possible workflow for editing existing labels with Labelbox.

### Annotating multiple fields#

The `label_schema` argument allows you to define annotation tasks for multiple fields at once:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_multiple_fields"
     8
     9label_schema = {
    10    "people": {
    11        "type": "detections",
    12        "classes": ["person"],
    13    },
    14    "keypoints": {
    15        "type": "keypoints",
    16        "classes": ["person", "cat", "dog", "food"],
    17        "attributes": {
    18            "occluded": {
    19                "type": "radio",
    20                "values": [True, False],
    21            }
    22        }
    23    }
    24}
    25
    26view.annotate(
    27    anno_key,
    28    backend="labelbox",
    29    label_schema=label_schema,
    30    launch_editor=True,
    31)
    32print(dataset.get_annotation_info(anno_key))
    33
    34# Add annotations in Labelbox...
    35
    36dataset.load_annotations(anno_key, cleanup=True)
    37dataset.delete_annotation_run(anno_key)
    

![labelbox-multiple-fields](../_images/labelbox_multiple_fields.png)

### Configuring Labelbox projects#

When using the Labelbox backend, you can provide the optional `project_name` and `members` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to configure the Labelbox project that is created.

The `members` parameter can contain a list of `(email, role)` tuples defining the email addresses and project-level roles of members to add to the Labelbox project. The supported roles are:

  * `"LABELER"`

  * `"REVIEWER"`

  * `"TEAM_MANAGER"`

  * `"ADMIN"`




If any email addresses do not correspond to users already in your organization, an email invitation will be sent to them.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(5)
     6
     7anno_key = "labelbox_assign_users"
     8
     9project_name = "your_project_name"
    10members = [
    11    ("user1@domain.com", "LABELER"),
    12    ("user2@domain.com", "REVIEWER"),
    13    ("user3@domain.com", "TEAM_MANAGER"),
    14]
    15
    16view.annotate(
    17    anno_key,
    18    backend="labelbox",
    19    label_field="people",
    20    label_type="detections",
    21    classes=["person"],
    22    project_name=project_name,
    23    members=members,
    24    launch_editor=True,
    25)
    26print(dataset.get_annotation_info(anno_key))
    27
    28# Cleanup (without downloading results)
    29results = dataset.load_annotation_results(anno_key)
    30results.cleanup()
    31dataset.delete_annotation_run(anno_key)
    

### Scalar labels#

[`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields are the preferred way to store information for common tasks such as classification and detection in your FiftyOne datasets. However, you can also store Labelbox annotations in scalar fields of type `float`, `int`, `str`, or `bool`.

When storing annotations in scalar fields, the `label_field` parameter is still used to define the name of the field, but the `classes` argument is now optional and the `attributes` argument is unused.

If `classes` are provided, you will be able to select from these values in Labelbox; otherwise, the Labelbox tag will show the `label_field` name and you must enter the appropriate scalar in the `value` attribute of the tag.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_scalar_fields"
     8
     9# Create two scalar fields, one with classes and one without
    10label_schema = {
    11    "scalar1": {
    12        "type": "scalar",
    13    },
    14    "scalar2": {
    15        "type": "scalar",
    16        "classes": ["class1", "class2", "class3"],
    17    }
    18}
    19
    20view.annotate(
    21    anno_key,
    22    backend="labelbox",
    23    label_schema=label_schema,
    24    launch_editor=True,
    25)
    26print(dataset.get_annotation_info(anno_key))
    27
    28# Cleanup (without downloading results)
    29results = dataset.load_annotation_results(anno_key)
    30results.cleanup()
    31dataset.delete_annotation_run(anno_key)
    

![labelbox-scalar](../_images/labelbox_scalar.png)

### Uploading alternate media#

In some cases, you may want to upload media files other than those stored in the `filepath` field of your datasetâs samples for annotation. For example, you may have a dataset with personal information like faces or license plates that must be anonymized before uploading for annotation.

The recommended approach in this case is to store the alternative media files for each sample on disk and record these paths in a new field of your FiftyOne dataset. You can then specify this field via the `media_field` parameter of [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate").

For example, letâs upload some blurred images to Labelbox for annotation:
    
    
     1import os
     2import cv2
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8view = dataset.take(1)
     9
    10alt_dir = "/tmp/blurred"
    11if not os.path.exists(alt_dir):
    12    os.makedirs(alt_dir)
    13
    14# Blur images
    15for sample in view:
    16    filepath = sample.filepath
    17    alt_filepath = os.path.join(alt_dir, os.path.basename(filepath))
    18
    19    img = cv2.imread(filepath)
    20    cv2.imwrite(alt_filepath, cv2.blur(img, (20, 20)))
    21
    22    sample["alt_filepath"] = alt_filepath
    23    sample.save()
    24
    25anno_key = "labelbox_alt_media"
    26
    27view.annotate(
    28    anno_key,
    29    backend="labelbox",
    30    label_field="objects",
    31    label_type="detections",
    32    classes=["person", "car"],
    33    media_field="alt_filepath",
    34    launch_editor=True,
    35)
    36print(dataset.get_annotation_info(anno_key))
    37
    38# Create annotations in Labelbox
    39
    40dataset.load_annotations(anno_key, cleanup=True)
    41dataset.delete_annotation_run(anno_key)
    

![labelbox-alt-media](../_images/labelbox_alt_media.png)

### Annotating classes directly#

By default, the Labelbox editor is constructed so that all label fields being annotated are shown on the left sidebar at the top-level. When an object is annotated, the class name is then selected as an attribute.

However, it can be useful to directly show the object classes at the top-level of the sidebar to avoid additional clicks. The `classes_as_attrs` argument can be set to `False` to provide this functionality.

Note

When `classes_as_attrs=False`, only one label field of each type of spatial label is allowed. For example, only one âdetectionsâ label field can be annotated. Annotating multiple âscalarâ, âclassificationâ, an âclassificationsâ fields is still allowed.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_classes_as_attrs"
     8
     9view.annotate(
    10    anno_key,
    11    backend="labelbox",
    12    label_field="new_detections",
    13    label_type="detections",
    14    classes=["dog", "cat", "person"],
    15    classes_as_attrs=False,
    16    launch_editor=True,
    17)
    18print(dataset.get_annotation_info(anno_key))
    19
    20# Create annotations in Labelbox...
    21
    22dataset.load_annotations(anno_key, cleanup=True)
    23dataset.delete_annotation_run(anno_key)
    

![labelbox_classes_as_attrs](../_images/labelbox_classes_as_attrs.png)

## Annotating videos#

You can annotate for video datasets using the Labelbox backend through the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart-video")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_video"
     8
     9view.annotate(
    10    anno_key,
    11    backend="labelbox",
    12    label_field="frames.new_detections",
    13    label_type="detections",
    14    classes=["person"],
    15    launch_editor=True,
    16)
    17print(dataset.get_annotation_info(anno_key))
    18
    19# Create annotations in Labelbox...
    20
    21# Download annotations
    22dataset.load_annotations(anno_key)
    23
    24# Load the view that was annotated in the App
    25view = dataset.load_annotation_view(anno_key)
    26session = fo.launch_app(view=view)
    27
    28# Cleanup
    29results = dataset.load_annotation_results(anno_key)
    30results.cleanup()
    31dataset.delete_annotation_run(anno_key)
    

Note

Prepend `"frames."` to reference frame-level fields when calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate").

![labelbox-video](../_images/labelbox_video.png)

## Additional utilities#

You can perform additional Labelbox-specific operations to monitor the progress of an annotation project initiated by [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") via the returned [`LabelboxAnnotationResults`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxAnnotationResults "fiftyone.utils.labelbox.LabelboxAnnotationResults") instance.

The sections below highlight some common actions that you may want to perform.

### Viewing project status#

You can use the [`get_status()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxAnnotationResults.get_status "fiftyone.utils.labelbox.LabelboxAnnotationResults.get_status") and [`print_status()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxAnnotationResults.print_status "fiftyone.utils.labelbox.LabelboxAnnotationResults.print_status") methods to get information about the current status of the project for that annotation run:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(3)
     6
     7anno_key = "labelbox_status"
     8
     9view.annotate(
    10    anno_key,
    11    backend="labelbox",
    12    label_field="people",
    13    label_type="detections",
    14    classes=["person"],
    15)
    16
    17# Print the project's status
    18results = dataset.load_annotation_results(anno_key)
    19results.print_status()
    20
    21results.cleanup()
    22dataset.delete_annotation_run(anno_key)
    
    
    
    Project: FiftyOne_quickstart
    ID: cktixtv70e8zm0yba501v0ltz
    Created at: 2021-09-13 17:46:21+00:00
    Updated at: 2021-09-13 17:46:24+00:00
    
    Members:
        User: user1
        Name: user1
        Role: Admin
        Email: USER1_EMAIL@email.com
        ID: ckl137jfiss1c07320dacd81l
    
        User: user2
        Name: FIRSTNAME LASTNAME
        Role: Labeler
        Email: USER2_EMAIL@email.com
        ID: ckl137jfiss1c07320dacd82y
    
    Reviews:
        Positive: 2
        Zero: 0
        Negative: 1
    

### Deleting projects#

You can use [`delete_project()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxAnnotationAPI.delete_project "fiftyone.utils.labelbox.LabelboxAnnotationAPI.delete_project") or [`delete_projects()`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxAnnotationAPI.delete_projects "fiftyone.utils.labelbox.LabelboxAnnotationAPI.delete_projects") methods to delete specific Labelbox project(s) associated with an annotation run.
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5view = dataset.take(1)
     6
     7anno_key = "labelbox_delete_tasks"
     8
     9view.annotate(
    10    anno_key,
    11    backend="labelbox",
    12    label_field="people",
    13    label_type="detections",
    14    classes=["person"],
    15)
    16
    17results = dataset.load_annotation_results(anno_key)
    18api = results.connect_to_api()
    19
    20api.delete_project(
    21    results.project_id,
    22    delete_batches=True,
    23    delete_ontologies=False,
    24)
    25
    26# OR
    27
    28# List all projects or datasets associated with your Labelbox account
    29project_ids = api.list_projects()
    30dataset_ids = api.list_datasets()
    31
    32# Delete all projects and datasets from your Labelbox account
    33api.delete_projects(project_ids)
    34api.delete_datasets(dataset_ids)
    

Note

Note that passing `delete_batches=True` when deleting projects will not delete the corresponding data rows from Labelbox when using the V2 export API (the default).

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
