---
source_url: https://docs.voxel51.com/api/fiftyone.utils.hmdb51.html
---

# fiftyone.utils.hmdb51#

Utilities for working with the [HMDB51 dataset](https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_hmdb51_dataset`(dataset_dir[,Â ...]) | Downloads and extracts the HMDB51 dataset.  
---|---  
  
fiftyone.utils.hmdb51.download_hmdb51_dataset(_dataset_dir_ , _scratch_dir =None_, _fold =1_, _cleanup =True_)#
    

Downloads and extracts the HMDB51 dataset.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to output the final dataset

  * **scratch_dir** (_None_) â a scratch directory to use to store temporary files

  * **fold** (_1_) â the test/train fold to use to arrange the files on disk. The supported values are `(1, 2, 3)`

  * **cleanup** (_True_) â whether to cleanup the scratch directory after extraction




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
