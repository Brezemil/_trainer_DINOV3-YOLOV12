---
source_url: https://docs.voxel51.com/api/fiftyone.utils.eval.activitynet.html
---

# fiftyone.utils.eval.activitynet#

ActivityNet-style temporal detection evaluation.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ActivityNetEvaluationConfig`(pred_field,Â gt_field) | ActivityNet-style evaluation config.  
---|---  
`ActivityNetEvaluation`(config) | ActivityNet-style evaluation.  
`ActivityNetDetectionResults`(samples,Â config,Â ...) | Class that stores the results of a ActivityNet detection evaluation.  
  
class fiftyone.utils.eval.activitynet.ActivityNetEvaluationConfig(_pred_field_ , _gt_field_ , _iou =None_, _classwise =None_, _compute_mAP =False_, _iou_threshs =None_, _custom_metrics =None_, _** kwargs_)#
    

Bases: [`DetectionEvaluationConfig`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluationConfig "fiftyone.utils.eval.detection.DetectionEvaluationConfig")

ActivityNet-style evaluation config.

Parameters:
    

  * **pred_field** â the name of the field containing the predicted [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") instances

  * **gt_field** â the name of the field containing the ground truth [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") instances

  * **iou** (_None_) â the IoU threshold to use to determine matches

  * **classwise** (_None_) â whether to only match segments with the same class label (True) or allow matches between classes (False)

  * **compute_mAP** (_False_) â whether to perform the necessary computations so that mAP and PR curves can be generated

  * **iou_threshs** (_None_) â a list of IoU thresholds to use when computing mAP and PR curves. Only applicable when `compute_mAP` is True

  * **custom_metrics** (_None_) â an optional list of custom metrics to compute or dict mapping metric names to kwargs dicts




**Attributes:**

`method` | The name of the method.  
---|---  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`requires_additional_fields` | Whether fields besides `pred_field` and `gt_field` are required in order to perform evaluation.  
`run_cls` | The `BaseRun` class associated with this config.  
`type` | The type of run.  
  
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

property requires_additional_fields#
    

Whether fields besides `pred_field` and `gt_field` are required in order to perform evaluation.

If True then the entire samples will be loaded rather than using [`select_fields()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_fields "fiftyone.core.collections.SampleCollection.select_fields") to optimize.

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

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.eval.activitynet.ActivityNetEvaluation(_config_)#
    

Bases: [`DetectionEvaluation`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionEvaluation "fiftyone.utils.eval.detection.DetectionEvaluation")

ActivityNet-style evaluation.

Parameters:
    

**config** â a `ActivityNetEvaluationConfig`

**Methods:**

