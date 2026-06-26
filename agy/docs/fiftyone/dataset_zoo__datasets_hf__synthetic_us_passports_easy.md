---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/synthetic_us_passports_easy.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy)

# Dataset Card for synthetic_us_passports#

![image/png](https://huggingface.co/datasets/Voxel51/synthetic_us_passports_easy/resolve/main/us_passports_synthetic.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 9750 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/synthetic_us_passports_easy")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

Based on the information youâve provided, hereâs a filled-out dataset card for your FiftyOne dataset:

## Dataset Details#

### Dataset Description#

This is a synthetic dataset of US passport images designed to test Vision Language Models (VLMs) on document understanding tasks. The dataset challenges models with realistic scenarios including tilted documents and high-resolution images where the passport occupies only a small region of interest. Each sample contains a synthetically generated US passport with complete biographical and document information fields.

The dataset is particularly useful for evaluating model robustness in document AI applications where documents may not be perfectly aligned or centered in the frame.

  * **Curated by:** Arnaud Stiegler

  * **Language(s) (NLP):** en

  * **License:** Apache-2.0




### Dataset Sources#

  * **Repository:** https://github.com/arnaudstiegler/synth-doc-AI

  * **Original Dataset:** https://huggingface.co/datasets/arnaudstiegler/synthetic_us_passports_easy




## Uses#

### Direct Use#

This dataset is intended for:

  * Training and evaluating Vision Language Models on document understanding tasks

  * Testing OCR and information extraction systems on passport documents

  * Benchmarking model robustness to document rotation and scale variations

  * Developing document processing pipelines that handle non-ideal capture conditions

  * Research on synthetic data generation for document AI




### Out-of-Scope Use#

This dataset should not be used for:

  * Creating actual fraudulent documents (all data is synthetic)

  * Training systems intended to process real passports without proper authorization

  * Any application that violates privacy laws or document security regulations

  * Production systems without validation on real-world data, as synthetic data may not capture all real-world variations




## Dataset Structure#

The FiftyOne dataset contains 9,750 samples with the following structure:

**Core Fields:**

  * `id`: Unique identifier for each sample

  * `filepath`: Path to the image file

  * `metadata`: Image metadata including dimensions and other properties

  * `created_at`: Timestamp of sample creation

  * `last_modified_at`: Timestamp of last modification




**Document Information Fields:**

  * `nationality`: Nationality field (Classification label)

  * `place_of_birth`: Place of birth (Classification label)

  * `authority`: Issuing authority (Classification label)

  * `sex`: Sex/gender field (Classification label)

  * `type`: Document type

  * `code`: Document code

  * `passport_number`: Passport identification number

  * `surname`: Last name

  * `given_names`: First and middle names

  * `dob`: Date of birth

  * `date_of_issue`: Date the passport was issued

  * `date_of_expiration`: Passport expiration date

  * `endorsements`: Additional endorsements or notes




The original dataset structure includes 12 fields per example:

  * Date_of_Expiration

  * Sex

  * Nationality

  * DOB (Date of Birth)

  * Passport_number

  * Place_of_Birth

  * Type

  * Authority

  * Code

  * Date_of_Issue

  * Surname

  * Given_Names




## Dataset Creation#

### Curation Rationale#

This dataset was created to address the need for robust document understanding systems that can handle real-world challenges such as:

  * **Document rotation** : Passports that are tilted or not perfectly aligned with the camera

  * **Scale variation** : High-resolution images where the document of interest occupies only a small portion of the frame




These challenges are common in practical applications but are often underrepresented in standard document AI benchmarks.

### Source Data#

#### Data Collection and Processing#

The dataset is entirely synthetic, generated using the following workflow:

  1. **Template-based generation** : Start with an empty US passport template

  2. **Field population** : Fill the template with synthetically generated values for all biographical and document fields

  3. **Realistic augmentation** : Paste the completed passport image onto a larger background with random tilt

  4. **Background variation** : Use either real document backgrounds or blank backgrounds to increase diversity




This synthetic approach ensures:

  * Complete ground truth annotations for all fields

  * Controlled variation in document pose and scale

  * No privacy concerns related to real personal information

  * Scalable generation of training data




The generation code is available at: https://github.com/arnaudstiegler/synth-doc-AI

#### Who are the source data producers?#

All data is synthetically generated. No real personal information or actual passport documents were used in the creation of this dataset.

### Annotations#

#### Annotation process#

Annotations are automatically generated as part of the synthetic data creation process. Since all document fields are programmatically populated during generation, ground truth labels are inherently accurate and require no manual annotation.

#### Who are the annotators?#

Not applicable - all annotations are automatically generated during the synthetic data creation process.

#### Personal and Sensitive Information#

This dataset contains **no real personal or sensitive information**. All passport data, including names, dates of birth, passport numbers, and other biographical information, is synthetically generated and does not correspond to any real individuals.

## Bias, Risks, and Limitations#

**Limitations:**

  * **Synthetic data gap** : Models trained solely on this synthetic data may not generalize perfectly to real passport images due to differences in paper texture, printing quality, wear and tear, and other physical characteristics

  * **Limited document types** : Only covers US passports in the âeasyâ configuration

  * **Controlled variations** : While the dataset includes tilt and scale variations, it may not capture all real-world conditions (lighting variations, shadows, reflections, partial occlusions, etc.)

  * **Demographic representation** : The distribution of synthetic names and biographical data may not reflect real-world demographic distributions




**Risks:**

  * Potential misuse for document fraud (though all data is clearly synthetic)

  * Over-reliance on synthetic data without real-world validation




### Recommendations#

Users should be made aware of the following:

  * This dataset is best used as a supplement to real-world data, not as a complete replacement

  * Models should be validated on real passport images before deployment in production systems

  * The synthetic nature of the data should be clearly communicated in any downstream applications

  * Additional augmentation and real-world testing are recommended for robust system development

  * This dataset should only be used for legitimate research and development purposes in document AI




## Citation#

**BibTeX:**
    
    
    @misc{stiegler_synthetic_us_passports,
      author = {Stiegler, Arnaud},
      title = {Synthetic US Passports (Easy)},
      year = {2024},
      publisher = {Hugging Face},
      howpublished = {\url{https://huggingface.co/datasets/arnaudstiegler/synthetic_us_passports_easy}}
    }
    

## More Information#

For more information about the dataset generation process and code, visit:

  * GitHub Repository: https://github.com/arnaudstiegler/synth-doc-AI

  * Hugging Face Dataset: https://huggingface.co/datasets/arnaudstiegler/synthetic_us_passports_easy




## Dataset Card Contact#

For questions or issues related to this dataset, please refer to the original dataset repository or contact the dataset curator through the Hugging Face dataset page.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
