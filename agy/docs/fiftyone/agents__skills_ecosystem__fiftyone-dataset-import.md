---
source_url: https://docs.voxel51.com/agents/skills_ecosystem/fiftyone-dataset-import.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-skills/blob/main/skills/fiftyone-dataset-import/SKILL.md)

# Dataset Import#

Import any dataset into FiftyOne with automatic format detection. Supports local files, Hugging Face Hub, cloud storage, and multimodal grouped data.

## Install#
    
    
    curl -sL skil.sh | sh -s -- voxel51/fiftyone-skills
    

When prompted, select **fiftyone-dataset-import** from the menu.

## Requirements#

  * [FiftyOne](https://docs.voxel51.com/getting_started/install.html)

  * [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server) (optional, recommended for App control)




## Usage#

Start the MCP server and ask your AI assistant:
    
    
    "Import the COCO dataset from /path/to/data"
    "Load the keremberke/license-plate-object-detection dataset from Hugging Face"
    "Import this folder of images, there are cameras and LiDAR files grouped by scene"
    

The skill scans your data, auto-detects the format and media types, and loads the dataset into FiftyOne. It handles images, videos, point clouds, COCO, YOLO, VOC, KITTI, and more without you specifying the format.

## Example#
    
    
    # Download sample COCO data to ~/fiftyone/coco-2017/validation
    fiftyone zoo datasets download coco-2017 --split validation
    

Then ask your assistant:
    
    
    "Import the COCO 2017 validation dataset from ~/fiftyone/coco-2017/validation and name it coco-2017-validation"
    

After the skill runs, verify in Python:
    
    
    import fiftyone as fo
    dataset = fo.load_dataset("coco-2017-validation")
    print(dataset)
    

Or ask your assistant to open it in the App:
    
    
    "Launch the FiftyOne App with the coco-2017-validation dataset"
    

## See also#

  * [Dataset Import docs](https://docs.voxel51.com/user_guide/dataset_creation/index.html)

  * [Hugging Face Hub integration](https://docs.voxel51.com/integrations/huggingface.html)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
