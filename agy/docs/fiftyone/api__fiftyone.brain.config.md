---
source_url: https://docs.voxel51.com/api/fiftyone.brain.config.html
---

# fiftyone.brain.config#

Brain config.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`BrainConfig`([d]) | FiftyOne brain configuration settings.  
---|---  
  
**Functions:**

`locate_brain_config`() | Returns the path to the `BrainConfig` on disk.  
---|---  
`load_brain_config`() | Loads the FiftyOne brain config.  
  
class fiftyone.brain.config.BrainConfig(_d =None_)#
    

Bases: [`EnvConfig`](api__fiftyone.core.config.md#fiftyone.core.config.EnvConfig "fiftyone.core.config.EnvConfig")

FiftyOne brain configuration settings.

**Methods:**

`attributes`() | Returns a list of class attributes to be serialized.  
---|---  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d) | Constructs an EnvConfig object from a JSON dictionary.  
`from_json`(path) | Constructs an EnvConfig object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`parse_bool`(d,Â key[,Â env_var,Â default]) | Parses a boolean value.  
`parse_dict`(d,Â key[,Â env_var,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â env_var,Â default]) | Parses an integer attribute.  
`parse_number`(d,Â key[,Â env_var,Â default]) | Parses a number attribute.  
`parse_path`(d,Â key[,Â env_var,Â default]) | Parses a path attribute.  
`parse_path_array`(d,Â key[,Â env_var,Â default]) | Parses a path array attribute.  
`parse_string`(d,Â key[,Â env_var,Â default]) | Parses a string attribute.  
`parse_string_array`(d,Â key[,Â env_var,Â default]) | Parses a string array attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by `serialize()` to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the `@property` decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_)#
    

Constructs an EnvConfig object from a JSON dictionary.

EnvConfig subclass constructors accept JSON dictionaries, so this method simply passes the dictionary to cls().

Parameters:
    

**d** â a JSON dictionary containing the fields expected by cls

Returns:
    

an instance of cls

classmethod from_json(_path_)#
    

Constructs an EnvConfig object from a JSON file.

EnvConfig instances allow their values to be overriden by environment variables, so, if the JSON file does not exist, this method silently loads an empty dictionary in its place.

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for `self.from_dict()`

  * ****kwargs** â optional keyword arguments for `self.from_dict()`



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

static parse_bool(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_dict(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_int(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default integer value to return if key is not present



Returns:
    

an int

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_number(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_path(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default string to return if key is not present



Returns:
    

a path string

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_path_array(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a path array attribute.

Each path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default list to return if key is not present



Returns:
    

a list of path strings

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_string(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default string to return if key is not present



Returns:
    

a string

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

static parse_string_array(_d_ , _key_ , _env_var =None_, _default =<eta.core.config.NoDefault object>_)#
    

Parses a string array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **env_var** â an optional environment variable to load the attribute from rather than using the JSON dictionary

  * **default** â an optional default list to return if key is not present



Returns:
    

a list of strings

Raises:
    

**EnvConfigError** â if the environment variable, the dictionary key, or a default value was not provided

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for `self.serialize()`



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for `self.serialize()`




fiftyone.brain.config.locate_brain_config()#
    

Returns the path to the `BrainConfig` on disk.

The default location is `~/.fiftyone/brain_config.json`, but you can override this path by setting the `FIFTYONE_BRAIN_CONFIG_PATH` environment variable.

Note that a config file may not actually exist on disk.

Returns:
    

the path to the `BrainConfig` on disk

fiftyone.brain.config.load_brain_config()#
    

Loads the FiftyOne brain config.

Returns:
    

a `BrainConfig` instance

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
