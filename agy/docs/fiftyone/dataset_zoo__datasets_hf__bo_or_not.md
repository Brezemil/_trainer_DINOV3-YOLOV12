---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/bo_or_not.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/bo_or_not)

# Dataset Card for bo-dataset#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 169 samples designed for binary classification of Bo (Barack Obamaâs Portuguese Water Dog) versus other pets.

![Bo Dataset](https://huggingface.co/datasets/Voxel51/bo_or_not/resolve/main/bo_dataset.png)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/bo_or_not")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset contains images for binary classification between Bo (Barack Obamaâs Portuguese Water Dog) and other pets (cats and dogs). The dataset was created to demonstrate transfer learning techniques using a pre-trained VGG16 model. Bo was a Portuguese Water Dog who lived in the White House during Barack Obamaâs presidency.

  * **Curated by:** Antonio Rueda-Toicen (antonio@getfiftyone.com)

  * **Language(s):** en

  * **License:** MIT

  * **Source code to produce the FiftyOne dataset:** [Colab Notebook](https://colab.research.google.com/drive/1XFoKgM_WQ9l2WgK6aS5GLFGc8uv0cdGB)




### Dataset Sources#

  * **Original Data Source:** [Presidential Doggy Door - Kaggle](https://www.kaggle.com/datasets/drvnmanju/presidential-doggy-door)

  * **Tutorial Implementation:** [Google Colab Notebook](https://colab.research.google.com/drive/1XFoKgM_WQ9l2WgK6aS5GLFGc8uv0cdGB)

    * [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XFoKgM_WQ9l2WgK6aS5GLFGc8uv0cdGB)

  * **Alternative Access:** [Google Drive](https://drive.google.com/drive/folders/1EU1ujeNtvsaKAIeyS7J8BDFC60iHvwi1?usp=drive_link)




## Uses#

### Direct Use#

This dataset is intended for:

  * Binary image classification tasks

  * Transfer learning demonstrations

  * Computer vision education and tutorials

  * Experimenting with pre-trained models like VGG16

  * Learning FiftyOne dataset management and visualization




### Out-of-Scope Use#

This dataset should not be used for:

  * Production security systems

  * Real-world pet identification systems

  * Commercial applications without proper validation

  * Any application requiring high accuracy pet identification




## Dataset Structure#

The dataset contains 169 images split across three sets:

  * **Training set:** 50% of original training data

  * **Validation set:** 50% of original training data

  * **Test set:** Independent test images




### Data Fields#

  * `filepath`: Path to the image file

  * `ground_truth`: Classification label (âboâ or ânot_boâ)

  * `tags`: Dataset split indicators (âtrainâ, âvalidationâ, âtestâ)

  * `vgg16-imagenet-predictions`: Original VGG16 ImageNet predictions

  * `vgg16-imagenet-embeddings`: Feature embeddings from VGG16

  * `fine_tuned_vgg16_prediction`: Fine-tuned model predictions (test set only)




### Label Distribution#

  * **bo** : Images of Bo (Barack Obamaâs Portuguese Water Dog)

  * **not_bo** : Images of other pets (cats and dogs)




## Dataset Creation#

### Curation Rationale#

This dataset was created to demonstrate transfer learning concepts using a real-world scenario where a computer vision system needs to identify a specific individual (Bo) among other similar animals. The task simulates a security application while providing an engaging educational example.

### Source Data#

#### Data Collection and Processing#

The images were collected and organized into a binary classification structure:

  * Images of Bo were labeled as âboâ

  * Images of other pets (cats and dogs) were labeled as ânot_boâ

  * Data was split into training/validation and test sets

  * Images were processed using standard computer vision preprocessing techniques




#### Data Augmentation#

The training process includes augmentation techniques:

  * Affine transformations (translation, scaling, rotation)

  * Elastic deformations

  * Perspective transformations

  * Horizontal flipping

  * Brightness and contrast adjustments

  * Random grayscale conversion




#### Who are the source data producers?#

The dataset was curated by Antonio Rueda-Toicen for educational purposes as part of FiftyOne documentation and tutorials.

### Model Training Details#

The dataset includes results from transfer learning using:

  * **Base Model:** VGG16 pre-trained on ImageNet

  * **Architecture Modification:** Replaced final classifier for binary classification

  * **Training Strategy:** Froze base VGG16 layers, trained only new classifier layers

  * **Loss Function:** Binary Cross Entropy with Logits

  * **Optimizer:** Adam (lr=0.003)

  * **Training Epochs:** 10 epochs with early stopping




## Technical Implementation#

### Preprocessing Pipeline#

Images are processed using:

  * Conversion to RGB format

  * Resizing to 256x256 pixels

  * Center cropping to 224x224 pixels

  * Normalization with ImageNet statistics (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])




### Evaluation Metrics#

The model performance is evaluated using:

  * Binary classification accuracy

  * Confusion matrix

  * Per-class precision and recall

  * FiftyOneâs built-in evaluation tools




## Bias, Risks, and Limitations#

### Limitations#

  * Small dataset size (169 samples) limits generalization

  * Limited to specific breeds and individuals

  * May not generalize to other Portuguese Water Dogs

  * Training data may not represent full diversity of pet appearances

  * Designed for educational purposes, not production use




### Potential Biases#

  * Dataset may be biased toward specific lighting conditions, angles, or image quality

  * Limited representation of pet diversity

  * Potential overfitting due to small dataset size




### Recommendations#

Users should be aware that this dataset is primarily educational and should not be used for production applications without significant additional validation and testing. The small size makes it unsuitable for robust real-world applications.

## Citation#

**BibTeX:**
    
    
    @misc{rueda_toicen_2024_bo_dataset,
      author = {Rueda-Toicen, Antonio},
      title = {Bo or Not Bo: Binary Classification with Transfer Learning},
      year = {2024},
      url = {https://colab.research.google.com/drive/1XFoKgM_WQ9l2WgK6aS5GLFGc8uv0cdGB},
      note = {FiftyOne educational dataset}
    }
    

## Dataset Card Authors#

Antonio Rueda-Toicen (antonio@getfiftyone.com)

## Dataset Card Contact#

For questions about this dataset, please contact Antonio Rueda-Toicen at antonio@getfiftyone.com or visit the [FiftyOne documentation](https://docs.voxel51.com/).

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
