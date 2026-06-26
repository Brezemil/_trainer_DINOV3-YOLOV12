---
source_url: https://docs.voxel51.com/api/fiftyone.core.labels.html?_gl=1*z39nk3*_gcl_au*MTI3OTEyMjEwMy4xNzI2MTQ5NDk3
---

# fiftyone.core.labels#

Labels stored in dataset samples.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Label`(*args,Â **kwargs) | Base class for labels.  
---|---  
`Attribute`(*args,Â **kwargs) | Base class for attributes.  
`BooleanAttribute`(*args,Â **kwargs) | A boolean attribute.  
`CategoricalAttribute`(*args,Â **kwargs) | A categorical attribute.  
`NumericAttribute`(*args,Â **kwargs) | A numeric attribute.  
`ListAttribute`(*args,Â **kwargs) | A list attribute.  
`Instance`(*args,Â **kwargs) | A label instance.  
`Regression`(*args,Â **kwargs) | A regression value.  
`Classification`(*args,Â **kwargs) | A classification label.  
`Classifications`(*args,Â **kwargs) | A list of classifications for an image.  
`Detection`(*args,Â **kwargs) | An object detection.  
`Detections`(*args,Â **kwargs) | A list of object detections in an image.  
`Polyline`(*args,Â **kwargs) | A set of semantically related polylines or polygons.  
`Polylines`(*args,Â **kwargs) | A list of polylines or polygons in an image.  
`Keypoint`(*args,Â **kwargs) | A list of keypoints in an image.  
`Keypoints`(*args,Â **kwargs) | A list of `Keypoint` instances in an image.  
`Segmentation`(*args,Â **kwargs) | A semantic segmentation for an image.  
`Heatmap`(*args,Â **kwargs) | A heatmap for an image.  
`TemporalDetection`(*args,Â **kwargs) | A temporal detection in a video whose support is defined by a start and end frame.  
`TemporalDetections`(*args,Â **kwargs) | A list of temporal detections for a video.  
`GeoLocation`(*args,Â **kwargs) | Location data in GeoJSON format.  
`GeoLocations`(*args,Â **kwargs) | A batch of location data in GeoJSON format.  
  
class fiftyone.core.labels.Label(_* args_, _** kwargs_)#
    

Bases: [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument")

Base class for labels.

Label instances represent a logical collection of data associated with a particular task for a sample or frame in a dataset.

**Methods:**

`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
---|---  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
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
  
**Attributes:**

`STRICT` |   
---|---  
`field_names` | An ordered tuple of the public fields of this document.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

class fiftyone.core.labels.Attribute(_* args_, _** kwargs_)#
    

