---
source_url: https://docs.voxel51.com/api/fiftyone.core.sample.html
---

# fiftyone.core.sample#

Dataset samples.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_default_sample_fields`([include_private,Â ...]) | Returns the default fields present on all samples.  
---|---  
  
**Classes:**

[`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")(filepath[,Â tags,Â metadata]) | A sample in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").  
---|---  
`SampleView`(doc,Â view[,Â selected_fields,Â ...]) | A view into a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") in a dataset.  
  
fiftyone.core.sample.get_default_sample_fields(_include_private =False_, _use_db_fields =False_)#
    

Returns the default fields present on all samples.

Parameters:
    

  * **include_private** (_False_) â whether to include fields starting with `_`

  * **use_db_fields** (_False_) â whether to return database fields rather than user-facing fields, when applicable



Returns:
    

a tuple of field names

class fiftyone.core.sample.Sample(_filepath_ , _tags =None_, _metadata =None_, _** kwargs_)#
    

Bases: `_SampleMixin`, [`Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document")

A sample in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

Samples store all information associated with a particular piece of data in a dataset, including basic metadata about the data, one or more sets of labels (ground truth, user-provided, or FiftyOne-generated), and additional features associated with subsets of the data and/or label sets.

Note

[`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that are **in datasets** are singletons, i.e., `dataset[sample_id]` will always return the same [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instance.

Parameters:
    

  * **filepath** â the path to the data on disk. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **tags** (_None_) â a list of tags for the sample

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance

  * ****kwargs** â additional fields to dynamically set on the sample




**Methods:**

`reload`([hard,Â include_frames]) | Reloads the sample from the database.  
---|---  
`save`() | Saves the sample to the database.  
`from_frame`(frame[,Â filepath]) | Creates a sample from the given frame.  
`from_doc`(doc[,Â dataset]) | Creates a sample backed by the given document.  
`from_dict`(d) | Loads the sample from a JSON dictionary.  
`add_labels`(labels[,Â label_field,Â ...]) | Adds the given labels to the sample.  
`clear_field`(field_name) | Clears the value of a field of the document.  
`compute_metadata`([overwrite,Â skip_failures]) | Populates the `metadata` field of the sample.  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the sample that has not been added to the database.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(sample[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the given sample into this sample.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([include_frames,Â include_private]) | Serializes the sample to a JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
**Attributes:**

`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
---|---  
`dataset_id` |   
`field_names` | An ordered tuple of the public field names of this document.  
`filename` | The basename of the media's filepath.  
`in_dataset` | Whether the document has been added to a dataset.  
`media_type` | The media type of the sample.  
  
reload(_hard =False_, _include_frames =True_)#
    

Reloads the sample from the database.

Parameters:
    

  * **hard** (_False_) â whether to reload the sampleâs schema in addition to its field values. This is necessary if new fields may have been added to the dataset schema

  * **include_frames** (_True_) â whether to reload any in-memory frames of video samples




save()#
    

Saves the sample to the database.

classmethod from_frame(_frame_ , _filepath =None_)#
    

Creates a sample from the given frame.

Parameters:
    

  * **frame** â a [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame")

  * **filepath** (_None_) â the path to the corresponding image frame on disk, if not available



Returns:
    

a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

classmethod from_doc(_doc_ , _dataset =None_)#
    

Creates a sample backed by the given document.

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.sample.DatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument "fiftyone.core.odm.sample.DatasetSampleDocument") or [`fiftyone.core.odm.sample.NoDatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument "fiftyone.core.odm.sample.NoDatasetSampleDocument")

  * **dataset** (_None_) â the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") that the sample belongs to



Returns:
    

a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

classmethod from_dict(_d_)#
    

Loads the sample from a JSON dictionary.

The returned sample will not belong to a dataset.

Returns:
    

a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

add_labels(_labels_ , _label_field =None_, _confidence_thresh =None_, _classes =None_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the given labels to the sample.

The provided `labels` can be any of the following:

  * A [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, in which case the labels are directly saved in the specified `label_field`

  * A dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the labels are added as follows:
        
        for key, value in labels.items():
            sample[label_key(key)] = value
        

  * A dict mapping frame numbers to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {label_field: label}
                for frame_number, label in labels.items()
            }
        )
        

  * A dict mapping frame numbers to dicts mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {
                    label_key(key): value
                    for key, value in frame_dict.items()
                }
                for frame_number, frame_dict in labels.items()
            }
        )
        




In the above, the `label_key` function maps label dict keys to field names, and is defined from `label_field` as follows:
    
    
    if isinstance(label_field, dict):
        label_key = lambda k: label_field.get(k, k)
    elif label_field is not None:
        label_key = lambda k: label_field + "_" + k
    else:
        label_key = lambda k: k
    

Parameters:
    

  * **labels** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") or dict of labels per the description above

  * **label_field** (_None_) â the sample field, prefix, or dict defining in which field(s) to save the labels

  * **confidence_thresh** (_None_) â an optional confidence threshold to apply to any applicable labels before saving them

  * **classes** (_None_) â an optional iterable of classes to which to restrict any applicable labels generated by the model

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic attributes




clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

compute_metadata(_overwrite =False_, _skip_failures =False_)#
    

Populates the `metadata` field of the sample.

Parameters:
    

  * **overwrite** (_False_) â whether to overwrite existing metadata

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if metadata cannot be computed




copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the sample that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property dataset_id#
    

property field_names#
    

An ordered tuple of the public field names of this document.

property filename#
    

The basename of the mediaâs filepath.

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

The returned document will not belong to a dataset.

Parameters:
    

**s** â the JSON string

Returns:
    

a `Document`

get_field(_field_name_)#
    

Gets the value of a field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has the given field.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_dataset#
    

Whether the document has been added to a dataset.

iter_fields(_include_id =False_, _include_timestamps =False_)#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Parameters:
    

  * **include_id** (_False_) â whether to include the `id` field

  * **include_timestamps** (_False_) â whether to include the `created_at` and `last_modified_at` fields



Returns:
    

an iterator that emits `(name, value)` tuples

property media_type#
    

The media type of the sample.

merge(_sample_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the fields of the given sample into this sample.

The behavior of this method is highly customizable. By default, all top-level fields from the provided sample are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both samples are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the dataset schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input sample fields to different field names of this sample




Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. May contain frame fields for video samples. This can also be a dict mapping field names of the input sample to field names of this sample

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge. May contain frame fields for video samples

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided sample

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

  * **ValueError** â if `field_name` is not an allowed field name

  * **AttributeError** â if the field does not exist and `create == False`




to_dict(_include_frames =False_, _include_private =False_)#
    

Serializes the sample to a JSON dictionary.

Parameters:
    

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **include_private** (_False_) â whether to include private fields



Returns:
    

a JSON dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

The document ID and private fields are excluded in this representation.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo_dict(_include_id =False_)#
    

Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.

Parameters:
    

**include_id** (_False_) â whether to include the document ID

Returns:
    

a BSON dict

update_fields(_fields_dict_ , _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Sets the dictionary of fields on the document.

Parameters:
    

  * **fields_dict** â a dict mapping field names to values

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the document schema. If False, an error is raised if any fields are not in the document schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

**AttributeError** â if `expand_schema == False` and a field does not exist

class fiftyone.core.sample.SampleView(_doc_ , _view_ , _selected_fields =None_, _excluded_fields =None_, _filtered_fields =None_)#
    

Bases: `_SampleMixin`, [`DocumentView`](api__fiftyone.core.document.md#fiftyone.core.document.DocumentView "fiftyone.core.document.DocumentView")

A view into a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") in a dataset.

Like [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances, the fields of a `SampleView` instance can be modified, new fields can be created, and any changes can be saved to the database.

`SampleView` instances differ from [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances in the following ways:

  * A sample view may contain only a subset of the fields of its source sample, either by selecting and/or excluding specific fields

  * A sample view may contain array fields or embedded array fields that have been filtered, thus containing only a subset of the array elements from the source sample

  * Excluded fields of a sample view may not be accessed or modified




Note

Sample views should never be created manually; they are generated when accessing the samples in a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

Parameters:
    

  * **doc** â a `fiftyone.core.odm.mixins.DatasetSampleDocument`

  * **view** â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") that the sample belongs to

  * **selected_fields** (_None_) â a set of field names that this sample view is restricted to, if any

  * **excluded_fields** (_None_) â a set of field names that are excluded from this sample view, if any

  * **filtered_fields** (_None_) â a set of field names of list fields that are filtered in this sample view, if any




**Methods:**

`to_dict`([include_frames,Â include_private]) | Serializes the sample view to a JSON dictionary.  
---|---  
`save`() | Saves the sample view to the database.  
`add_labels`(labels[,Â label_field,Â ...]) | Adds the given labels to the sample.  
`clear_field`(field_name) | Clears the value of a field of the document.  
`compute_metadata`([overwrite,Â skip_failures]) | Populates the `metadata` field of the sample.  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the sample that has not been added to the database.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(sample[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the given sample into this sample.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
**Attributes:**

`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
---|---  
`dataset_id` |   
`excluded_field_names` | The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.  
`field_names` | An ordered tuple of field names of this document view.  
`filename` | The basename of the media's filepath.  
`filtered_field_names` | The set of field names or `embedded.field.names` that have been filtered on this document view, or `None` if no fields are filtered.  
`in_dataset` | Whether the document has been added to a dataset.  
`media_type` | The media type of the sample.  
`selected_field_names` | The set of field names that are selected on this document view, or `None` if no fields are explicitly selected.  
  
to_dict(_include_frames =False_, _include_private =False_)#
    

Serializes the sample view to a JSON dictionary.

Parameters:
    

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **include_private** (_False_) â whether to include private fields



Returns:
    

a JSON dict

save()#
    

Saves the sample view to the database.

Warning

This will permanently delete any omitted or filtered contents from the source dataset.

add_labels(_labels_ , _label_field =None_, _confidence_thresh =None_, _classes =None_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the given labels to the sample.

The provided `labels` can be any of the following:

  * A [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, in which case the labels are directly saved in the specified `label_field`

  * A dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the labels are added as follows:
        
        for key, value in labels.items():
            sample[label_key(key)] = value
        

  * A dict mapping frame numbers to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {label_field: label}
                for frame_number, label in labels.items()
            }
        )
        

  * A dict mapping frame numbers to dicts mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {
                    label_key(key): value
                    for key, value in frame_dict.items()
                }
                for frame_number, frame_dict in labels.items()
            }
        )
        




In the above, the `label_key` function maps label dict keys to field names, and is defined from `label_field` as follows:
    
    
    if isinstance(label_field, dict):
        label_key = lambda k: label_field.get(k, k)
    elif label_field is not None:
        label_key = lambda k: label_field + "_" + k
    else:
        label_key = lambda k: k
    

Parameters:
    

  * **labels** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") or dict of labels per the description above

  * **label_field** (_None_) â the sample field, prefix, or dict defining in which field(s) to save the labels

  * **confidence_thresh** (_None_) â an optional confidence threshold to apply to any applicable labels before saving them

  * **classes** (_None_) â an optional iterable of classes to which to restrict any applicable labels generated by the model

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic attributes




clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

compute_metadata(_overwrite =False_, _skip_failures =False_)#
    

Populates the `metadata` field of the sample.

Parameters:
    

  * **overwrite** (_False_) â whether to overwrite existing metadata

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if metadata cannot be computed




copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the sample that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property dataset_id#
    

property excluded_field_names#
    

The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.

property field_names#
    

An ordered tuple of field names of this document view.

This may be a subset of all fields of the document if fields have been selected or excluded.

property filename#
    

The basename of the mediaâs filepath.

property filtered_field_names#
    

The set of field names or `embedded.field.names` that have been filtered on this document view, or `None` if no fields are filtered.

get_field(_field_name_)#
    

Gets the value of a field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has the given field.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_dataset#
    

Whether the document has been added to a dataset.

iter_fields(_include_id =False_, _include_timestamps =False_)#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Parameters:
    

  * **include_id** (_False_) â whether to include the `id` field

  * **include_timestamps** (_False_) â whether to include the `created_at` and `last_modified_at` fields



Returns:
    

an iterator that emits `(name, value)` tuples

property media_type#
    

The media type of the sample.

merge(_sample_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the fields of the given sample into this sample.

The behavior of this method is highly customizable. By default, all top-level fields from the provided sample are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both samples are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the dataset schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input sample fields to different field names of this sample




Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. May contain frame fields for video samples. This can also be a dict mapping field names of the input sample to field names of this sample

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge. May contain frame fields for video samples

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided sample

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




property selected_field_names#
    

The set of field names that are selected on this document view, or `None` if no fields are explicitly selected.

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

  * **ValueError** â if `field_name` is not an allowed field name

  * **AttributeError** â if the field does not exist and `create == False`




to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

The document ID and private fields are excluded in this representation.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo_dict(_include_id =False_)#
    

Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.

Parameters:
    

**include_id** (_False_) â whether to include the document ID

Returns:
    

a BSON dict

update_fields(_fields_dict_ , _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Sets the dictionary of fields on the document.

Parameters:
    

  * **fields_dict** â a dict mapping field names to values

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the document schema. If False, an error is raised if any fields are not in the document schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

**AttributeError** â if `expand_schema == False` and a field does not exist

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
