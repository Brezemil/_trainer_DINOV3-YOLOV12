---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/food_waste_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/food-waste-dataset)

# Dataset Card for Food Waste Dataset#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 375 samples focused on food waste analysis and nutritional content detection.

![image/png](https://huggingface.co/datasets/Voxel51/food-waste-dataset/resolve/main/food_waste_navigation.webp)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/food-waste-dataset")
    
    # Launch the app from a Jupyter notebook
    session = fo.launch_app(dataset, auto=False)
    print(session.url)
    

## Dataset Details#

### Dataset Description#

This dataset contains detailed information about food waste, combining visual data with comprehensive nutritional measurements. Each sample includes an image of a meal along with ingredient-level nutritional information measured both before and after consumption, enabling food waste analysis and nutritional content detection.

The dataset has been enhanced with:

  * **YOLO-E segmentation** for ingredient detection and segmentation

  * **DINOv2 embeddings** for visual similarity analysis

  * **Translated ingredient names** from German to English

  * **Nutritional metadata** including calories, fats, proteins, carbohydrates, and salt content

  * **Curated by:** L. Stroetmann, a la QUARTO, AI Service Center at Hasso Plattner Institute, Voxel51

  * **Enhanced by:** FiftyOne computer vision pipeline

  * **Language(s):** English (translated from German)

  * **License:** MIT




### Dataset Sources#

  * **Original Repository:** [AI-ServicesBB/food-waste-dataset](https://huggingface.co/datasets/AI-ServicesBB/food-waste-dataset)

  * **Processing Code:** Available in the accompanying Jupyter notebook

  * **Enhanced Version:** Includes segmentation masks and embeddings




## Uses#

### Direct Use#

This dataset is suitable for:

  * **Food waste analysis** and sustainability research

  * **Nutritional content detection** from images

  * **Ingredient segmentation** and recognition

  * **Computer vision model training** for food-related tasks

  * **Multi-modal learning** combining visual and nutritional data

  * **Food portion estimation** and consumption analysis




### Out-of-Scope Use#

This dataset should not be used for:

  * Medical diagnosis or personalized dietary recommendations

  * Commercial food recognition without proper validation

  * Applications requiring real-time nutritional analysis without expert oversight

  * Any use that could promote harmful eating behaviors




## Dataset Structure#

The dataset contains 375 samples split into train and test sets, with each sample containing:

### Image Data#

  * **filepath** : Path to the meal image

  * **metadata** : Image dimensions, format, and technical details




### Nutritional Information (Per Ingredient)#

  * **ingredient_name** : Name of each ingredient (translated to English)

  * **article_number** : Unique identifier for ingredients

  * **number_of_portions** : Portion count

  * **weight_per_portion** : Weight per individual portion

  * **weight_per_plate** : Total weight on plate

  * **kcal_per_plate** , **kj_per_plate** : Caloric content

  * **fat_per_plate** , **saturated_fat_per_plate** : Fat content

  * **carbohydrates_per_plate** , **sugar_per_plate** : Carbohydrate content

  * **protein_per_plate** : Protein content

  * **salt_per_plate** : Salt content




### Before/After Consumption Measurements#

  * **weight_before/after** : Total meal weight

  * **kcal_before/after** : Total calories

  * **fat_before/after** : Total fat content

  * **carbohydrates_before/after** : Total carbohydrates

  * **protein_before/after** : Total protein

  * **salt_before/after** : Total salt




### Food Waste Metrics#

  * **return_quantity** : Amount of food returned/wasted

  * **return_percentage** : Percentage of food wasted




### Computer Vision Annotations#

  * **yoloe_segmentation** : Ingredient segmentation masks from YOLO-E

  * **segment_embeddings** : DINOv2 embeddings for segmented regions

  * **dinov2-image-embeddings** : Full image embeddings

  * **similarity indices** : For content-based search and analysis




## Dataset Creation#

The Google Colab notebook used to curate and produce the dataset is available here:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/andandandand/practical-computer-vision/blob/main/notebooks/Food_Dataset_Curation_with_Fiftyone.ipynb)

### Curation Rationale#

This dataset was created to support research in food waste reduction and nutritional analysis. By combining visual data with detailed nutritional measurements, it enables the development of computer vision systems that can:

  * Automatically detect and quantify food waste

  * Estimate nutritional content from images

  * Analyze consumption patterns

  * Support sustainability initiatives in food service




### Source Data#

https://huggingface.co/datasets/AI-ServicesBB/food-waste-dataset

#### Data Collection and Processing#

The original dataset was collected by the L. Stroetmann, a la QUARTO, and the AI Service Center at HPI and contained:

  * Images of meals in German food service settings

  * Detailed nutritional information in German

  * Before and after consumption measurements




#### Processing steps included:#

  1. **Translation** : German ingredient names and field names translated to English

  2. **Segmentation** : YOLO-E model applied for ingredient detection

  3. **Embeddings** : DINOv2 model used for visual feature extraction

  4. **Similarity indexing** : Computed for both full images and segmented regions

  5. **Metadata computation** : Image technical details extracted




#### Who are the source data producers?#

The original data was produced by the AI Service Center at the Hasso Plattner Institute (HPI) as part of food waste research initiatives.

### Annotations#

#### Annotation process#

  * **Ingredient Translation** : Manual mapping of 40+ German ingredient names to English equivalents

  * **Segmentation** : Automated using YOLO-E model trained on food ingredients

  * **Embedding Generation** : Automated using DINOv2 vision transformer

  * **Quality Control** : Visual inspection of segmentation results




#### Who are the annotators?#

  * **Translation** : Manual annotation by dataset curator

  * **Segmentation** : YOLO-E model (yoloe-11s-seg.pt)

  * **Embeddings** : DINOv2-ViT-L14 model




## Technical Details#

### Ingredients Covered#

The dataset includes 40+ food ingredients including:

  * Proteins: meatballs, fish fillet, chicken, beef, pork, sausages

  * Carbohydrates: rice, potatoes, bread dumplings, spaetzle

  * Vegetables: green beans, carrots, cabbage, cauliflower, peas

  * Sauces and condiments: various gravies, mustard sauce, dressings

  * Dairy: cream, vegetable-based cream alternatives




### Model Performance#

The dataset includes pre-computed:

  * **Segmentation masks** with ingredient-level precision

  * **Visual embeddings** enabling similarity search

  * **UMAP visualization** for dataset exploration




## Bias, Risks, and Limitations#

### Limitations#

  * **Cultural bias** : Dataset reflects German food service context

  * **Ingredient coverage** : Limited to ~40 common ingredients

  * **Portion size** : Focused on institutional serving sizes

  * **Image quality** : Consistent lighting/background conditions

  * **Temporal scope** : Snapshot data, not longitudinal study




### Risks#

  * **Nutritional accuracy** : Automated estimates should not replace professional dietary advice

  * **Generalization** : Model performance may vary on different food cultures/preparations

  * **Privacy** : While anonymized, institutional food service data patterns might be identifiable




### Recommendations#

Users should:

  * Validate nutritional estimates with professional dietary knowledge

  * Consider cultural context, this dataset was collected in Germany

  * Use appropriate evaluation metrics for food waste applications

  * Acknowledge dataset limitations in publications and applications




## Citation#

If you use this dataset, please cite both the original source and the enhanced version:

**Original Dataset:**
    
    
    @dataset{hpi_food_waste_2024,
      title={Food Waste Dataset},
      author={Felix Boelter and Felix Venner},
      year={2024},
      url={https://huggingface.co/datasets/AI-ServicesBB/food-waste-dataset}
    }
    

**Enhanced Version:**
    
    
    @dataset{food_waste_fiftyone_2024,
      title={Food Waste Dataset with FiftyOne Enhancements},
      author={Felix Boelter and Felix Venner and Antonio Rueda-Toicen},
      year={2024},
      url={https://huggingface.co/datasets/andandandand/food-waste-dataset}
    }
    

## More Information#

For technical details about the processing pipeline, see the accompanying Google Colab notebook. The dataset supports various computer vision tasks and can be explored interactively using the FiftyOne application.

### Related Work#

  * FiftyOne: Open-source tool for dataset curation and model analysis

  * YOLO-E: State-of-the-art object detection and segmentation

  * DINOv2: Self-supervised vision transformer for embeddings

  * Food waste reduction and sustainability research




## Dataset Card Contact#

Antonio Rueda-Toicen

For questions about the original dataset, please refer to the AI Service Center, HPI.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
