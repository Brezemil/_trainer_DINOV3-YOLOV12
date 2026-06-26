---
source_url: https://docs.voxel51.com/api/fiftyone.utils.ucf101.html
---

# fiftyone.utils.ucf101#

Utilities for working with the [UCF101 dataset](https://www.crcv.ucf.edu/research/data-sets/ucf101).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_ucf101_dataset`(dataset_dir[,Â ...]) | Downloads and extracts the UCF101 dataset.  
---|---  
  
fiftyone.utils.ucf101.download_ucf101_dataset(_dataset_dir_ , _scratch_dir =None_, _fold =1_, _cleanup =True_)#
    

Downloads and extracts the UCF101 dataset.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to output the final dataset

  * **scratch_dir** (_None_) â a scratch directory to use to store temporary files

  * **fold** (_1_) â the test/train fold to use to arrange the files on disk. The supported values are `(1, 2, 3)`

  * **cleanup** (_True_) â whether to cleanup the scratch directory after extraction




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
