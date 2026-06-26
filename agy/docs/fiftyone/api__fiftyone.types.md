---
source_url: https://docs.voxel51.com/api/fiftyone.types.html
---

# fiftyone.types#

  * [fiftyone.types.dataset_types](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html)
    * [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset)
      * [`Dataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset.get_dataset_importer_cls)
      * [`Dataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset.get_dataset_exporter_cls)
    * [`UnlabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset)
      * [`UnlabeledDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset.get_dataset_exporter_cls)
      * [`UnlabeledDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset.get_dataset_importer_cls)
    * [`UnlabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledImageDataset)
      * [`UnlabeledImageDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledImageDataset.get_dataset_importer_cls)
      * [`UnlabeledImageDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledImageDataset.get_dataset_exporter_cls)
    * [`UnlabeledVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledVideoDataset)
      * [`UnlabeledVideoDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledVideoDataset.get_dataset_importer_cls)
      * [`UnlabeledVideoDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledVideoDataset.get_dataset_exporter_cls)
    * [`LabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset)
      * [`LabeledDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset.get_dataset_exporter_cls)
      * [`LabeledDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset.get_dataset_importer_cls)
    * [`LabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset)
      * [`LabeledImageDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset.get_dataset_importer_cls)
      * [`LabeledImageDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset.get_dataset_exporter_cls)
    * [`LabeledVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset)
      * [`LabeledVideoDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset.get_dataset_importer_cls)
      * [`LabeledVideoDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset.get_dataset_exporter_cls)
    * [`ImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset)
      * [`ImageClassificationDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset.get_dataset_exporter_cls)
      * [`ImageClassificationDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset.get_dataset_importer_cls)
    * [`VideoClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDataset)
      * [`VideoClassificationDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDataset.get_dataset_exporter_cls)
      * [`VideoClassificationDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDataset.get_dataset_importer_cls)
    * [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset)
      * [`ImageDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset.get_dataset_exporter_cls)
      * [`ImageDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset.get_dataset_importer_cls)
    * [`VideoDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDetectionDataset)
      * [`VideoDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDetectionDataset.get_dataset_exporter_cls)
      * [`VideoDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDetectionDataset.get_dataset_importer_cls)
    * [`ImageSegmentationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDataset)
      * [`ImageSegmentationDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDataset.get_dataset_exporter_cls)
      * [`ImageSegmentationDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDataset.get_dataset_importer_cls)
    * [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset)
      * [`ImageLabelsDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset.get_dataset_exporter_cls)
      * [`ImageLabelsDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset.get_dataset_importer_cls)
    * [`VideoLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset)
      * [`VideoLabelsDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset.get_dataset_exporter_cls)
      * [`VideoLabelsDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset.get_dataset_importer_cls)
    * [`GroupDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GroupDataset)
      * [`GroupDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GroupDataset.get_dataset_importer_cls)
      * [`GroupDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GroupDataset.get_dataset_exporter_cls)
    * [`ImageDirectory`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDirectory)
      * [`ImageDirectory.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDirectory.get_dataset_importer_cls)
      * [`ImageDirectory.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDirectory.get_dataset_exporter_cls)
    * [`VideoDirectory`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDirectory)
      * [`VideoDirectory.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDirectory.get_dataset_importer_cls)
      * [`VideoDirectory.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDirectory.get_dataset_exporter_cls)
    * [`MediaDirectory`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.MediaDirectory)
      * [`MediaDirectory.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.MediaDirectory.get_dataset_importer_cls)
      * [`MediaDirectory.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.MediaDirectory.get_dataset_exporter_cls)
    * [`FiftyOneImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageClassificationDataset)
      * [`FiftyOneImageClassificationDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageClassificationDataset.get_dataset_importer_cls)
      * [`FiftyOneImageClassificationDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageClassificationDataset.get_dataset_exporter_cls)
    * [`ImageClassificationDirectoryTree`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDirectoryTree)
      * [`ImageClassificationDirectoryTree.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDirectoryTree.get_dataset_importer_cls)
      * [`ImageClassificationDirectoryTree.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDirectoryTree.get_dataset_exporter_cls)
    * [`VideoClassificationDirectoryTree`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDirectoryTree)
      * [`VideoClassificationDirectoryTree.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDirectoryTree.get_dataset_importer_cls)
      * [`VideoClassificationDirectoryTree.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDirectoryTree.get_dataset_exporter_cls)
    * [`TFImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFImageClassificationDataset)
      * [`TFImageClassificationDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFImageClassificationDataset.get_dataset_importer_cls)
      * [`TFImageClassificationDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFImageClassificationDataset.get_dataset_exporter_cls)
    * [`FiftyOneImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageDetectionDataset)
      * [`FiftyOneImageDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageDetectionDataset.get_dataset_importer_cls)
      * [`FiftyOneImageDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageDetectionDataset.get_dataset_exporter_cls)
    * [`FiftyOneTemporalDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset)
      * [`FiftyOneTemporalDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset.get_dataset_importer_cls)
      * [`FiftyOneTemporalDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset.get_dataset_exporter_cls)
    * [`COCODetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.COCODetectionDataset)
      * [`COCODetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.COCODetectionDataset.get_dataset_importer_cls)
      * [`COCODetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.COCODetectionDataset.get_dataset_exporter_cls)
    * [`VOCDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VOCDetectionDataset)
      * [`VOCDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VOCDetectionDataset.get_dataset_importer_cls)
      * [`VOCDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VOCDetectionDataset.get_dataset_exporter_cls)
    * [`KITTIDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.KITTIDetectionDataset)
      * [`KITTIDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.KITTIDetectionDataset.get_dataset_importer_cls)
      * [`KITTIDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.KITTIDetectionDataset.get_dataset_exporter_cls)
    * [`OpenImagesV6Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV6Dataset)
      * [`OpenImagesV6Dataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV6Dataset.get_dataset_importer_cls)
      * [`OpenImagesV6Dataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV6Dataset.get_dataset_exporter_cls)
    * [`OpenImagesV7Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV7Dataset)
      * [`OpenImagesV7Dataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV7Dataset.get_dataset_importer_cls)
      * [`OpenImagesV7Dataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenImagesV7Dataset.get_dataset_exporter_cls)
    * [`FIWDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FIWDataset)
      * [`FIWDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FIWDataset.get_dataset_importer_cls)
      * [`FIWDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FIWDataset.get_dataset_exporter_cls)
    * [`OpenLABELImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELImageDataset)
      * [`OpenLABELImageDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELImageDataset.get_dataset_importer_cls)
      * [`OpenLABELImageDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELImageDataset.get_dataset_exporter_cls)
    * [`OpenLABELVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELVideoDataset)
      * [`OpenLABELVideoDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELVideoDataset.get_dataset_importer_cls)
      * [`OpenLABELVideoDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.OpenLABELVideoDataset.get_dataset_exporter_cls)
    * [`YOLOv4Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv4Dataset)
      * [`YOLOv4Dataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv4Dataset.get_dataset_importer_cls)
      * [`YOLOv4Dataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv4Dataset.get_dataset_exporter_cls)
    * [`YOLOv5Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv5Dataset)
      * [`YOLOv5Dataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv5Dataset.get_dataset_importer_cls)
      * [`YOLOv5Dataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.YOLOv5Dataset.get_dataset_exporter_cls)
    * [`TFObjectDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFObjectDetectionDataset)
      * [`TFObjectDetectionDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFObjectDetectionDataset.get_dataset_importer_cls)
      * [`TFObjectDetectionDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.TFObjectDetectionDataset.get_dataset_exporter_cls)
    * [`ImageSegmentationDirectory`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDirectory)
      * [`ImageSegmentationDirectory.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDirectory.get_dataset_importer_cls)
      * [`ImageSegmentationDirectory.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDirectory.get_dataset_exporter_cls)
    * [`CVATImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATImageDataset)
      * [`CVATImageDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATImageDataset.get_dataset_importer_cls)
      * [`CVATImageDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATImageDataset.get_dataset_exporter_cls)
    * [`CVATVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATVideoDataset)
      * [`CVATVideoDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATVideoDataset.get_dataset_importer_cls)
      * [`CVATVideoDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CVATVideoDataset.get_dataset_exporter_cls)
    * [`FiftyOneImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageLabelsDataset)
      * [`FiftyOneImageLabelsDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageLabelsDataset.get_dataset_importer_cls)
      * [`FiftyOneImageLabelsDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneImageLabelsDataset.get_dataset_exporter_cls)
    * [`FiftyOneVideoLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneVideoLabelsDataset)
      * [`FiftyOneVideoLabelsDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneVideoLabelsDataset.get_dataset_importer_cls)
      * [`FiftyOneVideoLabelsDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneVideoLabelsDataset.get_dataset_exporter_cls)
    * [`BDDDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.BDDDataset)
      * [`BDDDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.BDDDataset.get_dataset_importer_cls)
      * [`BDDDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.BDDDataset.get_dataset_exporter_cls)
    * [`DICOMDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.DICOMDataset)
      * [`DICOMDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.DICOMDataset.get_dataset_importer_cls)
      * [`DICOMDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.DICOMDataset.get_dataset_exporter_cls)
    * [`ActivityNetDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ActivityNetDataset)
      * [`ActivityNetDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ActivityNetDataset.get_dataset_importer_cls)
      * [`ActivityNetDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ActivityNetDataset.get_dataset_exporter_cls)
    * [`GeoJSONDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoJSONDataset)
      * [`GeoJSONDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoJSONDataset.get_dataset_importer_cls)
      * [`GeoJSONDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoJSONDataset.get_dataset_exporter_cls)
    * [`GeoTIFFDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoTIFFDataset)
      * [`GeoTIFFDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoTIFFDataset.get_dataset_importer_cls)
      * [`GeoTIFFDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.GeoTIFFDataset.get_dataset_exporter_cls)
    * [`CSVDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CSVDataset)
      * [`CSVDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CSVDataset.get_dataset_importer_cls)
      * [`CSVDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.CSVDataset.get_dataset_exporter_cls)
    * [`FiftyOneDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneDataset)
      * [`FiftyOneDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneDataset.get_dataset_importer_cls)
      * [`FiftyOneDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneDataset.get_dataset_exporter_cls)
    * [`LegacyFiftyOneDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LegacyFiftyOneDataset)
      * [`LegacyFiftyOneDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LegacyFiftyOneDataset.get_dataset_importer_cls)
      * [`LegacyFiftyOneDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LegacyFiftyOneDataset.get_dataset_exporter_cls)
    * [`PlacesDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.PlacesDataset)
      * [`PlacesDataset.get_dataset_importer_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.PlacesDataset.get_dataset_importer_cls)
      * [`PlacesDataset.get_dataset_exporter_cls()`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.PlacesDataset.get_dataset_exporter_cls)



## Module contents#

FiftyOne types.

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
  
class fiftyone.types.Dataset#
    

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

class fiftyone.types.UnlabeledDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.UnlabeledImageDataset#
    

Bases: [`UnlabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset "fiftyone.types.dataset_types.UnlabeledDataset")

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

