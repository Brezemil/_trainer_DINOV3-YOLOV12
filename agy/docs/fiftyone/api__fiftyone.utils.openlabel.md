---
source_url: https://docs.voxel51.com/api/fiftyone.utils.openlabel.html
---

# fiftyone.utils.openlabel#

Utilities for working with datasets in [OpenLABEL format](https://www.asam.net/index.php?eID=dumpFile&t=f&f=3876&token=413e8c85031ae64cc35cf42d0768627514868b2f).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SegmentationType`(value) | The FiftyOne label type used to store segmentations  
---|---  
`OpenLABELImageDatasetImporter`([dataset_dir,Â ...]) | Importer for OpenLABEL image datasets stored on disk.  
`OpenLABELVideoDatasetImporter`([dataset_dir,Â ...]) | Importer for OpenLABEL video datasets stored on disk.  
`OpenLABELAnnotations`() | Annotations parsed from OpenLABEL format able to be converted to FiftyOne labels.  
`OpenLABELStreamInfos`([infos]) | A collection of multiple `OpenLABELStreamInfo` objects.  
`OpenLABELStreamInfo`([frame_numbers,Â stream,Â ...]) | Information about a stream used to gather specific objects for a media file.  
`OpenLABELGroup`() | A utility for parsing groups of OpenLABEL elements  
`OpenLABELObjects`() | A collection of `OpenLABELObject` and corresponding utility methods.  
`OpenLABELStreams`() | A collection of OpenLABEL streams.  
`AttributeParser`() | Methods used to parse attributes from OpenLABEL annotations.  
`OpenLABELShape`(coords[,Â attributes,Â stream]) | A single OpenLABEL shape like a bounding box or polygon.  
`OpenLABELBBox`(coords[,Â attributes,Â stream]) | An OpenLABEL bounding box.  
`OpenLABELPoly2D`(coords[,Â attributes,Â stream]) | An OpenLABEL polyline.  
`OpenLABELPoint`(coords[,Â attributes,Â stream]) | An OpenLABEL keypoint.  
`OpenLABELShapes`([shapes,Â attributes,Â stream]) | A collection of OpenLABEL shapes.  
`OpenLABELStream`(name[,Â type,Â properties,Â ...]) | An OpenLABEL stream corresponding to one uri or file_id.  
`OpenLABELMetadata`(metadata_dict) | A parser and storage for OpenLABEL metadata.  
`OpenLABELObject`(key[,Â name,Â type,Â bboxes,Â ...]) | An object parsed from OpenLABEL labels.  
  
class fiftyone.utils.openlabel.SegmentationType(_value_)#
    

Bases: `Enum`

The FiftyOne label type used to store segmentations

**Attributes:**

`INSTANCE` |   
---|---  
`POLYLINE` |   
`SEMANTIC` |   
  
INSTANCE = 1#
    

POLYLINE = 2#
    

SEMANTIC = 3#
    

class fiftyone.utils.openlabel.OpenLABELImageDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _label_types =None_, _use_polylines =False_, _shuffle =False_, _seed =None_, _max_samples =None_, _skeleton =None_, _skeleton_key =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for OpenLABEL image datasets stored on disk.

See [this page](user_guide__import_datasets.md#openlabelimagedataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping file_ids to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * a folder name like `"labels"` or `"labels/"` specifying a subfolder of `dataset_dir` where the multiple label files reside

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to looking for `labels.json` and `label/`

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations", "keypoints")`. By default, all labels are loaded

  * **use_polylines** (_False_) â whether to represent segmentations as [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances rather than [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with dense masks

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") to reference when loading keypoints

  * **skeleton_key** (_None_) â the key in the OpenLABEL annotations pointing to the label of each keypoint matching the labels defined in the given `skeleton`




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

class fiftyone.utils.openlabel.OpenLABELVideoDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _label_types =None_, _use_polylines =False_, _shuffle =False_, _seed =None_, _max_samples =None_, _skeleton =None_, _skeleton_key =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for OpenLABEL video datasets stored on disk.

See [this page](user_guide__import_datasets.md#openlabelvideodataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping file_ids to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * a folder name like `"labels"` or `"labels/"` specifying a subfolder of `dataset_dir` where the multiple label files reside

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to looking for `labels.json` and `labels/`

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations", "keypoints")`. By default, all labels are loaded

  * **use_polylines** (_False_) â whether to represent segmentations as [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances rather than [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with dense masks

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") to reference when loading keypoints

  * **skeleton_key** (_None_) â the key in the OpenLABEL annotations pointing to the label of each keypoint matching the labels defined in the given `skeleton`




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the sample-level labels that it may return




setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the importer makes no guarantees about the frame labels that it may return




class fiftyone.utils.openlabel.OpenLABELAnnotations#
    

Bases: `object`

Annotations parsed from OpenLABEL format able to be converted to FiftyOne labels.

**Methods:**

`parse_labels`(base_dir,Â labels_path) | Parses a single OpenLABEL labels file.  
---|---  
`get_dimensions`(file_id) | Get the width and height of a given URI or file id  
`get_labels`(uri,Â label_types,Â frame_size,Â ...) | Get the FiftyOne labels corresponding to the annotations of a given URI.  
  
parse_labels(_base_dir_ , _labels_path_)#
    

Parses a single OpenLABEL labels file.

Parameters:
    

  * **base_dir** â path to the directory containing the labels file

  * **labels_path** â path to the labels json file



Returns:
    

a list of potential file_ids that the parsed labels correspond to

get_dimensions(_file_id_)#
    

Get the width and height of a given URI or file id

Parameters:
    

**file_id** â the unique identifier to a media file

Returns:
    

(width, height) of the given file

get_labels(_uri_ , _label_types_ , _frame_size_ , _seg_type_ , _skeleton =None_, _skeleton_key =None_)#
    

Get the FiftyOne labels corresponding to the annotations of a given URI. The results are two dictionaries, sample- and frame-level, mapping field names to values and label objects.

Parameters:
    

  * **uri** â the unique identifier to a media file

  * **label_types** â a list of label types to load. The supported values are `("detections", "segmentations", "keypoints")`.

  * **frame_size** â the (width, height) tuple for the media frame

  * **seg_type** â the `SegmentationType` to use for segmentation annotations

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") to use as a reference when loading keypoints

  * **skeleton_key** (_None_) â the name of the field in the OpenLABEL annotations containing the labels of keypoints matching the labels of the given skeleton



Returns:
    

a dictionary of sample level fields and label objects and a dictionary of frame numbers to frame level fields and label objects

class fiftyone.utils.openlabel.OpenLABELStreamInfos(_infos =None_)#
    

Bases: `object`

A collection of multiple `OpenLABELStreamInfo` objects.

**Methods:**

`get_stream_attributes`([frame_number]) | Aggregates attributes from all streams in this collection.  
---|---  
  
**Attributes:**

`frame_numbers` | All frame numbers existing in the `OpenLABELStreamInfo` objects in this collection.  
---|---  
  
get_stream_attributes(_frame_number =None_)#
    

Aggregates attributes from all streams in this collection.

Parameters:
    

**frame_number** (_None_) â a specific frame number for which to get stream attributes

Returns:
    

a dictionary of attributes from all streams in this collection

property frame_numbers#
    

All frame numbers existing in the `OpenLABELStreamInfo` objects in this collection.

class fiftyone.utils.openlabel.OpenLABELStreamInfo(_frame_numbers =None_, _stream =None_, _label_file_id =None_, _is_sample_level =None_)#
    

Bases: `object`

Information about a stream used to gather specific objects for a media file.

Parameters:
    

  * **frame_numbers** (_None_) â frame numbers related to this stream info

  * **stream** (_None_) â an `OpenLABELStream`

  * **label_file_id** (_None_) â a label file id related to this stream info

  * **is_sample_level** (_None_) â whether this stream info corresponds to sample-level or frame-level




**Attributes:**

`is_streamless` | Whether there exists a stream corresponding to this info.  
---|---  
  
**Methods:**

`get_stream_attributes`() | Get a dictionary of attributes for the stream in this object.  
---|---  
  
property is_streamless#
    

Whether there exists a stream corresponding to this info.

get_stream_attributes()#
    

Get a dictionary of attributes for the stream in this object.

Returns:
    

a dictionary of attributes from the corresponding stream

class fiftyone.utils.openlabel.OpenLABELGroup#
    

Bases: `object`

A utility for parsing groups of OpenLABEL elements

class fiftyone.utils.openlabel.OpenLABELObjects#
    

Bases: `OpenLABELGroup`

A collection of `OpenLABELObject` and corresponding utility methods.

**Attributes:**

`streams` | Get streams corresponding to any object in this collection.  
---|---  
`all_objects` | A list of `OpenLABELObject` instances in this collection.  
  
**Methods:**

`parse_objects_dict`(objects_dict,Â label_file_id) | Parses the OpenLABEL annotations corresponding to a specific dictionary of objects.  
---|---  
`add_object`(obj_key,Â label_file_id,Â obj) | Adds an `OpenLABELObject` to this collection.  
`get_objects`(stream_infos) | Gets any objects that correspond to an info in the given stream infos.  
`to_labels`(frame_size,Â label_types,Â seg_type,Â ...) | Converts the stored `OpenLABELObject` to FiftyOne labels.  
  
property streams#
    

Get streams corresponding to any object in this collection.

property all_objects#
    

A list of `OpenLABELObject` instances in this collection.

parse_objects_dict(_objects_dict_ , _label_file_id_ , _frame_number =None_)#
    

Parses the OpenLABEL annotations corresponding to a specific dictionary of objects.

Parameters:
    

  * **objects_dict** â the dict of OpenLABEL object annotations

  * **label_file_id** â the name of the annotations file containing these objects

  * **frame_number** (_None_) â an optional frame that this `objects_dict` is in




add_object(_obj_key_ , _label_file_id_ , _obj_)#
    

Adds an `OpenLABELObject` to this collection.

Parameters:
    

  * **obj_key** â the name of the object in the OpenLABEL annotations

  * **label_file_id** â the filename of the annotations file containing this label

  * **obj** â the `OpenLABELObject` to add




get_objects(_stream_infos_)#
    

Gets any objects that correspond to an info in the given stream infos.

Parameters:
    

**stream_infos** â a `OpenLABELStreamInfos` used to get corresponding objects

Returns:
    

an `OpenLABELObjects` with objects that correspond to any of the given stream infos

to_labels(_frame_size_ , _label_types_ , _seg_type_ , _stream_infos_ , _skeleton =None_, _skeleton_key =None_)#
    

Converts the stored `OpenLABELObject` to FiftyOne labels.

Parameters:
    

  * **frame_size** â the size of the image frame in pixels (width, height)

  * **label_types** â a list of label types to load

  * **seg_type** â the `SegmentationType` to use to store segmentations

  * **stream_infos** â the `OpenLABELStreamInfos` containing sample-level attributes to parse into labels

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") to use when loading keypoint annotations

  * **skeleton_key** (_None_) â the name of the field in the OpenLABEL annotations containing the labels of keypoints matching the labels of the given skeleton



Returns:
    

a dictionary of sample level fields and label objects and a dictionary of frame numbers to frame level fields and label objects

class fiftyone.utils.openlabel.OpenLABELStreams#
    

Bases: `OpenLABELGroup`

A collection of OpenLABEL streams.

**Attributes:**

`uris` | All unique media file identifiers corresponding to streams in this collection.  
---|---  
  
**Methods:**

`parse_streams_dict`(streams_dict,Â label_file_id) | Parses the OpenLABEL annotations corresponding to a specific dictionary of streams.  
---|---  
`get_dimensions`(uri) | Get the width and height of a given URI or file id.  
`get_stream_info`(uri) | Get all stream infos, including stream and relevant frame numbers, for a given media file identifier.  
  
property uris#
    

All unique media file identifiers corresponding to streams in this collection.

parse_streams_dict(_streams_dict_ , _label_file_id_ , _frame_number =None_)#
    

Parses the OpenLABEL annotations corresponding to a specific dictionary of streams.

Parameters:
    

  * **streams_dict** â the dict of OpenLABEL stream annotations

  * **label_file_id** â the name of the annotations file containing these streams

  * **frame_number** (_None_) â an optional frame that this `streams_dict` is in




get_dimensions(_uri_)#
    

Get the width and height of a given URI or file id.

Parameters:
    

**file_id** â the unique identifier to a media file

Returns:
    

the `(width, height)` of the given file

get_stream_info(_uri_)#
    

Get all stream infos, including stream and relevant frame numbers, for a given media file identifier.

Parameters:
    

**uri** â the unique media file identifier for which to get all stream infos

Returns:
    

the `OpenLABELStreamInfos` corresponding to the given uri

class fiftyone.utils.openlabel.AttributeParser#
    

Bases: `object`

Methods used to parse attributes from OpenLABEL annotations.

class fiftyone.utils.openlabel.OpenLABELShape(_coords_ , _attributes =None_, _stream =None_)#
    

Bases: `AttributeParser`

A single OpenLABEL shape like a bounding box or polygon.

**Methods:**

`from_shape_dict`(d) | Constructs a shape from a dictionary of information.  
---|---  
  
classmethod from_shape_dict(_d_)#
    

Constructs a shape from a dictionary of information.

Parameters:
    

**d** â a dictionary containing information about a shape

Returns:
    

an `OpenLABELShape`

class fiftyone.utils.openlabel.OpenLABELBBox(_coords_ , _attributes =None_, _stream =None_)#
    

Bases: `OpenLABELShape`

An OpenLABEL bounding box.

**Methods:**

`to_label`(label,Â attributes,Â width,Â height) | Convert this shape to a FiftyOne label.  
---|---  
`from_shape_dict`(d) | Constructs a shape from a dictionary of information.  
  
to_label(_label_ , _attributes_ , _width_ , _height_)#
    

Convert this shape to a FiftyOne label.

Parameters:
    

  * **label** â the class label for this shape

  * **attributes** â a dictionary of attributes for this shape

  * **width** â the width of the frame in pixels

  * **height** â the height of the frame in pixels



Returns:
    

an [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

classmethod from_shape_dict(_d_)#
    

Constructs a shape from a dictionary of information.

Parameters:
    

**d** â a dictionary containing information about a shape

Returns:
    

an `OpenLABELShape`

class fiftyone.utils.openlabel.OpenLABELPoly2D(_coords_ , _attributes =None_, _stream =None_)#
    

Bases: `OpenLABELShape`

An OpenLABEL polyline.

**Methods:**

`to_label`(label,Â attributes,Â width,Â height) | Convert this shape to a FiftyOne label.  
---|---  
`from_shape_dict`(d) | Constructs a shape from a dictionary of information.  
  
to_label(_label_ , _attributes_ , _width_ , _height_)#
    

Convert this shape to a FiftyOne label.

Parameters:
    

  * **label** â the class label for this shape

  * **attributes** â a dictionary of attributes for this shape

  * **width** â the width of the frame in pixels

  * **height** â the height of the frame in pixels



Returns:
    

an [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

classmethod from_shape_dict(_d_)#
    

Constructs a shape from a dictionary of information.

Parameters:
    

**d** â a dictionary containing information about a shape

Returns:
    

an `OpenLABELShape`

class fiftyone.utils.openlabel.OpenLABELPoint(_coords_ , _attributes =None_, _stream =None_)#
    

Bases: `OpenLABELShape`

An OpenLABEL keypoint.

**Methods:**

`to_label`(label,Â attributes,Â width,Â height[,Â ...]) | Convert this shape to a FiftyOne label.  
---|---  
`from_shape_dict`(d) | Constructs a shape from a dictionary of information.  
  
to_label(_label_ , _attributes_ , _width_ , _height_ , _skeleton =None_, _skeleton_key =None_)#
    

Convert this shape to a FiftyOne label.

Parameters:
    

  * **label** â the class label for this shape

  * **attributes** â a dictionary of attributes for this shape

  * **width** â the width of the frame in pixels

  * **height** â the height of the frame in pixels

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") used to sort list attributes based on the labels in the skeleton. Used only if `skeleton_key` is provided

  * **skeleton_key** (_None_) â the string key into the attributes dictionary containing the label of each point, used to sort list attribute fields based on the labels in the skeleton. Used only if `skeleton` is provided



Returns:
    

an [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

classmethod from_shape_dict(_d_)#
    

Constructs a shape from a dictionary of information.

Parameters:
    

**d** â a dictionary containing information about a shape

Returns:
    

an `OpenLABELShape`

class fiftyone.utils.openlabel.OpenLABELShapes(_shapes =None_, _attributes =None_, _stream =None_)#
    

Bases: `AttributeParser`

A collection of OpenLABEL shapes.

**Attributes:**

`streams` | A list of streams corresponding to any object in this collection.  
---|---  
  
**Methods:**

`from_object_data_list`(shape_type,Â l[,Â ...]) | Construct an `OpenLABELShapes` from a list of shape dictionaries.  
---|---  
`merge_shapes`(shapes) | Merges another `OpenLABELShapes` into this one.  
`to_labels`(label,Â attributes,Â width,Â height) | Convert this shape to a FiftyOne label.  
  
property streams#
    

A list of streams corresponding to any object in this collection.

classmethod from_object_data_list(_shape_type_ , _l_ , _attributes =None_)#
    

Construct an `OpenLABELShapes` from a list of shape dictionaries.

Parameters:
    

  * **shape_type** â the type of the shape being loaded. Options are (`OpenLABELBBox`, `OpenLABELPoly2D`, `OpenLABELPoint`)

  * **l** â a list of shape dictionaries parsed from OpenLABEL object annotations

  * **attributes** (_None_) â a dictionary of attributes corresponding to all shapes in this collection



Returns:
    

a `OpenLABELShapes`

merge_shapes(_shapes_)#
    

Merges another `OpenLABELShapes` into this one.

Parameters:
    

**shapes** â another `OpenLABELShapes` to merge into this object

to_labels(_label_ , _attributes_ , _width_ , _height_ , _is_points =False_, _skeleton =None_, _skeleton_key =None_)#
    

Convert this shape to a FiftyOne label.

Parameters:
    

  * **label** â the class label for this shape

  * **attributes** â a dictionary of attributes for this shape

  * **width** â the width of the frame in pixels

  * **height** â the height of the frame in pixels

  * **is_points** (_False_) â whether the labels being converted are keypoints

  * **skeleton** (_None_) â a [`fiftyone.core.odm.dataset.KeypointSkeleton`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.KeypointSkeleton "fiftyone.core.odm.dataset.KeypointSkeleton") used to sort list attributes based on the labels in the skeleton. Used only if `is_points` and `skeleton_key` is provided

  * **skeleton_key** (_None_) â the string key into the attributes dictionary containing the label of each point, used to sort list attribute fields based on the labels in the skeleton. Used only if `is_points` and `skeleton` is provided



Returns:
    

an [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

class fiftyone.utils.openlabel.OpenLABELStream(_name_ , _type =None_, _properties =None_, _uris =None_, _other_attrs =None_)#
    

Bases: `object`

An OpenLABEL stream corresponding to one uri or file_id.

Parameters:
    

  * **name** (_None_) â the name of the stream

  * **type** (_None_) â the type of the stream

  * **description** (_None_) â a string description for this stream

  * **properties** (_None_) â a dict of properties for this stream

  * **uri** (_None_) â the uri or file_id of the media corresponding to this stream

  * **other_attrs** (_None_) â a dictionary of other attributes corresponding to this stream




**Methods:**

`update_dict`(d[,Â frame_number]) | Updates this stream with additional information.  
---|---  
`get_frame_numbers`(uri) | Get frame numbers corresponding to the given uri.  
`from_anno_dict`(stream_name,Â d,Â frame_number) | Create an OpenLABEL stream from the stream information dictionary.  
  
**Attributes:**

`uris` | Get uris corresponding to any stream in this collection.  
---|---  
  
update_dict(_d_ , _frame_number =None_)#
    

Updates this stream with additional information.

Parameters:
    

  * **d** â a dict containing additional stream information

  * **frame_number** (_None_) â the frame number from which this stream information dict was parsed, âNoneâ if from the top-level streams




property uris#
    

Get uris corresponding to any stream in this collection.

get_frame_numbers(_uri_)#
    

Get frame numbers corresponding to the given uri.

classmethod from_anno_dict(_stream_name_ , _d_ , _frame_number_)#
    

Create an OpenLABEL stream from the stream information dictionary.

Parameters:
    

  * **stream_name** â the name of the stream

  * **d** â a dict containing information about this stream

  * **frame_number** â the frame number from which this stream information dict was parsed, âNoneâ if from the top-level streams



Returns:
    

An `OpenLABELStream`

class fiftyone.utils.openlabel.OpenLABELMetadata(_metadata_dict_)#
    

Bases: `object`

A parser and storage for OpenLABEL metadata.

**Methods:**

`parse_potential_file_ids`() | Parses metadata for any fields that may correspond to a label-wide media file_id.  
---|---  
  
parse_potential_file_ids()#
    

Parses metadata for any fields that may correspond to a label-wide media file_id.

Returns:
    

a list of potential file_id strings

class fiftyone.utils.openlabel.OpenLABELObject(_key_ , _name =None_, _type =None_, _bboxes =None_, _segmentations =None_, _keypoints =None_, _stream =None_, _other_attrs =None_, _is_frame_level =False_)#
    

Bases: `AttributeParser`

An object parsed from OpenLABEL labels.

Parameters:
    

  * **key** â the OpenLABEL key string for this object

  * **name** (_None_) â the name string of the object

  * **type** (_None_) â the type string of the object

  * **bboxes** (_None_) â an :class`OpenLABELShapes` of bounding boxes for this object

  * **segmentations** (_None_) â an :class`OpenLABELShapes` of polygon segmentations for this object

  * **keyponts** (_None_) â an `OpenLABELShapes` of keypoints for this object

  * **stream** (_None_) â the `OpenLABELStream` this object corresponds to

  * **other_attrs** (_None_) â a dict of attributes and their values for this object

  * **is_frame_level** (_False_) â whether this object is sample-level or frame-level




**Attributes:**

`streams` | Get streams corresponding to this object.  
---|---  
`is_streamless` | Whether any streams are connected to this object or corresponding frame-level objects.  
  
**Methods:**

`filter_stream`(stream_info) | Filters this object to contain only frame labels specified in the given stream info  
---|---  
`to_detections`(frame_size) | Converts the bounding boxes in this object to [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") objects.  
`to_polylines`(frame_size) | Converts the segmentations in this object to [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") objects.  
`to_keypoints`(frame_size[,Â skeleton,Â ...]) | Converts the keypoints in this object to [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects.  
`from_anno_dict`(obj_key,Â d[,Â frame_number]) | Create an `OpenLABELObject` from the raw label dictionary.  
`update_dict`(d[,Â frame_number]) | Updates this `OpenLABELObject` given the raw label dictionary.  
  
property streams#
    

Get streams corresponding to this object.

property is_streamless#
    

Whether any streams are connected to this object or corresponding frame-level objects.

filter_stream(_stream_info_)#
    

Filters this object to contain only frame labels specified in the given stream info

Parameters:
    

**stream_info** â the `OpenLABELStreamInfo` to use to filter this object

Returns:
    

an `OpenLABELObject` containing only frames related to the given stream info

to_detections(_frame_size_)#
    

Converts the bounding boxes in this object to [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") objects.

Parameters:
    

**frame_size** â the size of the frame in pixels (width, height)

Returns:
    

a list of [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") objects for each bounding box in this object

to_polylines(_frame_size_)#
    

Converts the segmentations in this object to [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") objects.

Parameters:
    

**frame_size** â the size of the frame in pixels (width, height)

Returns:
    

a list of [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") objects for each polyline in this object

to_keypoints(_frame_size_ , _skeleton =None_, _skeleton_key =None_)#
    

Converts the keypoints in this object to [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects.

Parameters:
    

**frame_size** â the size of the frame in pixels (width, height)

Returns:
    

a list of [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects for each keypoint in this object

classmethod from_anno_dict(_obj_key_ , _d_ , _frame_number =None_)#
    

Create an `OpenLABELObject` from the raw label dictionary.

Parameters:
    

  * **anno_id** â id of the object

  * **d** â dict containing the information for this object



Returns:
    

a tuple containing the `OpenLABELObject` and the frame numbers the object corresponds to, if any.

update_dict(_d_ , _frame_number =None_)#
    

Updates this `OpenLABELObject` given the raw label dictionary.

Parameters:
    

**d** â dict containing the information for this object

Returns:
    

newly parsed frame numbers the object corresponds to, if any

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
