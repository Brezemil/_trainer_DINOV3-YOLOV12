---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/sample_inspector.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/allenleetc/sample-inspector)

# Sample Inspector Plugin#

A [FiftyOne](https://github.com/voxel51/fiftyone) panel plugin that displays selected samples in a detail view with segmentation mask overlays, image adjustment controls, and class filtering.

Select one or more samples in the grid and the panel renders them with interactive controls for inspecting segmentation masks (both semantic and instance).

![Screenshot](https://raw.githubusercontent.com/allenleetc/sample-inspector/main/assets/usage.gif)

## Installation#
    
    
    fiftyone plugins download https://github.com/allenleetc/sample-inspector
    

## Features#

  * **Multi-sample grid** â select multiple samples and view them side by side

  * **Semantic segmentation overlays** â renders `mask_path` fields with color-coded class overlays

  * **Instance segmentation overlays** â renders `Detections` with per-instance mask overlays positioned at bounding boxes

  * **Brightness / Contrast** â adjustable sliders (0-200%)

  * **Overlay opacity** â control mask transparency (0-100%)

  * **Class filtering** â toggle individual classes on/off with chip selectors




## Operators#

### `get_mask_targets`#

An unlisted Python operator that fetches `mask_targets` and `default_mask_targets` from the dataset. Called internally by the panel to map pixel values to class labels for semantic segmentation overlays.

## Usage#

  1. Open the FiftyOne App and load a dataset with segmentation labels

  2. Open the **Sample Inspector** panel from the panels menu

  3. Select one or more samples in the grid

  4. Use the sliders to adjust brightness, contrast, and overlay opacity

  5. Use the class filter chips to toggle specific classes on/off




## Development#

Requires a local clone of the [FiftyOne](https://github.com/voxel51/fiftyone) repository and `FIFTYONE_DIR` set to its root.
    
    
    yarn install
    yarn build
    

See [FiftyOne JS Plugin Build Utils](https://github.com/voxel51/fiftyone-js-plugin-build) for build configuration details.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
