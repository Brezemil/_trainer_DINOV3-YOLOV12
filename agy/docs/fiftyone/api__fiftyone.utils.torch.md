---
source_url: https://docs.voxel51.com/api/fiftyone.utils.torch.html
---

# fiftyone.utils.torch#

PyTorch utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`load_torch_hub_image_model`(repo_or_dir,Â model) | Loads an image model from [PyTorch Hub](https://pytorch.org/hub) as a `TorchImageModel`.  
---|---  
`load_torch_hub_raw_model`(*args,Â **kwargs) | Loads a raw model from [PyTorch Hub](https://pytorch.org/hub) as a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)").  
`find_torch_hub_requirements`(repo_or_dir[,Â ...]) | Locates the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.  
`load_torch_hub_requirements`(repo_or_dir[,Â ...]) | Loads the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.  
`install_torch_hub_requirements`(repo_or_dir) | Installs the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.  
`ensure_torch_hub_requirements`(repo_or_dir[,Â ...]) | Verifies that the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model are installed.  
`to_rgb_pil`(img) | Converts image-like input to an RGB PIL image.  
`imgs_to_rgb_pil`(imgs) | Converts a batch of image-like inputs to RGB PIL images.  
`recommend_num_workers`([num_workers]) | Recommend a number of workers for running a [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)").  
`from_image_classification_dir_tree`(dataset_dir) | Creates a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") for the given image classification dataset directory tree.  
`get_local_size`(local_process_group) | Gets the number of processes per-machine in the local process group.  
`get_world_size`() | Returns the world size of the current operation.  
`get_local_rank`(local_process_group) | Gets the rank of the current process within the local processes group.  
`get_rank`() | Gets the rank of the current process.  
`local_scatter`(array,Â local_process_group) | Scatters the given array from the local leader to all local workers.  
`all_gather`(data[,Â group]) | Gathers arbitrary picklable data (not necessarily tensors).  
`local_broadcast_process_authkey`(...) |   
`get_samples_dict_for_get_item`(samples,Â ...) | Creates a dictionary to use as input to `fiftyone.utils.torch.GetItem` call method.  
`get_model_inputs_from_get_item`(samples,Â get_item) | Generate model inputs using a `fiftyone.utils.torch.GetItem`.  
  
**Classes:**

`GetItem`([field_mapping]) | A class that defines how to load the input for a model.  
---|---  
`TorchEmbeddingsMixin`(model[,Â layer_name,Â ...]) | Mixin for Torch models that can generate embeddings.  
`TorchImageModelConfig`(d) | Configuration for running a `TorchImageModel`.  
`ImageGetItem`([field_mapping,Â transform,Â ...]) | A `GetItem` that loads images to feed to `TorchImageModel` instances.  
`TorchImageModel`(config) | Wrapper for evaluating a Torch model on images.  
`TorchImageModelWithPrompts`(config) | A convenience class for identifying models that accept prompts.  
`TorchSamplesMixin`() |   
`ToPILImage`() | Transform that converts a tensor or ndarray to a PIL image, while also allowing PIL images to passthrough.  
`MinResize`(min_output_size[,Â interpolation]) | Transform that resizes the PIL image or torch Tensor, if necessary, so that its minimum dimensions are at least the specified size.  
`MaxResize`(max_output_size[,Â interpolation]) | Transform that resizes the PIL image or torch Tensor, if necessary, so that its maximum dimensions are at most the specified size.  
`PatchSize`(patch_size) | Transform that center crops the PIL image or torch Tensor, if necessary, so that its dimensions are multiples of the specified patch size.  
`SaveLayerTensor`(model,Â layer_name) | Callback that saves the input/output tensor of the specified layer of a Torch model during each `forward()` call.  
`OutputProcessor`([classes]) | Interface for processing the outputs of Torch models.  
`ClassifierOutputProcessor`([classes,Â ...]) | Output processor for single label classifiers.  
`DetectorOutputProcessor`([classes]) | Output processor for object detectors.  
`InstanceSegmenterOutputProcessor`([classes,Â ...]) | Output processor for instance segmenters.  
`KeypointOutputProcessor`(*args,Â **kwargs) | Output processor for keypoint prediction models.  
`KeypointDetectorOutputProcessor`([classes]) | Output processor for keypoint detection models.  
`SemanticSegmenterOutputProcessor`([classes,Â ...]) | Output processor for semantic segmenters.  
`FiftyOneTorchDataset`(samples,Â get_item[,Â ...]) | Constructs a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") that loads data from an arbitrary [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") via the provided `GetItem` instance.  
`TorchImageDataset`([image_paths,Â samples,Â ...]) | A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") of images.  
`TorchImageClassificationDataset`([...]) | A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") for image classification.  
`TorchImagePatchesDataset`([image_paths,Â ...]) | A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") of image patch tensors extracted from a list of images.  
`NumpySerializedList`(lst) |   
`TorchSerializedList`(lst) |   
`TorchShmSerializedList`(lst,Â local_process_group) |   
  
fiftyone.utils.torch.load_torch_hub_image_model(_repo_or_dir_ , _model_ , _hub_kwargs =None_, _** kwargs_)#
    

Loads an image model from [PyTorch Hub](https://pytorch.org/hub) as a `TorchImageModel`.

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    model = fout.load_torch_hub_image_model(
        "facebookresearch/dinov2",
        "dinov2_vits14",
        image_patch_size=14,
        embeddings_layer="head",
    )
    
    assert model.has_embeddings is True
    

Parameters:
    

  * **repo_or_dir** â see `torch:torch.hub.load`

  * **model** â see `torch:torch.hub.load`

  * ****kwargs** â additional parameters for `TorchImageModelConfig`



Returns:
    

a `TorchImageModel`

fiftyone.utils.torch.load_torch_hub_raw_model(_* args_, _** kwargs_)#
    

Loads a raw model from [PyTorch Hub](https://pytorch.org/hub) as a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)").

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    model = fout.load_torch_hub_raw_model(
        "facebookresearch/dinov2",
        "dinov2_vits14",
    )
    
    print(type(model))
    # <class 'dinov2.models.vision_transformer.DinoVisionTransformer'>
    

Parameters:
    

  * ***args** â positional arguments for `torch:torch.hub.load`

  * ****kwargs** â keyword arguments for `torch:torch.hub.load`



Returns:
    

a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

fiftyone.utils.torch.find_torch_hub_requirements(_repo_or_dir_ , _source ='github'_)#
    

Locates the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    req_path = fout.find_torch_hub_requirements("facebookresearch/dinov2")
    
    print(req_path)
    # '~/.cache/torch/hub/facebookresearch_dinov2_main/requirements.txt'
    

Parameters:
    

  * **repo_or_dir** â see `torch:torch.hub.load`

  * **source** (_"github"_) â see `torch:torch.hub.load`



Returns:
    

the path to the requirements file on disk

fiftyone.utils.torch.load_torch_hub_requirements(_repo_or_dir_ , _source ='github'_)#
    

Loads the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    requirements = fout.load_torch_hub_requirements("facebookresearch/dinov2")
    
    print(requirements)
    # ['torch==2.0.0', 'torchvision==0.15.0', ...]
    

Parameters:
    

  * **repo_or_dir** â see `torch:torch.hub.load`

  * **source** (_"github"_) â see `torch:torch.hub.load`



Returns:
    

a list of requirement strings

fiftyone.utils.torch.install_torch_hub_requirements(_repo_or_dir_ , _source ='github'_, _error_level =None_)#
    

Installs the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model.

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    fout.install_torch_hub_requirements("facebookresearch/dinov2")
    

Parameters:
    

  * **repo_or_dir** â see `torch:torch.hub.load`

  * **source** (_"github"_) â see `torch:torch.hub.load`

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if the install fails

    * 1: log warning if the install fails

    * 2: ignore install fails

By default, `fiftyone.config.requirement_error_level` is used




fiftyone.utils.torch.ensure_torch_hub_requirements(_repo_or_dir_ , _source ='github'_, _error_level =None_, _log_success =False_)#
    

Verifies that the package requirements from the `requirements.txt` file on disk associated with a downloaded [PyTorch Hub](https://pytorch.org/hub) model are installed.

Example usage:
    
    
    import fiftyone.utils.torch as fout
    
    fout.ensure_torch_hub_requirements("facebookresearch/dinov2")
    

Parameters:
    

  * **repo_or_dir** â see `torch:torch.hub.load`

  * **source** (_"github"_) â see `torch:torch.hub.load`

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if requirement is not satisfied

    * 1: log warning if requirement is not satisfied

    * 2: ignore unsatisifed requirements

By default, `fiftyone.config.requirement_error_level` is used

  * **log_success** (_False_) â whether to generate a log message if a requirement is satisfied




class fiftyone.utils.torch.GetItem(_field_mapping =None_, _** kwargs_)#
    

Bases: `object`

A class that defines how to load the input for a model.

Models that implement the [`fiftyone.core.models.SupportsGetItem`](api__fiftyone.core.models.md#fiftyone.core.models.SupportsGetItem "fiftyone.core.models.SupportsGetItem") mixin use this class to define how `FiftyOneTorchDataset` should load their inputs.

The `__call__()` method should accept a dictionary mapping the keys defined by `required_keys` to values extracted from the input [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instance according to the mapping defined by `field_mapping`.

Parameters:
    

**field_mapping** (_None_) â a user-supplied dict mapping keys in `required_keys` to field names of their dataset that contain the required values

**Attributes:**

`required_keys` | The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.  
---|---  
`field_mapping` | A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.  
  
property required_keys#
    

The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.

The user supplies the field names from which to extract these values from their samples via `field_mapping`.

property field_mapping#
    

A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.

class fiftyone.utils.torch.TorchEmbeddingsMixin(_model_ , _layer_name =None_, _as_feature_extractor =False_)#
    

Bases: [`EmbeddingsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin "fiftyone.core.models.EmbeddingsMixin")

Mixin for Torch models that can generate embeddings.

Parameters:
    

  * **model** â the Torch model, a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

  * **layer_name** (_None_) â the name of the embeddings layer whose output to save, or `None` if this model instance should not expose embeddings. Prepend `"<"` to save the input tensor instead

  * **as_feature_extractor** (_False_) â whether to operate the model as a feature extractor. If `layer_name` is provided, this layer is passed to torchvisionâs `create_feature_extractor()` function. If no `layer_name` is provided, the modelâs output is used as-is for feature extraction




**Attributes:**

`has_embeddings` | Whether this model has embeddings.  
---|---  
  
**Methods:**

`embed`(arg) | Generates an embedding for the given data.  
---|---  
`embed_all`(args) | Generates embeddings for the given iterable of data.  
`get_embeddings`() | Returns the embeddings generated by the last forward pass of the model.  
  
property has_embeddings#
    

Whether this model has embeddings.

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

get_embeddings()#
    

Returns the embeddings generated by the last forward pass of the model.

By convention, this method should always return an array whose first axis represents batch size (which will always be 1 when `predict()` was last used).

Returns:
    

a numpy array containing the embedding(s)

class fiftyone.utils.torch.TorchImageModelConfig(_d_)#
    

Bases: [`Config`](api__fiftyone.core.config.md#fiftyone.core.config.Config "fiftyone.core.config.Config")

Configuration for running a `TorchImageModel`.

Models are represented by this class via the following three components:

  1. Model:
         
         # Directly specify a model
         model
         
         # Load model from an entrypoint
         model = entrypoint_fcn(**entrypoint_args)
         

  2. Transforms:
         
         # Directly provide transforms
         transforms
         
         # Load transforms from a function
         transforms = transforms_fcn(**transforms_args)
         
         # Use the `image_XXX` parameters defined below to build a transform
         transforms = build_transforms(image_XXX, ...)
         

  3. OutputProcessor:
         
         # Directly provide an OutputProcessor
         output_processor
         
         # Load an OutputProcessor from a function
         output_processor = output_processor_cls(**output_processor_args)
         




Given these components, inference happens as follows:
    
    
    def predict_all(imgs):
        imgs = [transforms(img) for img in imgs]
        if not raw_inputs:
            imgs = torch.stack(imgs)
    
        output = model(imgs)
        return output_processor(output, ...)
    

Parameters:
    

  * **model** (_None_) â a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") instance to use

  * **entrypoint_fcn** (_None_) â a function or string like `"torchvision.models.inception_v3"` specifying the entrypoint function that loads the model

  * **entrypoint_args** (_None_) â a dictionary of arguments for `entrypoint_fcn`

  * **transforms** (_None_) â a preprocessing transform to apply

  * **transforms_fcn** (_None_) â a function or string like `"torchvision.models.Inception_V3_Weights.DEFAULT.transforms"` specifying a function that returns a preprocessing transform function to apply

  * **transforms_args** (_None_) â a dictionary of arguments for `transforms_args`

  * **ragged_batches** (_None_) â whether the provided `transforms` or `transforms_fcn` may return tensors of different sizes. This must be set to `False` to enable batch inference, if it is desired

  * **raw_inputs** (_None_) â whether to feed the raw list of images to the model rather than stacking them as a Torch tensor

  * **output_processor** (_None_) â an `OutputProcessor` instance to use

  * **output_processor_cls** (_None_) â a class or string like `"fifytone.utils.torch.ClassifierOutputProcessor"` specifying the `OutputProcessor` to use

  * **output_processor_args** (_None_) â a dictionary of arguments for `output_processor_cls(classes=classes, **kwargs)`

  * **confidence_thresh** (_None_) â an optional confidence threshold apply to any applicable predictions generated by the model

  * **filter_classes** (_None_) â an optional iterable of classes to use to filter any applicable predictions generated by the model

  * **classes** (_None_) â a list of class names for the model, if applicable

  * **labels_string** (_None_) â a comma-separated list of the class names for the model, if applicable

  * **labels_path** (_None_) â the path to the labels map for the model, if applicable

  * **mask_targets** (_None_) â a mask targets dict for the model, if applicable

  * **mask_targets_path** (_None_) â the path to a mask targets map for the model, if applicable

  * **skeleton** (_None_) â a keypoint skeleton dict for the model, if applicable

  * **image_min_size** (_None_) â resize the input images during preprocessing, if necessary, so that the image dimensions are at least this `(width, height)`

  * **image_min_dim** (_None_) â resize input images during preprocessing, if necessary, so that the smaller image dimension is at least this value

  * **image_max_size** (_None_) â resize the input images during preprocessing, if necessary, so that the image dimensions are at most this `(width, height)`

  * **image_max_dim** (_None_) â resize input images during preprocessing, if necessary, so that the largest image dimension is at most this value.

  * **image_size** (_None_) â a `(width, height)` to which to resize the input images during preprocessing

  * **image_dim** (_None_) â resize the smaller input dimension to this value during preprocessing

  * **image_patch_size** (_None_) â crop the input images during preprocessing, if necessary, so that the image dimensions are a multiple of this patch size

  * **image_mean** (_None_) â a 3-array of mean values in `[0, 1]` for preprocessing the input images

  * **image_std** (_None_) â a 3-array of std values in `[0, 1]` for preprocessing the input images inputs that are lists of Tensors

  * **embeddings_layer** (_None_) â the name of a layer whose output to expose as embeddings. Prepend `"<"` to save the input tensor instead

  * **as_feature_extractor** (_False_) â whether to operate the model as a feature extractor. If `embeddings_layer` is provided, this layer is passed to torchvisionâs `create_feature_extractor()` function. If no `embeddings_layer` is provided, the modelâs output is used as-is for feature extraction

  * **use_half_precision** (_None_) â whether to use half precision (only supported when using GPU)

  * **cudnn_benchmark** (_None_) â a value to use for [`torch.backends.cudnn.benchmark`](https://docs.pytorch.org/docs/stable/backends.html#torch.backends.cudnn.benchmark "\(in PyTorch v2.12\)") while the model is running

  * **device** (_None_) â a string specifying the device to use, eg `("cuda:0", "mps", "cpu")`. By default, CUDA is used if available, else CPU is used




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




class fiftyone.utils.torch.ImageGetItem(_field_mapping =None_, _transform =None_, _raw_inputs =False_, _using_half_precision =False_, _use_numpy =False_, _** kwargs_)#
    

Bases: `GetItem`

A `GetItem` that loads images to feed to `TorchImageModel` instances.

By default, images are loaded from the `"filepath"` field of samples, but users can override this by providing `field_mapping={"filepath": "another_field"}`.

Parameters:
    

  * **field_mapping** (_None_) â the user-supplied dict mapping keys in `required_keys` to field names of their dataset that contain the required values

  * **transform** (_None_) â a `torchvision.transforms` function to apply

  * **raw_inputs** (_False_) â whether to feed the raw list of images to the model rather than stacking them as a Torch tensor

  * **using_half_precision** (_False_) â whether the model is using half precision

  * **use_numpy** (_False_) â whether to use numpy arrays rather than PIL images and Torch tensors when loading data




**Attributes:**

`required_keys` | The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.  
---|---  
`field_mapping` | A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.  
  
property required_keys#
    

The list of keys that must exist on the dicts provided to the `__call__()` method at runtime.

The user supplies the field names from which to extract these values from their samples via `field_mapping`.

property field_mapping#
    

A user-supplied dictionary mappings keys in `required_keys` to field names of their dataset that contain the required values.

class fiftyone.utils.torch.TorchImageModel(_config_)#
    

Bases: [`SupportsGetItem`](api__fiftyone.core.models.md#fiftyone.core.models.SupportsGetItem "fiftyone.core.models.SupportsGetItem"), `TorchEmbeddingsMixin`, [`TorchModelMixin`](api__fiftyone.core.models.md#fiftyone.core.models.TorchModelMixin "fiftyone.core.models.TorchModelMixin"), [`LogitsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.LogitsMixin "fiftyone.core.models.LogitsMixin"), [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model")

Wrapper for evaluating a Torch model on images.

See [this page](model_zoo__design.md#model-zoo-custom-models) for example usage.

Parameters:
    

**config** â an `TorchImageModelConfig`

**Methods:**

`build_get_item`([field_mapping]) | Builds the `fiftyone.utils.torch.GetItem` instance that defines how the model's data should be loaded by data loaders.  
---|---  
`collate_fn`(batch) | The collate function to use when creating dataloaders for this model.  
`predict`(img) | Performs prediction on the given image.  
`predict_all`(imgs) | Performs prediction on the given batch of images.  
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

`media_type` | The media type processed by the model.  
---|---  
`has_logits` | Whether this instance can generate logits.  
`ragged_batches` | Whether `transforms()` may return tensors of different sizes.  
`transforms` | A `torchvision.transforms` function that will be applied to each input before prediction, if any.  
`has_collate_fn` | Whether this model has a custom collate function.  
`preprocess` | Whether to apply preprocessing transforms for inference, if any.  
`using_gpu` | Whether the model is using GPU.  
`device` | The `torch:torch.torch.device` that the model is using.  
`using_half_precision` | Whether the model is using half precision.  
`classes` | The list of class labels for the model, if known.  
`num_classes` | The number of classes for the model, if known.  
`mask_targets` | The mask targets for the model, if any.  
`skeleton` | The keypoint skeleton for the model, if any.  
`can_embed_prompts` | Whether this model can generate prompt embeddings.  
`has_embeddings` | Whether this model has embeddings.  
`required_keys` | The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.  
`store_logits` | Whether the model should store logits in its predictions.  
  
build_get_item(_field_mapping =None_)#
    

Builds the `fiftyone.utils.torch.GetItem` instance that defines how the modelâs data should be loaded by data loaders.

Parameters:
    

**field_mapping** (_None_) â a user-provided dict mapping required keys to dataset field names

Returns:
    

a `fiftyone.utils.torch.GetItem` instance

property media_type#
    

The media type processed by the model.

property has_logits#
    

Whether this instance can generate logits.

property ragged_batches#
    

Whether `transforms()` may return tensors of different sizes. If True, then passing ragged lists of images to `predict_all()` may not be not allowed.

property transforms#
    

A `torchvision.transforms` function that will be applied to each input before prediction, if any.

property has_collate_fn#
    

Whether this model has a custom collate function.

Set this to `True` if you want `collate_fn()` to be used during inference.

static collate_fn(_batch_)#
    

The collate function to use when creating dataloaders for this model.

In order to enable this functionality, the modelâs `has_collate_fn()` property must return `True`.

By default, this is the default collate function for [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)"), but subclasses can override this method as necessary.

Note that this function must be serializable so it is compatible with multiprocessing for dataloaders.

Parameters:
    

**batch** â a list of items to collate

Returns:
    

the collated batch, which will be fed directly to the model

property preprocess#
    

Whether to apply preprocessing transforms for inference, if any.

property using_gpu#
    

Whether the model is using GPU.

property device#
    

The `torch:torch.torch.device` that the model is using.

property using_half_precision#
    

Whether the model is using half precision.

property classes#
    

The list of class labels for the model, if known.

property num_classes#
    

The number of classes for the model, if known.

property mask_targets#
    

The mask targets for the model, if any.

property skeleton#
    

The keypoint skeleton for the model, if any.

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

property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

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

property required_keys#
    

The required keys that must be provided as parameters to methods like `apply_model()` and `compute_embeddings()` at runtime.

property store_logits#
    

Whether the model should store logits in its predictions.

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

class fiftyone.utils.torch.TorchImageModelWithPrompts(_config_)#
    

Bases: `TorchImageModel`

A convenience class for identifying models that accept prompts.

NOTE: A subclass shouldnât inherit from both, `TorchImageModelWithPrompts` and `TorchSamplesMixin`.

**Methods:**

`build_get_item`([field_mapping]) | Builds the `fiftyone.utils.torch.GetItem` instance that defines how the model's data should be loaded by data loaders.  
---|---  
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
  
build_get_item(_field_mapping =None_)#
    

Builds the `fiftyone.utils.torch.GetItem` instance that defines how the modelâs data should be loaded by data loaders.

Parameters:
    

**field_mapping** (_None_) â a user-provided dict mapping required keys to dataset field names

Returns:
    

a `fiftyone.utils.torch.GetItem` instance

property can_embed_prompts#
    

Whether this model can generate prompt embeddings.

This method returns `False` by default. Models that can generate prompt embeddings should override this via implementing the `PromptMixin` interface.

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

class fiftyone.utils.torch.TorchSamplesMixin#
    

Bases: [`SamplesMixin`](api__fiftyone.core.models.md#fiftyone.core.models.SamplesMixin "fiftyone.core.models.SamplesMixin")

**Methods:**

`predict`(img[,Â sample]) | Performs prediction on the given data.  
---|---  
`predict_all`(args[,Â samples]) | Performs prediction on the given iterable of data.  
  
**Attributes:**

`needs_fields` | A dict mapping model-specific keys to sample field names.  
---|---  
  
predict(_img_ , _sample =None_)#
    

Performs prediction on the given data.

Image models should support, at minimum, processing `arg` values that are uint8 numpy arrays (HWC).

Video models should support, at minimum, processing `arg` values that are `eta.core.video.VideoReader` instances.

Parameters:
    

  * **arg** â the data

  * **sample** (_None_) â the [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") associated with the data



Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance or dict of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

property needs_fields#
    

A dict mapping model-specific keys to sample field names.

predict_all(_args_ , _samples =None_)#
    

Performs prediction on the given iterable of data.

Image models should support, at minimum, processing `args` values that are either lists of uint8 numpy arrays (HWC) or numpy array tensors (NHWC).

Video models should support, at minimum, processing `args` values that are lists of `eta.core.video.VideoReader` instances.

Subclasses can override this method to increase efficiency, but, by default, this method simply iterates over the data and applies `predict()` to each.

Parameters:
    

  * **args** â an iterable of data

  * **samples** (_None_) â an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances associated with the data



Returns:
    

a list of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances or a list of dicts of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances containing the predictions

class fiftyone.utils.torch.ToPILImage#
    

Bases: `object`

Transform that converts a tensor or ndarray to a PIL image, while also allowing PIL images to passthrough.

fiftyone.utils.torch.to_rgb_pil(_img_)#
    

Converts image-like input to an RGB PIL image.

fiftyone.utils.torch.imgs_to_rgb_pil(_imgs_)#
    

Converts a batch of image-like inputs to RGB PIL images.

class fiftyone.utils.torch.MinResize(_min_output_size_ , _interpolation =None_)#
    

Bases: `object`

Transform that resizes the PIL image or torch Tensor, if necessary, so that its minimum dimensions are at least the specified size.

Parameters:
    

  * **min_output_size** â desired minimum output dimensions. Can either be a `(min_height, min_width)` tuple or a single `min_dim`

  * **interpolation** (_None_) â optional interpolation mode. Passed directly to [`torchvision.transforms.functional.resize()`](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.functional.resize.html#torchvision.transforms.functional.resize "\(in Torchvision v0.27\)")




class fiftyone.utils.torch.MaxResize(_max_output_size_ , _interpolation =None_)#
    

Bases: `object`

Transform that resizes the PIL image or torch Tensor, if necessary, so that its maximum dimensions are at most the specified size.

Parameters:
    

  * **max_output_size** â desired maximum output dimensions. Can either be a `(max_height, max_width)` tuple or a single `max_dim`

  * **interpolation** (_None_) â optional interpolation mode. Passed directly to [`torchvision.transforms.functional.resize()`](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.functional.resize.html#torchvision.transforms.functional.resize "\(in Torchvision v0.27\)")




class fiftyone.utils.torch.PatchSize(_patch_size_)#
    

Bases: `object`

Transform that center crops the PIL image or torch Tensor, if necessary, so that its dimensions are multiples of the specified patch size.

Parameters:
    

**patch_size** â the patch size

class fiftyone.utils.torch.SaveLayerTensor(_model_ , _layer_name_)#
    

Bases: `object`

Callback that saves the input/output tensor of the specified layer of a Torch model during each `forward()` call.

Parameters:
    

  * **model** â the Torch model, a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)")

  * **layer_name** â the name of the layer whose output to save. Prepend `"<"` to save the input tensor instead




**Attributes:**

`tensor` | The tensor saved from the last `forward()` call.  
---|---  
  
property tensor#
    

The tensor saved from the last `forward()` call.

class fiftyone.utils.torch.OutputProcessor(_classes =None_, _** kwargs_)#
    

Bases: `object`

Interface for processing the outputs of Torch models.

Parameters:
    

**classes** (_None_) â the list of class labels for the model. This may not be required or used by some models

class fiftyone.utils.torch.ClassifierOutputProcessor(_classes =None_, _store_logits =False_, _logits_key ='logits'_)#
    

Bases: `OutputProcessor`

Output processor for single label classifiers.

Parameters:
    

  * **classes** (_None_) â the list of class labels for the model

  * **store_logits** (_False_) â whether to store logits in the model outputs




class fiftyone.utils.torch.DetectorOutputProcessor(_classes =None_)#
    

Bases: `OutputProcessor`

Output processor for object detectors.

Parameters:
    

**classes** (_None_) â the list of class labels for the model

class fiftyone.utils.torch.InstanceSegmenterOutputProcessor(_classes =None_, _mask_thresh =0.5_)#
    

Bases: `OutputProcessor`

Output processor for instance segmenters.

Parameters:
    

  * **classes** (_None_) â the list of class labels for the model

  * **mask_thresh** (_0.5_) â a threshold to use to convert soft masks to binary masks




class fiftyone.utils.torch.KeypointOutputProcessor(_* args_, _** kwargs_)#
    

Bases: `OutputProcessor`

Output processor for keypoint prediction models.

class fiftyone.utils.torch.KeypointDetectorOutputProcessor(_classes =None_)#
    

Bases: `OutputProcessor`

Output processor for keypoint detection models.

Parameters:
    

**classes** (_None_) â the list of class labels for the model

class fiftyone.utils.torch.SemanticSegmenterOutputProcessor(_classes =None_, _no_background_cls =False_, _has_softmax_out =True_)#
    

Bases: `OutputProcessor`

Output processor for semantic segmenters.

Parameters:
    

  * **classes** (_None_) â the list of class labels for the model. This parameter is not used

  * **no_background_cls** (_False_) â if true, class indices are incremented by 1 in the mask

  * **has_softmax_out** (_True_) â if false, softmax is applied to output predictions




fiftyone.utils.torch.recommend_num_workers(_num_workers =None_)#
    

Recommend a number of workers for running a [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)").

Returns:
    

the recommended number of workers

class fiftyone.utils.torch.FiftyOneTorchDataset(_samples_ , _get_item_ , _vectorize =False_, _skip_failures =False_, _local_process_group =None_)#
    

Bases: [`Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)")

Constructs a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") that loads data from an arbitrary [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") via the provided `GetItem` instance.

Warning

For input views with repeated sample IDs, it is recommended to use `vectorize=True`. Do not use `vectorize=False` in this case, it will give unexpected results.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **get_item** â a `GetItem`

  * **vectorize** (_False_) â whether to load and cache the required fields from the sample collection upfront (True) or lazily load the values from each sample when items are retrieved (False). Vectorizing gives faster data loading times, but you must have enough memory to store the required field values for the entire collection. When `vectorize=True`, all field values must be serializable; ie `pickle.dumps(field_value)` must not raise an error

  * **skip_failures** (_False_) â whether to skip failures that occur when calling `get_item`. If True, the exception will be returned rather than the intended field values

  * **local_process_group** (_None_) â the local process group. Only used during distributed training




**Attributes:**

`samples` |   
---|---  
  
**Methods:**

`worker_init`(worker_id) | Initializes a worker during inference/training.  
---|---  
`distributed_init`(dataset_name,Â ...[,Â view_name]) | Initializes a trainer process during distributed training.  
  
property samples#
    

static worker_init(_worker_id_)#
    

Initializes a worker during inference/training.

This method is used as the `worker_init_fn` parameter for [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "\(in PyTorch v2.12\)").

Parameters:
    

**worker_id** â the worker ID

static distributed_init(_dataset_name_ , _local_process_group_ , _view_name =None_)#
    

Initializes a trainer process during distributed training.

This function should be called at the beginning of the training script. It facilitates communication between processes and safely creates a database connection for each trainer.

Parameters:
    

  * **dataset_name** â the name of the dataset to load

  * **local_process_group** â the process group with all the processes running the main training script

  * **view_name** (_None_) â the name of a saved view to load



Returns:
    

the loaded [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

class fiftyone.utils.torch.TorchImageDataset(_image_paths =None_, _samples =None_, _sample_ids =None_, _include_ids =False_, _transform =None_, _use_numpy =False_, _force_rgb =False_, _skip_failures =False_)#
    

Bases: [`Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)")

A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") of images.

Instances of this dataset emit images for each sample, or `(img, sample_id)` pairs if `sample_ids` are provided or `include_ids == True`.

By default, this class will load images in PIL format and emit Torch tensors, but you can use numpy images/tensors instead by passing `use_numpy = True`.

Parameters:
    

  * **image_paths** (_None_) â an iterable of image paths

  * **samples** (_None_) â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") from which to extract image paths

  * **sample_ids** (_None_) â an iterable of sample IDs corresponding to each image

  * **include_ids** (_False_) â whether to include the IDs of the `samples` in the returned items

  * **transform** (_None_) â an optional transform function to apply to each image patch. When `use_numpy == False`, this is typically a torchvision transform

  * **use_numpy** (_False_) â whether to use numpy arrays rather than PIL images and Torch tensors when loading data

  * **force_rgb** (_False_) â whether to force convert the images to RGB

  * **skip_failures** (_False_) â whether to return an `Exception` object rather than raising it if an error occurs while loading a sample




**Attributes:**

`has_sample_ids` | Whether this dataset has sample IDs.  
---|---  
  
property has_sample_ids#
    

Whether this dataset has sample IDs.

class fiftyone.utils.torch.TorchImageClassificationDataset(_image_paths =None_, _targets =None_, _samples =None_, _sample_ids =None_, _include_ids =False_, _transform =None_, _use_numpy =False_, _force_rgb =False_, _skip_failures =False_)#
    

Bases: [`Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)")

A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") for image classification.

Instances of this dataset emit images and their associated targets for each sample, either directly as `(img, target)` pairs or as `(img, target, sample_id)` pairs if `sample_ids` are provided or `include_ids == True`.

By default, this class will load images in PIL format and emit Torch tensors, but you can use numpy images/tensors instead by passing `use_numpy = True`.

Parameters:
    

  * **image_paths** (_None_) â an iterable of image paths

  * **targets** (_None_) â an iterable of targets, or the name of a field or embedded field of `samples` to use as targets

  * **samples** (_None_) â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") from which to extract image paths and targets

  * **sample_ids** (_None_) â an iterable of sample IDs corresponding to each image

  * **include_ids** (_False_) â whether to include the IDs of the `samples` in the returned items

  * **transform** (_None_) â an optional transform function to apply to each image patch. When `use_numpy == False`, this is typically a torchvision transform

  * **use_numpy** (_False_) â whether to use numpy arrays rather than PIL images and Torch tensors when loading data

  * **force_rgb** (_False_) â whether to force convert the images to RGB

  * **skip_failures** (_False_) â whether to return an `Exception` object rather than raising it if an error occurs while loading a sample




**Attributes:**

`has_sample_ids` | Whether this dataset has sample IDs.  
---|---  
  
property has_sample_ids#
    

Whether this dataset has sample IDs.

class fiftyone.utils.torch.TorchImagePatchesDataset(_image_paths =None_, _patches =None_, _samples =None_, _patches_field =None_, _handle_missing ='skip'_, _transform =None_, _sample_ids =None_, _include_ids =False_, _ragged_batches =False_, _use_numpy =False_, _force_rgb =False_, _force_square =False_, _alpha =None_, _skip_failures =False_)#
    

Bases: [`Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)")

A [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") of image patch tensors extracted from a list of images.

Provide either `image_paths` and `patches` or `samples` and `patches_field` in order to use this dataset.

Instances of this dataset emit image patches for each sample, or `(patches, sample_id)` tuples if `sample_ids` are provided or `include_ids == True`.

By default, this class will load images in PIL format and emit Torch tensors, but you can use numpy images/tensors instead by passing `use_numpy = True`.

If `ragged_batches = False` (the default), this class will emit tensors containing the stacked (along axis 0) patches from each image. In this case, the provided `transform` must ensure that all image patches are resized to the same shape so they can be stacked.

If `ragged_batches = True`, lists of patch tensors will be returned.

Parameters:
    

  * **image_paths** (_None_) â an iterable of image paths

  * **patches** (_None_) â a list of labels of type [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") specifying the image patch(es) to extract from each image. Elements can be `None` if an image has no patches

  * **samples** (_None_) â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") from which to extract patches

  * **patches_field** (_None_) â the name of the field defining the image patches in `samples` to extract. Must be of type [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * **handle_missing** (_"skip"_) â 

how to handle images with no patches. The supported values are:

    * âskipâ: skip the image and assign its embedding as `None`

    * âimageâ: use the whole image as a single patch

    * âerrorâ: raise an error

  * **transform** (_None_) â an optional transform function to apply to each image patch. When `use_numpy == False`, this is typically a torchvision transform

  * **sample_ids** (_None_) â an iterable of sample IDs corresponding to each image

  * **include_ids** (_False_) â whether to include the IDs of the `samples` in the returned items

  * **ragged_batches** (_False_) â whether the provided `transform` may return tensors of different dimensions and thus cannot be stacked

  * **use_numpy** (_False_) â whether to use numpy arrays rather than PIL images and Torch tensors when loading data

  * **force_rgb** (_False_) â whether to force convert the images to RGB

  * **force_square** (_False_) â whether to minimally manipulate the patch bounding boxes into squares prior to extraction

  * **alpha** (_None_) â an optional expansion/contraction to apply to the patches before extracting them, in `[-1, inf)`. If provided, the length and width of the box are expanded (or contracted, when `alpha < 0`) by `(100 * alpha)%`. For example, set `alpha = 0.1` to expand the boxes by 10%, and set `alpha = -0.1` to contract the boxes by 10%

  * **skip_failures** (_False_) â whether to return an `Exception` object rather than raising it if an error occurs while loading a sample




**Attributes:**

`has_sample_ids` | Whether this dataset has sample IDs.  
---|---  
  
property has_sample_ids#
    

Whether this dataset has sample IDs.

fiftyone.utils.torch.from_image_classification_dir_tree(_dataset_dir_)#
    

Creates a [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.Dataset "\(in PyTorch v2.12\)") for the given image classification dataset directory tree.

The directory should have the following format:
    
    
    <dataset_dir>/
        <classA>/
            <image1>.<ext>
            <image2>.<ext>
            ...
        <classB>/
            <image1>.<ext>
            <image2>.<ext>
            ...
    

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

a [`torchvision.datasets.ImageFolder`](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.ImageFolder.html#torchvision.datasets.ImageFolder "\(in Torchvision v0.27\)")

class fiftyone.utils.torch.NumpySerializedList(_lst : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")_)#
    

Bases: `object`

class fiftyone.utils.torch.TorchSerializedList(_lst : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")_)#
    

Bases: `NumpySerializedList`

class fiftyone.utils.torch.TorchShmSerializedList(_lst : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")_, _local_process_group_)#
    

Bases: `TorchSerializedList`

fiftyone.utils.torch.get_local_size(_local_process_group_)#
    

Gets the number of processes per-machine in the local process group.

Parameters:
    

**local_process_group** â the local process group

Returns:
    

the number of processes per-machine

fiftyone.utils.torch.get_world_size()#
    

Returns the world size of the current operation.

Returns:
    

the world size

fiftyone.utils.torch.get_local_rank(_local_process_group_)#
    

Gets the rank of the current process within the local processes group.

Parameters:
    

**local_process_group** â the local process group

Returns:
    

the rank of the current process

fiftyone.utils.torch.get_rank()#
    

Gets the rank of the current process.

Returns:
    

the rank of the current process

fiftyone.utils.torch.local_scatter(_array_ , _local_process_group_)#
    

Scatters the given array from the local leader to all local workers.

The worker with rank `i` gets `array[i]`.

Parameters:
    

  * **array** â an array with same size as the local process group

  * **local_process_group** â the local process group



Returns:
    

the array element for the current rank

fiftyone.utils.torch.all_gather(_data_ , _group =None_)#
    

Gathers arbitrary picklable data (not necessarily tensors).

Parameters:
    

  * **data** â any picklable object

  * **group** (_None_) â a torch process group. By default, uses a group which contains all ranks on gloo backend



Returns:
    

the list of data gathered from each rank

fiftyone.utils.torch.local_broadcast_process_authkey(_local_process_group_)#
    

fiftyone.utils.torch.get_samples_dict_for_get_item(_samples_ , _field_mapping_ , _skip_failures =False_)#
    

Creates a dictionary to use as input to `fiftyone.utils.torch.GetItem` call method.

Parameters:
    

  * **samples** â an iterable of fiftyone samples

  * **field_mapping** â a user-supplied dict mapping keys in `GetItem.required_keys` to field names of their dataset that contain the required values.

  * **skip_failures** (_False_) â If true, skips failures instead of raising an error.



Returns:
    

a list of dictionary mapping `GetItem.required_keys` to sample field values

fiftyone.utils.torch.get_model_inputs_from_get_item(_samples_ , _get_item_)#
    

Generate model inputs using a `fiftyone.utils.torch.GetItem`.

Parameters:
    

  * **samples** â an iterable of fiftyone samples

  * **get_item** â an instance of a `fiftyone.utils.torch.GetItem`



Returns:
    

a list of dictionary generated by calling `fiftyone.utils.torch.GetItem`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