class fiftyone.types.UnlabeledVideoDataset#
    

Bases: [`UnlabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset "fiftyone.types.dataset_types.UnlabeledDataset")

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

class fiftyone.types.LabeledDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.LabeledImageDataset#
    

Bases: [`LabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset "fiftyone.types.dataset_types.LabeledDataset")

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

class fiftyone.types.LabeledVideoDataset#
    

Bases: [`LabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset "fiftyone.types.dataset_types.LabeledDataset")

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

class fiftyone.types.ImageClassificationDataset#
    

Bases: [`LabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset "fiftyone.types.dataset_types.LabeledImageDataset")

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

class fiftyone.types.VideoClassificationDataset#
    

Bases: [`LabeledVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset "fiftyone.types.dataset_types.LabeledVideoDataset")

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

class fiftyone.types.ImageDetectionDataset#
    

Bases: [`LabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset "fiftyone.types.dataset_types.LabeledImageDataset")

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

class fiftyone.types.VideoDetectionDataset#
    

Bases: [`LabeledVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset "fiftyone.types.dataset_types.LabeledVideoDataset")

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

class fiftyone.types.ImageSegmentationDataset#
    

Bases: [`LabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset "fiftyone.types.dataset_types.LabeledImageDataset")

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

class fiftyone.types.ImageLabelsDataset#
    

