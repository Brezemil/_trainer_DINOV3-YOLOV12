---
source_url: https://docs.voxel51.com/getting_started/annotation/06_train_evaluate.html
---

[ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/06_train_evaluate.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/annotation/06_train_evaluate.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/annotation/06_train_evaluate.ipynb)

# Step 6: Train + Evaluate#

Train a 2D detector on your labeled data and evaluate it properly. Understanding **where** the model fails tells you what to label next.

> **Note:** We train on `human_detections` (2D labels from Step 4) using the **left camera slice**. For evaluation, we need labels on the val set too.
    
    
    [ ]:
    
    
    
    !pip install -q ultralytics
    
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    import os
    
    LABEL_FIELD_2D = "human_detections"
    
    dataset = fo.load_dataset("annotation_tutorial")
    
    # Get schema classes
    if "annotation_schema_2d" in dataset.info:
        SCHEMA_CLASSES = set(dataset.info["annotation_schema_2d"]["classes"])
    else:
        SCHEMA_CLASSES = {"Car", "Van", "Truck", "Pedestrian", "Person_sitting", "Cyclist", "Tram", "Misc"}
    
    print(f"Schema classes: {len(SCHEMA_CLASSES)}")
    

## Get Training Data#

**Important:** We train on the **left camera slice** of annotated groups. Only samples with actual labels are included.
    
    
    [ ]:
    
    
    
    # Training data: left camera slice with labels from annotated groups
    annotated_groups = dataset.match_tags("annotated:v0")
    annotated_left = annotated_groups.select_group_slices(["left"])
    
    # Filter to samples with actual detections
    train_view = annotated_left.match(F(f"{LABEL_FIELD_2D}.detections").length() > 0)
    
    print(f"Annotated groups: {len(annotated_groups.distinct('group.id'))}")
    print(f"Training samples (left camera with labels): {len(train_view)}")
    
    if len(train_view) == 0:
        print("\n>>> No training samples with labels. Complete Step 4 first.")
    
    
    
    [ ]:
    
    
    
    # Validation data: left camera slice from val set
    val_set = dataset.load_saved_view("val_set")
    val_left = val_set.select_group_slices(["left"])
    
    print(f"Validation groups: {len(val_set.distinct('group.id'))}")
    print(f"Validation samples (left camera): {len(val_left)}")
    
    
    
    [ ]:
    
    
    
    # For evaluation, we need human_detections on val set
    # In production, you'd label these. For tutorial, copy ground_truth
    # FILTERED to schema classes for consistency
    
    copied_count = 0
    skipped_count = 0
    
    for sample in val_left:
        if sample.ground_truth and not sample[LABEL_FIELD_2D]:
            filtered_dets = []
            for d in sample.ground_truth.detections:
                if d.label in SCHEMA_CLASSES:
                    filtered_dets.append(fo.Detection(
                        label=d.label,
                        bounding_box=d.bounding_box
                    ))
                    copied_count += 1
                else:
                    skipped_count += 1
            sample[LABEL_FIELD_2D] = fo.Detections(detections=filtered_dets)
            sample.save()
    
    print(f"Val set prepared: {copied_count} detections copied, {skipped_count} skipped (not in schema)")
    

## Export for Training#

Export the left camera images and labels in YOLO format.
    
    
    [ ]:
    
    
    
    if len(train_view) == 0:
        raise ValueError("No training samples. Complete Step 4 first.")
    
    # Get classes from training data
    classes = train_view.distinct(f"{LABEL_FIELD_2D}.detections.label")
    print(f"Classes in training data: {classes}")
    
    export_dir = "/tmp/annotation_tutorial_yolo"
    os.makedirs(export_dir, exist_ok=True)
    
    
    
    [ ]:
    
    
    
    # Export training data
    train_view.export(
        export_dir=os.path.join(export_dir, "train"),
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=LABEL_FIELD_2D,
        classes=classes,
    )
    
    # Export validation data (also needs labels)
    val_with_labels = val_left.match(F(f"{LABEL_FIELD_2D}.detections").length() > 0)
    val_with_labels.export(
        export_dir=os.path.join(export_dir, "val"),
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=LABEL_FIELD_2D,
        classes=classes,
    )
    
    print(f"Exported {len(train_view)} train, {len(val_with_labels)} val samples to {export_dir}")
    
    
    
    [ ]:
    
    
    
    # Create YAML config
    yaml_content = f"""path: {export_dir}
    train: train/images
    val: val/images
    
    names:
    """
    for i, cls in enumerate(classes):
        yaml_content += f"  {i}: {cls}\n"
    
    yaml_path = os.path.join(export_dir, "dataset.yaml")
    with open(yaml_path, "w") as f:
        f.write(yaml_content)
    
    print(f"Created {yaml_path}")
    

