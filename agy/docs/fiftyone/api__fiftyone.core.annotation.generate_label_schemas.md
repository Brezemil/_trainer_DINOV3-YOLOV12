---
source_url: https://docs.voxel51.com/api/fiftyone.core.annotation.generate_label_schemas.html
---

# fiftyone.core.annotation.generate_label_schemas#

Annotation label schema generation

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`generate_label_schemas`(sample_collection[,Â ...]) | Generates label schemas for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
---|---  
  
fiftyone.core.annotation.generate_label_schemas.generate_label_schemas(_sample_collection_ , _fields =None_, _scan_samples =True_)#
    

Generates label schemas for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

A label schema is defined by a `type` and `component` with respect to a field. Further settings depend on the `type` and `component` combination as outlined below.

The `type` value for a field is inferred from the collectionâs field schema. See [`fiftyone.core.collections.SampleCollection.get_field_schema()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_field_schema "fiftyone.core.collections.SampleCollection.get_field_schema")

Currently supported media types for the collection are `image` and `3d`. See [`fiftyone.core.collections.SampleCollection.media_type`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.media_type "fiftyone.core.collections.SampleCollection.media_type")

**Primitives and components**

Supported primitive types are:

>   * `bool`: [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")
> 
>   * `date`: [`fiftyone.core.fields.DateField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateField "fiftyone.core.fields.DateField")
> 
>   * `datetime`: [`fiftyone.core.fields.DateTimeField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DateTimeField "fiftyone.core.fields.DateTimeField")
> 
>   * `dict`: [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")
> 
>   * `float`: [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")
> 
>   * `id`: [`fiftyone.core.fields.ObjectIdField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ObjectIdField "fiftyone.core.fields.ObjectIdField") or [`fiftyone.core.fields.UUIDField`](api__fiftyone.core.fields.md#fiftyone.core.fields.UUIDField "fiftyone.core.fields.UUIDField")
> 
>   * `int`: [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField") or [`fiftyone.core.fields.FrameNumberField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FrameNumberField "fiftyone.core.fields.FrameNumberField")
> 
>   * `list<int>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")
> 
>   * `list<float>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")
> 
>   * `list<str>`: [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") of [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")
> 
>   * `str`: [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")
> 
> 


Supported `bool` components are:

>   * `checkbox`
> 
>   * `toggle` \- the default
> 
> 


`date` and `datetime` only support the `datepicker` component.

`dict` only supports the `json` component.

Supported `float` and `int` components are:

>   * `dropdown`
> 
>   * `radio`
> 
>   * `slider`: the default when `scan_samples` is `True` and distinct finite bounds are found that define a `range`
> 
>   * `text`: the default when `scan_samples` is `False` or distinct finite bounds are not found
> 
> 


Supported `list<float>` and `list<int>` components are:

>   * `checkboxes`
> 
>   * `dropdown`
> 
>   * `text` \- the default
> 
> 


Supported `list<str>` components are:

>   * `checkboxes`: the default if `<=5` values are scanned
> 
>   * `dropdown`: the default if `>5` and `<=1000` values are scanned
> 
>   * `text`: the default if `0` values or `>1000` values are scanned, or `scan_samples` is `False`
> 
> 


Supported `str` type components are:

>   * `dropdown`: the default if `>5` and `<=1000` values are scanned
> 
>   * `radio`: the default if `<=5` values are scanned
> 
>   * `text`: the default if `0` values or `>1000` values are scanned, or `scan_samples` is `False`
> 
> 


`float` types support a `precision` setting when a `text` component is configured for the number of digits to allow after the decimal.

All types support a `read_only` flag. `id` types must be `read_only`. If a field is `read_only` in the field schema, then the `read_only` label schema setting must be `True`, e.g. `created_at` and `last_modified_at` must be read only.

All components support `values` except `json`, `slider`, and `toggle` excepting `id` restrictions.

`checkboxes` and `dropdown` require the `values` setting.

`slider` requires the `range: [min, max]` setting.

**Labels**

The `label` subfield of all label types are configured via `classes` and support the same settings as a `str` type. See the example output below for `detections` fields in the quickstart dataset. If the label type has a visual representation, that field is handled by the Appâs builtin annotation UI, e.g. `bounding_box` for a `detection`. Primitive attributes of label types are configured via the `attributes` list.

When a label is marked as `read_only`, all its attributes inherit the setting as well.

All [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types are resolved by this method except [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection"), and [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") when provided in the `fields` argument, otherwise only App supported fields are resolved. For label types supported by the App for annotation, see [`fiftyone.core.annotation.utils.get_supported_app_annotation_fields()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.get_supported_app_annotation_fields "fiftyone.core.annotation.utils.get_supported_app_annotation_fields").

All attributes and the label class itself support a `default` setting that applies when creating a new label.

**Embedded documents**

One level of nesting is supported via `dot.notation` for `fiftyone.core.fields.EmbeddedDocumentField`` fields for the default `metadata` field and the `fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument`` document type. All label and primitive types are supported. See [here](https://docs.voxel51.com/user_guide/using_datasets.html#dynamic-attributes) for more details on adding dynamic attributes.

Example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.compute_metadata()
    
    fo.pprint(fo.generate_label_schemas(dataset, scan_samples=False))
    

Output:
    
    
    {
        "created_at": {
            "type": "datetime",
            "component": "datepicker",
            "read_only": True,
        },
        "filepath": {"type": "str", "component": "text"},
        "ground_truth": {
            "attributes": [
                {
                    "name": "attributes",
                    "type": "dict",
                    "component": "json",
                },
                {
                    "name": "confidence",
                    "type": "float",
                    "component": "text",
                },
                {
                    "name": "id",
                    "type": "id",
                    "component": "text",
                    "read_only": True,
                },
                {"name": "index", "type": "int", "component": "text"},
                {"name": "mask_path", "type": "str", "component": "text"},
                {"name": "tags", "type": "list<str>", "component": "text"},
            ],
            "component": "text",
            "type": "detections",
        },
        "id": {"type": "id", "component": "text", "read_only": True},
        "last_modified_at": {
            "type": "datetime",
            "component": "datepicker",
            "read_only": True,
        },
        "metadata.height": {"type": "int", "component": "text"},
        "metadata.mime_type": {"type": "str", "component": "text"},
        "metadata.num_channels": {"type": "int", "component": "text"},
        "metadata.size_bytes": {"type": "int", "component": "text"},
        "metadata.width": {"type": "int", "component": "text"},
        "predictions": {
            "attributes": [
                {
                    "name": "attributes",
                    "type": "dict",
                    "component": "json",
                },
                {
                    "name": "confidence",
                    "type": "float",
                    "component": "text",
                },
                {
                    "name": "id",
                    "type": "id",
                    "component": "text",
                    "read_only": True,
                },
                {"name": "index", "type": "int", "component": "text"},
                {"name": "mask_path", "type": "str", "component": "text"},
                {"name": "tags", "type": "list<str>", "component": "text"},
            ],
            "component": "text",
            "type": "detections",
        },
        "tags": {"type": "list<str>", "component": "text"},
        "uniqueness": {"type": "float", "component": "text"},
    }
    

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to generate the schema with

  * **fields** (_None_) â a field name, `embedded.field.name` or iterable of such values

  * **scan_samples** (_True_) â whether to scan the collection to populate component settings based on actual field values (ranges, values, etc). If False, the label schema is generated from _only_ the statically available information in the datasetâs field schema



Raises:
    

**ValueError** â if the sample collection or field is not supported

Returns:
    

a label schemas `dict`, or an individual fieldâs label schema `dict` if only one field is provided

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
