---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/reid_people_tracking.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/reid-people-tracking)

# Reid People Tracking#

Person re-identification dataset for tracking individuals across camera views.

![Screenshot from 2026-01-27 19-00-41](https://cdn-uploads.huggingface.co/production/uploads/629628d87d586f66c390fabe/78k7rk5M9BEwfD_22sT0h.png)

## Details#

Property | Value  
---|---  
Samples | 101  
Media | image  
Fields | global_id, confidence, camera_id, timestamp, embeddings  
  
## Usage#
    
    
    from fiftyone.utils.huggingface import load_from_hub
    dataset = load_from_hub("Voxel51/reid-people-tracking")
    

* * *

_Uploaded with[FiftyOne Skills](https://github.com/voxel51/fiftyone-skills)_

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
