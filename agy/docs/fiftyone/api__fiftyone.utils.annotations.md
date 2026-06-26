---
source_url: https://docs.voxel51.com/api/fiftyone.utils.annotations.html
---

# fiftyone.utils.annotations#

Annotation utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`connect_to_api`([backend]) | Returns an API instance connected to the annotation backend.  
---|---  
`annotate`(samples,Â anno_key[,Â label_schema,Â ...]) | Exports the samples and optional label field(s) to the given annotation backend.  
`load_annotations`(samples,Â anno_key[,Â ...]) | Downloads the labels from the given annotation run from the annotation backend and merges them into the collection.  
`draw_labeled_images`(samples,Â output_dir[,Â ...]) | Renders annotated versions of the images in the collection with the specified label data overlaid to the given directory.  
`draw_labeled_image`(sample,Â outpath[,Â ...]) | Renders an annotated version of the sample's image with the specified label data overlaid to disk.  
`draw_labeled_videos`(samples,Â output_dir[,Â ...]) | Renders annotated versions of the videos in the collection with the specified label data overlaid to the given directory.  
`draw_labeled_video`(sample,Â outpath[,Â ...]) | Renders an annotated version of the sample's video with the specified label data overlaid to disk.  
  
**Classes:**

`AnnotationBackendConfig`(name,Â label_schema) | Base class for configuring an `AnnotationBackend` instances.  
---|---  
`AnnotationBackend`(*args,Â **kwargs) | Base class for annotation backends.  
`AnnotationResults`(samples,Â config,Â anno_key,Â ...) | Base class for storing the intermediate results of an annotation run that has been initiated and is waiting for its results to be merged back into the FiftyOne dataset.  
`AnnotationAPI`() | Base class for APIs that connect to annotation backends.  
`DrawConfig`(d) | Configuration class that controls the look-and-feel of the annotations rendered on images/videos.  
  
fiftyone.utils.annotations.connect_to_api(_backend =None_, _** kwargs_)#
    

Returns an API instance connected to the annotation backend.

Some annotation backends may not expose this functionality.

Parameters:
    

  * **backend** (_None_) â the annotation backend to use. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * ****kwargs** â keyword arguments for the `AnnotationBackendConfig` subclass of the backend being used



Returns:
    

an `AnnotationAPI`

fiftyone.utils.annotations.annotate(_samples_ , _anno_key_ , _label_schema =None_, _label_field =None_, _label_type =None_, _classes =None_, _attributes =True_, _mask_targets =None_, _allow_additions =True_, _allow_deletions =True_, _allow_label_edits =True_, _allow_index_edits =True_, _allow_spatial_edits =True_, _media_field ='filepath'_, _backend =None_, _launch_editor =False_, _** kwargs_)#
    

Exports the samples and optional label field(s) to the given annotation backend.

The `backend` parameter controls which annotation backend to use. Depending on the backend you use, you may want/need to provide extra keyword arguments to this function for the constructor of the backendâs `AnnotationBackendConfig` class.

