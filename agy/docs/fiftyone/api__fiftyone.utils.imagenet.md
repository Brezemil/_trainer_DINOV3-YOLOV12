---
source_url: https://docs.voxel51.com/api/fiftyone.utils.imagenet.html
---

# fiftyone.utils.imagenet#

Utilities for working with the [ImageNet dataset](http://www.image-net.org).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`ensure_imagenet_manual_download`(source_dir,Â ...) | Ensures that the ImageNet archive(s) for the requested split have been manually downloaded to the required locations.  
---|---  
  
fiftyone.utils.imagenet.ensure_imagenet_manual_download(_source_dir_ , _split_ , _devkit =False_)#
    

Ensures that the ImageNet archive(s) for the requested split have been manually downloaded to the required locations.

Parameters:
    

  * **source_dir** â the dataset directory

  * **split** â the split of interest. Supported values are `("train", "validation")`

  * **devkit** (_False_) â whether to ensure that the devkit archive is present



Raises:
    

**OSError** â if the required files are not present

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
