---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.utils.html
---

# fiftyone.core.session.utils#

FiftyOne session utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`normalize_selected_samples`(samples) | Normalizes a list of selected samples to the canonical format.  
---|---  
  
fiftyone.core.session.utils.normalize_selected_samples(_samples : List_) → List[Dict]#
    

Normalizes a list of selected samples to the canonical format.

Despite its name, `selected_samples` represents whatever sample grid items are in the current view: samples, patches, clips, or frames.

Accepts both `list[str]` (all `"default"`) and `list[dict]` (`{"id": ..., "type": ...}`).

Parameters:
    

**samples** â a list of IDs (strings) or dicts with `id` and `type` keys

Returns:
    

a list of dicts with `id` and `type` keys

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
