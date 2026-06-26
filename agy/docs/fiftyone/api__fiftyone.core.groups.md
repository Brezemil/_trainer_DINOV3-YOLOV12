---
source_url: https://docs.voxel51.com/api/fiftyone.core.groups.html
---

# fiftyone.core.groups#

Sample groups.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Group`(*args,Â **kwargs) | A named group membership.  
---|---  
  
**Functions:**

`get_group_slice_name`(sample,Â group_field) | Gets the group slice name for a sample, if available.  
---|---  
`is_group_field`(field) | Determines whether the given field is a group field.  
  
class fiftyone.core.groups.Group(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

A named group membership.

Parameters:
    

  * **id** (_None_) â the group ID

  * **name** (_None_) â the group name




**Attributes:**

`id` | An Object ID field.  
---|---  
`name` | A unicode string field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`element`(name) |   
---|---  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




name#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




element(_name_)#
    

STRICT = False#
    

clean()#
    

Hook for doing document level data cleaning (usually validation or assignment) before validation is run.

Any ValidationError raised by this method will not be associated with a particular field; it will have a special-case association with the field defined by NON_FIELD_ERRORS.

clear_field(_field_name_)#
    

Clears the field from the document.

Parameters:
    

**field_name** â the field name

Raises:
    

**ValueError** â if the field does not exist

copy()#
    

Returns a deep copy of the document.

Returns:
    

a `SerializableDocument`

fancy_repr(_class_name =None_, _select_fields =None_, _exclude_fields =None_, _** kwargs_)#
    

Generates a customizable string representation of the document.

Parameters:
    

  * **class_name** (_None_) â optional class name to use

  * **select_fields** (_None_) â iterable of field names to restrict to

  * **exclude_fields** (_None_) â iterable of field names to exclude

  * ****kwargs** â additional key-value pairs to include in the string representation



Returns:
    

a string representation of the document

property field_names#
    

An ordered tuple of the public fields of this document.

field_to_mongo(_field_name_)#
    

field_to_python(_field_name_ , _value_)#
    

classmethod from_dict(_d_ , _extended =False_)#
    

Loads the document from a BSON/JSON dictionary.

Parameters:
    

  * **d** â a dictionary

  * **extended** (_False_) â whether the input dictionary may contain serialized extended JSON constructs



Returns:
    

a `SerializableDocument`

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

Returns:
    

a `SerializableDocument`

get_field(_field_name_)#
    

Gets the field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

get_text_score()#
    

Get text score from text query

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_fields()#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Returns:
    

an iterator that emits `(name, value)` tuples

merge(_doc_ , _merge_lists =True_, _merge_dicts =True_, _overwrite =True_)#
    

Merges the contents of the given document into this document.

Parameters:
    

  * **doc** â a `SerializableDocument` of same type as this document

  * **merge_lists** (_True_) â whether to merge the elements of top-level list fields rather than treating the list as a single value

  * **merge_dicts** (_True_) â whether to recursively merge the contents of top-level dict fields rather than treating the dict as a single value

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields




my_metaclass#
    

alias of `DocumentMetaclass`

set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

to_dict(_extended =False_)#
    

Serializes this document to a BSON/JSON dictionary.

Parameters:
    

**extended** (_False_) â whether to serialize extended JSON constructs such as ObjectIDs, Binary, etc. into JSON format

Returns:
    

a dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo(_* args_, _** kwargs_)#
    

Return as SON data ready for use with MongoDB.

validate(_clean =True_)#
    

Ensure that all fieldsâ values are valid and that required fields are present.

Raises `ValidationError` if any of the fieldsâ values are found to be invalid.

fiftyone.core.groups.get_group_slice_name(_sample_ , _group_field_)#
    

Gets the group slice name for a sample, if available.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **group_field** â the datasetâs group field name



Returns:
    

the slice name, or `None`

fiftyone.core.groups.is_group_field(_field_)#
    

Determines whether the given field is a group field.

Parameters:
    

**field** â a [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field")

Returns:
    

True/False

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
