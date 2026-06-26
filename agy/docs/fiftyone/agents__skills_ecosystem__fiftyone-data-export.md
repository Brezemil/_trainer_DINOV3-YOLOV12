---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-data-export.html
---

![Enterprise Skill](https://img.shields.io/badge/Enterprise-Skill-orange)

# Data Export#

Export a FiftyOne Enterprise dataset or filtered view to standard formats for model training, annotation pipelines, or downstream analysis.

![Data Export](https://cdn.voxel51.com/fiftyone-internal-skills/data_export.webp)

## Requirements#

[FiftyOne Enterprise](https://voxel51.com/fiftyone-teams)

[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

## Usage#

Ask your AI assistant:
    
    
    "Export the current view to COCO format"
    "Export my training split as YOLOv5 to my S3 bucket"
    "Export a CSV with filepath, tags, and metadata fields"
    "Export only the media files for my validation set"
    

The assistant reads your active view and schema, confirms the format and destination, and runs the export as a background job. Use the **Export** button in the top-right of the FiftyOne App â **Direct download** tab to download the result to your browser.

## See also#

[Exporting Datasets](https://docs.voxel51.com/user_guide/export_datasets.html)

[FiftyOne Enterprise](https://docs.voxel51.com/teams/index.html)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
