---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/skill_cards.html
---

**ð¥ fiftyone-dataset-import**

Universal dataset import for FiftyOne supporting all media types (images, videos, point clouds, 3D scenes), all label formats (COCO, YOLO, VOC, CVAT, KITTI, etc.), multimodal grouped datasets, and Hugging Face Hub datasets. Use when users want to import any dataset regardless of format or source, load datasets from Hugging Face, handle autonomous driving data with multiple cameras and LiDAR, or create grouped datasets from multimodal data.

Import

**ð¤ fiftyone-dataset-export**

Export FiftyOne datasets to standard formats (COCO, YOLO, VOC, CVAT, CSV, etc.) and Hugging Face Hub. Use when converting datasets, exporting for training, creating archives, sharing data in specific formats, or publishing datasets to Hugging Face Hub.

Export

**ð fiftyone-find-duplicates**

Find duplicate or near-duplicate images in FiftyOne datasets using brain similarity computation. Use when users want to deduplicate datasets, find similar images, cluster visually similar content, or remove redundant samples. Requires FiftyOne MCP server with @voxel51/brain plugin installed.

QA

**ð¤ fiftyone-dataset-inference**

Run model inference on FiftyOne datasets using Zoo models or custom models. Use when applying ML models for detection, classification, segmentation, or embeddings on existing datasets.

Inference

**ð fiftyone-model-evaluation**

Evaluate model predictions against ground truth using COCO, Open Images, or custom protocols. Use when computing mAP, precision, recall, confusion matrices, or analyzing TP/FP/FN examples for detection, classification, segmentation, or regression tasks.

Evaluation

**ð fiftyone-embeddings-visualization**

Visualize datasets in 2D using embeddings with UMAP or t-SNE dimensionality reduction. Use when users want to explore dataset structure, find clusters in images, identify outliers, color samples by class or metadata, or understand data distribution.

Embeddings

**ð§¹ fiftyone-dataset-curation**

End-to-end dataset curation for any FiftyOne dataset\: inspect schema and media quality (blur, brightness, corruption, resolution), audit annotation quality (mistakenness, hardness, duplicate labels, IoU overlaps), analyze class distributions and imbalances, explore embedding space and data gaps, find near/exact duplicates, create curated subsets using semantic search and brain ops, build train/val/test splits, and answer natural language questions about your data. Delegates to fiftyone-find-duplicates and fiftyone-embeddings-visualization. Requires FiftyOne MCP server with @voxel51/brain and @voxel51/utils plugins.

Curation

**ð fiftyone-develop-plugin**

Develop custom FiftyOne plugins (operators and panels) from scratch. Use when users want to create, build, or develop a new plugin for FiftyOne App, extend FiftyOne with custom operators, create interactive panels, add new functionality to FiftyOne, or integrate external APIs/services into FiftyOne.

Development

**ð fiftyone-code-style**

Write Python code following FiftyOne's official conventions. Use when contributing to FiftyOne, developing plugins, or writing code that integrates with FiftyOne's codebase. Covers module structure, import organization, Google-style docstrings, lazy imports, guard patterns, and error handling.

Development

**ð¨ fiftyone-voodo-design**

Build FiftyOne UIs using VOODO (@voxel51/voodo), the official React component library. Use when building plugin panels, creating interactive UIs, styling FiftyOne applications, or needing React components with proper design tokens. Fetches complete component API reference dynamically.

Development

**ð·ï¸ fiftyone-issue-triage**

Triage FiftyOne GitHub issues by validating status, categorizing resolution, and generating standardized responses. Use when reviewing issues to determine if already fixed, won't fix, not reproducible, no longer relevant, or still valid. Includes investigation workflow and response templates.

Support

**ð fiftyone-create-notebook**

Creates Jupyter notebooks for FiftyOne workflows including getting-started guides, tutorials, recipes, and full ML pipelines. Use when users want to create a notebook, write a tutorial, build a demo, document a workflow, or generate a FiftyOne walkthrough covering data loading, exploration, inference, evaluation, and export. Builds notebooks cell-by-cell using NotebookEdit.

Development

**ð§ fiftyone-troubleshoot**

Diagnose and fix common FiftyOne issues automatically. Use when a dataset disappeared, the App won't open, changes aren't saving, MongoDB errors occur, video codecs fail, notebook connectivity breaks, operators are missing, or any recurring FiftyOne pain point needs solving. Includes a NEVER-DO safety section to prevent accidental data loss or direct MongoDB manipulation.

