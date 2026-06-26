---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/fiftyone_embeddings_combined.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/fiftyone-embeddings-combined)

# FiftyOne Embeddings Dataset#

This dataset combines the FiftyOne Q&A and function calling datasets with pre-computed embeddings for fast similarity search.

## Dataset Information#

  * **Total samples** : 28,118

  * **Q &A samples**: 14,069

  * **Function samples** : 14,049

  * **Embedding model** : text-embedding-3-large

  * **Embedding dimension** : 3072




## Schema#

  * `query`: The original question/query text

  * `response`: The unified response content (either answer text for Q&A or function call text for function samples)

  * `content_type`: Either âqa_responseâ or âfunction_callâ

  * `embedding`: Pre-computed embedding vector (3072 dimensions), based on the `query` feature

  * `dataset_type`: Either âqaâ or âfunctionâ

  * `source_dataset`: Original dataset name

  * `embedding_model`: Model used to compute embeddings




## Usage#
    
    
    from datasets import load_dataset
    import numpy as np
    from scipy.spatial.distance import cosine
    
    # Load dataset with embeddings
    dataset = load_dataset("Voxel51/fiftyone-embeddings-combined", split="train")
    
    # Extract embeddings for similarity search
    embeddings = np.array([item['embedding'] for item in dataset])
    queries = [item['query'] for item in dataset]
    
    def find_similar(query_embedding, top_k=5):
        similarities = [1 - cosine(query_embedding, emb) for emb in embeddings]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for i in top_indices:
            item = dataset[i]
            results.append({
                'query': item['query'],
                'response': item['response'],  # Unified response field
                'type': item['content_type'],
                'similarity': similarities[i]
            })
        return results
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
