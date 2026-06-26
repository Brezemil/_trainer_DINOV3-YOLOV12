---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/colqwen2_5_v0_2.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/colqwen2_5_v0_2)

# ColQwen2.5-v0.2 for FiftyOne#

![image](https://raw.githubusercontent.com/harpreetsahota204/colqwen2_5_v0_2/main/colqwen_fo.gif)

Integration of [ColQwen2.5-v0.2](https://huggingface.co/vidore/colqwen2.5-v0.2) as a FiftyOne Zoo Model for visual document retrieval.

## Overview#

[ColQwen2.5](https://huggingface.co/vidore/colqwen2.5-v0.2) is a Vision Language Model based on Qwen2.5-VL-3B-Instruct that generates ColBERT-style multi-vector representations for efficient document retrieval. This version takes dynamic image resolutions (up to 768 image patches) and doesnât resize them, preserving aspect ratios for better accuracy. This integration adapts ColQwen2.5 for use with FiftyOneâs embedding and similarity infrastructure.

## Deviations from Native Implementation#

### The Challenge#

ColQwen2.5 natively produces **variable-length multi-vector embeddings** :

  * Images: Variable number of vectors (up to 768 patches) with 128 dimensions per vector

  * Queries: Variable number of vectors with 128 dimensions per vector




These variable-length embeddings are incompatible with FiftyOneâs standard similarity infrastructure, which requires **fixed-dimension vectors**.

### Our Solution: Two-Stage Compression#

#### Stage 1: Token Pooling (Intelligent Compression)#

We use ColQwen2.5âs built-in `HierarchicalTokenPooler` with `pool_factor=3`:

  * Images: Variable patches â Compressed by factor of 3

  * Queries: Variable vectors â Compressed by factor of 3

  * **Performance** : Retains ~97.8% of native ColQwen2.5 accuracy

  * **Benefit** : Removes redundant patches (e.g., white backgrounds) while preserving aspect ratios




#### Stage 2: Final Pooling (FiftyOne Compatibility)#

After token pooling, we apply a final pooling operation to produce **fixed-dimension embeddings** :

Strategy | Output | Best For  
---|---|---  
`mean` (default) | `(128,)` | Holistic document matching, layout understanding  
`max` | `(128,)` | Specific content/keyword matching  
  
Both strategies produce embeddings compatible with FiftyOneâs similarity search.

## Installation#
    
    
    # Install FiftyOne and ColQwen2.5 dependencies
    pip install fiftyone colpali-engine transformers torch huggingface-hub
    

**Note** : This model requires `colpali-engine` and `transformers`.

## Quick Start#

### Register the Zoo Model#
    
    
    import fiftyone.zoo as foz
    
    # Register this repository as a remote zoo model source
    foz.register_zoo_model_source(
        "https://github.com/harpreetsahota204/colqwen2_5_v0_2",
        overwrite=True
    )
    

### Load Dataset#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load document dataset from Hugging Face
    dataset = load_from_hub(
        "Voxel51/synthetic_us_passports_easy",
        overwrite=True,
        max_samples=500  # Optional: subset for testing
    )
    

### Basic Workflow#
    
    
    import fiftyone.zoo as foz
    import fiftyone.brain as fob
    
    # Load ColQwen2.5 model with desired pooling strategy
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pooling_strategy="max",  # or "mean" (default)
        pool_factor=3  # Compression factor
    )
    
    # Compute embeddings for all documents
    dataset.compute_embeddings(
        model=model,
        embeddings_field="colqwen_embeddings",
    )
    
    # Check embedding dimensions
    print(dataset.first()['colqwen_embeddings'].shape)  # Should be (128,)
    
    # Build similarity index
    text_img_index = fob.compute_similarity(
        dataset,
        model="vidore/colqwen2.5-v0.2",
        embeddings_field="colqwen_embeddings",
        brain_key="colqwen_sim",
        model_kwargs={
            "pooling_strategy": "max",
            "pool_factor": 3,
        }
    )
    
    # Query for specific content (e.g., searching passport data)
    queries = dataset.distinct("place_of_birth.label")
    sims = text_img_index.sort_by_similarity(
        queries,
        k=3  # Top 3 results per query
    )
    
    # Launch FiftyOne App
    session = fo.launch_app(sims, auto=False)
    

## Advanced Embedding Workflows#

### Embedding Visualization with UMAP#

Create 2D visualizations of your document embeddings:
    
    
    import fiftyone.brain as fob
    
    # First compute embeddings
    dataset.compute_embeddings(
        model=model,
        embeddings_field="colqwen_embeddings"
    )
    
    # Create UMAP visualization
    results = fob.compute_visualization(
        dataset,
        method="umap",  # Also supports "tsne", "pca"
        brain_key="colqwen_viz",
        embeddings="colqwen_embeddings",
        num_dims=2
    )
    
    # Explore in the App
    session = fo.launch_app(dataset)
    

### Similarity Search#

Build powerful similarity search with ColQwen2.5 embeddings:
    
    
    import fiftyone.brain as fob
    
    # Build similarity index
    results = fob.compute_similarity(
        dataset,
        backend="sklearn",  # Fast sklearn backend
        brain_key="colqwen_sim", 
        embeddings="colqwen_embeddings"
    )
    
    # Find similar images
    sample_id = dataset.first().id
    similar_samples = dataset.sort_by_similarity(
        sample_id,
        brain_key="colqwen_sim",
        k=10  # Top 10 most similar
    )
    
    # View results
    session = fo.launch_app(similar_samples)
    

### Dataset Representativeness#

Score how representative each sample is of your dataset:
    
    
    import fiftyone.brain as fob
    
    # Compute representativeness scores
    fob.compute_representativeness(
        dataset,
        representativeness_field="colqwen_represent",
        method="cluster-center",
        embeddings="colqwen_embeddings"
    )
    
    # Find most representative samples
    representative_view = dataset.sort_by("colqwen_represent", reverse=True)
    

### Duplicate Detection#

Find and remove near-duplicate documents:
    
    
    import fiftyone.brain as fob
    
    # Detect duplicates using embeddings
    results = fob.compute_uniqueness(
        dataset,
        embeddings="colqwen_embeddings"
    )
    
    # Filter to most unique samples
    unique_view = dataset.sort_by("uniqueness", reverse=True)
    

### Advanced: Custom Analysis Pipeline#

Combine multiple ColQwen2.5 outputs for comprehensive analysis:
    
    
    import fiftyone.zoo as foz
    import fiftyone.brain as fob
    
    # Global embeddings for similarity
    embedding_model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pooling_strategy="mean",
        pool_factor=3
    )
    dataset.compute_embeddings(embedding_model, "colqwen_embeddings")
    
    # Build similarity index
    fob.compute_similarity(
        dataset, 
        embeddings="colqwen_embeddings", 
        brain_key="colqwen_sim"
    )
    
    # Comprehensive analysis
    session = fo.launch_app(dataset)
    

## Technical Details#

### FiftyOne Integration Architecture#
    
    
    Raw embeddings â Token pooling (factor=3) â Final pooling (mean/max) â Fixed (128,)
    

**Retrieval Pipeline** :
    
    
    dataset.compute_embeddings(model, embeddings_field="embeddings")
    > embed_images(): Applies token + final pooling
        > Returns (128,) compressed vectors
            > Stores in FiftyOne for similarity search
    

Both pipelines produce consistent, fixed-dimension embeddings compatible with FiftyOneâs infrastructure.

### Key Implementation Notes#

  1. **`raw_inputs=True`** : ColQwen2_5_Processor handles all preprocessing, so FiftyOneâs default transforms are disabled

  2. **Image Format Conversion** : FiftyOne may pass images as PIL, numpy arrays, or tensors; we convert all to PIL for ColQwen2_5_Processor compatibility

  3. **Compression** : Uses token-pooled and final-pooled embeddings

  4. **Fixed Dimensions** : After compression, all embeddings are 128-dimensional and compatible with all FiftyOne brain methods

  5. **Single-Vector Scoring** : Uses `score_single_vector()` after embeddings are compressed to fixed dimensions




## Configuration Options#

### Pooling Strategy#
    
    
    # Mean pooling (default) - holistic document matching
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pooling_strategy="mean"
    )
    
    # Max pooling - specific content/keyword matching
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pooling_strategy="max"
    )
    

