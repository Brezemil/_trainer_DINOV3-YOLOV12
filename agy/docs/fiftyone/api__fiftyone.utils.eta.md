---
source_url: https://docs.voxel51.com/api/fiftyone.utils.eta.html
---

# fiftyone.utils.eta#

Utilities for interfacing with the [ETA library](https://github.com/voxel51/eta).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ETAModelConfig`(d) | Meta-config class that encapsulates the configuration of an eta.core.learning.Model that is to be run via the `ETAModel` wrapper.  
---|---  
`ETAModel`(config[,Â _model]) | Wrapper for running an `eta.core.learning.Model` model.  
  
**Functions:**

`from_image_labels`(image_labels_or_path[,Â ...]) | Loads the `eta.core.image.ImageLabels` or `eta.core.frames.FrameLabels` into a dictionary of labels.  
---|---  
`to_image_labels`(labels[,Â warn_unsupported]) | Converts the image label(s) to `eta.core.image.ImageLabels` format.  
`from_video_labels`(video_labels_or_path[,Â ...]) | Loads the `eta.core.video.VideoLabels` into a frame labels dictionary.  
`to_video_labels`([label,Â frames,Â support,Â ...]) | Converts the given labels to `eta.core.video.VideoLabels` format.  
`to_attribute`(classification[,Â name]) | Returns an `eta.core.data.Attribute` representation of the [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").  
`from_attribute`(attr) | Creates a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") from an `eta.core.data.Attribute`.  
`from_attributes`(attrs[,Â skip_non_categorical]) | Creates a [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") from a list of attributes.  
`to_detected_object`(detection[,Â name,Â ...]) | Returns an `eta.core.objects.DetectedObject` representation of the given [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
`from_detected_object`(dobj) | Creates a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") from an `eta.core.objects.DetectedObject`.  
`from_detected_objects`(objects) | Creates a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") from an `eta.core.objects.DetectedObjectContainer`.  
`to_polyline`(polyline[,Â name,Â extra_attrs]) | Returns an `eta.core.polylines.Polyline` representation of the given [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`from_polyline`(polyline) | Creates a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") from an `eta.core.polylines.Polyline`.  
`from_polylines`(polylines) | Creates a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") from an `eta.core.polylines.PolylineContainer`.  
`to_keypoints`(keypoint[,Â name,Â extra_attrs]) | Returns an `eta.core.keypoints.Keypoints` representation of the given [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").  
`from_keypoint`(keypoints) | Creates a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") from an `eta.core.keypoints.Keypoints`.  
`from_keypoints`(keypoints) | Creates a [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") from an `eta.core.keypoints.KeypointsContainer`.  
`to_video_event`(temporal_detection[,Â name,Â ...]) | Returns an `eta.core.events.VideoEvent` representation of the given [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection").  
`from_video_event`(video_event) | Creates a [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") from an `eta.core.events.VideoEvent`.  
`from_video_events`(video_events) | Creates a [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") from an `eta.core.events.VideoEventContainer`.  
  
class fiftyone.utils.eta.ETAModelConfig(_d_)#
    

Bases: [`ModelConfig`](api__fiftyone.core.models.md#fiftyone.core.models.ModelConfig "fiftyone.core.models.ModelConfig")

Meta-config class that encapsulates the configuration of an eta.core.learning.Model that is to be run via the `ETAModel` wrapper.

Example:
    
    
    import fiftyone.core.models as fom
    
    model = fom.load_model({
        "type": "fiftyone.utils.eta.ETAModel",
        "config": {
            "type": "eta.detectors.YOLODetector",
            "config": {
                "model_name": "yolo-v2-coco"
            }
        }
    })
    

Parameters:
    

  * **type** â the fully-qualified class name of the [`fiftyone.core.models.Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") subclass, which must be `ETAModel` or a subclass of it

  * **config** â a dict containing the `eta.core.learning.ModelConfig` for the ETA model




**Attributes:**

`confidence_thresh` | The confidence threshold of the underlying `eta.core.model.Model`.  
---|---  
  
**Methods:**

`attributes`() | Returns a list of class attributes to be serialized.  
---|---  
`build`() | Factory method that builds the Model instance from the config specified by this class.  
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
  
property confidence_thresh#
    

The confidence threshold of the underlying `eta.core.model.Model`.

Note that this may not be defined for some models.

attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

build()#
    

Factory method that builds the Model instance from the config specified by this class.

Returns:
    

a Model instance

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




class fiftyone.utils.eta.ETAModel(_config_ , __model =None_)#
    

Bases: [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model"), [`EmbeddingsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin "fiftyone.core.models.EmbeddingsMixin"), [`LogitsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.LogitsMixin "fiftyone.core.models.LogitsMixin")

Wrapper for running an `eta.core.learning.Model` model.

Parameters:
    

**config** â an `ETAModelConfig`

**Attributes:**

`media_type` | The media type processed by the model.  
---|---  
`ragged_batches` | True/False whether `transforms()` may return tensors of different sizes.  
`transforms` | The preprocessing function that will/must be applied to each input before prediction, or `None` if no preprocessing is performed.  
`preprocess` | Whether to apply `transforms()` during inference (True) or to assume that they have already been applied (False).  
`has_logits` | Whether this model can generate logits for its predictions.  
`has_embeddings` | Whether this model can generate embeddings.  
`can_embed_prompts` | Whether this model can generate prompt embeddings.  
`store_logits` | Whether the model should store logits in its predictions.  
  
**Methods:**

`get_embeddings`() | Returns the embeddings generated by the last forward pass of the model.  
---|---  
`embed`(arg) | Generates an embedding for the given data.  
`embed_all`(args) | Generates embeddings for the given iterable of data.  
`predict`(arg) | Performs prediction on the given data.  
`predict_all`(args) | Performs prediction on the given iterable of data.  
`from_eta_model`(model) | Builds an `ETAModel` for running the provided `eta.core.learning.Model` instance.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
  
property media_type#
    

The media type processed by the model.

Supported values are âimageâ and âvideoâ.

property ragged_batches#
    

True/False whether `transforms()` may return tensors of different sizes. If True, then passing ragged lists of data to `predict_all()` is not allowed.

property transforms#
    

The preprocessing function that will/must be applied to each input before prediction, or `None` if no preprocessing is performed.

property preprocess#
    

Whether to apply `transforms()` during inference (True) or to assume that they have already been applied (False).

property has_logits#
    

Whether this model can generate logits for its predictions.

This method returns `False` by default. Models that can generate logits should override this via implementing the `LogitsMixin` interface.

property has_embeddings#
    

Whether this model can generate embeddings.

This method returns `False` by default. Models that can generate embeddings should override this via implementing the `EmbeddingsMixin` interface.

get_embeddings()#
    

Returns the embeddings generated by the last forward pass of the model.

By convention, this method should always return an array whose first axis represents batch size (which will always be 1 when `predict()` was last used).

Returns:
    

a numpy array containing the embedding(s)

embed(_arg_)#
    

Generates an embedding for the given data.

Subclasses can override this method to increase efficiency, but, by default, this method simply calls `predict()` and then returns `get_embeddings()`.

Parameters:
    

**arg** â the data. See `predict()` for details

Returns:
    

a numpy array containing the embedding

embed_all(_args_)#
    

Generates embeddings for the given iterable of data.

Subclasses can override this method to increase efficiency, but, by default, this method simply iterates over the data and applies `embed()` to each.

Parameters:
    

**args** â an iterable of data. See `predict_all()` for details

Returns:
    

a numpy array containing the embeddings stacked along axis 0

predict(_arg_)#
    

Performs prediction on the given data.

Image models should support, at minimum, processing `arg` values that are uint8 numpy arrays (HWC).

Video models should support, at minimum, processing `arg` values that are `eta.core.video.VideoReader` instances.

Parameters:
    

**arg** â the data

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or dict of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

predict_all(_args_)#
    

Performs prediction on the given iterable of data.

Image models should support, at minimum, processing `args` values that are either lists of uint8 numpy arrays (HWC) or numpy array tensors (NHWC).

Video models should support, at minimum, processing `args` values that are lists of `eta.core.video.VideoReader` instances.

Subclasses can override this method to increase efficiency, but, by default, this method simply iterates over the data and applies `predict()` to each.

Parameters:
    

**args** â an iterable of data

Returns:
    

a list of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances or a list of dicts of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

classmethod from_eta_model(_model_)#
    

Builds an `ETAModel` for running the provided `eta.core.learning.Model` instance.

Parameters:
    

**model** â an `eta.core.learning.Model` instance

Returns:
    

an `ETAModel`

property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

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

property store_logits#
    

Whether the model should store logits in its predictions.

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

fiftyone.utils.eta.from_image_labels(_image_labels_or_path_ , _prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Loads the `eta.core.image.ImageLabels` or `eta.core.frames.FrameLabels` into a dictionary of labels.

Provide `labels_dict` if you want to customize which components of the labels are expanded. Otherwise, all labels are expanded as explained below.

If `multilabel` is False, frame attributes will be stored in separate `Classification` fields with names `prefix + attr.name`.

If `multilabel` if True, all frame attributes will be stored in a `Classifications` field called `prefix + "attributes"`.

Objects are expanded into fields with names `prefix + obj.name`, or `prefix + "detections"` for objects that do not have their `name` field populated.

Polylines are expanded into fields with names `prefix + polyline.name`, or `prefix + "polylines"` for polylines that do not have their `name` field populated.

Keypoints are expanded into fields with names `prefix + keypoints.name`, or `prefix + "keypoints"` for keypoints that do not have their `name` field populated.

Segmentation masks are expanded into a field with name `prefix + "mask"`.

Parameters:
    

  * **image_labels_or_path** â can be a `eta.core.image.ImageLabels` instance, a `eta.core.frames.FrameLabels` instance, a serialized dict representation of either, or the path to either on disk

  * **prefix** (_None_) â a string prefix to prepend to each field name in the output dict

  * **labels_dict** (_None_) â a dictionary mapping names of labels to keys to assign them in the output dictionary

  * **multilabel** (_False_) â whether to store attributes in a single `Classifications` instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)



Returns:
    

a dict mapping names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

fiftyone.utils.eta.to_image_labels(_labels_ , _warn_unsupported =True_)#
    

Converts the image label(s) to `eta.core.image.ImageLabels` format.

Parameters:
    

  * **labels** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or a dict mapping names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **warn_unsupported** (_True_) â whether to issue warnings if unsupported label values are encountered



Returns:
    

an `eta.core.image.ImageLabels` instance

fiftyone.utils.eta.from_video_labels(_video_labels_or_path_ , _prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Loads the `eta.core.video.VideoLabels` into a frame labels dictionary.

Parameters:
    

  * **video_labels_or_path** â can be a `eta.core.video.VideoLabels` instance, a serialized dict representation of one, or the path to one on disk

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded sample/frame label dictionaries

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the sample labels to field names into which to expand them. By default, all sample labels are loaded

  * **frame_labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the frame labels to field names into which to expand them. By default, all frame labels are loaded

  * **multilabel** (_False_) â whether to store attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)



Returns:
    

a tuple of

  * **label** : a dict mapping sample field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **frames** : a dict mapping frame numbers to dicts that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances




fiftyone.utils.eta.to_video_labels(_label =None_, _frames =None_, _support =None_, _warn_unsupported =True_)#
    

Converts the given labels to `eta.core.video.VideoLabels` format.

Parameters:
    

  * **label** (_None_) â video-level labels provided as a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or dict mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **frames** (_None_) â frame-level labels provided as a dict mapping frame numbers to dicts mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **support** (_None_) â an optional `[first, last]` support to store on the returned labels

  * **warn_unsupported** (_True_) â whether to issue warnings if unsupported label values are encountered



Returns:
    

a `eta.core.video.VideoLabels`

fiftyone.utils.eta.to_attribute(_classification_ , _name =None_)#
    

Returns an `eta.core.data.Attribute` representation of the [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").

Parameters:
    

  * **classification** â a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

  * **name** (_None_) â the name of the label field



Returns:
    

a `eta.core.data.CategoricalAttribute`

fiftyone.utils.eta.from_attribute(_attr_)#
    

Creates a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") from an `eta.core.data.Attribute`.

The attribute value is cast to a string, if necessary.

Parameters:
    

**attr** â an `eta.core.data.Attribute`

Returns:
    

a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

fiftyone.utils.eta.from_attributes(_attrs_ , _skip_non_categorical =False_)#
    

Creates a [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") from a list of attributes.

Parameters:
    

  * **attrs** â an iterable of `eta.core.data.Attribute` instances

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast all attribute values to strings (False)



Returns:
    

a [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

fiftyone.utils.eta.to_detected_object(_detection_ , _name =None_, _extra_attrs =True_)#
    

Returns an `eta.core.objects.DetectedObject` representation of the given [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Parameters:
    

  * **detection** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **name** (_None_) â the name of the label field

  * **extra_attrs** (_True_) â whether to include custom attributes in the conversion



Returns:
    

an `eta.core.objects.DetectedObject`

fiftyone.utils.eta.from_detected_object(_dobj_)#
    

Creates a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") from an `eta.core.objects.DetectedObject`.

Parameters:
    

**dobj** â a `eta.core.objects.DetectedObject`

Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

fiftyone.utils.eta.from_detected_objects(_objects_)#
    

Creates a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") from an `eta.core.objects.DetectedObjectContainer`.

Parameters:
    

**objects** â a `eta.core.objects.DetectedObjectContainer`

Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

fiftyone.utils.eta.to_polyline(_polyline_ , _name =None_, _extra_attrs =True_)#
    

Returns an `eta.core.polylines.Polyline` representation of the given [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

Parameters:
    

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **name** (_None_) â the name of the label field

  * **extra_attrs** (_True_) â whether to include custom attributes in the conversion



Returns:
    

an `eta.core.polylines.Polyline`

fiftyone.utils.eta.from_polyline(_polyline_)#
    

Creates a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") from an `eta.core.polylines.Polyline`.

Parameters:
    

**polyline** â an `eta.core.polylines.Polyline`

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

fiftyone.utils.eta.from_polylines(_polylines_)#
    

Creates a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") from an `eta.core.polylines.PolylineContainer`.

Parameters:
    

**polylines** â an `eta.core.polylines.PolylineContainer`

Returns:
    

a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

fiftyone.utils.eta.to_keypoints(_keypoint_ , _name =None_, _extra_attrs =True_)#
    

Returns an `eta.core.keypoints.Keypoints` representation of the given [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").

Parameters:
    

  * **keypoint** â a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

  * **name** (_None_) â the name of the label field

  * **extra_attrs** (_True_) â whether to include custom attributes in the conversion



Returns:
    

an `eta.core.keypoints.Keypoints`

fiftyone.utils.eta.from_keypoint(_keypoints_)#
    

Creates a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") from an `eta.core.keypoints.Keypoints`.

Parameters:
    

**keypoints** â an `eta.core.keypoints.Keypoints`

Returns:
    

a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

fiftyone.utils.eta.from_keypoints(_keypoints_)#
    

Creates a [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") from an `eta.core.keypoints.KeypointsContainer`.

Parameters:
    

**keypoints** â an `eta.core.keypoints.KeypointsContainer`

Returns:
    

a [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

fiftyone.utils.eta.to_video_event(_temporal_detection_ , _name =None_, _extra_attrs =True_)#
    

Returns an `eta.core.events.VideoEvent` representation of the given [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection").

Parameters:
    

  * **temporal_detection** â a [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection")

  * **name** (_None_) â the name of the label field

  * **extra_attrs** (_True_) â whether to include custom attributes in the conversion



Returns:
    

an `eta.core.events.VideoEvent`

fiftyone.utils.eta.from_video_event(_video_event_)#
    

Creates a [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") from an `eta.core.events.VideoEvent`.

Parameters:
    

**video_event** â an `eta.core.events.VideoEvent`

Returns:
    

a [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection")

fiftyone.utils.eta.from_video_events(_video_events_)#
    

Creates a [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections") from an `eta.core.events.VideoEventContainer`.

Parameters:
    

**video_events** â an `eta.core.events.VideoEventContainer`

Returns:
    

a [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections")

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
