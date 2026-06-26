---
source_url: https://docs.voxel51.com/api/fiftyone.utils.sam.html
---

# fiftyone.utils.sam#

[Segment Anything](https://segment-anything.com) wrapper for the FiftyOne Model Zoo.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SegmentAnythingModelConfig`(cfg_dict) | Configuration for running a `SegmentAnythingModel`.  
---|---  
`SAMPromptMode`(value) | Enumeration of supported prompt modes for SAM.  
`SegmentAnythingImageGetItem`([field_mapping,Â ...]) | A `GetItem` that loads images, bounding boxes and/or keypoints to feed to `SegmentAnythingModel` instances.  
`SegmentAnythingImageGetItemForVideo`([...]) | Workaround for applying image model to video reader frames.  
`SAMSegmenterOutputProcessor`([classes,Â ...]) | Converts SAM model outputs to FiftyOne format.  
`SegmentAnythingModel`(config) | Wrapper for running [Segment Anything](https://segment-anything.com) inference.  
  
**Functions:**

`preprocess_detections_to_sam`(detections,Â ...) | Pre-processes boxes from [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections").  
---|---  
`preprocess_keypoints_to_sam`(keypoints,Â ...) | Pre-processes points from [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints").  
  
class fiftyone.utils.sam.SegmentAnythingModelConfig(_cfg_dict_)#
    

Bases: [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig"), [`HasZooModel`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.HasZooModel "fiftyone.zoo.models.HasZooModel")

Configuration for running a `SegmentAnythingModel`.

See [`fiftyone.utils.torch.TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") for additional arguments.

Parameters:
    

  * **auto_kwargs** (_None_) â a dictionary of keyword arguments to pass to `segment_anything.SamAutomaticMaskGenerator(model, **auto_kwargs)`

  * **points_mask_index** (_None_) â an optional mask index to use for each keypoint output

  * **get_item_cls** (_None_) â a string like `"fiftyone.utils.sam.SegmentAnythingImageGetItem"` specifying the `GetItem` to use for SAM

  * **get_item_args** (_None_) â a dictionary of arguments for `get_item_cls(field_mapping=field_mapping, **kwargs)`




**Methods:**

`attributes`() | Returns a list of class attributes to be serialized.  
---|---  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`download_model_if_necessary`() | Downloads the published model specified by the config, if necessary.  
`from_dict`(d) | Constructs a Config object from a JSON dictionary.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`init`(d) | Initializes the published model config.  
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

download_model_if_necessary()#
    

Downloads the published model specified by the config, if necessary.

After this method is called, the model_path attribute will always contain the path to the model on disk.

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

init(_d_)#
    

Initializes the published model config.

This method should be called by ModelConfig.__init__(), and it performs the following tasks:

  * Parses the model_name and model_path parameters

  * Populates any default parameters in the provided ModelConfig dict




Parameters:
    

**d** â a ModelConfig dict

Returns:
    

a ModelConfig dict with any default parameters populated

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




class fiftyone.utils.sam.SAMPromptMode(_value_)#
    

Bases: `Enum`

Enumeration of supported prompt modes for SAM.

**Attributes:**

`auto` |   
---|---  
`box_only` |   
`point_only` |   
`box_point_combo` |   
  
auto = 1#
    

box_only = 2#
    

point_only = 3#
    

box_point_combo = 4#
    

class fiftyone.utils.sam.SegmentAnythingImageGetItem(_field_mapping =None_, _transform =None_, _use_numpy =False_, _box_transform =None_, _point_transform =None_, _** kwargs_)#
    

Bases: [`GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem")

A `GetItem` that loads images, bounding boxes and/or keypoints to feed to `SegmentAnythingModel` instances.

Parameters:
    

  * **field_mapping** (_None_) â the user-supplied dict mapping keys in `required_keys` to field names of their dataset that contain the required values

  * **transform** (_None_) â SAM specific image transform function to apply

  * **use_numpy** (_False_) â whether to use numpy arrays rather than PIL images and Torch tensors when loading data

  * **box_transform** (_None_) â SAM specific box transform function to apply

  * **point_transform** (_None_) â SAM specific point transform function to apply




**Attributes:**

`required_keys` | The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.  
---|---  
`field_mapping` | A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.  
  
property required_keys#
    

The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.

property field_mapping#
    

A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.

class fiftyone.utils.sam.SegmentAnythingImageGetItemForVideo(_field_mapping =None_, _transform =None_, _use_numpy =False_, _box_transform =None_, _point_transform =None_, _** kwargs_)#
    

Bases: `SegmentAnythingImageGetItem`

Workaround for applying image model to video reader frames.

Frames are not stored on disk and therefore cannot be loaded.

**Attributes:**

`required_keys` | The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.  
---|---  
`field_mapping` | A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.  
  
property required_keys#
    

The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.

property field_mapping#
    

A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.

fiftyone.utils.sam.preprocess_detections_to_sam(_detections_ , _img_hw_ , _box_transform_ , _** transform_kwargs_)#
    

Pre-processes boxes from [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections").

Parameters:
    

  * **detections** â a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance

  * **img_hw** â original image height and width

  * **box_transform** â SAM specific box transform function to apply



Returns:
    

a torch tensor of boxes for SAM model prompts a numpy array of boxes in XYXY pixels in original image space a list class labels for the boxes a list of positive/negative labels for the boxes

fiftyone.utils.sam.preprocess_keypoints_to_sam(_keypoints_ , _img_hw_ , _point_transform_ , _** transform_kwargs_)#
    

Pre-processes points from [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints").

Parameters:
    

  * **keypoints** â a [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") instance

  * **img_hw** â original image height and width

  * **point_transform** â SAM specific point transform function to apply



Returns:
    

a list of torch tensor of points in XYXY pixels for SAM model prompts a list of torch tensor of positive and negative labels for each point a list of class labels for each set of points

class fiftyone.utils.sam.SAMSegmenterOutputProcessor(_classes =None_, _mask_thresh =0.5_)#
    

Bases: [`OutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.OutputProcessor "fiftyone.utils.torch.OutputProcessor")

Converts SAM model outputs to FiftyOne format.

Parameters:
    

  * **classes** (_None_) â the list of class labels for the model. Not used in SAM output processor.

  * **mask_thresh** (_0.5_) â Threshold for converting float masks to boolean masks




class fiftyone.utils.sam.SegmentAnythingModel(_config_)#
    

Bases: [`TorchImageModelWithPrompts`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelWithPrompts "fiftyone.utils.torch.TorchImageModelWithPrompts")

Wrapper for running [Segment Anything](https://segment-anything.com) inference.

Box prompt example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset(
        "quickstart", max_samples=25, shuffle=True, seed=51
    )
    
    model = foz.load_zoo_model("segment-anything-vitb-torch")
    
    # Prompt with boxes
    dataset.apply_model(
        model,
        label_field="segmentations",
        box_prompt_field="ground_truth",
    )
    
    session = fo.launch_app(dataset)
    

Keypoint prompt example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset(
        "coco-2017",
        split="validation",
        label_types="detections",
        classes=["person"],
        max_samples=25,
        only_matching=True,
    )
    
    # Generate some keypoints
    model = foz.load_zoo_model("keypoint-rcnn-resnet50-fpn-coco-torch")
    dataset.default_skeleton = model.skeleton
    dataset.apply_model(model, label_field="gt")
    
    model = foz.load_zoo_model("segment-anything-vitb-torch")
    
    # Prompt with keypoints
    dataset.apply_model(
        model,
        label_field="segmentations",
        point_prompt_field="gt_keypoints",
    )
    
    session = fo.launch_app(dataset)
    

Automatic segmentation example:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset(
        "quickstart", max_samples=5, shuffle=True, seed=51
    )
    
    model = foz.load_zoo_model("segment-anything-vitb-torch")
    
    # Automatic segmentation
    dataset.apply_model(model, label_field="auto")
    
    session = fo.launch_app(dataset)
    

Parameters:
    

**config** â a `SegmentAnythingModelConfig`

**Methods:**

`predict_interactive`([sample,Â boxes,Â points,Â ...]) | Generates predictions in interactive mode.  
---|---  
`predict`(img[,Â sample]) | Performs prediction a single image.  
`predict_all`(imgs[,Â samples]) | Performs prediction on multiple images.  
`build_get_item`([field_mapping]) | Builds a `SegmentAnythingImageGetItem` for loading model input from samples.  
`collate_fn`(batch) | Collates a batch of inputs where each input is generated from `SegmentAnythingImageGetItem`.  
`embed`(arg) | Generates an embedding for the given data.  
`embed_all`(args) | Generates embeddings for the given iterable of data.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_embeddings`() | Returns the embeddings generated by the last forward pass of the model.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
  
**Attributes:**

`ragged_batches` | Whether `transforms()` may return tensors of different sizes.  
---|---  
`has_collate_fn` | Whether this model has a custom collate function.  
`can_embed_prompts` | Whether this model can generate prompt embeddings.  
`classes` | The list of class labels for the model, if known.  
`device` | The `torch:torch.torch.device` that the model is using.  
`has_embeddings` | Whether this model has embeddings.  
`has_logits` | Whether this instance can generate logits.  
`mask_targets` | The mask targets for the model, if any.  
`media_type` | The media type processed by the model.  
`num_classes` | The number of classes for the model, if known.  
`preprocess` | Whether to apply preprocessing transforms for inference, if any.  
`required_keys` | The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.  
`skeleton` | The keypoint skeleton for the model, if any.  
`store_logits` | Whether the model should store logits in its predictions.  
`transforms` | A `torchvision.transforms` function that will be applied to each input before prediction, if any.  
`using_gpu` | Whether the model is using GPU.  
`using_half_precision` | Whether the model is using half precision.  
  
predict_interactive(_sample =None_, _boxes =None_, _points =None_, _point_labels =None_, _prompt_classes =None_, _boxes_xyxy =None_)#
    

Generates predictions in interactive mode. Image embedding is cached.

Parameters:
    

  * **sample** (_None_) â a FiftyOne Sample with image media

  * **boxes** (_None_) â a tensor of Bx4 pre-processed SAM transformed boxes in XYXY pixels

  * **points** (_None_) â a tensor of BxNx2 or a list of B tensors with pre-processed points in XY pixels

  * **point_labels** (_None_) â a BxN tensor or a list of B tensors of labels for the point prompts

  * **prompt_classes** (_None_) â a list of B class labels

  * **boxes_xyxy** â a list of Bx4 boxes in XYXY pixels in original image space



Returns:
    

[`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") or dict containing the âmasksâ, âiou_predictionsâ, âlow_res_logitsâ from SAM model output.

predict(_img_ , _sample =None_)#
    

Performs prediction a single image.

Parameters:
    

  * **img** â a dictionary containing image, original size, and prompts. See `fiftyone.utils.sam.SegmentAnythingGetItem` for details.

  * **sample** (_None_) â sample is no longer used. Available for backward compatibility.



Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance or a dict containing the âmasksâ, âiou_predictionsâ, âlow_res_logitsâ from SAM model output.

predict_all(_imgs_ , _samples =None_)#
    

Performs prediction on multiple images.

To generate imgs dictionary and run prediction:

> field_mapping = {âbox_prompt_fieldâ: âground-truthâ} get_item = model.build_get_item(field_mapping=field_mapping) model_inputs = fout.get_model_inputs_from_get_item(samples, get_item) outputs = model.predict_all(model_inputs)

Parameters:
    

  * **imgs** â a list of dictionary or a dictionary containing images, original sizes, and prompts. See `fiftyone.utils.sam.SegmentAnythingGetItem` for details.

  * **samples** (_None_) â samples is no longer used. Available for backward compatibility.



Returns:
    

a list of [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instances or a list of dict containing the âmasksâ, âiou_predictionsâ, âlow_res_logitsâ from SAM model output.

build_get_item(_field_mapping =None_)#
    

Builds a `SegmentAnythingImageGetItem` for loading model input from samples.

Parameters:
    

**field_mapping** (_None_) â a dict mapping required keys to sample fields

Returns:
    

a `SegmentAnythingImageGetItem` instance

property ragged_batches#
    

Whether `transforms()` may return tensors of different sizes. If True, then passing ragged lists of images to `predict_all()` may not be not allowed.

property has_collate_fn#
    

Whether this model has a custom collate function.

Set this to `True` if you want `collate_fn()` to be used during inference.

static collate_fn(_batch_)#
    

Collates a batch of inputs where each input is generated from `SegmentAnythingImageGetItem`.

Parameters:
    

**batch** â a list of dict containing model input from `SegmentAnythingImageGetItem`

Returns:
    

âimageâ: a list of torch tensor of (1 x C X H X W) shape or HWC numpy arrays âboxesâ: a list of B X 4 boxes for SAM model input âboxes_xyxy: a list of B x 4 boxes in XYXY pixels in original image space âboxes_labelsâ: a list of B x N positive / negative labels for boxes âpoint_coordsâ: a list of B X N x 2 point coordinates, padded as needed âpoint_labelsâ: a list of B X N point positive/negative labels, padded as needed âprompt_typeâ: name of prompt type for the batch âclassesâ: a list of classes for each prompt

Return type:
    

a collated dictionary of model input for the batch. Expected keys are

property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

property classes#
    

The list of class labels for the model, if known.

property device#
    

The `torch:torch.torch.device` that the model is using.

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

get_embeddings()#
    

Returns the embeddings generated by the last forward pass of the model.

By convention, this method should always return an array whose first axis represents batch size (which will always be 1 when `predict()` was last used).

Returns:
    

a numpy array containing the embedding(s)

property has_embeddings#
    

Whether this model has embeddings.

property has_logits#
    

Whether this instance can generate logits.

property mask_targets#
    

The mask targets for the model, if any.

property media_type#
    

The media type processed by the model.

property num_classes#
    

The number of classes for the model, if known.

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

property preprocess#
    

Whether to apply preprocessing transforms for inference, if any.

property required_keys#
    

The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.

property skeleton#
    

The keypoint skeleton for the model, if any.

property store_logits#
    

Whether the model should store logits in its predictions.

property transforms#
    

A `torchvision.transforms` function that will be applied to each input before prediction, if any.

property using_gpu#
    

Whether the model is using GPU.

property using_half_precision#
    

Whether the model is using half precision.

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
