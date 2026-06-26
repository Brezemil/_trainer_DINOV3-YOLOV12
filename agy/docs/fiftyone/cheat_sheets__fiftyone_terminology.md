---
source_url: https://docs.voxel51.com/cheat_sheets/fiftyone_terminology.html
---

# FiftyOne terminology#

This cheat sheet introduces the key terminology in the world of FiftyOne.

## The basics#

| FiftyOne | The open-source framework, the core library, and the Python SDK.  
---|---  
FiftyOne App | The [provided user interface](user_guide__app.md#fiftyone-app) for graphically viewing, filtering, and understanding your datasets. Can be launched in the browser or within notebooks.  
FiftyOne Enterprise | [The enterprise-grade suite](https://voxel51.com/enterprise/) built on top of FiftyOne for collaboration, permissioning, and working with cloud-backed media.  
  
## Other components#

Brain | Library of [ML-powered capabilities](brain.md#fiftyone-brain) for computation and visualization.  
---|---  
Dataset Zoo | [Collection of common datasets](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo) available for download and loading into FiftyOne.  
Model Zoo | [Collection of pre-trained models](https://docs.voxel51.com/model_zoo/index.html#model-zoo) available for download and inference.  
Plugin | A module you can use to [customize and extend](plugins__overview.md#fiftyone-plugins) the behavior of FiftyOne.  
Operator | A [plugin subcomponent](plugins__using_plugins.md#using-operators) that defines an operation that can be executed either directly by users in the App and/or internally invoked by other plugin components  
Integration | A dataset, ML framework, annotation service, or other tool FiftyOne is [directly compatible with](https://docs.voxel51.com/integrations/index.html#integrations).  
  
## Data model#

Dataset | [Core data structure](user_guide__basics.md#basics-datasets) in FiftyOne, composed of `Sample` instances. Provides a consistent interface for loading images, videos, metadata, annotations, and predictions. The computer vision analog of a table of data.  
---|---  
Sample | The atomic elements of a `Dataset` that store all the information related to a given piece of data. Every [sample](user_guide__basics.md#basics-samples) has an associated media file. The computer vision analog of a row of tabular data.  
DatasetView | [A view into](https://docs.voxel51.com/user_guide/using_views.html#using-views) a `Dataset`, which can filter, sort, transform, etc. the dataset along various axes to obtain a desired subset of the samples.  
ViewStage | [A logical operation](https://docs.voxel51.com/user_guide/using_views.html#view-stages), such as filtering, matching, or sorting, which can be used to generate a `DatasetView`.  
Field | Attributes of `Sample` instances that [store customizable information](user_guide__basics.md#basics-fields) about the samples. The computer vision analog of a column in a table.  
Embedded Document Field | [A collection of related fields](https://docs.voxel51.com/user_guide/using_datasets.html#custom-embedded-documents) organized under a single top-level `Field`, similar to a nested dictionary.  
Label | Class hierarchy used to [store semantic information](user_guide__basics.md#basics-labels) about ground truth or predicted labels in a sample. Builtin `Label` types include `Classification`, `Detections`, `Keypoints`, and many others.  
Tag | A field containing a list of strings representing relevant information. [Tags](user_guide__basics.md#basics-tags) can be assigned to datasets, samples, or labels.  
Metadata | A special `Sample` field that can be automatically populated with media type-specific [metadata](user_guide__basics.md#basics-metadata) about the raw media associated with the sample.  
Aggregation | A class encapsulating the computation of an [aggregate statistic](user_guide__basics.md#basics-aggregations) about the contents of a dataset or view.  
  
## FiftyOne App#

Session | [An instance of the FiftyOne App](user_guide__app.md#app-sessions) connected to a specific dataset, via which you can use to programmatically interact with the App.  
---|---  
Sample grid | The rectangular [media grid](user_guide__app.md#app-filtering) that you can scroll through to quickly browse the samples in a dataset. Click on any media in the grid to open the sample modal.  
Sample modal | The [expanded modal](user_guide__app.md#app-sample-view) that provides detailed information and visualization about an individual sample in a dataset.  
Sidebar | Vertical component on [left side of App](user_guide__app.md#app-fields-sidebar) that provides convenient options for filtering the dataset and toggling the visibility of fields in the sample grid.  
View bar | [Horizontal bar at the top of the App](user_guide__app.md#app-create-view) where you can create and compose view stages via point and click operations to filter your dataset and show only the content of interest.  
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
