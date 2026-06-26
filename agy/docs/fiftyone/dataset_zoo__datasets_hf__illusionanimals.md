---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/illusionanimals.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/IllusionAnimals)

# Dataset Card for illusion_animals#

![image/png](https://huggingface.co/datasets/Voxel51/IllusionAnimals/resolve/main/illusion_animals_initial_explore.gif)

The core challenge presented in the [Illusory VQA](https://github.com/IllusoryVQA/IllusoryVQA) task is deceptively complex: given an image containing both a âReal Conceptâ (RC) and potentially an âIllusory Conceptâ (IC), can a VLM detect if an illusion is present and correctly answer questions about that illusory element?

This task requires perception beyond standard image recognition and assessing how well models can mimic human-like visual understanding, and is interestingly challenging because the model must simultaneously recognize whatâs actually in the image while also perceiving what appears to be there due to the illusion â much like our own visual system does.

## The Illusory Datasets#

For this task, the authors created four benchmark datasets, each targeting different aspects of visual illusion processing:

â¢ **IllusionMNIST:** Built using the classic MNIST handwritten digit dataset as the source material, this dataset contains 3,960 training samples and 1,219 test samples. The researchers added a âNo illusionâ class to make the task more challenging, requiring models to determine whether an illusion is actually present.

â¢ **IllusionFashionMNIST:** Based on the Fashion-MNIST dataset, which contains clothing items rather than digits, this collection includes 3,300 training samples and 1,267 test samples. Like its MNIST counterpart, it includes a âNo illusionâ class to further test discrimination abilities.

â¢ **IllusionAnimals:** This dataset features animal images generated using SDXL-Lightning and transformed with ControlNet to create illusory versions. It comprises 3,300 training samples and 1,100 test samples, with the additional âNo illusionâ class.

â¢ **IllusionChar:** This unique dataset focuses specifically on reading characters in images, with sequences of 3 to 5 characters per image. Including 9,900 training samples and 3,300 test samples, it tests how well models can interpret text within illusory contexts.

### This dataset is the IllusionAnimals subset#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/IllusionAnimals")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

Dataset Description

  * Curated by: Researchers from IUST (Iran University of Science and Technology)

  * GitHubRepo: https://github.com/IllusoryVQA/IllusoryVQA

  * Shared by: [Harpreet Sahota](https://huggingface.co/harpreetsahota), Hacker-in-Residence, Voxel5

  * Paper: https://arxiv.org/abs/2412.08169

  * Language(s): English

  * License: [MIT License](https://github.com/IllusoryVQA/IllusoryVQA?tab=MIT-1-ov-file#readme)




## Uses#

### Direct Use#

  * Benchmarking multimodal modelsâ ability to detect and interpret visual illusions

  * Training and evaluating visual question answering systems

  * Testing model robustness in illusion detection

  * Comparing human vs. machine perception of visual illusions




### Out-of-Scope Use#

  * The dataset should not be used for creating deceptive or misleading content

  * Should not be used for applications that could cause harm through visual manipulation




### Dataset Structure#

  * Training set: 3,300 samples

  * Test set: 1,100 samples

  * 10 classes: cat, dog, pigeon, butterfly, elephant, horse, deer, snake, fish, and rooster

  * Also includes a âNo illusionâ class

  * Image resolution: 512x512 pixels




## Dataset Creation#

Created to evaluate how well multimodal models can identify and interpret visual illusions compared to human perception, specifically focusing on animal-based illusions.

## Source Data#

### Data Collection and Processing#

  1. Base images created using SDXL-Lightning

  2. Descriptions generated using various LLMs (ChatGPT, Gemini, Mixtral-8x7B-Instruct-v0.1, Gemma-1.1-7b-it)

  3. Images transformed into illusions using ControlNet

  4. NSFW content filtered out using detector models

  5. Human validation performed on 10% random sample




### Who are the source data producers?#

  * Base images: SDXL-Lightning model

  * Descriptions: Multiple LLMs

  * Illusion transformations: ControlNet model

  * Validation: Human annotators




## Annotations#

### Annotation process#

  * Human evaluators reviewed 10% of samples

  * Annotators asked to identify classes and confirm perception of illusions

  * Three individuals participated in evaluation for this dataset




### Who are the annotators?#

Three human annotators (as described in the paper):

  * Ages: 22-24

  * Gender mix: Both male and female participants




## Personal and Sensitive Information#

  * Dataset was filtered to remove potentially offensive content

  * NSFW detector models were used to screen images

  * No personal information included in the dataset




## Bias, Risks, and Limitations#

  * Limited to single large objects in images

  * May not represent all types of visual illusions

  * Potential biases in the AI-generated base images

  * Challenge in assessing color changes due to illusions

  * Task difficulty may be reduced due to classification format




## Citation#
    
    
    @misc{rostamkhani2024illusoryvqabenchmarkingenhancing,
          title={Illusory VQA: Benchmarking and Enhancing Multimodal Models on Visual Illusions}, 
          author={Mohammadmostafa Rostamkhani and Baktash Ansari and Hoorieh Sabzevari and Farzan Rahmani and Sauleh Eetemadi},
          year={2024},
          eprint={2412.08169},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2412.08169}, 
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
