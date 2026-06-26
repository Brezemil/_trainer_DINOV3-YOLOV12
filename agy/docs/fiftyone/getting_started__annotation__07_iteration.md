---
source_url: https://docs.voxel51.com/getting_started/annotation/07_iteration.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/07_iteration.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/07_iteration.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/annotation/07_iteration.ipynb)

# Step 7: Iteration Loop#

Now you have a trained model and know where it fails. This step shows how to:

  1. Run a **Golden QA check** to detect annotation drift
  2. Select the **next batch** using a hybrid strategy

The hybrid strategy balances:

  * **30% Coverage** \- Diversity sampling to avoid tunnel vision
  * **70% Targeted** \- Samples similar to failures

This balance is critical. Only chasing failures creates a model thatâs great at edge cases and terrible at normal cases.
    
    
    [ ]:
    
    
    
    !pip install -q scikit-learn
    
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    import fiftyone.brain as fob
    from fiftyone import ViewField as F
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    from collections import Counter
    
    LABEL_FIELD_2D = "human_detections"
    
    dataset = fo.load_dataset("annotation_tutorial")
    
    # Get schema classes
    if "annotation_schema_2d" in dataset.info:
        SCHEMA_CLASSES = set(dataset.info["annotation_schema_2d"]["classes"])
    else:
        SCHEMA_CLASSES = {"Car", "Van", "Truck", "Pedestrian", "Person_sitting", "Cyclist", "Tram", "Misc"}
    

## Golden QA Check#

Before selecting the next batch, verify annotation quality hasnât drifted. The golden set is a small, carefully reviewed sample we check each iteration. **What to look for:**

  * Label count distribution staying stable
  * No unexpected empty samples
  * Class distribution roughly matching earlier rounds


    
    
    [ ]:
    
    
    
    # Load golden QA set (left camera slice)
    golden = dataset.load_saved_view("golden_qa").select_group_slices(["left"])
    
    # For tutorial, copy ground_truth to human_detections if not present
    for sample in golden:
        if sample.ground_truth and not sample[LABEL_FIELD_2D]:
            filtered_dets = [
                fo.Detection(label=d.label, bounding_box=d.bounding_box)
                for d in sample.ground_truth.detections
                if d.label in SCHEMA_CLASSES
            ]
            sample[LABEL_FIELD_2D] = fo.Detections(detections=filtered_dets)
            sample.save()
    
    print(f"Golden QA set (left camera): {len(golden)} samples")
    
    
    
    [ ]:
    
    
    
    # Golden QA Check: Compute baseline stats
    golden_stats = {
        "total_samples": len(golden),
        "samples_with_labels": 0,
        "total_detections": 0,
        "class_counts": Counter()
    }
    
    for sample in golden:
        if sample[LABEL_FIELD_2D] and len(sample[LABEL_FIELD_2D].detections) > 0:
            golden_stats["samples_with_labels"] += 1
            golden_stats["total_detections"] += len(sample[LABEL_FIELD_2D].detections)
            for det in sample[LABEL_FIELD_2D].detections:
                golden_stats["class_counts"][det.label] += 1
    
    print("=" * 40)
    print("GOLDEN QA CHECK")
    print("=" * 40)
    print(f"Samples with labels: {golden_stats['samples_with_labels']}/{golden_stats['total_samples']}")
    print(f"Total detections: {golden_stats['total_detections']}")
    print(f"Avg detections/sample: {golden_stats['total_detections']/max(1,golden_stats['samples_with_labels']):.1f}")
    print(f"\nTop classes:")
    for cls, count in golden_stats["class_counts"].most_common(5):
        print(f"  {cls}: {count}")
    print("=" * 40)
    print("\nIf these numbers change unexpectedly between iterations,")
    print("investigate annotation consistency before continuing.")
    
    
    
    [ ]:
    
    
    
    # Store golden stats for comparison in future iterations
    if "golden_qa_history" not in dataset.info:
        dataset.info["golden_qa_history"] = []
    
    dataset.info["golden_qa_history"].append({
        "iteration": len(dataset.info["golden_qa_history"]),
        "samples_with_labels": golden_stats["samples_with_labels"],
        "total_detections": golden_stats["total_detections"],
        "top_classes": dict(golden_stats["class_counts"].most_common(5))
    })
    dataset.save()
    
    print(f"Saved golden QA stats (iteration {len(dataset.info['golden_qa_history'])-1})")
    

