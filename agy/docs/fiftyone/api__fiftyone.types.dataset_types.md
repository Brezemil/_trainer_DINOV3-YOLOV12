---
source_url: https://docs.voxel51.com/api/fiftyone.types.dataset_types.html?highlight=dataset%20type
---

# fiftyone.types.dataset_types#

FiftyOne dataset types.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Dataset`() | Base type for datasets.  
---|---  
`UnlabeledDataset`() | Base type for datasets that represent an unlabeled collection of data samples.  
`UnlabeledImageDataset`() | Base type for datasets that represent an unlabeled collection of images.  
`UnlabeledVideoDataset`() | Base type for datasets that represent an unlabeled collection of videos.  
`LabeledDataset`() | Base type for datasets that represent a collection of data samples and their associated labels.  
`LabeledImageDataset`() | Base type for datasets that represent a collection of images and their associated labels.  
`LabeledVideoDataset`() | Base type for datasets that represent a collection of videos and their associated labels.  
`ImageClassificationDataset`() | Base type for datasets that represent a collection of images and a set of associated classification labels.  
`VideoClassificationDataset`() | Base type for datasets that represent a collection of videos and a set of associated classification labels.  
`ImageDetectionDataset`() | Base type for datasets that represent a collection of images and a set of associated detections.  
`VideoDetectionDataset`() | Base type for datasets that represent a collection of videos and a set of associated video detections.  
`ImageSegmentationDataset`() | Base type for datasets that represent a collection of images and a set of associated semantic segmentations.  
`ImageLabelsDataset`() | Base type for datasets that represent a collection of images and a set of associated multitask predictions.  
`VideoLabelsDataset`() | Base type for datasets that represent a collection of videos and a set of associated multitask predictions.  
`GroupDataset`() | Base type for datasets that contain grouped samples of any type(s).  
`ImageDirectory`() | A directory of images.  
`VideoDirectory`() | A directory of videos.  
`MediaDirectory`() | A directory of media files.  
`FiftyOneImageClassificationDataset`() | A labeled dataset consisting of images and their associated classification labels stored in a simple JSON format.  
`ImageClassificationDirectoryTree`() | A directory tree whose subfolders define an image classification dataset.  
`VideoClassificationDirectoryTree`() | A directory tree whose subfolders define a video classification dataset.  
`TFImageClassificationDataset`() | A labeled dataset consisting of images and their associated classification labels stored as [TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord).  
`FiftyOneImageDetectionDataset`() | A labeled dataset consisting of images and their associated object detections stored in a simple JSON format.  
`FiftyOneTemporalDetectionDataset`() | A labeled dataset consisting of videos and their associated temporal detections stored in a simple JSON format.  
`COCODetectionDataset`() | A labeled dataset consisting of images and their associated object detections saved in [COCO Object Detection Format](https://cocodataset.org/#format-data).  
`VOCDetectionDataset`() | A labeled dataset consisting of images and their associated object detections saved in [VOC format](http://host.robots.ox.ac.uk/pascal/VOC).  
`KITTIDetectionDataset`() | A labeled dataset consisting of images and their associated object detections saved in [KITTI format](http://www.cvlibs.net/datasets/kitti/eval_object.php).  
`OpenImagesV6Dataset`() | A labeled dataset consisting of images and their associated annotations saved in [Open Images format](https://storage.googleapis.com/openimages/web/download.html).  
`OpenImagesV7Dataset`() | A labeled dataset consisting of images and their associated annotations saved in [Open Images format](https://storage.googleapis.com/openimages/web/download.html).  
`FIWDataset`() | A labeled dataset consisting of images and their associated annotations saved in [Families in the Wild format](https://github.com/visionjo/pykinship#db-contents-and-structure).  
`OpenLABELImageDataset`() |   
`OpenLABELVideoDataset`() |   
`YOLOv4Dataset`() | A labeled dataset consisting of images and their associated object detections saved in [YOLOv4 format](https://github.com/AlexeyAB/darknet).  
`YOLOv5Dataset`() | A labeled dataset consisting of images and their associated object detections saved in [YOLOv5 format](https://github.com/ultralytics/yolov5).  
`TFObjectDetectionDataset`() | A labeled dataset consisting of images and their associated object detections stored as TFRecords in [TF Object Detection API format](https://github.com/tensorflow/models/blob/master/research/object_detection).  
`ImageSegmentationDirectory`() | An labeled dataset consisting of images and their associated semantic segmentations stored as images on disk.  
`CVATImageDataset`() | A labeled dataset consisting of images and their associated labels stored in [CVAT image format](https://github.com/opencv/cvat).  
`CVATVideoDataset`() | A labeled dataset consisting of images and their associated object detections stored in [CVAT video format](https://github.com/opencv/cvat).  
`FiftyOneImageLabelsDataset`() | A labeled dataset consisting of images and their associated multitask predictions stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).  
`FiftyOneVideoLabelsDataset`() | A labeled dataset consisting of videos and their associated labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).  
`BDDDataset`() | A labeled dataset consisting of images and their associated multitask predictions saved in [Berkeley DeepDrive (BDD) format](http://bdd-data.berkeley.edu).  
`DICOMDataset`() | An image dataset whose image data and optional properties are stored in [DICOM format](https://en.wikipedia.org/wiki/DICOM).  
`ActivityNetDataset`() | A video dataset composed of temporal activity detections from the [ActivityNet dataset](http://activity-net.org/download.html).  
`GeoJSONDataset`() | An image or video dataset whose geolocation data and optional properties are stored in [GeoJSON format](https://en.wikipedia.org/wiki/GeoJSON).  
`GeoTIFFDataset`() | An image dataset whose image and geolocation data are stored in [GeoTIFF format](https://en.wikipedia.org/wiki/GeoTIFF).  
`CSVDataset`() | A flexible CSV format that represents slice(s) of field values of a dataset as columns of a CSV file.  
`FiftyOneDataset`() | A disk representation of an entire [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") stored on disk in a serialized JSON format along with its source media.  
`LegacyFiftyOneDataset`() | Legacy disk representation of an entire [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") stored on disk in a serialized JSON format along with its source media.  
`PlacesDataset`() | A labeled dataset consisting of images and their associated labels from the Places dataset <http://places2.csail.mit.edu/index.html>.  
  
class fiftyone.types.dataset_types.Dataset#
    

Bases: `object`

Base type for datasets.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.UnlabeledDataset#
    

Bases: `Dataset`

Base type for datasets that represent an unlabeled collection of data samples.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

class fiftyone.types.dataset_types.UnlabeledImageDataset#
    

Bases: `UnlabeledDataset`

Base type for datasets that represent an unlabeled collection of images.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.UnlabeledVideoDataset#
    

Bases: `UnlabeledDataset`

Base type for datasets that represent an unlabeled collection of videos.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter "fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter "fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter "fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.LabeledDataset#
    

Bases: `Dataset`

Base type for datasets that represent a collection of data samples and their associated labels.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

class fiftyone.types.dataset_types.LabeledImageDataset#
    

Bases: `LabeledDataset`

Base type for datasets that represent a collection of images and their associated labels.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.LabeledVideoDataset#
    

Bases: `LabeledDataset`

Base type for datasets that represent a collection of videos and their associated labels.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.ImageClassificationDataset#
    

Bases: `LabeledImageDataset`

Base type for datasets that represent a collection of images and a set of associated classification labels.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

class fiftyone.types.dataset_types.VideoClassificationDataset#
    

Bases: `LabeledVideoDataset`

Base type for datasets that represent a collection of videos and a set of associated classification labels.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

class fiftyone.types.dataset_types.ImageDetectionDataset#
    

Bases: `LabeledImageDataset`

Base type for datasets that represent a collection of images and a set of associated detections.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

class fiftyone.types.dataset_types.VideoDetectionDataset#
    

Bases: `LabeledVideoDataset`

Base type for datasets that represent a collection of videos and a set of associated video detections.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

class fiftyone.types.dataset_types.ImageSegmentationDataset#
    

Bases: `LabeledImageDataset`

Base type for datasets that represent a collection of images and a set of associated semantic segmentations.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

class fiftyone.types.dataset_types.ImageLabelsDataset#
    

Bases: `LabeledImageDataset`

Base type for datasets that represent a collection of images and a set of associated multitask predictions.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

class fiftyone.types.dataset_types.VideoLabelsDataset#
    

Bases: `LabeledVideoDataset`

Base type for datasets that represent a collection of videos and a set of associated multitask predictions.

**Methods:**

`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
---|---  
`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
  
get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

class fiftyone.types.dataset_types.GroupDataset#
    

Bases: `Dataset`

Base type for datasets that contain grouped samples of any type(s).

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.GroupDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter "fiftyone.utils.data.importers.GroupDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.GroupDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter "fiftyone.utils.data.exporters.GroupDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.GroupDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter "fiftyone.utils.data.importers.GroupDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.GroupDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter "fiftyone.utils.data.importers.GroupDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.GroupDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter "fiftyone.utils.data.exporters.GroupDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.GroupDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter "fiftyone.utils.data.exporters.GroupDatasetExporter") class

class fiftyone.types.dataset_types.ImageDirectory#
    

Bases: `UnlabeledImageDataset`

A directory of images.

See [this page](user_guide__import_datasets.md#imagedirectory-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#imagedirectory-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.VideoDirectory#
    

Bases: `UnlabeledImageDataset`

A directory of videos.

See [this page](user_guide__import_datasets.md#videodirectory-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#videodirectory-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.MediaDirectory#
    

Bases: `UnlabeledDataset`

A directory of media files.

See [this page](user_guide__import_datasets.md#mediadirectory-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#mediadirectory-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneImageClassificationDataset#
    

Bases: `ImageClassificationDataset`

A labeled dataset consisting of images and their associated classification labels stored in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimageclassificationdataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyoneimageclassificationdataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.ImageClassificationDirectoryTree#
    

Bases: `ImageClassificationDataset`

A directory tree whose subfolders define an image classification dataset.

See [this page](user_guide__import_datasets.md#imageclassificationdirectorytree-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#imageclassificationdirectorytree-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.VideoClassificationDirectoryTree#
    

Bases: `VideoClassificationDataset`

A directory tree whose subfolders define a video classification dataset.

See [this page](user_guide__import_datasets.md#videoclassificationdirectorytree-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#videoclassificationdirectorytree-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.TFImageClassificationDataset#
    

Bases: `ImageClassificationDataset`

A labeled dataset consisting of images and their associated classification labels stored as [TFRecords](https://www.tensorflow.org/tutorials/load_data/tfrecord).

See [this page](user_guide__import_datasets.md#tfimageclassificationdataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#tfimageclassificationdataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneImageDetectionDataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections stored in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimagedetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyoneimagedetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset#
    

Bases: `VideoDetectionDataset`

A labeled dataset consisting of videos and their associated temporal detections stored in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyonetemporaldetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyonetemporaldetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.COCODetectionDataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections saved in [COCO Object Detection Format](https://cocodataset.org/#format-data).

See [this page](user_guide__import_datasets.md#cocodetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#cocodetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.VOCDetectionDataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections saved in [VOC format](http://host.robots.ox.ac.uk/pascal/VOC).

See [this page](user_guide__import_datasets.md#vocdetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#vocdetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.KITTIDetectionDataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections saved in [KITTI format](http://www.cvlibs.net/datasets/kitti/eval_object.php).

See [this page](user_guide__import_datasets.md#kittidetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#kittidetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.OpenImagesV6Dataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated annotations saved in [Open Images format](https://storage.googleapis.com/openimages/web/download.html).

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.OpenImagesV7Dataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated annotations saved in [Open Images format](https://storage.googleapis.com/openimages/web/download.html).

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.FIWDataset#
    

Bases: `Dataset`

A labeled dataset consisting of images and their associated annotations saved in [Families in the Wild format](https://github.com/visionjo/pykinship#db-contents-and-structure).

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.OpenLABELImageDataset#
    

Bases: `ImageLabelsDataset`

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.OpenLABELVideoDataset#
    

Bases: `VideoLabelsDataset`

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.YOLOv4Dataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections saved in [YOLOv4 format](https://github.com/AlexeyAB/darknet).

See [this page](user_guide__import_datasets.md#yolov4dataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#yolov4dataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.YOLOv5Dataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections saved in [YOLOv5 format](https://github.com/ultralytics/yolov5).

See [this page](user_guide__import_datasets.md#yolov5dataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#yolov5dataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.TFObjectDetectionDataset#
    

Bases: `ImageDetectionDataset`

A labeled dataset consisting of images and their associated object detections stored as TFRecords in [TF Object Detection API format](https://github.com/tensorflow/models/blob/master/research/object_detection).

See [this page](user_guide__import_datasets.md#tfobjectdetectiondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#tfobjectdetectiondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.ImageSegmentationDirectory#
    

Bases: `ImageSegmentationDataset`

An labeled dataset consisting of images and their associated semantic segmentations stored as images on disk.

See [this page](user_guide__import_datasets.md#imagesegmentationdirectory-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#imagesegmentationdirectory-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.CVATImageDataset#
    

Bases: `ImageLabelsDataset`

A labeled dataset consisting of images and their associated labels stored in [CVAT image format](https://github.com/opencv/cvat).

See [this page](user_guide__import_datasets.md#cvatimagedataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#cvatimagedataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.CVATVideoDataset#
    

Bases: `VideoLabelsDataset`

A labeled dataset consisting of images and their associated object detections stored in [CVAT video format](https://github.com/opencv/cvat).

See [this page](user_guide__import_datasets.md#cvatvideodataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#cvatvideodataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneImageLabelsDataset#
    

Bases: `ImageLabelsDataset`

A labeled dataset consisting of images and their associated multitask predictions stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyoneimagelabelsdataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyoneimagelabelsdataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneVideoLabelsDataset#
    

Bases: `VideoLabelsDataset`

A labeled dataset consisting of videos and their associated labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyonevideolabelsdataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyonevideolabelsdataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.BDDDataset#
    

Bases: `ImageLabelsDataset`

A labeled dataset consisting of images and their associated multitask predictions saved in [Berkeley DeepDrive (BDD) format](http://bdd-data.berkeley.edu).

See [this page](user_guide__import_datasets.md#bdddataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#bdddataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.DICOMDataset#
    

Bases: `ImageLabelsDataset`

An image dataset whose image data and optional properties are stored in [DICOM format](https://en.wikipedia.org/wiki/DICOM).

See [this page](user_guide__import_datasets.md#dicomdataset-import) for importing datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.ActivityNetDataset#
    

Bases: `FiftyOneTemporalDetectionDataset`

A video dataset composed of temporal activity detections from the [ActivityNet dataset](http://activity-net.org/download.html).

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter") class

class fiftyone.types.dataset_types.GeoJSONDataset#
    

Bases: `LabeledDataset`

An image or video dataset whose geolocation data and optional properties are stored in [GeoJSON format](https://en.wikipedia.org/wiki/GeoJSON).

See [this page](user_guide__import_datasets.md#geojsondataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#geojsondataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.GeoTIFFDataset#
    

Bases: `ImageLabelsDataset`

An image dataset whose image and geolocation data are stored in [GeoTIFF format](https://en.wikipedia.org/wiki/GeoTIFF).

See [this page](user_guide__import_datasets.md#geotiffdataset-import) for importing datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

class fiftyone.types.dataset_types.CSVDataset#
    

Bases: `Dataset`

A flexible CSV format that represents slice(s) of field values of a dataset as columns of a CSV file.

See [this page](user_guide__import_datasets.md#csvdataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#csvdataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.FiftyOneDataset#
    

Bases: `Dataset`

A disk representation of an entire [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") stored on disk in a serialized JSON format along with its source media.

See [this page](user_guide__import_datasets.md#fiftyonedataset-import) for importing datasets of this type, and see [this page](user_guide__export_datasets.md#fiftyonedataset-export) for exporting datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.LegacyFiftyOneDataset#
    

Bases: `Dataset`

Legacy disk representation of an entire [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") stored on disk in a serialized JSON format along with its source media.

Datasets of this type are read/written in the following format:
    
    
    <dataset_dir>/
        metadata.json
        samples.json
        data/
            <filename1>.<ext>
            <filename2>.<ext>
            ...
        annotations/
            <anno_key1>.json
            <anno_key2>.json
            ...
        brain/
            <brain_key1>.json
            <brain_key2>.json
            ...
        evaluations/
            <eval_key1>.json
            <eval_key2>.json
            ...
    

where `metadata.json` is a JSON file containing metadata associated with the dataset, `samples.json` is a JSON file containing a serialized representation of the samples in the dataset, `annotations/` contains any serialized `fiftyone.core.annotations.AnnotationResults`, `brain/` contains any serialized [`fiftyone.core.brain.BrainResults`](api__fiftyone.core.brain.md#fiftyone.core.brain.BrainResults "fiftyone.core.brain.BrainResults"), and `evaluations/` contains any serialized `fiftyone.core.evaluations.EvaluationResults`.

Video datasets have an additional `frames/` directory that contains a serialized representation of the frame labels for each video in the dataset.

Note

See [`fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter "fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter") for parameters that can be passed to methods like [`Dataset.from_dir()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.from_dir "fiftyone.core.dataset.Dataset.from_dir") to customize the import of datasets of this type.

Note

See [`fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter "fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter") for parameters that can be passed to methods like [`SampleCollection.export()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.export "fiftyone.core.collections.SampleCollection.export") to customize the export of datasets of this type.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter") class

class fiftyone.types.dataset_types.PlacesDataset#
    

Bases: `ImageClassificationDataset`

A labeled dataset consisting of images and their associated labels from the Places dataset <http://places2.csail.mit.edu/index.html>.

**Methods:**

`get_dataset_importer_cls`() | Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.  
---|---  
`get_dataset_exporter_cls`() | Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.  
  
get_dataset_importer_cls()#
    

Returns the [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class for importing datasets of this type from disk.

Returns:
    

a [`fiftyone.utils.data.importers.LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter") class

get_dataset_exporter_cls()#
    

Returns the [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class for exporting datasets of this type to disk.

Returns:
    

a [`fiftyone.utils.data.exporters.LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter") class

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
