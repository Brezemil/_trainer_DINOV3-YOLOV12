---
source_url: https://docs.voxel51.com/api/fiftyone.utils.open_clip.html
---

# fiftyone.utils.open_clip#

CLIP model wrapper for the FiftyOne Model Zoo.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`TorchOpenClipModelConfig`(d) | Configuration for running a `TorchOpenClipModel`.  
---|---  
`TorchOpenClipModel`(config) | Torch implementation of CLIP from [mlfoundations/open_clip](https://github.com/mlfoundations/open_clip).  
  
class fiftyone.utils.open_clip.TorchOpenClipModelConfig(_d_)#
    

Bases: [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig"), [`HasZooModel`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.HasZooModel "fiftyone.zoo.models.HasZooModel")

Configuration for running a `TorchOpenClipModel`.

See [`fiftyone.utils.torch.TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") for additional arguments.

Parameters:
    

  * **text_prompt** â the text prompt to use, e.g., `"A photo of"`

  * **clip_model** (_"ViT-B-32"_) â the Open CLIP model to use

  * **pretrained** (_"openai"_) â the pretrained version to use

  * **classes** (_None_) â a list of custom classes for zero-shot prediction




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




class fiftyone.utils.open_clip.TorchOpenClipModel(_config_)#
    

Bases: [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel"), [`PromptMixin`](api__fiftyone.core.models.md#fiftyone.core.models.PromptMixin "fiftyone.core.models.PromptMixin")

Torch implementation of CLIP from [mlfoundations/open_clip](https://github.com/mlfoundations/open_clip).

Parameters:
    

**config** â a `TorchOpenClipModelConfig`

**Attributes:**

`can_embed_prompts` | Whether this model can generate prompt embeddings.  
---|---  
`classes` | The list of class labels for the model, if known.  
`device` | The `torch:torch.torch.device` that the model is using.  
`has_collate_fn` | Whether this model has a custom collate function.  
`has_embeddings` | Whether this model has embeddings.  
`has_logits` | Whether this instance can generate logits.  
`mask_targets` | The mask targets for the model, if any.  
`media_type` | The media type processed by the model.  
`num_classes` | The number of classes for the model, if known.  
`preprocess` | Whether to apply preprocessing transforms for inference, if any.  
`ragged_batches` | Whether `transforms()` may return tensors of different sizes.  
`required_keys` | The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.  
`skeleton` | The keypoint skeleton for the model, if any.  
`store_logits` | Whether the model should store logits in its predictions.  
`transforms` | A `torchvision.transforms` function that will be applied to each input before prediction, if any.  
`using_gpu` | Whether the model is using GPU.  
`using_half_precision` | Whether the model is using half precision.  
  
**Methods:**

`embed_prompt`(prompt) | Generates an embedding for the given text prompt.  
---|---  
`embed_prompts`(prompts) | Generates an embedding for the given text prompts.  
`build_get_item`([field_mapping]) | Builds the [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance that defines how the model's data should be loaded by data loaders.  
`collate_fn`(batch) | The collate function to use when creating dataloaders for this model.  
`embed`(arg) | Generates an embedding for the given data.  
`embed_all`(args) | Generates embeddings for the given iterable of data.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_embeddings`() | Returns the embeddings generated by the last forward pass of the model.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`predict`(img) | Performs prediction on the given image.  
`predict_all`(imgs) | Performs prediction on the given batch of images.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
  
property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

embed_prompt(_prompt_)#
    

Generates an embedding for the given text prompt.

Parameters:
    

**prompt** â a text string

Returns:
    

a numpy vector

embed_prompts(_prompts_)#
    

Generates an embedding for the given text prompts.

Parameters:
    

**prompts** â an iterable of text strings

Returns:
    

a `num_prompts x num_dims` array of prompt embeddings

build_get_item(_field_mapping =None_)#
    

Builds the [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance that defines how the modelâs data should be loaded by data loaders.

Parameters:
    

**field_mapping** (_None_) â a user-provided dict mapping required keys to dataset field names

Returns:
    

a [`fiftyone.utils.torch.GetItem`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.GetItem "fiftyone.utils.torch.GetItem") instance

property classes#
    

The list of class labels for the model, if known.

static collate_fn(_batch_)#
    

The collate function to use when creating dataloaders for this model.

In order to enable this functionality, the modelâs `has_collate_fn()` property must return `True`.

By default, this is the default collate function for [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)"), but subclasses can override this method as necessary.

Note that this function must be serializable so it is compatible with multiprocessing for dataloaders.

Parameters:
    

**batch** â a list of items to collate

Returns:
    

the collated batch, which will be fed directly to the model

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

property has_collate_fn#
    

Whether this model has a custom collate function.

Set this to `True` if you want `collate_fn()` to be used during inference.

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

predict(_img_)#
    

Performs prediction on the given image.

Parameters:
    

**img** â 

the image to process, which can be any of the following:

  * A PIL image

  * A uint8 numpy array (HWC)

  * A Torch tensor (CHW)




Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or dict of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

predict_all(_imgs_)#
    

Performs prediction on the given batch of images.

Parameters:
    

**imgs** â 

the batch of images to process, which can be any of the following:

  * A list of PIL images

  * A list of uint8 numpy arrays (HWC)

  * A list of Torch tensors (CHW)

  * A uint8 numpy tensor (NHWC)

  * A Torch tensor (NCHW)




Returns:
    

a list of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances or a list of dicts of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

property preprocess#
    

Whether to apply preprocessing transforms for inference, if any.

property ragged_batches#
    

Whether `transforms()` may return tensors of different sizes. If True, then passing ragged lists of images to `predict_all()` may not be not allowed.

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