### Pool Factor#
    
    
    # More aggressive compression (faster, less accurate)
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pool_factor=5
    )
    
    # Less compression (slower, more accurate)
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pool_factor=2
    )
    

## Resources#

  * **Original Repository** : [illuin-tech/colpali](https://github.com/illuin-tech/colpali)

  * **Model Weights** : [vidore/colqwen2.5-v0.2](https://huggingface.co/vidore/colqwen2.5-v0.2)

  * **Paper** : [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)

  * **Base Model** : [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)




## Citation#

If you use ColQwen2.5 in your research, please cite:
    
    
    @misc{faysse2024colpaliefficientdocumentretrieval,
      title={ColPali: Efficient Document Retrieval with Vision Language Models}, 
      author={Manuel Faysse and Hugues Sibille and Tony Wu and Bilel Omrani and Gautier Viaud and CÃ©line Hudelot and Pierre Colombo},
      year={2024},
      eprint={2407.01449},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2407.01449}, 
    }
    

## License#

  * **Base Model (Qwen2.5-VL)** : [Qwen Research License Agreement](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct)

  * **Model Adapters** : Apache 2.0

  * **Integration Code** : Apache 2.0 (see LICENSE)




## Files#

  * `zoo.py`: ColQwen2.5 model implementation with token pooling

  * `__init__.py`: Package initialization

  * `manifest.json`: Zoo model metadata




## Requirements#

See `manifest.json` for complete dependencies:

  * `colpali-engine` (includes HierarchicalTokenPooler)

  * `transformers`

  * `torch` / `torchvision`

  * `huggingface-hub`

  * `fiftyone`




## Zero-Shot Classification#

ColQwen2.5 can also be used for zero-shot classification tasks:
    
    
    import fiftyone.zoo as foz
    
    # Load model
    model = foz.load_zoo_model(
        "vidore/colqwen2.5-v0.2",
        pooling_strategy="max",
        pool_factor=3
    )
    
    # Define classes and text prompt
    classes = dataset.distinct("place_of_birth.label")
    model.classes = classes
    model.text_prompt = "A person born in "
    
    # Apply model for zero-shot classification
    dataset.apply_model(
        model,
        label_field="predictions"
    )
    
    # View predictions
    print(dataset.first()['predictions'])
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
