---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.ingestors.html
---

# fiftyone.utils.data.ingestors#

Dataset ingestors.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ImageIngestor`(dataset_dir[,Â image_format]) | Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest images into the provided `dataset_dir` during import.  
---|---  
`UnlabeledImageDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests unlabeled images into the provided `dataset_dir` during import.  
`LabeledImageDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests labeled images into the provided `dataset_dir` during import.  
`VideoIngestor`(dataset_dir) | Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest videos into the provided `dataset_dir` during import.  
`UnlabeledVideoDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests unlabeled videos into the provided `dataset_dir` during import.  
`LabeledVideoDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests labeled videos into the provided `dataset_dir` during import.  
  
class fiftyone.utils.data.ingestors.ImageIngestor(_dataset_dir_ , _image_format =None_)#
    

Bases: `object`

Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest images into the provided `dataset_dir` during import.

Parameters:
    

  * **dataset_dir** â the directory where input images will be ingested into

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




class fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _image_format =None_, _max_samples =None_)#
    

Bases: [`UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter"), `ImageIngestor`

Dataset importer that ingests unlabeled images into the provided `dataset_dir` during import.

The source images are parsed from the provided `samples` using the provided [`fiftyone.utils.data.parsers.UnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser "fiftyone.utils.data.parsers.UnlabeledImageSampleParser").

If an image path is available via [`fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image_path "fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image_path"), then the image is directly copied from its source location into `dataset_dir`. In this case, the original filename is maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

If no image path is available, the image is read in-memory via [`fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image "fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image") and written to `dataset_dir` in the following format:
    
    
    <dataset_dir>/<image_count><image_format>
    

where `image_count` is the number of files in `dataset_dir`.

Parameters:
    

  * **dataset_dir** â the directory where input images will be ingested into

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â an [`fiftyone.utils.data.parsers.UnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser "fiftyone.utils.data.parsers.UnlabeledImageSampleParser") to use to parse the samples

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

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

class fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _image_format =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), `ImageIngestor`

Dataset importer that ingests labeled images into the provided `dataset_dir` during import.

The source images and labels are parsed from the provided `samples` using the provided [`fiftyone.utils.data.parsers.LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser "fiftyone.utils.data.parsers.LabeledImageSampleParser").

If an image path is available via [`fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image_path "fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image_path"), then the image is directly copied from its source location into `dataset_dir`. In this case, the original filename is maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

If no image path is available, the image is read in-memory via [`fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image "fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image") and written to `dataset_dir` in the following format:
    
    
    <dataset_dir>/<image_count><image_format>
    

where `image_count` is the number of files in `dataset_dir`.

Parameters:
    

  * **dataset_dir** â the directory where input images will be ingested into

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â an [`fiftyone.utils.data.parsers.LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser "fiftyone.utils.data.parsers.LabeledImageSampleParser") to use to parse the samples

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

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

class fiftyone.utils.data.ingestors.VideoIngestor(_dataset_dir_)#
    

Bases: `object`

Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest videos into the provided `dataset_dir` during import.

Parameters:
    

**dataset_dir** â the directory where input videos will be ingested into

class fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _max_samples =None_)#
    

Bases: [`UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter"), `VideoIngestor`

Dataset importer that ingests unlabeled videos into the provided `dataset_dir` during import.

The source videos are parsed from the provided `samples` using the provided [`fiftyone.utils.data.parsers.UnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser "fiftyone.utils.data.parsers.UnlabeledVideoSampleParser").

The source videos are directly copied from their source locations into `dataset_dir`, maintaining the original filenames, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **dataset_dir** â the directory where input videos will be ingested into

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â an [`fiftyone.utils.data.parsers.UnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser "fiftyone.utils.data.parsers.UnlabeledVideoSampleParser") to use to parse the samples

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

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

class fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter"), `VideoIngestor`

Dataset importer that ingests labeled videos into the provided `dataset_dir` during import.

The source videos and labels are parsed from the provided `samples` using the provided [`fiftyone.utils.data.parsers.LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser "fiftyone.utils.data.parsers.LabeledVideoSampleParser").

The source videos are directly copied from their source locations into `dataset_dir`, maintaining the original filenames, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **dataset_dir** â the directory where input videos will be ingested into

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â an [`fiftyone.utils.data.parsers.LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser "fiftyone.utils.data.parsers.LabeledVideoSampleParser") to use to parse the samples

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
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




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the importer makes no guarantees about the frame labels that it may return




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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
