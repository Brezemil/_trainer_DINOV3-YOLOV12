---
source_url: https://docs.voxel51.com/api/fiftyone.utils.csv.html
---

# fiftyone.utils.csv#

CSV utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`CSVDatasetImporter`([dataset_dir,Â data_path,Â ...]) | A flexible CSV importer that represents slice(s) of field values of a dataset as columns of a CSV file.  
---|---  
`CSVDatasetExporter`([export_dir,Â data_path,Â ...]) | A flexible CSV exporter that represents slice(s) of field values of a dataset as columns of a CSV file.  
  
class fiftyone.utils.csv.CSVDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _media_field ='filepath'_, _fields =None_, _skip_missing_media =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`GenericSampleDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter "fiftyone.utils.data.importers.GenericSampleDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

A flexible CSV importer that represents slice(s) of field values of a dataset as columns of a CSV file.

See [this page](user_guide__import_datasets.md#csvdataset-import) for format details.

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

    * a filename like `"labels.csv"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.csv`

  * **media_field** (_"filepath"_) â 

the name of the column containing the media path for each sample. The media paths in this column may be:

    * filenames or relative paths to media files in `data_path`

    * absolute media paths, in which case `data_path` has no effect

  * **fields** (_None_) â 

an optional parameter that specifies the columns to read and parse from the CSV file. Can be any of the following:

    * an iterable of column names to parse as strings

    * a dict mapping column names to functions that parse the column values into the appropriate type. Any keys with `None` values in this case are directly loaded as strings

If not provided, all columns are parsed as strings

  * **skip_missing_media** (_False_) â whether to skip (True) or raise an error (False) when rows with no `media_field` are encountered

  * **include_all_data** (_False_) â whether to generate samples for all media in the data directory (True) rather than only creating samples for media with CSV rows (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_sample_field_schema` | Whether this importer produces a sample field schema.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

class fiftyone.utils.csv.CSVDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _media_field ='filepath'_, _fields =None_)#
    

Bases: [`BatchDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter "fiftyone.utils.data.exporters.BatchDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

A flexible CSV exporter that represents slice(s) of field values of a dataset as columns of a CSV file.

See [this page](user_guide__export_datasets.md#csvdataset-export) for exporting datasets of this type.

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

    * a filename like `"labels.csv"` specifying the location in `export_dir` in which to export the labels

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

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the media in the exported labels

  * **media_field** (_"filepath"_) â the name of the field containing the media to export for each sample

  * **fields** (_None_) â 

an optional argument specifying the fields or `embedding.field.names` to include as columns in the exported CSV. Can be:

    * a field or iterable of fields

    * a dict mapping field names to column names

By default, only the `media_field` is exported




**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_samples`(sample_collection[,Â progress]) | Exports the given sample collection.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_samples(_sample_collection_ , _progress =None_)#
    

Exports the given sample collection.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
