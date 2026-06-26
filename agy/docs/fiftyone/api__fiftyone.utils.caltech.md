---
source_url: https://docs.voxel51.com/api/fiftyone.utils.caltech.html
---

# fiftyone.utils.caltech#

Utilities for working with the Caltech 101 <https://data.caltech.edu/records/mzrjq-6wc02> and Caltech 256 <https://data.caltech.edu/records/nyy15-4j048> datasets.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_caltech101_dataset`(dataset_dir[,Â ...]) | Downloads the Caltech 101 dataset.  
---|---  
`download_caltech256_dataset`(dataset_dir[,Â ...]) | Downloads the Caltech 256 dataset.  
  
fiftyone.utils.caltech.download_caltech101_dataset(_dataset_dir_ , _scratch_dir =None_)#
    

Downloads the Caltech 101 dataset.

See [this page](user_guide__import_datasets.md#imageclassificationdirectorytree-import) for the format in which `dataset_dir` will be arranged.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **scratch_dir** (_None_) â a scratch directory to use to download any necessary temporary files



Returns:
    

  * num_samples: the total number of downloaded images

  * classes: the list of all classes

  * did_download: whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

fiftyone.utils.caltech.download_caltech256_dataset(_dataset_dir_ , _scratch_dir =None_)#
    

Downloads the Caltech 256 dataset.

See [this page](user_guide__import_datasets.md#imageclassificationdirectorytree-import) for the format in which `dataset_dir` will be arranged.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **scratch_dir** (_None_) â a scratch directory to use to download any necessary temporary files



Returns:
    

  * num_samples: the total number of downloaded images

  * classes: the list of all classes

  * did_download: whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
