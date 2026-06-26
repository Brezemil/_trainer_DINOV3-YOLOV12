---
source_url: https://docs.voxel51.com/api/fiftyone.utils.bdd.html
---

# fiftyone.utils.bdd#

Utilities for working with datasets in [Berkeley DeepDrive (BDD) format](http://bdd-data.berkeley.edu).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`BDDDatasetImporter`([dataset_dir,Â data_path,Â ...]) | Importer for BDD datasets stored on disk.  
---|---  
`BDDDatasetExporter`([export_dir,Â data_path,Â ...]) | Exporter that writes BDD datasets to disk.  
  
**Functions:**

`load_bdd_annotations`(json_path) | Loads the BDD annotations from the given JSON file.  
---|---  
`parse_bdd100k_dataset`(source_dir,Â dataset_dir) | Parses the raw BDD100K download files in the specified directory into per-split directories in BDD format.  
  
class fiftyone.utils.bdd.BDDDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _include_all_data =False_, _extra_attrs =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for BDD datasets stored on disk.

See [this page](user_guide__import_datasets.md#bdddataset-import) for format details.

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

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.json`

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

class fiftyone.utils.bdd.BDDDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _image_format =None_, _extra_attrs =True_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes BDD datasets to disk.

See [this page](user_guide__export_datasets.md#bdddataset-export) for format details.

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

    * a filename like `"labels.json"` specifying the location in `export_dir` in which to export the labels

    * an absolute filepath to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be exported into `export_dir` using the default filename

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the images in the exported labels

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
`export_sample`(image_or_path,Â labels[,Â metadata]) | Exports the given sample to the dataset.  
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

export_sample(_image_or_path_ , _labels_ , _metadata =None_)#
    

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

fiftyone.utils.bdd.load_bdd_annotations(_json_path_)#
    

Loads the BDD annotations from the given JSON file.

See [this page](user_guide__import_datasets.md#bdddataset-import) for format details.

Parameters:
    

**json_path** â the path to the annotations JSON file

Returns:
    

a dict mapping filenames to BDD annotation dicts

fiftyone.utils.bdd.parse_bdd100k_dataset(_source_dir_ , _dataset_dir_ , _copy_files =True_, _overwrite =False_)#
    

Parses the raw BDD100K download files in the specified directory into per-split directories in BDD format.

This function assumes that the input `source_dir` contains the following contents:
    
    
    source_dir/
        labels/
            bdd100k_labels_images_train.json
            bdd100k_labels_images_val.json
        images/
            100k/
                train/
                test/
                val/
        ...
    

and will populate `dataset_dir` as follows:
    
    
    dataset_dir/
        train/
            data/
            labels.json
        validation/
            data/
            labels.json
        test/
            data/
    

Parameters:
    

  * **source_dir** â the source directory containing the manually downloaded BDD100K files

  * **dataset_dir** â the directory to construct the output split directories

  * **copy_files** (_True_) â whether to move (False) or create copies (True) of the source files when populating `dataset_dir`

  * **overwrite** (_False_) â whether to overwrite existing files/directories in the output location, if they exist



Raises:
    

**OSError** â if any required source files are not present

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
