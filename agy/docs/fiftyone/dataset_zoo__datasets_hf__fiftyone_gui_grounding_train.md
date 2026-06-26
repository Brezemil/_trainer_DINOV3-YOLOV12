---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/fiftyone_gui_grounding_train.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/FiftyOne-GUI-Grounding-Train)

# Dataset Card for FiftyOne GUI Grounding Training Set#

## Dataset Details#

### Dataset Description#

This dataset contains 739 annotated GUI screenshots designed for training computer vision models to understand and interact with graphical user interfaces. The dataset uses the specialized COCO4GUI format, which extends the standard COCO detection format to handle GUI-specific features, interaction sequences, and rich metadata.

The dataset captures real user interface interactions across various applications and platforms, with both bounding box annotations for UI elements and precise keypoint annotations for interaction locations (clicks, taps, etc.).

  * **Curated by:** GUI Dataset Collector Tool

  * **Funded by:** Voxel51

  * **Shared by:** Harpreet Sahota

  * **Language(s):** English (en)

  * **License:** Apache 2.0




### Dataset Sources#

  * **Repository:** [GUI Annotation Tool](https://github.com/harpreetsahota204/gui_annotation_tool)

  * **Paper:** N/A

  * **Using this dataset:** https://github.com/harpreetsahota204/visual_agents_workshop




## Uses#

### Direct Use#

This dataset is designed for:

  * **GUI Element Detection** : Training models to identify and locate UI components in screenshots

  * **Interaction Point Prediction** : Learning to predict where users should click/interact within interfaces

  * **GUI Understanding** : Developing models that can comprehend user interface layouts and functionality

  * **Workflow Sequence Learning** : Understanding sequences of user interactions and task flows

  * **Cross-platform GUI Analysis** : Training on diverse applications and platforms (macOS, various browsers, etc.)




### Out-of-Scope Use#

  * **Privacy-sensitive Applications** : Screenshots may contain application interfaces that could reveal user data

  * **Real-time Automation** : This is a training dataset, not intended for direct deployment in production automation systems

  * **Non-GUI Computer Vision** : Optimized specifically for GUI interactions, not general object detection




## Dataset Structure#

### Data Format#

  * **Images** : 739 PNG screenshots with timestamps (2025-07-22 to 2025-08-08)

  * **Annotations** : COCO4GUI format JSON with extended metadata

  * **Resolution** : Variable (typical: 2992x1866 pixels for macOS screenshots)




### Annotation Categories#

The dataset includes 7 interaction types:

  1. **click** \- Standard mouse clicks

  2. **type** \- Text input actions

  3. **select** \- Selection operations

  4. **hover** \- Mouse hover interactions

  5. **drag** \- Drag and drop operations

  6. **right_click** \- Context menu interactions

  7. **double_click** \- Double-click actions




### Annotation Structure#

Each annotation contains:

  * **Bounding boxes** : Rectangular regions around UI elements

  * **Keypoints** : Precise interaction coordinates (x, y, visibility)

  * **Rich attributes** :

    * `task_description`: Human-readable description of the interaction

    * `action_type`: Type of interaction being performed

    * `element_info`: Information about the UI element

    * `custom_metadata`: Additional context-specific data




### Metadata Fields#

  * **Application** : Source application (Arc Browser, Chrome, etc.)

  * **Platform** : Operating system (primarily macOS)

  * **Date captured** : Timestamp of screenshot capture

  * **Sequence information** : For tracking multi-step workflows

  * **GUI metadata** : Application-specific context




## Dataset Creation#

### Curation Rationale#

This dataset was created to address the need for high-quality, annotated GUI interaction data for training computer vision models that can understand and interact with user interfaces. The focus on both spatial (bounding boxes) and precise (keypoints) annotations enables training of models that can both identify UI elements and predict exact interaction points.

### Source Data#

#### Data Collection and Processing#

Data was collected using a specialized GUI annotation tool that:

  * **Captures live screenshots** of various applications and interfaces

  * **Provides real-time annotation capabilities** with bounding boxes and click points

  * **Maintains rich metadata** about applications, platforms, and interaction context

  * **Supports sequence tracking** for multi-step user workflows

  * **Exports in COCO4GUI format** optimized for FiftyOne integration




Screenshots span from July 22, 2025 to August 8, 2025, capturing diverse GUI states and interactions primarily on macOS systems using various browsers and applications.

#### Who are the source data producers?#

Screenshots were captured from real application interfaces during normal usage, with manual annotation of interaction points and UI elements using the GUI Dataset Collector tool.

### Annotations#

#### Annotation process#

Annotations were created using a specialized web-based GUI annotation tool that provides:

  * **Interactive bounding box drawing** for UI element regions

  * **Precise click point placement** for interaction coordinates

  * **Rich metadata entry** for task descriptions and element information

  * **Real-time preview** and editing capabilities

  * **Sequence tracking** for multi-step workflows




The tool automatically captures metadata like application name, platform, and timestamps while allowing annotators to add detailed descriptions of interactions and UI elements.

#### Who are the annotators?#

Annotations were created by the dataset curator using the GUI annotation tool during real interface interactions.

### Personal and Sensitive Information#

Screenshots may contain application interfaces that could potentially reveal:

  * **Application usage patterns**

  * **Interface layouts and designs**

  * **Partial text content** from applications




Care should be taken when using this dataset to ensure compliance with privacy requirements. The dataset focuses on interaction patterns rather than content, but users should review samples for any sensitive information relevant to their use case.

## Bias, Risks, and Limitations#

### Technical Limitations#

  * **Platform bias** : Primarily macOS screenshots, limiting cross-platform generalization

  * **Application bias** : Heavy focus on browser interfaces and specific applications

  * **Resolution consistency** : Variable screenshot resolutions may affect model training

  * **Temporal scope** : Data collected over a limited time period (July-August 2025)




### Potential Biases#

  * **Interface design bias** : Reflects specific application UI paradigms and design patterns

  * **Interaction pattern bias** : May not represent all user interaction styles or accessibility needs

  * **Language bias** : Primarily English-language interfaces




### Risks#

  * **Privacy concerns** : Screenshots may inadvertently contain sensitive interface elements

  * **Overfitting risk** : Limited diversity in applications and platforms

  * **Generalization challenges** : Models trained on this data may not generalize well to significantly different GUI paradigms




### Recommendations#

Users should:

  * **Augment with additional data** from diverse platforms and applications

  * **Validate on target use cases** before deployment

  * **Consider privacy implications** when using in production systems

  * **Test cross-platform performance** if deploying across different operating systems

  * **Implement proper data handling** procedures for any sensitive content




## Technical Details#

### FiftyOne Integration#

This dataset includes advanced FiftyOne features:

  * **Brain embeddings** : CLIP and image similarity indices computed

  * **Visualization** : UMAP embeddings for data exploration

  * **Uniqueness scoring** : Identifies diverse vs. redundant samples

  * **Representativeness metrics** : Helps identify core vs. outlier samples




### Enhanced Metadata#

The COCO4GUI format provides:

  * **Sequence tracking** : Links related interaction steps

  * **Rich attributes** : Detailed interaction context

  * **GUI-specific fields** : Application, platform, timing metadata

  * **Workflow information** : Multi-step task sequences




## Citation#

**BibTeX:**
    
    
    @dataset{fiftyone_gui_grounding_2025,
      title={FiftyOne GUI Grounding Training Set},
      author={Sahota, Harpreet},
      year={2025},
      publisher={Hugging Face},
      url={https://huggingface.co/datasets/harpreetsahota/FiftyOne-GUI-Grounding-Train}
    }
    

**APA:** Sahota, H. (2025). FiftyOne GUI Grounding Training Set [Dataset]. Hugging Face. https://huggingface.co/datasets/harpreetsahota/FiftyOne-GUI-Grounding-Train

## Dataset Card Authors#

Harpreet Sahota

## Dataset Card Contact#

For questions about this dataset, please contact the dataset author through the Hugging Face dataset repository.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
