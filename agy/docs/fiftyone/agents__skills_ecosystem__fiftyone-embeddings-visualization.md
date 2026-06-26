---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-embeddings-visualization.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-skills/blob/main/skills/fiftyone-embeddings-visualization/SKILL.md)

# Embeddings Visualization#

Visualize your dataset in 2D using UMAP or t-SNE to explore structure, find clusters, and identify outliers.

## Install#
    
    
    curl -sL skil.sh | sh -s -- voxel51/fiftyone-skills
    

When prompted, select **fiftyone-embeddings-visualization** from the menu.

## Requirements#

  * [FiftyOne](https://docs.voxel51.com/getting_started/install.html)

  * [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)

  * [`@voxel51/brain`](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/brain) plugin




## Usage#

Load a dataset in FiftyOne, then ask your AI assistant:
    
    
    "Visualize my dataset embeddings with UMAP"
    "Compute CLIP embeddings and show the 2D projection"
    "Color the embedding plot by class label and find outliers"
    

The skill computes embeddings if they donât exist, reduces them to 2D, and opens the Embeddings panel in the FiftyOne App.

## Example#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    

Then ask your assistant:
    
    
    "Compute CLIP embeddings for quickstart and show a UMAP visualization"
    

## See also#

  * [Embeddings visualization docs](https://docs.voxel51.com/brain.html#visualizing-embeddings)

  * [FiftyOne Brain](https://github.com/voxel51/fiftyone-brain)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
