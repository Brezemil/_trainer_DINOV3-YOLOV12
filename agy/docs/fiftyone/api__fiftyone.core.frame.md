---
source_url: https://docs.voxel51.com/api/fiftyone.core.frame.html
---

# fiftyone.core.frame#

Video frames.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_default_frame_fields`([include_private,Â ...]) | Returns the default fields present on all frames.  
---|---  
  
**Classes:**

`Frames`(sample) | An ordered dictionary of `Frame` instances keyed by frame number representing the frames of a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").  
---|---  
`FramesView`(sample_view) | An ordered dictionary of `FrameView` instances keyed by frame number representing the frames of a video [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView").  
`Frame`(**kwargs) | A frame in a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").  
`FrameView`(doc,Â view[,Â selected_fields,Â ...]) | A view into a `Frame` in a video dataset.  
  
fiftyone.core.frame.get_default_frame_fields(_include_private =False_, _use_db_fields =False_)#
    

Returns the default fields present on all frames.

Parameters:
    

  * **include_private** (_False_) â whether to include fields starting with `_`

  * **use_db_fields** (_False_) â whether to return database fields rather than user-facing fields, when applicable



Returns:
    

a tuple of field names

class fiftyone.core.frame.Frames(_sample_)#
    

Bases: `object`

An ordered dictionary of `Frame` instances keyed by frame number representing the frames of a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").

`Frames` instances behave like `defaultdict(Frame)` instances; an empty `Frame` instance is returned when accessing a new frame number.

`Frames` instances should never be created manually; they are instantiated automatically when video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances are created.

Parameters:
    

**sample** â the [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") to which the frames are attached

**Attributes:**

`field_names` | An ordered tuple of the names of the fields on the frames.  
---|---  
  
**Methods:**

`first`() | Returns the first `Frame` for the sample.  
---|---  
`last`() | Returns the last `Frame` for the sample.  
`head`([num_frames]) | Returns a list of the first few frames for the sample.  
`tail`([num_frames]) | Returns a list of the last few frames for the sample.  
`keys`() | Returns an iterator over the frame numbers with labels in the sample.  
`items`() | Returns an iterator over the frame numberes and `Frame` instances for the sample.  
`values`() | Returns an iterator over the `Frame` instances for the sample.  
`add_frame`(frame_number,Â frame[,Â ...]) | Adds the frame to this instance.  
`delete_frame`(frame_number) | Deletes the given frame number from this instance.  
`update`(frames[,Â overwrite,Â expand_schema,Â ...]) | Adds the frame labels to this instance.  
`merge`(frames[,Â fields,Â omit_fields,Â ...]) | Merges the given frames into this instance.  
`clear`() | Removes all frames from this sample.  
`save`() | Saves all frames for the sample to the database.  
`reload`([hard]) | Reloads all frames for the sample from the database.  
  
property field_names#
    

An ordered tuple of the names of the fields on the frames.

first()#
    

Returns the first `Frame` for the sample.

Returns:
    

a `Frame`

last()#
    

Returns the last `Frame` for the sample.

Returns:
    

a `Frame`

head(_num_frames =3_)#
    

Returns a list of the first few frames for the sample.

If fewer than `num_frames` frames exist, only the available frames are returned.

Parameters:
    

**num_frames** (_3_) â the number of frames

Returns:
    

a list of `Frame` objects

tail(_num_frames =3_)#
    

Returns a list of the last few frames for the sample.

If fewer than `num_frames` frames exist, only the available frames are returned.

Parameters:
    

**num_frames** (_3_) â the number of frames

Returns:
    

a list of `Frame` objects

keys()#
    

Returns an iterator over the frame numbers with labels in the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits frame numbers

items()#
    

Returns an iterator over the frame numberes and `Frame` instances for the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits `(frame_number, Frame)` tuples

values()#
    

Returns an iterator over the `Frame` instances for the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits `Frame` instances

add_frame(_frame_number_ , _frame_ , _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the frame to this instance.

If an existing frame with the same frame number exists, it is overwritten.

If the provided frame is a `Frame` instance that does not belong to a dataset, it is updated in-place to reflect its membership in this dataset. Otherwise, the provided frame is not modified.

Parameters:
    

  * **frame_number** â the frame number

  * **frame** â a `Frame` or `FrameView`

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




delete_frame(_frame_number_)#
    

Deletes the given frame number from this instance.

Parameters:
    

**frame_number** â the frame number

update(_frames_ , _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the frame labels to this instance.

Parameters:
    

  * **frames** â 

can be any of the following

    * a `Frames` instance

    * a dictionary mapping frame numbers to `Frame` instances

    * a dictionary mapping frame numbers to dictionaries mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **overwrite** (_True_) â whether to overwrite existing frames

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




merge(_frames_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the given frames into this instance.

The behavior of this method is highly customizable. By default, all top-level fields from the provided frames are merged into existing frames with the same frame numbers (and new frames created as necessary), overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both frames are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the frame schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input frame fields to different field names of this frame




Parameters:
    

  * **frames** â 

can be any of the following

    * a `Frames` instance

    * a dictionary mapping frame numbers to `Frame` instances

    * a dictionary mapping frame numbers to dictionaries mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. This can also be a dict mapping field names of the input frame to field names of this frame

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided frames

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




clear()#
    

Removes all frames from this sample.

save()#
    

Saves all frames for the sample to the database.

reload(_hard =False_)#
    

Reloads all frames for the sample from the database.

Parameters:
    

**hard** (_False_) â whether to reload the frame schema in addition to the field values for the frames. This is necessary if new fields may have been added to the datasetâs frame schema

class fiftyone.core.frame.FramesView(_sample_view_)#
    

Bases: `Frames`

An ordered dictionary of `FrameView` instances keyed by frame number representing the frames of a video [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView").

`FramesView` instances behave like `defaultdict(FrameView)` instances; an empty `FrameView` instance is returned when accessing a new frame number.

`FramesView` instances should never be created manually; they are instantiated automatically when video [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances are created.

Parameters:
    

**sample_view** â the [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") to which the frames are attached

**Attributes:**

`field_names` | An ordered tuple of the names of the fields on the frames.  
---|---  
  
**Methods:**

`add_frame`(frame_number,Â frame[,Â ...]) | Adds the frame to this instance.  
---|---  
`reload`() | Reloads the view into the frames of the attached sample.  
`save`() | Saves all frames for the sample to the database.  
`clear`() | Removes all frames from this sample.  
`delete_frame`(frame_number) | Deletes the given frame number from this instance.  
`first`() | Returns the first `Frame` for the sample.  
`head`([num_frames]) | Returns a list of the first few frames for the sample.  
`items`() | Returns an iterator over the frame numberes and `Frame` instances for the sample.  
`keys`() | Returns an iterator over the frame numbers with labels in the sample.  
`last`() | Returns the last `Frame` for the sample.  
`merge`(frames[,Â fields,Â omit_fields,Â ...]) | Merges the given frames into this instance.  
`tail`([num_frames]) | Returns a list of the last few frames for the sample.  
`update`(frames[,Â overwrite,Â expand_schema,Â ...]) | Adds the frame labels to this instance.  
`values`() | Returns an iterator over the `Frame` instances for the sample.  
  
property field_names#
    

An ordered tuple of the names of the fields on the frames.

add_frame(_frame_number_ , _frame_ , _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the frame to this instance.

If an existing frame with the same frame number exists, it is overwritten.

Unlike `Frames.add_frame`, the provided frame is never modified in-place. Instead, a new `FrameView` is constructed internally with the contents of the provided frame.

Parameters:
    

  * **frame_number** â the frame number

  * **frame** â a `Frame` or `FrameView`

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




reload()#
    

Reloads the view into the frames of the attached sample.

Calling this method has the following effects:

  * Clears the in-memory cache of `FrameView` instances that you have loaded via this object. Any frames that you subsequently access will be loaded directly from the database

  * Any additions, modifications, or deletions to frame views that you have loaded from this instance but not committed to the database by calling `save()` will be discarded




Note

`FrameView` objects are not singletons, so calling this method will not have any effect on `FrameView` instances that you have **previously** loaded via this object

Parameters:
    

**hard** (_False_) â whether to reload the frame schema in addition to the field values for the frames. This is necessary if new fields may have been added to the datasetâs frame schema

save()#
    

Saves all frames for the sample to the database.

clear()#
    

Removes all frames from this sample.

delete_frame(_frame_number_)#
    

Deletes the given frame number from this instance.

Parameters:
    

**frame_number** â the frame number

first()#
    

Returns the first `Frame` for the sample.

Returns:
    

a `Frame`

head(_num_frames =3_)#
    

Returns a list of the first few frames for the sample.

If fewer than `num_frames` frames exist, only the available frames are returned.

Parameters:
    

**num_frames** (_3_) â the number of frames

Returns:
    

a list of `Frame` objects

items()#
    

Returns an iterator over the frame numberes and `Frame` instances for the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits `(frame_number, Frame)` tuples

keys()#
    

Returns an iterator over the frame numbers with labels in the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits frame numbers

last()#
    

Returns the last `Frame` for the sample.

Returns:
    

a `Frame`

merge(_frames_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the given frames into this instance.

The behavior of this method is highly customizable. By default, all top-level fields from the provided frames are merged into existing frames with the same frame numbers (and new frames created as necessary), overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both frames are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the frame schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input frame fields to different field names of this frame




Parameters:
    

  * **frames** â 

can be any of the following

    * a `Frames` instance

    * a dictionary mapping frame numbers to `Frame` instances

    * a dictionary mapping frame numbers to dictionaries mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. This can also be a dict mapping field names of the input frame to field names of this frame

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided frames

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




tail(_num_frames =3_)#
    

Returns a list of the last few frames for the sample.

If fewer than `num_frames` frames exist, only the available frames are returned.

Parameters:
    

**num_frames** (_3_) â the number of frames

Returns:
    

a list of `Frame` objects

update(_frames_ , _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the frame labels to this instance.

Parameters:
    

  * **frames** â 

can be any of the following

    * a `Frames` instance

    * a dictionary mapping frame numbers to `Frame` instances

    * a dictionary mapping frame numbers to dictionaries mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **overwrite** (_True_) â whether to overwrite existing frames

  * **expand_schema** (_True_) â whether to dynamically add new frame fields encountered to the dataset schema. If False, an error is raised if the frameâs schema is not a subset of the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




values()#
    

Returns an iterator over the `Frame` instances for the sample.

The frames are traversed in ascending order.

Returns:
    

a generator that emits `Frame` instances

class fiftyone.core.frame.Frame(_** kwargs_)#
    

Bases: [`Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document")

