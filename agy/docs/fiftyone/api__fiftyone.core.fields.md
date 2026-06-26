---
source_url: https://docs.voxel51.com/api/fiftyone.core.fields.html
---

# fiftyone.core.fields#

Dataset sample fields.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`validate_constraints`([ftype,Â ...]) | Validates the given field constraints.  
---|---  
`matches_constraints`(field[,Â ftype,Â ...]) | Determines whether the field matches the given constraints.  
`validate_field`(field[,Â path,Â ftype,Â ...]) | Validates that the field matches the given constraints.  
`get_field_metadata`(field) | Returns a dict of editable metadata for the given field.  
`filter_schema`(schema[,Â ftype,Â ...]) | Filters the schema according to the given constraints.  
`flatten_schema`(schema[,Â ftype,Â ...]) | Returns a flat version of the given schema where all embedded document fields are included as top-level keys.  
`is_integer_mask_targets`(mask_targets) | Determines whether the provided mask targets use integer keys.  
`is_integer_target`(target) | Determines whether the provided target is an integer.  
`is_rgb_mask_targets`(mask_targets) | Determines whether the provided mask targets use RGB hex string keys.  
`is_rgb_target`(target) | Determines whether the provided target is an RGB string.  
`hex_to_int`(hex_str) | Converts a hex string like "#ff6d04" to a hex integer.  
`int_to_hex`(value) | Converts an RRGGBB integer value to hex string like "#ff6d04".  
`rgb_array_to_int`(mask) | Converts an RGB mask array to a 2D hex integer mask array.  
`int_array_to_rgb`(mask) | Converts a 2D hex integer mask array to an RGB mask array.  
  
**Classes:**

