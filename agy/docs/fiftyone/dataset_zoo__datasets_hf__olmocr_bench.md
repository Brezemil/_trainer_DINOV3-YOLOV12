---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/olmocr_bench.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/olmOCR_bench)

# Dataset Card for olmocr-bench#

![img/png](https://huggingface.co/datasets/Voxel51/olmOCR_bench/resolve/main/olm_ocr.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7019 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/olmOCR_bench")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

Here is the completed dataset card, filled in only from what can be verified from the paper and the notebook:

* * *

# Dataset Card for olmOCR-Bench#

## Dataset Details#

### Dataset Description#

olmOCR-Bench is a curated benchmark for evaluating PDF linearization and content-extraction tools. It comprises 1,402 distinct PDF pages (each treated as a single document for evaluation purposes) paired with 7,010 binary pass/fail unit-test cases. Rather than computing soft metrics such as edit distance or ROUGE against a reference transcription, each test is a deterministic, machine-verifiable property check â analogous to a software unit test â applied to the plain-text output of any OCR or PDF-parsing system under evaluation. The benchmark spans seven document categories chosen to stress-test aspects of linearization that remain challenging even for the best commercial and open-source systems: mathematical formulas from modern arXiv preprints, mathematical formulas from old scanned textbooks, table structure accuracy, natural reading order in multi-column layouts, header/footer exclusion, text presence in long dense small-print pages, and general text extraction from historical scanned documents.

  * **Curated by:** Allen Institute for AI (AllenAI) â Jake Poznanski, Aman Rangapur, Jon Borchardt, Jason Dunkelberger, Regan Huff, Daniel Lin, Christopher Wilhelm, Kyle Lo, Luca Soldaini

  * **Funded by:** Allen Institute for AI

  * **Shared by:** Allen Institute for AI

  * **Language(s) (NLP):** en

  * **License:** Open Data Commons Family




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/allenai/olmOCR-bench

  * **Paper:** https://arxiv.org/abs/2502.18443 â _olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models_

  * **Demo:** https://olmocr.allenai.org




* * *

## Uses#

### Direct Use#

olmOCR-Bench is intended as an evaluation benchmark for any system that converts PDF pages (or images of document pages) into plain text. Suitable systems include OCR pipelines (e.g., Marker, MinerU), document-understanding vision-language models (e.g., GPT-4o, Gemini Flash, Qwen-VL), and fine-tuned linearization models. The benchmark can be used to compare systems on overall pass rate (macro-averaged across document categories) or on specific capability sub-scores (math formulas, tables, reading order, header/footer suppression, tiny-text extraction).

### Out-of-Scope Use#

  * The benchmark is **not** suitable as training data; it is a held-out evaluation set.

  * It should not be used to evaluate general document understanding beyond plain-text linearization (e.g., VQA, layout prediction).

  * Because documents are English-only and skewed towards academic, historical, and formal document types, performance on olmOCR-Bench may not generalise to other languages or informal document styles.




* * *

## Dataset Structure#

### FiftyOne Representation#

The dataset is loaded into FiftyOne as a flat collection of **7,019 samples** (one sample per test case). Because each PDF page may have multiple test cases, images are duplicated across samples that share the same page. Each sample represents a single unit test applied to a single page image.

**Media:** Each sampleâs `filepath` points to a PNG image rendered from the source PDF at **200 DPI**. Typical image dimensions are 1700 Ã 2200 px, 3 channels (RGB).

#### Fields present on every sample#

Field | Type | Description  
---|---|---  
`category` | `str` | Document category: one of `arxiv_math`, `old_scans_math`, `table_tests`, `old_scans`, `headers_footers`, `multi_column`, `long_tiny_text`  
`pdf_name` | `str` | Stem of the source PDF filename (e.g. `2503.04048_pg46`)  
`page_number` | `int` | Page number within the source PDF (always `1` for these single-page benchmark documents)  
`source_url` | `str|None` | URL of the original source document  
`tags` | `list[str]` | Two-element list: `[category, test_type]`  
`test_id` | `str` | Unique test-case identifier (e.g. `2503.04048_pg46_math_000`)  
`test_type` | `str` | Unit-test type: one of `math`, `present`, `absent`, `order`, `table`  
`max_diffs` | `int` | Maximum allowed fuzzy-match edit operations (0 = exact after normalisation)  
`verified` | `bool|None` | Whether this test case was manually verified  
  
* * *

## Dataset Creation#

### Curation Rationale#

olmOCR-Bench was created to fill a gap in evaluation methodology for PDF linearization. Existing benchmarks rely on fuzzy reference-text matching or LLM-as-judge evaluation, both of which can miss fine-grained but semantically important errors (e.g., a subtly wrong math subscript). olmOCR-Bench instead uses deterministic binary unit tests, enabling unambiguous, reproducible comparisons across heterogeneous systems. The seven document categories were chosen to capture failure modes observed during the development of olmOCR itself.

### Source Data#

#### Data Collection and Processing#

Documents were sourced from several publicly accessible repositories:

  * **arXiv Math** : Recent math-section arXiv papers with a single TeX source file. LaTeX expressions were matched back to source TeX and validated for KaTeX rendering compatibility.

  * **Old Scans Math** : Public-domain mathematics textbooks from the Internet Archive. Formula test cases were manually annotated.

  * **Tables** : Pages from an internal crawled PDF corpus, filtered for tables by Gemini Flash 2.0; cell relationships generated by Gemini Flash 2.0 and manually reviewed.

  * **Old Scans** : Historical letters and typewritten documents with pre-existing human transcriptions from the Library of Congress digital archives (https://crowd.loc.gov). Reading-order cases derived from transcriptions; header/footer cases added manually.

  * **Headers & Footers**: Pages from the internal crawled corpus; header/footer regions detected by DocLayout-YOLO, text extracted by Gemini Flash 2.0, manually reviewed.

  * **Multi-Column** : Pages from the internal crawled corpus with multi-column layouts; Claude Sonnet 3.7 rendered pages to HTML from which reading-order cases were extracted and manually reviewed.

  * **Long Tiny Text** : Dense small-print pages (dictionaries, reference sections) crawled from the Internet Archive; test cases generated by Gemini Flash 2.0 and manually verified.




All documents were decontaminated against the olmOCR-mix-0225 training set via URL-level deduplication. Documents containing PII not intended for public dissemination were removed using a GPT-4o-based filter. PDFs were converted to PNG at 200 DPI using `pdf2image` (Poppler backend).

#### Who are the source data producers?#

  * **arXiv Math** : Authors of recent mathematics preprints on arXiv.

  * **Old Scans Math** : Authors of historical public-domain mathematics textbooks.

  * **Tables, Headers/Footers, Multi-Column** : Authors of publicly crawled web documents (diverse, unidentified).

  * **Old Scans** : Historical correspondents and typists; transcriptions by Library of Congress crowdsourcing volunteers.

  * **Long Tiny Text** : Authors and publishers of public-domain dense-print documents on the Internet Archive.




### Annotations#

#### Annotation process#

Test cases were produced through a combination of automated generation and human review:

  * arXiv math expressions: algorithmically matched from TeX source, manually verified.

  * Old-scan math expressions: manually annotated.

  * Table cell relationships: generated by Gemini Flash 2.0, manually reviewed.

  * Reading-order cases (old scans): algorithmically derived from existing human transcriptions, manually reviewed.

  * Header/footer snippets: extracted by Gemini Flash 2.0, manually reviewed.

  * Multi-column reading-order cases: extracted from Claude Sonnet 3.7 HTML renderings, manually reviewed.

  * Long-tiny-text presence cases: generated by Gemini Flash 2.0, manually verified.




Every category underwent at least one round of manual human review. The `verified` field on each FiftyOne sample records whether a test case passed this check.

#### Who are the annotators?#

Members of the Allen Institute for AI research team, assisted by GPT-4o, Gemini Flash 2.0, and Claude Sonnet 3.7 for semi-automated case generation.

#### Personal and Sensitive Information#

The authors screened for PII using a GPT-4o classifier and removed non-public documents. The historical Library of Congress documents may contain names of historical figures, but these are already part of the public record.

* * *

## Bias, Risks, and Limitations#

  * **Language** : English only. Performance does not indicate capability on non-English documents.

  * **Domain skew** : Heavily weighted toward academic, historical, and formal web documents.

  * **Math evaluation** : Assessed via KaTeX symbol bounding-box relationships, not semantic equivalence. Equivalent expressions in different notation may score as failures.

  * **Table evaluation** : Only Markdown and HTML formats are checked; HTML is required for rowspan/colspan tests.

  * **Resolution** : PDFs rendered at 200 DPI; systems ingesting the original PDF binary may behave differently.

  * **Benchmark-model leakage** : URL-level decontamination against olmOCR-mix-0225 was performed, but overlap with third-party model training data cannot be ruled out.




### Recommendations#

Report per-category scores alongside the macro-averaged overall score; aggregate performance can mask category-specific weaknesses. Treat results as specific to English-language formal documents in the covered categories.

## Citation#

**BibTeX:**
    
    
    @article{poznanski2025olmocr,
      title   = {olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models},
      author  = {Poznanski, Jake and Rangapur, Aman and Borchardt, Jon and Dunkelberger, Jason
                 and Huff, Regan and Lin, Daniel and Wilhelm, Christopher and Lo, Kyle and Soldaini, Luca},
      journal = {arXiv preprint arXiv:2502.18443},
      year    = {2025},
      url     = {https://arxiv.org/abs/2502.18443}
    }
    

**APA:**

Poznanski, J., Rangapur, A., Borchardt, J., Dunkelberger, J., Huff, R., Lin, D., Wilhelm, C., Lo, K., & Soldaini, L. (2025). _olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models_. arXiv preprint arXiv:2502.18443. https://arxiv.org/abs/2502.18443

* * *

## More Information#

  * olmOCR code and model weights: https://github.com/allenai/olmocr

  * olmOCR-mix-0225 training data: https://huggingface.co/datasets/allenai/olmOCR-mix-0225




## Dataset Card Authors#

Dataset card written from the olmOCR paper (arXiv:2502.18443) and inspection of the `allenai/olmOCR-bench` HuggingFace repository and FiftyOne parsing code in `scratch.ipynb`.

## Dataset Card Contact#

For questions about the benchmark, contact the Allen Institute for AI: `{jakep|kylel|lucas}@allenai.org`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
