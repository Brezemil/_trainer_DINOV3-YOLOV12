---
source_url: https://docs.voxel51.com/api/fiftyone.utils.groups.html
---

# fiftyone.utils.groups#

Grouped dataset utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`group_collections`(coll_dict,Â group_key[,Â ...]) | Merges the given collections into a grouped dataset using the specified field as a group key.  
---|---  
  
fiftyone.utils.groups.group_collections(_coll_dict_ , _group_key_ , _group_field ='group'_)#
    

Merges the given collections into a grouped dataset using the specified field as a group key.

The returned dataset will contain all samples from the input collections with non-None values for the specified `group_key`, with all samples with a given `group_key` value in the same group.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.utils.groups as foug
    
    dataset1 = fo.Dataset()
    dataset1.add_samples(
        [
            fo.Sample(filepath="image-left1.jpg", group_id=1),
            fo.Sample(filepath="image-left2.jpg", group_id=2),
            fo.Sample(filepath="image-left3.jpg", group_id=3),
            fo.Sample(filepath="skip-me1.jpg"),
        ]
    )
    
    dataset2 = fo.Dataset()
    dataset2.add_samples(
        [
            fo.Sample(filepath="image-right1.jpg", group_id=1),
            fo.Sample(filepath="image-right2.jpg", group_id=2),
            fo.Sample(filepath="image-right4.jpg", group_id=4),
            fo.Sample(filepath="skip-me2.jpg"),
        ]
    )
    
    dataset = foug.group_collections(
        {"left": dataset1, "right": dataset2}, "group_id"
    )
    

Parameters:
    

  * **coll_dict** â a dict mapping slice names to [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances

  * **group_key** â the field to use as a group membership key. The field may contain values of any hashable type (int, string, etc)

  * **group_field** (_"group"_) â a name to use for the group field of the returned dataset



Returns:
    

a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
