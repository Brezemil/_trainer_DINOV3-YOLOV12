---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/mashupvqa.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/MashUpVQA)

# Dataset Card for MashUpVQA#

![image/png](https://huggingface.co/datasets/Voxel51/MashUpVQA/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 12780 samples.

MashUpVQA is a remix of several visual question answering dataets. Our hope is that a dataset with a consistent format and lots of variety will make it easier the assess the performance of a VQA system.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/MashUpVQA")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

MashUpVQA was curated by

  * **Curated by:** [Harpreet Sahota, Hacker-in-Residence](https://huggingface.co/harpreetsahota) at [Voxel 51](https://huggingface.co/Voxel51)

  * **Language(s) (NLP):** en

  * **License:** MashUpVQA is a composite dataset created by combining multiple individual datasets. Each of these datasets may be subject to its own terms of use and licensing. The licensing terms of depend on the licensing terms of each individual dataset included in this compilation. As we have integrated data from various sources, we do not hold copyright over the data and acknowledge that each source retains rights over their respective data. Users of MashUpVQA are responsible for ensuring that their use of the data complies with the legal and licensing requirements of each individual dataset included. **Please ensure that you review and adhere to the licensing requirements of each individual dataset prior to using this data.**




## Dataset Structure#

Each sample in the dataset comprises:

  * An image

  * A question to be asked of the image

  * An answer




### Dataset Sources#

#### Code for creating the dataset can be found in this [notebook](https://colab.research.google.com/drive/1jexIg5-o4fPJsseuYQoPLpWaeWWnItpy?usp=sharing).#

The MashupVQA dataset is a composite dataset designed for vibe-checking and evaluating Visual Question Answering (VQA) systems, where models attempt to answer questions based on visual input. This dataset integrates multiple diverse datasets to cover a wide range of challenges in VQA, promoting robustness and versatility in developed models.

Hereâs a summary of the constituent datasets:

  1. **TextVQA** : Focuses on answering questions that require reading text within images, sourced from Open Images. The questions necessitate models to not only detect and read text but also reason about its relevance to the query. [TextVQA on LMMs Lab](https://huggingface.co/datasets/lmms-lab/textvqa).

  2. **WildVision** : Contains a collection of public benchmarks for evaluating multimodal large language models, useful for general multimodal understanding tasks. [WildVision Dataset](https://huggingface.co/datasets/WildVision/PublicBenchHub/tree/main).

  3. **RealWorldQA** : Tests models on real-world visuals like vehicle camera images, focusing on practical, verifiable question-answer pairs. [RealWorldQA Dataset](https://huggingface.co/datasets/xai-org/RealworldQA).

  4. **AI2 Diagrams (AI2D)** : Offers a challenge in understanding scientific diagrams, with over 5,000 annotated diagrams from grade school textbooks. [AI2D on LMMs Lab](https://huggingface.co/datasets/lmms-lab/ai2d).

  5. **DocVQA** : Focuses on document images spanning a century, with questions about their content, challenging models to handle various types of printed and handwritten text. [DocVQA on LMMs Lab](https://huggingface.co/datasets/lmms-lab/DocVQA).

  6. **InfographicVQA** : Involves answering questions from infographic images, requiring reasoning over text, layout, and graphical elements. [InfographicVQA on LMMs Lab](https://huggingface.co/datasets/lmms-lab/DocVQA).

  7. **MME** : A benchmark for evaluating multimodal large language models across diverse tasks like OCR, commonsense reasoning, and numerical calculations. [MME on LMMs Lab](https://huggingface.co/datasets/lmms-lab/MME).

  8. **VisualWebBench** : Tests understanding of web page content across multiple levels, from whole page comprehension to specific element interactions. [VisualWebBench Repo](https://github.com/VisualWebBench/VisualWebBench).

  9. **OCR-VQA** : Dedicated to answering questions based on text identified in images, specifically book covers. [OCR-VQA on Hugging Face](https://huggingface.co/datasets/howard-hou/OCR-VQA).

  10. **Localized Narratives** : Provides rich annotations linking spoken descriptions to visual content through mouse traces, enhancing modelsâ ability to connect visual and textual information. [Localized Narratives on Hugging Face](https://huggingface.co/datasets/vikhyatk/lnqa).

  11. **VQA-RAD** : Specializes in medical VQA with radiology images, where questions and answers are generated by clinicians, focusing on medically relevant visual content. [VQA-RAD on Hugging Face](https://huggingface.co/datasets/flaviagiammarino/vqa-rad).




#### Data Collection and Processing#

This [notebook](https://colab.research.google.com/drive/1jexIg5-o4fPJsseuYQoPLpWaeWWnItpy?usp=sharing) demonstrates the process of creating a mashup dataset called âMashUpVQAâ by combining and preprocessing three datasets: TextVQA, WildVision, and VQAv2. The goal is to create a consistent and consolidated dataset for multimodal question-answering tasks.

### Dataset Loading and Preprocessing#

  1. Each dataset is loaded from the Hugging Face hub using the `load_from_hub` function of `fiftyone`.

  2. Smaller subsets of the datasets are created using the `take` and `clone` methods to reduce the dataset size for easier processing.

  3. The datasets undergo a common preprocessing pipeline:

  4.      * A âsource_datasetâ field is added to indicate the source Hugging Face repo.

     * Unused fields are deleted based on the dataset configuration.

     * Fields are renamed for consistency across datasets (if needed).




### Answer Consolidation#

  1. A new âanswerâ field is added to each dataset using `add_sample_field` method of the `fo.dataset` object.

  2. The `parse_answer` function is applied to each sampleâs âquestionâ and âanswersâ fields to consolidate the answers into a single, most plausible answer.

  3. The parsed answers are set as the values of the âanswerâ field using `set_values`.

  4. The original âanswersâ field is deleted from each dataset.




The preprocessed datasets are concatenated into a single dataset named and exported to the Hub in the FiftyOne dataset format.

## Dataset Card Authors#

[Harpreet Sahota](https://huggingface.co/harpreetsahota)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
