---
source_url: https://docs.voxel51.com/api/fiftyone.utils.lfw.html
---

# fiftyone.utils.lfw#

Utilities for working with the [Labeled Faces in the Wild dataset](http://vis-www.cs.umass.edu/lfw).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_lfw_dataset`(dataset_dir[,Â ...]) | Downloads and extracts the Labeled Faces in the Wild dataset.  
---|---  
  
fiftyone.utils.lfw.download_lfw_dataset(_dataset_dir_ , _scratch_dir =None_, _cleanup =True_)#
    

Downloads and extracts the Labeled Faces in the Wild dataset.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to output the final dataset

  * **scratch_dir** (_None_) â a scratch directory to use to store temporary files

  * **cleanup** (_True_) â whether to cleanup the scratch directory after extraction




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
