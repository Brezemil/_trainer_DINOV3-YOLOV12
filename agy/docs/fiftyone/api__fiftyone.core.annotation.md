---
source_url: https://docs.voxel51.com/api/fiftyone.core.annotation.html
---

# fiftyone.core.annotation#

  * [fiftyone.core.annotation.attributes](api__fiftyone.core.annotation.attributes.md)
    * [`MAX_CONDITION_DEPTH`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.MAX_CONDITION_DEPTH)
    * [`attr_insert_to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.attr_insert_to_dict)
    * [`WhenOperator`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator)
      * [`WhenOperator.EQUALS`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.EQUALS)
      * [`WhenOperator.IN`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.IN)
      * [`WhenOperator.AND`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.AND)
      * [`WhenOperator.OR`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.OR)
      * [`WhenOperator.encode()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.encode)
      * [`WhenOperator.replace()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.replace)
      * [`WhenOperator.split()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.split)
      * [`WhenOperator.rsplit()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rsplit)
      * [`WhenOperator.join()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.join)
      * [`WhenOperator.capitalize()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.capitalize)
      * [`WhenOperator.casefold()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.casefold)
      * [`WhenOperator.title()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.title)
      * [`WhenOperator.center()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.center)
      * [`WhenOperator.count()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.count)
      * [`WhenOperator.expandtabs()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.expandtabs)
      * [`WhenOperator.find()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.find)
      * [`WhenOperator.partition()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.partition)
      * [`WhenOperator.index()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.index)
      * [`WhenOperator.ljust()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.ljust)
      * [`WhenOperator.lower()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.lower)
      * [`WhenOperator.lstrip()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.lstrip)
      * [`WhenOperator.rfind()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rfind)
      * [`WhenOperator.rindex()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rindex)
      * [`WhenOperator.rjust()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rjust)
      * [`WhenOperator.rstrip()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rstrip)
      * [`WhenOperator.rpartition()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.rpartition)
      * [`WhenOperator.splitlines()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.splitlines)
      * [`WhenOperator.strip()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.strip)
      * [`WhenOperator.swapcase()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.swapcase)
      * [`WhenOperator.translate()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.translate)
      * [`WhenOperator.upper()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.upper)
      * [`WhenOperator.startswith()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.startswith)
      * [`WhenOperator.endswith()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.endswith)
      * [`WhenOperator.removeprefix()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.removeprefix)
      * [`WhenOperator.removesuffix()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.removesuffix)
      * [`WhenOperator.isascii()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isascii)
      * [`WhenOperator.islower()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.islower)
      * [`WhenOperator.isupper()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isupper)
      * [`WhenOperator.istitle()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.istitle)
      * [`WhenOperator.isspace()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isspace)
      * [`WhenOperator.isdecimal()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isdecimal)
      * [`WhenOperator.isdigit()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isdigit)
      * [`WhenOperator.isnumeric()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isnumeric)
      * [`WhenOperator.isalpha()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isalpha)
      * [`WhenOperator.isalnum()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isalnum)
      * [`WhenOperator.isidentifier()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isidentifier)
      * [`WhenOperator.isprintable()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.isprintable)
      * [`WhenOperator.zfill()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.zfill)
      * [`WhenOperator.format()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.format)
      * [`WhenOperator.format_map()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.format_map)
      * [`WhenOperator.maketrans()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOperator.maketrans)
    * [`WhenCondition`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenCondition)
      * [`WhenCondition.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenCondition.to_dict)
      * [`WhenCondition.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenCondition.from_dict)
    * [`collect_leaf_conditions()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.collect_leaf_conditions)
    * [`When`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When)
      * [`When.operator`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.operator)
      * [`When.field`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.field)
      * [`When.value`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.value)
      * [`When.then`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.then)
      * [`When.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.to_dict)
      * [`When.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.When.from_dict)
    * [`WhenEquals`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals)
      * [`WhenEquals.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.from_dict)
      * [`WhenEquals.then`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.then)
      * [`WhenEquals.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.to_dict)
      * [`WhenEquals.operator`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.operator)
      * [`WhenEquals.field`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.field)
      * [`WhenEquals.value`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenEquals.value)
    * [`WhenIn`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn)
      * [`WhenIn.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.from_dict)
      * [`WhenIn.then`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.then)
      * [`WhenIn.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.to_dict)
      * [`WhenIn.operator`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.operator)
      * [`WhenIn.field`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.field)
      * [`WhenIn.value`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenIn.value)
    * [`WhenAnd`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenAnd)
      * [`WhenAnd.conditions`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenAnd.conditions)
      * [`WhenAnd.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenAnd.to_dict)
      * [`WhenAnd.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenAnd.from_dict)
    * [`WhenOr`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOr)
      * [`WhenOr.conditions`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOr.conditions)
      * [`WhenOr.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOr.to_dict)
      * [`WhenOr.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.WhenOr.from_dict)
    * [`AttributeSpec`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec)
      * [`AttributeSpec.name`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.name)
      * [`AttributeSpec.type`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.type)
      * [`AttributeSpec.component`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.component)
      * [`AttributeSpec.values`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.values)
      * [`AttributeSpec.when`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.when)
      * [`AttributeSpec.read_only`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.read_only)
      * [`AttributeSpec.default`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.default)
      * [`AttributeSpec.range`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.range)
      * [`AttributeSpec.precision`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.precision)
      * [`AttributeSpec.to_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.to_dict)
      * [`AttributeSpec.from_dict()`](api__fiftyone.core.annotation.attributes.md#fiftyone.core.annotation.attributes.AttributeSpec.from_dict)
  * [fiftyone.core.annotation.constants](api__fiftyone.core.annotation.constants.md)
  * [fiftyone.core.annotation.generate_label_schemas](api__fiftyone.core.annotation.generate_label_schemas.md)
    * [`generate_label_schemas()`](api__fiftyone.core.annotation.generate_label_schemas.md#fiftyone.core.annotation.generate_label_schemas.generate_label_schemas)
  * [fiftyone.core.annotation.hydrate_label_schemas](api__fiftyone.core.annotation.hydrate_label_schemas.md)
    * [`attributes_with_source()`](api__fiftyone.core.annotation.hydrate_label_schemas.md#fiftyone.core.annotation.hydrate_label_schemas.attributes_with_source)
    * [`hydrate_applied_ontology()`](api__fiftyone.core.annotation.hydrate_label_schemas.md#fiftyone.core.annotation.hydrate_label_schemas.hydrate_applied_ontology)
    * [`dehydrate_applied_ontology()`](api__fiftyone.core.annotation.hydrate_label_schemas.md#fiftyone.core.annotation.hydrate_label_schemas.dehydrate_applied_ontology)
    * [`inline_applied_ontology()`](api__fiftyone.core.annotation.hydrate_label_schemas.md#fiftyone.core.annotation.hydrate_label_schemas.inline_applied_ontology)
  * [fiftyone.core.annotation.utils](api__fiftyone.core.annotation.utils.md)
    * [`ensure_collection_is_supported()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.ensure_collection_is_supported)
    * [`get_supported_app_annotation_fields()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.get_supported_app_annotation_fields)
    * [`list_valid_annotation_fields()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.list_valid_annotation_fields)
    * [`flatten_fields()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.flatten_fields)
    * [`get_type()`](api__fiftyone.core.annotation.utils.md#fiftyone.core.annotation.utils.get_type)
  * [fiftyone.core.annotation.validate_label_schemas](api__fiftyone.core.annotation.validate_label_schemas.md)
    * [`ValidationErrors`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors)
      * [`ValidationErrors.add_note()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.add_note)
      * [`ValidationErrors.args`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.args)
      * [`ValidationErrors.derive()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.derive)
      * [`ValidationErrors.exceptions`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.exceptions)
      * [`ValidationErrors.message`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.message)
      * [`ValidationErrors.split()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.split)
      * [`ValidationErrors.subgroup()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.subgroup)
      * [`ValidationErrors.with_traceback()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.ValidationErrors.with_traceback)
    * [`validate_label_schemas()`](api__fiftyone.core.annotation.validate_label_schemas.md#fiftyone.core.annotation.validate_label_schemas.validate_label_schemas)



## Module contents#

Annotation framework

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`AnnotationInfo`(key[,Â version,Â timestamp,Â config]) | Information about an annotation run on a dataset.  
---|---  
`AnnotationMethodConfig`(**kwargs) | Base class for configuring `AnnotationMethod` instances.  
`AnnotationMethod`(config) | Base class for annotation methods.  
`AnnotationResults`(samples,Â config,Â key[,Â ...]) | Base class for annotation run results.  
  
class fiftyone.core.annotation.AnnotationInfo(_key_ , _version =None_, _timestamp =None_, _config =None_)#
    

Bases: [`BaseRunInfo`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunInfo "fiftyone.core.runs.BaseRunInfo")

Information about an annotation run on a dataset.

Parameters:
    

  * **key** â the annotation key

  * **timestamp** (_None_) â the UTC `datetime` when the annotation run was initiated

  * **config** (_None_) â the `AnnotationMethodConfig` for the run




**Methods:**

`config_cls`() | The `BaseRunConfig` class associated with this class.  
---|---  
`attributes`() | Returns a list of class attributes to be serialized.  
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
  
classmethod config_cls()#
    

The `BaseRunConfig` class associated with this class.

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




class fiftyone.core.annotation.AnnotationMethodConfig(_** kwargs_)#
    

Bases: [`BaseRunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunConfig "fiftyone.core.runs.BaseRunConfig")

Base class for configuring `AnnotationMethod` instances.

Parameters:
    

****kwargs** â any leftover keyword arguments after subclasses have done their parsing

**Attributes:**

`type` | The type of run.  
---|---  
`method` | The name of the method.  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`run_cls` | The `BaseRun` class associated with this config.  
  
**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
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
  
property type#
    

The type of run.

property method#
    

The name of the method.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

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
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

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

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

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

property run_cls#
    

The `BaseRun` class associated with this config.

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




class fiftyone.core.annotation.AnnotationMethod(_config_)#
    

Bases: [`BaseRun`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRun "fiftyone.core.runs.BaseRun")

Base class for annotation methods.

Parameters:
    

**config** â an `AnnotationMethodConfig`

**Methods:**

`run_info_cls`() | The `BaseRunInfo` class associated with this class.  
---|---  
`cleanup`(samples,Â key) | Cleans up the results of the run with the given key from the collection.  
`delete_run`(samples,Â key[,Â cleanup]) | Deletes the results associated with the given run key from the collection.  
`delete_runs`(samples[,Â cleanup]) | Deletes all runs from the collection.  
`ensure_requirements`() | Ensures that any necessary packages to execute this run are installed.  
`ensure_usage_requirements`() | Ensures that any necessary packages to use existing results for this run are installed.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_fields`(samples,Â key) | Gets the fields that were involved in the given run.  
`get_run_info`(samples,Â key) | Gets the `BaseRunInfo` for the given key on the collection.  
`has_cached_run_results`(samples,Â key) | Determines whether `BaseRunResults` for the given key are cached on the collection.  
`list_runs`(samples[,Â type,Â method]) | Returns the list of run keys on the given collection.  
`load_run_results`(samples,Â key[,Â cache,Â ...]) | Loads the `BaseRunResults` for the given key on the collection.  
`load_run_view`(samples,Â key[,Â select_fields]) | Loads the view on which the specified run was performed.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`register_run`(samples,Â key[,Â overwrite,Â cleanup]) | Registers a run of this method under the given key on the given collection.  
`rename`(samples,Â key,Â new_key) | Performs any necessary operations required to rename this run's key.  
`save_run_info`(samples,Â run_info[,Â ...]) | Saves the run information on the collection.  
`save_run_results`(samples,Â key,Â run_results) | Saves the run results on the collection.  
`update_run_config`(samples,Â key,Â config) | Updates the `BaseRunConfig` for the given run on the collection.  
`update_run_key`(samples,Â key,Â new_key) | Replaces the key for the given run with a new key.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
`validate_run`(samples,Â key[,Â overwrite]) | Validates that the collection can accept this run.  
  
classmethod run_info_cls()#
    

The `BaseRunInfo` class associated with this class.

cleanup(_samples_ , _key_)#
    

Cleans up the results of the run with the given key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key




classmethod delete_run(_samples_ , _key_ , _cleanup =True_)#
    

Deletes the results associated with the given run key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **cleanup** (_True_) â whether to execute the runâs `BaseRun.cleanup()` method




classmethod delete_runs(_samples_ , _cleanup =True_)#
    

Deletes all runs from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **cleanup** (_True_) â whether to execute the runâs `BaseRun.cleanup()` methods




ensure_requirements()#
    

Ensures that any necessary packages to execute this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

ensure_usage_requirements()#
    

Ensures that any necessary packages to use existing results for this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

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

get_fields(_samples_ , _key_)#
    

Gets the fields that were involved in the given run.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

a list of fields

classmethod get_run_info(_samples_ , _key_)#
    

Gets the `BaseRunInfo` for the given key on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

a `BaseRunInfo`

classmethod has_cached_run_results(_samples_ , _key_)#
    

Determines whether `BaseRunResults` for the given key are cached on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

True/False

classmethod list_runs(_samples_ , _type =None_, _method =None_, _** kwargs_)#
    

Returns the list of run keys on the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **type** (_None_) â 

a specific run type to match, which can be:

    * a string [`fiftyone.core.runs.BaseRunConfig.type`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunConfig.type "fiftyone.core.runs.BaseRunConfig.type")

    * a [`fiftyone.core.runs.BaseRun`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRun "fiftyone.core.runs.BaseRun") class or its fully-qualified class name string

  * **method** (_None_) â a specific [`fiftyone.core.runs.BaseRunConfig.method`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunConfig.method "fiftyone.core.runs.BaseRunConfig.method") string to match

  * ****kwargs** â optional config parameters to match



Returns:
    

a list of run keys

classmethod load_run_results(_samples_ , _key_ , _cache =True_, _load_view =True_, _** kwargs_)#
    

Loads the `BaseRunResults` for the given key on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **cache** (_True_) â whether to cache the results on the collection

  * **load_view** (_True_) â whether to load the run view in the results (True) or the full dataset (False)

  * ****kwargs** â keyword arguments for the runâs `BaseRunConfig.load_credentials()` method



Returns:
    

a `BaseRunResults`, or None if the run did not save results

classmethod load_run_view(_samples_ , _key_ , _select_fields =False_)#
    

Loads the view on which the specified run was performed.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **select_fields** (_False_) â whether to exclude fields involved in other runs of the same type



Returns:
    

a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

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

register_run(_samples_ , _key_ , _overwrite =True_, _cleanup =True_)#
    

Registers a run of this method under the given key on the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **overwrite** (_True_) â whether to allow overwriting an existing run of the same type

  * **cleanup** (_True_) â whether to execute an existing runâs `BaseRun.cleanup()` method when overwriting it




rename(_samples_ , _key_ , _new_key_)#
    

Performs any necessary operations required to rename this runâs key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **new_key** â a new run key




classmethod save_run_info(_samples_ , _run_info_ , _overwrite =True_, _cleanup =True_)#
    

Saves the run information on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **run_info** â a `BaseRunInfo`

  * **overwrite** (_True_) â whether to overwrite an existing run with the same key

  * **cleanup** (_True_) â whether to execute an existing runâs `BaseRun.cleanup()` method when overwriting it




classmethod save_run_results(_samples_ , _key_ , _run_results_ , _overwrite =True_, _cache =True_)#
    

Saves the run results on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **run_results** â a `BaseRunResults`, or None

  * **overwrite** (_True_) â whether to overwrite an existing result with the same key

  * **cache** (_True_) â whether to cache the results on the collection




classmethod update_run_config(_samples_ , _key_ , _config_)#
    

Updates the `BaseRunConfig` for the given run on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **config** â a `BaseRunConfig`




classmethod update_run_key(_samples_ , _key_ , _new_key_)#
    

Replaces the key for the given run with a new key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **new_key** â a new run key




classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

validate_run(_samples_ , _key_ , _overwrite =True_)#
    

Validates that the collection can accept this run.

The run may be invalid if, for example, a run of a different type has already been run under the same key and thus overwriting it would cause ambiguity on how to cleanup the results.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **overwrite** (_True_) â whether to allow overwriting an existing run of the same type



Raises:
    

**ValueError** â if the run is invalid

class fiftyone.core.annotation.AnnotationResults(_samples_ , _config_ , _key_ , _backend =None_)#
    

Bases: [`BaseRunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunResults "fiftyone.core.runs.BaseRunResults")

Base class for annotation run results.

**Methods:**

`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
---|---  
`base_results_cls`(type) | Returns the results class for the given run type.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

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

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

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

property key#
    

The run key for these results.

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

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




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
