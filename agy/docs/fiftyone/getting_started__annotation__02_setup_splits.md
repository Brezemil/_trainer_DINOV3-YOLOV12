---
source_url: https://docs.voxel51.com/getting_started/annotation/02_setup_splits.html
---

[ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/02_setup_splits.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/02_setup_splits.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/annotation/02_setup_splits.ipynb)

# Step 2: Setup Data Splits#

Before iterating on annotations, you need proper data splits. Without them, youâll contaminate your evaluation and build a model that only looks good on paper. This step uses the **quickstart-groups** dataset (KITTI multimodal data with left/right cameras and point clouds) and creates:

  * **Test set (15%)** \- Frozen. Never used for selection or training. Final evaluation only.
  * **Validation set (15%)** \- For iteration decisions. Used to evaluate between training rounds.
  * **Golden QA set (5%)** \- Small, heavily reviewed. Detects label drift.
  * **Pool (65%)** \- Active learning pool. All new labels come from here.



> **Critical:** Splits are created at the **group level** (scene), not sample level. This ensures the same scene stays together across all slices (left, right, pcd), preventing data leakage.
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import random
    
    DATASET_NAME = "annotation_tutorial"
    

## Load or Create the Dataset#

We clone `quickstart-groups` to a persistent working dataset. This keeps your annotations separate from the zoo dataset.
    
    
    [ ]:
    
    
    
    # Load or create the dataset (idempotent - safe to rerun)
    if DATASET_NAME in fo.list_datasets():
        print(f"Loading existing dataset: {DATASET_NAME}")
        dataset = fo.load_dataset(DATASET_NAME)
    
        # Check if splits already exist
        existing_views = dataset.list_saved_views()
        if "pool" in existing_views:
            print("Splits already exist. Skipping creation.")
            SPLITS_EXIST = True
        else:
            SPLITS_EXIST = False
    else:
        print(f"Creating new dataset: {DATASET_NAME}")
        source = foz.load_zoo_dataset("quickstart-groups")
        dataset = source.clone(DATASET_NAME)
        dataset.persistent = True
        SPLITS_EXIST = False
    
    print(f"\nDataset: {dataset.name}")
    print(f"Media type: {dataset.media_type}")
    print(f"Group slices: {dataset.group_slices}")
    print(f"Default slice: {dataset.default_group_slice}")
    print(f"Num groups (scenes): {len(dataset.distinct('group.id'))}")
    total_samples = sum(len(dataset.select_group_slices([s])) for s in dataset.group_slices)
    print(f"Num samples (all slices): {total_samples}")
    

## Understand the Grouped Structure#

The `quickstart-groups` dataset is a **grouped dataset** from KITTI: | Slice | Content | Purpose  
---|---|---  
`left` | Left camera images | 2D detection annotation  
`right` | Right camera images | Stereo pair (optional use)  
`pcd` | Point cloud data | 3D cuboid annotation  
  
Each **group** represents one scene/frame with synchronized data across all sensors.
    
    
    [ ]:
    
    
    
    # Explore a single group
    group_ids = dataset.distinct("group.id")
    example_group_id = group_ids[0]
    
    print(f"Example group ID: {example_group_id}")
    print(f"\nSamples in this group:")
    
    example_group = dataset.get_group(example_group_id)
    for slice_name, sample in example_group.items():
        print(f"  {slice_name}: {sample.filepath.split("/")[-1]}")
    

## Create Splits at the Group Level#

**Why group-level splits?**

If we split at the sample level, the same scene could end up in both train and test (just different slices). This causes data leakage - the model âseesâ scenes at training time that appear in evaluation.

By splitting at the **group level** , we ensure:

  * All slices from the same scene stay together

  * No information leaks between splits



    
    
    [ ]:
    
    
    
    # Tag ALL samples in each group with the split tag
    # Must iterate all slices since grouped datasets segment by slice
    if not SPLITS_EXIST:
        from fiftyone import ViewField as F
    
        # Build group-to-split mapping
        group_to_split = {}
        for gid in test_groups:
            group_to_split[gid] = "split:test"
        for gid in val_groups:
            group_to_split[gid] = "split:val"
        for gid in golden_groups:
            group_to_split[gid] = "split:golden"
        for gid in pool_groups:
            group_to_split[gid] = "split:pool"
    
        # Tag samples across ALL slices
        for slice_name in dataset.group_slices:
            view = dataset.select_group_slices([slice_name])
            for sample in view.iter_samples(autosave=True):
                split_tag = group_to_split.get(sample.group.id)
                if split_tag:
                    sample.tags.append(split_tag)
    
        # Save views for easy access
        dataset.save_view("test_set", dataset.match_tags("split:test"))
        dataset.save_view("val_set", dataset.match_tags("split:val"))
        dataset.save_view("golden_qa", dataset.match_tags("split:golden"))
        dataset.save_view("pool", dataset.match_tags("split:pool"))
    
        print("Splits created and saved as views.")
    else:
        print("Using existing splits.")
    
    
    
    [ ]:
    
    
    
    # Add annotation tracking field (idempotent)
    if "annotation_status" not in dataset.get_field_schema():
        dataset.add_sample_field("annotation_status", fo.StringField)
        dataset.set_values("annotation_status", ["unlabeled"] * dataset.count())
        print("Added annotation_status field (all samples start as 'unlabeled')")
    else:
        print("annotation_status field already exists.")
    
    
    
    [ ]:
    
    
    
    # Verify setup
    from fiftyone import ViewField as F
    
    print("Saved views:", dataset.list_saved_views())
    print()
    
    for view_name in ["test_set", "val_set", "golden_qa", "pool"]:
        view = dataset.load_saved_view(view_name)
        # Count unique groups in view
        n_groups = len(view.distinct("group.id"))
        n_samples = len(view)
        print(f"{view_name}: {n_groups} groups, {n_samples} samples (all slices)")
    

## Launch the App#

Explore your grouped dataset in the App. Notice:

  * The **group mode** shows synchronized samples

  * Use the **slice selector** to switch between left, right, and pcd

  * Filter by split tags to see each partition



    
    
    [ ]:
    
    
    
    session = fo.launch_app(dataset)
    

## Summary#

You created four data splits with clear purposes:

  * Test (frozen), Val (iteration), Golden (QA), Pool (labeling source)

  * **Splits are at the group level** \- same scene = same split across all slices




**Artifacts:**

  * `annotation_tutorial` dataset (persistent clone of quickstart-groups)

  * Split tags: `split:test`, `split:val`, `split:golden`, `split:pool`

  * Saved views: `test_set`, `val_set`, `golden_qa`, `pool`

  * `annotation_status` field for tracking progress




**Next:** Step 3 - Smart Sample Selection

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
