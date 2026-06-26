---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.converters.html
---

# fiftyone.utils.data.converters#

Dataset format conversion utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`convert_dataset`([input_dir,Â input_type,Â ...]) | Converts a dataset stored on disk to another format on disk.  
---|---  
  
fiftyone.utils.data.converters.convert_dataset(_input_dir =None_, _input_type =None_, _input_kwargs =None_, _dataset_importer =None_, _output_dir =None_, _output_type =None_, _output_kwargs =None_, _dataset_exporter =None_, _overwrite =False_)#
    

Converts a dataset stored on disk to another format on disk.

The input dataset may be specified by providing either an `input_dir` and a corresponding `input_type` or by providing a `dataset_importer`.

The output dataset may be specified by providing either an `output_dir` and a corresponding `output_type` or by providing a `dataset_exporter`.

Parameters:
    

  * **input_dir** (_None_) â the input dataset directory

  * **input_type** (_None_) â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type of the dataset in `input_dir`

  * **input_kwargs** (_None_) â optional kwargs dict to pass to the constructor of the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") for the `input_type` you specify

  * **dataset_importer** (_None_) â a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") to use to import the input dataset

  * **output_dir** (_None_) â the directory to which to write the output dataset

  * **output_type** (_None_) â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type to write to `output_dir`

  * **output_kwargs** (_None_) â optional kwargs dict to pass to the constructor of the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") for the `output_type` you specify

  * **dataset_exporter** (_None_) â a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") to use to export the dataset

  * **overwrite** (_False_) â whether to delete existing directories before performing the export (True) or to merge the export with existing files and directories (False)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
