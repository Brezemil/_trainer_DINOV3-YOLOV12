---
source_url: https://docs.voxel51.com/api/fiftyone.core.state.html
---

# fiftyone.core.state#

Defines the shared state between the FiftyOne App and backend.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`StateDescription`([color_scheme,Â config,Â ...]) | Class that describes the shared state between the FiftyOne App and a corresponding [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session").  
---|---  
`SampleField`(*,Â ftype,Â path,Â subfield,Â ...) |   
  
**Functions:**

`serialize_fields`(schema) |   
---|---  
`build_color_scheme`([color_scheme,Â dataset,Â ...]) |   
  
class fiftyone.core.state.StateDescription(_color_scheme =None_, _config =None_, _dataset =None_, _field_visibility_stage =None_, _group_id =None_, _group_slice =None_, _sample_id =None_, _selected =None_, _selected_labels =None_, _selected_samples =None_, _sample_selection_style =None_, _label_selection_style =None_, _spaces =None_, _view =None_, _view_name =None_)#
    

Bases: `Serializable`

Class that describes the shared state between the FiftyOne App and a corresponding [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session").

Parameters:
    

  * **color_scheme** (_None_) â a [`fiftyone.core.odm.dataset.ColorScheme`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme")

  * **config** (_None_) â an optional [`fiftyone.core.config.AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig")

  * **dataset** (_None_) â the current [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **field_visibility_stage** (_None_) â a field visibility stage

  * **group_id** (_None_) â a [`fiftyone.core.groups.Group.id`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group.id "fiftyone.core.groups.Group.id")

  * **group_slice** (_None_) â a [`fiftyone.core.groups.Group.name`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group.name "fiftyone.core.groups.Group.name")

  * **sample_id** (_None_) â a `fiftyone.core.sample.Sample.id`

  * **selected_labels** (_None_) â the list of currently selected labels

  * **selected_samples** (_None_) â a list of dicts with sample selection info

  * **sample_selection_style** (_None_) â a dict mapping selection types to icon style names (e.g. `{"default": "checkmark", "alt": "thumbsdown"}`)

  * **label_selection_style** (_None_) â a dict mapping selection types to label selection style names (e.g. `{"default": "dashed", "alt": "dashed-red"}`)

  * **spaces** (_None_) â a [`fiftyone.core.odm.workspace.Space`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space")

  * **view** (_None_) â the current [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

  * **view_name** (_None_) â the name of the view if the current view is a saved view




**Methods:**

`attributes`() | Returns a list of class attributes to be serialized.  
---|---  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`from_dict`(d) | Constructs a `StateDescription` from a JSON dictionary.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

serialize(_reflective =True_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

classmethod from_dict(_d_)#
    

Constructs a `StateDescription` from a JSON dictionary.

Parameters:
    

**d** â a JSON dictionary

Returns:
    

`StateDescription`

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.core.state.SampleField(_*, ftype: str, path: str, subfield: Optional[str], embedded_doc_type: Optional[str], db_field: Optional[str], description: Optional[str], info: Optional[<strawberry.types.scalar.ScalarWrapper object at 0x7f315f768c90>]_)#
    

Bases: `object`

**Attributes:**

`ftype` |   
---|---  
`path` |   
`subfield` |   
`embedded_doc_type` |   
`db_field` |   
`description` |   
`info` |   
  
ftype: str#
    

path: str#
    

subfield: str | None#
    

embedded_doc_type: str | None#
    

db_field: str | None#
    

description: str | None#
    

info: <strawberry.types.scalar.ScalarWrapper object at 0x7f315f768c90> | None#
    

fiftyone.core.state.serialize_fields(_schema : Dict_) → List[SampleField]#
    

fiftyone.core.state.build_color_scheme(_color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") | None = None_, _dataset : [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") | None = None_, _app_config : [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") | None = None_) → [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme")#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
