---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/bioscan_30k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/BIOSCAN-30k)

# Dataset Card for BIOSCAN-30k#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 30000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/BIOSCAN-30k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

The BIOSCAN-5M dataset is a multimodal collection of over 5.15 million arthropod specimens (98% insects), curated to advance biodiversity monitoring through machine learning. It expands the earlier BIOSCAN-1M dataset by including high-resolution images, DNA barcode sequences, taxonomic labels (phylum to species), geographical locations, specimen size data, and Barcode Index Numbers (BINs). Designed for both closed-world (known species) and open-world (novel species) scenarios, it supports tasks like taxonomic classification, clustering, and multimodal learning.

**This dataset is a randomly chosen subset of 30,000 samples across all splits from the Cropped 256 dataset**

### Key Features:#

  * Images: 5.15M high-resolution microscope images (1024Ã768px) with cropped/resized versions.

  * Genetic Data: Raw DNA barcode sequences (COI gene) and BIN clusters.

  * Taxonomy: Labels for 7 taxonomic ranks (phylum, class, order, family, subfamily, genus, species).

  * Geographical Metadata: Collection country, province/state, latitude/longitude.

  * Size Metadata: Pixel count, area fraction, and scale factor for specimens.




### Dataset Description#

  * **Curated by:** International consortium led by the Centre for Biodiversity Genomics, University of Guelph, University of Waterloo, and Simon Fraser University.

  * **Funded by :** Government of Canadaâs New Frontiers in Research Fund (NFRF), CFI Major Science Initiatives, Walder Foundation, NVIDIA Academic Grant.

  * **Shared by:** [Harpreet Sahota, Hacker-in-Residence @ Voxel51](https://huggingface.co/harpreetsahota)

  * **License:** [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

  * **Copyright Holder:** CBG Photography Group

  * **Copyright Institution:** Centre for Biodiversity Genomics (email:CBGImaging@gmail.com)

  * **Photographer:** CBG Robotic Imager

  * **Copyright License:** Creative Commons Attribution 3.0 Unported (CC BY 3.0)

  * **Copyright Contact:** collectionsBIO@gmail.com




### Dataset Sources#

  * **Repository:** https://github.com/bioscan-ml/BIOSCAN-5M

  * **Paper:** https://arxiv.org/abs/2406.12723

  * **Project Page:** https://biodiversitygenomics.net/projects/5m-insects/




## Uses#

### Direct Use#

  * Taxonomic Classification: Train models for species/genus identification using DNA barcodes, images, or multi-modal fusion.

  * Novel Species Discovery: Cluster embeddings from unseen species using self-supervised features.

  * Biodiversity Monitoring: Analyze geographical distribution and size variations across taxa.

  * Multimodal Learning: Explore contrastive learning across DNA, images, and taxonomic labels.




### Out-of-Scope Use#

  * Non-biological applications (e.g., general image recognition).

  * Clinical/medical diagnosis (insects are non-human specimens).

  * Tasks requiring higher-resolution genetic data beyond COI barcodes.




#### This dataset, parsed into FiftyOne format, is meant to serve as a tool for exploring and understanding what is in the dataset.#

## Dataset Structure#

### Data Types:#

  * Images: Original (1024Ã768px) and cropped/resized (341Ã256px).

  * DNA: 660bp nucleotide sequences (FASTA format).

  * Metadata: CSV/JSON files with taxonomic labels, BINs, GPS coordinates, size metrics.




#### Splits:#

  * Closed-World: train (289K), val (14.7K), test (39.3K) for known species.

  * Open-World: key_unseen (36.4K), val_unseen (8.8K), test_unseen (7.8K) for novel species.

  * Pretrain: 4.68M unlabelled samples.

  * Heldout: 76.5K samples for novelty detection.

  * Relationships: Each specimen has a unique processid linking images, DNA, and metadata.

  * Taxonomic hierarchy: Labels follow Linnaean taxonomy (phylum â species).




## Curation Rationale#

Created to address the lack of large-scale multimodal datasets for insect biodiversity research. Aims to enable ML models for species identification, novel species discovery, and ecological analysis.

## Source Data#

  * Collected globally via the BIOSCAN project (47 countries), primarily using malaise traps. Managed by the International Barcode of Life Consortium (iBOL).




## Processing:#

  * Images: Cropped using fine-tuned DETR model to isolate specimens.

  * DNA: Filtered for COI barcode quality; aligned with MAFFT.

  * Taxonomy: Hybrid AI/human verification to resolve label conflicts.

  * Geodata: Standardized country/province names; validated coordinates.




## Annotations#

  * Taxonomic Labels: Verified by entomologists using DNA barcodes and morphological features.

  * DNA BINs: Automatically assigned via BOLD system (sequence similarity).

  * Geographical Data: Extracted from collector metadata.

  * Size Data: Calculated from image pixel counts and microscope scaling factors.




## Guidelines:#

  * Species labels with non-standard formats (e.g., âsp.â, numerals) were excluded from âseenâ species.

  * Inferred missing subfamily labels (e.g., âunassigned Sciaridaeâ) to maintain taxonomic hierarchy.




## Citation#
    
    
    @misc{gharaee2024bioscan5m,
        title={{BIOSCAN-5M}: A Multimodal Dataset for Insect Biodiversity},
        author={Zahra Gharaee and Scott C. Lowe and ZeMing Gong and Pablo Millan Arias
            and Nicholas Pellegrino and Austin T. Wang and Joakim Bruslund Haurum
            and Iuliia Zarubiieva and Lila Kari and Dirk Steinke and Graham W. Taylor
            and Paul Fieguth and Angel X. Chang
        },
        year={2024},
        eprint={2406.12723},
        archivePrefix={arXiv},
        primaryClass={cs.LG},
        doi={10.48550/arxiv.2406.12723},
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
