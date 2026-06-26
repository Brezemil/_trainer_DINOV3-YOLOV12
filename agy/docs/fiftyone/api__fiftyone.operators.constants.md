---
source_url: https://docs.voxel51.com/api/fiftyone.operators.constants.html
---

# fiftyone.operators.constants#

FiftyOne operator constants.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ViewTarget`() | Choices for target view that an operator should operate on  
---|---  
  
class fiftyone.operators.constants.ViewTarget#
    

Bases: `object`

Choices for target view that an operator should operate on

See [`fiftyone.operators.types.ViewTargetProperty()`](api__fiftyone.operators.types.md#fiftyone.operators.types.ViewTargetProperty "fiftyone.operators.types.ViewTargetProperty") for details.

**Attributes:**

`BASE_VIEW` | Base view from which a generated view was created  
---|---  
`CURRENT_VIEW` | Current view in the app  
`DATASET` | Entire dataset  
`DATASET_VIEW` | Empty dataset view, i.e., `ctx.dataset.view()`.  
`SELECTED_LABELS` | Selected labels in the app view, if any.  
`SELECTED_SAMPLES` | Selected samples in the app view, if any.  
`CUSTOM_VIEW_TARGET` | Custom view target specified by the caller.  
  
BASE_VIEW = 'BASE_VIEW'#
    

Base view from which a generated view was created

If the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), base view is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

CURRENT_VIEW = 'CURRENT_VIEW'#
    

Current view in the app

DATASET = 'DATASET'#
    

Entire dataset

DATASET_VIEW = 'DATASET_VIEW'#
    

Empty dataset view, i.e., `ctx.dataset.view()`.

Note: unlikely to be useful in the typical case.

SELECTED_LABELS = 'SELECTED_LABELS'#
    

Selected labels in the app view, if any.

SELECTED_SAMPLES = 'SELECTED_SAMPLES'#
    

Selected samples in the app view, if any.

CUSTOM_VIEW_TARGET = 'CUSTOM_VIEW_TARGET'#
    

Custom view target specified by the caller.

When using this option, specify âcustom_view_targetâ in the operator parameters with a list of JSON-serialized view stages to apply.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
