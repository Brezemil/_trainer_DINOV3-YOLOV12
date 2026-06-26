---
source_url: https://docs.voxel51.com/api/fiftyone.utils.cityscapes.html
---

# fiftyone.utils.cityscapes#

Utilities for working with the [Cityscapes dataset](https://www.cityscapes-dataset.com).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`parse_cityscapes_dataset`(source_dir,Â ...[,Â ...]) | Parses the Cityscapes archive(s) in the specified directory and writes the requested splits in subdirectories of `dataset_dir` in [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format.  
---|---  
  
fiftyone.utils.cityscapes.parse_cityscapes_dataset(_source_dir_ , _dataset_dir_ , _scratch_dir_ , _splits_ , _fine_annos =None_, _coarse_annos =None_, _person_annos =None_)#
    

Parses the Cityscapes archive(s) in the specified directory and writes the requested splits in subdirectories of `dataset_dir` in [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format.

The archives must have been manually downloaded into the directory before this method is called.

The `source_dir` should contain the following files:
    
    
    source_dir/
        leftImg8bit_trainvaltest.zip
        gtFine_trainvaltest.zip             # optional
        gtCoarse.zip                        # optional
        gtBbox_cityPersons_trainval.zip     # optional
    

Parameters:
    

  * **source_dir** â the directory containing the manually downloaded Cityscapes files

  * **dataset_dir** â the directory in which to build the output dataset

  * **scratch_dir** â a scratch directory to use for temporary files

  * **splits** â a list of splits to parse. Supported values are `(train, test, validation)`

  * **fine_annos** (_None_) â whether to load the fine annotations (True), or not (False), or only if the ZIP file exists (None)

  * **coarse_annos** (_None_) â whether to load the coarse annotations (True), or not (False), or only if the ZIP file exists (None)

  * **person_annos** (_None_) â whether to load the person detections (True), or not (False), or only if the ZIP file exists (None)



Raises:
    

**OSError** â if any required source files are not present

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
