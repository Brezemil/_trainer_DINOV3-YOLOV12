---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/pdf_loader.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/brimoor/pdf-loader)

# PDF Loader Plugin#

A [FiftyOne plugin](https://docs.voxel51.com/plugins/index.html) for loading PDFs as images.

## Installation#

If you havenât already, [install FiftyOne](https://docs.voxel51.com/getting_started/install.html):
    
    
    pip install fiftyone
    

Then install the plugin and its dependencies:
    
    
    fiftyone plugins download https://github.com/brimoor/pdf-loader
    
    brew install poppler
    pip install pdf2image
    

## Usage#

### Using the App UI#

  1. Launch the App:



    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    session = fo.launch_app(dataset)
    

  2. Press ``` or click the `Browse operations` icon above the grid

  3. Run the `pdf_loader` operator




### Using the SDK#

You can use the plugin programmatically from Python:
    
    
    import fiftyone as fo
    import fiftyone.operators as foo
    
    import requests
    import os
    
    # Download a PDF from a URL (optional - you can use any local PDF)
    url = "https://arxiv.org/pdf/2309.11419"
    filename = url.split('/')[-1] + ".pdf"  # Add .pdf extension
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")
    
    # Load the PDF loader operator
    pdf_loader = foo.get_operator("@brimoor/pdf-loader/pdf_loader")
    
    # Create a dataset for the PDF pages
    pdf_dataset = fo.Dataset("pdf_dataset")
    
    # Convert PDF to images and add to dataset
    pdf_loader(
        pdf_dataset,
        input_path="./2309.11419.pdf",  # Path to your PDF file
        output_dir="./pdf_images",     # Directory to save the images
        dpi=200,                        # Image quality in DPI
        fmt="png",                      # Image format (png or jpg)
        tags=None,                      # Optional tags for samples
        delegate=False                  # Set to True for async execution
    )
    

## What next?#

Install the [PyTesseract OCR](https://github.com/jacobmarks/pytesseract-ocr-plugin) and [Semantic Document Search](https://github.com/jacobmarks/semantic-document-search-plugin) plugins to make your documents searchable!

  1. Install the plugins and their dependencies:



    
    
    fiftyone plugins download https://github.com/jacobmarks/pytesseract-ocr-plugin
    pip install pytesseract
    
    <video controls width="100%" style="max-width: 600px; height: auto;"><source src="https://github.com/jacobmarks/semantic-document-search-plugin
    pip install qdrant_client
    pip install sentence_transformers
    

  2. Launch a Qdrant server:



    
    
    docker run -p "6333:6333" -p "6334:6334" -d qdrant/qdrant" type="video/mp4"></video>
    

  3. Run the `run_ocr_engine` operator to detect text blocks

  4. Run the `create_semantic_document_index` operator to generate a semantic index for the text blocks

  5. Run the `semantically_search_documents` operator to perform arbitrary searches against the index!




## Implementation#

This plugin is a basically a wrapper around the following code:
    
    
    import os
    from pdf2image import convert_from_path
    
    INPUT_PATH = "/path/to/your.pdf"
    OUTPUT_DIR = "/path/for/page/images"
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    convert_from_path(INPUT_PATH, output_folder=OUTPUT_DIR, fmt="jpg")
    
    dataset.add_images_dir(OUTPUT_DIR)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