## Prepare for Next Batch Selection#
    
    
    [ ]:
    
    
    
    # Get unlabeled groups from pool
    pool = dataset.load_saved_view("pool")
    pool_left = pool.select_group_slices(["left"])
    
    # Find samples still unlabeled
    remaining = pool_left.match(F("annotation_status") == "unlabeled")
    remaining_groups = remaining.distinct("group.id")
    
    print(f"Pool (left camera): {len(pool_left)} samples")
    print(f"Remaining unlabeled: {len(remaining)} samples ({len(remaining_groups)} groups)")
    
    
    
    [ ]:
    
    
    
    # Get failure samples from evaluation
    try:
        failures = dataset.load_saved_view("eval_v0_failures")
        print(f"Failure samples: {len(failures)}")
    except:
        failures = dataset.limit(0)  # Empty view
        print("No failure view found. Run Step 6 first, or continue with coverage-only selection.")
    

## Define Acquisition Budget#

**Batch sizing guidance:**

  * Size batches to your labeling capacity
  * For this tutorial, weâll select ~20% of remaining groups


    
    
    [ ]:
    
    
    
    # Select batch size based on remaining pool
    batch_size = max(10, int(0.20 * len(remaining_groups)))
    
    # Split: 30% coverage (ZCore), 70% targeted
    coverage_budget = int(0.30 * batch_size)
    targeted_budget = batch_size - coverage_budget
    
    print(f"Batch v1 budget: {batch_size} groups")
    print(f"  Coverage (diversity): {coverage_budget} (30%)")
    print(f"  Targeted (failures): {targeted_budget} (70%)")
    

## Part 1: Coverage Selection (30%)#

Use ZCore scores computed in Step 3 to select diverse groups from remaining pool.
    
    
    [ ]:
    
    
    
    # Get samples with ZCore scores from remaining pool
    remaining_with_scores = remaining.match(F("zcore") != None)
    
    if len(remaining_with_scores) == 0:
        print("No ZCore scores found in remaining pool. Using random coverage selection.")
        # Random fallback
        coverage_groups = list(remaining_groups)[:coverage_budget]
    else:
        # Build group -> score mapping
        group_scores = {}
        for sample in remaining_with_scores:
            group_scores[sample.group.id] = sample.zcore
    
        # Sort and select top groups
        sorted_groups = sorted(group_scores.items(), key=lambda x: x[1], reverse=True)
        coverage_groups = [gid for gid, _ in sorted_groups[:coverage_budget]]
    
    print(f"Coverage selection: {len(coverage_groups)} groups")
    

## Part 2: Targeted Selection (70%)#

Find groups similar to failures using embedding-based neighbor search.
    
    
    [ ]:
    
    
    
    def find_neighbor_groups(query_embs, query_group_ids, pool_embs, pool_group_ids, n_per_query=3):
        """Find nearest neighbor groups in embedding space."""
        if len(query_embs) == 0 or len(pool_embs) == 0:
            return []
    
        sims = cosine_similarity(query_embs, pool_embs)
        neighbor_groups = set()
    
        for sim_row in sims:
            top_idx = np.argsort(sim_row)[-n_per_query:]
            for idx in top_idx:
                neighbor_groups.add(pool_group_ids[idx])
    
        return list(neighbor_groups)
    
    
    
    [ ]:
    
    
    
    # Get embeddings for remaining samples
    remaining_samples = list(remaining)
    remaining_embs = np.array([s.embeddings for s in remaining_samples if s.embeddings is not None])
    remaining_group_ids = [s.group.id for s in remaining_samples if s.embeddings is not None]
    
    if len(failures) > 0 and len(remaining_embs) > 0:
        failure_embs = np.array([s.embeddings for s in failures if s.embeddings is not None])
        failure_group_ids = [s.group.id for s in failures if s.embeddings is not None]
    
        print(f"Finding neighbors of {len(failure_embs)} failure samples...")
    
        # Find neighbor groups (excluding already-selected coverage groups)
        targeted_groups = find_neighbor_groups(
            failure_embs, failure_group_ids,
            remaining_embs, remaining_group_ids,
            n_per_query=5
        )
        targeted_groups = [gid for gid in targeted_groups if gid not in coverage_groups][:targeted_budget]
        print(f"Targeted selection: {len(targeted_groups)} groups")
    else:
        print("No failures to target or no embeddings. Using coverage-only selection.")
        # Fall back to more coverage
        if len(remaining_with_scores) > coverage_budget:
            extra_groups = [gid for gid, _ in sorted_groups[coverage_budget:coverage_budget + targeted_budget]]
            targeted_groups = [gid for gid in extra_groups if gid not in coverage_groups]
        else:
            targeted_groups = []
        print(f"Additional coverage selection: {len(targeted_groups)} groups")
    

