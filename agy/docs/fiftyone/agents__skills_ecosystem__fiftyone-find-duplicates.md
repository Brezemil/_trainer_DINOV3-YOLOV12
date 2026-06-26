---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-find-duplicates.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-skills/blob/main/skills/fiftyone-find-duplicates/SKILL.md)

# Find Duplicates#

Find and remove duplicate or near-duplicate images from a FiftyOne dataset using brain similarity.

## Install#
    
    
    curl -sL skil.sh | sh -s -- voxel51/fiftyone-skills
    

When prompted, select **fiftyone-find-duplicates** from the menu.

## Requirements#

  * [FiftyOne](https://docs.voxel51.com/getting_started/install.html)

  * [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

  * [`@voxel51/brain`](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/brain) plugin




## Usage#

Load a dataset in FiftyOne, then ask your AI assistant:
    
    
    "Find duplicate images in my dataset"
    "Remove near-duplicates and keep only unique samples"
    "Show me which images are visually similar"
    

The skill computes similarity embeddings, identifies duplicates above a configurable threshold, and lets you review them in the App before deleting.

## Example#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    

Then ask your assistant:
    
    
    "Find near-duplicate images in the quickstart dataset"
    

## See also#

  * [Deduplication docs](https://docs.voxel51.com/brain.html#brain-similarity)

  * [FiftyOne Brain](https://github.com/voxel51/fiftyone-brain)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