`evaluate`(sample[,Â eval_key]) | Performs ActivityNet-style evaluation on the given video.  
---|---  
`generate_results`(samples,Â matches[,Â ...]) | Generates aggregate evaluation results for the samples.  
`add_fields_to_sidebar_group`(samples,Â eval_key) |   
`cleanup`(samples,Â eval_key) | Cleans up the results of the run with the given key from the collection.  
`cleanup_custom_metrics`(samples,Â eval_key[,Â ...]) |   
`compute_custom_metrics`(samples,Â eval_key,Â ...) |   
`delete_run`(samples,Â key[,Â cleanup]) | Deletes the results associated with the given run key from the collection.  
`delete_runs`(samples[,Â cleanup]) | Deletes all runs from the collection.  
`ensure_requirements`() | Ensures that any necessary packages to execute this run are installed.  
`ensure_usage_requirements`() | Ensures that any necessary packages to use existing results for this run are installed.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_custom_metric_fields`(samples,Â eval_key) |   
`get_fields`(samples,Â eval_key[,Â ...]) | Gets the fields that were involved in the given run.  
`get_run_info`(samples,Â key) | Gets the `BaseRunInfo` for the given key on the collection.  
`has_cached_run_results`(samples,Â key) | Determines whether `BaseRunResults` for the given key are cached on the collection.  
`list_runs`(samples[,Â type,Â method]) | Returns the list of run keys on the given collection.  
`load_run_results`(samples,Â key[,Â cache,Â ...]) | Loads the `BaseRunResults` for the given key on the collection.  
`load_run_view`(samples,Â key[,Â select_fields]) | Loads the view on which the specified run was performed.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`register_run`(samples,Â key[,Â overwrite,Â cleanup]) | Registers a run of this method under the given key on the given collection.  
`register_samples`(samples,Â eval_key[,Â dynamic]) | Registers the collection on which evaluation will be performed.  
`rename`(samples,Â eval_key,Â new_eval_key) | Performs any necessary operations required to rename this run's key.  
`rename_custom_metrics`(samples,Â eval_key,Â ...) |   
`run_info_cls`() | The `BaseRunInfo` class associated with this class.  
`save_run_info`(samples,Â run_info[,Â ...]) | Saves the run information on the collection.  
`save_run_results`(samples,Â key,Â run_results) | Saves the run results on the collection.  
`update_run_config`(samples,Â key,Â config) | Updates the `BaseRunConfig` for the given run on the collection.  
`update_run_key`(samples,Â key,Â new_key) | Replaces the key for the given run with a new key.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
`validate_run`(samples,Â key[,Â overwrite]) | Validates that the collection can accept this run.  
  
evaluate(_sample_ , _eval_key =None_)#
    

Performs ActivityNet-style evaluation on the given video.

Predicted segments are matched to ground truth segments in descending order of confidence, with matches requiring a minimum IoU of `self.config.iou`.

The `self.config.classwise` parameter controls whether to only match segments with the same class label (True) or allow matches between classes (False).

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **eval_key** (_None_) â the evaluation key for this evaluation



Returns:
    

a list of matched `(gt_label, pred_label, iou, pred_confidence, gt_id, pred_id)` tuples

generate_results(_samples_ , _matches_ , _eval_key =None_, _classes =None_, _missing =None_, _progress =None_)#
    

Generates aggregate evaluation results for the samples.

If `self.config.compute_mAP` is True, this method performs ActivityNet-style evaluation as in `evaluate()` to generate precision and recall sweeps over the range of IoU thresholds in `self.config.iou_threshs`. In this case, an `ActivityNetDetectionResults` instance is returned that can compute mAP and PR curves.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **matches** â a list of `(gt_label, pred_label, iou, pred_confidence, gt_id, pred_id)` matches. Either label can be `None` to indicate an unmatched segment

  * **eval_key** (_None_) â the evaluation key for this evaluation

  * **classes** (_None_) â the list of possible classes. If not provided, the observed ground truth/predicted labels are used for results purposes

  * **missing** (_None_) â a missing label string. Any unmatched segments are given this label for results purposes

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a `DetectionResults`

add_fields_to_sidebar_group(_samples_ , _eval_key_ , _omit_fields =None_)#
    

cleanup(_samples_ , _eval_key_)#
    

Cleans up the results of the run with the given key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key




cleanup_custom_metrics(_samples_ , _eval_key_ , _metric_uris =None_)#
    

compute_custom_metrics(_samples_ , _eval_key_ , _results_ , _metric_uris =None_)#
    

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

get_custom_metric_fields(_samples_ , _eval_key_ , _metric_uris =None_)#
    

get_fields(_samples_ , _eval_key_ , _include_custom_metrics =True_)#
    

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




register_samples(_samples_ , _eval_key_ , _dynamic =True_)#
    

Registers the collection on which evaluation will be performed.

This method will be called before the first call to `evaluate()`. Subclasses can extend this method to perform any setup required for an evaluation run.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **eval_key** â the evaluation key for this evaluation

  * **dynamic** (_True_) â whether to declare the dynamic object-level attributes that are populated on the datasetâs schema




rename(_samples_ , _eval_key_ , _new_eval_key_)#
    

Performs any necessary operations required to rename this runâs key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **new_key** â a new run key




rename_custom_metrics(_samples_ , _eval_key_ , _new_eval_key_ , _metric_uris =None_)#
    

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

class fiftyone.utils.eval.activitynet.ActivityNetDetectionResults(_samples_ , _config_ , _eval_key_ , _matches_ , _precision_ , _recall_ , _classwise_AP_ , _iou_threshs_ , _classes_ , _thresholds =None_, _missing =None_, _custom_metrics =None_, _backend =None_)#
    

Bases: [`DetectionResults`](api__fiftyone.utils.eval.detection.md#fiftyone.utils.eval.detection.DetectionResults "fiftyone.utils.eval.detection.DetectionResults")

Class that stores the results of a ActivityNet detection evaluation.

Parameters:
    

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") used

  * **config** â the `ActivityNetEvaluationConfig` used

  * **eval_key** â the evaluation key

  * **matches** â a list of `(gt_label, pred_label, iou, pred_confidence, gt_id, pred_id)` matches. Either label can be `None` to indicate an unmatched segment

  * **precision** â an array of precision values of shape `num_iou_threshs x num_classes x num_recall`

  * **recall** â an array of recall values

  * **classwise_AP** â an array of average precision values of shape `num_iou_threshs x num_classes`

  * **iou_threshs** â an array of IoU thresholds

  * **classes** â the list of possible classes

  * **thresholds** (_None_) â an optional array of decision thresholds of shape `num_iou_threshs x num_classes x num_recall`

  * **missing** (_None_) â a missing label string. Any unmatched segments are given this label for evaluation purposes

  * **custom_metrics** (_None_) â an optional dict of custom metrics

  * **backend** (_None_) â a `ActivityNetEvaluation` backend




**Methods:**

`plot_pr_curves`([classes,Â iou_thresh,Â backend]) | Plots precision-recall (PR) curves for the results.  
---|---  
`mAP`([classes]) | Computes ActivityNet-style mean average precision (mAP) for the specified classes.  
`add_custom_metrics`(custom_metrics[,Â overwrite]) | Computes the given custom metrics and adds them to these results.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`clear_subset`() | Clears the subset set by `use_subset()`, if any.  
`confusion_matrix`([classes,Â include_other,Â ...]) | Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`metrics`([classes,Â average,Â beta]) | Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.  
`plot_confusion_matrix`([classes,Â ...]) | Plots a confusion matrix for the evaluation results.  
`print_metrics`([classes,Â average,Â beta,Â digits]) | Prints the metrics computed via `metrics()`.  
`print_report`([classes,Â digits]) | Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`report`([classes]) | Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_subset`(subset_def) | Restricts the evaluation results to the specified subset.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`has_subset` | Whether these results are currently restricted to a subset via `use_subset()`.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
plot_pr_curves(_classes =None_, _iou_thresh =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots precision-recall (PR) curves for the results.

Parameters:
    

  * **classes** (_None_) â a list of classes to generate curves for. By default, the top 3 AP classes will be plotted

  * **iou_thresh** (_None_) â an optional IoU threshold or list of IoU thresholds for which to plot curves. If multiple thresholds are provided, precision data is averaged across these thresholds. By default, precision data is averaged over all IoU thresholds. Refer to `iou_threshs` to see the available thresholds

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_pr_curves()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_pr_curves "fiftyone.core.plots.plotly.plot_pr_curves")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_pr_curves()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_pr_curves "fiftyone.core.plots.matplotlib.plot_pr_curves")



