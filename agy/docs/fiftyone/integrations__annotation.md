---
source_url: https://docs.voxel51.com/integrations/annotation.html
---

# Annotating Datasets#

FiftyOne provides a powerful annotation API that makes it easy to add or edit labels on your [datasets](https://docs.voxel51.com/user_guide/using_datasets.html#using-datasets) or specific [views](https://docs.voxel51.com/user_guide/using_views.html#using-views) into them.

Note

Did you know? You can request, manage, and import annotations from within the FiftyOne App by installing the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation) plugin!

Note

Check out [this tutorial](tutorials__cvat_annotation.md) to see an example workflow that uses the annotation API to create, delete, and fix annotations on a FiftyOne dataset.

## Basic recipe#

The basic workflow to use the annotation API to add or edit labels on your FiftyOne datasets is as follows:

  1. Load a [labeled or unlabeled dataset](user_guide__import_datasets.md#importing-datasets) into FiftyOne

  2. Explore the dataset using the [App](user_guide__app.md#fiftyone-app) or [dataset views](https://docs.voxel51.com/user_guide/using_views.html#using-views) to locate either unlabeled samples that you wish to annotate or labeled samples whose annotations you want to edit

  3. Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method on your dataset or view to upload the samples and optionally their existing labels to the annotation backend

  4. In the annotation tool, perform the necessary annotation work

  5. Back in FiftyOne, load your dataset and use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to merge the annotations back into your FiftyOne dataset

  6. If desired, delete the annotation tasks and the record of the annotation run from your FiftyOne dataset




  
The example below demonstrates this workflow using the default [CVAT backend](integrations__cvat.md#cvat-integration).

Note

You must create an account at [app.cvat.ai](https://app.cvat.ai) in order to run this example.

Note that you can store your credentials as described in [this section](integrations__cvat.md#cvat-setup) to avoid entering them manually each time you interact with CVAT.

First, we create the annotation tasks:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5# Step 1: Load your data into FiftyOne
     6
     7dataset = foz.load_zoo_dataset(
     8    "quickstart", dataset_name="cvat-annotation-example"
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
    26# Let's edit the ground truth annotations for the sample with the most
    27# high confidence false positives
    28sample_id = most_fp_view.first().id
    29view = dataset.select(sample_id)
    30
    31# Step 3: Send samples to CVAT
    32
    33# A unique identifier for this run
    34anno_key = "cvat_basic_recipe"
    35
    36view.annotate(
    37    anno_key,
    38    label_field="ground_truth",
    39    attributes=["iscrowd"],
    40    launch_editor=True,
    41)
    42print(dataset.get_annotation_info(anno_key))
    43
    44# Step 4: Perform annotation in CVAT and save the tasks
    

Then, once the annotation work is complete, we merge the annotations back into FiftyOne:
    
    
     1import fiftyone as fo
     2
     3anno_key = "cvat_basic_recipe"
     4
     5# Step 5: Merge annotations back into FiftyOne dataset
     6
     7dataset = fo.load_dataset("cvat-annotation-example")
     8dataset.load_annotations(anno_key)
     9
    10# Load the view that was annotated in the App
    11view = dataset.load_annotation_view(anno_key)
    12session = fo.launch_app(view=view)
    13
    14# Step 6: Cleanup
    15
    16# Delete tasks from CVAT
    17results = dataset.load_annotation_results(anno_key)
    18results.cleanup()
    19
    20# Delete run record (not the labels) from FiftyOne
    21dataset.delete_annotation_run(anno_key)
    

Note

Check out [this page](integrations__cvat.md#cvat-examples) to see a variety of common annotation patterns using the CVAT backend to illustrate the full process.

## Setup#

By default, all annotation is performed via [app.cvat.ai](https://app.cvat.ai), which simply requires that you create an account and then configure your username and password credentials.

However, you can configure FiftyOne to use a [self-hosted CVAT server](integrations__cvat.md#cvat-self-hosted-server), or you can even use a completely custom backend.

Note

See [this page](integrations__cvat.md#cvat-setup) for CVAT-specific setup instructions.

### Changing your annotation backend#

You can use a specific backend for a particular annotation run by passing the `backend` parameter to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):
    
    
    1view.annotate(..., backend="<backend>", ...)
    

Alternatively, you can change your default annotation backend for an entire session by setting the `FIFTYONE_ANNOTATION_DEFAULT_BACKEND` environment variable.
    
    
    export FIFTYONE_ANNOTATION_DEFAULT_BACKEND=<backend>
    

Finally, you can permanently change your default annotation backend by updating the `default_backend` key of your annotation config at `~/.fiftyone/annotation_config.json`:
    
    
    {
        "default_backend": "<backend>",
        "backends": {
            "<backend>": {...},
            ...
        }
    }
    

### Configuring your backend#

Annotation backends may be configured in a variety of backend-specific ways, which you can see by inspecting the parameters of a backendâs associated [`AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig") class.

The relevant classes for the builtin annotation backends are:

  * `"cvat"`: [`fiftyone.utils.cvat.CVATBackendConfig`](api__fiftyone.utils.cvat.md#fiftyone.utils.cvat.CVATBackendConfig "fiftyone.utils.cvat.CVATBackendConfig")

  * `"labelstudio"`: [`fiftyone.utils.labelstudio.LabelStudioBackendConfig`](api__fiftyone.utils.labelstudio.md#fiftyone.utils.labelstudio.LabelStudioBackendConfig "fiftyone.utils.labelstudio.LabelStudioBackendConfig")

  * `"labelbox"`: [`fiftyone.utils.labelbox.LabelboxBackendConfig`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxBackendConfig "fiftyone.utils.labelbox.LabelboxBackendConfig")




You can configure an annotation backendâs parameters for a specific run by simply passing supported config parameters as keyword arguments each time you call [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):
    
    
    1view.annotate(
    2    ...
    3    backend="cvat",
    4    url="http://localhost:8080",
    5    username=...,
    6    password=...,
    7)
    

Alternatively, you can more permanently configure your backend(s) via your annotation config.

## Annotation config#

FiftyOne provides an annotation config that you can use to either temporarily or permanently configure the behavior of the annotation API.

### Viewing your config#

You can print your current annotation config at any time via the Python library and the CLI:
    
    
    import fiftyone as fo
    
    # Print your current annotation config
    print(fo.annotation_config)
    
    
    
    {
        "default_backend": "cvat",
        "backends": {
            "cvat": {
                "config_cls": "fiftyone.utils.cvat.CVATBackendConfig",
                "url": "https://app.cvat.ai"
            }
        }
    }
    
    
    
    # Print your current annotation config
    fiftyone annotation config
    
    
    
    {
        "default_backend": "cvat",
        "backends": {
            "cvat": {
                "config_cls": "fiftyone.utils.cvat.CVATBackendConfig",
                "url": "https://app.cvat.ai"
            }
        }
    }
    

Note

If you have customized your annotation config via any of the methods described below, printing your config is a convenient way to ensure that the changes you made have taken effect as you expected.

### Modifying your config#

You can modify your annotation config in a variety of ways. The following sections describe these options in detail.

#### Order of precedence#

The following order of precedence is used to assign values to your annotation config settings as runtime:

  1. Config settings applied at runtime by directly editing `fiftyone.annotation_config`

  2. `FIFTYONE_XXX` environment variables

  3. Settings in your JSON config (`~/.fiftyone/annotation_config.json`)

  4. The default config values




#### Editing your JSON config#

You can permanently customize your annotation config by creating a `~/.fiftyone/annotation_config.json` file on your machine. The JSON file may contain any desired subset of config fields that you wish to customize.

For example, the following config JSON file customizes the URL of your CVAT server without changing any other default config settings:
    
    
    {
        "backends": {
            "cvat": {
                "url": "http://localhost:8080"
            }
        }
    }
    

When `fiftyone` is imported, any options from your JSON config are merged into the default config, as per the order of precedence described above.

Note

You can customize the location from which your JSON config is read by setting the `FIFTYONE_ANNOTATION_CONFIG_PATH` environment variable.

#### Setting environment variables#

Annotation config settings may be customized on a per-session basis by setting the `FIFTYONE_XXX` environment variable(s) for the desired config settings.

The `FIFTYONE_ANNOTATION_DEFAULT_BACKEND` environment variable allows you to configure your default backend:
    
    
    export FIFTYONE_ANNOTATION_DEFAULT_BACKEND=labelbox
    

You can declare parameters for specific annotation backends by setting environment variables of the form `FIFTYONE_<BACKEND>_<PARAMETER>`. Any settings that you declare in this way will be passed as keyword arguments to methods like [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") whenever the corresponding backend is in use. For example, you can configure the URL, username, password, and email (if applicable) of your CVAT server as follows:
    
    
    export FIFTYONE_CVAT_URL=http://localhost:8080
    export FIFTYONE_CVAT_USERNAME=...
    export FIFTYONE_CVAT_PASSWORD=...
    export FIFTYONE_CVAT_EMAIL=...  # if applicable
    

The `FIFTYONE_ANNOTATION_BACKENDS` environment variable can be set to a `list,of,backends` that you want to expose in your session, which may exclude native backends and/or declare additional custom backends whose parameters are defined via additional config modifications of any kind:
    
    
    export FIFTYONE_ANNOTATION_BACKENDS=custom,cvat,labelbox
    

When declaring new backends, you can include `*` to append new backend(s) without omitting or explicitly enumerating the builtin backends. For example, you can add a `custom` annotation backend as follows:
    
    
    export FIFTYONE_ANNOTATION_BACKENDS=*,custom
    export FIFTYONE_CUSTOM_CONFIG_CLS=your.custom.AnnotationConfig
    

#### Modifying your config in code#

You can dynamically modify your annotation config at runtime by directly editing the `fiftyone.annotation_config` object.

Any changes to your annotation config applied via this manner will immediately take effect in all subsequent calls to `fiftyone.annotation_config` during your current session.
    
    
    1import fiftyone as fo
    2
    3fo.annotation_config.default_backend = "<backend>"
    

## Requesting annotations#

Use the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") method to send the samples and optionally existing labels in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to your annotation backend for processing.

The basic syntax is:
    
    
    1anno_key = "..."
    2view.annotate(anno_key, ...)
    

The `anno_key` argument defines a unique identifier for the annotation run, and you will provide it to methods like [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`get_annotation_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations"), [`load_annotation_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotation_results "fiftyone.core.collections.SampleCollection.load_annotation_results"), [`rename_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_annotation_run "fiftyone.core.collections.SampleCollection.rename_annotation_run"), and [`delete_annotation_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_annotation_run "fiftyone.core.collections.SampleCollection.delete_annotation_run") to manage the run in the future.

Warning

FiftyOne assumes that all labels in an annotation run can fit in memory.

If you are annotating very large scale video datasets with dense frame labels, you may violate this assumption. Instead, consider breaking the work into multiple smaller annotation runs that each contain limited subsets of the samples you wish to annotate.

You can use [`Dataset.stats()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.stats "fiftyone.core.dataset.Dataset.stats") to get a sense for the total size of the labels in a dataset as a rule of thumb to estimate the size of a candidate annotation run.

In addition, [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") provides various parameters that you can use to customize the annotation tasks that you wish to be performed.

The following parameters are supported by all annotation backends:

  * **backend** (_None_): the annotation backend to use. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * **media_field** (_âfilepathâ_): the sample field containing the path to the source media to upload

  * **launch_editor** (_False_): whether to launch the annotation backendâs editor after uploading the samples




The following parameters allow you to configure the labeling schema to use for your annotation tasks. See this section for more details:

  * **label_schema** (_None_): a dictionary defining the label schema to use. If this argument is provided, it takes precedence over the remaining fields

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




  
In addition, each annotation backend can typically be configured in a variety of backend-specific ways. See this section for more details.

Note

Specific annotation backends may not support all `label_type` options.

### Label schema#

The `label_schema`, `label_field`, `label_type`, `classes`, `attributes`, and `mask_targets` parameters to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") allow you to define the annotation schema that you wish to be used.

The label schema may define new label field(s) that you wish to populate, and it may also include existing label field(s), in which case you can add, delete, or edit the existing labels on your FiftyOne dataset.

The `label_schema` argument is the most flexible way to define how to construct tasks in CVAT. In its most verbose form, it is a dictionary that defines the label type, annotation type, possible classes, and possible attributes for each label field:
    
    
     1anno_key = "..."
     2
     3label_schema = {
     4    "new_field": {
     5        "type": "classifications",
     6        "classes": ["class1", "class2"],
     7        "attributes": {
     8            "attr1": {
     9                "type": "select",
    10                "values": ["val1", "val2"],
    11                "default": "val1",
    12            },
    13            "attr2": {
    14                "type": "radio",
    15                "values": [True, False],
    16                "default": False,
    17            }
    18        },
    19    },
    20    "existing_field": {
    21        "classes": ["class3", "class4"],
    22        "attributes": {
    23            "attr3": {
    24                "type": "text",
    25            }
    26        }
    27    },
    28}
    29
    30dataset.annotate(anno_key, label_schema=label_schema)
    

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
    11                        "type": "select",
    12                        "values": ["val1", "val2"],
    13                        "default": "val1",
    14                    }
    15                 }
    16            },
    17            "class3",
    18            "class4",
    19        ],
    20        "attributes": {
    21            "attr2": {
    22                "type": "radio",
    23                "values": [True, False],
    24                "default": False,
    25            }
    26        },
    27    },
    28}
    29
    30dataset.annotate(anno_key, label_schema=label_schema)
    

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
    10        "type": "select",
    11        "values": ["val1", "val2"],
    12        "default": "val1",
    13    },
    14    "attr2": {
    15        "type": "radio",
    16        "values": [True, False],
    17        "default": False,
    18    }
    19}
    20
    21dataset.annotate(
    22    anno_key,
    23    label_field=label_field,
    24    label_type=label_type,
    25    classes=classes,
    26    attributes=attributes,
    27)
    

When you are annotating existing label fields, you can omit some of these parameters from [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), as FiftyOne can infer the appropriate values to use:

  * **label_type** : if omitted, the [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type of the field will be used to infer the appropriate value for this parameter

  * **classes** : if omitted, the observed labels on your dataset will be used to construct a classes list

  * **mask_targets** : if omitted for a semantic segmentation field, the mask targets from the [`mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.mask_targets "fiftyone.core.dataset.Dataset.mask_targets") or [`default_mask_targets`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.default_mask_targets "fiftyone.core.dataset.Dataset.default_mask_targets") properties of your dataset will be used, if available




### Label attributes#

The `attributes` parameter allows you to configure whether [custom attributes](https://docs.voxel51.com/user_guide/using_datasets.html#using-labels) beyond the default `label` attribute are included in the annotation tasks.

When adding new label fields for which you want to include attributes, you must use the dictionary syntax demonstrated below to define the schema of each attribute that you wish to label:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "occluded": {
     5        "type": "radio",
     6        "values": [True, False],
     7        "default": False,
     8    },
     9    "gender": {
    10        "type": "select",
    11        "values": ["male", "female"],
    12    },
    13    "caption": {
    14        "type": "text",
    15    }
    16}
    17
    18view.annotate(
    19    anno_key,
    20    label_field="new_field",
    21    label_type="detections",
    22    classes=["dog", "cat", "person"],
    23    attributes=attributes,
    24)
    

You can always omit this parameter if you do not require attributes beyond the default `label`.

Each annotation backend may support different `type` values, as declared by the [`supported_attr_types()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend.supported_attr_types "fiftyone.utils.annotations.AnnotationBackend.supported_attr_types") method of its [`AnnotationBackend`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend "fiftyone.utils.annotations.AnnotationBackend") class. For example, CVAT supports the following choices for `type`:

  * `text`: a free-form text box. In this case, `default` is optional and `values` is unused

  * `select`: a selection dropdown. In this case, `values` is required and `default` is optional

  * `radio`: a radio button list UI. In this case, `values` is required and `default` is optional

  * `checkbox`: a boolean checkbox UI. In this case, `default` is optional and `values` is unused




When you are annotating existing label fields, the `attributes` parameter can take additional values:

  * `True` (default): export all custom attributes observed on the existing labels, using their observed values to determine the appropriate UI type and possible values, if applicable

  * `False`: do not include any custom attributes in the export

  * a list of custom attributes to include in the export

  * a full dictionary syntax described above




Note that only scalar-valued label attributes are supported. Other attribute types like lists, dictionaries, and arrays will be omitted.

### Restricting additions, deletions, and edits#

When you create annotation runs that involve editing existing label fields, you can optionally specify that certain changes are not allowed by passing the following flags to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"):

  * **allow_additions** (_True_): whether to allow new labels to be added

  * **allow_deletions** (_True_): whether to allow labels to be deleted

  * **allow_label_edits** (_True_): whether to allow the `label` attribute to be modified

  * **allow_index_edits** (_True_): whether to allow the `index` attribute of video tracks to be modified

  * **allow_spatial_edits** (_True_): whether to allow edits to the spatial properties (bounding boxes, vertices, keypoints, etc) of labels




If you are using the `label_schema` parameter to provide a full annotation schema to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), you can also directly include the above flags in the configuration dicts for any existing label field(s) you wish.

For example, suppose you have an existing `ground_truth` field that contains objects of various types and you would like to add new `sex` and `age` attributes to all people in this field while also strictly enforcing that no objects can be added, deleted, or have their labels or bounding boxes modified. You can configure an annotation run for this as follows:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "sex": {
     5        "type": "select",
     6        "values": ["male", "female"],
     7    },
     8    "age": {
     9        "type": "text",
    10    },
    11}
    12
    13view.annotate(
    14    anno_key,
    15    label_field="ground_truth",
    16    classes=["person"],
    17    attributes=attributes,
    18    allow_additions=False,
    19    allow_deletions=False,
    20    allow_label_edits=False,
    21    allow_spatial_edits=False,
    22)
    

You can also include a `read_only=True` parameter when uploading existing label attributes to specify that the attributeâs value should be uploaded to the annotation backend for informational purposes, but any edits to the attributeâs value should not be imported back into FiftyOne.

For example, if you have vehicles with their `make` attribute populated and you want to populate a new `model` attribute based on this information without allowing changes to the vehicleâs `make`, you can configure an annotation run for this as follows:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "make": {
     5        "type": "text",
     6        "read_only": True,
     7    },
     8    "model": {
     9        "type": "text",
    10    },
    11}
    12
    13view.annotate(
    14    anno_key,
    15    label_field="ground_truth",
    16    classes=["vehicle"],
    17    attributes=attributes,
    18)
    

Note

Some annotation backends may not support restrictions to additions, deletions, spatial edits, and read-only attributes in their editing interface.

However, any restrictions that you specify via the above parameters will still be enforced when you call [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") to merge the annotations back into FiftyOne.

### Labeling videos#

When annotating spatiotemporal objects in videos, you have a few additional options at your fingertips.

First, each object attribute specification can include a `mutable` property that controls whether the attributeâs value can change between frames for each object:
    
    
     1anno_key = "..."
     2
     3attributes = {
     4    "type": {
     5        "type": "select",
     6        "values": ["sedan", "suv", "truck"],
     7        "mutable": False,
     8    },
     9    "occluded": {
    10        "type": "radio",
    11        "values": [True, False],
    12        "default": False,
    13        "mutable": True,
    14    },
    15}
    16
    17view.annotate(
    18    anno_key,
    19    label_field="frames.new_field",
    20    label_type="detections",
    21    classes=["vehicle"],
    22    attributes=attributes,
    23)
    

The meaning of the `mutable` attribute is defined as follows:

  * `True` (default): the attribute is dynamic and can have a different value for every frame in which the object track appears

  * `False`: the attribute is static and is the same for every frame in which the object track appears




In addition, if you are using an annotation backend [like CVAT](integrations__cvat.md#cvat-annotating-videos) that supports keyframes, then when you download annotation runs that include track annotations, the downloaded label corresponding to each keyframe of an object track will have its `keyframe=True` attribute set to denote that it was a keyframe.

Similarly, when you create an annotation run on a video dataset that involves _editing_ existing video tracks, if at least one existing label has a `keyframe=True` attribute set, then the available keyframe information will be uploaded to the annotation backend.

## Loading annotations#

After your annotations tasks in the annotation backend are complete, you can use the [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") method to download them and merge them back into your FiftyOne dataset.
    
    
    1view.load_annotations(anno_key)
    

The `anno_key` parameter is the unique identifier for the annotation run that you provided when calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"). You can use [`list_annotation_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_annotation_runs "fiftyone.core.collections.SampleCollection.list_annotation_runs") to see the available keys on a dataset.

Note

By default, calling [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") will not delete any information for the run from the annotation backend.

However, you can pass `cleanup=True` to delete all information associated with the run from the backend after the annotations are downloaded.

You can use the optional `dest_field` parameter to override the taskâs label schema and instead load annotations into different field name(s) of your dataset. This can be useful, for example, when editing existing annotations, if you would like to do a before/after comparison of the edits that you import. If the annotation run involves multiple fields, `dest_field` should be a dictionary mapping label schema field names to destination field names.

Some annotation backends like CVAT cannot explicitly prevent annotators from creating labels that donât obey the runâs label schema. You can pass the optional `unexpected` parameter to [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") to configure how to deal with any such unexpected labels that are found. The supported values are:

  * `"prompt"` (**default**): present an interactive prompt to direct/discard unexpected labels

  * `"keep"`: automatically keep all unexpected labels in a field whose name matches the label type

  * `"ignore"`: automatically ignore any unexpected labels

  * `"return"`: return a dict containing all unexpected labels, if any




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

## Custom annotation backends#

If you would like to use an annotation tool that is not natively supported by FiftyOne, you can follow the instructions below to implement an interface for your tool and then configure your environment so that the [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") and [`load_annotations()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_annotations "fiftyone.core.collections.SampleCollection.load_annotations") methods will use your custom backend.

Annotation backends are defined by writing subclasses of the following three classes with the appropriate abstract methods implemented:

  * [`AnnotationBackend`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend "fiftyone.utils.annotations.AnnotationBackend"): this class implements the logic required for your annotation backend to declare the types of labeling tasks that it supports, as well as the core [`upload_annotations()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend.upload_annotations "fiftyone.utils.annotations.AnnotationBackend.upload_annotations") and [`download_annotations()`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend.download_annotations "fiftyone.utils.annotations.AnnotationBackend.download_annotations") methods, which handle uploading and downloading data and labels to your annotation tool

  * [`AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig"): this class defines the available parameters that users can pass as keyword arguments to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") to customize the behavior of the annotation run

  * [`AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults"): this class stores any intermediate information necessary to track the progress of an annotation run that has been created and is now waiting for its results to be merged back into the FiftyOne dataset




Note

Refer to the [fiftyone.utils.cvat](https://github.com/voxel51/fiftyone/blob/develop/fiftyone/utils/cvat.py) module for an example of how the above subclasses are implemented for the CVAT backend.

The recommended way to expose a custom backend is to add it to your annotation config at `~/.fiftyone/annotation_config.json` as follows:
    
    
    {
        "default_backend": "<backend>",
        "backends": {
            "<backend>": {
                "config_cls": "your.custom.AnnotationConfig",
                # custom parameters here
            }
        }
    }
    

In the above, `<backend>` defines the name of your custom backend, which you can henceforward pass as the `backend` parameter to [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate"), and the `config_cls` parameter specifies the fully-qualified name of the [`AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig") subclass for your annotation backend.

With the `default_backend` parameter set to your custom backend as shown above, calling [`annotate()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.annotate "fiftyone.core.collections.SampleCollection.annotate") will automatically use your backend.

Alternatively, you can manually opt to use your custom backend on a per-run basis by passing the `backend` parameter:
    
    
    1view.annotate(..., backend="<backend>", ...)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
