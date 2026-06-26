---
source_url: https://docs.voxel51.com/api/fiftyone.utils.random.html
---

# fiftyone.utils.random#

Random sampling utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`random_split`(sample_collection,Â split_fracs) | Generates a random partition of the samples in the collection according to the specified split fractions.  
---|---  
`weighted_sample`(sample_collection,Â k,Â weights) | Generates a random sample of size `k` from the given collection such that the probability of selecting each sample is proportional to the given per-sample weights.  
`balanced_sample`(sample_collection,Â k,Â path) | Generates a random sample of size `k` from the given collection such that the expected histogram of `path` values in the sample is uniform.  
  
fiftyone.utils.random.random_split(_sample_collection_ , _split_fracs_ , _seed =None_)#
    

Generates a random partition of the samples in the collection according to the specified split fractions.

Example:
    
    
    import fiftyone as fo
    import fiftyone.utils.random as four
    import fiftyone.zoo as foz
    
    # A dataset with `ground_truth` detections and no tags
    dataset = (
        foz.load_zoo_dataset("quickstart")
        .select_fields("ground_truth")
        .set_field("tags", [])
    ).clone()
    
    #
    # Generate a random sample and encode results via tags
    #
    
    four.random_split(dataset, {"train": 0.7, "test": 0.2, "val": 0.1})
    
    print(dataset.count_sample_tags())
    # {'train': 140, 'test': 40, 'val': 20}
    
    #
    # Generate a random sample in-memory
    #
    
    view1, view2 = four.random_split(dataset, [0.5, 0.5])
    
    assert len(view1) + len(view2) == len(dataset)
    assert set(view1.values("id")).isdisjoint(set(view2.values("id")))
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **split_fracs** â 

can be either of the following:

    * a dict mapping tag strings to split fractions in `[0, 1]`. In this case, the partition is denoted by tagging each sample with its assigned split

    * a list of split fractions in `[0, 1]`. In this case, a corresponding list of [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") instances containing the partition is returned

In either case, the split fractions are normalized so that they sum to 1, if necessary

  * **seed** (_None_) â an optional random seed



Returns:
    

one of the following

  * `None`, if `split_fracs` is a dict

  * a tuple of [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") instances, if `split_fracs` is a list




fiftyone.utils.random.weighted_sample(_sample_collection_ , _k_ , _weights_ , _tag =None_, _exact =True_, _seed =None_)#
    

Generates a random sample of size `k` from the given collection such that the probability of selecting each sample is proportional to the given per-sample weights.

Example:
    
    
    import fiftyone as fo
    import fiftyone.utils.random as four
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="train")
    
    # Sample proportional to label length
    weights = dataset.values(F("ground_truth.label").strlen())
    sample = four.weighted_sample(dataset, 10000, weights)
    
    # Plot results
    plot = fo.CategoricalHistogram(
        "ground_truth.label",
        order=lambda kv: -len(kv[0]),  # order by label length
        init_view=sample,
    )
    plot.show()
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **k** â the number of samples to select

  * **weights** â an array of per-sample weights

  * **tag** (_None_) â an optional sample tag to use to encode the results

  * **exact** (_True_) â whether to tag exactly `k` samples (True) or sample so that the expected number of samples is `k` (False)

  * **seed** (_None_) â an optional random seed to use



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the sample

fiftyone.utils.random.balanced_sample(_sample_collection_ , _k_ , _path_ , _tag =None_, _exact =True_, _seed =None_)#
    

Generates a random sample of size `k` from the given collection such that the expected histogram of `path` values in the sample is uniform.

Example:
    
    
    import fiftyone as fo
    import fiftyone.utils.random as four
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="train")
    
    # Sample proportional to label length
    weights = dataset.values(F("ground_truth.label").strlen())
    view1 = four.weighted_sample(dataset, 10000, weights)
    
    # Now take a balanced sample from this unbalanced sample
    view2 = four.balanced_sample(view1, 2000, "ground_truth.label")
    
    # Plot results
    plot1 = fo.CategoricalHistogram("ground_truth.label", init_view=dataset)
    plot2 = fo.CategoricalHistogram(
        "ground_truth.label",
        order=lambda kv: -len(kv[0]),  # order by label length
        init_view=view1,
    )
    plot3 = fo.CategoricalHistogram("ground_truth.label", init_view=view2)
    plot = fo.ViewGrid([plot1, plot2, plot3])
    plot.show()
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **k** â the number of samples to select

  * **path** â the categorical field against which to sample, e.g., `"ground_truth.label"`

  * **tag** (_None_) â an optional sample tag to use to encode the results

  * **exact** (_True_) â whether to tag exactly `k` samples (True) or sample so that the expected number of samples is `k` (False)

  * **seed** (_None_) â an optional random seed to use



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the sample

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
