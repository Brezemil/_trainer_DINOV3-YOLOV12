---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-data-import.html
---

![Enterprise Skill](https://img.shields.io/badge/Enterprise-Skill-orange)

# Data Import#

Import media and labels into a FiftyOne Enterprise dataset. Supports images, videos, point clouds, and all major label formats including COCO, YOLO, VOC, KITTI, and Hugging Face Hub.

![Data Import](https://cdn.voxel51.com/fiftyone-internal-skills/import.webp)

## Requirements#

[FiftyOne Enterprise](https://voxel51.com/fiftyone-teams)

[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

## Usage#

Ask your AI assistant:
    
    
    "I want to add more samples to this dataset. I have a COCO labels file at gs://my-bucket/labels.json and images at gs://my-bucket/data/"
    "Import my YOLO dataset from /data/yolo into a new dataset called my-detections"
    "Load images from /data/raw into my existing dataset"
    

The skill confirms paths and format with you, presents an import plan, then runs the import as a delegated job.

## See also#

[FiftyOne Enterprise docs](https://docs.voxel51.com/teams/index.html)

[Supported dataset formats](https://docs.voxel51.com/user_guide/dataset_creation/index.html)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
