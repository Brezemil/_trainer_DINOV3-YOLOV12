---
source_url: https://docs.voxel51.com/api/fiftyone.core.config.html
---

# fiftyone.core.config#

FiftyOne config.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Config`() | Base class for JSON serializable config classes.  
---|---  
`Configurable`(config) | Base class for classes that can be initialized with a `Config` instance that configures their behavior.  
`EnvConfig`() |   
`FiftyOneConfig`([d]) | FiftyOne configuration settings.  
`AppConfig`([d]) | FiftyOne App configuration settings.  
`AnnotationConfig`([d]) | FiftyOne annotation configuration settings.  
`EvaluationConfig`([d]) | FiftyOne evaluation configuration settings.  
`HTTPRetryConfig`() | Values used to configure the behavior of the retry logic of HTTP calls made throughout the library.  
  
**Exceptions:**

`FiftyOneConfigError` | Exception raised when a FiftyOne configuration issue is encountered.  
---|---  
`AppConfigError` | Exception raised when an invalid `AppConfig` instance is encountered.  
  
**Functions:**

`locate_config`() | Returns the path to the `FiftyOneConfig` on disk.  
---|---  
`locate_app_config`() | Returns the path to the `AppConfig` on disk.  
`locate_annotation_config`() | Returns the path to the `AnnotationConfig` on disk.  
`locate_evaluation_config`() | Returns the path to the `EvaluationConfig` on disk.  
`load_config`() | Loads the FiftyOne config.  
`load_app_config`() | Loads the FiftyOne App config.  
`load_annotation_config`() | Loads the FiftyOne annotation config.  
`load_evaluation_config`() | Loads the FiftyOne evaluation config.  
  
class fiftyone.core.config.Config#
    

Bases: `Config`

Base class for JSON serializable config classes.

**Methods:**

`attributes`() | Returns a list of class attributes to be serialized.  
---|---  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a Config object from a JSON dictionary.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

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

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a Config object from a JSON dictionary.

Config subclass constructors accept JSON dictionaries, so this method simply passes the dictionary to cls().

Parameters:
    

**d** â a dict of fields expected by cls

Returns:
    

an instance of cls

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

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

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.core.config.Configurable(_config_)#
    

Bases: `Configurable`

Base class for classes that can be initialized with a `Config` instance that configures their behavior.

`Configurable` subclasses must obey the following rules:

>   1. Configurable class `Foo` has an associated Config class `FooConfig` that is importable from the same namespace as `Foo`
> 
>   2. Configurable class `Foo` must be initializable via the syntax `Foo(config)`, where config is a `FooConfig` instance
> 
> 


Parameters:
    

**config** â a `Config`

**Methods:**

`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
---|---  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
  
classmethod from_config(_config_)#
    

Instantiates a Configurable class from a <cls>Config instance.

classmethod from_dict(_d_)#
    

Instantiates a Configurable class from a <cls>Config dict.

Parameters:
    

**d** â a dict to construct a <cls>Config

Returns:
    

an instance of cls

classmethod from_json(_json_path_)#
    

Instantiates a Configurable class from a <cls>Config JSON file.

Parameters:
    

**json_path** â path to a JSON file for type <cls>Config

Returns:
    

an instance of cls

classmethod from_kwargs(_** kwargs_)#
    

Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.

Parameters:
    

****kwargs** â keyword arguments that define the fields of a <cls>Config dict

Returns:
    

an instance of cls

static parse(_class_name_ , _module_name =None_)#
    

Parses a Configurable subclass name string.

Assumes both the Configurable class and the Config class are defined in the same module. The module containing the classes will be loaded if necessary.

Parameters:
    

  * **class_name** â a string containing the name of the Configurable class, e.g. âClassNameâ, or a fully-qualified class name, e.g. âeta.core.config.ClassNameâ

  * **module_name** â a string containing the fully-qualified module name, e.g. âeta.core.configâ, or None if class_name includes the module name. Set module_name = __name__ to load a class from the calling module



Returns:
    

the Configurable class config_cls: the Config class associated with cls

Return type:
    

