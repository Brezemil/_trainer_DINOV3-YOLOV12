---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/fiftyone_gui_grounding_train_with_synthetic.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/FiftyOne-GUI-Grounding-Train-with-Synthetic)

# Dataset Card for FiftyOne GUI Grounding Training Set with Synthetic Augmentation#

## Dataset Details#

### Dataset Description#

This dataset represents a significant expansion of the original FiftyOne GUI Grounding Training Set, growing from 739 real GUI screenshots to 4,036 total samples through systematic synthetic data generation. The dataset combines authentic GUI interactions with carefully crafted synthetic variants designed to improve model robustness, accessibility awareness, and cross-platform performance.

The synthetic samples were generated using the specialized [Synthetic GUI Samples Plugin for FiftyOne](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins), which applies computer vision transformations while preserving annotation accuracy and spatial relationships.

  * **Curated by:** Harpreet Sahota

  * **Funded by:** Voxel51

  * **Shared by:** Harpreet Sahota

  * **Language(s):** English (en)

  * **License:** Apache-2.0




### Dataset Sources#

  * **Original Repository:** [GUI Annotation Tool](https://github.com/harpreetsahota204/gui_annotation_tool)

  * **COCO4GUI FiftyOne Integration:** [COCO4GUI FiftyOne](https://github.com/harpreetsahota204/coco4gui_fiftyone)

  * **Synthetic Generation Plugin:** [Synthetic GUI Samples Plugin](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins)

  * **Generation Notebook:** [Using Synthetic GUI Samples Plugin via SDK](https://github.com/harpreetsahota204/visual_agents_workshop/blob/main/session_2/Using_Synthetic_GUI_Samples_Plugin_via_SDK.ipynb)




## Loading into FiftyOne#

### Quick Start with Hugging Face Hub#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the augmented dataset directly from Hugging Face Hub
    dataset = load_from_hub("Voxel51/FiftyOne-GUI-Grounding-Train-with-Synthetic")
    
    # Launch the FiftyOne App
    session = fo.launch_app(dataset)
    

### Loading with COCO4GUI Dataset Type#

For enhanced metadata and provenance tracking:
    
    
    import fiftyone as fo
    from coco4gui import COCO4GUIDataset
    
    # Load with full COCO4GUI features including synthetic provenance
    dataset = fo.Dataset.from_dir(
        dataset_dir="/path/to/your/augmented_gui_dataset",
        dataset_type=COCO4GUIDataset,
        name="gui_dataset_with_synthetic",
        data_path="data",
        labels_path="annotations_coco.json",
        include_sequence_info=True,
        include_gui_metadata=True,
        extra_attrs=True,
        persistent=True,
    )
    
    # Launch FiftyOne app
    session = fo.launch_app(dataset)
    

### Analyzing Synthetic vs Real Samples#
    
    
    from fiftyone import ViewField as F
    
    # Separate real and synthetic samples
    real_samples = dataset.match(~F("transform_record").exists())
    synthetic_samples = dataset.match(F("transform_record").exists())
    
    print(f"Real samples: {len(real_samples)}")
    print(f"Synthetic samples: {len(synthetic_samples)}")
    
    # Analyze transformation types
    transform_types = synthetic_samples.distinct("transform_record.transforms.name")
    print(f"Transformation types: {transform_types}")
    

## Uses#

### Direct Use#

This augmented dataset is designed for:

  * **Robust GUI Element Detection** : Training models that work across diverse visual conditions

  * **Accessibility-Aware AI** : Models that understand GUI accessibility challenges (colorblind simulation)

  * **Multi-Resolution GUI Understanding** : Training on various screen sizes and device types

  * **Visual Robustness Testing** : Models that handle inverted colors, grayscale interfaces, and visual variations

  * **Cross-Platform GUI Analysis** : Enhanced diversity for better generalization

  * **Multilingual GUI Interaction** : With text augmentation variants for global applications




### Enhanced Use Cases#

  * **Accessibility Research** : Study GUI perception across different visual conditions using colorblind simulations

  * **Robustness Evaluation** : Test model performance on visually challenging interfaces

  * **Data Efficiency Studies** : Compare model performance with and without synthetic augmentation

  * **Cross-Device Training** : Prepare models for deployment across different screen resolutions




### Out-of-Scope Use#

  * **Production Deployment Without Validation** : Synthetic data should be validated on real-world scenarios

  * **Privacy-Sensitive Applications** : Original privacy considerations still apply

  * **Real-Time Systems** : Performance characteristics may differ between real and synthetic samples




## Dataset Structure#

### Composition#

  * **Total Samples** : 4,036

  * **Real Samples** : 739 (original dataset)

  * **Synthetic Samples** : 3,297 (generated variants)

  * **Augmentation Ratio** : ~4.5x expansion




### Synthetic Augmentation Types#

Based on the [Synthetic GUI Samples Plugin](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins), the dataset includes:

#### 1\. **Visual Accessibility Augmentations**#

  * **Grayscale Conversion** : 3-channel grayscale variants for testing color-independent recognition

  * **Color Inversion** : High-contrast and dark mode interface variants

  * **Colorblind Simulation** : Six types of color vision deficiency simulation:

    * Deuteranopia (green-blind)

    * Protanopia (red-blind)

    * Tritanopia (blue-blind)

    * Deuteranomaly (green-weak)

    * Protanomaly (red-weak)

    * Tritanomaly (blue-weak)




#### 2\. **Resolution Scaling**#

  * **Multi-Device Variants** : Screenshots scaled to common device resolutions:

    * Mobile/Tablet: 1024Ã768, 1280Ã800

    * Laptop/Desktop: 1366Ã768, 1920Ã1080, 1440Ã900

    * High-End: 2560Ã1440, 3840Ã2160 (4K)

    * Ultrawide: 2560Ã1080, 3440Ã1440




#### 3\. **Text Augmentation** (if applied)#

  * **Task Description Rephrasing** : LLM-generated alternative descriptions

  * **Multilingual Variants** : Translated task descriptions for global applications




### Annotation Preservation#

All synthetic samples maintain:

  * **Spatial Accuracy** : Bounding boxes and keypoints scaled proportionally

  * **Annotation Completeness** : All original attributes and metadata preserved

  * **Provenance Tracking** : Complete transformation history in `transform_record` field




### Enhanced Metadata Schema#
    
    
    # Original fields plus synthetic-specific metadata
    sample.transform_record = {
        "transforms": [{"name": "grayscale", "params": {}}],
        "source_sample_id": "original_sample_id",
        "timestamp": "2025-01-15T10:30:00Z",
        "plugin": "synthetic_gui_samples_plugins"
    }
    
    # Preserved original metadata
    sample.application         # "Chrome", "Arc Browser", etc.
    sample.platform           # "macOS", "Windows", etc.
    sample.date_captured       # Original capture timestamp
    sample.sequence_id         # Workflow sequence information
    

## Dataset Creation#

### Curation Rationale#

The synthetic augmentation was designed to address several key limitations in GUI understanding models:

  1. **Visual Robustness** : Many GUI models fail on visually challenging interfaces (dark mode, high contrast, etc.)

  2. **Accessibility Blindness** : Models often ignore how interfaces appear to users with visual impairments

  3. **Resolution Sensitivity** : Training on single-resolution data leads to poor cross-device performance

  4. **Data Scarcity** : Manual GUI annotation is expensive and time-consuming




### Synthetic Generation Process#

The augmentation process used the [Synthetic GUI Samples Plugin](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins) with the following pipeline:

  1. **Source Data** : 739 manually annotated GUI screenshots

  2. **Transformation Selection** : Systematic application of visual augmentations

  3. **Quality Validation** : Automated verification of annotation accuracy

  4. **Provenance Tracking** : Complete transformation history preservation

  5. **Dataset Integration** : Seamless combination with original samples




### Source Data#

#### Original Data Collection#

  * **Method** : Real GUI screenshots from various applications

  * **Time Period** : July-August 2025

  * **Platform** : Primarily macOS with various browsers and applications

  * **Annotation Process** : Manual annotation using specialized GUI annotation tool




#### Synthetic Data Generation#

  * **Tool** : [Synthetic GUI Samples Plugin for FiftyOne](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins)

  * **Transformations** : Computer vision and accessibility-focused augmentations

  * **Validation** : Automated annotation consistency checks

  * **Quality Control** : Systematic verification of spatial relationships




### Annotations#

#### Original Annotation Process#

  * **Tool** : Specialized web-based GUI annotation tool

  * **Annotators** : Expert annotation by dataset curator

  * **Quality** : Manual verification and consistency checking




#### Synthetic Annotation Handling#

  * **Preservation** : All original annotations automatically preserved

  * **Scaling** : Spatial coordinates proportionally adjusted for resolution changes

  * **Validation** : Automated verification of annotation accuracy post-transformation

  * **Provenance** : Complete transformation history tracked




## Bias, Risks, and Limitations#

### Enhanced Considerations for Synthetic Data#

#### Technical Limitations#

  * **Synthetic Realism** : Generated variants may not capture all real-world visual variations

  * **Transformation Artifacts** : Some augmentations may introduce visual artifacts not present in real interfaces

  * **Limited Diversity** : Synthetic samples are constrained by the diversity of the original dataset

  * **Platform Bias** : Still primarily macOS-based despite augmentation




#### Synthetic-Specific Biases#

  * **Augmentation Bias** : Over-representation of certain visual transformations

  * **Quality Variation** : Synthetic samples may have different quality characteristics than real samples

  * **Edge Case Handling** : Synthetic transformations may not handle all annotation edge cases perfectly




#### Risks and Mitigations#

  * **Overfitting to Synthetic Data** : Models may learn synthetic artifacts rather than real patterns

    * _Mitigation_ : Maintain clear real/synthetic sample identification for balanced training

  * **False Confidence** : Large dataset size may mask underlying diversity limitations

    * _Mitigation_ : Regular validation on held-out real data

  * **Annotation Drift** : Repeated transformations may introduce cumulative annotation errors

    * _Mitigation_ : Direct transformation from original samples only




### Recommendations#

#### For Model Training#

  * **Balanced Sampling** : Use both real and synthetic samples in training

  * **Validation Strategy** : Always validate on real, held-out data

  * **Progressive Training** : Start with real data, gradually introduce synthetic variants

  * **Transformation Awareness** : Consider transformation type as a training signal




#### For Evaluation#

  * **Separate Evaluation** : Test on real and synthetic data separately

  * **Robustness Testing** : Use synthetic variants to test specific robustness aspects

  * **Accessibility Evaluation** : Leverage colorblind simulations for accessibility testing




## Technical Details#

### Synthetic Generation Statistics#

  * **Original Dataset Size** : 739 samples

  * **Augmentation Factor** : ~4.5x

  * **Total Synthetic Samples** : 3,297

  * **Transformation Types** : 5+ different augmentation categories

  * **Quality Validation** : 100% automated annotation verification




### FiftyOne Integration Features#

  * **Advanced Brain Embeddings** : CLIP and image similarity indices for both real and synthetic samples

  * **Provenance Tracking** : Complete transformation history in metadata

  * **Filtering Capabilities** : Easy separation of real vs synthetic samples

  * **Visualization Support** : UMAP embeddings showing real/synthetic sample distribution




### Performance Characteristics#

  * **Storage Efficiency** : Optimized image formats and metadata storage

  * **Loading Speed** : Efficient batch loading with FiftyOne integration

  * **Memory Usage** : Scalable handling of large augmented datasets




## Citation#

**BibTeX:**
    
    
    @dataset{fiftyone_gui_grounding_synthetic_2025,
      title={FiftyOne GUI Grounding Training Set with Synthetic Augmentation},
      author={Sahota, Harpreet},
      year={2025},
      publisher={Hugging Face},
      url={https://huggingface.co/datasets/Voxel51/FiftyOne-GUI-Grounding-Train-with-Synthetic},
      note={Augmented using Synthetic GUI Samples Plugin for FiftyOne}
    }
    
    @software{synthetic_gui_plugin_2025,
      title={Synthetic GUI Samples Plugin for FiftyOne},
      author={Sahota, Harpreet},
      year={2025},
      url={https://github.com/harpreetsahota204/synthetic_gui_samples_plugins},
      license={Apache-2.0}
    }
    

**APA:** Sahota, H. (2025). FiftyOne GUI Grounding Training Set with Synthetic Augmentation [Dataset]. Hugging Face. https://huggingface.co/datasets/harpreetsahota/FiftyOne-GUI-Grounding-Train-with-Synthetic

## Dataset Card Authors#

Harpreet Sahota

## Dataset Card Contact#

For questions about this dataset or the synthetic generation process, please contact the dataset author through:

  * [Hugging Face dataset repository](https://huggingface.co/datasets/harpreetsahota/FiftyOne-GUI-Grounding-Train-with-Synthetic)

  * [Synthetic GUI Samples Plugin repository](https://github.com/harpreetsahota204/synthetic_gui_samples_plugins)

  * [COCO4GUI FiftyOne integration repository](https://github.com/harpreetsahota204/coco4gui_fiftyone)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