## Combine and Tag Batch v1#
    
    
    [ ]:
    
    
    
    # Combine selections
    batch_v1_groups = list(set(coverage_groups + targeted_groups))
    
    if len(batch_v1_groups) == 0:
        print("No groups selected. Check that Steps 3 and 6 completed successfully.")
    else:
        # Select ALL samples in these groups (all slices)
        batch_v1 = dataset.match(F("group.id").is_in(batch_v1_groups))
    
        # Tag
        batch_v1.tag_samples("batch:v1")
        batch_v1.tag_samples("to_annotate")
        batch_v1.set_values("annotation_status", ["selected"] * len(batch_v1))
    
        # Track source for analysis
        dataset.match(F("group.id").is_in(coverage_groups)).tag_samples("source:coverage")
        dataset.match(F("group.id").is_in(targeted_groups)).tag_samples("source:targeted")
    
        # Save view
        dataset.save_view("batch_v1", dataset.match_tags("batch:v1"))
    
        print(f"\nBatch v1: {len(batch_v1_groups)} groups")
        print(f"  Coverage: {len(coverage_groups)}")
        print(f"  Targeted: {len(targeted_groups)}")
        print(f"  Total samples (all slices): {len(batch_v1)}")
    

## The Complete Loop#

You now have the full iteration recipe:
    
    
    1. Run Golden QA check (detect drift)
    2. Annotate the current batch:
       - Step 4: 2D detections on left camera
       - Step 5: 3D cuboids on point cloud
    3. Train on all annotated data (Step 6)
    4. Evaluate on val set, tag failures
    5. Select next batch: 30% coverage + 70% targeted
    6. Repeat until stopping criteria
    

### Stopping Criteria#

Stop when:

  * Gains per labeled sample flatten (diminishing returns)
  * Remaining failures are mostly label ambiguity
  * Val metrics hit your target threshold



### The 30% Coverage Rule#

**Donât skip the coverage budget.** Only chasing failures leads to:

  * Overfitting to edge cases
  * Distorted class priors
  * Models that fail on ânormalâ inputs

Coverage keeps you honest.
    
    
    [ ]:
    
    
    
    # Progress summary
    pool = dataset.load_saved_view("pool")
    pool_groups = pool.distinct("group.id")
    total_pool_groups = len(pool_groups)
    
    annotated_groups = len(dataset.match_tags("annotated:v0").distinct("group.id"))
    selected_v1_groups = len(dataset.match_tags("batch:v1").distinct("group.id"))
    
    pool_left = pool.select_group_slices(["left"])
    still_unlabeled = len(pool_left.match(F("annotation_status") == "unlabeled").distinct("group.id"))
    
    print("=" * 40)
    print("ANNOTATION PROGRESS (by group/scene)")
    print("=" * 40)
    print(f"Pool total:      {total_pool_groups} groups")
    print(f"Annotated (v0):  {annotated_groups} groups ({100*annotated_groups/total_pool_groups:.0f}%)")
    print(f"Selected (v1):   {selected_v1_groups} groups ({100*selected_v1_groups/total_pool_groups:.0f}%)")
    print(f"Still unlabeled: {still_unlabeled} groups ({100*still_unlabeled/total_pool_groups:.0f}%)")
    print("=" * 40)
    

## Summary#

You implemented the iteration loop:

  * **Golden QA check** to detect annotation drift
  * **Hybrid acquisition** : 30% coverage + 70% targeted
  * Tagged `batch:v1` ready for annotation (all slices: left, right, pcd)

**Why this works:**

  * Coverage prevents overfitting to edge cases
  * Targeting fixes known failures
  * Golden QA catches annotation drift early
  * The combination improves faster than either strategy alone

**Your turn:** Repeat Steps 4-7 with batch_v1, then batch_v2, etc.

* * *

## Congratulations!#

Youâve completed the Full Loop annotation tutorial. You now know how to:

  1. **Setup** \- Create group-level splits for multimodal data
  2. **Select** \- Use ZCore for diversity-based sample selection
  3. **Annotate 2D** \- Label detections on camera images
  4. **Annotate 3D** \- Label cuboids on point clouds
  5. **Train + Evaluate** \- Train a model and analyze failures
  6. **Iterate** \- Use hybrid acquisition to select the next batch

This workflow scales from small experiments to production annotation pipelines. IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