`Field`([description,Â info,Â read_only,Â created_at]) | A generic field.  
---|---  
`IntField`([description,Â info,Â read_only,Â ...]) | A 32 bit integer field.  
`ObjectIdField`([description,Â info,Â ...]) | An Object ID field.  
`UUIDField`([description,Â info,Â read_only,Â ...]) | A UUID field.  
`BooleanField`([description,Â info,Â read_only,Â ...]) | A boolean field.  
`DateField`([description,Â info,Â read_only,Â ...]) | A date field.  
`DateTimeField`([description,Â info,Â ...]) | A datetime field.  
`FloatField`([description,Â info,Â read_only,Â ...]) | A floating point number field.  
`StringField`([description,Â info,Â read_only,Â ...]) | A unicode string field.  
`ColorField`([description,Â info,Â read_only,Â ...]) | A string field that holds a hex color string like '#FF6D04'.  
`ListField`([field,Â description,Â info,Â ...]) | A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.  
`HeatmapRangeField`(**kwargs) | A `[min, max]` range of the values in a [`fiftyone.core.labels.Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap").  
`DictField`([field,Â description,Â info,Â ...]) | A dictionary field that wraps a standard Python dictionary.  
`KeypointsField`([field,Â description,Â info,Â ...]) | A list of `(x, y)` coordinate pairs.  
`PolylinePointsField`([field,Â description,Â ...]) | A list of lists of `(x, y)` coordinate pairs.  
`GeoPointField`([description,Â info,Â ...]) | A GeoJSON field storing a longitude and latitude coordinate point.  
`GeoLineStringField`([description,Â info,Â ...]) | A GeoJSON field storing a line of longitude and latitude coordinates.  
`GeoPolygonField`([description,Â info,Â ...]) | A GeoJSON field storing a polygon of longitude and latitude coordinates.  
`GeoMultiPointField`([description,Â info,Â ...]) | A GeoJSON field storing a list of points.  
`GeoMultiLineStringField`([description,Â info,Â ...]) | A GeoJSON field storing a list of lines.  
`GeoMultiPolygonField`([description,Â info,Â ...]) | A GeoJSON field storing a list of polygons.  
`VectorField`([description,Â info,Â read_only,Â ...]) | A one-dimensional array field.  
`ArrayField`([description,Â info,Â read_only,Â ...]) | An n-dimensional array field.  
`FrameNumberField`([description,Â info,Â ...]) | A video frame number field.  
`FrameSupportField`(**kwargs) | A `[first, last]` frame support in a video.  
`ClassesField`(**kwargs) | A `ListField` that stores class label strings.  
`MaskTargetsField`(**kwargs) | A `DictField` that stores mapping between integer keys or RGB string hex keys and string targets.  
`EmbeddedDocumentField`(document_type[,Â ...]) | A field that stores instances of a given type of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") object.  
`EmbeddedDocumentListField`(document_type[,Â ...]) | A field that stores a list of a given type of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") objects.  
`ReferenceField`(document_type[,Â dbref,Â ...]) | A reference field.  
  
fiftyone.core.fields.validate_constraints(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_)#
    

Validates the given field constraints.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of types to enforce. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to enforce. Must be subclass(es) of `Field`

  * **read_only** (_None_) â whether to optionally enforce that the field is read-only (True) or not read-only (False)

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date



Returns:
    

True/False whether any constraints were provided

Raises:
    

**ValueError** â if the constraints are not valid

fiftyone.core.fields.matches_constraints(_field_ , _ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_)#
    

Determines whether the field matches the given constraints.

Parameters:
    

  * **field** â a `Field`

  * **ftype** (_None_) â an optional field type or iterable of types to enforce. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to enforce. Must be subclass(es) of `Field`

  * **read_only** (_None_) â whether to optionally enforce that the field is read-only (True) or not read-only (False)

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date



Returns:
    

True/False

fiftyone.core.fields.validate_field(_field_ , _path =None_, _ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_)#
    

Validates that the field matches the given constraints.

Parameters:
    

  * **field** â a `Field`

  * **path** (_None_) â the field or `embedded.field.name`. Only used to generate more informative error messages

  * **ftype** (_None_) â an optional field type or iterable of types to enforce. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to enforce. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to enforce. Must be subclass(es) of `Field`

  * **read_only** (_None_) â whether to optionally enforce that the field is read-only (True) or not read-only (False)



Raises:
    

**ValueError** â if the constraints are not valid

fiftyone.core.fields.get_field_metadata(_field_)#
    

Returns a dict of editable metadata for the given field.

Parameters:
    

**field** â a `Field`

Returns:
    

a dict of field metadata

fiftyone.core.fields.filter_schema(_schema_ , _ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Filters the schema according to the given constraints.

Parameters:
    

  * **schema** â a dict mapping field names to `Field` instances

  * **ftype** (_None_) â an optional field type or iterable of types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **flat** (_False_) â whether to return a flattened schema where all embedded document fields are included as top-level keys

  * **unwind** (_True_) â whether to traverse into list fields. Only applicable when `flat=True`

  * **mode** (_None_) â whether to apply the above constraints before and/or after flattening the schema. Only applicable when `flat=True`. Supported values are `("before", "after", "both")`. The default is `"after"`



Returns:
    

a dict mapping field names to `Field` instances

fiftyone.core.fields.flatten_schema(_schema_ , _ftype =None_, _embedded_doc_type =None_, _subfield =None_, _unwind =True_, _read_only =None_, _info_keys =None_, _created_after =None_, _include_private =False_)#
    

Returns a flat version of the given schema where all embedded document fields are included as top-level keys.

Parameters:
    

  * **schema** â a dict mapping field names to `Field` instances

  * **ftype** (_None_) â an optional field type or iterable of types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **unwind** (_True_) â whether to traverse into list fields

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **info_keys** (_None_) â an optional key or list of keys that must be in the fieldâs `info` dict

  * **created_after** (_None_) â an optional `datetime` specifying a minimum creation date

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema



Returns:
    

a dict mapping flattened paths to `Field` instances

class fiftyone.core.fields.Field(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `BaseField`

A generic field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
---|---  
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`read_only` | Whether the field is read-only.  
`created_at` | The datetime the field was created.  
`auto_creation_counter` |   
`creation_counter` |   
`name` |   
`owner_document` |   
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value[,Â clean]) | Perform validation on a value.  
  
property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

property created_at#
    

The datetime the field was created.

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

auto_creation_counter = -12#
    

creation_counter = 323#
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

name = None#
    

property owner_document#
    

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_ , _clean =True_)#
    

Perform validation on a value.

class fiftyone.core.fields.IntField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `IntField`, `Field`

A 32 bit integer field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

class fiftyone.core.fields.ObjectIdField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `ObjectIdField`, `Field`

An Object ID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`validate`(value) | Perform validation on a value.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

validate(_value_)#
    

Perform validation on a value.

class fiftyone.core.fields.UUIDField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `UUIDField`, `Field`

A UUID field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

class fiftyone.core.fields.BooleanField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `BooleanField`, `Field`

A boolean field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.DateField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `DateField`, `Field`

A date field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

class fiftyone.core.fields.DateTimeField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `DateTimeField`, `Field`

A datetime field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.FloatField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `FloatField`, `Field`

A floating point number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`validate`(value) | Perform validation on a value.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.StringField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `StringField`, `Field`

A unicode string field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

class fiftyone.core.fields.ColorField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `StringField`

A string field that holds a hex color string like â#FF6D04â.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.ListField(_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `ListField`, `Field`

A list field that wraps a standard `Field`, allowing multiple instances of the field to be stored as a list in the database.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the list elements

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Make sure that a list of valid fields is being used.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Make sure that a list of valid fields is being used.

class fiftyone.core.fields.HeatmapRangeField(_** kwargs_)#
    

Bases: `ListField`

A `[min, max]` range of the values in a [`fiftyone.core.labels.Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap").

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Make sure that a list of valid fields is being used.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.DictField(_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `DictField`, `Field`

A dictionary field that wraps a standard Python dictionary.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **field** (_None_) â an optional `Field` instance describing the type of the values in the dict

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Make sure that a list of valid fields is being used.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.KeypointsField(_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `ListField`

A list of `(x, y)` coordinate pairs.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Make sure that a list of valid fields is being used.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.PolylinePointsField(_field =None_, _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `ListField`

A list of lists of `(x, y)` coordinate pairs.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Make sure that a list of valid fields is being used.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoPointField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `PointField`

A GeoJSON field storing a longitude and latitude coordinate point.

The data is stored as `[longitude, latitude]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoLineStringField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `LineStringField`

A GeoJSON field storing a line of longitude and latitude coordinates.

The data is stored as follows:
    
    
    [[lon1, lat1], [lon2, lat2], ...]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoPolygonField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `PolygonField`

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




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoMultiPointField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `MultiPointField`

A GeoJSON field storing a list of points.

The data is stored as follows:
    
    
    [[lon1, lat1], [lon2, lat2], ...]
    

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoMultiLineStringField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `MultiLineStringField`

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




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.GeoMultiPolygonField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `_GeoField`, `MultiPolygonField`

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




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.VectorField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `BinaryField`, `Field`

A one-dimensional array field.

`VectorField` instances accept numeric lists, tuples, and 1D numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

class fiftyone.core.fields.ArrayField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `BinaryField`, `Field`

An n-dimensional array field.

`ArrayField` instances accept numpy array values. The underlying data is serialized and stored in the database as zlib-compressed bytes generated by `numpy.save` and always retrieved as a numpy array.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

class fiftyone.core.fields.FrameNumberField(_description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `IntField`

A video frame number field.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Perform validation on a value.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Perform validation on a value.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.FrameSupportField(_** kwargs_)#
    

Bases: `ListField`

A `[first, last]` frame support in a video.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`validate`(value) | Make sure that a list of valid fields is being used.  
---|---  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.ClassesField(_** kwargs_)#
    

Bases: `ListField`

A `ListField` that stores class label strings.

If this field is not set, its default value is `[]`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Make sure that a list of valid fields is being used.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Make sure that a list of valid fields is being used.

class fiftyone.core.fields.MaskTargetsField(_** kwargs_)#
    

Bases: `DictField`

A `DictField` that stores mapping between integer keys or RGB string hex keys and string targets.

If this field is not set, its default value is `{}`.

Parameters:
    

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`to_mongo`(value) | Convert a Python type to a MongoDB-compatible type.  
---|---  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Make sure that a list of valid fields is being used.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
to_mongo(_value_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Make sure that a list of valid fields is being used.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

fiftyone.core.fields.is_integer_mask_targets(_mask_targets_)#
    

Determines whether the provided mask targets use integer keys.

Parameters:
    

**mask_targets** â a mask targets dict

Returns:
    

True/False

fiftyone.core.fields.is_integer_target(_target_)#
    

Determines whether the provided target is an integer.

Parameters:
    

**target** â an integer or RGB hex string

Returns:
    

True/False

fiftyone.core.fields.is_rgb_mask_targets(_mask_targets_)#
    

Determines whether the provided mask targets use RGB hex string keys.

Parameters:
    

**mask_targets** â a mask targets dict

Returns:
    

True/False

fiftyone.core.fields.is_rgb_target(_target_)#
    

Determines whether the provided target is an RGB string.

Parameters:
    

**target** â an integer or RGB hex string

Returns:
    

True/False

fiftyone.core.fields.hex_to_int(_hex_str_)#
    

Converts a hex string like â#ff6d04â to a hex integer.

Parameters:
    

**hex_str** â a hex string

Returns:
    

an integer

fiftyone.core.fields.int_to_hex(_value_)#
    

Converts an RRGGBB integer value to hex string like â#ff6d04â.

Parameters:
    

**value** â an integer value

Returns:
    

a hex string

fiftyone.core.fields.rgb_array_to_int(_mask_)#
    

Converts an RGB mask array to a 2D hex integer mask array.

Parameters:
    

**mask** â an RGB mask array

Returns:
    

a 2D integer mask array

fiftyone.core.fields.int_array_to_rgb(_mask_)#
    

Converts a 2D hex integer mask array to an RGB mask array.

Parameters:
    

**mask** â a 2D integer mask array

Returns:
    

an RGB mask array

class fiftyone.core.fields.EmbeddedDocumentField(_document_type_ , _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `EmbeddedDocumentField`, `Field`

A field that stores instances of a given type of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") object.

Parameters:
    

  * **document_type** â the [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Methods:**

`has_field`(path) | Determines whether this field has the given embedded field.  
---|---  
`get_field`(path) | Returns the field for the provided path, or `None`.  
`get_field_schema`([ftype,Â embedded_doc_type,Â ...]) | Returns a schema dictionary describing the fields of the embedded document field.  
`validate`(value,Â **kwargs) | Make sure that the document instance is an instance of the EmbeddedDocument subclass provided when the document was defined.  
`copy`() | Returns a copy of the field.  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
  
**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`document_type` |   
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
has_field(_path_)#
    

Determines whether this field has the given embedded field.

Parameters:
    

**path** â the field name or `embedded.field.name`

Returns:
    

True/False

get_field(_path_)#
    

Returns the field for the provided path, or `None`.

Parameters:
    

**path** â a field name or `embedded.field.name`

Returns:
    

a `Field` instance or `None`

get_field_schema(_ftype =None_, _embedded_doc_type =None_, _subfield =None_, _read_only =None_, _include_private =False_, _flat =False_, _unwind =True_, _mode =None_)#
    

Returns a schema dictionary describing the fields of the embedded document field.

Parameters:
    

  * **ftype** (_None_) â an optional field type or iterable of types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **embedded_doc_type** (_None_) â an optional embedded document type or iterable of types to which to restrict the returned schema. Must be subclass(es) of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument")

  * **subfield** (_None_) â an optional subfield type or iterable of subfield types to which to restrict the returned schema. Must be subclass(es) of `Field`

  * **read_only** (_None_) â whether to restrict to (True) or exclude (False) read-only fields. By default, all fields are included

  * **include_private** (_False_) â whether to include fields that start with `_` in the returned schema

  * **flat** (_False_) â whether to return a flattened schema where all embedded document fields are included as top-level keys

  * **unwind** (_True_) â whether to traverse into list fields. Only applicable when `flat=True`

  * **mode** (_None_) â whether to apply the above constraints before and/or after flattening the schema. Only applicable when `flat=True`. Supported values are `("before", "after", "both")`. The default is `"after"`



Returns:
    

a dict mapping field names to `Field` instances

validate(_value_ , _** kwargs_)#
    

Make sure that the document instance is an instance of the EmbeddedDocument subclass provided when the document was defined.

auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

property document_type#
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

class fiftyone.core.fields.EmbeddedDocumentListField(_document_type_ , _description =None_, _info =None_, _read_only =False_, _created_at =None_, _** kwargs_)#
    

Bases: `EmbeddedDocumentListField`, `Field`

A field that stores a list of a given type of [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") objects.

Parameters:
    

  * **document_type** â the [`fiftyone.core.odm.BaseEmbeddedDocument`](api__fiftyone.core.odm.md#fiftyone.core.odm.BaseEmbeddedDocument "fiftyone.core.odm.BaseEmbeddedDocument") type stored in this field

  * **description** (_None_) â an optional description

  * **info** (_None_) â an optional info dict

  * **read_only** (_False_) â whether the field is read-only

  * **created_at** (_None_) â the datetime the field was created




**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(value[,Â use_db_field,Â fields]) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Make sure that a list of valid fields is being used.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_value_ , _use_db_field =True_, _fields =None_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Make sure that a list of valid fields is being used.

class fiftyone.core.fields.ReferenceField(_document_type_ , _dbref =False_, _reverse_delete_rule =0_, _** kwargs_)#
    

Bases: `ReferenceField`, `Field`

A reference field.

Parameters:
    

**document_type** â the [`fiftyone.core.odm.Document`](api__fiftyone.core.odm.md#fiftyone.core.odm.Document "fiftyone.core.odm.Document") type stored in this field

**Attributes:**

`auto_creation_counter` |   
---|---  
`created_at` | The datetime the field was created.  
`creation_counter` |   
`description` | A user-editable description of the field.  
`document_type` |   
`info` | A user-editable dictionary of information about the field.  
`name` |   
`owner_document` |   
`path` | The fully-qualified path of this field in the dataset's schema, or `None` if the field is not associated with a dataset.  
`read_only` | Whether the field is read-only.  
  
**Methods:**

`copy`() | Returns a copy of the field.  
---|---  
`error`([message,Â errors,Â field_name]) | Raise a ValidationError.  
`lookup_member`(member_name) |   
`prepare_query_value`(op,Â value) | Prepare a value that is being used in a query for PyMongo.  
`save`([_enforce_read_only]) | Saves any edits to this field's `description` and `info` attributes.  
`set_auto_dereferencing`(value) |   
`to_mongo`(document) | Convert a Python type to a MongoDB-compatible type.  
`to_python`(value) | Convert a MongoDB-compatible type to a Python type.  
`validate`(value) | Perform validation on a value.  
  
auto_creation_counter = -12#
    

copy()#
    

Returns a copy of the field.

The returned copy is not associated with a dataset.

Returns:
    

a `Field`

property created_at#
    

The datetime the field was created.

creation_counter = 323#
    

property description#
    

A user-editable description of the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    

property document_type#
    

error(_message =''_, _errors =None_, _field_name =None_)#
    

Raise a ValidationError.

property info#
    

A user-editable dictionary of information about the field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    

lookup_member(_member_name_)#
    

name = None#
    

property owner_document#
    

property path#
    

The fully-qualified path of this field in the datasetâs schema, or `None` if the field is not associated with a dataset.

prepare_query_value(_op_ , _value_)#
    

Prepare a value that is being used in a query for PyMongo.

property read_only#
    

Whether the field is read-only.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    field = dataset.get_field("uniqueness")
    field.read_only = True
    field.save()
    

save(__enforce_read_only =True_)#
    

Saves any edits to this fieldâs `description` and `info` attributes.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.add_dynamic_sample_fields()
    
    field = dataset.get_field("ground_truth")
    field.description = "Ground truth annotations"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    field = dataset.get_field("ground_truth.detections.area")
    field.description = "Area of the box, in pixels^2"
    field.info = {"url": "https://fiftyone.ai"}
    field.save()
    
    dataset.reload()
    
    field = dataset.get_field("ground_truth")
    print(field.description)  # Ground truth annotations
    print(field.info)  # {'url': 'https://fiftyone.ai'}
    
    field = dataset.get_field("ground_truth.detections.area")
    print(field.description)  # 'Area of the box, in pixels^2'
    field.info = {"url": "https://fiftyone.ai"}
    

set_auto_dereferencing(_value_)#
    

to_mongo(_document_)#
    

Convert a Python type to a MongoDB-compatible type.

to_python(_value_)#
    

Convert a MongoDB-compatible type to a Python type.

validate(_value_)#
    

Perform validation on a value.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
