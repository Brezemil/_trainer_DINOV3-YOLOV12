---
source_url: https://docs.voxel51.com/api/fiftyone.utils.tf.html
---

# fiftyone.utils.tf#

TensorFlow utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`from_images_dir`(images_dir[,Â recursive,Â ...]) | Creates a `tf.data.Dataset` for the given directory of images.  
---|---  
`from_images_patt`(images_patt[,Â force_rgb,Â ...]) | Creates a `tf.data.Dataset` for the given glob pattern of images.  
`from_images`(image_paths[,Â force_rgb,Â ...]) | Creates a `tf.data.Dataset` for the given list of images.  
`from_image_paths_and_labels`(image_paths,Â labels) | Creates a `tf.data.Dataset` for an image classification dataset stored as a list of image paths and labels.  
`from_image_classification_dir_tree`(dataset_dir) | Creates a `tf.data.Dataset` for the given image classification dataset directory tree.  
`from_tf_records`(tf_records_patt[,Â ...]) | Creates a `tf.data.Dataset` for the TFRecords at the given path(s).  
`write_tf_records`(examples,Â tf_records_path) | Writes the given `tf.train.Example` protos to disk as TFRecords.  
  
**Classes:**

`TFRecordsWriter`(tf_records_path[,Â num_shards]) | Class for writing TFRecords to disk.  
---|---  
`TFRecordSampleParser`([force_rgb]) | Base class for sample parsers that ingest `tf.train.Example` protos containing labeled images.  
`TFImageClassificationSampleParser`([force_rgb]) | Parser for image classification samples stored as [TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord).  
`TFObjectDetectionSampleParser`([force_rgb]) | Parser for samples in [TF Object Detection API format](https://github.com/tensorflow/models/blob/master/research/object_detection).  
`TFRecordsLabeledImageDatasetImporter`([...]) | Base class for [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") instances that import `tf.train.Example` protos containing labeled images.  
`TFImageClassificationDatasetImporter`([...]) | Importer for TF image classification datasets stored on disk.  
`TFObjectDetectionDatasetImporter`([...]) | Importer for TF detection datasets stored on disk.  
`TFRecordsDatasetExporter`([export_dir,Â ...]) | Base class for [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") instances that export labeled images as TFRecords datasets on disk.  
`TFImageClassificationDatasetExporter`([...]) | Exporter that writes an image classification dataset to disk as TFRecords.  
`TFObjectDetectionDatasetExporter`([...]) | Exporter that writes an object detection dataset to disk as TFRecords in the TF Object Detection API format.  
`TFExampleGenerator`([force_rgb]) | Base class for sample writers that emit `tf.train.Example` protos.  
`TFImageClassificationExampleGenerator`([...]) | Class for generating `tf.train.Example` protos for samples in TF image classification format.  
`TFObjectDetectionExampleGenerator`([...]) | Class for generating `tf.train.Example` protos for samples in TF Object Detection API format.  
  
fiftyone.utils.tf.from_images_dir(_images_dir_ , _recursive =True_, _force_rgb =False_, _num_parallel_calls =None_)#
    

Creates a `tf.data.Dataset` for the given directory of images.

Parameters:
    

  * **images_dir** â a directory of images

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **num_parallel_calls** (_None_) â the number of samples to read asynchronously in parallel. See <https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map> for details



Returns:
    

a `tf.data.Dataset` that emits decoded images

fiftyone.utils.tf.from_images_patt(_images_patt_ , _force_rgb =False_, _num_parallel_calls =None_)#
    

Creates a `tf.data.Dataset` for the given glob pattern of images.

Parameters:
    

  * **images_patt** â a glob pattern of images like `/path/to/images/*.jpg`

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **num_parallel_calls** (_None_) â the number of samples to read asynchronously in parallel. See <https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map> for details



Returns:
    

a `tf.data.Dataset` that emits decoded images

fiftyone.utils.tf.from_images(_image_paths_ , _force_rgb =False_, _num_parallel_calls =None_)#
    

Creates a `tf.data.Dataset` for the given list of images.

Parameters:
    

  * **image_paths** â an iterable of image paths

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **num_parallel_calls** (_None_) â the number of samples to read asynchronously in parallel. See <https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map> for details



Returns:
    

a `tf.data.Dataset` that emits decoded images

fiftyone.utils.tf.from_image_paths_and_labels(_image_paths_ , _labels_ , _force_rgb =False_, _num_parallel_calls =None_)#
    

Creates a `tf.data.Dataset` for an image classification dataset stored as a list of image paths and labels.

Parameters:
    

  * **image_paths** â an iterable of image paths

  * **labels** â an iterable of labels

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **num_parallel_calls** (_None_) â the number of samples to read asynchronously in parallel. See <https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map> for details



Returns:
    

a `tf.data.Dataset` that emits `(img, label)` pairs

fiftyone.utils.tf.from_image_classification_dir_tree(_dataset_dir_ , _force_rgb =False_, _num_parallel_calls =None_)#
    

Creates a `tf.data.Dataset` for the given image classification dataset directory tree.

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
    

  * **dataset_dir** â the dataset directory

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **num_parallel_calls** (_None_) â the number of samples to read asynchronously in parallel. See <https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map> for details



Returns:
    

a tuple of

  * **dataset** : a `tf.data.Dataset` that emits ``(img, label)` pairs

  * **classes** : a list of class label strings




fiftyone.utils.tf.from_tf_records(_tf_records_patt_ , _buffer_size =None_, _num_parallel_reads =None_)#
    

Creates a `tf.data.Dataset` for the TFRecords at the given path(s).

Parameters:
    

  * **tf_records_patt** â the path (or glob pattern of paths) to the TFRecords file(s) to load

  * **buffer_size** (_None_) â an optional buffer size, in bytes, to use when reading the records. Reasonable values are 1-100MBs

  * **num_parallel_reads** (_None_) â an optional number of files to read in parallel. If a negative value is passed, this parameter is set to the number of CPU cores on the host machine. By default, the files are read in series



Returns:
    

a `tf.data.Dataset` that emits `tf.train.Example` protos

fiftyone.utils.tf.write_tf_records(_examples_ , _tf_records_path_ , _num_shards =None_)#
    

Writes the given `tf.train.Example` protos to disk as TFRecords.

Parameters:
    

  * **examples** â an iterable that emits `tf.train.Example` protos

  * **tf_records_path** â the path to write the `.tfrecords` file. If sharding is requested `-%%05d-of-%%05d` is appended to the path

  * **num_shards** (_None_) â an optional number of shards to split the records into (using a round robin strategy)




class fiftyone.utils.tf.TFRecordsWriter(_tf_records_path_ , _num_shards =None_)#
    

Bases: `object`

Class for writing TFRecords to disk.

Example Usage:
    
    
    with TFRecordsWriter("/path/for/tf.records", num_shards=5) as writer:
        for tf_example in tf_examples:
            writer.write(tf_example)
    

Parameters:
    

  * **tf_records_path** â the path to write the `.tfrecords` file. If sharding is requested `-%%05d-of-%%05d` is appended to the path

  * **num_shards** (_None_) â an optional number of shards to split the records into (using a round robin strategy). If omitted, no sharding is used




**Methods:**

`write`(tf_example) | Writres the `tf.train.Example` proto to disk.  
---|---  
  
write(_tf_example_)#
    

Writres the `tf.train.Example` proto to disk.

Parameters:
    

**tf_example** â a `tf.train.Example` proto

class fiftyone.utils.tf.TFRecordSampleParser(_force_rgb =False_)#
    

Bases: [`LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser "fiftyone.utils.data.parsers.LabeledImageSampleParser")

Base class for sample parsers that ingest `tf.train.Example` protos containing labeled images.

Parameters:
    

**force_rgb** (_False_) â whether to force convert all images to RGB

**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_label`() | Returns the label for the current sample.  
`clear_sample`() | Clears the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
**Attributes:**

`current_sample` | The current sample.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
  
get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_label()#
    

Returns the label for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.tf.TFImageClassificationSampleParser(_force_rgb =False_)#
    

Bases: `TFRecordSampleParser`

Parser for image classification samples stored as [TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord).

This implementation supports samples that are `tf.train.Example` protos whose features follow the format described in [this page](user_guide__import_datasets.md#tfimageclassificationdataset-import).

Parameters:
    

**force_rgb** (_False_) â whether to force convert all images to RGB

**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
---|---  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image_metadata`() | Returns the image metadata for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_image`() | Returns the image from the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_label()#
    

Returns the label for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.tf.TFObjectDetectionSampleParser(_force_rgb =False_)#
    

Bases: `TFRecordSampleParser`

Parser for samples in [TF Object Detection API format](https://github.com/tensorflow/models/blob/master/research/object_detection).

This implementation supports samples that are `tf.train.Example` protos whose features follow the format described in [this page](user_guide__import_datasets.md#tfobjectdetectiondataset-import).

Parameters:
    

**force_rgb** (_False_) â whether to force convert all images to RGB

**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
---|---  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image_metadata`() | Returns the image metadata for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_image`() | Returns the image from the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_label()#
    

Returns the label for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.tf.TFRecordsLabeledImageDatasetImporter(_dataset_dir =None_, _tf_records_path =None_, _images_dir =None_, _image_format =None_, _force_rgb =False_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Base class for [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") instances that import `tf.train.Example` protos containing labeled images.

This class assumes that the input TFRecords only contain the images themselves and not their paths on disk, and, therefore, the images are read in-memory and written to the provided `images_dir` during import.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `tf_records_path` must be provided

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` or glob pattern like `"*.records-*-of-*"` specifying the location of the records in `dataset_dir`

    * an absolute filepath or glob pattern for the records. In this case, `dataset_dir` has no effect on the location of the records

If None, the parameter will default to `*record*`

  * **images_dir** (_None_) â the directory in which the images will be written. If not provided, the images will be unpacked into `dataset_dir`

  * **image_format** (_None_) â the image format to use to write the images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB

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

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




class fiftyone.utils.tf.TFImageClassificationDatasetImporter(_dataset_dir =None_, _tf_records_path =None_, _images_dir =None_, _image_format =None_, _force_rgb =False_, _max_samples =None_)#
    

Bases: `TFRecordsLabeledImageDatasetImporter`

Importer for TF image classification datasets stored on disk.

This class assumes that the input TFRecords only contain the images themselves and not their paths on disk, and, therefore, the images are read in-memory and written to the provided `images_dir` during import.

See [this page](user_guide__import_datasets.md#tfimageclassificationdataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `tf_records_path` must be provided

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` or glob pattern like `"*.records-*-of-*"` specifying the location of the records in `dataset_dir`

    * an absolute filepath or glob pattern for the records. In this case, `dataset_dir` has no effect on the location of the records

If None, the parameter will default to `*record*`

  * **images_dir** (_None_) â the directory in which the images will be written. If not provided, the images will be unpacked into `dataset_dir`

  * **image_format** (_None_) â the image format to use to write the images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




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

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.tf.TFObjectDetectionDatasetImporter(_dataset_dir =None_, _tf_records_path =None_, _images_dir =None_, _image_format =None_, _force_rgb =False_, _max_samples =None_)#
    

Bases: `TFRecordsLabeledImageDatasetImporter`

Importer for TF detection datasets stored on disk.

This class assumes that the input TFRecords only contain the images themselves and not their paths on disk, and, therefore, the images are read in-memory and written to the provided `images_dir` during import.

See [this page](user_guide__import_datasets.md#tfobjectdetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `tf_records_path` must be provided

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` or glob pattern like `"*.records-*-of-*"` specifying the location of the records in `dataset_dir`

    * an absolute filepath or glob pattern for the records. In this case, `dataset_dir` has no effect on the location of the records

If None, the parameter will default to `*record*`

  * **images_dir** (_None_) â the directory in which the images will be written. If not provided, the images will be unpacked into `dataset_dir`

  * **image_format** (_None_) â the image format to use to write the images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




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

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.tf.TFRecordsDatasetExporter(_export_dir =None_, _tf_records_path =None_, _num_shards =None_, _image_format =None_, _force_rgb =False_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Base class for [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") instances that export labeled images as TFRecords datasets on disk.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `tf_records_path` is an absolute path

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` specifying the location of the records in `export_dir`

    * an absolute filepath for the records. In this case, `export_dir` has no effect on the location of the records

If None, the parameter will default to `tf.records`

  * **num_shards** (_None_) â an optional number of shards to split the records into (using a round robin strategy). If specified, `-%%05d-of-%%05d` is appended to the records path

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_image_or_path_ , _label_ , _metadata =None_)#
    

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

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.tf.TFImageClassificationDatasetExporter(_export_dir =None_, _tf_records_path =None_, _num_shards =None_, _image_format =None_, _force_rgb =False_)#
    

Bases: `TFRecordsDatasetExporter`

Exporter that writes an image classification dataset to disk as TFRecords.

See [this page](user_guide__export_datasets.md#tfimageclassificationdataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. Can be omitted if `tf_records_path` is provided

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` specifying the location of the records in `export_dir`

    * an absolute filepath for the records. In this case, `export_dir` has no effect on the location of the records

If None, the parameter will default to `tf.records`

  * **num_shards** (_None_) â an optional number of shards to split the records into (using a round robin strategy). If specified, `-%%05d-of-%%05d` is appended to the records path

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
---|---  
`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been exported.  
---|---  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

export_sample(_image_or_path_ , _label_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

  * **metadata** (_None_) â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the sample. Only required when `requires_image_metadata()` is `True`




log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.tf.TFObjectDetectionDatasetExporter(_export_dir =None_, _tf_records_path =None_, _num_shards =None_, _image_format =None_, _force_rgb =False_, _classes =None_)#
    

Bases: `TFRecordsDatasetExporter`

Exporter that writes an object detection dataset to disk as TFRecords in the TF Object Detection API format.

See [this page](user_guide__export_datasets.md#tfobjectdetectiondataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. Can be omitted if `tf_records_path` is provided

  * **tf_records_path** (_None_) â 

an optional parameter that enables explicit control over the location of the TF records. Can be any of the following:

    * a filename like `"tf.records"` specifying the location of the records in `export_dir`

    * an absolute filepath for the records. In this case, `export_dir` has no effect on the location of the records

If None, the parameter will default to `tf.records`

  * **num_shards** (_None_) â an optional number of shards to split the records into (using a round robin strategy). If specified, `-%%05d-of-%%05d` is appended to the records path

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **classes** (_None_) â the list of possible class labels




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
---|---  
`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been exported.  
---|---  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

export_sample(_image_or_path_ , _label_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

  * **metadata** (_None_) â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the sample. Only required when `requires_image_metadata()` is `True`




log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.tf.TFExampleGenerator(_force_rgb =False_)#
    

Bases: `object`

Base class for sample writers that emit `tf.train.Example` protos.

Parameters:
    

**force_rgb** (_False_) â whether to force convert all images to RGB

**Methods:**

`make_tf_example`(image_or_path,Â label,Â *args,Â ...) | Makes a `tf.train.Example` for the given data.  
---|---  
  
make_tf_example(_image_or_path_ , _label_ , _* args_, _** kwargs_)#
    

Makes a `tf.train.Example` for the given data.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **label** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label")

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments



Returns:
    

a `tf.train.Example`

class fiftyone.utils.tf.TFImageClassificationExampleGenerator(_force_rgb =False_)#
    

Bases: `TFExampleGenerator`

Class for generating `tf.train.Example` protos for samples in TF image classification format.

See [this page](user_guide__export_datasets.md#tfimageclassificationdataset-export) for format details.

Parameters:
    

**force_rgb** (_False_) â whether to force convert all images to RGB

**Methods:**

`make_tf_example`(image_or_path,Â classification) | Makes a `tf.train.Example` for the given data.  
---|---  
  
make_tf_example(_image_or_path_ , _classification_ , _filename =None_)#
    

Makes a `tf.train.Example` for the given data.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **classification** â a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instance, or `None`

  * **filename** (_None_) â a filename for the image. Required when `image_or_path` is an image, in which case the extension of this filename determines the encoding used. If `image_or_path` is the path to an image, this is optional; by default, the basename of `image_path` is used



Returns:
    

a `tf.train.Example`

class fiftyone.utils.tf.TFObjectDetectionExampleGenerator(_force_rgb =False_, _classes =None_)#
    

Bases: `TFExampleGenerator`

Class for generating `tf.train.Example` protos for samples in TF Object Detection API format.

See [this page](user_guide__export_datasets.md#tfobjectdetectiondataset-export) for format details.

Parameters:
    

  * **force_rgb** (_False_) â whether to force convert all images to RGB

  * **classes** (_None_) â the list of possible class labels




**Methods:**

`make_tf_example`(image_or_path,Â detections[,Â ...]) | Makes a `tf.train.Example` for the given data.  
---|---  
  
make_tf_example(_image_or_path_ , _detections_ , _filename =None_)#
    

Makes a `tf.train.Example` for the given data.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **detections** â a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance, or `None`

  * **filename** (_None_) â a filename for the image. Required when `image_or_path` is an image, in which case the extension of this filename determines the encoding used. If `image_or_path` is the path to an image, this is optional; by default, the basename of `image_path` is used



Returns:
    

a `tf.train.Example`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