Returns:
    

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if you are working in a notebook context and the plotly backend is used

  * a plotly or matplotlib figure, otherwise




Return type:
    

one of the following

mAP(_classes =None_)#
    

Computes ActivityNet-style mean average precision (mAP) for the specified classes.

See [this page](https://github.com/activitynet/ActivityNet/tree/master/Evaluation) for more details about ActivityNet-style mAP.

Parameters:
    

**classes** (_None_) â a list of classes for which to compute mAP

Returns:
    

the mAP in `[0, 1]`

add_custom_metrics(_custom_metrics_ , _overwrite =True_)#
    

Computes the given custom metrics and adds them to these results.

Parameters:
    

  * **custom_metrics** â a list of custom metrics to compute or a dict mapping metric names to kwargs dicts

  * **overwrite** (_True_) â whether to recompute any custom metrics that have already been applied




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

clear_subset()#
    

Clears the subset set by `use_subset()`, if any.

Subsequent operations will be performed on the full results.

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

confusion_matrix(_classes =None_, _include_other =False_, _include_missing =False_)#
    

Generates a confusion matrix for the results via [`sklearn.metrics.confusion_matrix()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "\(in scikit-learn v1.9\)").

The rows of the confusion matrix represent ground truth and the columns represent predictions.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_False_) â whether to include an extra row/column at the end of the matrix for labels that do not appear in `classes`. Only applicable if `classes` are provided

  * **include_missing** (_False_) â whether to include a row/column at the end of the matrix for unmatched labels. Only applicable if `self.missing` does not already appear in `classes`. If both âotherâ and âmissingâ rows/columns are requested, this one is last



Returns:
    

a `num_classes x num_classes` confusion matrix

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

property has_subset#
    

Whether these results are currently restricted to a subset via `use_subset()`.

property key#
    

The run key for these results.

metrics(_classes =None_, _average ='micro'_, _beta =1.0_)#
    

Computes classification metrics for the results, including accuracy, precision, recall, and F-beta score.

See [`sklearn.metrics.precision_recall_fscore_support()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "\(in scikit-learn v1.9\)") for details.

Also includes any custom metrics from `custom_metrics`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use



Returns:
    

a dict

plot_confusion_matrix(_classes =None_, _include_other =None_, _include_missing =None_, _other_label ='(other)'_, _backend ='plotly'_, _** kwargs_)#
    

Plots a confusion matrix for the evaluation results.

If you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the confusion matrix

  * **include_other** (_None_) â 

whether to include a row/column for examples whose label is in `classes` but are matched to labels that do not appear in `classes`. Only applicable if `classes` are provided. The supported values are:

    * None (default): only include a row/column for other labels if there are any

    * True: do include a row/column for other labels

    * False: do not include a row/column for other labels

  * **include_missing** (_None_) â 

whether to include a row/column for missing ground truth/predictions in the confusion matrix. The supported values are:

    * None (default): only include a row/column for missing labels if there are any

    * True: do include a row/column for missing labels

    * False: do not include a row/column for missing labels

  * **other_label** (_"__(__other_ _)__"_) â the label to use for âotherâ predictions

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

  * a [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap"), if the plotly backend is used

  * a matplotlib figure, otherwise




Return type:
    

one of the following

print_metrics(_classes =None_, _average ='micro'_, _beta =1.0_, _digits =2_)#
    

Prints the metrics computed via `metrics()`.

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the calculations

  * **average** (_"micro"_) â the averaging strategy to use

  * **beta** (_1.0_) â the F-beta value to use

  * **digits** (_2_) â the number of digits of precision to print




print_report(_classes =None_, _digits =2_)#
    

Prints a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

  * **classes** (_None_) â an optional list of classes to include in the report

  * **digits** (_2_) â the number of digits of precision to print




report(_classes =None_)#
    

Generates a classification report for the results via [`sklearn.metrics.classification_report()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "\(in scikit-learn v1.9\)").

Parameters:
    

**classes** (_None_) â an optional list of classes to include in the report

Returns:
    

a dict

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

use_subset(_subset_def_)#
    

Restricts the evaluation results to the specified subset.

Subsequent calls to supported methods on this instance will only contain results from the specified subset rather than the full results.

Use `clear_subset()` to reset to the full results. Or, equivalently, use the context manager interface as demonstrated below to automatically reset the results when the context exits.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.random as four
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    four.random_split(dataset, {"sunny": 0.7, "cloudy": 0.2, "rainy": 0.1})
    
    results = dataset.evaluate_detections(
        "predictions",
        gt_field="ground_truth",
        eval_key="eval",
    )
    
    counts = dataset.count_values("ground_truth.detections.label")
    classes = sorted(counts, key=counts.get, reverse=True)[:5]
    
    # Full results
    results.print_report(classes=classes)
    
    # Sunny samples
    subset_def = dict(type="field", field="tags", value="sunny")
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    
    # Small objects
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    small_objects = bbox_area <= 0.05
    subset_def = dict(type="attribute", expr=small_objects)
    with results.use_subset(subset_def):
        results.print_report(classes=classes)
    

Parameters:
    

**subset_def** â 

the subset definition, which can be:

  * a dict or list of dicts defining the subset. See above for examples and see `get_subset_view()` for full syntax

  * a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") defining the subset




Returns:
    

self

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
