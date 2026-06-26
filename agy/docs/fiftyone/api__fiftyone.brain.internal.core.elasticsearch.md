---
source_url: https://docs.voxel51.com/api/fiftyone.brain.internal.core.elasticsearch.html
---

# fiftyone.brain.internal.core.elasticsearch#

Elastisearch similarity backend.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ElasticsearchSimilarityConfig`([index_name,Â ...]) | Configuration for a Elasticsearch similarity instance.  
---|---  
`ElasticsearchSimilarity`(config) | Elasticsearch similarity factory.  
`ElasticsearchSimilarityIndex`(samples,Â ...[,Â ...]) | Class for interacting with Elasticsearch similarity indexes.  
  
class fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig(_index_name =None_, _metric ='cosine'_, _hosts =None_, _cloud_id =None_, _username =None_, _password =None_, _api_key =None_, _ca_certs =None_, _bearer_auth =None_, _ssl_assert_fingerprint =None_, _verify_certs =None_, _** kwargs_)#
    

Bases: [`SimilarityConfig`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityConfig "fiftyone.brain.similarity.SimilarityConfig")

Configuration for a Elasticsearch similarity instance.

Parameters:
    

  * **index_name** (_None_) â the name of the Elasticsearch index to use or create. If none is provided, a new index will be created

  * **metric** (_"cosine"_) â the embedding distance metric to use when creating a new index. Supported values are `("cosine", "dotproduct", "euclidean", "innerproduct")`

  * **hosts** (_None_) â the full Elasticsearch server address(es) to use. Can be a string or list of strings

  * **cloud_id** (_None_) â the Cloud ID of an Elastic Cloud to connect to

  * **username** (_None_) â a username to use

  * **password** (_None_) â a password to use

  * **api_key** (_None_) â an API key to use

  * **ca_certs** (_None_) â a path to a CA certificate

  * **bearer_auth** (_None_) â a bearer token to use

  * **ssl_assert_fingerprint** (_None_) â a SHA256 fingerprint to use

  * **verify_certs** (_None_) â whether to verify SSL certificates

  * ****kwargs** â keyword arguments for [`fiftyone.brain.similarity.SimilarityConfig`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityConfig "fiftyone.brain.similarity.SimilarityConfig")




**Attributes:**

`method` | The name of the similarity backend.  
---|---  
`hosts` |   
`cloud_id` |   
`username` |   
`password` |   
`api_key` |   
`ca_certs` |   
`bearer_auth` |   
`ssl_assert_fingerprint` |   
`verify_certs` |   
`max_k` | A maximum k value for nearest neighbor queries, or None if there is no limit.  
`supports_least_similarity` | Whether this backend supports least similarity queries.  
`supported_aggregations` | A tuple of supported values for the `aggregation` parameter of the backend's `sort_by_similarity()` and `_kneighbors()` methods.  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`run_cls` | The `BaseRun` class associated with this config.  
`type` | The type of run.  
  
**Methods:**

`load_credentials`([hosts,Â cloud_id,Â ...]) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
---|---  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
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
  
property method#
    

The name of the similarity backend.

property hosts#
    

property cloud_id#
    

property username#
    

property password#
    

property api_key#
    

property ca_certs#
    

property bearer_auth#
    

property ssl_assert_fingerprint#
    

property verify_certs#
    

property max_k#
    

A maximum k value for nearest neighbor queries, or None if there is no limit.

property supports_least_similarity#
    

Whether this backend supports least similarity queries.

property supported_aggregations#
    

A tuple of supported values for the `aggregation` parameter of the backendâs `sort_by_similarity()` and `_kneighbors()` methods.

load_credentials(_hosts =None_, _cloud_id =None_, _username =None_, _password =None_, _api_key =None_, _ca_certs =None_, _bearer_auth =None_, _ssl_assert_fingerprint =None_, _verify_certs =None_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

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
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the `@property` decorator. By default, this is False

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

  * ***args** â optional positional arguments for `self.from_dict()`

  * ****kwargs** â optional keyword arguments for `self.from_dict()`



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

  * ***args** â optional positional arguments for `self.from_dict()`

  * ****kwargs** â optional keyword arguments for `self.from_dict()`



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
    

the raw (untouched) value of the given field, which is equal to a value from `choices`

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

  * ****kwargs** â optional keyword arguments for `self.serialize()`



Returns:
    

a string representation of the object

property type#
    

The type of run.

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

  * ****kwargs** â optional keyword arguments for `self.serialize()`




class fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarity(_config_)#
    

Bases: [`Similarity`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.Similarity "fiftyone.brain.similarity.Similarity")

Elasticsearch similarity factory.

Parameters:
    

**config** â a `ElasticsearchSimilarityConfig`

**Methods:**

`ensure_requirements`() | Ensures that any necessary packages to execute this run are installed.  
---|---  
`ensure_usage_requirements`() | Ensures that any necessary packages to use existing results for this run are installed.  
`initialize`(samples,Â brain_key) | Initializes a similarity index.  
`cleanup`(samples,Â key) | Cleans up the results of the run with the given key from the collection.  
`delete_run`(samples,Â key[,Â cleanup]) | Deletes the results associated with the given run key from the collection.  
`delete_runs`(samples[,Â cleanup]) | Deletes all runs from the collection.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_fields`(samples,Â brain_key) | Gets the fields that were involved in the given run.  
`get_run_info`(samples,Â key) | Gets the `BaseRunInfo` for the given key on the collection.  
`has_cached_run_results`(samples,Â key) | Determines whether `BaseRunResults` for the given key are cached on the collection.  
`list_runs`(samples[,Â type,Â method]) | Returns the list of run keys on the given collection.  
`load_run_results`(samples,Â key[,Â cache,Â ...]) | Loads the `BaseRunResults` for the given key on the collection.  
`load_run_view`(samples,Â key[,Â select_fields]) | Loads the view on which the specified run was performed.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`register_run`(samples,Â key[,Â overwrite,Â cleanup]) | Registers a run of this method under the given key on the given collection.  
`rename`(samples,Â key,Â new_key) | Performs any necessary operations required to rename this run's key.  
`run_info_cls`() | The `BaseRunInfo` class associated with this class.  
`save_run_info`(samples,Â run_info[,Â ...]) | Saves the run information on the collection.  
`save_run_results`(samples,Â key,Â run_results) | Saves the run results on the collection.  
`update_run_config`(samples,Â key,Â config) | Updates the `BaseRunConfig` for the given run on the collection.  
`update_run_key`(samples,Â key,Â new_key) | Replaces the key for the given run with a new key.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
`validate_run`(samples,Â key[,Â overwrite]) | Validates that the collection can accept this run.  
  
