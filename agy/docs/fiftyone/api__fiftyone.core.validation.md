---
source_url: https://docs.voxel51.com/api/fiftyone.core.validation.html
---

# fiftyone.core.validation#

Validation utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`validate_image_sample`(sample) | Validates that the sample's media is an image.  
---|---  
`validate_video_sample`(sample) | Validates that the sample's media is a video.  
`validate_collection`(sample_collection[,Â ...]) | Validates that the provided samples are a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`validate_image_collection`(sample_collection) | Validates that the provided samples are an image [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`validate_video_collection`(sample_collection) | Validates that the provided samples are a video [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`validate_grouped_non_dynamic_collection`(...) | Validates that the provided samples are a grouped [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").  
`validate_non_grouped_collection`(...) | Validates that the provided samples are a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") that is _not_ grouped.  
`validate_collection_label_fields`(...[,Â ...]) | Validates that the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") has fields with the specified [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types.  
`get_field`(sample,Â field_name[,Â ...]) | Gets the given sample field and optionally validates its type and value.  
`get_fields`(sample,Â field_names[,Â ...]) | Gets the given sample fields and optionally validates their types and values.  
  
fiftyone.core.validation.validate_image_sample(_sample_)#
    

Validates that the sampleâs media is an image.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

Raises:
    

**ValueError if the sample's media is not an image** â 

fiftyone.core.validation.validate_video_sample(_sample_)#
    

Validates that the sampleâs media is a video.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

Raises:
    

**ValueError if the sample's media is not a video** â 

fiftyone.core.validation.validate_collection(_sample_collection_ , _media_type =None_)#
    

Validates that the provided samples are a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

Parameters:
    

  * **sample_collection** â a sample collection

  * **media_type** (_None_) â an optional media type or iterable of media types that the collection must have



Raises:
    

  * **ValueError** â if the provided samples are not a

  * [**fiftyone.core.collections.SampleCollection**](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") â 




fiftyone.core.validation.validate_image_collection(_sample_collection_)#
    

Validates that the provided samples are an image [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

Parameters:
    

**sample_collection** â a sample collection

Raises:
    

  * **ValueError** â if the provided samples are not an image

  * [**fiftyone.core.collections.SampleCollection**](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") â 




fiftyone.core.validation.validate_video_collection(_sample_collection_)#
    

Validates that the provided samples are a video [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

Parameters:
    

**sample_collection** â a sample collection

Raises:
    

  * **ValueError** â if the provided samples are not a video

  * [**fiftyone.core.collections.SampleCollection**](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") â 




fiftyone.core.validation.validate_grouped_non_dynamic_collection(_sample_collection_)#
    

Validates that the provided samples are a grouped [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection").

Parameters:
    

**sample_collection** â a sample collection

Raises:
    

  * **ValueError** â if the provided samples are not grouped

  * [**fiftyone.core.collections.SampleCollection**](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") â 




fiftyone.core.validation.validate_non_grouped_collection(_sample_collection_)#
    

Validates that the provided samples are a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") that is _not_ grouped.

Parameters:
    

**sample_collection** â a sample collection

Raises:
    

  * **ValueError** â if the provided samples are a grouped

  * [**fiftyone.core.collections.SampleCollection**](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") â 




fiftyone.core.validation.validate_collection_label_fields(_sample_collection_ , _field_names_ , _allowed_label_types_ , _same_type =False_)#
    

Validates that the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") has fields with the specified [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **field_names** â a field name or iterable of field names

  * **allowed_label_types** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type or iterable of allowed [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types

  * **same_type** (_False_) â whether to enforce that all fields have same type. This condition is enforced separately for sample- and frame-level fields



Raises:
    

**ValueError if the required conditions are not met** â 

fiftyone.core.validation.get_field(_sample_ , _field_name_ , _allowed_types =None_, _allow_none =True_)#
    

Gets the given sample field and optionally validates its type and value.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **field_name** â the name of the field to get

  * **allowed_types** (_None_) â an optional iterable of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types to enforce that the field value has

  * **allow_none** (_True_) â whether to allow the field to be None



Returns:
    

the field value

Raises:
    

  * **ValueError if the field does not exist****or****does not meet the specified** â 

  * **criteria** â 




fiftyone.core.validation.get_fields(_sample_ , _field_names_ , _allowed_types =None_, _same_type =False_, _allow_none =True_)#
    

Gets the given sample fields and optionally validates their types and values.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **field_names** â an iterable of field names to get

  * **allowed_types** (_None_) â an optional iterable of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types to enforce that the field values have

  * **same_type** (_False_) â whether to enforce that all fields have same type

  * **allow_none** (_True_) â whether to allow the fields to be None



Returns:
    

a tuple of field values

Raises:
    

  * **ValueError if a field does not exist****or****does not meet the specified** â 

  * **criteria** â 




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
