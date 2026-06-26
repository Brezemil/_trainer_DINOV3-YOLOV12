---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.mixins.html
---

# fiftyone.core.odm.mixins#

Mixins and helpers for dataset backing documents.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`get_default_fields`(cls[,Â include_private,Â ...]) | Gets the default fields present on all instances of the given `DatasetMixin` class.  
---|---  
  
**Classes:**

`DatasetMixin`() | Mixin interface for [`fiftyone.core.odm.document.Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document") subclasses that are backed by a dataset.  
---|---  
`NoDatasetMixin`() | Mixin for [`fiftyone.core.odm.document.SerializableDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument "fiftyone.core.odm.document.SerializableDocument") subtypes that are not backed by a dataset.  
  
fiftyone.core.odm.mixins.get_default_fields(_cls_ , _include_private =False_, _use_db_fields =False_)#
    

Gets the default fields present on all instances of the given `DatasetMixin` class.

Parameters:
    

  * **cls** â the `DatasetMixin` class

  * **include_private** (_False_) â whether to include fields starting with `_`

  * **use_db_fields** (_False_) â whether to return database fields rather than user-facing fields, when applicable



Returns:
    

a tuple of field names

class fiftyone.core.odm.mixins.DatasetMixin#
    

Bases: `object`

Mixin interface for [`fiftyone.core.odm.document.Document`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.Document "fiftyone.core.odm.document.Document") subclasses that are backed by a dataset.

**Attributes:**

`collection_name` |   
---|---  
`field_names` |   
  
**Methods:**

`get_field`(field_name) |   
---|---  
`set_field`(field_name,Â value[,Â create,Â ...]) |   
`clear_field`(field_name) |   
`get_field_schema`([ftype,Â embedded_doc_type,Â ...]) | Returns a schema dictionary describing the fields of this document.  
`merge_field_schema`(schema[,Â expand_schema,Â ...]) | Merges the field schema into this document.  
`add_field`(path,Â ftype[,Â embedded_doc_type,Â ...]) | Adds a new field or embedded field to the document, if necessary.  
`add_implied_field`(path,Â value[,Â ...]) | Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.  
  
property collection_name#
    

property field_names#
    

get_field(_field_name_)#
    

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_, __enforce_read_only =True_)#
    

clear_field(_field_name_)#
    

classmethod get_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of this document.

If the document belongs to a dataset, the schema will apply to all documents in the collection.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of field types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **flat** (_False_) â whether to return a flattened schema where all embedded document fields are included as top-level keys

  * **unwind** (_True_) â whether to traverse into list fields. Only applicable when `flat=True`

  * **mode** (_None_) â whether to apply the above constraints before and/or after flattening the schema. Only applicable when `flat=True`. Supported values are `("before", "after", "both")`. The default is `"after"`



Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances

classmethod merge_field_schema(_schema_ , _expand_schema =True_, _recursive =True_, _validate =True_, _overwrite =False_)#
    

Merges the field schema into this document.

Parameters:
    

  * **schema** â a dict mapping field names or `embedded.field.names` to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that fields already exist with consistent types (False)

  * **recursive** (_True_) â whether to recursively merge embedded document fields

  * **validate** (_True_) â whether to validate fields against existing fields at the same path

  * **overwrite** (_False_) â whether to overwrite the editable metadata of existing fields



Returns:
    

True/False whether any new fields were added

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name or a new field is found but `expand_schema == False`

classmethod add_field(_path_ , _ftype_ , _embedded_doc_type =None_, _subfield =None_, _fields =None_, _description =None_, _info =None_, _read_only =False_, _expand_schema =True_, _recursive =True_, _validate =True_, _** kwargs_)#
    

Adds a new field or embedded field to the document, if necessary.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **ftype** â the field type to create. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â the [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") type of the field. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **subfield** (_None_) â the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") type of the contained field. Only applicable when `ftype` is [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") or [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")

  * **fields** (_None_) â a list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances defining embedded document attributes. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field should be read-only

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

classmethod add_implied_field(_path_ , _value_ , _expand_schema =True_, _dynamic =False_, _recursive =True_, _validate =True_)#
    

Adds the field or embedded field to the document, if necessary, inferring the field type from the provided value.

Parameters:
    

  * **path** â the field name or `embedded.field.name`

  * **value** â the field value

  * **expand_schema** (_True_) â whether to add new fields to the schema (True) or simply validate that the field already exists with a consistent type (False)

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields

  * **recursive** (_True_) â whether to recursively add embedded document fields

  * **validate** (_True_) â whether to validate the field against an existing field at the same path



Returns:
    

True/False whether one or more fields or embedded fields were added to the document or its children

Raises:
    

**ValueError** â if a field in the schema is not compliant with an existing field of the same name

class fiftyone.core.odm.mixins.NoDatasetMixin#
    

Bases: `object`

Mixin for [`fiftyone.core.odm.document.SerializableDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.SerializableDocument "fiftyone.core.odm.document.SerializableDocument") subtypes that are not backed by a dataset.

**Attributes:**

`field_names` |   
---|---  
`in_db` |   
  
**Methods:**

`has_field`(field_name) |   
---|---  
`get_field`(field_name) |   
`set_field`(field_name,Â value[,Â create,Â ...]) |   
`clear_field`(field_name) |   
`to_dict`([extended]) |   
`from_dict`(d[,Â extended]) |   
`save`() |   
`reload`() |   
`delete`() |   
  
property field_names#
    

property in_db#
    

has_field(_field_name_)#
    

get_field(_field_name_)#
    

set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

clear_field(_field_name_)#
    

to_dict(_extended =False_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

save()#
    

reload()#
    

delete()#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