Support

**ð fiftyone-generate-data-lens-connector**

Generate a Data Lens connector from an external database schema. Use when users want to connect an external data source (PostgreSQL, BigQuery, Databricks, MySQL, SQLite, etc.) to FiftyOne Data Lens, create a DataLensOperator from a CREATE TABLE statement or column list, or build a plugin that lets users browse and import data from their database through the FiftyOne App.

Development

**ð¡ï¸ fiftyone-eval-plugin**

Evaluates FiftyOne plugins for quality, security, and agent-readiness. Use when reviewing a plugin before installation, auditing an existing plugin, validating a plugin you just built, or assessing community plugins for safety. Checks manifest integrity, security risks (filesystem access, network calls, command execution, data exfiltration), schema quality, risk classification, code conventions, and agent discoverability. Produces a structured report with scores and actionable recommendations.

Development

**ð§© fiftyone-zoo-remote-model**

Integrate models into FiftyOne's remote model zoo. Use when wrapping a model (detection, classification, segmentation, embedding, keypoint, or vision-language) for `register_zoo_model_source` and `load_zoo_model` so it works with `dataset.apply_model`, debugging zoo registration, fixing `manifest.json` issues, building custom `fom.Model` / `TorchModelMixin` subclasses, or resolving DataLoader pickle errors and `ModuleNotFoundError` from spawned multi-worker DataLoader workers.

Development

**ð¤ fiftyone-data-distribution**

Enterprise  
Use when the user wants to understand, explore, analyze, or summarize a dataset â including requests like "what does my data look like", "give me an overview", "summarize this dataset", "tell me about this dataset", "what fields do I have", "what classes are in my dataset", "how many samples per class", "show me the distribution", "analyze my data", "explore my dataset", or "give me stats on my data". Discovers all interesting fields automatically, presents distribution summaries as tables, flags imbalances and outliers, and opens the Histograms panel in the App for visual exploration.

Curate,Enterprise

**ð¤ fiftyone-data-enrichment**

Enterprise  
Enriches a FiftyOne dataset with no or minimal metadata by computing image properties, visual embeddings, and UMAP visualizations. Use when the user has raw unlabeled media and wants to draw insights, run natural language queries, or set up downstream labeling workflows. Does NOT perform auto-labeling â delegate that to fiftyone-auto-labeling.

Curate,Enterprise

**ð¤ fiftyone-data-export**

Enterprise  
Exports a FiftyOne dataset or filtered subset to standard formats (COCO, YOLO, VOC, CSV, etc.) for downstream workflows like model training. Use when the user wants to export specific views, label fields, or media for use outside FiftyOne.

Export,Enterprise

**ð¤ fiftyone-data-import**

Enterprise  
Imports media and/or labels into a FOE dataset using the builtin import operator. Use when the user wants to ingest images, videos, or point clouds with or without annotation labels to begin curation, annotation, or evaluation workflows.

Import,Enterprise

**ð¤ fiftyone-data-quality**

Enterprise  
Use when the user wants to check data quality, find bad images, or detect noisy, blurry, or duplicate samples â including requests like "check my data quality", "find blurry images", "are there duplicates in my dataset", "my images look bad", "clean my dataset". Computes quality metrics and opens the Data Quality panel for interactive review.

Curate,Enterprise

**ð¤ fiftyone-model-evaluation**

Enterprise  
Evaluates a model and explores results in the ME panel. Use when the user wants to compute mAP, precision, recall, F1, confusion matrices, or TP/FP/FN â or when they want to explore existing evaluation results, configure scenarios, or surface failure modes by class, data slice, or confidence range.

Evaluate,Enterprise

**ð¤ fiftyone-dataset-discovery**

Enterprise  
Use when the user wants to find, browse, or load a dataset â including requests like "what datasets do I have", "find something medical", "do I have any driving data", "open the video dataset". Lists available datasets filtered by name, tag, or media type, then loads the chosen one into the App.

Curate,Enterprise

**ð¤ fiftyone-sdk-guidance**

Enterprise  
Use when the user asks how to do something in the FiftyOne Python SDK, asks a docs question, or when no skill or operator is available to accomplish their goal â including requests like "how do I do X in Python", "show me the SDK for filtering", "there's no operator for this, can I do it in code", "what's the API for embeddings", "write me a Python script to do Y". Searches live FiftyOne documentation and returns runnable code examples.

Docs,Enterprise

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
