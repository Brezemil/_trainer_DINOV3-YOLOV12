---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.parsers.html
---

# fiftyone.utils.data.parsers#

Sample parsers.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`add_images`(dataset,Â samples,Â sample_parser) | Adds the given images to the dataset.  
---|---  
`add_labeled_images`(dataset,Â samples,Â ...[,Â ...]) | Adds the given labeled images to the dataset.  
`add_videos`(dataset,Â samples,Â sample_parser) | Adds the given videos to the dataset.  
`add_labeled_videos`(dataset,Â samples,Â ...[,Â ...]) | Adds the given labeled videos to the dataset.  
  
**Classes:**

`SampleParser`() | Base interface for sample parsers.  
---|---  
`UnlabeledImageSampleParser`() | Interface for `SampleParser` instances that parse unlabeled image samples.  
`UnlabeledVideoSampleParser`() | Interface for `SampleParser` instances that parse unlabeled video samples.  
`UnlabeledMediaSampleParser`() | Interface for `SampleParser` instances that parse unlabeled media samples.  
`ImageSampleParser`() | Sample parser that parses unlabeled image samples.  
`VideoSampleParser`() | Sample parser that parses unlabeled video samples.  
`MediaSampleParser`() | Sample parser that parses unlabeled media samples.  
`LabeledImageSampleParser`() | Interface for `SampleParser` instances that parse labeled image samples.  
`LabeledVideoSampleParser`() | Interface for `SampleParser` instances that parse labeled video samples.  
`LabeledImageTupleSampleParser`() | Generic sample parser that parses samples that are `(image_or_path, label)` tuples, where:  
`ImageClassificationSampleParser`([classes]) | Generic parser for image classification(s) samples whose labels are represented as [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances.  
`ImageDetectionSampleParser`([label_field,Â ...]) | Generic parser for image detection samples whose labels are represented as [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instances.  
`ImageLabelsSampleParser`([prefix,Â ...]) | Generic parser for multitask image prediction samples whose labels are stored in `eta.core.image.ImageLabels` format.  
`FiftyOneImageClassificationSampleParser`([...]) | Parser for samples in FiftyOne image classification datasets.  
`FiftyOneTemporalDetectionSampleParser`([...]) | Parser for samples in FiftyOne temporal detection datasets.  
`FiftyOneImageDetectionSampleParser`([classes]) | Parser for samples in FiftyOne image detection datasets.  
`FiftyOneImageLabelsSampleParser`([prefix,Â ...]) | Parser for samples in FiftyOne image labels datasets.  
`VideoLabelsSampleParser`([prefix,Â ...]) | Generic parser for labeled video samples whose labels are represented in `eta.core.video.VideoLabels` format.  
`FiftyOneVideoLabelsSampleParser`([prefix,Â ...]) | Parser for samples in FiftyOne video labels datasets.  
`FiftyOneUnlabeledImageSampleParser`([...]) | Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain images.  
`FiftyOneLabeledImageSampleParser`(label_field) | Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain labeled images.  
`ExtractClipsMixin`([compute_metadata,Â ...]) | Mixin for sample parsers that extract clips from [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.  
`FiftyOneUnlabeledVideoSampleParser`([...]) | Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain videos.  
`FiftyOneLabeledVideoSampleParser`([...]) | Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain labeled videos.  
`FiftyOneUnlabeledMediaSampleParser`([...]) | Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain unlabeled media.  
  
fiftyone.utils.data.parsers.add_images(_dataset_ , _samples_ , _sample_parser_ , _tags =None_, _generator =False_, _progress =None_)#
    

Adds the given images to the dataset.

This operation does not read the images.

See [this guide](user_guide__sample_parsers.md#custom-sample-parser) for more details about adding images to a dataset by defining your own `UnlabeledImageSampleParser`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a `UnlabeledImageSampleParser` instance to use to parse the samples

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

fiftyone.utils.data.parsers.add_labeled_images(_dataset_ , _samples_ , _sample_parser_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _generator =False_, _progress =None_)#
    

Adds the given labeled images to the dataset.

This operation will iterate over all provided samples, but the images will not be read (unless the sample parser requires it in order to compute image metadata).

See [this guide](user_guide__sample_parsers.md#custom-sample-parser) for more details about adding labeled images to a dataset by defining your own `LabeledImageSampleParser`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a `LabeledImageSampleParser` instance to use to parse the samples

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. If the parser produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the parser produces a dictionary of labels per sample, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **expand_schema** (_True_) â whether to dynamically add new sample fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

fiftyone.utils.data.parsers.add_videos(_dataset_ , _samples_ , _sample_parser_ , _tags =None_, _generator =False_, _progress =None_)#
    

Adds the given videos to the dataset.

This operation does not read the videos.

See [this guide](user_guide__sample_parsers.md#custom-sample-parser) for more details about adding videos to a dataset by defining your own `UnlabeledVideoSampleParser`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a `UnlabeledVideoSampleParser` instance to use to parse the samples

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

fiftyone.utils.data.parsers.add_labeled_videos(_dataset_ , _samples_ , _sample_parser_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _generator =False_, _progress =None_)#
    

Adds the given labeled videos to the dataset.

This operation will iterate over all provided samples, but the videos will not be read/decoded/etc.

See [this guide](user_guide__sample_parsers.md#custom-sample-parser) for more details about adding labeled videos to a dataset by defining your own `LabeledVideoSampleParser`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a `LabeledVideoSampleParser` instance to use to parse the samples

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. If the parser produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample/frame, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the parser produces a dictionary of labels per sample/frame, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **expand_schema** (_True_) â whether to dynamically add new sample fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

class fiftyone.utils.data.parsers.SampleParser#
    

Bases: `object`

Base interface for sample parsers.

`SampleParser` instances are used to parse samples emitted by dataset iterators when ingesting them into [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") instances.

The general recipe for using `SampleParser` instances is as follows:
    
    
    sample_parser = SampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        field = sample_parser.get_<field>()
    

where `field` is a subclass specific field to parse from the sample.

**Attributes:**

`current_sample` | The current sample.  
---|---  
  
**Methods:**

`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
---|---  
`clear_sample`() | Clears the current sample.  
  
property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

class fiftyone.utils.data.parsers.UnlabeledImageSampleParser#
    

Bases: `SampleParser`

Interface for `SampleParser` instances that parse unlabeled image samples.

Instances of this class must return images in `numpy` format.

The general recipe for using `UnlabeledImageSampleParser` instances is as follows:
    
    
    sample_parser = UnlabeledImageSampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        img = sample_parser.get_image()
        if sample_parser.has_image_path:
            image_path = sample_parser.get_image_path()
    
        if sample_parser.has_image_metadata:
            image_metadata = sample_parser.get_image_metadata()
    

**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.UnlabeledVideoSampleParser#
    

Bases: `SampleParser`

Interface for `SampleParser` instances that parse unlabeled video samples.

The general recipe for using `UnlabeledVideoSampleParser` instances is as follows:
    
    
    sample_parser = UnlabeledVideoSampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        video_path = sample_parser.get_video_path()
        video_metadata = sample_parser.get_video_metadata()
    

**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.UnlabeledMediaSampleParser#
    

Bases: `SampleParser`

Interface for `SampleParser` instances that parse unlabeled media samples.

The general recipe for using `UnlabeledMediaSampleParser` instances is as follows:
    
    
    sample_parser = UnlabeledMediaSampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        filepath = sample_parser.get_media_path()
        metadata = sample_parser.get_metadata()
    

**Attributes:**

`has_metadata` | Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_media_path`() | Returns the media path for the current sample.  
---|---  
`get_metadata`() | Returns the metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.

get_media_path()#
    

Returns the media path for the current sample.

Returns:
    

the path to the media on disk

get_metadata()#
    

Returns the metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.ImageSampleParser#
    

Bases: `UnlabeledImageSampleParser`

Sample parser that parses unlabeled image samples.

This implementation assumes that the provided sample is either an image that can be converted to numpy format via `np.asarray()` or the path to an image on disk.

**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`clear_sample`() | Clears the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.VideoSampleParser#
    

Bases: `UnlabeledVideoSampleParser`

Sample parser that parses unlabeled video samples.

This implementation assumes that the provided sample is a path to a video on disk.

**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.MediaSampleParser#
    

Bases: `UnlabeledMediaSampleParser`

Sample parser that parses unlabeled media samples.

This implementation assumes that the provided sample is a path to a media file on disk.

**Attributes:**

`has_metadata` | Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_media_path`() | Returns the media path for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_metadata`() | Returns the metadata for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.

get_media_path()#
    

Returns the media path for the current sample.

Returns:
    

the path to the media on disk

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_metadata()#
    

Returns the metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.LabeledImageSampleParser#
    

Bases: `SampleParser`

Interface for `SampleParser` instances that parse labeled image samples.

Instances of this class must return images in `numpy` format and labels as [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances.

The general recipe for using `LabeledImageSampleParser` instances is as follows:
    
    
    sample_parser = LabeledImageSampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        img = sample_parser.get_image()
        label = sample_parser.get_label()
    
        if sample_parser.has_image_path:
            image_path = sample_parser.get_image_path()
    
        if sample_parser.has_image_metadata:
            image_metadata = sample_parser.get_image_metadata()
    

**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_label`() | Returns the label for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.LabeledVideoSampleParser#
    

Bases: `SampleParser`

Interface for `SampleParser` instances that parse labeled video samples.

The general recipe for using `LabeledVideoSampleParser` instances is as follows:
    
    
    sample_parser = LabeledVideoSampleParser(...)
    
    for sample in samples:
        sample_parser.with_sample(sample)
        video_path = sample_parser.get_video_path()
        label = sample_parser.get_label()
        frames = sample_parser.get_frame_labels()
    
        if sample_parser.has_video_metadata:
            video_metadata = sample_parser.get_video_metadata()
    

**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`get_label`() | Returns the sample-level labels for the current sample.  
`get_frame_labels`() | Returns the frame labels for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the sample-level labels that it may return




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the parser makes no guarantees about the frame labels that it may return




get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_label()#
    

Returns the sample-level labels for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

get_frame_labels()#
    

Returns the frame labels for the current sample.

Returns:
    

a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame, or `None` if the sample has no frame labels

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.LabeledImageTupleSampleParser#
    

Bases: `LabeledImageSampleParser`

Generic sample parser that parses samples that are `(image_or_path, label)` tuples, where:

>   * `image_or_path` is either an image that can be converted to numpy format via `np.asarray()` or the path to an image on disk
> 
>   * `label` is a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance
> 
> 


This implementation provides a `_current_image()` property that caches the image for the current sample, for efficiency in case multiple getters require access to the image (e.g., to normalize coordinates, compute metadata, etc).

See the following subclasses of this parser for implementations that parse labels for common tasks:

>   * Image classification: `ImageClassificationSampleParser`
> 
>   * Object detection: `ImageDetectionSampleParser`
> 
>   * Multitask image prediction: `ImageLabelsSampleParser`
> 
> 


**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`clear_sample`() | Clears the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.ImageClassificationSampleParser(_classes =None_)#
    

Bases: `LabeledImageTupleSampleParser`

Generic parser for image classification(s) samples whose labels are represented as [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances.

This implementation supports samples that are `(image_or_path, target)` tuples, where:

>   * `image_or_path` is either an image that can be converted to numpy format via `np.asarray()` or the path to an image on disk
> 
>   * `target` can be any of the following:
> 
>     * None, for unlabeled images
> 
>     * a label string or list of label strings
> 
>     * a class ID or list of class IDs, if `classes` is provided
> 
>     * a dict or list of dicts of the following form:
>           
>           {
>               "label": <label-or-target>,
>               "confidence": <confidence>,
>               "attributes": <optional-attributes>,
>           }
>           
> 
>     * a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") or [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance
> 
> 


Parameters:
    

**classes** (_None_) â an optional list of class label strings. If provided, it is assumed that `target` contains class ID that should be mapped to label strings via `classes[target]`

**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
---|---  
`current_sample` | The current sample.  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
  
**Methods:**

`get_label`() | Returns the label for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




get_label()#
    

Returns the label for the current sample.

Parameters:
    

**sample** â the sample

Returns:
    

a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instance

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.ImageDetectionSampleParser(_label_field ='label'_, _bounding_box_field ='bounding_box'_, _confidence_field =None_, _attributes_field =None_, _classes =None_, _normalized =True_)#
    

Bases: `LabeledImageTupleSampleParser`

Generic parser for image detection samples whose labels are represented as [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instances.

This implementation supports samples that are `(image_or_path, detections_or_path)` tuples, where:

>   * `image_or_path` is either an image that can be converted to numpy format via `np.asarray()` or the path to an image on disk
> 
>   * `detections_or_path` can be any of the following:
>
>>     * None, for unlabeled images
>> 
>>     * a list of detections in the following format:
>>           
>>           [
>>               {
>>                   "<label_field>": <label-or-target>,
>>                   "<bounding_box_field>": [
>>                       <top-left-x>, <top-left-y>, <width>, <height>
>>                   ],
>>                   "<confidence_field>": <optional-confidence>,
>>                   "<attributes_field>": {
>>                       <optional-name>: <optional-value>,
>>                       ...
>>                   }
>>               },
>>               ...
>>           ]
>>           
>> 
>> In the above, `label-or-target` is either a class ID (if `classes` is provided) or a label string, and the bounding box coordinates can either be relative coordinates in `[0, 1]` (if `normalized == True`) or absolute pixels coordinates (if `normalized == False`). The confidence and attributes fields are optional for each sample.
>> 
>> The input field names can be configured as necessary when instantiating the parser.
>> 
>>     * the path on disk to a file in the above format
>> 
>>     * a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance
> 
> 


Parameters:
    

  * **label_field** (_"label"_) â the name of the object label field in the target dicts

  * **bounding_box_field** (_"bounding_box"_) â the name of the bounding box field in the target dicts

  * **confidence_field** (_None_) â the name of the optional confidence field in the target dicts

  * **attributes_field** (_None_) â the name of the optional attributes field in the target dicts

  * **classes** (_None_) â an optional list of class label strings. If provided, it is assumed that the `target` values are class IDs that should be mapped to label strings via `classes[target]`

  * **normalized** (_True_) â whether the bounding box coordinates are absolute pixel coordinates (`False`) or relative coordinates in [0, 1] (`True`)




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
---|---  
`current_sample` | The current sample.  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
  
**Methods:**

`get_label`() | Returns the label for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




get_label()#
    

Returns the label for the current sample.

Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.ImageLabelsSampleParser(_prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: `LabeledImageTupleSampleParser`

Generic parser for multitask image prediction samples whose labels are stored in `eta.core.image.ImageLabels` format.

This implementation provided by this class supports samples that are `(image_or_path, image_labels_or_path)` tuples, where:

>   * `image_or_path` is either an image that can be converted to numpy format via `np.asarray()` or the path to an image on disk
> 
>   * `image_labels_or_path` is an `eta.core.image.ImageLabels` instance, an `eta.core.frames.FrameLabels` instance, a serialized dict representation of either, or the path to either on disk
> 
> 


Parameters:
    

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded label dictionary

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the image labels to field names into which to expand them

  * **multilabel** (_False_) â whether to store attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)




**Attributes:**

`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
---|---  
`current_sample` | The current sample.  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
  
**Methods:**

`get_label`() | Returns the label for the current sample.  
---|---  
`clear_sample`() | Clears the current sample.  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




get_label()#
    

Returns the label for the current sample.

Returns:
    

a labels dictionary

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser(_classes =None_)#
    

Bases: `ImageClassificationSampleParser`

Parser for samples in FiftyOne image classification datasets.

See [this page](user_guide__import_datasets.md#fiftyoneimageclassificationdataset-import) for format details.

Parameters:
    

**classes** (_None_) â an optional list of class label strings. If provided, it is assumed that `target` is a class ID that should be mapped to a label string via `classes[target]`

**Methods:**

`clear_sample`() | Clears the current sample.  
---|---  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
**Attributes:**

`current_sample` | The current sample.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
  
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

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_label()#
    

Returns the label for the current sample.

Parameters:
    

**sample** â the sample

Returns:
    

a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instance

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

class fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser(_classes =None_, _compute_metadata =False_)#
    

Bases: `LabeledVideoSampleParser`

Parser for samples in FiftyOne temporal detection datasets.

See [this page](user_guide__import_datasets.md#fiftyonetemporaldetectiondataset-import) for format details.

Parameters:
    

  * **classes** (_None_) â an optional list of class label strings. If provided, it is assumed that `target` is a class ID that should be mapped to a label string via `classes[target]`

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances on-the-fly if `get_video_metadata()` is called and no metadata is available




**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.  
`current_sample` | The current sample.  
  
**Methods:**

`with_sample`(sample[,Â metadata]) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
---|---  
`get_video_path`() | Returns the video path for the current sample.  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`get_label`() | Returns the sample-level labels for the current sample.  
`get_frame_labels`() | Returns the frame labels for the current sample.  
`clear_sample`() | Clears the current sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the sample-level labels that it may return




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the parser makes no guarantees about the frame labels that it may return




with_sample(_sample_ , _metadata =None_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_label()#
    

Returns the sample-level labels for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

get_frame_labels()#
    

Returns the frame labels for the current sample.

Returns:
    

a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame, or `None` if the sample has no frame labels

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

class fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser(_classes =None_)#
    

Bases: `ImageDetectionSampleParser`

Parser for samples in FiftyOne image detection datasets.

See [this page](user_guide__import_datasets.md#fiftyoneimagedetectiondataset-import) for format details.

Parameters:
    

**classes** (_None_) â an optional list of class label strings. If provided, it is assumed that the `target` values are class IDs that should be mapped to label strings via `classes[target]`

**Methods:**

`clear_sample`() | Clears the current sample.  
---|---  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
**Attributes:**

`current_sample` | The current sample.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
  
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

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_label()#
    

Returns the label for the current sample.

Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance

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

class fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser(_prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: `ImageLabelsSampleParser`

Parser for samples in FiftyOne image labels datasets.

See [this page](user_guide__import_datasets.md#fiftyoneimagelabelsdataset-import) for format details.

Parameters:
    

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded label dictionary

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the image labels to field names into which to expand them

  * **multilabel** (_False_) â whether to store attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)




**Methods:**

`clear_sample`() | Clears the current sample.  
---|---  
`get_image`() | Returns the image from the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_image_path`() | Returns the image path for the current sample.  
`get_label`() | Returns the label for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
**Attributes:**

`current_sample` | The current sample.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
  
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

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_label()#
    

Returns the label for the current sample.

Returns:
    

a labels dictionary

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

class fiftyone.utils.data.parsers.VideoLabelsSampleParser(_prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: `LabeledVideoSampleParser`

Generic parser for labeled video samples whose labels are represented in `eta.core.video.VideoLabels` format.

This implementation provided by this class supports samples that are `(video_path, video_labels_or_path)` tuples, where:

>   * `video_path` is the path to a video on disk
> 
>   * `video_labels_or_path` is an `eta.core.video.VideoLabels` instance, a serialized dict representation of one, or the path to one on disk
> 
> 


Parameters:
    

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded sample/frame label dictionaries

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the sample labels to field names into which to expand them. By default, all sample labels are loaded

  * **frame_labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the frame labels to field names into which to expand them. By default, all frame labels are loaded

  * **multilabel** (_False_) â whether to store attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)




**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`get_label`() | Returns the sample-level labels for the current sample.  
`get_frame_labels`() | Returns the frame labels for the current sample.  
`clear_sample`() | Clears the current sample.  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the sample-level labels that it may return




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the parser makes no guarantees about the frame labels that it may return




get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_label()#
    

Returns the sample-level labels for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

get_frame_labels()#
    

Returns the frame labels for the current sample.

Returns:
    

a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame, or `None` if the sample has no frame labels

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser(_prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: `VideoLabelsSampleParser`

Parser for samples in FiftyOne video labels datasets.

See [this page](user_guide__import_datasets.md#fiftyonevideolabelsdataset-import) for format details.

Parameters:
    

  * **expand** (_True_) â whether to expand the labels for each frame into separate [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded frame label dictionaries

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the frame labels to field names into which to expand them

  * **multilabel** (_False_) â whether to store attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical attributes (True) or cast them to strings (False)




**Methods:**

`clear_sample`() | Clears the current sample.  
---|---  
`get_frame_labels`() | Returns the frame labels for the current sample.  
`get_label`() | Returns the sample-level labels for the current sample.  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`get_video_path`() | Returns the video path for the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
**Attributes:**

`current_sample` | The current sample.  
---|---  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.  
`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.  
  
clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the parser makes no guarantees about the frame labels that it may return




get_frame_labels()#
    

Returns the frame labels for the current sample.

Returns:
    

a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame, or `None` if the sample has no frame labels

get_label()#
    

Returns the sample-level labels for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the sample-level labels that it may return




with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser(_compute_metadata =False_)#
    

Bases: `UnlabeledImageSampleParser`

Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain images.

Parameters:
    

**compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances on-the-fly if `get_image_metadata()` is called and no metadata is available

**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser(_label_field_ , _label_fcn =None_, _compute_metadata =False_)#
    

Bases: `LabeledImageSampleParser`

Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain labeled images.

Parameters:
    

  * **label_field** â the name of the label field to parse, or a dictionary mapping label field names to keys for the return label dictionaries

  * **label_fcn** (_None_) â an optional function or dictionary mapping label field names to functions (must match `label_field`) to apply to each label before returning it

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances on-the-fly if `get_image_metadata()` is called and no metadata is available




**Attributes:**

`has_image_path` | Whether this parser produces paths to images on disk for samples that it parses.  
---|---  
`has_image_metadata` | Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.  
`current_sample` | The current sample.  
  
**Methods:**

`get_image`() | Returns the image from the current sample.  
---|---  
`get_image_path`() | Returns the image path for the current sample.  
`get_image_metadata`() | Returns the image metadata for the current sample.  
`get_label`() | Returns the label for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_image_path#
    

Whether this parser produces paths to images on disk for samples that it parses.

property has_image_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the labels that it may return




get_image()#
    

Returns the image from the current sample.

Returns:
    

a numpy image

get_image_path()#
    

Returns the image path for the current sample.

Returns:
    

the path to the image on disk

get_image_metadata()#
    

Returns the image metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

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

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.ExtractClipsMixin(_compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: `object`

Mixin for sample parsers that extract clips from [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.

Parameters:
    

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances on-the-fly when no pre-computed metadata is available

  * **write_clips** (_True_) â whether to write clips when their paths are requested

  * **clip_dir** (_None_) â a directory to write clips. Only applicable when parsing [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances

  * **video_format** (_None_) â the video format to use when writing video clips to disk. By default, `fiftyone.config.default_video_ext` is used




class fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser(_compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: `ExtractClipsMixin`, `UnlabeledVideoSampleParser`

Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain videos.

This class also supports [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.

Parameters:
    

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances on-the-fly if `get_video_metadata()` is called and no metadata is available

  * **write_clips** (_True_) â whether to write clips when `get_video_path()` is called

  * **clip_dir** (_None_) â a directory to write clips. Only applicable when parsing [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances

  * **video_format** (_None_) â the video format to use when writing video clips to disk. By default, `fiftyone.config.default_video_ext` is used




**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser(_label_field =None_, _frame_labels_field =None_, _label_fcn =None_, _frame_labels_fcn =None_, _compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: `ExtractClipsMixin`, `LabeledVideoSampleParser`

Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain labeled videos.

This class also supports [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.

Parameters:
    

  * **label_field** (_None_) â the name of a label field to parse, or a dictionary mapping label field names to output keys to use in the returned sample-level labels dictionary

  * **frame_labels_field** (_None_) â the name of a frame label field to parse, or a dictionary mapping field names to output keys describing the frame label fields to export

  * **label_fcn** (_None_) â an optional function or dictionary mapping label field names to functions (must match `label_field`) to apply to each sample label before returning it

  * **frame_labels_fcn** (_None_) â an optional function or dictionary mapping frame label field names to functions (must match `frame_labels_field`) to apply to each frame label before returning it

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances on-the-fly if `get_video_metadata()` is called and no metadata is available

  * **write_clips** (_True_) â whether to write clips when `get_video_path()` is called

  * **clip_dir** (_None_) â a directory to write clips. Only applicable when parsing [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances

  * **video_format** (_None_) â the video format to use when writing video clips to disk. By default, `fiftyone.config.default_video_ext` is used




**Attributes:**

`has_video_metadata` | Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.  
`current_sample` | The current sample.  
  
**Methods:**

`get_video_path`() | Returns the video path for the current sample.  
---|---  
`get_video_metadata`() | Returns the video metadata for the current sample.  
`get_label`() | Returns the sample-level labels for the current sample.  
`get_frame_labels`() | Returns the frame labels for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_video_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for samples that it parses.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the parser makes no guarantees about the sample-level labels that it may return




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this parser within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the parser is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the parser will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the parser makes no guarantees about the frame labels that it may return




get_video_path()#
    

Returns the video path for the current sample.

Returns:
    

the path to the video on disk

get_video_metadata()#
    

Returns the video metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance

get_label()#
    

Returns the sample-level labels for the current sample.

Returns:
    

a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

get_frame_labels()#
    

Returns the frame labels for the current sample.

Returns:
    

a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame, or `None` if the sample has no frame labels

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

class fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser(_compute_metadata =False_)#
    

Bases: `MediaSampleParser`

Parser for [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances that contain unlabeled media.

Parameters:
    

**compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances on-the-fly if `get_metadata()` is called and no metadata is available

**Attributes:**

`has_metadata` | Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.  
---|---  
`current_sample` | The current sample.  
  
**Methods:**

`get_media_path`() | Returns the media path for the current sample.  
---|---  
`get_metadata`() | Returns the metadata for the current sample.  
`clear_sample`() | Clears the current sample.  
`with_sample`(sample) | Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.  
  
property has_metadata#
    

Whether this parser produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for samples that it parses.

get_media_path()#
    

Returns the media path for the current sample.

Returns:
    

the path to the media on disk

get_metadata()#
    

Returns the metadata for the current sample.

Returns:
    

a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance

clear_sample()#
    

Clears the current sample.

Also clears any cached sample information stored by the parser.

property current_sample#
    

The current sample.

Raises:
    

**ValueError** â if there is no current sample

with_sample(_sample_)#
    

Sets the current sample so that subsequent calls to methods of this parser will return information from the given sample.

Guaranteed to call `clear_sample()` before setting the current sample.

Parameters:
    

**sample** â a sample

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
