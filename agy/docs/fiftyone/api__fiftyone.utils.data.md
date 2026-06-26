---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.html
---

# fiftyone.utils.data#

  * [fiftyone.utils.data.base](api__fiftyone.utils.data.base.md)
    * [`map_values()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.map_values)
    * [`parse_images_dir()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.parse_images_dir)
    * [`parse_videos_dir()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.parse_videos_dir)
    * [`parse_image_classification_dir_tree()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.parse_image_classification_dir_tree)
    * [`download_image_classification_dataset()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.download_image_classification_dataset)
    * [`download_images()`](api__fiftyone.utils.data.base.md#fiftyone.utils.data.base.download_images)
  * [fiftyone.utils.data.converters](api__fiftyone.utils.data.converters.md)
    * [`convert_dataset()`](api__fiftyone.utils.data.converters.md#fiftyone.utils.data.converters.convert_dataset)
  * [fiftyone.utils.data.exporters](api__fiftyone.utils.data.exporters.md)
    * [`export_samples()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.export_samples)
    * [`write_dataset()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.write_dataset)
    * [`build_dataset_exporter()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.build_dataset_exporter)
    * [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin)
    * [`MediaExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter)
      * [`MediaExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter.setup)
      * [`MediaExporter.export()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter.export)
      * [`MediaExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter.close)
    * [`ImageExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageExporter)
      * [`ImageExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageExporter.close)
      * [`ImageExporter.export()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageExporter.export)
      * [`ImageExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageExporter.setup)
    * [`VideoExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoExporter)
      * [`VideoExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoExporter.close)
      * [`VideoExporter.export()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoExporter.export)
      * [`VideoExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoExporter.setup)
    * [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter)
      * [`DatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter.setup)
      * [`DatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter.log_collection)
      * [`DatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter.export_sample)
      * [`DatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter.close)
    * [`BatchDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter)
      * [`BatchDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter.export_sample)
      * [`BatchDatasetExporter.export_samples()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter.export_samples)
      * [`BatchDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter.close)
      * [`BatchDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter.log_collection)
      * [`BatchDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter.setup)
    * [`GenericSampleDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter)
      * [`GenericSampleDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter.export_sample)
      * [`GenericSampleDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter.close)
      * [`GenericSampleDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter.log_collection)
      * [`GenericSampleDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter.setup)
    * [`GroupDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter)
      * [`GroupDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter.export_sample)
      * [`GroupDatasetExporter.export_group()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter.export_group)
      * [`GroupDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter.close)
      * [`GroupDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter.log_collection)
      * [`GroupDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GroupDatasetExporter.setup)
    * [`UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter)
      * [`UnlabeledImageDatasetExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter.requires_image_metadata)
      * [`UnlabeledImageDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter.export_sample)
      * [`UnlabeledImageDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter.close)
      * [`UnlabeledImageDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter.log_collection)
      * [`UnlabeledImageDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter.setup)
    * [`UnlabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter)
      * [`UnlabeledVideoDatasetExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter.requires_video_metadata)
      * [`UnlabeledVideoDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter.export_sample)
      * [`UnlabeledVideoDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter.close)
      * [`UnlabeledVideoDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter.log_collection)
      * [`UnlabeledVideoDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter.setup)
    * [`UnlabeledMediaDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter)
      * [`UnlabeledMediaDatasetExporter.requires_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter.requires_metadata)
      * [`UnlabeledMediaDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter.export_sample)
      * [`UnlabeledMediaDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter.close)
      * [`UnlabeledMediaDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter.log_collection)
      * [`UnlabeledMediaDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter.setup)
    * [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter)
      * [`LabeledImageDatasetExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.requires_image_metadata)
      * [`LabeledImageDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.label_cls)
      * [`LabeledImageDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.export_sample)
      * [`LabeledImageDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.close)
      * [`LabeledImageDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.log_collection)
      * [`LabeledImageDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter.setup)
    * [`LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter)
      * [`LabeledVideoDatasetExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.requires_video_metadata)
      * [`LabeledVideoDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.label_cls)
      * [`LabeledVideoDatasetExporter.frame_labels_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.frame_labels_cls)
      * [`LabeledVideoDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.export_sample)
      * [`LabeledVideoDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.close)
      * [`LabeledVideoDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.log_collection)
      * [`LabeledVideoDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter.setup)
    * [`LegacyFiftyOneDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter)
      * [`LegacyFiftyOneDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter.setup)
      * [`LegacyFiftyOneDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter.log_collection)
      * [`LegacyFiftyOneDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter.export_sample)
      * [`LegacyFiftyOneDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter.close)
    * [`FiftyOneDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter)
      * [`FiftyOneDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter.setup)
      * [`FiftyOneDatasetExporter.export_samples()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter.export_samples)
      * [`FiftyOneDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter.close)
      * [`FiftyOneDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter.export_sample)
      * [`FiftyOneDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneDatasetExporter.log_collection)
    * [`ImageDirectoryExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter)
      * [`ImageDirectoryExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter.requires_image_metadata)
      * [`ImageDirectoryExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter.setup)
      * [`ImageDirectoryExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter.export_sample)
      * [`ImageDirectoryExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter.close)
      * [`ImageDirectoryExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageDirectoryExporter.log_collection)
    * [`VideoDirectoryExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter)
      * [`VideoDirectoryExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter.requires_video_metadata)
      * [`VideoDirectoryExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter.setup)
      * [`VideoDirectoryExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter.export_sample)
      * [`VideoDirectoryExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter.close)
      * [`VideoDirectoryExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoDirectoryExporter.log_collection)
    * [`MediaDirectoryExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter)
      * [`MediaDirectoryExporter.requires_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter.requires_metadata)
      * [`MediaDirectoryExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter.setup)
      * [`MediaDirectoryExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter.export_sample)
      * [`MediaDirectoryExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter.close)
      * [`MediaDirectoryExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaDirectoryExporter.log_collection)
    * [`FiftyOneImageClassificationDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter)
      * [`FiftyOneImageClassificationDatasetExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.requires_image_metadata)
      * [`FiftyOneImageClassificationDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.label_cls)
      * [`FiftyOneImageClassificationDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.setup)
      * [`FiftyOneImageClassificationDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.export_sample)
      * [`FiftyOneImageClassificationDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.close)
      * [`FiftyOneImageClassificationDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter.log_collection)
    * [`ImageClassificationDirectoryTreeExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter)
      * [`ImageClassificationDirectoryTreeExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.requires_image_metadata)
      * [`ImageClassificationDirectoryTreeExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.label_cls)
      * [`ImageClassificationDirectoryTreeExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.setup)
      * [`ImageClassificationDirectoryTreeExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.export_sample)
      * [`ImageClassificationDirectoryTreeExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.close)
      * [`ImageClassificationDirectoryTreeExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter.log_collection)
    * [`VideoClassificationDirectoryTreeExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter)
      * [`VideoClassificationDirectoryTreeExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.requires_video_metadata)
      * [`VideoClassificationDirectoryTreeExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.label_cls)
      * [`VideoClassificationDirectoryTreeExporter.frame_labels_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.frame_labels_cls)
      * [`VideoClassificationDirectoryTreeExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.setup)
      * [`VideoClassificationDirectoryTreeExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.export_sample)
      * [`VideoClassificationDirectoryTreeExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.close)
      * [`VideoClassificationDirectoryTreeExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter.log_collection)
    * [`FiftyOneImageDetectionDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter)
      * [`FiftyOneImageDetectionDatasetExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.requires_image_metadata)
      * [`FiftyOneImageDetectionDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.label_cls)
      * [`FiftyOneImageDetectionDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.setup)
      * [`FiftyOneImageDetectionDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.export_sample)
      * [`FiftyOneImageDetectionDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.close)
      * [`FiftyOneImageDetectionDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter.log_collection)
    * [`FiftyOneTemporalDetectionDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter)
      * [`FiftyOneTemporalDetectionDatasetExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.requires_video_metadata)
      * [`FiftyOneTemporalDetectionDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.label_cls)
      * [`FiftyOneTemporalDetectionDatasetExporter.frame_labels_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.frame_labels_cls)
      * [`FiftyOneTemporalDetectionDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.setup)
      * [`FiftyOneTemporalDetectionDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.export_sample)
      * [`FiftyOneTemporalDetectionDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.close)
      * [`FiftyOneTemporalDetectionDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter.log_collection)
    * [`ImageSegmentationDirectoryExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter)
      * [`ImageSegmentationDirectoryExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.requires_image_metadata)
      * [`ImageSegmentationDirectoryExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.label_cls)
      * [`ImageSegmentationDirectoryExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.setup)
      * [`ImageSegmentationDirectoryExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.export_sample)
      * [`ImageSegmentationDirectoryExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.close)
      * [`ImageSegmentationDirectoryExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter.log_collection)
    * [`FiftyOneImageLabelsDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter)
      * [`FiftyOneImageLabelsDatasetExporter.requires_image_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.requires_image_metadata)
      * [`FiftyOneImageLabelsDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.label_cls)
      * [`FiftyOneImageLabelsDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.setup)
      * [`FiftyOneImageLabelsDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.log_collection)
      * [`FiftyOneImageLabelsDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.export_sample)
      * [`FiftyOneImageLabelsDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter.close)
    * [`FiftyOneVideoLabelsDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter)
      * [`FiftyOneVideoLabelsDatasetExporter.requires_video_metadata`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.requires_video_metadata)
      * [`FiftyOneVideoLabelsDatasetExporter.label_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.label_cls)
      * [`FiftyOneVideoLabelsDatasetExporter.frame_labels_cls`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.frame_labels_cls)
      * [`FiftyOneVideoLabelsDatasetExporter.setup()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.setup)
      * [`FiftyOneVideoLabelsDatasetExporter.log_collection()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.log_collection)
      * [`FiftyOneVideoLabelsDatasetExporter.export_sample()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.export_sample)
      * [`FiftyOneVideoLabelsDatasetExporter.close()`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter.close)
  * [fiftyone.utils.data.importers](api__fiftyone.utils.data.importers.md)
    * [`import_samples()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.import_samples)
    * [`merge_samples()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.merge_samples)
    * [`build_dataset_importer()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.build_dataset_importer)
    * [`parse_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.parse_dataset_info)
    * [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin)
    * [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter)
      * [`DatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.__len__)
      * [`DatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.__next__)
      * [`DatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.has_dataset_info)
      * [`DatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.setup)
      * [`DatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.get_dataset_info)
      * [`DatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter.close)
    * [`BatchDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter)
      * [`BatchDatasetImporter.import_samples()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter.import_samples)
      * [`BatchDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter.close)
      * [`BatchDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter.get_dataset_info)
      * [`BatchDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter.has_dataset_info)
      * [`BatchDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter.setup)
    * [`GenericSampleDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter)
      * [`GenericSampleDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.__len__)
      * [`GenericSampleDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.__next__)
      * [`GenericSampleDatasetImporter.has_sample_field_schema`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.has_sample_field_schema)
      * [`GenericSampleDatasetImporter.get_sample_field_schema()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.get_sample_field_schema)
      * [`GenericSampleDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.close)
      * [`GenericSampleDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.get_dataset_info)
      * [`GenericSampleDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.has_dataset_info)
      * [`GenericSampleDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter.setup)
    * [`GroupDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter)
      * [`GroupDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.__len__)
      * [`GroupDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.__next__)
      * [`GroupDatasetImporter.group_field`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.group_field)
      * [`GroupDatasetImporter.get_group_media_types()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.get_group_media_types)
      * [`GroupDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.close)
      * [`GroupDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.get_dataset_info)
      * [`GroupDatasetImporter.get_sample_field_schema()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.get_sample_field_schema)
      * [`GroupDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.has_dataset_info)
      * [`GroupDatasetImporter.has_sample_field_schema`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.has_sample_field_schema)
      * [`GroupDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GroupDatasetImporter.setup)
    * [`UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter)
      * [`UnlabeledImageDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.__len__)
      * [`UnlabeledImageDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.__next__)
      * [`UnlabeledImageDatasetImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.has_image_metadata)
      * [`UnlabeledImageDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.close)
      * [`UnlabeledImageDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.get_dataset_info)
      * [`UnlabeledImageDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.has_dataset_info)
      * [`UnlabeledImageDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter.setup)
    * [`UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter)
      * [`UnlabeledVideoDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.__len__)
      * [`UnlabeledVideoDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.__next__)
      * [`UnlabeledVideoDatasetImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.has_video_metadata)
      * [`UnlabeledVideoDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.close)
      * [`UnlabeledVideoDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.get_dataset_info)
      * [`UnlabeledVideoDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.has_dataset_info)
      * [`UnlabeledVideoDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter.setup)
    * [`UnlabeledMediaDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter)
      * [`UnlabeledMediaDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.__len__)
      * [`UnlabeledMediaDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.__next__)
      * [`UnlabeledMediaDatasetImporter.has_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.has_metadata)
      * [`UnlabeledMediaDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.close)
      * [`UnlabeledMediaDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.get_dataset_info)
      * [`UnlabeledMediaDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.has_dataset_info)
      * [`UnlabeledMediaDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter.setup)
    * [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter)
      * [`LabeledImageDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.__len__)
      * [`LabeledImageDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.__next__)
      * [`LabeledImageDatasetImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.has_image_metadata)
      * [`LabeledImageDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.label_cls)
      * [`LabeledImageDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.close)
      * [`LabeledImageDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.get_dataset_info)
      * [`LabeledImageDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.has_dataset_info)
      * [`LabeledImageDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter.setup)
    * [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter)
      * [`LabeledVideoDatasetImporter.__len__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.__len__)
      * [`LabeledVideoDatasetImporter.__next__()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.__next__)
      * [`LabeledVideoDatasetImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.has_video_metadata)
      * [`LabeledVideoDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.label_cls)
      * [`LabeledVideoDatasetImporter.frame_labels_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.frame_labels_cls)
      * [`LabeledVideoDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.close)
      * [`LabeledVideoDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.get_dataset_info)
      * [`LabeledVideoDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.has_dataset_info)
      * [`LabeledVideoDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter.setup)
    * [`LegacyFiftyOneDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter)
      * [`LegacyFiftyOneDatasetImporter.has_sample_field_schema`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.has_sample_field_schema)
      * [`LegacyFiftyOneDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.has_dataset_info)
      * [`LegacyFiftyOneDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.setup)
      * [`LegacyFiftyOneDatasetImporter.get_sample_field_schema()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.get_sample_field_schema)
      * [`LegacyFiftyOneDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.get_dataset_info)
      * [`LegacyFiftyOneDatasetImporter.import_extras()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.import_extras)
      * [`LegacyFiftyOneDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter.close)
    * [`FiftyOneDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter)
      * [`FiftyOneDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter.setup)
      * [`FiftyOneDatasetImporter.import_samples()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter.import_samples)
      * [`FiftyOneDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter.close)
      * [`FiftyOneDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter.get_dataset_info)
      * [`FiftyOneDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneDatasetImporter.has_dataset_info)
    * [`ImageDirectoryImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter)
      * [`ImageDirectoryImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter.has_dataset_info)
      * [`ImageDirectoryImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter.has_image_metadata)
      * [`ImageDirectoryImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter.setup)
      * [`ImageDirectoryImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter.close)
      * [`ImageDirectoryImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageDirectoryImporter.get_dataset_info)
    * [`VideoDirectoryImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter)
      * [`VideoDirectoryImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter.has_dataset_info)
      * [`VideoDirectoryImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter.has_video_metadata)
      * [`VideoDirectoryImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter.setup)
      * [`VideoDirectoryImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter.close)
      * [`VideoDirectoryImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoDirectoryImporter.get_dataset_info)
    * [`MediaDirectoryImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter)
      * [`MediaDirectoryImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter.has_dataset_info)
      * [`MediaDirectoryImporter.has_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter.has_metadata)
      * [`MediaDirectoryImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter.setup)
      * [`MediaDirectoryImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter.close)
      * [`MediaDirectoryImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.MediaDirectoryImporter.get_dataset_info)
    * [`FiftyOneImageClassificationDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter)
      * [`FiftyOneImageClassificationDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.has_dataset_info)
      * [`FiftyOneImageClassificationDatasetImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.has_image_metadata)
      * [`FiftyOneImageClassificationDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.label_cls)
      * [`FiftyOneImageClassificationDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.setup)
      * [`FiftyOneImageClassificationDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.get_dataset_info)
      * [`FiftyOneImageClassificationDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter.close)
    * [`ImageClassificationDirectoryTreeImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter)
      * [`ImageClassificationDirectoryTreeImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.has_image_metadata)
      * [`ImageClassificationDirectoryTreeImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.has_dataset_info)
      * [`ImageClassificationDirectoryTreeImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.label_cls)
      * [`ImageClassificationDirectoryTreeImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.setup)
      * [`ImageClassificationDirectoryTreeImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.get_dataset_info)
      * [`ImageClassificationDirectoryTreeImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter.close)
    * [`VideoClassificationDirectoryTreeImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter)
      * [`VideoClassificationDirectoryTreeImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.has_video_metadata)
      * [`VideoClassificationDirectoryTreeImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.has_dataset_info)
      * [`VideoClassificationDirectoryTreeImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.label_cls)
      * [`VideoClassificationDirectoryTreeImporter.frame_labels_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.frame_labels_cls)
      * [`VideoClassificationDirectoryTreeImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.setup)
      * [`VideoClassificationDirectoryTreeImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.get_dataset_info)
      * [`VideoClassificationDirectoryTreeImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter.close)
    * [`FiftyOneImageDetectionDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter)
      * [`FiftyOneImageDetectionDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.has_dataset_info)
      * [`FiftyOneImageDetectionDatasetImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.has_image_metadata)
      * [`FiftyOneImageDetectionDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.label_cls)
      * [`FiftyOneImageDetectionDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.setup)
      * [`FiftyOneImageDetectionDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.get_dataset_info)
      * [`FiftyOneImageDetectionDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter.close)
    * [`FiftyOneTemporalDetectionDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter)
      * [`FiftyOneTemporalDetectionDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.has_dataset_info)
      * [`FiftyOneTemporalDetectionDatasetImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.has_video_metadata)
      * [`FiftyOneTemporalDetectionDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.label_cls)
      * [`FiftyOneTemporalDetectionDatasetImporter.frame_labels_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.frame_labels_cls)
      * [`FiftyOneTemporalDetectionDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.setup)
      * [`FiftyOneTemporalDetectionDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.get_dataset_info)
      * [`FiftyOneTemporalDetectionDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter.close)
    * [`ImageSegmentationDirectoryImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter)
      * [`ImageSegmentationDirectoryImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.has_dataset_info)
      * [`ImageSegmentationDirectoryImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.has_image_metadata)
      * [`ImageSegmentationDirectoryImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.label_cls)
      * [`ImageSegmentationDirectoryImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.setup)
      * [`ImageSegmentationDirectoryImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.close)
      * [`ImageSegmentationDirectoryImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter.get_dataset_info)
    * [`FiftyOneImageLabelsDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter)
      * [`FiftyOneImageLabelsDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.has_dataset_info)
      * [`FiftyOneImageLabelsDatasetImporter.has_image_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.has_image_metadata)
      * [`FiftyOneImageLabelsDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.label_cls)
      * [`FiftyOneImageLabelsDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.setup)
      * [`FiftyOneImageLabelsDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.get_dataset_info)
      * [`FiftyOneImageLabelsDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter.close)
    * [`FiftyOneVideoLabelsDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter)
      * [`FiftyOneVideoLabelsDatasetImporter.has_dataset_info`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.has_dataset_info)
      * [`FiftyOneVideoLabelsDatasetImporter.has_video_metadata`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.has_video_metadata)
      * [`FiftyOneVideoLabelsDatasetImporter.label_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.label_cls)
      * [`FiftyOneVideoLabelsDatasetImporter.frame_labels_cls`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.frame_labels_cls)
      * [`FiftyOneVideoLabelsDatasetImporter.setup()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.setup)
      * [`FiftyOneVideoLabelsDatasetImporter.get_dataset_info()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.get_dataset_info)
      * [`FiftyOneVideoLabelsDatasetImporter.close()`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter.close)
  * [fiftyone.utils.data.ingestors](api__fiftyone.utils.data.ingestors.md)
    * [`ImageIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.ImageIngestor)
    * [`UnlabeledImageDatasetIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor)
      * [`UnlabeledImageDatasetIngestor.has_dataset_info`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor.has_dataset_info)
      * [`UnlabeledImageDatasetIngestor.has_image_metadata`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor.has_image_metadata)
      * [`UnlabeledImageDatasetIngestor.setup()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor.setup)
      * [`UnlabeledImageDatasetIngestor.close()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor.close)
      * [`UnlabeledImageDatasetIngestor.get_dataset_info()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledImageDatasetIngestor.get_dataset_info)
    * [`LabeledImageDatasetIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor)
      * [`LabeledImageDatasetIngestor.has_dataset_info`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.has_dataset_info)
      * [`LabeledImageDatasetIngestor.has_image_metadata`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.has_image_metadata)
      * [`LabeledImageDatasetIngestor.label_cls`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.label_cls)
      * [`LabeledImageDatasetIngestor.setup()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.setup)
      * [`LabeledImageDatasetIngestor.close()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.close)
      * [`LabeledImageDatasetIngestor.get_dataset_info()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledImageDatasetIngestor.get_dataset_info)
    * [`VideoIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.VideoIngestor)
    * [`UnlabeledVideoDatasetIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor)
      * [`UnlabeledVideoDatasetIngestor.has_dataset_info`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor.has_dataset_info)
      * [`UnlabeledVideoDatasetIngestor.has_video_metadata`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor.has_video_metadata)
      * [`UnlabeledVideoDatasetIngestor.setup()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor.setup)
      * [`UnlabeledVideoDatasetIngestor.close()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor.close)
      * [`UnlabeledVideoDatasetIngestor.get_dataset_info()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.UnlabeledVideoDatasetIngestor.get_dataset_info)
    * [`LabeledVideoDatasetIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor)
      * [`LabeledVideoDatasetIngestor.has_dataset_info`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.has_dataset_info)
      * [`LabeledVideoDatasetIngestor.has_video_metadata`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.has_video_metadata)
      * [`LabeledVideoDatasetIngestor.label_cls`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.label_cls)
      * [`LabeledVideoDatasetIngestor.frame_labels_cls`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.frame_labels_cls)
      * [`LabeledVideoDatasetIngestor.setup()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.setup)
      * [`LabeledVideoDatasetIngestor.close()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.close)
      * [`LabeledVideoDatasetIngestor.get_dataset_info()`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.LabeledVideoDatasetIngestor.get_dataset_info)
  * [fiftyone.utils.data.parsers](api__fiftyone.utils.data.parsers.md)
    * [`add_images()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.add_images)
    * [`add_labeled_images()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.add_labeled_images)
    * [`add_videos()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.add_videos)
    * [`add_labeled_videos()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.add_labeled_videos)
    * [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser)
      * [`SampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser.current_sample)
      * [`SampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser.with_sample)
      * [`SampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser.clear_sample)
    * [`UnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser)
      * [`UnlabeledImageSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.has_image_path)
      * [`UnlabeledImageSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.has_image_metadata)
      * [`UnlabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image)
      * [`UnlabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image_path)
      * [`UnlabeledImageSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.get_image_metadata)
      * [`UnlabeledImageSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.clear_sample)
      * [`UnlabeledImageSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.current_sample)
      * [`UnlabeledImageSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser.with_sample)
    * [`UnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser)
      * [`UnlabeledVideoSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.has_video_metadata)
      * [`UnlabeledVideoSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.get_video_path)
      * [`UnlabeledVideoSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.get_video_metadata)
      * [`UnlabeledVideoSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.clear_sample)
      * [`UnlabeledVideoSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.current_sample)
      * [`UnlabeledVideoSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser.with_sample)
    * [`UnlabeledMediaSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser)
      * [`UnlabeledMediaSampleParser.has_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.has_metadata)
      * [`UnlabeledMediaSampleParser.get_media_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.get_media_path)
      * [`UnlabeledMediaSampleParser.get_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.get_metadata)
      * [`UnlabeledMediaSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.clear_sample)
      * [`UnlabeledMediaSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.current_sample)
      * [`UnlabeledMediaSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser.with_sample)
    * [`ImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser)
      * [`ImageSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.has_image_path)
      * [`ImageSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.has_image_metadata)
      * [`ImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.get_image)
      * [`ImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.get_image_path)
      * [`ImageSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.clear_sample)
      * [`ImageSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.current_sample)
      * [`ImageSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.get_image_metadata)
      * [`ImageSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageSampleParser.with_sample)
    * [`VideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser)
      * [`VideoSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.has_video_metadata)
      * [`VideoSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.get_video_path)
      * [`VideoSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.clear_sample)
      * [`VideoSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.current_sample)
      * [`VideoSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.get_video_metadata)
      * [`VideoSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoSampleParser.with_sample)
    * [`MediaSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser)
      * [`MediaSampleParser.has_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.has_metadata)
      * [`MediaSampleParser.get_media_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.get_media_path)
      * [`MediaSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.clear_sample)
      * [`MediaSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.current_sample)
      * [`MediaSampleParser.get_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.get_metadata)
      * [`MediaSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser.with_sample)
    * [`LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser)
      * [`LabeledImageSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.has_image_path)
      * [`LabeledImageSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.has_image_metadata)
      * [`LabeledImageSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.label_cls)
      * [`LabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image)
      * [`LabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image_path)
      * [`LabeledImageSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_image_metadata)
      * [`LabeledImageSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.get_label)
      * [`LabeledImageSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.clear_sample)
      * [`LabeledImageSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.current_sample)
      * [`LabeledImageSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser.with_sample)
    * [`LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser)
      * [`LabeledVideoSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.has_video_metadata)
      * [`LabeledVideoSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.label_cls)
      * [`LabeledVideoSampleParser.frame_labels_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.frame_labels_cls)
      * [`LabeledVideoSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.get_video_path)
      * [`LabeledVideoSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.get_video_metadata)
      * [`LabeledVideoSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.get_label)
      * [`LabeledVideoSampleParser.get_frame_labels()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.get_frame_labels)
      * [`LabeledVideoSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.clear_sample)
      * [`LabeledVideoSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.current_sample)
      * [`LabeledVideoSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser.with_sample)
    * [`LabeledImageTupleSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser)
      * [`LabeledImageTupleSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.has_image_path)
      * [`LabeledImageTupleSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.has_image_metadata)
      * [`LabeledImageTupleSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.label_cls)
      * [`LabeledImageTupleSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.get_image)
      * [`LabeledImageTupleSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.get_image_path)
      * [`LabeledImageTupleSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.get_label)
      * [`LabeledImageTupleSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.clear_sample)
      * [`LabeledImageTupleSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.current_sample)
      * [`LabeledImageTupleSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.get_image_metadata)
      * [`LabeledImageTupleSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser.with_sample)
    * [`ImageClassificationSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser)
      * [`ImageClassificationSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.label_cls)
      * [`ImageClassificationSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.get_label)
      * [`ImageClassificationSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.clear_sample)
      * [`ImageClassificationSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.current_sample)
      * [`ImageClassificationSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.get_image)
      * [`ImageClassificationSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.get_image_metadata)
      * [`ImageClassificationSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.get_image_path)
      * [`ImageClassificationSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.has_image_metadata)
      * [`ImageClassificationSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.has_image_path)
      * [`ImageClassificationSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser.with_sample)
    * [`ImageDetectionSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser)
      * [`ImageDetectionSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.label_cls)
      * [`ImageDetectionSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.get_label)
      * [`ImageDetectionSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.clear_sample)
      * [`ImageDetectionSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.current_sample)
      * [`ImageDetectionSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.get_image)
      * [`ImageDetectionSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.get_image_metadata)
      * [`ImageDetectionSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.get_image_path)
      * [`ImageDetectionSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.has_image_metadata)
      * [`ImageDetectionSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.has_image_path)
      * [`ImageDetectionSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser.with_sample)
    * [`ImageLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser)
      * [`ImageLabelsSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.label_cls)
      * [`ImageLabelsSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.get_label)
      * [`ImageLabelsSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.clear_sample)
      * [`ImageLabelsSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.current_sample)
      * [`ImageLabelsSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.get_image)
      * [`ImageLabelsSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.get_image_metadata)
      * [`ImageLabelsSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.get_image_path)
      * [`ImageLabelsSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.has_image_metadata)
      * [`ImageLabelsSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.has_image_path)
      * [`ImageLabelsSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser.with_sample)
    * [`FiftyOneImageClassificationSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser)
      * [`FiftyOneImageClassificationSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.clear_sample)
      * [`FiftyOneImageClassificationSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.current_sample)
      * [`FiftyOneImageClassificationSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.get_image)
      * [`FiftyOneImageClassificationSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.get_image_metadata)
      * [`FiftyOneImageClassificationSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.get_image_path)
      * [`FiftyOneImageClassificationSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.get_label)
      * [`FiftyOneImageClassificationSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.has_image_metadata)
      * [`FiftyOneImageClassificationSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.has_image_path)
      * [`FiftyOneImageClassificationSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.label_cls)
      * [`FiftyOneImageClassificationSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageClassificationSampleParser.with_sample)
    * [`FiftyOneTemporalDetectionSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser)
      * [`FiftyOneTemporalDetectionSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.has_video_metadata)
      * [`FiftyOneTemporalDetectionSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.label_cls)
      * [`FiftyOneTemporalDetectionSampleParser.frame_labels_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.frame_labels_cls)
      * [`FiftyOneTemporalDetectionSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.with_sample)
      * [`FiftyOneTemporalDetectionSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.get_video_path)
      * [`FiftyOneTemporalDetectionSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.get_video_metadata)
      * [`FiftyOneTemporalDetectionSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.get_label)
      * [`FiftyOneTemporalDetectionSampleParser.get_frame_labels()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.get_frame_labels)
      * [`FiftyOneTemporalDetectionSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.clear_sample)
      * [`FiftyOneTemporalDetectionSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneTemporalDetectionSampleParser.current_sample)
    * [`FiftyOneImageDetectionSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser)
      * [`FiftyOneImageDetectionSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.clear_sample)
      * [`FiftyOneImageDetectionSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.current_sample)
      * [`FiftyOneImageDetectionSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.get_image)
      * [`FiftyOneImageDetectionSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.get_image_metadata)
      * [`FiftyOneImageDetectionSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.get_image_path)
      * [`FiftyOneImageDetectionSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.get_label)
      * [`FiftyOneImageDetectionSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.has_image_metadata)
      * [`FiftyOneImageDetectionSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.has_image_path)
      * [`FiftyOneImageDetectionSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.label_cls)
      * [`FiftyOneImageDetectionSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageDetectionSampleParser.with_sample)
    * [`FiftyOneImageLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser)
      * [`FiftyOneImageLabelsSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.clear_sample)
      * [`FiftyOneImageLabelsSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.current_sample)
      * [`FiftyOneImageLabelsSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.get_image)
      * [`FiftyOneImageLabelsSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.get_image_metadata)
      * [`FiftyOneImageLabelsSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.get_image_path)
      * [`FiftyOneImageLabelsSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.get_label)
      * [`FiftyOneImageLabelsSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.has_image_metadata)
      * [`FiftyOneImageLabelsSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.has_image_path)
      * [`FiftyOneImageLabelsSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.label_cls)
      * [`FiftyOneImageLabelsSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneImageLabelsSampleParser.with_sample)
    * [`VideoLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser)
      * [`VideoLabelsSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.has_video_metadata)
      * [`VideoLabelsSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.label_cls)
      * [`VideoLabelsSampleParser.frame_labels_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.frame_labels_cls)
      * [`VideoLabelsSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.get_video_path)
      * [`VideoLabelsSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.get_label)
      * [`VideoLabelsSampleParser.get_frame_labels()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.get_frame_labels)
      * [`VideoLabelsSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.clear_sample)
      * [`VideoLabelsSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.current_sample)
      * [`VideoLabelsSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.get_video_metadata)
      * [`VideoLabelsSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser.with_sample)
    * [`FiftyOneVideoLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser)
      * [`FiftyOneVideoLabelsSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.clear_sample)
      * [`FiftyOneVideoLabelsSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.current_sample)
      * [`FiftyOneVideoLabelsSampleParser.frame_labels_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.frame_labels_cls)
      * [`FiftyOneVideoLabelsSampleParser.get_frame_labels()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.get_frame_labels)
      * [`FiftyOneVideoLabelsSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.get_label)
      * [`FiftyOneVideoLabelsSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.get_video_metadata)
      * [`FiftyOneVideoLabelsSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.get_video_path)
      * [`FiftyOneVideoLabelsSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.has_video_metadata)
      * [`FiftyOneVideoLabelsSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.label_cls)
      * [`FiftyOneVideoLabelsSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneVideoLabelsSampleParser.with_sample)
    * [`FiftyOneUnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser)
      * [`FiftyOneUnlabeledImageSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.has_image_path)
      * [`FiftyOneUnlabeledImageSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.has_image_metadata)
      * [`FiftyOneUnlabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.get_image)
      * [`FiftyOneUnlabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.get_image_path)
      * [`FiftyOneUnlabeledImageSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.get_image_metadata)
      * [`FiftyOneUnlabeledImageSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.clear_sample)
      * [`FiftyOneUnlabeledImageSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.current_sample)
      * [`FiftyOneUnlabeledImageSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledImageSampleParser.with_sample)
    * [`FiftyOneLabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser)
      * [`FiftyOneLabeledImageSampleParser.has_image_path`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.has_image_path)
      * [`FiftyOneLabeledImageSampleParser.has_image_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.has_image_metadata)
      * [`FiftyOneLabeledImageSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.label_cls)
      * [`FiftyOneLabeledImageSampleParser.get_image()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.get_image)
      * [`FiftyOneLabeledImageSampleParser.get_image_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.get_image_path)
      * [`FiftyOneLabeledImageSampleParser.get_image_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.get_image_metadata)
      * [`FiftyOneLabeledImageSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.get_label)
      * [`FiftyOneLabeledImageSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.clear_sample)
      * [`FiftyOneLabeledImageSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.current_sample)
      * [`FiftyOneLabeledImageSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledImageSampleParser.with_sample)
    * [`ExtractClipsMixin`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ExtractClipsMixin)
    * [`FiftyOneUnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser)
      * [`FiftyOneUnlabeledVideoSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.has_video_metadata)
      * [`FiftyOneUnlabeledVideoSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.get_video_path)
      * [`FiftyOneUnlabeledVideoSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.get_video_metadata)
      * [`FiftyOneUnlabeledVideoSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.clear_sample)
      * [`FiftyOneUnlabeledVideoSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.current_sample)
      * [`FiftyOneUnlabeledVideoSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledVideoSampleParser.with_sample)
    * [`FiftyOneLabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser)
      * [`FiftyOneLabeledVideoSampleParser.has_video_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.has_video_metadata)
      * [`FiftyOneLabeledVideoSampleParser.label_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.label_cls)
      * [`FiftyOneLabeledVideoSampleParser.frame_labels_cls`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.frame_labels_cls)
      * [`FiftyOneLabeledVideoSampleParser.get_video_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.get_video_path)
      * [`FiftyOneLabeledVideoSampleParser.get_video_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.get_video_metadata)
      * [`FiftyOneLabeledVideoSampleParser.get_label()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.get_label)
      * [`FiftyOneLabeledVideoSampleParser.get_frame_labels()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.get_frame_labels)
      * [`FiftyOneLabeledVideoSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.clear_sample)
      * [`FiftyOneLabeledVideoSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.current_sample)
      * [`FiftyOneLabeledVideoSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneLabeledVideoSampleParser.with_sample)
    * [`FiftyOneUnlabeledMediaSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser)
      * [`FiftyOneUnlabeledMediaSampleParser.has_metadata`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.has_metadata)
      * [`FiftyOneUnlabeledMediaSampleParser.get_media_path()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.get_media_path)
      * [`FiftyOneUnlabeledMediaSampleParser.get_metadata()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.get_metadata)
      * [`FiftyOneUnlabeledMediaSampleParser.clear_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.clear_sample)
      * [`FiftyOneUnlabeledMediaSampleParser.current_sample`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.current_sample)
      * [`FiftyOneUnlabeledMediaSampleParser.with_sample()`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.FiftyOneUnlabeledMediaSampleParser.with_sample)



