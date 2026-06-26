---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/minicpm_v.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/minicpm-v)

# MiniCPM-V Integration for FiftyOne#

![MiniCPM-V Demo](https://raw.githubusercontent.com/harpreetsahota204/minicpm-v/main/minicpm-mq.gif)

Integrate [MiniCPM-V 4.5](https://github.com/OpenBMB/MiniCPM-V), a powerful 8B parameter multimodal language model, as a remote source zoo model in [FiftyOne](https://github.com/voxel51/fiftyone). This integration enables seamless use of MiniCPM-Vâs advanced vision-language capabilities directly within your FiftyOne workflows.

## Features#

MiniCPM-V 4.5 achieves GPT-4V-level performance while being significantly smaller and more efficient:

  * **Multiple Vision Tasks** : Object detection, classification, keypoint detection, OCR, visual question answering, and phrase grounding

  * **High Performance** : Outperforms both proprietary models (GPT-4o, Gemini 2.0 Pro) and larger open-source models (Qwen2.5-VL 72B) on many benchmarks

  * **Strong OCR & Document Understanding**: Handles images up to 1.8M pixels with excellent text recognition

  * **Multilingual Support** : Works with 30+ languages

  * **Local Deployment** : Supports CPU and GPU inference




## Requirements#

  * [FiftyOne](https://github.com/voxel51/fiftyone) installed

  * PyTorch

  * Transformers library

  * Sufficient disk space for model weights (~16GB)




## Quick Start#

### Installation#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # Register the MiniCPM-V model source
    foz.register_zoo_model_source(
        "https://github.com/harpreetsahota204/minicpm-v", 
        overwrite=True
    )
    
    # Load the model (downloads on first use)
    model = foz.load_zoo_model(
        "openbmb/MiniCPM-V-4_5",
        # install_requirements=True  # Uncomment if dependencies are missing
    )
    

### Basic Usage Example#
    
    
    # Load a sample dataset
    dataset = foz.load_zoo_dataset("quickstart", max_samples=10, overwrite=True)
    
    # Prepare object labels for detection
    labels_per_sample = dataset.values("ground_truth.detections.label")
    unique_labels_per_sample = [list(set(labels)) for labels in labels_per_sample]
    dataset.set_values("objects", unique_labels_per_sample)
    

## Supported Operations#

### 1\. Visual Question Answering (VQA)#

Generate natural language descriptions or answers about images.
    
    
    model.operation = "vqa"
    model.prompt = "Describe this image in detail"
    dataset.apply_model(model, label_field="descriptions")
    

### 2\. Object Detection#

Detect and localize objects with bounding boxes.
    
    
    # Using a list of objects to detect
    model.operation = "detect"
    model.prompt = ['person', 'car', 'dog', 'traffic light']
    dataset.apply_model(model, label_field="pred_detections")
    
    # Or using a comma-separated string
    model.prompt = 'person, car, dog, traffic light'
    dataset.apply_model(model, label_field="pred_detections")
    
    # Using a prompt field from the dataset
    model.operation = "detect"
    dataset.apply_model(model, label_field="pf_detections", prompt_field="objects")
    

### 3\. Phrase Grounding#

Locate specific regions described by natural language phrases.
    
    
    model.operation = "phrase_grounding"
    dataset.apply_model(model, label_field="pg_detections", prompt_field="descriptions")
    

### 4\. Image Classification#

Classify images into predefined or open-ended categories.
    
    
    model.operation = "classify"
    model.prompt = "Classify this image into exactly one of the following: indoor, outdoor, people, animals"
    dataset.apply_model(model, label_field="pred_class")
    

### 5\. Keypoint Detection#

Identify key points of interest in images.
    
    
    model.operation = "point"
    model.prompt = "Find all people and objects"
    dataset.apply_model(model, label_field="pred_points")
    

### 6\. Optical Character Recognition (OCR)#

Extract text from images while preserving formatting.
    
    
    model.operation = "ocr"
    model.prompt = "Extract all text from this image"
    dataset.apply_model(model, label_field="extracted_text")
    

## Advanced Configuration#

### Custom System Prompts#

You can customize the system prompt for any operation:
    
    
    model.system_prompt = "You are a specialized assistant for medical image analysis..."
    model.operation = "vqa"
    model.prompt = "Identify any abnormalities in this X-ray"
    

### Device Selection#

The model automatically detects and uses the best available device:

  * CUDA (NVIDIA GPUs)

  * MPS (Apple Silicon)

  * CPU (fallback)




### Model Parameters#

The model supports various configuration options through kwargs:
    
    
    model = foz.load_zoo_model(
        "openbmb/MiniCPM-V-4_5",
        operation="detect",  # Set default operation
        prompt="person, vehicle",  # Set default prompt
        system_prompt="Custom system instructions..."  # Custom system prompt
    )
    

## License Information#

This integration code is licensed under Apache 2.0. However, the MiniCPM-V model weights are subject to the [MiniCPM Model License](https://github.com/OpenBMB/MiniCPM-V/blob/main/MiniCPM%20Model%20License.md).

### Important License Considerations#

**Limited Free Commercial Use:**

Commercial use of the model weights is tightly regulated:

  * **Free use allowed** for:

  * Edge devices not exceeding 5,000 units

  * Applications with under 1 million daily active users

  * **Registration required** via questionnaire with OpenBMB

  * **Restrictions** :

  * Cannot use outputs to enhance other models

  * Prohibited for harmful, discriminatory, or deceptive purposes

  * No trademark rights or implied affiliation with OpenBMB

  * **Other commercial use** requires explicit authorization from OpenBMB




Aspect | License Terms  
---|---  
**Commercial Use** | Severely limited unless under strict thresholds and registration  
**Derivatives** | Cannot use MiniCPM outputs to enhance other models  
**Use Cases** | Broadly prohibits harmful, discriminatory, or deceptive usage  
**Branding** | No rights to use OpenBMBâs trademarks or imply affiliation  
**Liability** | Full âas-isâ provision; user bears all risk  
  
## Resources#

  * [MiniCPM-V GitHub Repository](https://github.com/OpenBMB/MiniCPM-V)

  * [MiniCPM-V on Hugging Face](https://huggingface.co/openbmb/MiniCPM-V-4_5)

  * [FiftyOne Documentation](https://docs.voxel51.com/)

  * [FiftyOne Zoo Models](https://docs.voxel51.com/user_guide/model_zoo/index.html)




## Citation#

If you use MiniCPM-V in your research, please cite:
    
    
    @article{yao2024minicpm,
      title={MiniCPM-V: A GPT-4V Level MLLM on Your Phone},
      author={Yao, Yuan and Yu, Tianyu and Zhang, Ao and Wang, Chongyi and Cui, Junbo and Zhu, Hongji and Cai, Tianchi and Li, Haoyu and Zhao, Weilin and He, Zhihui and others},
      journal={arXiv preprint arXiv:2408.01800},
      year={2024}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