The natively provided backends and their associated config classes are:

  * `"cvat"`: [`fiftyone.utils.cvat.CVATBackendConfig`](api__fiftyone.utils.cvat.md#fiftyone.utils.cvat.CVATBackendConfig "fiftyone.utils.cvat.CVATBackendConfig")

  * `"labelstudio"`: [`fiftyone.utils.labelstudio.LabelStudioBackendConfig`](api__fiftyone.utils.labelstudio.md#fiftyone.utils.labelstudio.LabelStudioBackendConfig "fiftyone.utils.labelstudio.LabelStudioBackendConfig")

  * `"labelbox"`: [`fiftyone.utils.labelbox.LabelboxBackendConfig`](api__fiftyone.utils.labelbox.md#fiftyone.utils.labelbox.LabelboxBackendConfig "fiftyone.utils.labelbox.LabelboxBackendConfig")




See [this page](integrations__annotation.md#requesting-annotations) for more information about using this method, including how to define label schemas and how to configure login credentials for your annotation provider.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **anno_key** â a string key to use to refer to this annotation run

  * **label_schema** (_None_) â a dictionary defining the label schema to use. If this argument is provided, it takes precedence over the other schema-related arguments

  * **label_field** (_None_) â a string indicating a new or existing label field to annotate

  * **label_type** (_None_) â 

a string indicating the type of labels to annotate. The possible values are:

    * `"classification"`: a single classification stored in [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") fields

    * `"classifications"`: multilabel classifications stored in [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") fields

    * `"detections"`: object detections stored in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields

    * `"instances"`: instance segmentations stored in [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields with their [`mask`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection.mask "fiftyone.core.labels.Detection.mask") attributes populated

    * `"polylines"`: polylines stored in [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `False`

    * `"polygons"`: polygons stored in [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") fields with their [`filled`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline.filled "fiftyone.core.labels.Polyline.filled") attributes set to `True`

    * `"keypoints"`: keypoints stored in [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") fields

    * `"segmentation"`: semantic segmentations stored in [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") fields

    * `"scalar"`: scalar labels stored in [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField"), [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField"), [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField"), or [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField") fields

All new label fields must have their type specified via this argument or in `label_schema`. Note that annotation backends may not support all label types

  * **classes** (_None_) â a list of strings indicating the class options for `label_field` or all fields in `label_schema` without classes specified. All new label fields must have a class list provided via one of the supported methods. For existing label fields, if classes are not provided by this argument nor `label_schema`, the observed labels on your dataset are used

  * **attributes** (_True_) â 

specifies the label attributes of each label field to include (other than their `label`, which is always included) in the annotation export. Can be any of the following:

    * `True`: export all label attributes

    * `False`: donât export any custom label attributes

    * an attribute or list of attributes to export

    * a dict mapping attribute names to dicts specifying the details of the attribute field

If a `label_schema` is also provided, this parameter determines which attributes are included for all fields that do not explicitly define their per-field attributes (in addition to any per-class attributes)

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to semantic label strings. Only applicable when annotating semantic segmentations. All new label fields must have mask targets provided via one of the supported methods. For existing label fields, if mask targets are not provided by this argument nor `label_schema`, any applicable mask targets stored on your dataset will be used, if available

  * **allow_additions** (_True_) â whether to allow new labels to be added. Only applicable when editing existing label fields

  * **allow_deletions** (_True_) â whether to allow labels to be deleted. Only applicable when editing existing label fields

  * **allow_label_edits** (_True_) â whether to allow the `label` attribute of existing labels to be modified. Only applicable when editing existing fields with `label` attributes

  * **allow_index_edits** (_True_) â whether to allow the `index` attribute of existing video tracks to be modified. Only applicable when editing existing frame fields with `index` attributes

  * **allow_spatial_edits** (_True_) â whether to allow edits to the spatial properties (bounding boxes, vertices, keypoints, masks, etc) of labels. Only applicable when editing existing spatial label fields

  * **media_field** (_"filepath"_) â the field containing the paths to the media files to upload

  * **backend** (_None_) â the annotation backend to use. The supported values are `fiftyone.annotation_config.backends.keys()` and the default is `fiftyone.annotation_config.default_backend`

  * **launch_editor** (_False_) â whether to launch the annotation backendâs editor after uploading the samples

  * ****kwargs** â keyword arguments for the `AnnotationBackendConfig` subclass of the backend being used



Returns:
    

an `AnnotationResults`

fiftyone.utils.annotations.load_annotations(_samples_ , _anno_key_ , _dest_field =None_, _unexpected ='prompt'_, _cleanup =False_, _progress =None_, _** kwargs_)#
    

Downloads the labels from the given annotation run from the annotation backend and merges them into the collection.

See [this page](integrations__annotation.md#loading-annotations) for more information about using this method to import annotations that you have scheduled by calling `annotate()`.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **anno_key** â an annotation key

  * **dest_field** (_None_) â an optional name of a new destination field into which to load the annotations, or a dict mapping field names in the runâs label schema to new destination field names

  * **unexpected** (_"prompt"_) â 

how to deal with any unexpected labels that donât match the runâs label schema when importing. The supported values are:

    * `"prompt"`: present an interactive prompt to direct/discard unexpected labels

    * `"ignore"`: automatically ignore any unexpected labels

    * `"keep"`: automatically keep all unexpected labels in a field whose name matches the label type

    * `"return"`: return a dict containing all unexpected labels, or `None` if there arenât any

  * **cleanup** (_False_) â whether to delete any information regarding this run from the annotation backend after loading the annotations

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â keyword arguments for the runâs [`fiftyone.core.annotation.AnnotationMethodConfig.load_credentials()`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationMethodConfig.load_credentials "fiftyone.core.annotation.AnnotationMethodConfig.load_credentials") method



Returns:
    

`None`, unless `unexpected=="return"` and unexpected labels are found, in which case a dict containing the extra labels is returned

class fiftyone.utils.annotations.AnnotationBackendConfig(_name_ , _label_schema_ , _media_field ='filepath'_, _** kwargs_)#
    

Bases: [`AnnotationMethodConfig`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationMethodConfig "fiftyone.core.annotation.AnnotationMethodConfig")

Base class for configuring an `AnnotationBackend` instances.

Subclasses are free to define additional keyword arguments if they desire.

Parameters:
    

  * **name** â the name of the backend

  * **label_schema** â a dictionary containing the description of label fields, classes and attributes to annotate

  * **media_field** (_"filepath"_) â string field name containing the paths to media files on disk to upload

  * ****kwargs** â any leftover keyword arguments after subclasses have done their parsing




**Attributes:**

`method` | The name of the annotation backend.  
---|---  
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`run_cls` | The `BaseRun` class associated with this config.  
`type` | The type of run.  
  
**Methods:**

`load_credentials`(**kwargs) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
---|---  
`serialize`(*args,Â **kwargs) | Serializes the object into a dictionary.  
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
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property method#
    

The name of the annotation backend.

load_credentials(_** kwargs_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

serialize(_* args_, _** kwargs_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

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




class fiftyone.utils.annotations.AnnotationBackend(_* args_, _** kwargs_)#
    

Bases: [`AnnotationMethod`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationMethod "fiftyone.core.annotation.AnnotationMethod")

Base class for annotation backends.

Parameters:
    

**config** â an `AnnotationBackendConfig`

**Attributes:**

`supported_media_types` | The list of media types that this backend supports.  
---|---  
`supported_label_types` | The list of label types supported by the backend.  
`supported_scalar_types` | The list of scalar field types supported by the backend.  
`supported_attr_types` | The list of attribute types supported by the backend.  
`supports_clips_views` | Whether this backend supports annotating clips views.  
`supports_keyframes` | Whether this backend supports uploading only keyframes when editing existing video track annotations.  
`supports_video_sample_fields` | Whether this backend supports annotating video labels at a sample-level.  
`requires_label_schema` | Whether this backend requires a pre-defined label schema for its annotation runs.  
  
**Methods:**

`recommend_attr_tool`(name,Â value) | Recommends an attribute tool for an attribute with the given name and value.  
---|---  
`requires_attr_values`(attr_type) | Determines whether the list of possible values are required for attributes of the given type.  
`connect_to_api`() | Returns an API instance connected to the annotation backend.  
`use_api`(api) | Registers an API instance to use for subsequent operations.  
`upload_annotations`(samples,Â anno_key[,Â ...]) | Uploads the samples and relevant existing labels from the label schema to the annotation backend.  
`download_annotations`(results) | Downloads the annotations from the annotation backend for the given results.  
`get_fields`(samples,Â anno_key) | Gets the fields that were involved in the given run.  
`cleanup`(samples,Â key) | Cleans up the results of the run with the given key from the collection.  
`delete_run`(samples,Â key[,Â cleanup]) | Deletes the results associated with the given run key from the collection.  
`delete_runs`(samples[,Â cleanup]) | Deletes all runs from the collection.  
`ensure_requirements`() | Ensures that any necessary packages to execute this run are installed.  
`ensure_usage_requirements`() | Ensures that any necessary packages to use existing results for this run are installed.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
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
  
property supported_media_types#
    

The list of media types that this backend supports.

For example, CVAT supports `["image", "video"]`.

property supported_label_types#
    

The list of label types supported by the backend.

Backends may support any subset of the following label types:

  * `"classification"`

  * `"classifications"`

  * `"detection"`

  * `"detections"`

  * `"instance"`

  * `"instances"`

  * `"polyline"`

  * `"polylines"`

  * `"polygon"`

  * `"polygons"`

  * `"keypoint"`

  * `"keypoints"`

  * `"segmentation"`

  * `"scalar"`




property supported_scalar_types#
    

The list of scalar field types supported by the backend.

For example, CVAT supports the following types:

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")




property supported_attr_types#
    

The list of attribute types supported by the backend.

This list defines the valid string values for the `type` field of an attributes dict of the label schema provided to the backend.

For example, CVAT supports `["text", "select", "radio", "checkbox"]`.

property supports_clips_views#
    

Whether this backend supports annotating clips views.

property supports_keyframes#
    

Whether this backend supports uploading only keyframes when editing existing video track annotations.

property supports_video_sample_fields#
    

Whether this backend supports annotating video labels at a sample-level.

property requires_label_schema#
    

Whether this backend requires a pre-defined label schema for its annotation runs.

recommend_attr_tool(_name_ , _value_)#
    

Recommends an attribute tool for an attribute with the given name and value.

For example, a backend may recommend a tool as follows for a boolean value:
    
    
    {
        "type": "radio",
        "values": [False, True],
    }
    

or a tool as follows for a generic value:
    
    
    {"type": "text"}
    

Parameters:
    

  * **name** â the name of the attribute

  * **value** â the attribute value, which may be `None`



Returns:
    

an attribute type dict

requires_attr_values(_attr_type_)#
    

Determines whether the list of possible values are required for attributes of the given type.

Parameters:
    

**attr_type** â the attribute type string

Returns:
    

True/False

connect_to_api()#
    

Returns an API instance connected to the annotation backend.

Existing API instances are reused, if available.

Some annotation backends may not expose this functionality.

Returns:
    

an `AnnotationAPI`, or `None` if the backend does not expose an API

use_api(_api_)#
    

Registers an API instance to use for subsequent operations.

Parameters:
    

**api** â an `AnnotationAPI`

upload_annotations(_samples_ , _anno_key_ , _launch_editor =False_)#
    

Uploads the samples and relevant existing labels from the label schema to the annotation backend.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **anno_key** â the annotation key

  * **launch_editor** (_False_) â whether to launch the annotation backendâs editor after uploading the samples



Returns:
    

an `AnnotationResults`

download_annotations(_results_)#
    

Downloads the annotations from the annotation backend for the given results.

The returned labels should be represented as either scalar values or [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances.

For image datasets, the return dictionary should have the following nested structure:
    
    
    # Scalar fields
    results[label_type][sample_id] = scalar
    
    # Label fields
    results[label_type][sample_id][label_id] = label
    

For video datasets, the returned labels dictionary should have the following nested structure:
    
    
    # Scalar fields
    results[label_type][sample_id][frame_id] = scalar
    
    # Label fields
    results[label_type][sample_id][frame_id][label_id] = label
    

The valid values for `label_type` are:

  * âclassificationsâ: single or multilabel classifications

  * âdetectionsâ: detections or instance segmentations

  * âpolylinesâ: polygons or polylines

  * âsegmentationâ: semantic segmentations

  * âscalarâ: scalar values




Parameters:
    

**results** â an `AnnotationResults`

Returns:
    

the labels results dict

get_fields(_samples_ , _anno_key_)#
    

Gets the fields that were involved in the given run.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

a list of fields

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

class fiftyone.utils.annotations.AnnotationResults(_samples_ , _config_ , _anno_key_ , _id_map_ , _backend =None_)#
    

Bases: [`AnnotationResults`](api__fiftyone.core.annotation.md#fiftyone.core.annotation.AnnotationResults "fiftyone.core.annotation.AnnotationResults")

Base class for storing the intermediate results of an annotation run that has been initiated and is waiting for its results to be merged back into the FiftyOne dataset.

The `id_map` dictionary must record the IDs of any **existing labels** that are being edited by the annotation run. Any new label fields do not need to have keys in this dictionary.

For image datasets, `id_map` should have the following format:
    
    
    {
        "<label-field>": {
            "<sample-id>": "label-id" or ["label-id", ...],
            ...
        },
        ...
    }
    

For video datasets, `id_map` should have the following format:
    
    
    {
        "<label-field>": {
            "<sample-id>": {
                "<frame-id>": label-id" or ["label-id", ...],
                ...
            },
            ...
        },
        ...
    }
    

When editing scalar fields, set the dictionary values corresponding to uploaded scalars to `True` (since scalars do not have IDs).

If a particular sample or frame was included in the annotation run but no labels/scalars were uploaded for editing, the corresponding entry in `id_map` can be either missing or have a value of `None`.

Note

This class is serialized for storage in the database by calling `serialize()`.

Any public attributes of this class are included in the representation generated by `serialize()`, so they must be JSON serializable.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **config** â an `AnnotationBackendConfig`

  * **anno_key** â the annotation key

  * **id_map** â a dictionary recording the existing label IDs, in the format described above

  * **backend** (_None_) â an `AnnotationBackend`




**Methods:**

`connect_to_api`() | Returns an API instance connected to the annotation backend.  
---|---  
`use_api`(api) | Registers an API instance to use for subsequent operations.  
`launch_editor`() | Launches the annotation backend's editor for these results.  
`cleanup`() | Deletes all information for this run from the annotation backend.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
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
  
connect_to_api()#
    

Returns an API instance connected to the annotation backend.

Existing API instances are reused, if available.

Some annotation backends may not expose this functionality.

Returns:
    

an `AnnotationAPI`, or `None` if the backend does not expose an API

use_api(_api_)#
    

Registers an API instance to use for subsequent operations.

Parameters:
    

**api** â an `AnnotationAPI`

launch_editor()#
    

Launches the annotation backendâs editor for these results.

cleanup()#
    

Deletes all information for this run from the annotation backend.

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




class fiftyone.utils.annotations.AnnotationAPI#
    

Bases: `object`

Base class for APIs that connect to annotation backends.

**Methods:**

`close`() | Closes the API session.  
---|---  
  
close()#
    

Closes the API session.

class fiftyone.utils.annotations.DrawConfig(_d_)#
    

Bases: `AnnotationConfig`

Configuration class that controls the look-and-feel of the annotations rendered on images/videos.

Parameters:
    

  * **show_frame_attr_names** â (True) whether to render video/frame attribute names, if available

  * **show_frame_attr_confidences** â (False) whether to render video/frame attribute confidences, if available

  * **frame_attrs_box_gap** â (â1%â) the gap between the frame attributes box and the upper left corner of the image. This value is parsed by `eta.core.image.Width(frame_attrs_box_gap)`

  * **show_object_boxes** â (True) whether to render object bounding boxes, if available. If this is `False`, labels, confidences, attributes, etc. are also hidden

  * **show_object_names** â (True) whether to render object names, if available

  * **show_object_labels** â (True) whether to render object labels, if available

  * **show_object_attrs** â (True) whether to render object attributes, if available

  * **show_object_confidences** â (False) whether to render object label confidences, if available

  * **per_object_name_colors** â (True) whether to render boxes for objects with different names in different colors

  * **per_object_label_colors** â (True) whether to render boxes for objects with different labels in different colors

  * **per_object_index_colors** â (True) whether to render boxes for objects with different indexes in different colors

  * **show_object_attr_names** â (True) whether to render object attribute names, if available

  * **show_object_attr_confidences** â (False) whether to render object attribute confidences, if available

  * **show_object_indices** â (True) whether to render object indices, if available

  * **show_object_masks** â (True) whether to render object segmentation masks, if available

  * **occluded_object_attr** â (âoccludedâ) the name of the boolean attribute indicating whether an object is occluded

  * **hide_occluded_objects** â (False) whether to hide objects when they are occluded

  * **show_event_boxes** â (True) whether to render event bounding boxes, if available. If this is `False`, all attributes, confidences, etc. are also hidden

  * **show_event_labels** â (True) whether to render event labels, if available

  * **show_event_attrs** â (True) whether to render event attributes, if available

  * **show_event_names** â (True) whether to render event names, if available

  * **show_event_confidences** â (False) whether to render event label confidences, if available

  * **per_event_name_colors** â (True) whether to render boxes for events with different names in different colors

  * **per_event_label_colors** â (True) whether to render boxes for events with different labels in different colors

  * **per_event_index_colors** â (True) whether to render boxes for events with different indexes in different colors

  * **show_event_attr_names** â (True) whether to render event attribute names, if available

  * **show_event_attr_confidences** â (False) whether to render event attribute confidences, if available

  * **show_event_indices** â (True) whether to render event indices, if available. By default, this is `True`

  * **show_event_masks** â (True) whether to render event segmentation masks, if available

  * **show_event_label_on_objects** â (True) whether to render event labels as attributes on objects that belong to events

  * **show_event_objects_in_same_color** â (True) whether to render objects that belong to events in the same color as their parent event

  * **occluded_event_attr** â (âoccludedâ) the name of the boolean attribute indicating whether an event is occluded

  * **hide_occluded_events** â (False) whether to hide events when they are occluded

  * **bbox_alpha** â (0.75) the transparency of bounding boxes

  * **bbox_label_text_pad_pixels** â (2) the padding, in pixels, around the text in bounding box labels

  * **bbox_linewidth** â 
    3. the linewidth, in pixels, of bounding boxes

  * **mask_border_thickness** â (2) the thickness, in pixels, to use when drawing the borders of segmentation masks

  * **mask_fill_alpha** â (0.7) the transparency of segmentation masks

  * **show_frame_mask_semantics** â (True) whether to render semantic labels for frame mask regions, when mask indexes are available

  * **attrs_box_render_method** â (âpanelâ) the method used to render object attributes

  * **attrs_box_bg_color** â (â#000000â) the background color for attributes boxes

  * **attrs_box_bg_alpha** â (0.5) the transparency of attribute panel boxes

  * **attrs_box_text_pad_pixels** â (5) the padding, in pixels, around the text in attribute boxes

  * **attrs_box_text_line_spacing_pixels** â (1) the padding, in pixels, between each line of text in attribute boxes

  * **show_keypoints_names** â (False) whether to render keypoints names, if available

  * **show_keypoints_labels** â (False) whether to render keypoints labels, if available

  * **show_keypoints_attrs** â (False) whether to render keypoints attributes, if available

  * **show_keypoints_attr_names** â (False) whether to render keypoint attribute names, if available

  * **show_keypoints_attr_confidences** â (False) whether to render keypoint attribute confidences, if available

  * **per_keypoints_name_colors** â (True) whether to render keypoints with different names in different colors

  * **per_keypoints_label_colors** â (True) whether to render keypoints with different labels in different colors

  * **keypoints_size** â 
    6. the size to render keypoints

  * **keypoints_alpha** â (0.75) the transparency of keypoints

  * **keypoints_skeleton** â 

(None) an optional keypoint skeleton dictionary of the following form:
        
        {
            "labels": [
                "left hand" "left shoulder", "right shoulder",
                "right hand", "left eye", "right eye", "mouth"
            ],
            "edges": [[0, 1, 2, 3], [4, 5, 6]],
        }
        

  * **draw_keypoints_skeletons** â (True) whether to render keypoint skeletons, if available

  * **keypoints_edge_linewidth** (_2_) â the linewidth, in pixels, of keypoint skeleton edges

  * **keypoints_edge_alpha** â (0.75) the transparency of keypoint skeleton edges

  * **show_polyline_names** â (True) whether to render polyline names, if available

  * **show_polyline_labels** â (True) whether to render polyline labels, if available

  * **show_polyline_attrs** â (True) whether to render polyline attributes, if available

  * **show_polyline_attr_names** â (True) whether to render polyline attribute names, if available

  * **show_polyline_attr_confidences** â (False) whether to render polyline attribute confidences, if available

  * **hide_non_filled_polyline_annos** â (False) whether to override other settings and hide the annotation panels for non-filled polylines (those with `filled == False`)

  * **per_polyline_name_colors** â (True) whether to render polylines with different names in different colors

  * **per_polyline_label_colors** â (True) whether to render polylines with different labels in different colors

  * **polyline_alpha** â (0.75) the transparency of polylines

  * **polyline_linewidth** â (3) the linewidth, in pixels, of non-filled polylines

  * **fill_polylines** â (True) whether to draw polylines as filled, when possible

  * **show_all_names** â (False) whether to render all names, if available. If set to `True`, this overrides all other name flags

  * **hide_all_names** â (False) whether to hide all names, if available. If set to `True`, this overrides all other name flags

  * **show_name_only_titles** â (False) whether to render titles that only contain the `name` of the entity (i.e., no label, confidence, index, etc)

  * **show_all_confidences** â (False) whether to render all confidences, if available. If set to `True`, this overrides all other confidence flags

  * **hide_all_confidences** â (False) whether to hide all confidences, if available. If set to `True`, this overrides all other confidence flags

  * **labels_whitelist** â (None) an optional whitelist of labels (of any kind). If provided, only entities whose `label` is in this list will be rendered

  * **labels_blacklist** â (None) an optional list of labels (of any kind) to not render

  * **attr_names_blacklist** â (None) an optional list of attribute names (of any kind) to not render

  * **attr_values_blacklist** â (None) an optional list of attribute values (of any kind) to not render

  * **hide_false_boolean_attrs** â (False) whether to hide attributes (of any kind) when they are `False`

  * **confidence_scaled_alpha** â (False) whether to scale alpha values of objects and events based on their associated confidences

  * **colormap_config** â (None) the `eta.core.annotations.ColormapConfig` to use to select colors for objects/event boxes

  * **text_color** â (â#FFFFFFâ) the annotation text color

  * **font_path** â (`eta.core.constants.DEFAULT_FONT_PATH`) the path to the `PIL.ImageFont` to use

  * **font_size** â 
    16. the font size to use

  * **scale_by_media_height** â (True) whether to scale font sizes and linewidths according to the height of the media (relative to a height of 720 pixels)

  * **add_logo** â (False) whether to add a logo to the frames

  * **logo_config** â (None) the `eta.core.logo.LogoConfig` describing the logo to use




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
`set_media_size`([frame_size,Â shape,Â img]) | Sets the size of the media to the given value.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`colormap` |   
---|---  
`font` |   
`linewidth` |   
`logo` |   
`media_height` |   
`scale_factor` |   
  
attributes()#
    

Returns a list of class attributes to be serialized.

This method is called internally by serialize() to determine the class attributes to serialize.

Subclasses can override this method, but, by default, all attributes in vars(self) are returned, minus private attributes, i.e., those starting with â_â. The order of the attributes in this list is preserved when serializing objects, so a common pattern is for subclasses to override this method if they want their JSON files to be organized in a particular way.

Returns:
    

a list of class attributes to be serialized

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property colormap#
    

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

property font#
    

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

property linewidth#
    

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property logo#
    

property media_height#
    

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

property scale_factor#
    

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

set_media_size(_frame_size =None_, _shape =None_, _img =None_)#
    

Sets the size of the media to the given value. This allows for optimizing font sizes, linewidths, and logo resolutions to suit the dimensions of the media being annotated.

Exactly _one_ keyword argument must be provided.

Parameters:
    

  * **frame_size** â the (width, height) of the image/video frame

  * **shape** â the (height, width, â¦) of the image/video frame, e.g. from img.shape

  * **img** â an example image/video frame




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




fiftyone.utils.annotations.draw_labeled_images(_samples_ , _output_dir_ , _rel_dir =None_, _label_fields =None_, _config =None_, _progress =None_, _** kwargs_)#
    

Renders annotated versions of the images in the collection with the specified label data overlaid to the given directory.

The filenames of the sample images are maintained, unless a name conflict would occur in `output_dir`, in which case an index of the form `"-%d" % count` is appended to the base filename.

The images are written in format `fo.config.default_image_ext`.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **output_dir** â the directory to write the annotated images

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each annotated image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **label_fields** (_None_) â a label field or list of label fields to render. If omitted, all compatible fields are rendered

  * **config** (_None_) â an optional `DrawConfig` configuring how to draw the labels

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments specifying parameters of the default `DrawConfig` to override



Returns:
    

the list of paths to the labeled images

fiftyone.utils.annotations.draw_labeled_image(_sample_ , _outpath_ , _label_fields =None_, _config =None_, _** kwargs_)#
    

Renders an annotated version of the sampleâs image with the specified label data overlaid to disk.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **outpath** â the path to write the annotated image

  * **label_fields** (_None_) â a label field or list of label fields to render. If omitted, all compatible fields are rendered

  * **config** (_None_) â an optional `DrawConfig` configuring how to draw the labels

  * ****kwargs** â optional keyword arguments specifying parameters of the default `DrawConfig` to override




fiftyone.utils.annotations.draw_labeled_videos(_samples_ , _output_dir_ , _rel_dir =None_, _label_fields =None_, _config =None_, _progress =None_, _** kwargs_)#
    

Renders annotated versions of the videos in the collection with the specified label data overlaid to the given directory.

The filenames of the videos are maintained, unless a name conflict would occur in `output_dir`, in which case an index of the form `"-%d" % count` is appended to the base filename.

The videos are written in format `fo.config.default_video_ext`.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **output_dir** â the directory to write the annotated videos

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each annotated video. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **label_fields** (_None_) â a label field or list of label fields to render. If omitted, all compatible fields are rendered

  * **config** (_None_) â an optional `DrawConfig` configuring how to draw the labels

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments specifying parameters of the default `DrawConfig` to override



Returns:
    

the list of paths to the labeled videos

fiftyone.utils.annotations.draw_labeled_video(_sample_ , _outpath_ , _support =None_, _label_fields =None_, _config =None_, _** kwargs_)#
    

Renders an annotated version of the sampleâs video with the specified label data overlaid to disk.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **outpath** â the path to write the annotated image

  * **support** (_None_) â an optional `[first, last]` range of frames to render

  * **label_fields** (_None_) â a label field or list of label fields to render. If omitted, all compatible fields are rendered

  * **config** (_None_) â an optional `DrawConfig` configuring how to draw the labels

  * ****kwargs** â optional keyword arguments specifying parameters of the default `DrawConfig` to override




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
