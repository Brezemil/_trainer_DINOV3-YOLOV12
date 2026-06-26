---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/american_sign_language_mnist.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/American-Sign-Language-MNIST)

# Dataset Card for ASL-MNIST#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 34,627 samples of American Sign Language (ASL) alphabet images, converted from the original Kaggle Sign Language MNIST dataset into a format optimized for computer vision workflows.

![](https://huggingface.co/datasets/Voxel51/American-Sign-Language-MNIST/resolve/main/ASL-MNIST.png)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/American-Sign-Language-MNIST",
                             max_samples=200)
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

This dataset is a derived work of the public domain ASL MNIST dataset. The original content is CC0, and we have applied an MIT license to the packaging and any additional code or annotations.

### Dataset Description#

This dataset contains 34,627 grayscale images of American Sign Language (ASL) alphabet hand gestures. Each image is 28x28 pixels and represents one of 24 letters from the ASL alphabet. The dataset excludes the letters J and Z as these require motion to be properly signed and cannot be represented in static images.

The original data was sourced from Kaggleâs Sign Language MNIST dataset and has been converted into individual image files with proper FiftyOne annotations for easy visualization, querying, and analysis.

  * **Curated by:** Antonio Rueda-Toicen (Voxel51)

  * **Funded by:** Voxel51

  * **Shared by:** Voxel51

  * **Language(s) (NLP):** en

  * **License:** MIT




### Dataset Sources#

  * **Original Repository:** [Kaggle Sign Language MNIST](https://www.kaggle.com/datasets/datamunge/sign-language-mnist)

  * **Processing Code:** [Google Colab Notebook](https://github.com/andandandand/practical-computer-vision/blob/main/ASL_from_Kaggle_to_FiftyOne.ipynb) \- Converted from CSV format to individual JPG images using FiftyOne

  * **FiftyOne Documentation:** [voxel51/fiftyone](https://github.com/voxel51/fiftyone)




## Uses#

This dataset is ideal for:

  * **Computer vision research** : Training and evaluating image classification models

  * **Sign language recognition** : Developing ASL alphabet recognition systems

  * **Educational purposes** : Teaching machine learning concepts with a meaningful, accessible dataset

  * **Prototyping** : Quick experimentation with image classification algorithms

  * **FiftyOne demonstrations** : Showcasing dataset visualization and management capabilities




### Out-of-Scope Use#

This dataset should not be used for:

  * **Complete ASL communication systems** : Missing J and Z letters, and doesnât include words, phrases, or grammar

  * **Real-time sign language interpretation** : Static images donât capture the dynamic nature of full ASL communication

  * **Medical or accessibility applications** : Without proper validation in clinical settings

  * **Production ASL recognition systems** : Without additional data augmentation and validation




## Dataset Structure#

The dataset contains 34,627 samples split into training and test sets:

  * **Training samples** : ~27,455 images

  * **Test samples** : ~7,172 images

  * **Image format** : 28x28 pixel grayscale JPG images

  * **Labels** : 24 ASL alphabet letters (A-I, K-Y, excluding J and Z)




### Label Mapping#

The dataset uses the following label mapping:
    
    
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
    18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'
    

Note: Labels 9 (J) and 25 (Z) are excluded as these letters require motion in ASL.

## Dataset Creation#

This dataset was created to provide an easily accessible, well-structured version of the ASL alphabet dataset for computer vision research and education. The conversion to FiftyOne format enables:

  * Rich visualization and exploration capabilities

  * Advanced querying and filtering

  * Seamless integration with machine learning workflows

  * Better understanding of dataset characteristics and potential biases




### Source Data#

#### Data Collection and Processing#

The original data came from the Kaggle Sign Language MNIST dataset. The processing pipeline included:

  1. **Download** : Retrieved CSV files from Kaggle using the Kaggle API

  2. **Image conversion** : Converted pixel arrays from CSV rows into 28x28 grayscale images

  3. **File organization** : Saved images as individual JPG files with systematic naming

  4. **Annotation** : Created FiftyOne classification labels for each image

  5. **Metadata computation** : Added image metadata for enhanced searchability




Processing was performed using Python with pandas, PIL, NumPy, and FiftyOne libraries.

#### Who are the source data producers?#

The original dataset was created by the Kaggle user âdatamungeâ and represents hand gesture images collected for ASL alphabet recognition research. The specific methodology for the original data collection is not detailed in the source.

### Annotations#

#### Annotation process#

Annotations were automatically generated during the conversion process:

  * Each image received a classification label corresponding to its ASL letter

  * Labels were mapped from numeric indices to letter strings

  * Split information (train/test) was preserved as tags

  * No manual annotation was required as labels were inherited from the original dataset




#### Who are the annotators?#

The original labels were provided in the source Kaggle dataset. The FiftyOne conversion and annotation formatting was performed by Antonio Rueda-Toicen at Voxel51.

### Personal and Sensitive Information#

The dataset contains images of human hands performing sign language gestures. While hands are visible, no faces or other personally identifiable information is included in the images. The 28x28 pixel resolution is too low to identify individuals from hand features alone.

## Bias, Risks, and Limitations#

### Known Limitations#

  * **Incomplete alphabet** : Missing J and Z letters limits complete ASL alphabet coverage

  * **Static images only** : Cannot represent the dynamic/motion aspects of ASL

  * **Limited diversity** : May not represent the full diversity of hand sizes, skin tones, or signing styles

  * **Low resolution** : 28x28 pixels may not capture fine details important for real-world applications

  * **Single signer perspective** : May not generalize well to different signing styles or hand appearances




### Potential Biases#

  * **Demographic representation** : Unknown diversity in the original data collection

  * **Lighting conditions** : Images may reflect specific lighting setups that donât generalize

  * **Hand positioning** : May favor certain hand orientations or positions

  * **Background consistency** : Controlled backgrounds may not reflect real-world conditions




### Recommendations#

Users should be aware of these limitations and consider:

  * Supplementing with additional diverse ASL datasets for production use

  * Validating model performance across different demographic groups

  * Testing with real-world conditions and lighting variations

  * Incorporating motion-based data for complete ASL recognition systems

  * Consulting with ASL community members for culturally appropriate applications




## Citation#

**BibTeX:**
    
    
    @dataset{rueda_toicen_2024_asl_mnist,
      title={American Sign Language MNIST Dataset (FiftyOne Format)},
      author={Rueda-Toicen, Antonio},
      year={2024},
      publisher={Hugging Face},
      url={https://huggingface.co/datasets/andandandand/American-Sign-Language-MNIST}
    }
    

## Glossary#

  * **ASL** : American Sign Language, a complete, natural language that uses hand gestures, facial expressions, and body language

  * **FiftyOne** : An open-source tool for building high-quality datasets and computer vision models

  * **MNIST** : A reference to the famous Modified National Institute of Standards and Technology database, indicating 28x28 pixel grayscale images

  * **Classification** : The machine learning task of assigning a category or label to an input




## More Information#

For more information about FiftyOne and dataset management best practices, visit:

  * [FiftyOne Documentation](https://docs.voxel51.com/)

  * [FiftyOne GitHub Repository](https://github.com/voxel51/fiftyone)

  * [Computer Vision Datasets Guide](https://docs.voxel51.com/user_guide/dataset_creation/index.html)




## Dataset Card Authors#

Antonio Rueda-Toicen (Voxel51)

## Dataset Card Contact#

Antonio Rueda-Toicen - antonio@getfiftyone.com

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
