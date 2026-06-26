---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/moondream3.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/moondream3)

# Moondream3 FiftyOne Zoo Model#

![Moondream3 Demo](https://raw.githubusercontent.com/harpreetsahota204/moondream3/main/md3_hd.gif)

A [FiftyOne](https://github.com/voxel51/fiftyone) remote source zoo model implementation for [Moondream 3 (Preview)](https://huggingface.co/moondream/moondream3-preview), a state-of-the-art vision language model with a mixture-of-experts architecture (9B total parameters, 2B active).

## About Moondream3#

Moondream 3 is a frontier-level visual reasoning model that delivers exceptional performance while maintaining blazingly fast inference speeds. It features:

  * **9B MoE architecture** with only 2B active parameters

  * **32K context length** for complex queries and structured outputs

  * **Native grounding skills** including object detection and pointing

  * **Superior OCR capabilities** for text extraction

  * **Frontier-level visual reasoning** that matches or beats much larger models




### Key Capabilities#

  * **Object Detection** : Astonishingly good at detecting objects with complex queries

  * **Pointing** : Native support for identifying specific points in images

  * **Structured Output** : Intelligent JSON/structured outputs with minimal prompting

  * **OCR** : Drastically improved text recognition and extraction

  * **Visual Q &A**: Answer complex questions about images with reasoning capabilities

  * **Zero-shot Classification** : Classify images without training

  * **Image Captioning** : Generate short, normal, or long descriptions




## Installation#

### Prerequisites#

  1. **Request Model Access** : This is a gated model. You need to:

     * Request access at [Hugging Face](https://huggingface.co/moondream/moondream3-preview)

     * Authenticate with your HuggingFace token:
    
    hf auth login
    

  2. **Install FiftyOne** :
         
         pip install fiftyone
         

  3. **Install Dependencies** :
         
         pip install transformers torch torchvision huggingface-hub
         




### Setting up the Zoo Model#

  1. Register the zoo model source:



    
    
    import fiftyone.zoo as foz
    
    foz.register_zoo_model_source(
        "https://github.com/harpreetsahota204/moondream3", 
        overwrite=True
    )
    

  2. Download the model:



    
    
    foz.download_zoo_model(
        "https://github.com/harpreetsahota204/moondream3",
        model_name="moondream/moondream3-preview"
    )
    

  3. Load the model:



    
    
    model = foz.load_zoo_model("moondream/moondream3-preview")
    

## Usage Examples#

### Quick Start#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.huggingface as fouh
    
    dataset = fouh.load_from_hub(
        "Voxel51/GQA-Scene-Graph",
        max_samples=50,
        overwrite=True
        )
    
    #adding a list of objects which are present in the image
    sample_objects = dataset.values("detections.detections.label")
    
    sample_level_objects =  [list(set(obj)) for obj in sample_objects]
    
    dataset.set_values("sample_level_objects", sample_level_objects)
    # Load Moondream3
    model = foz.load_zoo_model("moondream/moondream3-preview")
    
    # Apply different operations
    model.operation = "caption"
    dataset.apply_model(model, label_field="md_captions")
    

### Image Captioning#

Generate captions of varying lengths:
    
    
    # Short captions
    model.operation = "caption"
    model.length = "short"
    dataset.apply_model(model, label_field="md_short_captions")
    
    # Long detailed captions
    model.length = "long"
    dataset.apply_model(model, label_field="md_long_captions")
    

### Object Detection#

Detect specific objects in images:
    
    
    model.operation = "detect"
    
    # Detect from a list of objects
    model.prompt = ["car", "person", "traffic light"]
    dataset.apply_model(model, label_field="md_detections_list")
    
    # Or detect objects from a field in your dataset
    dataset.apply_model(
        model, 
        prompt_field="sample_level_objects",
        label_field="md_detections"
    )
    

### Pointing (Keypoints)#

Identify specific points for objects:
    
    
    model.operation = "point"
    # model.prompt = ["horse", "saddle", "rider"] #you can pass a list or use a prompt field
    dataset.apply_model(model, prompt_field="sample_level_objects", label_field="md_keypoints")
    

### Visual Question Answering#

Ask questions about images:
    
    
    model.operation = "query"
    model.prompt = "What is happening in this image?"
    dataset.apply_model(model, label_field="md_vqa_response")
    
    # Or use questions from dataset fields
    dataset.apply_model(
        model,
        prompt_field="questions",
        label_field="answers"
    )
    

### Zero-shot Classification#

Classify images without training:
    
    
    model.operation = "classify"
    model.prompt = "dog, cat, bird, fish" # or you can pass a list ["dog", "cat", "bird", "fish"]
    dataset.apply_model(model, label_field="classification")
    

### Phrase Grounding (Hack)#

While not natively supported, you can achieve phrase grounding by using captions as prompts for detection:
    
    
    # First generate captions
    model.operation = "caption"
    dataset.apply_model(model, label_field="md_captions")
    
    # Then use captions for detection
    model.operation = "detect"
    dataset.apply_model(
        model, 
        prompt_field="md_captions",
        label_field="grounded_detections"
    )
    

## Supported Operations#

Operation | Description | Parameters  
---|---|---  
`caption` | Generate image descriptions | `length`: âshortâ, ânormalâ, âlongâ  
`detect` | Object detection with bounding boxes | `prompt`: objects to detect (list or string)  
`point` | Identify keypoints for objects | `prompt`: objects to find (list or string)  
`query` | Visual question answering | `prompt`: question about the image  
`classify` | Zero-shot classification | `prompt`: comma-separated class options  
  
## Architecture Details#

Moondream3 features:

  * 24 layers (first 4 dense, remainder with MoE FFNs)

  * 64 experts with 8 activated per token

  * GeGLU architecture with 2048 hidden dimension

  * Custom efficient SuperBPE tokenizer

  * SigLIP-based vision encoder with multi-crop processing

  * Multi-headed attention with learned temperature scaling




## Performance#

Moondream3 achieves frontier-level performance on visual reasoning benchmarks while maintaining 2B active parameters, making it:

  * **Fast** : Blazingly fast inference compared to larger models

  * **Inexpensive** : Cheap to run at scale

  * **Trainable** : Easily fine-tunable for specialized tasks

  * **Practical** : Suitable for real-world deployment




## License#

The model weights are licensed under the [Business Source License 1.1 with an Additional Use Grant (No Third-Party Service)](https://huggingface.co/moondream/moondream3-preview/blob/main/LICENSE.md).

**You can:**

  * Use for personal projects

  * Self-host inside your company (commercial use OK)




**You need a license for:**

  * Offering as an external API

  * Managed hosting for customers




For commercial licensing inquiries: contact@m87.ai

## Resources#

  * [Model on Hugging Face](https://huggingface.co/moondream/moondream3-preview)

  * [Interactive Playground](https://moondream.ai/c/playground)

  * [Cloud API](https://moondream.ai/c/docs/quickstart)

  * [Release Blog Post](https://moondream.ai/blog/moondream-3-preview)

  * [FiftyOne Documentation](https://docs.voxel51.com/)




## Example Notebook#

Check out the included Jupyter notebook `using_moondream3_zoo_model.ipynb` for comprehensive examples of all operations.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/harpreetsahota204/moondream3/blob/main/using_moondream3_zoo_model.ipynb)

## Contributing#

Contributions are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments#

  * [Moondream AI](https://moondream.ai/) for creating this amazing model

  * [Voxel51](https://voxel51.com/) for the FiftyOne framework

  * The open-source community




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
