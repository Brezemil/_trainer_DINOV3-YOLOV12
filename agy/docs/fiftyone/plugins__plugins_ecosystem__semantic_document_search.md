---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/semantic_document_search.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/semantic-document-search-plugin)

# Semantic Document Search Plugin#

![display_and_search_thesis](https://github.com/jacobmarks/semantic-document-search-plugin/assets/12500356/ac87511d-c3f9-4718-891d-89e14aef4152)

This plugin is a Python plugin that allows you to semantically search through your text blocks (from Optical Character Recognition) in your dataset.

It uses a Qdrant index, with the GTE-base model from Hugging Faceâs Sentence Transformers library.

# Usage#

You will need to have text blocks in your dataset. You can do this with the [PyTesseract OCR plugin](https://github.com/jacobmarks/pytesseract-ocr-plugin).

Create a vector index for your text blocks with the `create_semantic_document_index` operator. You can then use the `semantically_search_documents` operator to search through your text blocks.

If you have multiple detections with text blocks, you can create multiple indexes. The index is stored in Qdrant with the collection name `<dataset_name>_sds_<field_name>`. When you use the `semantically_search_documents` operator, you can specify which index to use.

# Watch On Youtube#

[![Video Thumbnail](https://img.youtube.com/vi/I0FFDCbWZcM/0.jpg)](https://www.youtube.com/watch?v=I0FFDCbWZcM&list=PLuREAXoPgT0RZrUaT0UpX_HzwKkoB-S9j&index=13)

# Installation#

Download the plugin with the following command:
    
    
    fiftyone plugins download https://github.com/jacobmarks/semantic-document-search-plugin
    

You will need to install the Sentence Transformers library, and the Qdrant client Python library, which can be achieved with
    
    
    fiftyone plugins requirements @jacobmarks/semantic_document_search --install
    

You will also need to have a Qdrant instance running. You can do this with Docker once you have your Docker daemon running:
    
    
    docker run -p "6333:6333" -p "6334:6334" -d qdrant/qdrant
    

# Using with PyTesseract OCR Plugin#

This _semantic_ search plugin is in many ways analogous to the [keyword search plugin](https://github.com/jacobmarks/keyword-search-plugin), and is likewise designed to be used with the [PyTesseract OCR plugin](https://github.com/jacobmarks/pytesseract-ocr-plugin).

You can install the PyTesseract OCR plugin with the following command:
    
    
    fiftyone plugins download https://github.com/jacobmarks/pytesseract-ocr-plugin
    

# Operators#

## `create_semantic_document_index`#

![create_index](https://github.com/jacobmarks/semantic-document-search-plugin/assets/12500356/2ac0da4a-36b6-40d9-86e3-ec61a94f050c)

**Description** : Create a Qdrant index for the specified text field within a detections label field.

## `semantically_search_documents`#

![search_index](https://github.com/jacobmarks/semantic-document-search-plugin/assets/12500356/1c174879-398b-414d-8891-02bccf3c6be7)

**Description** : Semantically search for text in your dataset. Only labels matching your query will be shown.

You can specify the number of results to return, and the threshold for the similarity score.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