Bases: [`LabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledImageDataset "fiftyone.types.dataset_types.LabeledImageDataset")

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

class fiftyone.types.VideoLabelsDataset#
    

Bases: [`LabeledVideoDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledVideoDataset "fiftyone.types.dataset_types.LabeledVideoDataset")

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

class fiftyone.types.GroupDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.ImageDirectory#
    

Bases: [`UnlabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledImageDataset "fiftyone.types.dataset_types.UnlabeledImageDataset")

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

class fiftyone.types.VideoDirectory#
    

Bases: [`UnlabeledImageDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledImageDataset "fiftyone.types.dataset_types.UnlabeledImageDataset")

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

class fiftyone.types.MediaDirectory#
    

Bases: [`UnlabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.UnlabeledDataset "fiftyone.types.dataset_types.UnlabeledDataset")

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

class fiftyone.types.FiftyOneImageClassificationDataset#
    

Bases: [`ImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset "fiftyone.types.dataset_types.ImageClassificationDataset")

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

class fiftyone.types.ImageClassificationDirectoryTree#
    

Bases: [`ImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset "fiftyone.types.dataset_types.ImageClassificationDataset")

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

class fiftyone.types.VideoClassificationDirectoryTree#
    

Bases: [`VideoClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoClassificationDataset "fiftyone.types.dataset_types.VideoClassificationDataset")

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