## Module contents#

Data utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`F` |   
---|---  
`defaultdict` | defaultdict(default_factory=None, /, [...]) --> dict with default factory  
`FiftyOneLabeledImageSampleParser`(label_field) | Parser for `fiftyone.core.sample.Sample` instances that contain labeled images.  
`FiftyOneLabeledVideoSampleParser`([...]) | Parser for `fiftyone.core.sample.Sample` instances that contain labeled videos.  
`FiftyOneUnlabeledImageSampleParser`([...]) | Parser for `fiftyone.core.sample.Sample` instances that contain images.  
`FiftyOneUnlabeledMediaSampleParser`([...]) | Parser for `fiftyone.core.sample.Sample` instances that contain unlabeled media.  
`FiftyOneUnlabeledVideoSampleParser`([...]) | Parser for `fiftyone.core.sample.Sample` instances that contain videos.  
`ImageClassificationSampleParser`([classes]) | Generic parser for image classification(s) samples whose labels are represented as [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") instances.  
`ImageSampleParser`() | Sample parser that parses unlabeled image samples.  
`ExportPathsMixin`() | Mixin for `DatasetExporter` classes that provides convenience methods for parsing the `data_path`, `labels_path`, and `export_media` parameters supported by many exporters.  
`MediaExporter`(export_mode[,Â export_path,Â ...]) | Base class for `DatasetExporter` utilities that provide support for populating a directory or manifest of media files.  
`ImageExporter`(*args[,Â default_ext]) | Utility class for `DatasetExporter` instances that export images.  
`VideoExporter`(*args[,Â default_ext]) | Utility class for `DatasetExporter` instances that export videos.  
`DatasetExporter`([export_dir]) | Base interface for exporting datasets.  
`BatchDatasetExporter`([export_dir]) | Base interface for exporters that export entire [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances in a single batch.  
`GenericSampleDatasetExporter`([export_dir]) | Interface for exporting datasets of arbitrary `fiftyone.core.sample.Sample` instances.  
`GroupDatasetExporter`([export_dir]) | Interface for exporting grouped datasets.  
`UnlabeledImageDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled image samples.  
`UnlabeledVideoDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled video samples.  
`UnlabeledMediaDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled samples.  
`LabeledImageDatasetExporter`([export_dir]) | Interface for exporting datasets of labeled image samples.  
`LabeledVideoDatasetExporter`([export_dir]) | Interface for exporting datasets of labeled video samples.  
`LegacyFiftyOneDatasetExporter`(export_dir[,Â ...]) | Legacy exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.  
`FiftyOneDatasetExporter`(export_dir[,Â ...]) | Exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.  
`ImageDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of images to disk.  
`VideoDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of videos to disk.  
`MediaDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of media files of arbitrary type to disk.  
`FiftyOneImageClassificationDatasetExporter`([...]) | Exporter that writes an image classification dataset to disk in a simple JSON format.  
`ImageClassificationDirectoryTreeExporter`(...) | Exporter that writes an image classification directory tree to disk.  
`VideoClassificationDirectoryTreeExporter`(...) | Exporter that writes a video classification directory tree to disk.  
`FiftyOneImageDetectionDatasetExporter`([...]) | Exporter that writes an image detection dataset to disk in a simple JSON format.  
`FiftyOneTemporalDetectionDatasetExporter`([...]) | Exporter that writes a temporal video detection dataset to disk in a simple JSON format.  
`ImageSegmentationDirectoryExporter`([...]) | Exporter that writes an image segmentation dataset to disk.  
`FiftyOneImageLabelsDatasetExporter`(export_dir) | Exporter that writes a labeled image dataset to disk with labels stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).  
`FiftyOneVideoLabelsDatasetExporter`(export_dir) | Exporter that writes a labeled video dataset with labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).  
`datetime`(year,Â month,Â day[,Â hour[,Â minute[,Â ...) | The year, month and day arguments are required.  
`Sample`(filepath[,Â tags,Â metadata]) | A sample in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").  
`FiftyOneImageClassificationSampleParser`([...]) | Parser for samples in FiftyOne image classification datasets.  
`FiftyOneTemporalDetectionSampleParser`([...]) | Parser for samples in FiftyOne temporal detection datasets.  
`FiftyOneImageDetectionSampleParser`([classes]) | Parser for samples in FiftyOne image detection datasets.  
`FiftyOneImageLabelsSampleParser`([prefix,Â ...]) | Parser for samples in FiftyOne image labels datasets.  
`FiftyOneVideoLabelsSampleParser`([prefix,Â ...]) | Parser for samples in FiftyOne video labels datasets.  
`ImportPathsMixin`() | Mixin for `DatasetImporter` classes that provides convenience methods for parsing the `data_path` and `labels_path` parameters supported by many importers.  
`DatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Base interface for importing datasets stored on disk into FiftyOne.  
`BatchDatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Base interface for importers that load all of their samples in a single call to `import_samples()`.  
`GenericSampleDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets that contain arbitrary `fiftyone.core.sample.Sample` instances.  
`GroupDatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Interface for importing datasets that contain arbitrary grouped `fiftyone.core.sample.Sample` instances.  
`UnlabeledImageDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled image samples.  
`UnlabeledVideoDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled video samples.  
`UnlabeledMediaDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled media samples.  
`LabeledImageDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of labeled image samples.  
`LabeledVideoDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of labeled video samples.  
`LegacyFiftyOneDatasetImporter`(dataset_dir[,Â ...]) | Legacy importer for FiftyOne datasets stored on disk in a serialized JSON format.  
`FiftyOneDatasetImporter`(dataset_dir[,Â ...]) | Importer for FiftyOne datasets stored on disk in serialized JSON format.  
`ImageDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of images stored on disk.  
`VideoDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of videos stored on disk.  
`MediaDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of media files stored on disk.  
`FiftyOneImageClassificationDatasetImporter`([...]) | Importer for image classification datasets stored on disk in a simple JSON format.  
`ImageClassificationDirectoryTreeImporter`(...) | Importer for an image classification directory tree stored on disk.  
`VideoClassificationDirectoryTreeImporter`(...) | Importer for a viideo classification directory tree stored on disk.  
`FiftyOneImageDetectionDatasetImporter`([...]) | Importer for image detection datasets stored on disk in a simple JSON format.  
`FiftyOneTemporalDetectionDatasetImporter`([...]) | Importer for temporal video detection datasets stored on disk in a simple JSON format.  
`ImageSegmentationDirectoryImporter`([...]) | Importer for image segmentation datasets stored on disk.  
`FiftyOneImageLabelsDatasetImporter`(dataset_dir) | Importer for labeled image datasets whose labels are stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).  
`FiftyOneVideoLabelsDatasetImporter`(dataset_dir) | Importer for labeled video datasets whose labels are stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).  
`ImageIngestor`(dataset_dir[,Â image_format]) | Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest images into the provided `dataset_dir` during import.  
`UnlabeledImageDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests unlabeled images into the provided `dataset_dir` during import.  
`LabeledImageDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests labeled images into the provided `dataset_dir` during import.  
`VideoIngestor`(dataset_dir) | Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest videos into the provided `dataset_dir` during import.  
`UnlabeledVideoDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests unlabeled videos into the provided `dataset_dir` during import.  
`LabeledVideoDatasetIngestor`(dataset_dir,Â ...) | Dataset importer that ingests labeled videos into the provided `dataset_dir` during import.  
`SampleParser`() | Base interface for sample parsers.  
`UnlabeledImageSampleParser`() | Interface for `SampleParser` instances that parse unlabeled image samples.  
`UnlabeledVideoSampleParser`() | Interface for `SampleParser` instances that parse unlabeled video samples.  
`UnlabeledMediaSampleParser`() | Interface for `SampleParser` instances that parse unlabeled media samples.  
`VideoSampleParser`() | Sample parser that parses unlabeled video samples.  
`MediaSampleParser`() | Sample parser that parses unlabeled media samples.  
`LabeledImageSampleParser`() | Interface for `SampleParser` instances that parse labeled image samples.  
`LabeledVideoSampleParser`() | Interface for `SampleParser` instances that parse labeled video samples.  
`LabeledImageTupleSampleParser`() | Generic sample parser that parses samples that are `(image_or_path, label)` tuples, where:  
`ImageDetectionSampleParser`([label_field,Â ...]) | Generic parser for image detection samples whose labels are represented as [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instances.  
`ImageLabelsSampleParser`([prefix,Â ...]) | Generic parser for multitask image prediction samples whose labels are stored in `eta.core.image.ImageLabels` format.  
`VideoLabelsSampleParser`([prefix,Â ...]) | Generic parser for labeled video samples whose labels are represented in `eta.core.video.VideoLabels` format.  
`ExtractClipsMixin`([compute_metadata,Â ...]) | Mixin for sample parsers that extract clips from [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.  
  
**Functions:**

`map_values`(sample_collection,Â path,Â map[,Â ...]) | Maps the values in the given field to new values for each sample in the collection.  
---|---  
`parse_images_dir`(dataset_dir[,Â recursive]) | Parses the contents of the given directory of images.  
`parse_videos_dir`(dataset_dir[,Â recursive]) | Parses the contents of the given directory of videos.  
`parse_image_classification_dir_tree`(dataset_dir) | Parses the contents of the given image classification dataset directory tree, which should have the following format.  
`download_image_classification_dataset`(...[,Â ...]) | Downloads the classification dataset specified by the given CSV file, which should have the following format.  
`download_images`(image_urls,Â output_dir[,Â ...]) | Downloads the images from the given URLs.  
`build_dataset_exporter`(dataset_type[,Â ...]) | Builds the `DatasetExporter` instance for the given parameters.  
`build_dataset_importer`(dataset_type[,Â ...]) | Builds the `DatasetImporter` instance for the given parameters.  
`convert_dataset`([input_dir,Â input_type,Â ...]) | Converts a dataset stored on disk to another format on disk.  
`export_samples`(samples[,Â export_dir,Â ...]) | Exports the given samples to disk.  
`write_dataset`(samples,Â sample_parser,Â ...[,Â ...]) | Writes the samples to disk as a dataset in the specified format.  
`get_document`(name) | Get a registered Document class by name.  
`import_samples`(dataset,Â dataset_importer[,Â ...]) | Adds the samples from the given `DatasetImporter` to the dataset.  
`merge_samples`(dataset,Â dataset_importer[,Â ...]) | Merges the samples from the given `DatasetImporter` into the dataset.  
`parse_dataset_info`(dataset,Â info[,Â overwrite]) | Parses the info returned by `DatasetImporter.get_dataset_info()` and stores it on the relevant properties of the dataset.  
`add_images`(dataset,Â samples,Â sample_parser) | Adds the given images to the dataset.  
`add_labeled_images`(dataset,Â samples,Â ...[,Â ...]) | Adds the given labeled images to the dataset.  
`add_videos`(dataset,Â samples,Â sample_parser) | Adds the given videos to the dataset.  
`add_labeled_videos`(dataset,Â samples,Â ...[,Â ...]) | Adds the given labeled videos to the dataset.  
  
fiftyone.utils.data.F#
    

alias of [`ViewField`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewField "fiftyone.core.expressions.ViewField")

fiftyone.utils.data.map_values(_sample_collection_ , _path_ , _map_ , _progress =False_)#
    

Maps the values in the given field to new values for each sample in the collection.

This function performs the same operation as [`map_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_values "fiftyone.core.collections.SampleCollection.map_values") but it immediately saves the mapped values to the database rather than creating a view.

