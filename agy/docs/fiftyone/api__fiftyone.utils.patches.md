---
source_url: https://docs.voxel51.com/api/fiftyone.utils.patches.html
---

# fiftyone.utils.patches#

Image patch utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ImagePatchesExtractor`(samples[,Â ...]) | Class for iterating over the labeled/unlabeled image patches in a collection.  
---|---  
  
**Functions:**

`parse_patches`(doc,Â patches_field[,Â ...]) | Parses the patches from the given document.  
---|---  
`extract_patch`(img,Â detection[,Â ...]) | Extracts the patch from the image.  
  
class fiftyone.utils.patches.ImagePatchesExtractor(_samples_ , _patches_field =None_, _include_labels =False_, _force_rgb =False_, _force_square =False_, _alpha =None_)#
    

Bases: `object`

Class for iterating over the labeled/unlabeled image patches in a collection.

By default, this class emits only the image patches, but you can set `include_labels` to True to emit `(img_patch, label)` tuples.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **patches_field** (_None_) â the name of the field defining the image patches in each sample to extract. Must be of type [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"). This can be automatically inferred (only) if `samples` is a patches view

  * **include_labels** (_False_) â whether to emit `(img_patch, label)` tuples rather than just image patches

  * **force_rgb** (_False_) â whether to force convert the images to RGB

  * **force_square** (_False_) â whether to minimally manipulate the patch bounding boxes into squares prior to extraction

  * **alpha** (_None_) â an optional expansion/contraction to apply to the patches before extracting them, in `[-1, inf)`. If provided, the length and width of the box are expanded (or contracted, when `alpha < 0`) by `(100 * alpha)%`. For example, set `alpha = 0.1` to expand the boxes by 10%, and set `alpha = -0.1` to contract the boxes by 10%




fiftyone.utils.patches.parse_patches(_doc_ , _patches_field_ , _handle_missing ='skip'_)#
    

Parses the patches from the given document.

Parameters:
    

  * **patches_field** â the name of the field defining the image patches. Must be of type [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * **handle_missing** (_"skip"_) â 

how to handle documents with no patches. Supported values are:

>     * âskipâ: skip the document and return `None`
> 
>     * âimageâ: use the whole image as a single patch
> 
>     * âerrorâ: raise an error



Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") instance, or `None`

fiftyone.utils.patches.extract_patch(_img_ , _detection_ , _force_square =False_, _alpha =None_)#
    

Extracts the patch from the image.

Parameters:
    

  * **img** â a numpy image array

  * **detection** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") defining the patch

  * **force_square** (_False_) â whether to minimally manipulate the patch bounding box into a square prior to extraction

  * **alpha** (_None_) â an optional expansion/contraction to apply to the patch before extracting it, in `[-1, inf)`. If provided, the length and width of the box are expanded (or contracted, when `alpha < 0`) by `(100 * alpha)%`. For example, set `alpha = 0.1` to expand the box by 10%, and set `alpha = -0.1` to contract the box by 10%



Returns:
    

the image patch

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
