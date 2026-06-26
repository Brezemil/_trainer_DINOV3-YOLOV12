---
source_url: https://docs.voxel51.com/api/fiftyone.core.document.html
---

# fiftyone.core.document#

Base classes for objects that are backed by database documents.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Document`(**kwargs) | Abstract base class for objects that are associated with [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") instances and are backed by documents in database collections.  
---|---  
`DocumentView`(doc,Â view[,Â selected_fields,Â ...]) | A view into a `Document` in a dataset.  
  
class fiftyone.core.document.Document(_** kwargs_)#
    

Bases: `_Document`

Abstract base class for objects that are associated with [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") instances and are backed by documents in database collections.

Document subclasses whose in-dataset instances should be singletons can inherit this behavior by deriving from the [`fiftyone.core.singletons.DocumentSingleton`](api__fiftyone.core.singletons.md#fiftyone.core.singletons.DocumentSingleton "fiftyone.core.singletons.DocumentSingleton") metaclass.

Parameters:
    

****kwargs** â field names and values

**Methods:**

`copy`([fields,Â omit_fields]) | Returns a deep copy of the document that has not been added to the database.  
---|---  
`reload`([hard]) | Reloads the document from the database.  
`from_doc`(doc[,Â dataset]) | Creates a document backed by the given database document.  
`from_dict`(d) | Loads the document from a JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`clear_field`(field_name) | Clears the value of a field of the document.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(document[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the document into this document.  
`save`() | Saves the document to the database.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([include_private]) | Serializes the document to a JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
**Attributes:**

`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
---|---  
`field_names` | An ordered tuple of the public field names of this document.  
`in_dataset` | Whether the document has been added to a dataset.  
  
copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the document that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a `Document`

reload(_hard =False_)#
    

Reloads the document from the database.

Parameters:
    

**hard** (_False_) â whether to reload the documentâs schema in addition to its field values. This is necessary if new fields may have been added to the document schema

classmethod from_doc(_doc_ , _dataset =None_)#
    

Creates a document backed by the given database document.

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.document.Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

  * **dataset** (_None_) â the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") that the document belongs to, if any



Returns:
    

a `Document`

classmethod from_dict(_d_)#
    

Loads the document from a JSON dictionary.

The returned document will not belong to a dataset.

Returns:
    

a `Document`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

The returned document will not belong to a dataset.

Parameters:
    

**s** â the JSON string

Returns:
    

a `Document`

clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property field_names#
    

An ordered tuple of the public field names of this document.

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
    

Saves the document to the database.

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

class fiftyone.core.document.DocumentView(_doc_ , _view_ , _selected_fields =None_, _excluded_fields =None_, _filtered_fields =None_)#
    

Bases: `_Document`

A view into a `Document` in a dataset.

Like `Document` instances, the fields of a `DocumentView` instance can be modified, new fields can be created, and any changes can be saved to the database.

`DocumentView` instances differ from `Document` instances in the following ways:

  * A document view may contain only a subset of the fields of its source document, either by selecting and/or excluding specific fields

  * A document view may contain array fields or embedded array fields that have been filtered, thus containing only a subset of the array elements from the source document

  * Excluded fields of a document view may not be accessed or modified




Note

`DocumentView.save()` will not delete any excluded fields or filtered array elements from the source document.

Document views should never be created manually; they are generated when accessing the contents of a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.document.Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document")

  * **view** â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") that the document belongs to

  * **selected_fields** (_None_) â a set of field names that this document view is restricted to, if any

  * **excluded_fields** (_None_) â a set of field names that are excluded from this document view, if any

  * **filtered_fields** (_None_) â a set of field names of array fields that are filtered in this document view, if any




**Attributes:**

`field_names` | An ordered tuple of field names of this document view.  
---|---  
`selected_field_names` | The set of field names that are selected on this document view, or `None` if no fields are explicitly selected.  
`excluded_field_names` | The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.  
`filtered_field_names` | The set of field names or `embedded.field.names` that have been filtered on this document view, or `None` if no fields are filtered.  
`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
`in_dataset` | Whether the document has been added to a dataset.  
  
**Methods:**

`has_field`(field_name) | Determines whether the document has the given field.  
---|---  
`get_field`(field_name) | Gets the value of a field of the document.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`clear_field`(field_name) | Clears the value of a field of the document.  
`to_dict`([include_private]) | Serializes the document to a JSON dictionary.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the document that has not been added to the database.  
`save`() | Saves the document view to the database.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(document[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the document into this document.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
property field_names#
    

An ordered tuple of field names of this document view.

This may be a subset of all fields of the document if fields have been selected or excluded.

property selected_field_names#
    

The set of field names that are selected on this document view, or `None` if no fields are explicitly selected.

property excluded_field_names#
    

The set of field names that are excluded on this document view, or `None` if no fields are explicitly excluded.

property filtered_field_names#
    

The set of field names or `embedded.field.names` that have been filtered on this document view, or `None` if no fields are filtered.

has_field(_field_name_)#
    

Determines whether the document has the given field.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

get_field(_field_name_)#
    

Gets the value of a field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

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




clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

to_dict(_include_private =False_)#
    

Serializes the document to a JSON dictionary.

Parameters:
    

**include_private** (_False_) â whether to include private fields

Returns:
    

a JSON dict

to_mongo_dict(_include_id =False_)#
    

Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.

Parameters:
    

**include_id** (_False_) â whether to include the document ID

Returns:
    

a BSON dict

copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the document that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a `Document`

save()#
    

Saves the document view to the database.

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

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

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

The document ID and private fields are excluded in this representation.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

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