A frame in a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").

Frames store all information associated with a particular frame of a video, including one or more sets of labels (ground truth, user-provided, or FiftyOne-generated) as well as additional features associated with subsets of the data and/or label sets.

Note

`Frame` instances that are attached to samples **in datasets** are singletons, i.e., `sample.frames[frame_number]` will always return the same `Frame` instance.

Parameters:
    

****kwargs** â frame fields and values

**Attributes:**

`dataset_id` |   
---|---  
`sample_id` |   
`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
`field_names` | An ordered tuple of the public field names of this document.  
`in_dataset` | Whether the document has been added to a dataset.  
  
**Methods:**

`save`() | Saves the frame to the database.  
---|---  
`clear_field`(field_name) | Clears the value of a field of the document.  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the document that has not been added to the database.  
`from_dict`(d) | Loads the document from a JSON dictionary.  
`from_doc`(doc[,Â dataset]) | Creates a document backed by the given database document.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(document[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the document into this document.  
`reload`([hard]) | Reloads the document from the database.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([include_private]) | Serializes the document to a JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
property dataset_id#
    

property sample_id#
    

save()#
    

Saves the frame to the database.

clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the document that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a `Document`

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property field_names#
    

An ordered tuple of the public field names of this document.

classmethod from_dict(_d_)#
    

Loads the document from a JSON dictionary.

The returned document will not belong to a dataset.

Returns:
    

a `Document`

classmethod from_doc(_doc_ , _dataset =None_)#
    

Creates a document backed by the given database document.

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.document.Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

  * **dataset** (_None_) â the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") that the document belongs to, if any



Returns:
    

a `Document`

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

merge(_document_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the fields of the document into this document.

The behavior of this method is highly customizable. By default, all top-level fields from the provided document are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both documents are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the document schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input document fields to different field names of this document




Parameters:
    

  * **document** â a `Document` or `DocumentView` of the same type

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. This can also be a dict mapping field names of the input document to field names of this document

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided document

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the document schema. If False, an error is raised if any fields are not in the document schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

**AttributeError** â if `expand_schema == False` and a field does not exist

reload(_hard =False_)#
    

Reloads the document from the database.

Parameters:
    

**hard** (_False_) â whether to reload the documentâs schema in addition to its field values. This is necessary if new fields may have been added to the document schema

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




to_dict(_include_private =False_)#
    

Serializes the document to a JSON dictionary.

Parameters:
    

**include_private** (_False_) â whether to include private fields

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

class fiftyone.core.frame.FrameView(_doc_ , _view_ , _selected_fields =None_, _excluded_fields =None_, _filtered_fields =None_)#
    

Bases: [`DocumentView`](api__fiftyone.core.document.md#fiftyone.core.document.DocumentView "fiftyone.core.document.DocumentView")

A view into a `Frame` in a video dataset.

Like `Frame` instances, the fields of a `FrameView` instance can be modified, new fields can be created, and any changes can be saved to the database.

`FrameView` instances differ from `Frame` instances in the following ways:

  * A frame view may contain only a subset of the fields of its source frame, either by selecting and/or excluding specific fields

  * A frame view may contain array fields or embedded array fields that have been filtered, thus containing only a subset of the array elements from the source frame

  * Excluded fields of a frame view may not be accessed or modified




Note

`FrameView.save()` will not delete any excluded fields or filtered array elements from the source frame.

Frame views should never be created manually; they are generated when accessing the frames in a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.frame.DatasetFrameDocument`](api__fiftyone.core.odm.frame.md#fiftyone.core.odm.frame.DatasetFrameDocument "fiftyone.core.odm.frame.DatasetFrameDocument")

  * **view** â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") that the frame belongs to

  * **selected_fields** (_None_) â a set of field names that this frame view is restricted to, if any

  * **excluded_fields** (_None_) â a set of field names that are excluded from this frame view, if any

  * **filtered_fields** (_None_) â a set of field names of list fields that are filtered in this frame view, if any




**Attributes:**

`dataset_id` |   
---|---  
`sample_id` |   
`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
`excluded_field_names` | The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.  
`field_names` | An ordered tuple of field names of this document view.  
`filtered_field_names` | The set of field names or `embedded.field.names` that have been filtered on this document view, or `None` if no fields are filtered.  
`in_dataset` | Whether the document has been added to a dataset.  
`selected_field_names` | The set of field names that are selected on this document view, or `None` if no fields are explicitly selected.  
  
**Methods:**

`clear_field`(field_name) | Clears the value of a field of the document.  
---|---  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the document that has not been added to the database.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(document[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the document into this document.  
`save`() | Saves the document view to the database.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([include_private]) | Serializes the document to a JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
property dataset_id#
    

property sample_id#
    

clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the document that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a `Document`

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property excluded_field_names#
    

The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.

property field_names#
    

An ordered tuple of field names of this document view.

This may be a subset of all fields of the document if fields have been selected or excluded.

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

merge(_document_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the fields of the document into this document.

The behavior of this method is highly customizable. By default, all top-level fields from the provided document are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both documents are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the document schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input document fields to different field names of this document




Parameters:
    

  * **document** â a `Document` or `DocumentView` of the same type

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. This can also be a dict mapping field names of the input document to field names of this document

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided document

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the document schema. If False, an error is raised if any fields are not in the document schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

**AttributeError** â if `expand_schema == False` and a field does not exist

save()#
    

Saves the document view to the database.

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




to_dict(_include_private =False_)#
    

Serializes the document to a JSON dictionary.

Parameters:
    

**include_private** (_False_) â whether to include private fields

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