Bases: [`DynamicEmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument "fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument")

Base class for attributes.

Attribute instances represent an atomic piece of information, its `value`, usually embedded with a `name` within a dict field of another `Label` instance.

Parameters:
    

**value** (_None_) â the attribute value

**Attributes:**

`value` | A generic field.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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
  
value#
    

A generic field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.BooleanAttribute(_* args_, _** kwargs_)#
    

Bases: `Attribute`

A boolean attribute.

Parameters:
    

**value** (_None_) â the attribute value

**Attributes:**

`value` | A boolean field.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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
  
value#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.CategoricalAttribute(_* args_, _** kwargs_)#
    

Bases: `Attribute`

A categorical attribute.

Parameters:
    

  * **value** (_None_) â the attribute value

  * **confidence** (_None_) â a confidence in `[0, 1]` for the value

  * **logits** (_None_) â logits associated with the attribute




**Attributes:**

`value` | A unicode string field.  
---|---  
`confidence` | A floating point number field.  
`logits` | A one-dimensional array field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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
  
value#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




logits#
    

A one-dimensional array field.

`VectorField` instances accept numeric lists, tuples, and 1D numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.NumericAttribute(_* args_, _** kwargs_)#
    

Bases: `Attribute`

A numeric attribute.

Parameters:
    

**value** (_None_) â the attribute value

**Attributes:**

`value` | A floating point number field.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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
  
value#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.ListAttribute(_* args_, _** kwargs_)#
    

Bases: `Attribute`

A list attribute.

The list can store arbitrary JSON-serialiable values.

Parameters:
    

**value** (_None_) â the attribute value

**Attributes:**

`value` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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
  
value#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Instance(_* args_, _** kwargs_)#
    

Bases: [`EmbeddedDocument`](api__fiftyone.core.odm.embedded_document.md#fiftyone.core.odm.embedded_document.EmbeddedDocument "fiftyone.core.odm.embedded_document.EmbeddedDocument")

A label instance.

Parameters:
    

**id** (_None_) â the label instance ID

**Attributes:**

`id` | An Object ID field.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
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

class fiftyone.core.labels.Regression(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `Label`

A regression value.

Parameters:
    

  * **value** (_None_) â the regression value

  * **confidence** (_None_) â a confidence in `[0, 1]` for the regression




**Attributes:**

`value` | A floating point number field.  
---|---  
`confidence` | A floating point number field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
value#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Classification(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `Label`

A classification label.

Parameters:
    

  * **label** (_None_) â the label string

  * **confidence** (_None_) â a confidence in `[0, 1]` for the classification

  * **logits** (_None_) â logits associated with the labels




**Attributes:**

`label` | A unicode string field.  
---|---  
`confidence` | A floating point number field.  
`logits` | A one-dimensional array field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
label#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




logits#
    

A one-dimensional array field.

`VectorField` instances accept numeric lists, tuples, and 1D numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Classifications(_* args_, _** kwargs_)#
    

Bases: `_HasLabelList`, `Label`

A list of classifications for an image.

Parameters:
    

  * **classifications** (_None_) â a list of `Classification` instances

  * **logits** (_None_) â logits associated with the labels




**Attributes:**

`classifications` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`logits` | A one-dimensional array field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
classifications#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




logits#
    

A one-dimensional array field.

`VectorField` instances accept numeric lists, tuples, and 1D numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




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

class fiftyone.core.labels.Detection(_* args_, _** kwargs_)#
    

Bases: `_HasAttributesDict`, `_HasID`, `_HasMedia`, `_HasInstance`, `Label`

An object detection.

This class can represent 2D or 3D objects:

  * For [2D objects](https://docs.voxel51.com/user_guide/using_datasets.html#object-detection), you must provide the `bounding_box` parameter, and you can also provide the optional `mask` or `mask_path` parameters to represent [instance segmentations](https://docs.voxel51.com/user_guide/using_datasets.html#instance-segmentation)

  * For [3D objects](https://docs.voxel51.com/user_guide/using_datasets.html#d-detections), you must instead provide the `location`, `dimensions`, and `rotation` parameters




Parameters:
    

  * **label** (_None_) â the label string

  * **bounding_box** (_None_) â 

a list of relative bounding box coordinates in `[0, 1]` in the following format (2D only):
        
        [<top-left-x>, <top-left-y>, <width>, <height>]
        

  * **mask** (_None_) â an instance segmentation mask for the detection within its bounding box, which should be a 2D binary or 0/1 integer numpy array (2D only)

  * **mask_path** (_None_) â the absolute path to the instance segmentation image on disk, which should be a single-channel PNG image where any non-zero values represent the instanceâs extent (2D only)

  * **location** (_None_) â the object center `[x, y, z]` in scene coordinates (3D only)

  * **dimensions** (_None_) â the object size `[x, y, z]` in scene units (3D only)

  * **rotation** (_None_) â the object rotation `[x, y, z]` around its center, in `[-pi, pi]` (3D only)

  * **confidence** (_None_) â a confidence in `[0, 1]` for the detection

  * **index** (_None_) â an index for the object

  * **instance** (_None_) â an instance of `Instance` to link this detection label to other similar labels

  * **attributes** (_{}_) â a dict mapping attribute names to `Attribute` instances




**Attributes:**

`label` | A unicode string field.  
---|---  
`bounding_box` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`mask` | An n-dimensional array field.  
`mask_path` | A unicode string field.  
`confidence` | A floating point number field.  
`index` | A 32 bit integer field.  
`has_mask` | Whether this instance has a mask.  
`STRICT` |   
`attributes` | A dictionary field that wraps a standard Python dictionary.  
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`instance_id` | The label's instance ID, or None if it does not have one.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`get_mask`() | Returns the detection mask for this instance.  
---|---  
`import_mask`([update]) | Imports this instance's mask from disk to its `mask` attribute.  
`export_mask`(outpath[,Â update,Â overwrite_path]) | Exports this instance's mask to the given path.  
`to_polyline`([tolerance,Â filled]) | Returns a `Polyline` representation of this instance.  
`to_segmentation`([mask,Â frame_size,Â target]) | Returns a `Segmentation` representation of this instance.  
`to_shapely`([frame_size]) | Returns a Shapely representation of this instance.  
`from_mask`(mask[,Â label]) | Creates a `Detection` instance with its `mask` attribute populated from the given full image mask.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
label#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




bounding_box#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




mask#
    

An n-dimensional array field.

`ArrayField` instances accept numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




mask_path#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




index#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property has_mask#
    

Whether this instance has a mask.

get_mask()#
    

Returns the detection mask for this instance.

Returns:
    

a numpy array, or `None`

import_mask(_update =False_)#
    

Imports this instanceâs mask from disk to its `mask` attribute.

Parameters:
    

**update** (_False_) â whether to clear this instanceâs `mask_path` attribute after importing

export_mask(_outpath_ , _update =False_, _overwrite_path =False_)#
    

Exports this instanceâs mask to the given path.

Parameters:
    

  * **outpath** â the path to write the mask

  * **update** (_False_) â whether to clear this instanceâs `mask` attribute and set its `mask_path` attribute when exporting in-database segmentations

  * **overwrite_path** (_False_) â whether to write the in-database `mask` to disk even when `mask_path` is already set




to_polyline(_tolerance =2_, _filled =True_)#
    

Returns a `Polyline` representation of this instance.

If the detection has a mask, the returned polyline will trace the boundary of the mask; otherwise, the polyline will trace the bounding box itself.

Parameters:
    

  * **tolerance** (_2_) â a tolerance, in pixels, when generating an approximate polyline for the instance mask. Typical values are 1-3 pixels

  * **filled** (_True_) â whether the polyline should be filled



Returns:
    

a `Polyline`

to_segmentation(_mask =None_, _frame_size =None_, _target =255_)#
    

Returns a `Segmentation` representation of this instance.

The detection must have an instance mask, i.e., its `mask` attribute must be populated.

You must provide either `mask` or `frame_size` to use this method.

Parameters:
    

  * **mask** (_None_) â an optional numpy array to use as an initial mask to which to add this object

  * **frame_size** (_None_) â the `(width, height)` of the segmentation mask to render. This parameter has no effect if a `mask` is provided

  * **target** (_255_) â the pixel value or RGB hex string to use to render the object



Returns:
    

a `Segmentation`

to_shapely(_frame_size =None_)#
    

Returns a Shapely representation of this instance.

Parameters:
    

**frame_size** (_None_) â the `(width, height)` of the image. If provided, the returned geometry will use absolute coordinates

Returns:
    

a `shapely.geometry.polygon.Polygon`

classmethod from_mask(_mask_ , _label =None_, _** attributes_)#
    

Creates a `Detection` instance with its `mask` attribute populated from the given full image mask.

The instance mask for the object is extracted by computing the bounding rectangle of the non-zero values in the image mask.

Parameters:
    

  * **mask** â a boolean or 0/1 numpy array

  * **label** (_None_) â the label string

  * ****attributes** â additional attributes for the `Detection`



Returns:
    

a `Detection`

STRICT = False#
    

attributes#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property instance_id#
    

The labelâs instance ID, or None if it does not have one.

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Attribute may either exist in the `attributes` dict or as dynamic attributes.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

If the specified attribute already exists in the `attributes` dict, its value is updated there. Otherwise, the attribute is set (or created) as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Detections(_* args_, _** kwargs_)#
    

Bases: `_HasLabelList`, `Label`

A list of object detections in an image.

Parameters:
    

**detections** (_None_) â a list of `Detection` instances

**Attributes:**

`detections` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`to_polylines`([tolerance,Â filled]) | Returns a `Polylines` representation of this instance.  
---|---  
`to_segmentation`([mask,Â frame_size,Â mask_targets]) | Returns a `Segmentation` representation of this instance.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
detections#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_polylines(_tolerance =2_, _filled =True_)#
    

Returns a `Polylines` representation of this instance.

For detections with masks, the returned polylines will trace the boundaries of the masks; otherwise, the polylines will trace the bounding boxes themselves.

Parameters:
    

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for the instance masks. Typical values are 1-3 pixels

  * **filled** (_True_) â whether the polylines should be filled



Returns:
    

a `Polylines`

to_segmentation(_mask =None_, _frame_size =None_, _mask_targets =None_)#
    

Returns a `Segmentation` representation of this instance.

Only detections with instance masks (i.e., their `mask` attributes populated) will be rendered.

You must provide either `mask` or `frame_size` to use this method.

Parameters:
    

  * **mask** (_None_) â an optional array to use as an initial mask to which to add objects

  * **frame_size** (_None_) â the `(width, height)` of the segmentation mask to render. This parameter has no effect if a `mask` is provided

  * **mask_targets** (_None_) â a dict mapping integer pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which object classes to render and which pixel values to use for each class. If omitted, all objects are rendered with pixel value 255



Returns:
    

a `Segmentation`

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




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

class fiftyone.core.labels.Polyline(_* args_, _** kwargs_)#
    

Bases: `_HasAttributesDict`, `_HasID`, `_HasInstance`, `Label`

A set of semantically related polylines or polygons.

Parameters:
    

  * **label** (_None_) â a label for the polyline

  * **points** (_None_) â a list of lists of `(x, y)` points in `[0, 1] x [0, 1]` describing the vertices of each shape in the polyline

  * **confidence** (_None_) â a confidence in `[0, 1]` for the polyline

  * **index** (_None_) â an index for the polyline

  * **instance** (_None_) â an instance of `Instance` to link this polyline label to other similar labels

  * **closed** (_False_) â whether the shapes are closed, i.e., and edge should be drawn from the last vertex to the first vertex of each shape

  * **filled** (_False_) â whether the polyline represents polygons, i.e., shapes that should be filled when rendering them

  * **attributes** (_{}_) â a dict mapping attribute names to `Attribute` instances for the polyline




**Attributes:**

`label` | A unicode string field.  
---|---  
`points` | A list of lists of `(x, y)` coordinate pairs.  
`confidence` | A floating point number field.  
`index` | A 32 bit integer field.  
`closed` | A boolean field.  
`filled` | A boolean field.  
`STRICT` |   
`attributes` | A dictionary field that wraps a standard Python dictionary.  
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`instance_id` | The label's instance ID, or None if it does not have one.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`to_detection`([mask_size,Â frame_size]) | Returns a `Detection` representation of this instance whose bounding box tightly encloses the polyline.  
---|---  
`to_segmentation`([mask,Â frame_size,Â target,Â ...]) | Returns a `Segmentation` representation of this instance.  
`to_shapely`([frame_size,Â filled]) | Returns a Shapely representation of this instance.  
`from_mask`(mask[,Â label,Â tolerance]) | Creates a `Polyline` instance with polygons describing the non-zero region(s) of the given full image mask.  
`from_cuboid`(vertices[,Â frame_size,Â label]) | Constructs a cuboid from its 8 vertices in the format below.  
`from_rotated_box`(xc,Â yc,Â w,Â h,Â theta[,Â ...]) | Constructs a rotated bounding box from its center, dimensions, and rotation.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
label#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




points#
    

A list of lists of `(x, y)` coordinate pairs.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




index#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




closed#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




filled#
    

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_detection(_mask_size =None_, _frame_size =None_)#
    

Returns a `Detection` representation of this instance whose bounding box tightly encloses the polyline.

If a `mask_size` is provided, an instance mask of the specified size encoding the polylineâs shape is included.

Alternatively, if a `frame_size` is provided, the required mask size is then computed based off of the polyline points and `frame_size`.

Parameters:
    

  * **mask_size** (_None_) â an optional `(width, height)` at which to render an instance mask for the polyline

  * **frame_size** (_None_) â used when no `mask_size` is provided. an optional `(width, height)` of the frame containing this polyline that is used to compute the required `mask_size`



Returns:
    

a `Detection`

to_segmentation(_mask =None_, _frame_size =None_, _target =255_, _thickness =1_)#
    

Returns a `Segmentation` representation of this instance.

You must provide either `mask` or `frame_size` to use this method.

Parameters:
    

  * **mask** (_None_) â an optional numpy array to use as an initial mask to which to add objects

  * **frame_size** (_None_) â the `(width, height)` of the segmentation mask to render. This parameter has no effect if a `mask` is provided

  * **target** (_255_) â the pixel value or RGB hex string to use to render the object

  * **thickness** (_1_) â the thickness, in pixels, at which to render (non-filled) polylines



Returns:
    

a `Segmentation`

to_shapely(_frame_size =None_, _filled =None_)#
    

Returns a Shapely representation of this instance.

The type of geometry returned depends on the number of shapes (`points`) and whether they are polygons or lines (`filled`).

Parameters:
    

  * **frame_size** (_None_) â the `(width, height)` of the image. If provided, the returned geometry will use absolute coordinates

  * **filled** (_None_) â whether to treat the shape as filled (True) or hollow (False) regardless of its `filled` attribute



Returns:
    

  * `shapely.geometry.polygon.Polygon`: if `filled` is True and `points` contains a single shape

  * `shapely.geometry.multipolygon.MultiPolygon`: if `filled` is True and `points` contains multiple shapes

  * `shapely.geometry.linestring.LineString`: if `filled` is False and `points` contains a single shape

  * `shapely.geometry.multilinestring.MultiLineString`: if `filled` is False and `points` contains multiple shapes




Return type:
    

one of the following

classmethod from_mask(_mask_ , _label =None_, _tolerance =2_, _** attributes_)#
    

Creates a `Polyline` instance with polygons describing the non-zero region(s) of the given full image mask.

Parameters:
    

  * **mask** â a boolean or 0/1 numpy array

  * **label** (_None_) â the label string

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polygons for each region. Typical values are 1-3 pixels

  * ****attributes** â additional attributes for the `Polyline`



Returns:
    

a `Polyline`

classmethod from_cuboid(_vertices_ , _frame_size =None_, _label =None_, _** attributes_)#
    

Constructs a cuboid from its 8 vertices in the format below:
    
    
       7--------6
      /|       /|
     / |      / |
    3--------2  |
    |  4-----|--5
    | /      | /
    |/       |/
    0--------1
    

If a `frame_size` is provided, `vertices` must be absolute pixel coordinates; otherwise `vertices` should be normalized coordinates in `[0, 1] x [0, 1]`.

Parameters:
    

  * **vertices** â a list of 8 `(x, y)` vertices in the above format

  * **frame_size** (_None_) â the `(width, height)` of the frame

  * **label** (_None_) â the label string

  * ****attributes** â additional arguments for the `Polyline`



Returns:
    

a `Polyline`

classmethod from_rotated_box(_xc_ , _yc_ , _w_ , _h_ , _theta_ , _frame_size =None_, _label =None_, _** attributes_)#
    

Constructs a rotated bounding box from its center, dimensions, and rotation.

If a `frame_size` is provided, the provided box coordinates must be absolute pixel coordinates; otherwise they should be normalized coordinates in `[0, 1]`. Note that rotations in normalized coordinates only make sense when the source aspect ratio is square.

Parameters:
    

  * **xc** â the x-center coordinate

  * **yc** â the y-center coorindate

  * **w** â the box width

  * **y** â the box height

  * **theta** â the counter-clockwise rotation of the box in radians

  * **frame_size** (_None_) â the `(width, height)` of the frame

  * **label** (_None_) â the label string

  * ****attributes** â additional arguments for the `Polyline`



Returns:
    

a `Polyline`

STRICT = False#
    

attributes#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property instance_id#
    

The labelâs instance ID, or None if it does not have one.

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Attribute may either exist in the `attributes` dict or as dynamic attributes.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

If the specified attribute already exists in the `attributes` dict, its value is updated there. Otherwise, the attribute is set (or created) as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Polylines(_* args_, _** kwargs_)#
    

Bases: `_HasLabelList`, `Label`

A list of polylines or polygons in an image.

Parameters:
    

**polylines** (_None_) â a list of `Polyline` instances

**Attributes:**

`polylines` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`to_detections`([mask_size,Â frame_size]) | Returns a `Detections` representation of this instance whose bounding boxes tightly enclose the polylines.  
---|---  
`to_segmentation`([mask,Â frame_size,Â ...]) | Returns a `Segmentation` representation of this instance.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
polylines#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_detections(_mask_size =None_, _frame_size =None_)#
    

Returns a `Detections` representation of this instance whose bounding boxes tightly enclose the polylines.

If a `mask_size` is provided, instance masks of the specified size encoding the polylineâs shape are included in each `Detection`.

Alternatively, if a `frame_size` is provided, the required mask size is then computed based off of the polyline points and `frame_size`.

Parameters:
    

  * **mask_size** (_None_) â an optional `(width, height)` at which to render instance masks for the polylines

  * **frame_size** (_None_) â used when no `mask_size` is provided. an optional `(width, height)` of the frame containing these polylines that is used to compute the required `mask_size`



Returns:
    

a `Detections`

to_segmentation(_mask =None_, _frame_size =None_, _mask_targets =None_, _thickness =1_)#
    

Returns a `Segmentation` representation of this instance.

You must provide either `mask` or `frame_size` to use this method.

Parameters:
    

  * **mask** (_None_) â an optional numpy array to use as an initial mask to which to add objects

  * **frame_size** (_None_) â the `(width, height)` of the segmentation mask to render. This parameter has no effect if a `mask` is provided

  * **mask_targets** (_None_) â a dict mapping integer pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which object classes to render and which pixel values to use for each class. If omitted, all objects are rendered with pixel value 255

  * **thickness** (_1_) â the thickness, in pixels, at which to render (non-filled) polylines



Returns:
    

a `Segmentation`

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




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

class fiftyone.core.labels.Keypoint(_* args_, _** kwargs_)#
    

Bases: `_HasAttributesDict`, `_HasID`, `_HasInstance`, `Label`

A list of keypoints in an image.

Parameters:
    

  * **label** (_None_) â a label for the points

  * **points** (_None_) â a list of `(x, y)` keypoints in `[0, 1] x [0, 1]`

  * **confidence** (_None_) â a list of confidences in `[0, 1]` for each point

  * **index** (_None_) â an index for the keypoints

  * **instance** (_None_) â an instance of `Instance` to link this keypoint label to other similar labels

  * **attributes** (_{}_) â a dict mapping attribute names to `Attribute` instances




**Attributes:**

`label` | A unicode string field.  
---|---  
`points` | A list of `(x, y)` coordinate pairs.  
`confidence` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`index` | A 32 bit integer field.  
`STRICT` |   
`attributes` | A dictionary field that wraps a standard Python dictionary.  
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`instance_id` | The label's instance ID, or None if it does not have one.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`to_shapely`([frame_size]) | Returns a Shapely representation of this instance.  
---|---  
`apply_confidence_threshold`(confidence_thresh) | Replaces all `points` on this instance whose confidence are below the provided threshold with `np.nan`.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
label#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




points#
    

A list of `(x, y)` coordinate pairs.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




index#
    

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_shapely(_frame_size =None_)#
    

Returns a Shapely representation of this instance.

Parameters:
    

**frame_size** (_None_) â the `(width, height)` of the image. If provided, the returned geometry will use absolute coordinates

Returns:
    

a `shapely.geometry.multipoint.MultiPoint`

apply_confidence_threshold(_confidence_thresh_)#
    

Replaces all `points` on this instance whose confidence are below the provided threshold with `np.nan`.

Use `filter_keypoints <fiftyone.core.collections.SampleCollection.filter_keypoints()` to perform this operation as temporary view rather than a permanent data transformation.

Parameters:
    

**confidence_thresh** â a confidence threshold

STRICT = False#
    

attributes#
    

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

The specified attribute may either exist in the `attributes` dict or as a dynamic attribute.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property instance_id#
    

The labelâs instance ID, or None if it does not have one.

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Attribute may either exist in the `attributes` dict or as dynamic attributes.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

If the specified attribute already exists in the `attributes` dict, its value is updated there. Otherwise, the attribute is set (or created) as a dynamic attribute.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Keypoints(_* args_, _** kwargs_)#
    

Bases: `_HasLabelList`, `Label`

A list of `Keypoint` instances in an image.

Parameters:
    

**keypoints** (_None_) â a list of `Keypoint` instances

**Attributes:**

`keypoints` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
keypoints#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




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

class fiftyone.core.labels.Segmentation(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `_HasMedia`, `Label`

A semantic segmentation for an image.

Provide either the `mask` or `mask_path` argument to define the segmentation.

Parameters:
    

  * **mask** (_None_) â a numpy array with integer values encoding the semantic labels

  * **mask_path** (_None_) â the absolute path to the segmentation image on disk




**Attributes:**

`mask` | An n-dimensional array field.  
---|---  
`mask_path` | A unicode string field.  
`has_mask` | Whether this instance has a mask.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`get_mask`() | Returns the segmentation mask for this instance.  
---|---  
`import_mask`([update]) | Imports this instance's mask from disk to its `mask` attribute.  
`export_mask`(outpath[,Â update,Â overwrite_path]) | Exports this instance's mask to the given path.  
`transform_mask`(targets_map[,Â outpath,Â update]) | Transforms this instance's mask according to the provided targets map.  
`to_detections`([mask_targets,Â mask_types]) | Returns a `Detections` representation of this instance with instance masks populated.  
`to_polylines`([mask_targets,Â mask_types,Â ...]) | Returns a `Polylines` representation of this instance.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
mask#
    

An n-dimensional array field.

`ArrayField` instances accept numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




mask_path#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property has_mask#
    

Whether this instance has a mask.

get_mask()#
    

Returns the segmentation mask for this instance.

Returns:
    

a numpy array, or `None`

import_mask(_update =False_)#
    

Imports this instanceâs mask from disk to its `mask` attribute.

Parameters:
    

**update** (_False_) â whether to clear this instanceâs `mask_path` attribute after importing

export_mask(_outpath_ , _update =False_, _overwrite_path =False_)#
    

Exports this instanceâs mask to the given path.

Parameters:
    

  * **outpath** â the path to write the mask

  * **update** (_False_) â whether to clear this instanceâs `mask` attribute and set its `mask_path` attribute when exporting in-database segmentations

  * **overwrite_path** (_False_) â whether to write the in-database `mask` to disk even when `mask_path` is already set




transform_mask(_targets_map_ , _outpath =None_, _update =False_)#
    

Transforms this instanceâs mask according to the provided targets map.

This method can be used to transform between grayscale and RGB masks, or it can be used to edit the pixel values or colors of a mask without changing the number of channels.

Note that any pixel values not in `targets_map` will be zero in the transformed mask.

Parameters:
    

  * **targets_map** â a dict mapping existing pixel values (2D masks) or RGB hex strings (3D masks) to new pixel values or RGB hex strings. You may convert between grayscale and RGB using this argument

  * **outpath** (_None_) â an optional path to write the transformed mask on disk

  * **update** (_False_) â whether to save the transformed mask on this instance



Returns:
    

the transformed mask

to_detections(_mask_targets =None_, _mask_types ='stuff'_)#
    

Returns a `Detections` representation of this instance with instance masks populated.

Each `"stuff"` class will be converted to a single `Detection` whose instance mask spans all region(s) of the class.

Each `"thing"` class will result in one `Detection` instance per connected region of that class in the segmentation.

Parameters:
    

  * **mask_targets** (_None_) â a dict mapping integer pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which classes to generate detections for. If omitted, all labels are assigned to their pixel values

  * **mask_types** (_"stuff"_) â 

whether the classes are `"stuff"` (amorphous regions of pixels) or `"thing"` (connected regions, each representing an instance of the thing). Can be any of the following:

    * `"stuff"` if all classes are stuff classes

    * `"thing"` if all classes are thing classes

    * a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to `"stuff"` or `"thing"` for each class



Returns:
    

a `Detections`

to_polylines(_mask_targets =None_, _mask_types ='stuff'_, _tolerance =2_)#
    

Returns a `Polylines` representation of this instance.

Each `"stuff"` class will be converted to a single `Polyline` that may contain multiple disjoint shapes capturing the class.

Each `"thing"` class will result in one `Polyline` instance per connected region of that class.

Parameters:
    

  * **mask_targets** (_None_) â a dict mapping integer pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which classes to generate detections for. If omitted, all labels are assigned to their pixel values

  * **mask_types** (_"stuff"_) â 

whether the classes are `"stuff"` (amorphous regions of pixels) or `"thing"` (connected regions, each representing an instance of the thing). Can be any of the following:

    * `"stuff"` if all classes are stuff classes

    * `"thing"` if all classes are thing classes

    * a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to `"stuff"` or `"thing"` for each class

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for each region. Typical values are 1-3 pixels



Returns:
    

a `Polylines`

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.Heatmap(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `_HasMedia`, `Label`

A heatmap for an image.

Provide either the `map` or `map_path` argument to define the heatmap.

Parameters:
    

  * **map** (_None_) â a 2D numpy array

  * **map_path** (_None_) â the absolute path to the heatmap image on disk

  * **range** (_None_) â an optional `[min, max]` range of the mapâs values. If None is provided, `[0, 1]` will be assumed if `map` contains floating point values, `[0, 255]` will be assumed if `map` contains integer values, and the dtype of the image will be assumed if `map_path` is used




**Attributes:**

`map` | An n-dimensional array field.  
---|---  
`map_path` | A unicode string field.  
`range` | A `[min, max]` range of the values in a `fiftyone.core.labels.Heatmap`.  
`has_map` | Whether this instance has a map.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`get_map`() | Returns the map array for this instance.  
---|---  
`import_map`([update]) | Imports this instance's map from disk to its `map` attribute.  
`export_map`(outpath[,Â update]) | Exports this instance's map to the given path.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
map#
    

An n-dimensional array field.

`ArrayField` instances accept numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




map_path#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




range#
    

A `[min, max]` range of the values in a `fiftyone.core.labels.Heatmap`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




property has_map#
    

Whether this instance has a map.

get_map()#
    

Returns the map array for this instance.

Returns:
    

a numpy array, or `None`

import_map(_update =False_)#
    

Imports this instanceâs map from disk to its `map` attribute.

Parameters:
    

  * **outpath** â the path to write the map

  * **update** (_False_) â whether to clear this instanceâs `map_path` attribute after importing




export_map(_outpath_ , _update =False_)#
    

Exports this instanceâs map to the given path.

Parameters:
    

  * **outpath** â the path to write the map

  * **update** (_False_) â whether to clear this instanceâs `map` and `range` attributes and set its `map_path` attribute when exporting in-database heatmaps




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.TemporalDetection(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `Label`

A temporal detection in a video whose support is defined by a start and end frame.

Parameters:
    

  * **label** (_None_) â the label string

  * **support** (_None_) â the `[first, last]` frame numbers, inclusive

  * **confidence** (_None_) â a confidence in `[0, 1]` for the detection




**Attributes:**

`label` | A unicode string field.  
---|---  
`support` | A `[first, last]` frame support in a video.  
`confidence` | A floating point number field.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`from_timestamps`(timestamps[,Â sample,Â metadata]) | Creates a `TemporalDetection` instance from `[start, stop]` timestamps for the specified video.  
---|---  
`to_timestamps`([sample,Â metadata]) | Returns the `[start, stop]` timestamps, in seconds, for this temporal detection in the given video.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
label#
    

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




support#
    

A `[first, last]` frame support in a video.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




confidence#
    

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




classmethod from_timestamps(_timestamps_ , _sample =None_, _metadata =None_, _** kwargs_)#
    

Creates a `TemporalDetection` instance from `[start, stop]` timestamps for the specified video.

You must provide either `sample` or `metadata` to inform the conversion.

Parameters:
    

  * **timestamps** â the `[start, stop]` timestamps, in seconds or âHH:MM:SS.XXXâ format

  * **sample** (_None_) â a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") whose `metadata` field is populated

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance

  * ****kwargs** â additional arguments for `TemporalDetection`



Returns:
    

a `TemporalDetection`

to_timestamps(_sample =None_, _metadata =None_)#
    

Returns the `[start, stop]` timestamps, in seconds, for this temporal detection in the given video.

You must provide either `sample` or `metadata` to inform the conversion.

Parameters:
    

  * **sample** (_None_) â a video [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") whose `metadata` field is populated

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance



Returns:
    

the `[start, stop]` timestamps of this detection, in seconds

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.TemporalDetections(_* args_, _** kwargs_)#
    

Bases: `_HasLabelList`, `Label`

A list of temporal detections for a video.

Parameters:
    

**detections** (_None_) â a list of `TemporalDetection` instances

**Attributes:**

`detections` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
---|---  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
  
**Methods:**

`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
---|---  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
detections#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




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

class fiftyone.core.labels.GeoLocation(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `Label`

Location data in GeoJSON format.

Parameters:
    

  * **point** (_None_) â a `[longitude, latitude]` point

  * **line** (_None_) â 

a line defined by coordinates as shown below:
        
        [[lon1, lat1], [lon2, lat2], ...]
        

  * **polygon** (_None_) â 

a polygon defined by coorindates as shown below:
        
        [
            [[lon1, lat1], [lon2, lat2], ...],
            [[lon1, lat1], [lon2, lat2], ...],
            ...
        ]
        

where the first outer list describes the boundary of the polygon and any remaining entries describe holes




**Attributes:**

`point` | A GeoJSON field storing a longitude and latitude coordinate point.  
---|---  
`line` | A GeoJSON field storing a line of longitude and latitude coordinates.  
`polygon` | A GeoJSON field storing a polygon of longitude and latitude coordinates.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`to_geo_json`() | Returns a GeoJSON `geometry` dict for this instance.  
---|---  
`from_geo_json`(d) | Creates a `GeoLocation` from a GeoJSON dictionary.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
point#
    

A GeoJSON field storing a longitude and latitude coordinate point.

The data is stored as `[longitude, latitude]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




line#
    

A GeoJSON field storing a line of longitude and latitude coordinates.

The data is stored as follows:
    
    
    [[lon1, lat1], [lon2, lat2], ...]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




polygon#
    

A GeoJSON field storing a polygon of longitude and latitude coordinates.

The data is stored as follows:
    
    
    [
        [[lon1, lat1], [lon2, lat2], ...],
        [[lon1, lat1], [lon2, lat2], ...],
        ...
    ]
    

where the first element describes the boundary of the polygon and any remaining entries describe holes.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_geo_json()#
    

Returns a GeoJSON `geometry` dict for this instance.

Returns:
    

a GeoJSON dict

classmethod from_geo_json(_d_)#
    

Creates a `GeoLocation` from a GeoJSON dictionary.

Parameters:
    

**d** â a GeoJSON dict

Returns:
    

a `GeoLocation`

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

class fiftyone.core.labels.GeoLocations(_* args_, _** kwargs_)#
    

Bases: `_HasID`, `Label`

A batch of location data in GeoJSON format.

The attributes of this class accept lists of data in the format of the corresponding attributes of `GeoLocation`.

Parameters:
    

  * **points** (_None_) â a list of points

  * **lines** (_None_) â a list of lines

  * **polygons** (_None_) â a list of polygons




**Attributes:**

`points` | A GeoJSON field storing a list of points.  
---|---  
`lines` | A GeoJSON field storing a list of lines.  
`polygons` | A GeoJSON field storing a list of polygons.  
`STRICT` |   
`field_names` | An ordered tuple of the public fields of this document.  
`id` | An Object ID field.  
`tags` | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
  
**Methods:**

`to_geo_json`() | Returns a GeoJSON `geometry` dict for this instance.  
---|---  
`from_geo_json`(d) | Creates a `GeoLocation` from a GeoJSON dictionary.  
`clean`() | Hook for doing document level data cleaning (usually validation or assignment) before validation is run.  
`clear_field`(field_name) | Clears the field from the document.  
`copy`() | Returns a deep copy of the document.  
`delete_attribute`(name) | Deletes the attribute with the given name.  
`fancy_repr`([class_name,Â select_fields,Â ...]) | Generates a customizable string representation of the document.  
`field_to_mongo`(field_name) |   
`field_to_python`(field_name,Â value) |   
`from_dict`(d[,Â extended]) | Loads the document from a BSON/JSON dictionary.  
`from_json`(s) | Loads the document from a JSON string.  
`get_attribute_value`(name[,Â default]) | Gets the value of the attribute with the given name.  
`get_field`(field_name) | Gets the field of the document.  
`get_text_score`() | Get text score from text query  
`has_attribute`(name) | Determines whether the label has an attribute with the given name.  
`has_field`(field_name) | Determines whether the document has a field of the given name.  
`iter_attributes`() | Returns an iterator over the custom attributes of the label.  
`iter_fields`() | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(doc[,Â merge_lists,Â merge_dicts,Â overwrite]) | Merges the contents of the given document into this document.  
`set_attribute_value`(name,Â value) | Sets the value of the attribute with the given name.  
`set_field`(field_name,Â value[,Â create]) | Sets the value of a field of the document.  
`to_dict`([extended]) | Serializes this document to a BSON/JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo`(*args,Â **kwargs) | Return as SON data ready for use with MongoDB.  
`validate`([clean]) | Ensure that all fields' values are valid and that required fields are present.  
  
**Classes:**

`my_metaclass` |   
---|---  
  
points#
    

A GeoJSON field storing a list of points.

The data is stored as follows:
    
    
    [[lon1, lat1], [lon2, lat2], ...]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




lines#
    

A GeoJSON field storing a list of lines.

The data is stored as follows:
    
    
    [
        [[lon1, lat1], [lon2, lat2], ...],
        [[lon1, lat1], [lon2, lat2], ...],
        ...
    ]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




polygons#
    

A GeoJSON field storing a list of polygons.

The data is stored as follows:
    
    
    [
        [
            [[lon1, lat1], [lon2, lat2], ...],
            [[lon1, lat1], [lon2, lat2], ...],
            ...
        ],
        [
            [[lon1, lat1], [lon2, lat2], ...],
            [[lon1, lat1], [lon2, lat2], ...],
            ...
        ],
        ...
    ]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




to_geo_json()#
    

Returns a GeoJSON `geometry` dict for this instance.

Returns:
    

a GeoJSON dict

classmethod from_geo_json(_d_)#
    

Creates a `GeoLocation` from a GeoJSON dictionary.

Parameters:
    

**d** â a GeoJSON dict

Returns:
    

a `GeoLocation`

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

delete_attribute(_name_)#
    

Deletes the attribute with the given name.

Parameters:
    

**name** â the attribute name

Raises:
    

**AttributeError** â if the attribute does not exist

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

get_attribute_value(_name_ , _default =<fiftyone.core.labels._NoDefault object>_)#
    

Gets the value of the attribute with the given name.

Parameters:
    

  * **name** â the attribute name

  * **default** (_no_default_) â a default value to return if the attribute does not exist. Can be `None`



Returns:
    

the attribute value

Raises:
    

**AttributeError** â if the attribute does not exist and no default value was provided

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

has_attribute(_name_)#
    

Determines whether the label has an attribute with the given name.

Parameters:
    

**name** â the attribute name

Returns:
    

True/False

has_field(_field_name_)#
    

Determines whether the document has a field of the given name.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

id#
    

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




iter_attributes()#
    

Returns an iterator over the custom attributes of the label.

Returns:
    

a generator that emits `(name, value)` tuples

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

set_attribute_value(_name_ , _value_)#
    

Sets the value of the attribute with the given name.

The attribute will be declared if it does not exist.

Parameters:
    

  * **name** â the attribute name

  * **value** â the value




set_field(_field_name_ , _value_ , _create =True_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist



Raises:
    

**ValueError** â if `field_name` is not an allowed field name or does not exist and `create == False`

tags#
    

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
