---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/inquire_rerank.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/INQUIRE_Rerank)

# Dataset Card for INQUIRE-ReRank#

![image/png](https://huggingface.co/datasets/Voxel51/INQUIRE_Rerank/resolve/main/inquire_rerank.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 16000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/INQUIRE_Rerank")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Important Notes:#

Although the similarity index over the dataset has already been constructed, you will need to ensure that you have the following installed:

`pip install open_clip_torch`

After installing this, ensure you downloaded the OpenCLIP and BioCLIP model weights. You can ensure this by running the following lines of code after you have downloaded this dataset:
    
    
    import fiftyone.zoo as foz
    
    bio_clip_model = foz.load_zoo_model(
        name_or_url="open-clip-torch",
        clip_model="hf-hub:imageomics/bioclip",
        pretrained="",
    )
    
    clip_model = foz.load_zoo_model("open-clip-torch")
    

Then, you can perform a natural language search over the dataset via the App (as shown in the gif above) or via the SDK:
    
    
    #using the similarity index built with the OpenCLIP model
    view_1 = dataset.sort_by_similarity("mongoose on the plains", k=5, brain_key="open_clip_sim")
    
    #using the similarity index built with the BioCLIP model
    view_2 = dataset.sort_by_similarity("mongoose on the plains", k=5, brain_key="bio_clip_sim")
    

To visualize the map, you will need to [obtain a free Mapbox Token](https://docs.mapbox.com/help/getting-started/access-tokens/) and set the following environment variable prior to launching the app:

`export MAPBOX_TOKEN=XXXXXXXX`

## Dataset Details#

### Dataset Description#

INQUIRE (A Natural World Text-to-Image Retrieval Benchmark) is a challenging benchmark for evaluating expert-level text-to-image retrieval systems. It consists of 250 expert-level queries paired with comprehensive relevance annotations over a pool of 5 million natural world images (iNat24). Unlike previous text-to-image retrieval benchmarks which contain simple queries with exactly one relevant image per query, INQUIRE includes complex, domain-specific queries with multiple relevant images (ranging from 1-1,500 matches per query, with 33,000 total matches). The benchmark is structured as two tasks: INQUIRE-FULLRANK (full dataset ranking) and INQUIRE-RERANK (reranking of top-100 retrievals). The dataset is designed to bridge the gap between AI capabilities and the needs of real-world scientific inquiry, with a focus on accelerating ecological and biodiversity research.

  * **Curated by:** Massachusetts Institute of Technology, University College London, University of Edinburgh, University of Massachusetts Amherst, and iNaturalist

  * **Funded by:** Generative AI Laboratory (GAIL) at the University of Edinburgh, the Global Center on AI and Biodiversity Change (NSF OISE-2330423 and NSERC 585136), and the Biome Health Project funded by WWF-UK

  * **Shared by:** The INQUIRE research team

  * **Language(s) (NLP):** en

  * **License:** CC BY-NC 4.0




### Dataset Sources#

  * **Repository:** https://github.com/inquire-benchmark/INQUIRE

  * **Project Page:** https://inquire-benchmark.github.io/

  * **Paper:** Vendrow, E., Pantazis, O., Shepard, A., Brostow, G., Jones, K. E., Mac Aodha, O., Beery, S., & Van Horn, G. (2024). INQUIRE: A Natural World Text-to-Image Retrieval Benchmark. arXiv:2411.02537v3

  * **Dataset on HF:** https://huggingface.co/datasets/evendrow/INQUIRE-Rerank




To see the code for how to parse this dataset into FiftyOne format, [checkout this notebook on Colab](https://colab.research.google.com/drive/1rVC5D6KJAA8ZPAUk87fjIMo2kb5agw6Z?usp=sharing).

## Uses#

### Direct Use#

This dataset is intended to be used for:

  * Benchmarking text-to-image retrieval models on expert-level queries

  * Evaluating reranking methods for image retrieval

  * Developing more effective retrieval systems for ecological and biodiversity research

  * Testing multimodal modelsâ understanding of fine-grained natural world concepts

  * Research into domain-specific retrieval that requires expert knowledge




### Out-of-Scope Use#

This dataset should not be used for:

  * Making conservation assessments based on predictions from biased or inaccurate models

  * Commercial applications (prohibited by the CC BY-NC 4.0 license)

  * Training general-purpose image generation models

  * Applications that might create inaccurate or harmful associations between queries and wildlife images

  * Creating derivative datasets that do not respect the original image licenses




## Dataset Structure#

The INQUIRE benchmark consists of two main components:

  1. **iNat24 Dataset** :

     * 5 million natural world images spanning 10,000 species

     * Collected from the iNaturalist platform between 2021-2023

     * Each image includes metadata: species label, location, observation time, license information, and full taxonomic classification

  2. **INQUIRE Queries and Annotations** :

     * 250 expert-level text queries

     * Each query belongs to one of four supercategories (Appearance, Behavior, Context, or Species)

     * Further subdivided into 16 fine-grained categories (e.g., Health and Disease, Feeding and Hydration)

     * Comprehensive relevance annotations for each query (33,000 total positive matches)

     * Split into 50 validation and 200 test queries

  3. **INQUIRE-RERANK Task** :

     * Fixed set of 100 images per query (retrieved using CLIP ViT-H-14)

     * 200 queries filtered to ensure at least one positive image is among the top 100

     * Split into 40 validation and 160 test queries




## Dataset Creation#

### Curation Rationale#

INQUIRE was created to address several limitations in existing text-to-image retrieval benchmarks:

  * Current benchmarks are small (1,000-5,000 images)

  * They contain simple queries and are no longer challenging for modern models

  * Each query typically has only one relevant image, unlike real-world retrieval scenarios

  * They lack expert-level concepts that would require domain knowledge




The natural world domain was chosen because it contains rich visual concepts requiring expert knowledge, and improvements in retrieval could accelerate scientific discovery in ecology and biodiversity research.

### Source Data#

#### Data Collection and Processing#

  * iNat24 was created from an iNaturalist observation database export (generated on 2023-12-30)

  * Images were filtered to include only observations from 2021-2023

  * The dataset uses the iNat21 taxonomy (for compatibility with that dataset)

  * Images were selected using a spatial-temporal clustering approach to reduce geographic bias

  * All images were resized to have a maximum dimension of 500px

  * Images containing human faces, personally identifiable information, or inappropriate content were filtered out




#### Who are the source data producers?#

The images in iNat24 were contributed by citizen scientists on the iNaturalist platform. These are typically nature enthusiasts who photograph and document plants, animals, and other organisms they encounter, and upload them to the platform with species identification.

### Annotations#

#### Annotation process#

  * Queries were collected through interviews with experts across ecological and environmental domains

  * Only queries that could be discerned from images alone and feasibly labeled over the entire dataset were retained

  * For each query, annotators labeled candidate images as either relevant or not relevant

  * When applicable, species labels were used to narrow down the search space for comprehensive labeling

  * For queries that couldnât be filtered by species, annotators labeled top CLIP retrievals until at least 100 consecutive retrievals were not relevant

  * In total, 194,334 images were labeled, with 32,696 identified as relevant across all queries




#### Who are the annotators?#

The annotations were performed by a carefully selected team of paid MSc students or equivalent, many with expertise in ecology allowing for labeling of difficult queries. Annotators were paid at the equivalent of $15.50 per hour.

#### Personal and Sensitive Information#

The dataset was filtered to remove images containing human faces, personally identifiable information, or other sensitive content. A combination of automated methods (RetinaFace face detection) and manual inspection was used to identify and remove such images.

## Bias, Risks, and Limitations#

  * Geographic bias: The images in iNat24 are not uniformly distributed globally, with higher representation from North America, Europe, and parts of Australasia, reflecting the spatial biases present in the iNaturalist platform.

  * Taxonomic bias: Some species groups may be overrepresented compared to others based on popularity among citizen scientists.

  * Potential for misinterpretation: The expert-level nature of some queries means that models might make confident but incorrect predictions.

  * Limited to visual information: The dataset only captures what can be observed in images, which may not capture all ecologically relevant information.

  * Seasonal bias: Observations might be skewed toward certain seasons when volunteer activity is higher.




### Recommendations#

  * Users should be aware of the geographic biases when applying models trained or evaluated on this data to regions with limited representation.

  * Conservation or scientific decisions should not be made solely based on model predictions without expert validation.

  * When developing retrieval systems, consider implementing filters to prevent potentially harmful text-to-image associations.

  * Future work could focus on addressing the geographic and taxonomic biases through targeted data collection.

  * Systems evaluated on this benchmark should be transparent about their limitations when deployed in real-world scientific applications.




## Citation#

**BibTeX:**
    
    
    @inproceedings{vendrow2024inquire,
      title={INQUIRE: A Natural World Text-to-Image Retrieval Benchmark},
      author={Vendrow, Edward and Pantazis, Omiros and Shepard, Alexander and Brostow, Gabriel and Jones, Kate E. and Mac Aodha, Oisin and Beery, Sara and Van Horn, Grant},
      booktitle={38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks},
      year={2024},
      eprint={2411.02537},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
    }
    

**APA:** Vendrow, E., Pantazis, O., Shepard, A., Brostow, G., Jones, K. E., Mac Aodha, O., Beery, S., & Van Horn, G. (2024). INQUIRE: A Natural World Text-to-Image Retrieval Benchmark. In 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks.

## Glossary#

  * **mAP@50** : Mean Average Precision at 50, a metric for evaluating retrieval quality

  * **nDCG** : Normalized Discounted Cumulative Gain, a ranking metric that considers the relative ordering of retrieved items

  * **MRR** : Mean Reciprocal Rank, a measure of the rank of the first correct retrieval

  * **Reranking** : The process of refining an initial set of retrievals using a more sophisticated model

  * **iNaturalist** : A citizen science platform where users contribute observations of biodiversity




## Dataset Card Authors#

The INQUIRE research team: Edward Vendrow, Omiros Pantazis, Alexander Shepard, Gabriel Brostow, Kate E. Jones, Oisin Mac Aodha, Sara Beery, and Grant Van Horn

## Dataset Card Contact#

For questions or issues related to the dataset, please contact the team through the GitHub repository: https://github.com/inquire-benchmark/INQUIRE

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