ensure_requirements()#
    

Ensures that any necessary packages to execute this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

ensure_usage_requirements()#
    

Ensures that any necessary packages to use existing results for this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

initialize(_samples_ , _brain_key_)#
    

Initializes a similarity index.

Parameters:
    

  * **samples** â a `fiftyone.core.collections.SampleColllection`

  * **brain_key** â the brain key



Returns:
    

a `SimilarityIndex`

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

get_fields(_samples_ , _brain_key_)#
    

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
    

cls

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




classmethod run_info_cls()#
    

The `BaseRunInfo` class associated with this class.

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

class fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityIndex(_samples_ , _config_ , _brain_key_ , _backend =None_)#
    

Bases: [`SimilarityIndex`](api__fiftyone.brain.similarity.md#fiftyone.brain.similarity.SimilarityIndex "fiftyone.brain.similarity.SimilarityIndex")

Class for interacting with Elasticsearch similarity indexes.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `ElasticsearchSimilarityConfig` used

  * **brain_key** â the brain key

  * **backend** (_None_) â a `ElasticsearchSimilarity` instance




**Attributes:**

`total_index_size` | The total number of data points in the index.  
---|---  
`client` | The `elasticsearch.Elasticsearch` instance for this index.  
`backend` | The `BaseRun` for these results.  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `SimilarityConfig` for these results.  
`current_label_ids` | The label IDs of the currently active data points in the index, or `None` if not applicable.  
`current_sample_ids` | The sample IDs of the currently active data points in the index.  
`has_view` | Whether the index is currently restricted to a view.  
`index_size` | The number of active data points in the index.  
`is_external` | Whether this similarity index manages its own embeddings (True) or loads them directly from the `embeddings_field` of the dataset (False).  
`key` | The run key for these results.  
`label_ids` | The label IDs of the full index, or `None` if not applicable or not supported.  
`missing_size` | The total number of data points in `view()` that are missing from this index, or `None` if unknown.  
`sample_ids` | The sample IDs of the full index, or `None` if not supported.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
`supports_prompts` | Whether this similarity index supports prompt queries.  
`view` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") against which results are currently being generated.  
  
**Methods:**

`add_to_index`(embeddings,Â sample_ids[,Â ...]) | Adds the given embeddings to the index.  
---|---  
`remove_from_index`([sample_ids,Â label_ids,Â ...]) | Removes the specified embeddings from the index.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`clear_view`() | Clears the view set by `use_view()`, if any.  
`compute_embeddings`(samples[,Â model,Â ...]) | Computes embeddings for the given samples using this backend's model.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`get_embeddings`([sample_ids,Â label_ids,Â ...]) | Retrieves the embeddings for the given IDs from the index.  
`get_model`() | Returns the stored model for this index.  
`reload`() | Reloads the index for the current view.  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`sort_by_similarity`(query[,Â k,Â reverse,Â ...]) | Returns a view that sorts the samples/labels in `view()` by similarity to the specified query.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_view`(samples[,Â allow_missing,Â warn_missing]) | Restricts the index to the provided view.  
`values`(path_or_expr) | Extracts a flat list of values from the given field or expression corresponding to the current `view()`.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
`cleanup`() | Deletes the similarity index from the backend.  
  
property total_index_size#
    

The total number of data points in the index.

If `use_view()` has been called to restrict the index, this value may be larger than the current `index_size()`.

property client#
    

The `elasticsearch.Elasticsearch` instance for this index.

add_to_index(_embeddings_ , _sample_ids_ , _label_ids =None_, _overwrite =True_, _allow_existing =True_, _warn_existing =False_, _reload =True_, _batch_size =500_)#
    

Adds the given embeddings to the index.

Parameters:
    

  * **embeddings** â a `num_embeddings x num_dims` array of embeddings

  * **sample_ids** â a `num_embeddings` array of sample IDs

  * **label_ids** (_None_) â a `num_embeddings` array of label IDs, if applicable

  * **overwrite** (_True_) â whether to replace (True) or ignore (False) existing embeddings with the same sample/label IDs

  * **allow_existing** (_True_) â whether to ignore (True) or raise an error (False) when `overwrite` is False and a provided ID already exists in the

  * **warn_existing** (_False_) â whether to log a warning if an embedding is not added to the index because its ID already exists

  * **reload** (_True_) â whether to call `reload()` to refresh the current view after the update




remove_from_index(_sample_ids =None_, _label_ids =None_, _allow_missing =True_, _warn_missing =False_, _reload =True_)#
    

Removes the specified embeddings from the index.

Parameters:
    

  * **sample_ids** (_None_) â an array of sample IDs

  * **label_ids** (_None_) â an array of label IDs, if applicable

  * **allow_missing** (_True_) â whether to allow the index to not contain IDs that you provide (True) or whether to raise an error in this case (False)

  * **warn_missing** (_False_) â whether to log a warning if the index does not contain IDs that you provide

  * **reload** (_True_) â whether to call `reload()` to refresh the current view after the update




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

clear_view()#
    

Clears the view set by `use_view()`, if any.

Subsequent operations will be performed on the full index.

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

compute_embeddings(_samples_ , _model =None_, _batch_size =None_, _num_workers =None_, _skip_failures =True_, _skip_existing =False_, _warn_existing =False_, _force_square =False_, _alpha =None_, _progress =None_)#
    

Computes embeddings for the given samples using this backendâs model.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **model** (_None_) â a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") to apply. If not provided, these results must have been created with a stored model, which will be used by default

  * **batch_size** (_None_) â an optional batch size to use when computing embeddings. Only applicable when a `model` is provided

  * **num_workers** (_None_) â the number of workers to use when loading images. Only applicable when a Torch-based model is being used to compute embeddings

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if embeddings cannot be generated for a sample

  * **skip_existing** (_False_) â whether to skip generating embeddings for sample/label IDs that are already in the index

  * **warn_existing** (_False_) â whether to log a warning if any IDs already exist in the index

  * **force_square** (_False_) â whether to minimally manipulate the patch bounding boxes into squares prior to extraction. Only applicable when a `model` and `patches_field` are specified

  * **alpha** (_None_) â an optional expansion/contraction to apply to the patches before extracting them, in `[-1, inf)`. If provided, the length and width of the box are expanded (or contracted, when `alpha < 0`) by `(100 * alpha)%`. For example, set `alpha = 0.1` to expand the boxes by 10%, and set `alpha = -0.1` to contract the boxes by 10%. Only applicable when a `model` and `patches_field` are specified

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

  * a `num_embeddings x num_dims` array of embeddings

  * a `num_embeddings` array of sample IDs

  * a `num_embeddings` array of label IDs, if applicable, or else `None`




Return type:
    

a tuple of

property config#
    

The `SimilarityConfig` for these results.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

property current_label_ids#
    

The label IDs of the currently active data points in the index, or `None` if not applicable.

If `use_view()` has been called, this may be a subset of the full index.

If the index does not support full label ID lists (ie if `label_ids()` is `None`), then this will be all label IDs in the current `view()` regardless of whether all labels are indexed.

property current_sample_ids#
    

The sample IDs of the currently active data points in the index.

If `use_view()` has been called, this may be a subset of the full index.

If the index does not support full sample ID lists (ie if `sample_ids()` is `None`), then this will be all sample IDs in the current `view()` regardless of whether all samples are indexed.

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the `@property` decorator. By default, this is False

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

  * ***args** â optional positional arguments for `self.from_dict()`

  * ****kwargs** â optional keyword arguments for `self.from_dict()`



Returns:
    

an instance of the Serializable class

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

get_embeddings(_sample_ids =None_, _label_ids =None_, _allow_missing =True_, _warn_missing =False_)#
    

Retrieves the embeddings for the given IDs from the index.

If no IDs are provided, the entire index is returned.

Parameters:
    

  * **sample_ids** (_None_) â a sample ID or list of sample IDs for which to retrieve embeddings

  * **label_ids** (_None_) â a label ID or list of label IDs for which to retrieve embeddings

  * **allow_missing** (_True_) â whether to allow the index to not contain IDs that you provide (True) or whether to raise an error in this case (False)

  * **warn_missing** (_False_) â whether to log a warning if the index does not contain IDs that you provide



Returns:
    

  * a `num_embeddings x num_dims` array of embeddings

  * a `num_embeddings` array of sample IDs

  * a `num_embeddings` array of label IDs, if applicable, or else `None`




Return type:
    

a tuple of

get_model()#
    

Returns the stored model for this index.

Returns:
    

a [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model")

property has_view#
    

Whether the index is currently restricted to a view.

Use `use_view()` to restrict the index to a view, and use `clear_view()` to reset to the full index.

property index_size#
    

The number of active data points in the index.

If `use_view()` has been called to restrict the index, this property will reflect the size of the active index.

property is_external#
    

Whether this similarity index manages its own embeddings (True) or loads them directly from the `embeddings_field` of the dataset (False).

property key#
    

The run key for these results.

property label_ids#
    

The label IDs of the full index, or `None` if not applicable or not supported.

property missing_size#
    

The total number of data points in `view()` that are missing from this index, or `None` if unknown.

This property is only applicable when `use_view()` has been called, and it will be `None` if no data points are missing or when the backend does not support it.

reload()#
    

Reloads the index for the current view.

Subclasses may override this method, but by default this method simply passes the current `view()` back into `use_view()`, which updates the indexâs current ID set based on any changes to the view since the index was last loaded.

property sample_ids#
    

The sample IDs of the full index, or `None` if not supported.

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

sort_by_similarity(_query_ , _k =None_, _reverse =False_, _aggregation ='mean'_, _dist_field =None_, __mongo =False_)#
    

Returns a view that sorts the samples/labels in `view()` by similarity to the specified query.

When querying by IDs, the query can be any ID(s) in the full index of this instance, even if the current `view()` contains a subset of the full index.

Parameters:
    

  * **query** â 

the query, which can be any of the following:

    * an ID or iterable of IDs

    * a `num_dims` vector or `num_queries x num_dims` array of vectors

    * a prompt or iterable of prompts (if supported by the index)

  * **k** (_None_) â the number of matches to return. Some backends may support `None`, in which case all samples will be sorted

  * **reverse** (_False_) â whether to sort by least similarity (True) or greatest similarity (False). Some backends may not support least similarity

  * **aggregation** (_"mean"_) â the aggregation method to use when multiple queries are provided. The default is `"mean"`, which means that the query vectors are averaged prior to searching. Some backends may support additional options

  * **dist_field** (_None_) â the name of a float field in which to store the distance of each example to the specified query. The field is created if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property supports_prompts#
    

Whether this similarity index supports prompt queries.

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for `self.serialize()`



Returns:
    

a string representation of the object

use_view(_samples_ , _allow_missing =True_, _warn_missing =False_)#
    

Restricts the index to the provided view.

Subsequent calls to methods on this instance will only contain results from the specified view rather than the full index.

Use `clear_view()` to reset to the full index. Or, equivalently, use the context manager interface as demonstrated below to automatically reset the view when the context exits.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.brain as fob
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    results = fob.compute_similarity(dataset)
    print(results.index_size)  # 200
    
    view = dataset.take(50)
    
    with results.use_view(view):
        print(results.index_size)  # 50
    
        results.find_unique(10)
        print(results.unique_ids)
    
        plot = results.visualize_unique()
        plot.show()
    

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **allow_missing** (_True_) â whether to allow the provided collection to contain data points that this index does not contain (True) or whether to raise an error in this case (False)

  * **warn_missing** (_False_) â whether to log a warning if the provided collection contains data points that this index does not contain



Returns:
    

self

values(_path_or_expr_)#
    

Extracts a flat list of values from the given field or expression corresponding to the current `view()`.

This method always returns values in the same order as `current_sample_ids()` and `current_label_ids()`.

Parameters:
    

**path_or_expr** â 

the values to extract, which can be:

  * the name of a sample field or `embedded.field.name` from which to extract numeric or string values

  * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")




Returns:
    

a list of values

property view#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") against which results are currently being generated.

If `use_view()` has been called, this view may be different than the collection on which the full index was generated.

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for `self.serialize()`




cleanup()#
    

Deletes the similarity index from the backend.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
