---
source_url: https://docs.voxel51.com/api/fiftyone.utils.fiw.html
---

# fiftyone.utils.fiw#

Utilities for working with the [Families in the Wild dataset](https://web.northeastern.edu/smilelab/fiw/).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`FIWDatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Importer for Faces in the Wild-formatted datasets stored on disk.  
---|---  
  
**Functions:**

`get_pairwise_labels`(samples[,Â label_type]) | Gets a list of all pairs of people that are related and the label of their relation, either through the "kinships" or "relationships" field.  
---|---  
`get_identifier_filepaths_map`(samples) | Creates a mapping of `family_id/member_id` identifier to a list of filepaths for each person.  
`download_fiw_dataset`(dataset_dir,Â split[,Â ...]) | Downloads and extracts the Families in the Wild dataset.  
  
class fiftyone.utils.fiw.FIWDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`BatchDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.BatchDatasetImporter "fiftyone.utils.data.importers.BatchDatasetImporter")

Importer for Faces in the Wild-formatted datasets stored on disk.

See [this page](https://github.com/visionjo/pykinship#db-contents-and-structure) for format details.

**Methods:**

`import_samples`(dataset[,Â tags]) | Imports samples and labels stored on disk following the format of the Families in the Wild dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
import_samples(_dataset_ , _tags =None_)#
    

Imports samples and labels stored on disk following the format of the Families in the Wild dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **tags** (_None_) â an optional list of tags to attach to each sample



Returns:
    

a list of IDs of the samples that were added to the dataset

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

fiftyone.utils.fiw.get_pairwise_labels(_samples_ , _label_type ='kinships'_)#
    

Gets a list of all pairs of people that are related and the label of their relation, either through the âkinshipsâ or ârelationshipsâ field.

Example:
    
    
    [
       ["F0009/MID2", "F0009/MID4", "sibling"],
       ...
    ]
    

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_type** (_"kinships"_) â the type of label of which to return pairwise listings options are `("kinships", "relationships")`



Returns:
    

a list of triplets containing the identifier of person 1, identifier of person 2, and their kinship or relationship

fiftyone.utils.fiw.get_identifier_filepaths_map(_samples_)#
    

Creates a mapping of `family_id/member_id` identifier to a list of filepaths for each person.

Example:
    
    
    {
        "F0325/MID4": [
            "/path/to/fiftyone/fiw/train/data/F0325/MID4/P03451_face4.jpg",
            ...
        ],
        ...
    }
    

Parameters:
    

**samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Returns:
    

a dict mapping `family_id/member_id` identifiers to a list of filepaths containing images of the corresponding person

fiftyone.utils.fiw.download_fiw_dataset(_dataset_dir_ , _split_ , _scratch_dir =None_, _cleanup =False_)#
    

Downloads and extracts the Families in the Wild dataset.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to output the final dataset

  * **split** â the split being loaded

  * **scratch_dir** (_None_) â a scratch directory to use to store temporary files

  * **cleanup** (_True_) â whether to cleanup the scratch directory after extraction




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