## Train YOLOv8#
    
    
    [ ]:
    
    
    
    from ultralytics import YOLO
    
    # Train (small model, few epochs for demo)
    model = YOLO('yolov8n.pt')
    results = model.train(
        data=yaml_path,
        epochs=10,
        imgsz=640,
        batch=8,
        name='tutorial_v0',
        project='/tmp/yolo_tutorial'
    )
    
    model_path = '/tmp/yolo_tutorial/tutorial_v0/weights/best.pt'
    print(f"Model saved: {model_path}")
    

## Run Inference on Validation#
    
    
    [ ]:
    
    
    
    # Load trained model
    model = YOLO(model_path)
    
    # Run inference on val set (left camera slice)
    for sample in val_left:
        results = model(sample.filepath, verbose=False)[0]
    
        detections = []
        if results.boxes is not None:
            for box in results.boxes:
                x1, y1, x2, y2 = box.xyxyn[0].tolist()
                conf = box.conf[0].item()
                cls_idx = int(box.cls[0].item())
                label = classes[cls_idx] if cls_idx < len(classes) else f"class_{cls_idx}"
    
                detections.append(fo.Detection(
                    label=label,
                    bounding_box=[x1, y1, x2-x1, y2-y1],
                    confidence=conf
                ))
    
        sample["predictions"] = fo.Detections(detections=detections)
        sample.save()
    
    print(f"Added predictions to {len(val_left)} val samples")
    

## Evaluate#
    
    
    [ ]:
    
    
    
    # Run evaluation
    results = val_left.evaluate_detections(
        "predictions",
        gt_field=LABEL_FIELD_2D,
        eval_key="eval_v0",
        compute_mAP=True
    )
    
    print(f"mAP: {results.mAP():.3f}")
    results.print_report()
    

## Analyze Failures#

Understanding failures is more important than the mAP number.
    
    
    [ ]:
    
    
    
    # Reload to see eval fields
    val_left = dataset.load_saved_view("val_set").select_group_slices(["left"])
    
    # Find high-FN samples (model missed objects)
    high_fn = val_left.sort_by("eval_v0_fn", reverse=True).limit(10)
    high_fn.tag_samples("failure:high_fn")
    
    # Find high-FP samples (model hallucinated)
    high_fp = val_left.sort_by("eval_v0_fp", reverse=True).limit(10)
    high_fp.tag_samples("failure:high_fp")
    
    print(f"Tagged {len(high_fn)} high-FN samples")
    print(f"Tagged {len(high_fp)} high-FP samples")
    
    
    
    [ ]:
    
    
    
    # View failures in App
    session = fo.launch_app(val_left)
    

In the App:

  1. Filter by `failure:high_fn` to see where model missed objects
  2. Filter by `failure:high_fp` to see where model hallucinated
  3. Look for patterns: specific classes? distances? occlusions?

These patterns tell you what to label next.
    
    
    [ ]:
    
    
    
    # Save evaluation info
    dataset.info["eval_v0"] = {
        "mAP": results.mAP(),
        "train_samples": len(train_view),
        "val_samples": len(val_left),
        "model_path": model_path
    }
    dataset.save()
    
    # Save failure view
    failures = val_left.match_tags(["failure:high_fn", "failure:high_fp"])
    dataset.save_view("eval_v0_failures", failures)
    
    print(f"Saved {len(failures)} failure samples to view 'eval_v0_failures'")
    

## Summary#

You trained and evaluated a 2D detector:

  * Used **left camera slice** from annotated groups
  * Exported in YOLO format
  * Trained YOLOv8n for 10 epochs
  * Evaluated with FiftyOne: mAP + per-sample FP/FN
  * Tagged failure cases for next iteration

**Key insight:** The failure tags tell you what to label next. **Artifacts:**

  * `predictions` field with model outputs
  * `eval_v0` evaluation results
  * Failure tags: `failure:high_fn`, `failure:high_fp`
  * `eval_v0_failures` saved view

**Next:** Step 7 - Iteration Loop IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
