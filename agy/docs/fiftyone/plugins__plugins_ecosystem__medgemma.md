---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/medgemma.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/medgemma)

# Implementing MedGemma as a Remote Zoo Model for FiftyOne#

This repository integrates Googleâs MedGemma models with FiftyOne, allowing you to easily use these powerful medical AI models for analyzing and classifying medical images in your FiftyOne datasets.

# â¹ Important! Be sure to request access to the model!#

This is a gated model, so you will need to fill out the form on the model card: https://huggingface.co/google/medgemma-4b-it

Approval should be instantaneous.

Youâll also have to set your Hugging Face in your enviornment:
    
    
    export HF_TOKEN="your_token"
    

Or sign-in to Hugging Face via the CLI:
    
    
    huggingface-cli login
    

## What is MedGemma?#

MedGemma is a collection of Gemma 3 variants that are trained specifically for medical text and image comprehension. These models excel at understanding various medical imaging modalities including:

  * Chest X-rays

  * Dermatology images

  * Ophthalmology images

  * Histopathology slides




This integration is for **MedGemma 4B** , a multimodal version that can process both images and text

## Installation#

First, ensure you have FiftyOne installed:
    
    
    pip install fiftyone
    

Then register this repository as a custom model source:
    
    
    import fiftyone.zoo as foz
    foz.register_zoo_model_source("https://github.com/harpreetsahota204/medgemma", overwrite=True)
    

## Usage#

### Download and Load the Model#
    
    
    import fiftyone.zoo as foz
    
    # Download the model (only needed once)
    foz.download_zoo_model(
        "https://github.com/harpreetsahota204/medgemma",
        model_name="google/medgemma-4b-it", 
    )
    
    # Load the model
    model = foz.load_zoo_model(
        "google/medgemma-4b-it"
    )
    

### Setting the Operation Mode#

The model supports two main operations:
    
    
    # For medical image classification
    model.operation = "classify"
    
    # For visual question answering on medical images
    model.operation = "vqa"
    

### Classification Example#
    
    
    import fiftyone as fo
    
    
    from fiftyone.utils.huggingface import load_from_hub
    
    dataset = load_from_hub(
        "Voxel51/MedXpertQA",
        name="MedXpertQA",
        max_samples=10,
        overwrite=True
        )
    
    # Set classification parameters
    model.operation = "classify"
    model.prompt = "What medical conditions are visible in this image?"
    
    # Run classification on the dataset
    dataset.apply_model(model, label_field="medgemma_classifications")
    
    

### Visual Question Answering Example#
    
    
    # Set VQA parameters
    model.operation = "vqa"
    model.prompt = "Is there evidence of pneumonia in this chest X-ray? Explain your reasoning."
    
    # Apply to dataset
    dataset.apply_model(model, label_field="pneumonia_assessment")
    
    

### Custom System Prompts#

You can customize the system prompt to better suit your specific needs:
    
    
    model.system_prompt = """You are an expert dermatologist specializing in skin cancer detection.
    Analyze the provided skin lesion image and determine if there are signs of malignancy.
    Provide your assessment in JSON format with detailed observations."""
    

## Performance Considerations#

  * For optimal performance, a CUDA-capable GPU is recommended

  * The model supports quantization to reduce memory requirements:
        
        model = foz.load_zoo_model(
            "google/medgemma-4b-it",
            quantized=True  # Enable 4-bit quantization
        )
        




# â Example notebook#

You can refer to the example notebook to get hands on.

## License#

MedGemma is governed by the [Health AI Developer Foundations terms of use](https://developers.google.com/health-ai-developer-foundations/terms).

This integration is licensed under the Apache 2.0 License.

## Notes#

  * This integration is designed for research and development purposes

  * Always validate model outputs in clinical contexts

  * Review the [MedGemma documentation](https://developers.google.com/health-ai-developer-foundations/medgemma) for detailed information about the modelâs capabilities and limitations




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