[cls](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls")

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

class fiftyone.core.config.EnvConfig#
    

Bases: `EnvConfig`

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

This method is called internally by serialize() to determine the class attributes to serialize.

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

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

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.core.config.FiftyOneConfig(_d =None_)#
    

Bases: `EnvConfig`

FiftyOne configuration settings.

**Attributes:**

`show_progress_bars` |   
---|---  
  
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
  
property show_progress_bars#
    

attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

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

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




exception fiftyone.core.config.FiftyOneConfigError#
    

Bases: `EnvConfigError`

Exception raised when a FiftyOne configuration issue is encountered.

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

class fiftyone.core.config.AppConfig(_d =None_)#
    

Bases: `EnvConfig`

FiftyOne App configuration settings.

**Methods:**

`get_colormap`([colorscale,Â n,Â hex_strs]) | Generates a continuous colormap with the specified number of colors from the given colorscale.  
---|---  
`attributes`() | Returns a list of class attributes to be serialized.  
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
  
get_colormap(_colorscale =None_, _n =256_, _hex_strs =False_)#
    

Generates a continuous colormap with the specified number of colors from the given colorscale.

The provided `colorscale` can be any of the following:

  * The string name of any colorscale recognized by plotly. See <https://plotly.com/python/colorscales> for possible options

  * A manually-defined colorscale like the following:
        
        [
            [0.000, "rgb(165,0,38)"],
            [0.111, "rgb(215,48,39)"],
            [0.222, "rgb(244,109,67)"],
            [0.333, "rgb(253,174,97)"],
            [0.444, "rgb(254,224,144)"],
            [0.555, "rgb(224,243,248)"],
            [0.666, "rgb(171,217,233)"],
            [0.777, "rgb(116,173,209)"],
            [0.888, "rgb(69,117,180)"],
            [1.000, "rgb(49,54,149)"],
        ]
        




The colorscale will be sampled evenly at the required resolution in order to generate the colormap.

Parameters:
    

  * **colorscale** (_None_) â a valid colorscale. See above for possible options. By default, `colorscale` is used

  * **n** (_256_) â the desired number of colors

  * **hex_strs** (_False_) â whether to return `#RRGGBB` hex strings rather than `(R, G, B)` tuples



Returns:
    

a list of `(R, G, B)` tuples in [0, 255], or, if `hex_strs` is True, a list of #RRGGBB strings

attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

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

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




exception fiftyone.core.config.AppConfigError#
    

Bases: `EnvConfigError`

Exception raised when an invalid `AppConfig` instance is encountered.

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

class fiftyone.core.config.AnnotationConfig(_d =None_)#
    

Bases: `EnvConfig`

FiftyOne annotation configuration settings.

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

This method is called internally by serialize() to determine the class attributes to serialize.

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

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

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.core.config.EvaluationConfig(_d =None_)#
    

Bases: `EnvConfig`

FiftyOne evaluation configuration settings.

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

This method is called internally by serialize() to determine the class attributes to serialize.

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

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

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



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

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




fiftyone.core.config.locate_config()#
    

Returns the path to the `FiftyOneConfig` on disk.

The default location is `~/.fiftyone/config.json`, but you can override this path by setting the `FIFTYONE_CONFIG_PATH` environment variable.

Note that a config file may not actually exist on disk.

Returns:
    

the path to the `FiftyOneConfig` on disk

fiftyone.core.config.locate_app_config()#
    

Returns the path to the `AppConfig` on disk.

The default location is `~/.fiftyone/app_config.json`, but you can override this path by setting the `FIFTYONE_APP_CONFIG_PATH` environment variable.

Note that the file may not actually exist.

Returns:
    

the path to the `AppConfig` on disk

fiftyone.core.config.locate_annotation_config()#
    

Returns the path to the `AnnotationConfig` on disk.

The default location is `~/.fiftyone/annotation_config.json`, but you can override this path by setting the `FIFTYONE_ANNOTATION_CONFIG_PATH` environment variable.

Note that a config file may not actually exist on disk.

Returns:
    

the path to the `AnnotationConfig` on disk

class fiftyone.core.config.HTTPRetryConfig#
    

Bases: `object`

Values used to configure the behavior of the retry logic of HTTP calls made throughout the library.

NOTE: calls made directly through storage clients (GCS, S3) use their own internal retry logic implementation and may not perfectly match this configuration. This configuration is for direct HTTP requests.

**Attributes:**

`RETRY_CODES` |   
---|---  
`FACTOR` |   
`MAX_TRIES` |   
  
RETRY_CODES = {408, 429, 500, 502, 503, 504, 509}#
    

FACTOR = 0.1#
    

MAX_TRIES = 10#
    

fiftyone.core.config.locate_evaluation_config()#
    

Returns the path to the `EvaluationConfig` on disk.

The default location is `~/.fiftyone/evaluation_config.json`, but you can override this path by setting the `FIFTYONE_EVALUATION_CONFIG_PATH` environment variable.

Note that a config file may not actually exist on disk.

Returns:
    

the path to the `EvaluationConfig` on disk

fiftyone.core.config.load_config()#
    

Loads the FiftyOne config.

Returns:
    

a `FiftyOneConfig` instance

fiftyone.core.config.load_app_config()#
    

Loads the FiftyOne App config.

Returns:
    

an `AppConfig` instance

fiftyone.core.config.load_annotation_config()#
    

Loads the FiftyOne annotation config.

Returns:
    

an `AnnotationConfig` instance

fiftyone.core.config.load_evaluation_config()#
    

Loads the FiftyOne evaluation config.

Returns:
    

an `EvaluationConfig` instance

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