class fiftyone.types.TFImageClassificationDataset#
    

Bases: [`ImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset "fiftyone.types.dataset_types.ImageClassificationDataset")

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

class fiftyone.types.FiftyOneImageDetectionDataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.FiftyOneTemporalDetectionDataset#
    

Bases: [`VideoDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoDetectionDataset "fiftyone.types.dataset_types.VideoDetectionDataset")

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

class fiftyone.types.COCODetectionDataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.VOCDetectionDataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.KITTIDetectionDataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.OpenImagesV6Dataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.OpenImagesV7Dataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.FIWDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.OpenLABELImageDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.OpenLABELVideoDataset#
    

Bases: [`VideoLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset "fiftyone.types.dataset_types.VideoLabelsDataset")

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

class fiftyone.types.YOLOv4Dataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.YOLOv5Dataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.TFObjectDetectionDataset#
    

Bases: [`ImageDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageDetectionDataset "fiftyone.types.dataset_types.ImageDetectionDataset")

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

class fiftyone.types.ImageSegmentationDirectory#
    

Bases: [`ImageSegmentationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageSegmentationDataset "fiftyone.types.dataset_types.ImageSegmentationDataset")

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

class fiftyone.types.CVATImageDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.CVATVideoDataset#
    

Bases: [`VideoLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset "fiftyone.types.dataset_types.VideoLabelsDataset")

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

class fiftyone.types.FiftyOneImageLabelsDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.FiftyOneVideoLabelsDataset#
    

Bases: [`VideoLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.VideoLabelsDataset "fiftyone.types.dataset_types.VideoLabelsDataset")

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

class fiftyone.types.BDDDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.DICOMDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.ActivityNetDataset#
    

Bases: [`FiftyOneTemporalDetectionDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset "fiftyone.types.dataset_types.FiftyOneTemporalDetectionDataset")

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

class fiftyone.types.GeoJSONDataset#
    

Bases: [`LabeledDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.LabeledDataset "fiftyone.types.dataset_types.LabeledDataset")

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

class fiftyone.types.GeoTIFFDataset#
    

Bases: [`ImageLabelsDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageLabelsDataset "fiftyone.types.dataset_types.ImageLabelsDataset")

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

class fiftyone.types.CSVDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.FiftyOneDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.LegacyFiftyOneDataset#
    

Bases: [`Dataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.Dataset "fiftyone.types.dataset_types.Dataset")

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

class fiftyone.types.PlacesDataset#
    

Bases: [`ImageClassificationDataset`](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html#fiftyone.types.dataset_types.ImageClassificationDataset "fiftyone.types.dataset_types.ImageClassificationDataset")

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
