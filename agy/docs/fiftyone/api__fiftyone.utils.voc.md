---
source_url: https://docs.voxel51.com/api/fiftyone.utils.voc.html
---

# fiftyone.utils.voc#

Utilities for working with datasets in [VOC format](http://host.robots.ox.ac.uk/pascal/VOC).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`VOCDetectionDatasetImporter`([dataset_dir,Â ...]) | Importer for VOC detection datasets stored on disk.  
---|---  
`VOCDetectionDatasetExporter`([export_dir,Â ...]) | Exporter that writes VOC detection datasets to disk.  
`VOCAnnotation`([path,Â folder,Â filename,Â ...]) | Class representing a VOC annotations file.  
`VOCObject`(name,Â bndbox,Â **attributes) | An object in VOC detection format.  
`VOCBoundingBox`(xmin,Â ymin,Â xmax,Â ymax) | A bounding box in VOC detection format.  
`VOCAnnotationWriter`() | Class for writing annotations in VOC format.  
  
**Functions:**

`load_voc_detection_annotations`(xml_path) | Loads the VOC detection annotations from the given XML file.  
---|---  
  
class fiftyone.utils.voc.VOCDetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _include_all_data =False_, _extra_attrs =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for VOC detection datasets stored on disk.

See [this page](user_guide__import_datasets.md#vocdetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping filenames to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location of the labels in `dataset_dir`

    * an absolute folder path to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels/`

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with label entries (False)

  * **extra_attrs** (_True_) â 

whether to load extra annotation attributes onto the imported labels. Supported values are:

    * `True`: load all extra attributes found

    * `False`: do not load extra attributes

    * a name or list of names of specific attributes to load

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
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

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

class fiftyone.utils.voc.VOCDetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _include_paths =True_, _image_format =None_, _extra_attrs =True_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes VOC detection datasets to disk.

See [this page](user_guide__export_datasets.md#vocdetectiondataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `data_path` and `labels_path` are absolute paths

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a JSON filename like `"data.json"` specifying the filename of the manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, the default value of this parameter will be chosen based on the value of the `export_media` parameter

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the labels

    * an absolute folder path to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be exported into `export_dir` using the default folder name

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` and `labels_path` to generate output paths for each exported image and labels file. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **include_paths** (_True_) â whether to include the absolute paths to the images in the `<path>` elements of the exported XML

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **extra_attrs** (_True_) â 

whether to include extra object attributes in the exported labels. Supported values are:

    * `True`: export all extra attributes found

    * `False`: do not export extra attributes

    * a name or list of names of specific attributes to export




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â detections[,Â ...]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_image_or_path_ , _detections_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

  * **metadata** (_None_) â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the sample. Only required when `requires_image_metadata()` is `True`




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.voc.VOCAnnotation(_path =None_, _folder =None_, _filename =None_, _segmented =None_, _metadata =None_, _objects =None_)#
    

Bases: `object`

Class representing a VOC annotations file.

Parameters:
    

  * **path** (_None_) â the path to the image

  * **folder** (_None_) â the name of the folder containing the image

  * **filename** (_None_) â the image filename

  * **segmented** (_None_) â whether the objects are segmented

  * **metadata** (_None_) â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

  * **objects** (_None_) â a list of `VOCObject` instances




**Methods:**

`to_detections`([extra_attrs]) | Returns a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") representation of the objects in the annotation.  
---|---  
`from_labeled_image`(metadata,Â detections[,Â ...]) | Creates a `VOCAnnotation` instance for the given labeled image data.  
`from_xml`(xml_path) | Creates a `VOCAnnotation` instance from an XML annotations file.  
`from_dict`(d) | Creates a `VOCAnnotation` instance from a JSON dict representation.  
  
to_detections(_extra_attrs =True_)#
    

Returns a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") representation of the objects in the annotation.

Parameters:
    

**extra_attrs** (_True_) â 

whether to load extra annotation attributes onto the imported labels. Supported values are:

  * `True`: load all extra attributes found

  * `False`: do not load extra attributes

  * a name or list of names of specific attributes to load




Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

classmethod from_labeled_image(_metadata_ , _detections_ , _path =None_, _filename =None_, _extra_attrs =True_)#
    

Creates a `VOCAnnotation` instance for the given labeled image data.

Parameters:
    

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the image

  * **detections** â a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * **path** (_None_) â the absolute path to the image

  * **filename** (_None_) â the filename of the image

  * **extra_attrs** (_True_) â 

whether to include extra object attributes. Supported values are:

    * `True`: include all extra attributes found

    * `False`: do not include extra attributes

    * a name or list of names of specific attributes to include



Returns:
    

a `VOCAnnotation`

classmethod from_xml(_xml_path_)#
    

Creates a `VOCAnnotation` instance from an XML annotations file.

Parameters:
    

**xml_path** â the path to the XML file

Returns:
    

a `VOCAnnotation`

classmethod from_dict(_d_)#
    

Creates a `VOCAnnotation` instance from a JSON dict representation.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `VOCAnnotation`

class fiftyone.utils.voc.VOCObject(_name_ , _bndbox_ , _** attributes_)#
    

Bases: `object`

An object in VOC detection format.

Parameters:
    

  * **name** â the object label

  * **bndbox** â a `VOCBoundingBox`

  * ****attributes** â additional custom attributes




**Methods:**

`from_annotation_dict`(d) | Creates a `VOCObject` from a VOC annotation dict.  
---|---  
`from_detection`(detection,Â metadata[,Â ...]) | Creates a `VOCObject` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
`to_detection`(frame_size[,Â extra_attrs]) | Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the object.  
  
classmethod from_annotation_dict(_d_)#
    

Creates a `VOCObject` from a VOC annotation dict.

Parameters:
    

**d** â an annotation dict

Returns:
    

a `VOCObject`

classmethod from_detection(_detection_ , _metadata_ , _extra_attrs =True_)#
    

Creates a `VOCObject` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Parameters:
    

  * **detection** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the image

  * **extra_attrs** (_True_) â 

whether to include extra object attributes. Supported values are:

    * `True`: include all extra attributes found

    * `False`: do not include extra attributes

    * a name or list of names of specific attributes to include



Returns:
    

a `VOCObject`

to_detection(_frame_size_ , _extra_attrs =True_)#
    

Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the object.

Parameters:
    

  * **frame_size** â the `(width, height)` of the image

  * **extra_attrs** (_True_) â 

whether to include extra annotation attributes on the object. Supported values are:

    * `True`: include all extra attributes found

    * `False`: do not include extra attributes

    * a name or list of names of specific attributes to include



Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

class fiftyone.utils.voc.VOCBoundingBox(_xmin_ , _ymin_ , _xmax_ , _ymax_)#
    

Bases: `object`

A bounding box in VOC detection format.

Parameters:
    

  * **xmin** â the top-left x coordinate

  * **ymin** â the top-left y coordinate

  * **xmax** â the bottom-right x coordinate

  * **ymax** â the bottom-right y coordinate




**Methods:**

`from_bndbox_dict`(d) | Creates a `VOCBoundingBox` from a `bndbox` dict.  
---|---  
`from_detection_format`(bounding_box,Â frame_size) | Creates a `VOCBoundingBox` from a bounding box stored in [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") format.  
`to_detection_format`(frame_size) | Returns a representation of the bounding box suitable for storing in the `bounding_box` field of a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
  
classmethod from_bndbox_dict(_d_)#
    

Creates a `VOCBoundingBox` from a `bndbox` dict.

Parameters:
    

**d** â a `bndbox` dict

Returns:
    

a `VOCBoundingBox`

classmethod from_detection_format(_bounding_box_ , _frame_size_)#
    

Creates a `VOCBoundingBox` from a bounding box stored in [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") format.

Parameters:
    

  * **bounding_box** â `[x-top-left, y-top-left, width, height]`

  * **frame_size** â the `(width, height)` of the image



Returns:
    

a `VOCBoundingBox`

to_detection_format(_frame_size_)#
    

Returns a representation of the bounding box suitable for storing in the `bounding_box` field of a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Parameters:
    

**frame_size** â the `(width, height)` of the image

Returns:
    

`[x-top-left, y-top-left, width, height]`

class fiftyone.utils.voc.VOCAnnotationWriter#
    

Bases: `object`

Class for writing annotations in VOC format.

See [this page](user_guide__export_datasets.md#vocdetectiondataset-export) for format details.

**Methods:**

`write`(annotation,Â xml_path) | Writes the annotations to disk.  
---|---  
  
write(_annotation_ , _xml_path_)#
    

Writes the annotations to disk.

Parameters:
    

  * **annotation** â a `VOCAnnotation` instance

  * **xml_path** â the path to write the annotation XML file




fiftyone.utils.voc.load_voc_detection_annotations(_xml_path_)#
    

Loads the VOC detection annotations from the given XML file.

See [this page](user_guide__import_datasets.md#vocdetectiondataset-import) for format details.

Parameters:
    

**xml_path** â the path to the annotations XML file

Returns:
    

a `VOCAnnotation` instance

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
