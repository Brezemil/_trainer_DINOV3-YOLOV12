---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/medxpertqa.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/MedXpertQA)

# Dataset Card for MedXpertQA#

![image/png](https://huggingface.co/datasets/Voxel51/MedXpertQA/resolve/main/MedXpertQA.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1581 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/MedXpertQA")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Parsing Details#

  1. **Data Filtering** : We started with the test split from MedXpertQA/MM/test.jsonl and filtered it to only keep records that had exactly one image in their âimagesâ list. This was done using a simple JSON parser and list comprehension, resulting in 1,581 records that met our criteria.

  2. **Data Structure** : Each record in our filtered dataset contained medical case information including:

     * Question text and multiple choice options

     * Image references

     * Classifications (medical task, body system, question type)

     * Ground truth labels

  3. **FiftyOne Conversion** : We transformed this filtered data into FiftyOne format by:

     * Creating samples with proper image filepath references (MedXpertQA/images directory)

     * Converting metadata fields (question text, options, ID) into sample fields

     * Converting categorical fields (label, medical task, body system, question type) into FiftyOne Classification objects

     * Efficiently batch-loading all samples into a new FiftyOne dataset




The parsing code is as follows:
    
    
    import fiftyone as fo
    import os
    import json
    
    # Read the input JSONL file
    input_file = "MedXpertQA/MM/test.jsonl"
    
    filtered_data = []
    with open(input_file, 'r') as fin:
        for line in fin:
            record = json.loads(line.strip())
            # Only keep records where images list has exactly one element
            if len(record['images']) == 1:
                filtered_data.append(record) # filtered_data now contains all records with exactly one image
    
    
    
    # Create a new FiftyOne dataset
    dataset = fo.Dataset("MedXpertQA", overwrite=True)
    
    # Create list to hold all samples
    samples = []
    
    # Process all records
    for item in filtered_data:
        # Create a sample
        sample = fo.Sample(
            filepath=os.path.join("MedXpertQA/images", item["images"][0])
        )
        
        # Add metadata fields
        sample["question_id"] = item["id"]
        sample["question"] = item["question"]
        sample["options"] = item["options"]
        
        # Add classification fields
        sample["label"] = fo.Classification(label=item["label"])
        sample["medical_task"] = fo.Classification(label=item["medical_task"])
        sample["body_system"] = fo.Classification(label=item["body_system"])
        sample["question_type"] = fo.Classification(label=item["question_type"])
        
        # Add to samples list
        samples.append(sample)
    
    # Add all samples at once
    dataset.add_samples(samples)
    

### Dataset Description#

MedXpertQA is a highly challenging and comprehensive medical multiple-choice benchmark designed to evaluate expert-level medical knowledge and advanced reasoning capabilities in AI models. It consists of 4,460 questions spanning 17 medical specialties and 11 body systems, with two main subsets: MedXpertQA Text for text-only evaluations and MedXpertQA MM for multimodal assessments. The dataset stands out for its comprehensive coverage of specialized medical scenarios, expert-level difficulty, and alignment with realistic clinical decision-making processes.

  * **Curated by:** Researchers from Tsinghua University and Shanghai Artificial Intelligence Laboratory (Yuxin Zuo, Shang Qu, Yifei Li, Zhangren Chen, Xuekai Zhu, Ermo Hua, Kaiyan Zhang, Ning Ding, Bowen Zhou)

  * **Shared by [optional]:** Tsinghua University and Shanghai Artificial Intelligence Laboratory

  * **Language(s) (NLP):** en

  * **License:** Not explicitly stated in the paper




### Dataset Sources#

  * **Repository:** https://github.com/TsinghuaC3I/MedXpertQA

  * **Dataset Repository on Hugging Face:** https://huggingface.co/datasets/TsinghuaC3I/MedXpertQA

  * **Paper:** [MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://arxiv.org/abs/2501.18362)

  * **Leaderboard** Available at https://medxpertqa.github.io




## Uses#

### Direct Use#

MedXpertQA is designed to evaluate and benchmark the expert-level medical capabilities of large language models (LLMs) and large multimodal models (LMMs). Specific uses include:

  1. Assessing medical reasoning capabilities across diverse medical specialties and body systems

  2. Evaluating multimodal understanding of medical images, including radiology, pathology, and other clinical visuals

  3. Comparing model performance on challenging medical diagnostic and treatment planning tasks

  4. Benchmarking o1-like reasoning models on complex medical reasoning tasks

  5. Identifying strengths and weaknesses in AI systemsâ medical knowledge across different specialties




### Out-of-Scope Use#

MedXpertQA should not be used for:

  1. Directly making clinical decisions or providing medical advice without expert oversight

  2. Training medical professionals (as the dataset is designed for AI model evaluation)

  3. Generating leaderboards or comparisons without accounting for the datasetâs specific challenge profiles

  4. Evaluating general visual understanding capabilities unrelated to medical contexts

  5. Sharing examples online due to data leakage concerns (explicitly mentioned in the paper)




## Dataset Structure#

MedXpertQA consists of two primary subsets:

  1. **MedXpertQA Text** : 2,450 text-only questions with 10 options each

     * Average question length: 257.37 tokens

     * Incorporates clinical scenarios and specialty-specific assessments

  2. **MedXpertQA MM** : 2,000 multimodal questions with 5 options each

     * Contains 2,839 images (1.43 images per question average)

     * Average question length: 149.35 tokens

     * Encompasses 10 different image types including radiology, pathology, vital signs, diagrams, etc.




Each subset is further split into:

  * A few-shot development set with 5 questions

  * A test set with the remaining questions




Questions are categorized across:

  * **17 medical specialties** : From various American Board medical exams

  * **11 body systems** : Cardiovascular (13.7%), Nervous (13.7%), Skeletal (19.8%), etc.

  * **3 task categories** :

    * Diagnosis (50.54%): Primary, differential, etiologic, prognostic, etc.

    * Treatment (26.83%): Medicines, surgical procedures, preventive measures, etc.

    * Basic Medicine (22.63%): Anatomy, basic biology, genetics, statistics, etc.

  * **Reasoning classification** :

    * Reasoning: Complex multi-step reasoning questions

    * Understanding: Knowledge and perception assessment




## FiftyOne Dataset Structure#

**Basic Info:** 1,581 medical images with question-answer annotations

**Core Fields:**

  * `question_id`: StringField - Unique identifier for the question

  * `question`: StringField - Medical question text

  * `options`: DictField - Multiple choice answer options

  * `label`: EmbeddedDocumentField(Classification) - Correct answer classification

  * `medical_task`: EmbeddedDocumentField(Classification) - Type of medical task (e.g., diagnosis)

  * `body_system`: EmbeddedDocumentField(Classification) - Relevant body system or anatomy

  * `question_type`: EmbeddedDocumentField(Classification) - Question format or structure type




## Dataset Creation#

### Curation Rationale#

MedXpertQA was created to address critical limitations in existing medical benchmarks:

  1. Insufficient difficulty of current benchmarks (e.g., o1-preview achieving 96% and 99% accuracy on MedQA-USMLE and MMLU Medical Genetics)

  2. Lack of comprehensive coverage across specialized medical domains

  3. Poor alignment with real-world clinical scenarios, especially in multimodal benchmarks

  4. Absence of challenging reasoning tasks that require expert-level decision-making

  5. Need for a benchmark that can thoroughly assess advanced reasoning capabilities in medical contexts




The authors aimed to create a benchmark that could reliably evaluate both the medical knowledge and complex reasoning abilities required in real-world medical practice.

### Source Data#

#### Data Collection and Processing#

The dataset was built through a rigorous multi-stage process:

  1. **Initial Collection** : The authors collected 37,543 questions from:

     * USMLE and COMLEX-USA (medical licensing exams)

     * 17 American specialty board exams

     * ACR DXIT and TXIT exams, EDiR exams (radiology)

     * NEJM Image Challenge

     * Also gathered human response distributions and expert annotations

  2. **Data Filtering** :

     * **AI Expert Filtering** : Used 8 AI models (basic and advanced) to identify questions that challenge AI

     * **Human Expert Filtering** : Applied adaptive Brier score thresholds based on human response distributions

     * **Similarity Filtering** : Removed highly similar questions using MedCPT-Query-Encoder and edit distance

  3. **Data Augmentation** :

     * **Question Rephrasing** : Used LLMs to rephrase questions while preserving all original information

     * **Option Expansion** : Expanded options to 10 for Text and maintained 5 for MM

     * Used gpt-4o-2024-11-20 and claude-3-5-sonnet-20241022 for this process

  4. **Expert Review** : Medical professionals with physiciansâ licenses reviewed all content for accuracy and validity




#### Who are the source data producers?#

The source data was produced by professional medical examination boards and educational institutions, including:

  * United States Medical Licensing Examination (USMLE)

  * Comprehensive Osteopathic Medical Licensing Examination (COMLEX-USA)

  * American medical specialty boards (17 different specialties)

  * American College of Radiology (ACR)

  * European Board of Radiology (EDiR)

  * New England Journal of Medicine (NEJM)




These authoritative medical institutions create rigorous examinations to evaluate medical professionalsâ competency.

### Annotations#

#### Annotation process#

The dataset includes several types of annotations:

  1. **Task and Subtask Labels** : Used gpt-4o-2024-11-20 to categorize questions into:

     * Main tasks: Diagnosis, Treatment, Basic Medicine

     * Fine-grained subtasks within each category

  2. **Body System Labels** : LLM-annotated system classification based on Liachovitzky (2015)

  3. **Reasoning/Understanding Classification** : Used gpt-4o to determine whether each question primarily challenges reasoning or understanding capabilities

  4. **Expert Annotations** : The original sources provided:

     * Difficulty ratings

     * Explanations for correct answers

     * Human response distributions




#### Who are the annotators?#

Multiple groups contributed to annotations:

  * Original medical exam creators provided initial answer explanations and difficulty ratings

  * LLMs (primarily gpt-4o) were used for task, subtask, system, and reasoning classifications

  * Medical experts with physicianâs licenses performed the final review to ensure accuracy




#### Personal and Sensitive Information#

The dataset consists of medical examination questions rather than real patient data. The questions are designed to test medical knowledge rather than containing personally identifiable information. The authors state they obtained data from âfreely and publicly accessible sourcesâ and performed question rephrasing and option shuffling to comply with fair use laws.

## Bias, Risks, and Limitations#

  1. **Data Leakage Risk** : The authors acknowledge that since questions are from publicly available sources, thereâs a risk of data leakage. They mitigate this through question rephrasing and option augmentation.

  2. **Potential Medical Biases** : May reflect biases present in medical education and examination systems in the United States (from which most source material is derived).

  3. **Specialty Coverage Limitation** : While covering 17 specialties, this doesnât encompass all medical specialties or subspecialties.

  4. **Western Medical Focus** : Primarily based on U.S. medical standards and may not fully represent global or alternative medical practices.

  5. **Evaluation-Only Purpose** : The dataset is specifically designed for evaluation rather than training, with a relatively small size compared to training datasets.




### Recommendations#

  1. Users should not share examples online to prevent data leakage, as explicitly requested by the authors.

  2. The dataset should be used for evaluation purposes only, not for medical training or direct clinical applications.

  3. Researchers should consider the datasetâs U.S.-centric medical focus when interpreting results.

  4. Performance comparisons between Text and MM subsets should be avoided due to their different construction parameters.

  5. When evaluating model performance, researchers should analyze results across different medical specialties and body systems to provide a more nuanced understanding of capabilities.




## Citation#

**BibTeX:**
    
    
    @article{zuo2025medxpertqa,
      title={MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding},
      author={Zuo, Yuxin and Qu, Shang and Li, Yifei and Chen, Zhangren and Zhu, Xuekai and Hua, Ermo and Zhang, Kaiyan and Ding, Ning and Zhou, Bowen},
      journal={arXiv preprint arXiv:2501.18362},
      year={2025}
    }
    

**APA:** Zuo, Y., Qu, S., Li, Y., Chen, Z., Zhu, X., Hua, E., Zhang, K., Ding, N., & Zhou, B. (2025). MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding. arXiv preprint arXiv:2501.18362v2.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