Examples:
    
    
    import random
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.data as foud
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    values = [random.choice(ANIMALS) for _ in range(len(dataset))]
    dataset.set_values("str_field", values)
    dataset.set_values("list_field", [[v] for v in values])
    
    dataset.set_field("ground_truth.detections.tags", [F("label")]).save()
    
    # Map all animals to string "animal"
    mapping = {a: "animal" for a in ANIMALS}
    
    #
    # Map values in top-level fields
    #
    
    foud.map_values(dataset, "str_field", mapping)
    
    print(dataset.count_values("str_field"))
    # {"animal": 200}
    
    foud.map_values(dataset, "list_field", mapping)
    
    print(dataset.count_values("list_field"))
    # {"animal": 200}
    
    #
    # Map values in nested fields
    #
    
    foud.map_values(dataset, "ground_truth.detections.label", mapping)
    
    print(dataset.count_values("ground_truth.detections.label"))
    # {"animal": 183, ...}
    
    foud.map_values(dataset, "ground_truth.detections.tags", mapping)
    
    print(dataset.count_values("ground_truth.detections.tags"))
    # {"animal": 183, ...}
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **path** â the field or `embedded.field.name` to map

  * **map** â a dict mapping values to new values

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.data.parse_images_dir(_dataset_dir_ , _recursive =True_)#
    

