---
source_url: https://docs.voxel51.com/api/fiftyone.core.odm.utils.html
---

# fiftyone.core.odm.utils#

Utilities for documents.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`serialize_value`(value[,Â extended]) | Serializes the given value.  
---|---  
`deserialize_value`(value) | Deserializes the given value.  
`validate_field_name`(field_name[,Â ...]) | Verifies that the given field name is valid.  
`create_field`(name,Â ftype[,Â ...]) | Creates the field defined by the given specification.  
`create_implied_field`(path,Â value[,Â dynamic]) | Creates the field for the given value.  
`get_field_kwargs`(field) | Constructs the field keyword arguments dictionary for the given field.  
`get_implied_field_kwargs`(value[,Â dynamic]) | Infers the field keyword arguments dictionary for a field that can hold the given value.  
`validate_fields_match`(name,Â field,Â ...) | Validates that the types of the given fields match.  
`load_dataset`(*args,Â **kwargs) |   
  
**Classes:**

`DocumentRegistry`() | A registry of [`fiftyone.core.odm.document.MongoEngineBaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument "fiftyone.core.odm.document.MongoEngineBaseDocument") classes found when importing data from the database.  
---|---  
  
**Exceptions:**

`DocumentRegistryError` | Error raised when an unknown document class is encountered.  
---|---  
  
fiftyone.core.odm.utils.serialize_value(_value_ , _extended =False_)#
    

Serializes the given value.

Parameters:
    

  * **value** â the value

  * **extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format



Returns:
    

the serialized value

fiftyone.core.odm.utils.deserialize_value(_value_)#
    

Deserializes the given value.

Parameters:
    

**value** â the serialized value

Returns:
    

the value

fiftyone.core.odm.utils.validate_field_name(_field_name_ , _media_type =None_, _is_frame_field =False_)#
    

Verifies that the given field name is valid.

Parameters:
    

  * **field_name** â the field name

  * **media_type** (_None_) â the media type of the sample, if known

  * **is_frame_field** (_False_) â whether this is a frame-level field



Raises:
    

**ValueError** â if the field name is invalid

fiftyone.core.odm.utils.create_field(_name_ , _ftype_ , _embedded_doc_type =None_, _subfield =None_, _fields =None_, _db_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Creates the field defined by the given specification.

Note

This method is used exclusively to create user-defined (non-default) fields. Any parameters accepted here must be stored on [`fiftyone.core.odm.dataset.SampleFieldDocument`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.SampleFieldDocument "fiftyone.core.odm.dataset.SampleFieldDocument") or else datasets will âloseâ any additional decorations when they are loaded from the database.

Parameters:
    

  * **name** â the field name

  * **ftype** â the field type to create. Must be a subclass of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **embedded_doc_type** (_None_) â the [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") type of the field. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **subfield** (_None_) â the [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") type of the contained field. Only applicable when `ftype` is [`fiftyone.core.fields.ListField`](api__fiftyone.core.fields.md#fiftyone.core.fields.ListField "fiftyone.core.fields.ListField") or [`fiftyone.core.fields.DictField`](api__fiftyone.core.fields.md#fiftyone.core.fields.DictField "fiftyone.core.fields.DictField")

  * **fields** (_None_) â a list of [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances defining embedded document attributes. Only applicable when `ftype` is [`fiftyone.core.fields.EmbeddedDocumentField`](api__fiftyone.core.fields.md#fiftyone.core.fields.EmbeddedDocumentField "fiftyone.core.fields.EmbeddedDocumentField")

  * **db_field** (_None_) â the database field to store this field in. By default, `name` is used

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field should be read-only

  * **created_at** (_None_) â the datetime the field was created



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

fiftyone.core.odm.utils.create_implied_field(_path_ , _value_ , _dynamic =False_)#
    

Creates the field for the given value.

Parameters:
    

  * **path** â the field name or path

  * **value** â a value

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Returns:
    

a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

fiftyone.core.odm.utils.get_field_kwargs(_field_)#
    

Constructs the field keyword arguments dictionary for the given field.

Parameters:
    

**field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") or `str(field)` representation of one

Returns:
    

a field specification dict

fiftyone.core.odm.utils.get_implied_field_kwargs(_value_ , _dynamic =False_)#
    

Infers the field keyword arguments dictionary for a field that can hold the given value.

Parameters:
    

  * **value** â a value

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Returns:
    

a field specification dict

fiftyone.core.odm.utils.validate_fields_match(_name_ , _field_ , _existing_field_)#
    

Validates that the types of the given fields match.

Embedded document fields are not validated, if applicable.

Parameters:
    

  * **name** â the field name or `embedded.field.name`

  * **field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

  * **existing_field** â the reference [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")



Raises:
    

**ValueError** â if the fields do not match

class fiftyone.core.odm.utils.DocumentRegistry#
    

Bases: `object`

A registry of [`fiftyone.core.odm.document.MongoEngineBaseDocument`](api__fiftyone.core.odm.document.md#fiftyone.core.odm.document.MongoEngineBaseDocument "fiftyone.core.odm.document.MongoEngineBaseDocument") classes found when importing data from the database.

exception fiftyone.core.odm.utils.DocumentRegistryError#
    

Bases: `Exception`

Error raised when an unknown document class is encountered.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

fiftyone.core.odm.utils.load_dataset(_* args_, _** kwargs_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
