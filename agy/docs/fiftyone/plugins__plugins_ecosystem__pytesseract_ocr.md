---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/pytesseract_ocr.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/pytesseract-ocr-plugin)

# PyTesseract Optical Character Recognition Plugin#

![funsd_predictions](https://github.com/jacobmarks/pytesseract-ocr-plugin/assets/12500356/1bda669c-f2f8-456f-912f-c3f6a6a0fadd)

## Updates#

  * **2023-10-19** : Added support for customizing prediction fields, and embedded field for OCR text.




This plugin is a Python plugin that allows you to perform optical character recognition on documents using PyTesseract â the Python bindings for the Tesseract OCR engine!

# Watch On Youtube#

[![Video Thumbnail](https://img.youtube.com/vi/jnNPGrM6Wr4/0.jpg)](https://www.youtube.com/watch?v=jnNPGrM6Wr4&list=PLuREAXoPgT0RZrUaT0UpX_HzwKkoB-S9j&index=6)

# Installation#
    
    
    fiftyone plugins download https://github.com/jacobmarks/pytesseract-ocr-plugin
    

You will also need to install the pluginâs requirements:
    
    
    pip install -r requirements.txt
    

# Operators#

## `run_ocr_engine`#

  * Runs the PyTesseract OCR engine on the documents in the dataset, converts the results to FiftyOne labels, and stores individual word predictions as well as block-level predictions on the dataset.




# Usage#

You can access the operator via the Appâs action menu, or by pressing the â`â key on your keyboard and selecting the operator from the dropdown menu.

If you have a view loaded and/or samples selected, the operator will give you the option to run the OCR engine on only those samples or on the entire dataset.

You can either choose to run the operator in the foreground, or to delegate the execution of the operator to a background job.

![ocr_queue_job](https://github.com/jacobmarks/pytesseract-ocr-plugin/assets/12500356/2ab239c1-8d37-44a7-b8d6-93285afe7f08)

Once youâve generated OCR predictions, you can search through them using the [Keyword Search plugin](https://github.com/jacobmarks/keyword-search-plugin)!

![funsd_block_predictions](https://github.com/jacobmarks/pytesseract-ocr-plugin/assets/12500356/a7b6e81f-7a1e-4663-8ae9-c32c3266015d)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