Parses the contents of the given directory of images.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories



Returns:
    

a list of image paths

fiftyone.utils.data.parse_videos_dir(_dataset_dir_ , _recursive =True_)#
    

Parses the contents of the given directory of videos.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories



Returns:
    

a list of video paths

fiftyone.utils.data.parse_image_classification_dir_tree(_dataset_dir_)#
    

Parses the contents of the given image classification dataset directory tree, which should have the following format:
    
    
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
    

**dataset_dir** â the dataset directory

Returns:
    

a list of `(image_path, target)` pairs classes: a list of class label strings

Return type:
    

[samples](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityIndex.samples "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityIndex.samples")

fiftyone.utils.data.download_image_classification_dataset(_csv_path_ , _dataset_dir_ , _classes =None_, _num_workers =None_)#
    

Downloads the classification dataset specified by the given CSV file, which should have the following format:
    
    
    <label1>,<image_url1>
    <label2>,<image_url2>
    ...
    

The image filenames are the basenames of the URLs, which are assumed to be unique.

The dataset is written to disk in [`fiftyone.types.FiftyOneImageClassificationDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneImageClassificationDataset "fiftyone.types.FiftyOneImageClassificationDataset") format.

Parameters:
    

  * **csv_path** â a CSV file containing the labels and image URLs

  * **dataset_dir** â the directory to write the dataset

  * **classes** (_None_) â an optional list of classes. By default, this will be inferred from the contents of `csv_path`

  * **num_workers** (_None_) â a suggested number of threads to use to download images




fiftyone.utils.data.download_images(_image_urls_ , _output_dir_ , _num_workers =None_)#
    

Downloads the images from the given URLs.

The filenames in `output_dir` are the basenames of the URLs, which are assumed to be unique.

Parameters:
    

  * **image_urls** â a list of image URLs to download

  * **output_dir** â the directory to write the images

  * **num_workers** (_None_) â a suggested number of threads to use



Returns:
    

the list of downloaded image paths

fiftyone.utils.data.build_dataset_exporter(_dataset_type_ , _strip_none =True_, _warn_unused =True_, _** kwargs_)#
    

Builds the `DatasetExporter` instance for the given parameters.

Parameters:
    

  * **dataset_type** â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type

  * **strip_none** (_True_) â whether to exclude None-valued items from `kwargs`

  * **warn_unused** (_True_) â whether to issue warnings for any non-None unused parameters encountered

  * ****kwargs** â keyword arguments to pass to the dataset exporterâs constructor via `DatasetExporter(**kwargs)`



Returns:
    

  * the `DatasetExporter` instance

  * a dict of unused keyword arguments




Return type:
    

a tuple of

fiftyone.utils.data.build_dataset_importer(_dataset_type_ , _strip_none =True_, _warn_unused =True_, _name =None_, _** kwargs_)#
    

Builds the `DatasetImporter` instance for the given parameters.

Parameters:
    

  * **dataset_type** â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type

  * **strip_none** (_True_) â whether to exclude None-valued items from `kwargs`

  * **warn_unused** (_True_) â whether to issue warnings for any non-None unused parameters encountered

  * **name** (_None_) â the name of the dataset being imported into, if known

  * ****kwargs** â keyword arguments to pass to the dataset importerâs constructor via `DatasetImporter(**kwargs)`



Returns:
    

  * the `DatasetImporter` instance

  * a dict of unused keyword arguments




Return type:
    

a tuple of

fiftyone.utils.data.convert_dataset(_input_dir =None_, _input_type =None_, _input_kwargs =None_, _dataset_importer =None_, _output_dir =None_, _output_type =None_, _output_kwargs =None_, _dataset_exporter =None_, _overwrite =False_)#
    

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




class fiftyone.utils.data.defaultdict#
    

Bases: `dict`

defaultdict(default_factory=None, /, [â¦]) â> dict with default factory

The default factory is called without arguments to produce a new value when a key is not present, in __getitem__ only. A defaultdict compares equal to a dict with the same items. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.

**Methods:**

`clear`() |   
---|---  
`copy`() |   
`fromkeys`(iterable[,Â value]) | Create a new dictionary with keys from iterable and values set to value.  
`get`(key[,Â default]) | Return the value for key if key is in the dictionary, else default.  
`items`() |   
`keys`() |   
`pop`(k[,d]) | If the key is not found, return the default if given; otherwise, raise a KeyError.  
`popitem`() | Remove and return a (key, value) pair as a 2-tuple.  
`setdefault`(key[,Â default]) | Insert key with a value of default if key is not in the dictionary.  
`update`([E,Â ]**F) | If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]  
`values`() |   
  
**Attributes:**

`default_factory` | Factory for default value called by __missing__().  
---|---  
  
clear() → None. Remove all items from D.#
    

copy() → a shallow copy of D.#
    

default_factory#
    

Factory for default value called by __missing__().

classmethod fromkeys(_iterable_ , _value =None_, _/_)#
    

Create a new dictionary with keys from iterable and values set to value.

get(_key_ , _default =None_, _/_)#
    

Return the value for key if key is in the dictionary, else default.

items() → a set-like object providing a view on D's items#
    

keys() → a set-like object providing a view on D's keys#
    

pop(_k_[, _d_]) → v, remove specified key and return the corresponding value.#
    

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()#
    

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(_key_ , _default =None_, _/_)#
    

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update([_E_ , ]_**F_) → None. Update D from dict/iterable E and F.#
    

If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values() → an object providing a view on D's values#
    

class fiftyone.utils.data.FiftyOneLabeledImageSampleParser(_label_field_ , _label_fcn =None_, _compute_metadata =False_)#
    

Bases: [`LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser "fiftyone.utils.data.parsers.LabeledImageSampleParser")

