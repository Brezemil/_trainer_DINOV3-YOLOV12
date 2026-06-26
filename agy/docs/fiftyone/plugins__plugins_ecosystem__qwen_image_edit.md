---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/qwen_image_edit.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/qwen_image_edit)

# Qwen Image Edit Panel#

![image](https://raw.githubusercontent.com/harpreetsahota204/qwen_image_edit/main/qwen_image_edit_panel.gif)

A [FiftyOne](https://docs.voxel51.com) plugin that brings chat-based image editing directly into the sample modal. Write a prompt, see all generated results inline, iterate, and save your favourite edits back to your dataset â all without leaving the app.

Inference runs **entirely on your local GPU** using the [Qwen Image Edit 2511](https://huggingface.co/drbaph/Qwen-Image-Edit-2511-FP8) model in FP8 quantized form. No API keys or external services required.

## Installation#

Download the plugin:
    
    
    fiftyone plugins download https://github.com/harpreetsahota204/qwen_image_edit --overwrite
    

Set the operator timeout **before** launching FiftyOne. The default 600-second timeout is not enough for a cold-start model load (up to ~10 min on first run) or a long multi-step inference call (1â5 min per edit depending on steps and image count):
    
    
    export FIFTYONE_OPERATOR_TIMEOUT=1800   # 30 minutes
    

Then launch the app:
    
    
    import fiftyone as fo
    import os
    
    os.environ["FIFTYONE_OPERATOR_TIMEOUT"] = "1800"
    
    dataset = fo.load_dataset("your-dataset")
    fo.launch_app(dataset)
    

Or from the shell:
    
    
    export FIFTYONE_OPERATOR_TIMEOUT=1800
    fiftyone app launch
    

> **Important:** `FIFTYONE_OPERATOR_TIMEOUT` must be set in the same environment that runs the FiftyOne server, not just the Python session that opens the browser. Per-function timeout decorators from `fiftyone.operators.decorators` use Pythonâs `signal` module and do not work in FiftyOneâs operator worker threads â the environment variable is the only supported mechanism.

* * *

## Requirements#

Requirement | Detail  
---|---  
FiftyOne |   
PyTorch | CUDA build (`torch`)  
Diffusers | `diffusers`  
Accelerate | `accelerate`  
Pillow | `Pillow`  
GPU | CUDA-capable, â¥ 80 GB VRAM recommended  
  
Install Python dependencies:
    
    
    pip install torch diffusers accelerate Pillow fiftyone
    

* * *

## What it does#

Open any sample in the FiftyOne modal and the **Qwen Image Edit** panel appears alongside it. From there you can:

  * **Prompt-driven edits** â describe the change you want in plain text and the panel runs the Qwen FP8 pipeline locally on your GPU to apply it.

  * **Multiple images per prompt** â set _Images per prompt_ to generate several variations in one call. Each is shown as a separate card so you can compare them side by side in the panel.

  * **Iterative refinement** â each edit turn is added to the panelâs history. Click the **** (set as source) button on any image â from any turn â to use it as the starting point for your next edit.

  * **Advanced controls** â optionally supply a negative prompt, override inference steps, adjust _True CFG scale_ (Qwenâs classifier-free guidance strength), and fix a random _Seed_ for reproducibility.

  * **Per-image actions** â every generated image has its own **Save** , **Trash** , and ** Set as source** buttons. Save any subset you like; trash the ones you donât want to keep.

  * **Save to dataset** â clicking Save copies the image into your datasetâs media directory and registers it as a new group slice (`edit_1`, `edit_2`, â¦). If the dataset is flat it is automatically converted to a grouped dataset on first save.

  * **Label copying** â when saving, optionally copy any label fields (detections, classifications, segmentations, etc.) from the source sample onto each new edited slice.

  * **Session memory** â your edit history for each sample is preserved in the browser session, so switching between samples and coming back doesnât lose your work.

  * **Live status** â during the first run the panel shows real-time download and GPU-loading status. During inference it shows step-level progress (e.g. `Step 11/40 (28%)`) with an elapsed-time counter.




* * *

## Model#

|   
---|---  
**Repo** | [`Qwen/Qwen-Image-Edit-2511`](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)  
**Weights** | [`drbaph/Qwen-Image-Edit-2511-FP8`](https://huggingface.co/drbaph/Qwen-Image-Edit-2511-FP8) â FP8 E4M3FN quantized transformer, ~4 GB  
**Precision** | `torch.bfloat16` compute, `torch.float8_e4m3fn` storage  
**GPU** | CUDA-capable GPU with at least 80 GB VRAM recommended  
  
The transformer weights are downloaded on the **first edit only** and cached by HuggingFace Hub (`~/.cache/huggingface/`). All subsequent runs load directly from cache. The panel shows download and loading status live while you wait.

* * *

## First-run note#

The first time you submit a prompt the panel will:

  1. Download the FP8 transformer checkpoint (~20.4 GB) from HuggingFace Hub â this is a one-time step and may take several minutes depending on your connection.

  2. Load the full pipeline onto your GPU â this can take several minutes.

  3. Begin denoising â progress is shown step by step (e.g. `Step 1/40 (2%) â¦ Step 40/40 (100%)`).




All subsequent edits in the same session skip steps 1 and 2 and go straight to inference.

* * *

## Getting Started#

If you want to quickly test the plugin, you can use the FiftyOne quickstart dataset:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

Alternatively, if you have your own dataset and want to test the plugin with your data, see the [FiftyOne documentation on importing datasets](https://docs.voxel51.com/user_guide/import_datasets.html) to learn how to load your data into FiftyOne.

## Usage#

  1. Open a dataset in the FiftyOne app and click into any sample.

  2. Open the **Qwen Image Edit** panel from the modal panel selector.

  3. _(Optional)_ Click ** Advanced** to set a negative prompt, inference steps, True CFG scale, seed, or images-per-prompt count.

  4. Type a prompt describing your edit and press **Enter** or click ****.

  5. The panel shows live status during download/loading and step-by-step progress during inference.

  6. When results appear, each generated image has three buttons:

     * **** â set this image as the source for your next edit.

     * ** Trash** â delete the temp file and remove the card.

     * ** Save** â persist the image as a new `edit_N` group slice on the dataset.

  7. Click **** on any image (including the original) to branch from it, then type a new prompt and repeat.




### Advanced parameters#

Parameter | Default | Description  
---|---|---  
Negative prompt | _(empty)_ | Concepts to suppress. Sent as a single space when blank (Qwen requires a non-empty string).  
Steps | 40 | Number of denoising steps. More steps = higher quality, slower inference.  
True CFG scale | 4.0 | Classifier-free guidance strength specific to Qwen.  
Seed | 51 | Random seed. Fix this to get reproducible results across calls.  
Images per prompt | 1 | Number of images to generate per edit. All are shown as separate cards.  
  
* * *

## Saved sample fields#

Each saved edit slice carries the following fields in addition to the image:

Field | Type | Description  
---|---|---  
`edit_prompt` | String | The prompt used for this edit.  
`edit_model` | String | Model identifier.  
`edit_negative_prompt` | String | Negative prompt (if any).  
`edit_num_inference_steps` | Int | Steps used.  
`edit_true_cfg_scale` | Float | True CFG scale used.  
`edit_seed` | Int | Seed used.  
`generation_time` | Float | Wall-clock seconds the pipeline call took.  
`edit_history` | List | Full turn history (prompt + filepath) for the session.  
`tags` | List | Always includes `"edited"`.  
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
