---
source_url: https://docs.voxel51.com/api/fiftyone.core.annotation.utils.html
---

# fiftyone.core.annotation.utils#

Annotation utils

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`ensure_collection_is_supported`(sample_collection) | Ensure a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") is supported by the App for annotation.  
---|---  
`get_supported_app_annotation_fields`(...) | Gets the supported App annotation fields for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`list_valid_annotation_fields`(sample_collection) | Lists all valid annotation fields for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`flatten_fields`(collection,Â fields[,Â ...]) | Flattens embedded document fields into dot-separated paths.  
`get_type`(field) | Get the `type` of a field for a label schema  
  
fiftyone.core.annotation.utils.ensure_collection_is_supported(_sample_collection_)#
    

Ensure a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") is supported by the App for annotation.

> Args:
>     
> 
> sample_collection: a
>     
> 
> [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

fiftyone.core.annotation.utils.get_supported_app_annotation_fields(_sample_collection_)#
    

Gets the supported App annotation fields for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

Currently supported media types for the collection are `image` and `3d`. See [`fiftyone.core.collections.SampleCollection.media_type`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.media_type "fiftyone.core.collections.SampleCollection.media_type")

All supported primitive and `embedded.document` primitives are supported as documented in `generate_label_schemas()`

The below [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types are also resolved.

Supported `image` [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types are:
    

  * `classification`: [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

  * `classifications`: [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

  * `detection`: [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * `detections`: [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")



Supported `3d` label types are:
    

  * `classification`: [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

  * `classifications`: [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

  * `polyline`: [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * `polylines`: [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")




Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Returns:
    

a list of supported fields

fiftyone.core.annotation.utils.list_valid_annotation_fields(_sample_collection_ , _require_app_support =False_, _flatten =False_)#
    

Lists all valid annotation fields for a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

A field may be valid, but not yet supported by the App for human annotation.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **require_app_support** (_False_) â whether to only include fields supported by the App for annotation

  * **flatten** (_False_) â whether to flatten embedded documents with `dot.notation`



Returns:
    

a sorted list of valid annotation field names

fiftyone.core.annotation.utils.flatten_fields(_collection_ , _fields_ , _require_app_support =False_)#
    

Flattens embedded document fields into dot-separated paths.

Parameters:
    

  * **collection** â the sample collection

  * **fields** â iterable of field names to flatten

  * **require_app_support** (_False_) â whether to only include fields supported by the App for annotation



Returns:
    

sorted list of flattened field names

fiftyone.core.annotation.utils.get_type(_field_)#
    

Get the `type` of a field for a label schema

Parameters:
    

**field** â the field instance

Returns:
    

a label schema `type`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