Parser for `fiftyone.core.sample.Sample` instances that contain labeled images.

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

class fiftyone.utils.data.FiftyOneLabeledVideoSampleParser(_label_field =None_, _frame_labels_field =None_, _label_fcn =None_, _frame_labels_fcn =None_, _compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: [`ExtractClipsMixin`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ExtractClipsMixin "fiftyone.utils.data.parsers.ExtractClipsMixin"), [`LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser "fiftyone.utils.data.parsers.LabeledVideoSampleParser")

Parser for `fiftyone.core.sample.Sample` instances that contain labeled videos.

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

class fiftyone.utils.data.FiftyOneUnlabeledImageSampleParser(_compute_metadata =False_)#
    

Bases: [`UnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser "fiftyone.utils.data.parsers.UnlabeledImageSampleParser")

Parser for `fiftyone.core.sample.Sample` instances that contain images.

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

class fiftyone.utils.data.FiftyOneUnlabeledMediaSampleParser(_compute_metadata =False_)#
    

Bases: [`MediaSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.MediaSampleParser "fiftyone.utils.data.parsers.MediaSampleParser")

Parser for `fiftyone.core.sample.Sample` instances that contain unlabeled media.

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

class fiftyone.utils.data.FiftyOneUnlabeledVideoSampleParser(_compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: [`ExtractClipsMixin`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ExtractClipsMixin "fiftyone.utils.data.parsers.ExtractClipsMixin"), [`UnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser "fiftyone.utils.data.parsers.UnlabeledVideoSampleParser")

Parser for `fiftyone.core.sample.Sample` instances that contain videos.

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

class fiftyone.utils.data.ImageClassificationSampleParser(_classes =None_)#
    

Bases: [`LabeledImageTupleSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser "fiftyone.utils.data.parsers.LabeledImageTupleSampleParser")

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

class fiftyone.utils.data.ImageSampleParser#
    

Bases: [`UnlabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledImageSampleParser "fiftyone.utils.data.parsers.UnlabeledImageSampleParser")

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

fiftyone.utils.data.export_samples(_samples_ , _export_dir =None_, _dataset_type =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _dataset_exporter =None_, _label_field =None_, _frame_labels_field =None_, _progress =None_, _num_samples =None_, _** kwargs_)#
    

Exports the given samples to disk.

You can perform exports with this method via the following basic patterns:

  1. Provide `export_dir` and `dataset_type` to export the content to a directory in the default layout for the specified format, as documented in [this page](user_guide__export_datasets.md#exporting-datasets)

  2. Provide `dataset_type` along with `data_path`, `labels_path`, and/or `export_media` to directly specify where to export the source media and/or labels (if applicable) in your desired format. This syntax provides the flexibility to, for example, perform workflows like labels-only exports

  3. Provide a `dataset_exporter` to which to feed samples to perform a fully-customized export




In all workflows, the remaining parameters of this method can be provided to further configure the export.

See [this page](user_guide__export_datasets.md#exporting-datasets) for more information about the available export formats and examples of using this method.

See [this guide](user_guide__export_datasets.md#custom-dataset-exporter) for more details about exporting datasets in custom formats by defining your own [`fiftyone.utils.data.exporters.DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter").

This method will automatically coerce the data to match the requested export in the following cases:

  * When exporting in either an unlabeled image or image classification format, if a spatial label field is provided ([`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), then the **image patches** of the provided samples will be exported

  * When exporting in labeled image dataset formats that expect list-type labels ([`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), if a label field contains labels in non-list format (e.g., [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")), the labels will be automatically upgraded to single-label lists

  * When exporting in labeled image dataset formats that expect [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") labels, if a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field is provided, the labels will be automatically upgraded to detections that span the entire images




Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **export_dir** (_None_) â the directory to which to export the samples in format `dataset_type`

  * **dataset_type** (_None_) â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type to write

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media for certain export formats. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of a JSON manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, a default value of this parameter will be chosen based on the value of the `export_media` parameter. Note that this parameter is not applicable to certain export formats such as binary types like TF records

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Only applicable when exporting in certain labeled dataset formats. Can be any of the following:

    * a type-specific folder name like `"labels"` or `"labels/"` or a filename like `"labels.json"` or `"labels.xml"` specifying the location in `export_dir` in which to export the labels

    * an absolute directory or filepath in which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

For labeled datasets, the default value of this parameter will be chosen based on the export format so that the labels will be exported into `export_dir`

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media. This option is only useful when exporting labeled datasets whose label format stores sufficient information to locate the associated media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, an appropriate default value of this parameter will be chosen based on the value of the `data_path` parameter. Note that some dataset formats may not support certain values for this parameter (e.g., when exporting in binary formats such as TF records, âsymlinkâ is not an option)

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **dataset_exporter** (_None_) â a `DatasetExporter` to use to write the dataset

  * **label_field** (_None_) â the name of the label field to export, or a dictionary mapping field names to output keys describing the label fields to export. Only applicable if `dataset_exporter` is a `LabeledImageDatasetExporter` or `LabeledVideoDatasetExporter`, or if you are exporting image patches

  * **frame_labels_field** (_None_) â the name of the frame label field to export, or a dictionary mapping field names to output keys describing the frame label fields to export. Only applicable if `dataset_exporter` is a `LabeledVideoDatasetExporter`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_samples** (_None_) â the number of samples in `samples`. If omitted, this is computed (if possible) via `len(samples)` if needed for progress tracking

  * ****kwargs** â optional keyword arguments to pass to the dataset exporterâs constructor. If you are exporting image patches, this can also contain keyword arguments for [`fiftyone.utils.patches.ImagePatchesExtractor`](api__fiftyone.utils.patches.md#fiftyone.utils.patches.ImagePatchesExtractor "fiftyone.utils.patches.ImagePatchesExtractor")




fiftyone.utils.data.write_dataset(_samples_ , _sample_parser_ , _dataset_exporter_ , _sample_collection =None_, _progress =None_, _num_samples =None_)#
    

Writes the samples to disk as a dataset in the specified format.

Parameters:
    

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a [`fiftyone.utils.data.parsers.SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser") to use to parse the samples

  * **dataset_exporter** â a `DatasetExporter` to use to write the dataset

  * **sample_collection** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") from which `samples` were extracted. If `samples` is itself a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), this parameter defaults to `samples`. This parameter is optional and is only passed to `DatasetExporter.log_collection()`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_samples** (_None_) â the number of samples in `samples`. If omitted, this is computed (if possible) via `len(samples)` if needed for progress tracking




class fiftyone.utils.data.ExportPathsMixin#
    

Bases: `object`

Mixin for `DatasetExporter` classes that provides convenience methods for parsing the `data_path`, `labels_path`, and `export_media` parameters supported by many exporters.

class fiftyone.utils.data.MediaExporter(_export_mode_ , _export_path =None_, _rel_dir =None_, _chunk_size =None_, _supported_modes =None_, _default_ext =None_, _ignore_exts =False_)#
    

Bases: `object`

Base class for `DatasetExporter` utilities that provide support for populating a directory or manifest of media files.

This class is designed for populating a single, flat directory or manifest of media files, and automatically takes care of things like name clashes as necessary.

The export strategy used is defined by the `export_mode` parameter, and users of this class can restrict the available options via the `supported_modes` parameter.

Parameters:
    

  * **export_mode** â 

the export mode to use. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media. This option is only useful when exporting labeled datasets whose label format stores sufficient information to locate the associated media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

  * **export_path** (_None_) â 

the location to export the media. Can be any of the following:

    * When `export_media` is True, âmoveâ, or âsymlinkâ, a directory in which to export the media

    * When `export_mode` is âmanifestâ, the path to write a JSON file mapping UUIDs to input filepaths

    * When `export_media` is False, this parameter has no effect

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **supported_modes** (_None_) â an optional tuple specifying a subset of the `export_mode` values that are allowed

  * **default_ext** (_None_) â the file extension to use when generating default output paths

  * **ignore_exts** (_False_) â whether to omit file extensions when generating UUIDs for files




**Methods:**

`setup`() | Performs necessary setup to begin exporting media.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`close`() | Performs any necessary actions to complete the export.  
  
setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

close()#
    

Performs any necessary actions to complete the export.

class fiftyone.utils.data.ImageExporter(_* args_, _default_ext =None_, _** kwargs_)#
    

Bases: [`MediaExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter "fiftyone.utils.data.exporters.MediaExporter")

Utility class for `DatasetExporter` instances that export images.

See `MediaExporter` for details.

**Methods:**

`close`() | Performs any necessary actions to complete the export.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`setup`() | Performs necessary setup to begin exporting media.  
  
close()#
    

Performs any necessary actions to complete the export.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

class fiftyone.utils.data.VideoExporter(_* args_, _default_ext =None_, _** kwargs_)#
    

Bases: [`MediaExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.MediaExporter "fiftyone.utils.data.exporters.MediaExporter")

Utility class for `DatasetExporter` instances that export videos.

See `MediaExporter` for details.

**Methods:**

`close`() | Performs any necessary actions to complete the export.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`setup`() | Performs necessary setup to begin exporting media.  
  
close()#
    

Performs any necessary actions to complete the export.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

class fiftyone.utils.data.DatasetExporter(_export_dir =None_)#
    

Bases: `object`

Base interface for exporting datasets.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.data.BatchDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Base interface for exporters that export entire [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances in a single batch.

This interface allows for greater efficiency for export formats that handle aggregating over the samples themselves.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
---|---  
`export_samples`(sample_collection[,Â progress]) | Exports the given sample collection.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.GenericSampleDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of arbitrary `fiftyone.core.sample.Sample` instances.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(sample) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_sample_)#
    

Exports the given sample to the dataset.

Parameters:
    

**sample** â a `fiftyone.core.sample.Sample`

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.GroupDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting grouped datasets.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
---|---  
`export_group`(group) | Exports the given group to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




export_group(_group_)#
    

Exports the given group to the dataset.

Parameters:
    

**group** â a dict mapping group slice names to `fiftyone.core.sample.Sample` instances

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.UnlabeledImageDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of unlabeled image samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(image_or_path[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

export_sample(_image_or_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.UnlabeledVideoDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of unlabeled video samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(video_path[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

export_sample(_video_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.UnlabeledMediaDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of unlabeled samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_metadata` | Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(filepath[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.

export_sample(_filepath_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **filepath** â a media path

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the sample. Only required when `requires_metadata()` is `True`




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.LabeledImageDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of labeled image samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.LabeledVideoDatasetExporter(_export_dir =None_)#
    

Bases: [`DatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.DatasetExporter "fiftyone.utils.data.exporters.DatasetExporter")

Interface for exporting datasets of labeled video samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`export_sample`(video_path,Â label,Â frames[,Â ...]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple label fields with value-types specified by this dictionary. Not all keys need be present in the exported sample-level labels

  * `None`. In this case, the exporter makes no guarantees about the sample-level labels that it can export




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple frame label fields with value-types specified by this dictionary. Not all keys need be present in the exported frame labels

  * `None`. In this case, the exporter makes no guarantees about the frame labels that it can export




export_sample(_video_path_ , _label_ , _frames_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

  * **frames** â a dictionary mapping frame numbers to dictionaries that map field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no frame-level labels

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.LegacyFiftyOneDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _chunk_size =None_, _abs_paths =False_, _export_saved_views =True_, _export_runs =True_, _export_workspaces =True_, _pretty_print =False_)#
    

Bases: [`GenericSampleDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.GenericSampleDatasetExporter "fiftyone.utils.data.exporters.GenericSampleDatasetExporter")

Legacy exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.

Warning

The [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format was upgraded in `fiftyone==0.8` and this exporter is now deprecated. The new exporter is `FiftyOneDatasetExporter`.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `False`: donât export media

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **abs_paths** (_False_) â whether to store absolute paths to the media in the exported labels

  * **export_saved_views** (_True_) â whether to include saved views in the export. Only applicable when exporting full datasets

  * **export_runs** (_True_) â whether to include annotation/brain/evaluation runs in the export. Only applicable when exporting full datasets

  * **export_workspaces** (_True_) â whether to include saved workspaces in the export. Only applicable when exporting full datasets

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(sample) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_sample_)#
    

Exports the given sample to the dataset.

Parameters:
    

**sample** â a `fiftyone.core.sample.Sample`

close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.data.FiftyOneDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _chunk_size =None_, _export_saved_views =True_, _export_runs =True_, _export_workspaces =True_, _use_dirs =False_, _ordered =True_)#
    

Bases: [`BatchDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.BatchDatasetExporter "fiftyone.utils.data.exporters.BatchDatasetExporter")

Exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.

See [this page](user_guide__export_datasets.md#fiftyonedataset-export) for format details.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `False`: donât export media

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **export_saved_views** (_True_) â whether to include saved views in the export. Only applicable when exporting full datasets

  * **export_runs** (_True_) â whether to include annotation/brain/evaluation runs in the export. Only applicable when exporting full datasets

  * **export_workspaces** (_True_) â whether to include saved workspaces in the export. Only applicable when exporting full datasets

  * **use_dirs** (_False_) â whether to export metadata into directories of per sample/frame files

  * **ordered** (_True_) â whether to preserve the order of the exported collections




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

class fiftyone.utils.data.ImageDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_)#
    

Bases: [`UnlabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter "fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter")

Exporter that writes a directory of images to disk.

See [this page](user_guide__export_datasets.md#imagedirectory-export) for format details.

The filenames of input image paths will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_image_or_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

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

class fiftyone.utils.data.VideoDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: [`UnlabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter "fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter")

Exporter that writes a directory of videos to disk.

See [this page](user_guide__export_datasets.md#videodirectory-export) for format details.

The filenames of the input videos will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_video_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

class fiftyone.utils.data.MediaDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: [`UnlabeledMediaDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter "fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter")

Exporter that writes a directory of media files of arbitrary type to disk.

See [this page](user_guide__export_datasets.md#mediadirectory-export) for format details.

The filenames of the input media files will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each output file. This identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_metadata` | Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(filepath[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_filepath_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **filepath** â a media path

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the sample. Only required when `requires_metadata()` is `True`




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

class fiftyone.utils.data.FiftyOneImageClassificationDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _include_confidence =False_, _include_attributes =False_, _classes =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes an image classification dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyoneimageclassificationdataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **include_confidence** (_False_) â 

whether to include classification confidences in the export. The supported values are:

    * `False` (default): do not include confidences

    * `True`: always include confidences

    * `None`: include confidences only if they exist

  * **include_attributes** (_False_) â 

whether to include dynamic attributes of the classifications in the export. Supported values are:

    * `False` (default): do not include attributes

    * `True`: always include a (possibly empty) attributes dict

    * `None`: include attributes only if they exist

    * a name or iterable of names of specific attributes to include

  * **classes** (_None_) â the list of possible class labels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.data.ImageClassificationDirectoryTreeExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter")

Exporter that writes an image classification directory tree to disk.

See [this page](user_guide__export_datasets.md#imageclassificationdirectorytree-export) for format details.

The filenames of the input images are maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â classification) | Exports the given sample to the dataset.  
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

export_sample(_image_or_path_ , _classification_ , _metadata =None_)#
    

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

class fiftyone.utils.data.VideoClassificationDirectoryTreeExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: [`LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter")

Exporter that writes a video classification directory tree to disk.

See [this page](user_guide__export_datasets.md#videoclassificationdirectorytree-export) for format details.

The filenames of the input images are maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path,Â classification,Â _) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple label fields with value-types specified by this dictionary. Not all keys need be present in the exported sample-level labels

  * `None`. In this case, the exporter makes no guarantees about the sample-level labels that it can export




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple frame label fields with value-types specified by this dictionary. Not all keys need be present in the exported frame labels

  * `None`. In this case, the exporter makes no guarantees about the frame labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_video_path_ , _classification_ , ___ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

  * **frames** â a dictionary mapping frame numbers to dictionaries that map field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no frame-level labels

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

class fiftyone.utils.data.FiftyOneImageDetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _classes =None_, _include_confidence =None_, _include_attributes =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes an image detection dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyoneimagedetectiondataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_None_) â 

whether to include detection confidences in the export. The supported values are:

    * `None` (default): include confidences only if they exist

    * `True`: always include confidences

    * `False`: do not include confidences

  * **include_attributes** (_None_) â 

whether to include dynamic attributes of the detections in the export. Supported values are:

    * `None` (default): include attributes only if they exist

    * `True`: always include a (possibly empty) attributes dict

    * `False`: do not include attributes

    * a name or iterable of names of specific attributes to include

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




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

class fiftyone.utils.data.FiftyOneTemporalDetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _use_timestamps =False_, _classes =None_, _include_confidence =None_, _include_attributes =None_, _pretty_print =False_)#
    

Bases: [`LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes a temporal video detection dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyonetemporaldetectiondataset-export) for format details.

Each input video is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the videos in the exported labels

  * **use_timestamps** (_False_) â whether to export the support of each temporal detection in seconds rather than frame numbers

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_None_) â 

whether to include detection confidences in the export. The supported values are:

    * `None` (default): include confidences only if they exist

    * `True`: always include confidences

    * `False`: do not include confidences

  * **include_attributes** (_None_) â 

whether to include dynamic attributes of the detections in the export. Supported values are:

    * `None` (default): include attributes only if they exist

    * `True`: always include a (possibly empty) attributes dict

    * `False`: do not include attributes

    * a name or iterable of names of specific attributes to include

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path,Â temporal_detections,Â _) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple label fields with value-types specified by this dictionary. Not all keys need be present in the exported sample-level labels

  * `None`. In this case, the exporter makes no guarantees about the sample-level labels that it can export




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple frame label fields with value-types specified by this dictionary. Not all keys need be present in the exported frame labels

  * `None`. In this case, the exporter makes no guarantees about the frame labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_video_path_ , _temporal_detections_ , ___ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

  * **frames** â a dictionary mapping frame numbers to dictionaries that map field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no frame-level labels

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

class fiftyone.utils.data.ImageSegmentationDirectoryExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _image_format =None_, _mask_format ='.png'_, _mask_size =None_, _mask_targets =None_, _thickness =1_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes an image segmentation dataset to disk.

See [this page](user_guide__export_datasets.md#imagesegmentationdirectory-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the masks

    * an absolute directory in which to export the masks. In this case, the `export_dir` has no effect on the location of the masks

If None, the masks will be exported into `export_dir` using the default folder name

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` and `labels_path` to generate output paths for each exported image and mask. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **mask_format** (_".png"_) â the image format to use when writing masks to disk

  * **mask_size** (_None_) â the `(width, height)` at which to render segmentation masks when exporting instances or polylines. If not provided, masks will be rendered to match the resolution of each input image

  * **mask_targets** (_None_) â a dict mapping integer pixel values in `[0, 255]` to label strings defining which object classes to render and which pixel values to use for each class. If omitted, all objects are rendered with pixel value 255

  * **thickness** (_1_) â the thickness, in pixels, at which to render (non-filled) polylines




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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.data.FiftyOneImageLabelsDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter")

Exporter that writes a labeled image dataset to disk with labels stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).

See [this page](user_guide__export_datasets.md#fiftyoneimagelabelsdataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(image_or_path,Â labels[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

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

class fiftyone.utils.data.FiftyOneVideoLabelsDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _pretty_print =False_)#
    

Bases: [`LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter")

Exporter that writes a labeled video dataset with labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

See [this page](user_guide__export_datasets.md#fiftyonevideolabelsdataset-export) for format details.

If the path to a video is provided, the video is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(video_path,Â label,Â frames[,Â ...]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple label fields with value-types specified by this dictionary. Not all keys need be present in the exported sample-level labels

  * `None`. In this case, the exporter makes no guarantees about the sample-level labels that it can export




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple frame label fields with value-types specified by this dictionary. Not all keys need be present in the exported frame labels

  * `None`. In this case, the exporter makes no guarantees about the frame labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_video_path_ , _label_ , _frames_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

  * **frames** â a dictionary mapping frame numbers to dictionaries that map field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no frame-level labels

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.data.datetime(_year_ , _month_ , _day_[, _hour_[, _minute_[, _second_[, _microsecond_[, _tzinfo_]]]]])#
    

Bases: `date`

The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be ints.

**Attributes:**

`hour` |   
---|---  
`minute` |   
`second` |   
`microsecond` |   
`tzinfo` |   
`fold` |   
`day` |   
`max` |   
`min` |   
`month` |   
`resolution` |   
`year` |   
  
**Methods:**

`fromtimestamp` | timestamp[, tz] -> tz's local time from POSIX timestamp.  
---|---  
`utcfromtimestamp` | Construct a naive UTC datetime from a POSIX timestamp.  
`now`([tz]) | Returns new datetime object representing current time local to tz.  
`utcnow` | Return a new datetime representing UTC day and time.  
`combine` | date, time -> datetime with same date and time fields  
`fromisoformat` | string -> datetime from a string in most ISO 8601 formats  
`timetuple` | Return time tuple, compatible with time.localtime().  
`timestamp` | Return POSIX timestamp as float.  
`utctimetuple` | Return UTC time tuple, compatible with time.localtime().  
`date` | Return date object with same year, month and day.  
`time` | Return time object with same time but with tzinfo=None.  
`timetz` | Return time object with same time and tzinfo.  
`replace` | Return datetime with new specified fields.  
`astimezone` | tz -> convert to local time in new timezone tz  
`ctime` | Return ctime() style string.  
`isoformat` | [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].  
`strptime` | string, format -> new datetime parsed from a string (like time.strptime()).  
`utcoffset` | Return self.tzinfo.utcoffset(self).  
`tzname` | Return self.tzinfo.tzname(self).  
`dst` | Return self.tzinfo.dst(self).  
`fromisocalendar` | int, int, int -> Construct a date from the ISO year, week number and weekday.  
`fromordinal` | int -> date corresponding to a proleptic Gregorian ordinal.  
`isocalendar` | Return a named tuple containing ISO year, week number, and weekday.  
`isoweekday` | Return the day of the week represented by the date.  
`strftime` | format -> strftime() style string.  
`today` | Current date or datetime: same as self.__class__.fromtimestamp(time.time()).  
`toordinal` | Return proleptic Gregorian ordinal.  
`weekday` | Return the day of the week represented by the date.  
  
hour#
    

minute#
    

second#
    

microsecond#
    

tzinfo#
    

fold#
    

classmethod fromtimestamp()#
    

timestamp[, tz] -> tzâs local time from POSIX timestamp.

classmethod utcfromtimestamp()#
    

Construct a naive UTC datetime from a POSIX timestamp.

classmethod now(_tz =None_)#
    

Returns new datetime object representing current time local to tz.

> tz
>     
> 
> Timezone object.

If no tz is specified, uses local timezone.

classmethod utcnow()#
    

Return a new datetime representing UTC day and time.

classmethod combine()#
    

date, time -> datetime with same date and time fields

classmethod fromisoformat()#
    

string -> datetime from a string in most ISO 8601 formats

timetuple()#
    

Return time tuple, compatible with time.localtime().

timestamp()#
    

Return POSIX timestamp as float.

utctimetuple()#
    

Return UTC time tuple, compatible with time.localtime().

date()#
    

Return date object with same year, month and day.

time()#
    

Return time object with same time but with tzinfo=None.

timetz()#
    

Return time object with same time and tzinfo.

replace()#
    

Return datetime with new specified fields.

astimezone()#
    

tz -> convert to local time in new timezone tz

ctime()#
    

Return ctime() style string.

isoformat()#
    

[sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM]. sep is used to separate the year from the time, and defaults to âTâ. The optional argument timespec specifies the number of additional terms of the time to include. Valid options are âautoâ, âhoursâ, âminutesâ, âsecondsâ, âmillisecondsâ and âmicrosecondsâ.

classmethod strptime()#
    

string, format -> new datetime parsed from a string (like time.strptime()).

utcoffset()#
    

Return self.tzinfo.utcoffset(self).

tzname()#
    

Return self.tzinfo.tzname(self).

dst()#
    

Return self.tzinfo.dst(self).

day#
    

classmethod fromisocalendar()#
    

int, int, int -> Construct a date from the ISO year, week number and weekday.

This is the inverse of the date.isocalendar() function

classmethod fromordinal()#
    

int -> date corresponding to a proleptic Gregorian ordinal.

isocalendar()#
    

Return a named tuple containing ISO year, week number, and weekday.

isoweekday()#
    

Return the day of the week represented by the date. Monday == 1 â¦ Sunday == 7

max = datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)#
    

min = datetime.datetime(1, 1, 1, 0, 0)#
    

month#
    

resolution = datetime.timedelta(microseconds=1)#
    

strftime()#
    

format -> strftime() style string.

classmethod today()#
    

Current date or datetime: same as self.__class__.fromtimestamp(time.time()).

toordinal()#
    

Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.

weekday()#
    

Return the day of the week represented by the date. Monday == 0 â¦ Sunday == 6

year#
    

fiftyone.utils.data.get_document(_name_)#
    

Get a registered Document class by name.

class fiftyone.utils.data.Sample(_filepath_ , _tags =None_, _metadata =None_, _** kwargs_)#
    

Bases: `_SampleMixin`, [`Document`](api__fiftyone.core.document.md#fiftyone.core.document.Document "fiftyone.core.document.Document")

A sample in a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

Samples store all information associated with a particular piece of data in a dataset, including basic metadata about the data, one or more sets of labels (ground truth, user-provided, or FiftyOne-generated), and additional features associated with subsets of the data and/or label sets.

Note

`Sample` instances that are **in datasets** are singletons, i.e., `dataset[sample_id]` will always return the same `Sample` instance.

Parameters:
    

  * **filepath** â the path to the data on disk. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **tags** (_None_) â a list of tags for the sample

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance

  * ****kwargs** â additional fields to dynamically set on the sample




**Methods:**

`reload`([hard,Â include_frames]) | Reloads the sample from the database.  
---|---  
`save`() | Saves the sample to the database.  
`from_frame`(frame[,Â filepath]) | Creates a sample from the given frame.  
`from_doc`(doc[,Â dataset]) | Creates a sample backed by the given document.  
`from_dict`(d) | Loads the sample from a JSON dictionary.  
`add_labels`(labels[,Â label_field,Â ...]) | Adds the given labels to the sample.  
`clear_field`(field_name) | Clears the value of a field of the document.  
`compute_metadata`([overwrite,Â skip_failures]) | Populates the `metadata` field of the sample.  
`copy`([fields,Â omit_fields]) | Returns a deep copy of the sample that has not been added to the database.  
`from_json`(s) | Loads the document from a JSON string.  
`get_field`(field_name) | Gets the value of a field of the document.  
`has_field`(field_name) | Determines whether the document has the given field.  
`iter_fields`([include_id,Â include_timestamps]) | Returns an iterator over the `(name, value)` pairs of the public fields of the document.  
`merge`(sample[,Â fields,Â omit_fields,Â ...]) | Merges the fields of the given sample into this sample.  
`set_field`(field_name,Â value[,Â create,Â ...]) | Sets the value of a field of the document.  
`to_dict`([include_frames,Â include_private]) | Serializes the sample to a JSON dictionary.  
`to_json`([pretty_print]) | Serializes the document to a JSON string.  
`to_mongo_dict`([include_id]) | Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.  
`update_fields`(fields_dict[,Â expand_schema,Â ...]) | Sets the dictionary of fields on the document.  
  
**Attributes:**

`dataset` | The dataset to which this document belongs, or `None` if it has not been added to a dataset.  
---|---  
`dataset_id` |   
`field_names` | An ordered tuple of the public field names of this document.  
`filename` | The basename of the media's filepath.  
`in_dataset` | Whether the document has been added to a dataset.  
`media_type` | The media type of the sample.  
  
reload(_hard =False_, _include_frames =True_)#
    

Reloads the sample from the database.

Parameters:
    

  * **hard** (_False_) â whether to reload the sampleâs schema in addition to its field values. This is necessary if new fields may have been added to the dataset schema

  * **include_frames** (_True_) â whether to reload any in-memory frames of video samples




save()#
    

Saves the sample to the database.

classmethod from_frame(_frame_ , _filepath =None_)#
    

Creates a sample from the given frame.

Parameters:
    

  * **frame** â a [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame")

  * **filepath** (_None_) â the path to the corresponding image frame on disk, if not available



Returns:
    

a `Sample`

classmethod from_doc(_doc_ , _dataset =None_)#
    

Creates a sample backed by the given document.

Parameters:
    

  * **doc** â a [`fiftyone.core.odm.sample.DatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.DatasetSampleDocument "fiftyone.core.odm.sample.DatasetSampleDocument") or [`fiftyone.core.odm.sample.NoDatasetSampleDocument`](api__fiftyone.core.odm.sample.md#fiftyone.core.odm.sample.NoDatasetSampleDocument "fiftyone.core.odm.sample.NoDatasetSampleDocument")

  * **dataset** (_None_) â the [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") that the sample belongs to



Returns:
    

a `Sample`

classmethod from_dict(_d_)#
    

Loads the sample from a JSON dictionary.

The returned sample will not belong to a dataset.

Returns:
    

a `Sample`

add_labels(_labels_ , _label_field =None_, _confidence_thresh =None_, _classes =None_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Adds the given labels to the sample.

The provided `labels` can be any of the following:

  * A [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, in which case the labels are directly saved in the specified `label_field`

  * A dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the labels are added as follows:
        
        for key, value in labels.items():
            sample[label_key(key)] = value
        

  * A dict mapping frame numbers to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {label_field: label}
                for frame_number, label in labels.items()
            }
        )
        

  * A dict mapping frame numbers to dicts mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:
        
        sample.frames.merge(
            {
                frame_number: {
                    label_key(key): value
                    for key, value in frame_dict.items()
                }
                for frame_number, frame_dict in labels.items()
            }
        )
        




In the above, the `label_key` function maps label dict keys to field names, and is defined from `label_field` as follows:
    
    
    if isinstance(label_field, dict):
        label_key = lambda k: label_field.get(k, k)
    elif label_field is not None:
        label_key = lambda k: label_field + "_" + k
    else:
        label_key = lambda k: k
    

Parameters:
    

  * **labels** â a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") or dict of labels per the description above

  * **label_field** (_None_) â the sample field, prefix, or dict defining in which field(s) to save the labels

  * **confidence_thresh** (_None_) â an optional confidence threshold to apply to any applicable labels before saving them

  * **classes** (_None_) â an optional iterable of classes to which to restrict any applicable labels generated by the model

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic attributes




clear_field(_field_name_)#
    

Clears the value of a field of the document.

Parameters:
    

**field_name** â the name of the field to clear

Raises:
    

**AttributeError** â if the field does not exist

compute_metadata(_overwrite =False_, _skip_failures =False_)#
    

Populates the `metadata` field of the sample.

Parameters:
    

  * **overwrite** (_False_) â whether to overwrite existing metadata

  * **skip_failures** (_False_) â whether to gracefully continue without raising an error if metadata cannot be computed




copy(_fields =None_, _omit_fields =None_)#
    

Returns a deep copy of the sample that has not been added to the database.

Parameters:
    

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the copy. This can also be a dict mapping existing field names to new field names

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the copy



Returns:
    

a `Sample`

property dataset#
    

The dataset to which this document belongs, or `None` if it has not been added to a dataset.

property dataset_id#
    

property field_names#
    

An ordered tuple of the public field names of this document.

property filename#
    

The basename of the mediaâs filepath.

classmethod from_json(_s_)#
    

Loads the document from a JSON string.

The returned document will not belong to a dataset.

Parameters:
    

**s** â the JSON string

Returns:
    

a `Document`

get_field(_field_name_)#
    

Gets the value of a field of the document.

Parameters:
    

**field_name** â the field name

Returns:
    

the field value

Raises:
    

**AttributeError** â if the field does not exist

has_field(_field_name_)#
    

Determines whether the document has the given field.

Parameters:
    

**field_name** â the field name

Returns:
    

True/False

property in_dataset#
    

Whether the document has been added to a dataset.

iter_fields(_include_id =False_, _include_timestamps =False_)#
    

Returns an iterator over the `(name, value)` pairs of the public fields of the document.

Parameters:
    

  * **include_id** (_False_) â whether to include the `id` field

  * **include_timestamps** (_False_) â whether to include the `created_at` and `last_modified_at` fields



Returns:
    

an iterator that emits `(name, value)` tuples

property media_type#
    

The media type of the sample.

merge(_sample_ , _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Merges the fields of the given sample into this sample.

The behavior of this method is highly customizable. By default, all top-level fields from the provided sample are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both samples are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether new fields can be added to the dataset schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input sample fields to different field names of this sample




Parameters:
    

  * **sample** â a `fiftyone.core.sample.Sample`

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. May contain frame fields for video samples. This can also be a dict mapping field names of the input sample to field names of this sample

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge. May contain frame fields for video samples

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided sample

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if any fields are not in the dataset schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields




set_field(_field_name_ , _value_ , _create =True_, _validate =True_, _dynamic =False_)#
    

Sets the value of a field of the document.

Parameters:
    

  * **field_name** â the field name

  * **value** â the field value

  * **create** (_True_) â whether to create the field if it does not exist

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

  * **ValueError** â if `field_name` is not an allowed field name

  * **AttributeError** â if the field does not exist and `create == False`




to_dict(_include_frames =False_, _include_private =False_)#
    

Serializes the sample to a JSON dictionary.

Parameters:
    

  * **include_frames** (_False_) â whether to include the frame labels for video samples

  * **include_private** (_False_) â whether to include private fields



Returns:
    

a JSON dict

to_json(_pretty_print =False_)#
    

Serializes the document to a JSON string.

The document ID and private fields are excluded in this representation.

Parameters:
    

**pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations

Returns:
    

a JSON string

to_mongo_dict(_include_id =False_)#
    

Serializes the document to a BSON dictionary equivalent to the representation that would be stored in the database.

Parameters:
    

**include_id** (_False_) â whether to include the document ID

Returns:
    

a BSON dict

update_fields(_fields_dict_ , _expand_schema =True_, _validate =True_, _dynamic =False_)#
    

Sets the dictionary of fields on the document.

Parameters:
    

  * **fields_dict** â a dict mapping field names to values

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the document schema. If False, an error is raised if any fields are not in the document schema

  * **validate** (_True_) â whether to validate values for existing fields

  * **dynamic** (_False_) â whether to declare dynamic embedded document fields



Raises:
    

**AttributeError** â if `expand_schema == False` and a field does not exist

class fiftyone.utils.data.FiftyOneImageClassificationSampleParser(_classes =None_)#
    

Bases: [`ImageClassificationSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageClassificationSampleParser "fiftyone.utils.data.parsers.ImageClassificationSampleParser")

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

class fiftyone.utils.data.FiftyOneTemporalDetectionSampleParser(_classes =None_, _compute_metadata =False_)#
    

Bases: [`LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser "fiftyone.utils.data.parsers.LabeledVideoSampleParser")

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

class fiftyone.utils.data.FiftyOneImageDetectionSampleParser(_classes =None_)#
    

Bases: [`ImageDetectionSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageDetectionSampleParser "fiftyone.utils.data.parsers.ImageDetectionSampleParser")

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

class fiftyone.utils.data.FiftyOneImageLabelsSampleParser(_prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: [`ImageLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.ImageLabelsSampleParser "fiftyone.utils.data.parsers.ImageLabelsSampleParser")

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

class fiftyone.utils.data.FiftyOneVideoLabelsSampleParser(_prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: [`VideoLabelsSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.VideoLabelsSampleParser "fiftyone.utils.data.parsers.VideoLabelsSampleParser")

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

fiftyone.utils.data.import_samples(_dataset_ , _dataset_importer_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _add_info =True_, _generator =False_, _progress =None_)#
    

Adds the samples from the given `DatasetImporter` to the dataset.

See [this guide](user_guide__import_datasets.md#custom-dataset-importer) for more details about importing datasets in custom formats by defining your own `DatasetImporter`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **dataset_importer** â a `DatasetImporter`

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. Only applicable if `dataset_importer` is a `LabeledImageDatasetImporter` or `LabeledVideoDatasetImporter`. If the importer produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample/frame, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the importer produces a dictionary of labels per sample, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **expand_schema** (_True_) â whether to dynamically add new sample fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **add_info** (_True_) â whether to add dataset info from the importer (if any) to the dataset

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

fiftyone.utils.data.merge_samples(_dataset_ , _dataset_importer_ , _label_field =None_, _tags =None_, _key_field ='filepath'_, _key_fcn =None_, _skip_existing =False_, _insert_new =True_, _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _dynamic =False_, _add_info =True_, _progress =None_)#
    

Merges the samples from the given `DatasetImporter` into the dataset.

See [this guide](user_guide__import_datasets.md#custom-dataset-importer) for more details about importing datasets in custom formats by defining your own `DatasetImporter`.

By default, samples with the same absolute `filepath` are merged, but you can customize this behavior via the `key_field` and `key_fcn` parameters. For example, you could set `key_fcn = lambda sample: os.path.basename(sample.filepath)` to merge samples with the same base filename.

The behavior of this method is highly customizable. By default, all top-level fields from the imported samples are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both collections are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether existing samples should be modified or skipped

  * Whether new samples should be added or omitted

  * Whether new fields can be added to the dataset schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input fields to different field names of this dataset




Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **dataset_importer** â a `DatasetImporter`

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. Only applicable if `dataset_importer` is a `LabeledImageDatasetImporter` or `LabeledVideoDatasetImporter`. If the importer produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample/frame, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the importer produces a dictionary of labels per sample, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **key_field** (_"filepath"_) â the sample field to use to decide whether to join with an existing sample

  * **key_fcn** (_None_) â a function that accepts a `fiftyone.core.sample.Sample` instance and computes a key to decide if two samples should be merged. If a `key_fcn` is provided, `key_field` is ignored

  * **skip_existing** (_False_) â whether to skip existing samples (True) or merge them (False)

  * **insert_new** (_True_) â whether to insert new samples (True) or skip them (False)

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. If provided, fields other than these are omitted from `samples` when merging or adding samples. One exception is that `filepath` is always included when adding new samples, since the field is required. This can also be a dict mapping field names of the input collection to field names of this dataset

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge. If provided, these fields are omitted from imported samples, if present. One exception is that `filepath` is always included when adding new samples, since the field is required

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided samples

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **add_info** (_True_) â whether to add dataset info from the importer (if any) to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.data.parse_dataset_info(_dataset_ , _info_ , _overwrite =True_)#
    

Parses the info returned by `DatasetImporter.get_dataset_info()` and stores it on the relevant properties of the dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **info** â an info dict

  * **overwrite** (_True_) â whether to overwrite existing dataset info fields




class fiftyone.utils.data.ImportPathsMixin#
    

Bases: `object`

Mixin for `DatasetImporter` classes that provides convenience methods for parsing the `data_path` and `labels_path` parameters supported by many importers.

class fiftyone.utils.data.DatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `object`

Base interface for importing datasets stored on disk into FiftyOne.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

subclass-specific information for the sample

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.BatchDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Base interface for importers that load all of their samples in a single call to `import_samples()`.

This interface allows for greater efficiency for import formats that handle aggregating over the samples themselves.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Methods:**

`import_samples`(dataset[,Â tags,Â progress]) | Imports the samples into the given dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
import_samples(_dataset_ , _tags =None_, _progress =None_)#
    

Imports the samples into the given dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **tags** (_None_) â an optional list of tags to attach to each sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.GenericSampleDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets that contain arbitrary `fiftyone.core.sample.Sample` instances.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

a `fiftyone.core.sample.Sample` instance

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_sample_field_schema` | Whether this importer produces a sample field schema.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.GroupDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`GenericSampleDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter "fiftyone.utils.data.importers.GenericSampleDatasetImporter")

Interface for importing datasets that contain arbitrary grouped `fiftyone.core.sample.Sample` instances.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported across all group slices.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next group in the dataset.

Returns:
    

a dict mapping slice names to `fiftyone.core.sample.Sample` instances

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`group_field` | The name of the group field to populate on each sample.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`has_sample_field_schema` | Whether this importer produces a sample field schema.  
  
**Methods:**

`get_group_media_types`() | Returns a dictionary describing the group slices of the samples loaded by this importer.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property group_field#
    

The name of the group field to populate on each sample.

get_group_media_types()#
    

Returns a dictionary describing the group slices of the samples loaded by this importer.

Returns:
    

a dict mapping slice names to media types

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

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.UnlabeledImageDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets of unlabeled image samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(image_path, image_metadata)` tuple, where

  * `image_path`: the path to the image on disk

  * `image_metadata`: an [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for the image, or `None` if `has_image_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.UnlabeledVideoDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets of unlabeled video samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(video_path, video_metadata)` tuple, where

  * `video_path`: the path to the video on disk

  * `video_metadata`: an [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for the video, or `None` if `has_video_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.UnlabeledMediaDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets of unlabeled media samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(filepath, metadata)` tuple, where

  * `filepath`: the path to the media on disk

  * `metadata`: a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the media, or `None` if `has_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_metadata` | Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.LabeledImageDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets of labeled image samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(image_path, image_metadata, label)` tuple, where

  * `image_path`: the path to the image on disk

  * `image_metadata`: an [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for the image, or `None` if `has_image_metadata()` is `False`

  * `label`: an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.LabeledVideoDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter")

Interface for importing datasets of labeled video samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(video_path, video_metadata, labels, frames)` tuple, where

  * `video_path`: the path to the video on disk

  * `video_metadata`: an [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for the video, or `None` if `has_video_metadata()` is `False`

  * `labels`: sample-level labels for the video, which can be any of the following:

    * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance

    * a dictionary mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

    * `None` if the sample has no sample-level labels

  * `frames`: frame-level labels for the video, which can be any of the following:

    * a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame

    * `None` if the sample has no frame-level labels




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
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

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.LegacyFiftyOneDatasetImporter(_dataset_dir_ , _rel_dir =None_, _import_saved_views =True_, _import_runs =True_, _import_workspaces =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`GenericSampleDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.GenericSampleDatasetImporter "fiftyone.utils.data.importers.GenericSampleDatasetImporter")

Legacy importer for FiftyOne datasets stored on disk in a serialized JSON format.

Warning

The [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format was upgraded in `fiftyone==0.8` and this importer is now deprecated.

However, to maintain backwards compatibility, `FiftyOneDatasetImporter` will check for instances of datasets of this type at runtime and defer to this class to load them.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **rel_dir** (_None_) â a relative directory to prepend to each filepath if it is not absolute. This path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **import_saved_views** (_True_) â whether to include saved views in the import. Only applicable when importing full datasets

  * **import_runs** (_True_) â whether to include annotation/brain/evaluation runs in the import. Only applicable when importing full datasets

  * **import_workspaces** (_True_) â whether to include saved workspaces in the import. Only applicable when importing full datasets

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
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`import_extras`(sample_collection) |   
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

import_extras(_sample_collection_)#
    

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

class fiftyone.utils.data.FiftyOneDatasetImporter(_dataset_dir_ , _rel_dir =None_, _import_saved_views =True_, _import_runs =True_, _import_workspaces =True_, _ordered =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`BatchDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter "fiftyone.utils.data.importers.BatchDatasetImporter")

Importer for FiftyOne datasets stored on disk in serialized JSON format.

See [this page](user_guide__import_datasets.md#fiftyonedataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **rel_dir** (_None_) â a relative directory to prepend to the `filepath` of each sample if the filepath is not absolute. This path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **import_saved_views** (_True_) â whether to include saved views in the import. Only applicable when importing full datasets

  * **import_runs** (_True_) â whether to include annotation/brain/evaluation runs in the import. Only applicable when importing full datasets

  * **import_workspaces** (_True_) â whether to include saved workspaces in the import. Only applicable when importing full datasets

  * **ordered** (_True_) â whether to preserve document order when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`import_samples`(dataset[,Â tags,Â progress]) | Imports the samples into the given dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

import_samples(_dataset_ , _tags =None_, _progress =None_)#
    

Imports the samples into the given dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **tags** (_None_) â an optional list of tags to attach to each sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

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

class fiftyone.utils.data.ImageDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter")

Importer for a directory of images stored on disk.

See [this page](user_guide__import_datasets.md#imagedirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

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

class fiftyone.utils.data.VideoDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter")

Importer for a directory of videos stored on disk.

See [this page](user_guide__import_datasets.md#videodirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

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

class fiftyone.utils.data.MediaDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`UnlabeledMediaDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter "fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter")

Importer for a directory of media files stored on disk.

See [this page](user_guide__import_datasets.md#mediadirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each media file when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_metadata` | Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.

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

class fiftyone.utils.data.FiftyOneImageClassificationDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for image classification datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimageclassificationdataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with labels (False)

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

class fiftyone.utils.data.ImageClassificationDirectoryTreeImporter(_dataset_dir_ , _compute_metadata =False_, _classes =None_, _unlabeled ='_unlabeled'_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter")

Importer for an image classification directory tree stored on disk.

See [this page](user_guide__import_datasets.md#imageclassificationdirectorytree-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **classes** (_None_) â an optional string or list of strings specifying a subset of classes to load

  * **unlabeled** (_"_unlabeled"_) â the name of the subdirectory containing unlabeled images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.VideoClassificationDirectoryTreeImporter(_dataset_dir_ , _compute_metadata =False_, _classes =None_, _unlabeled ='_unlabeled'_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter")

Importer for a viideo classification directory tree stored on disk.

See [this page](user_guide__import_datasets.md#videoclassificationdirectorytree-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **classes** (_None_) â an optional string or list of strings specifying a subset of classes to load

  * **unlabeled** (_"_unlabeled"_) â the name of the subdirectory containing unlabeled images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.FiftyOneImageDetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for image detection datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimagedetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with labels (False)

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

class fiftyone.utils.data.FiftyOneTemporalDetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for temporal video detection datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyonetemporaldetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **include_all_data** (_False_) â whether to generate samples for all videos in the data directory (True) rather than only creating samples for videos with labels (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

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

class fiftyone.utils.data.ImageSegmentationDirectoryImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _load_masks =False_, _force_grayscale =False_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for image segmentation datasets stored on disk.

See [this page](user_guide__import_datasets.md#imagesegmentationdirectory-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping filenames to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels/`

  * **load_masks** (_False_) â whether to load the masks into the database (True) or simply record the paths to the masks (False)

  * **force_grayscale** (_False_) â whether to load RGB masks as grayscale by storing only the first channel

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with masks (False)

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

class fiftyone.utils.data.FiftyOneImageLabelsDatasetImporter(_dataset_dir_ , _compute_metadata =False_, _prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter")

Importer for labeled image datasets whose labels are stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyoneimagelabelsdataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded label dictionary

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the image labels to field names into which to expand them

  * **multilabel** (_False_) â whether to store frame attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical frame attributes (True) or cast them to strings (False)

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

class fiftyone.utils.data.FiftyOneVideoLabelsDatasetImporter(_dataset_dir_ , _compute_metadata =False_, _prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter")

Importer for labeled video datasets whose labels are stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyonevideolabelsdataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded sample/frame label dictionaries

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the sample labels to field names into which to expand them. By default, all sample labels are loaded

  * **frame_labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the frame labels to field names into which to expand them. By default, all frame labels are loaded

  * **multilabel** (_False_) â whether to store frame attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical frame attributes (True) or cast them to strings (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

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

class fiftyone.utils.data.ImageIngestor(_dataset_dir_ , _image_format =None_)#
    

Bases: `object`

Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest images into the provided `dataset_dir` during import.

Parameters:
    

  * **dataset_dir** â the directory where input images will be ingested into

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




class fiftyone.utils.data.UnlabeledImageDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _image_format =None_, _max_samples =None_)#
    

Bases: [`UnlabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledImageDatasetImporter "fiftyone.utils.data.importers.UnlabeledImageDatasetImporter"), [`ImageIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.ImageIngestor "fiftyone.utils.data.ingestors.ImageIngestor")

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

class fiftyone.utils.data.LabeledImageDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _image_format =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImageIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.ImageIngestor "fiftyone.utils.data.ingestors.ImageIngestor")

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

class fiftyone.utils.data.VideoIngestor(_dataset_dir_)#
    

Bases: `object`

Mixin for [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") instances that ingest videos into the provided `dataset_dir` during import.

Parameters:
    

**dataset_dir** â the directory where input videos will be ingested into

class fiftyone.utils.data.UnlabeledVideoDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _max_samples =None_)#
    

Bases: [`UnlabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter "fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter"), [`VideoIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.VideoIngestor "fiftyone.utils.data.ingestors.VideoIngestor")

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

class fiftyone.utils.data.LabeledVideoDatasetIngestor(_dataset_dir_ , _samples_ , _sample_parser_ , _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter"), [`VideoIngestor`](api__fiftyone.utils.data.ingestors.md#fiftyone.utils.data.ingestors.VideoIngestor "fiftyone.utils.data.ingestors.VideoIngestor")

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

fiftyone.utils.data.add_images(_dataset_ , _samples_ , _sample_parser_ , _tags =None_, _generator =False_, _progress =None_)#
    

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

fiftyone.utils.data.add_labeled_images(_dataset_ , _samples_ , _sample_parser_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _generator =False_, _progress =None_)#
    

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

fiftyone.utils.data.add_videos(_dataset_ , _samples_ , _sample_parser_ , _tags =None_, _generator =False_, _progress =None_)#
    

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

fiftyone.utils.data.add_labeled_videos(_dataset_ , _samples_ , _sample_parser_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _generator =False_, _progress =None_)#
    

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

class fiftyone.utils.data.SampleParser#
    

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

class fiftyone.utils.data.UnlabeledImageSampleParser#
    

Bases: [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser")

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

class fiftyone.utils.data.UnlabeledVideoSampleParser#
    

Bases: [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser")

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

class fiftyone.utils.data.UnlabeledMediaSampleParser#
    

Bases: [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser")

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

class fiftyone.utils.data.VideoSampleParser#
    

Bases: [`UnlabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledVideoSampleParser "fiftyone.utils.data.parsers.UnlabeledVideoSampleParser")

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

class fiftyone.utils.data.MediaSampleParser#
    

Bases: [`UnlabeledMediaSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.UnlabeledMediaSampleParser "fiftyone.utils.data.parsers.UnlabeledMediaSampleParser")

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

class fiftyone.utils.data.LabeledImageSampleParser#
    

Bases: [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser")

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

class fiftyone.utils.data.LabeledVideoSampleParser#
    

Bases: [`SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser")

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

class fiftyone.utils.data.LabeledImageTupleSampleParser#
    

Bases: [`LabeledImageSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageSampleParser "fiftyone.utils.data.parsers.LabeledImageSampleParser")

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

class fiftyone.utils.data.ImageDetectionSampleParser(_label_field ='label'_, _bounding_box_field ='bounding_box'_, _confidence_field =None_, _attributes_field =None_, _classes =None_, _normalized =True_)#
    

Bases: [`LabeledImageTupleSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser "fiftyone.utils.data.parsers.LabeledImageTupleSampleParser")

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

class fiftyone.utils.data.ImageLabelsSampleParser(_prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: [`LabeledImageTupleSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledImageTupleSampleParser "fiftyone.utils.data.parsers.LabeledImageTupleSampleParser")

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

class fiftyone.utils.data.VideoLabelsSampleParser(_prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_)#
    

Bases: [`LabeledVideoSampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.LabeledVideoSampleParser "fiftyone.utils.data.parsers.LabeledVideoSampleParser")

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

class fiftyone.utils.data.ExtractClipsMixin(_compute_metadata =False_, _write_clips =True_, _clip_dir =None_, _video_format =None_)#
    

Bases: `object`

Mixin for sample parsers that extract clips from [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances.

Parameters:
    

  * **compute_metadata** (_False_) â whether to compute [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances on-the-fly when no pre-computed metadata is available

  * **write_clips** (_True_) â whether to write clips when their paths are requested

  * **clip_dir** (_None_) â a directory to write clips. Only applicable when parsing [`fiftyone.core.clips.ClipView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipView "fiftyone.core.clips.ClipView") instances

  * **video_format** (_None_) â the video format to use when writing video clips to disk. By default, `fiftyone.config.default_video_ext` is used




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
