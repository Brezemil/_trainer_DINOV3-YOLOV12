---
source_url: https://docs.voxel51.com/model_zoo/models/plugin_model_cards.html
---

**nvidia/LocateAnything-3B**

NVIDIA LocateAnything-3B\: open-vocabulary grounding VLM (3B params, Qwen2.5-3B + MoonViT + Parallel Box Decoder). Image and (frame-sampled) video. 7 operations\: detect, grounding, point, scene_text, layout, text_grounding, gui_box. Returns fo.Detections or fo.Keypoints (image), {frame\: label} (video).

Detection,Keypoints,Grounding,Ocr,Layout,Gui,PyTorch,Zero-shot,Image,Video,Vlm,Open-vocabulary,Plugin

**Qwen/Qwen3-VL-8B-Instruct**

Qwen3-VL is a multimodal vision-language model that processes and understands both text and visual input, enabling it to analyze images, video, and perform advanced reasoning and tasks involving both modalities.

Classification,Detections,PyTorch,Temporal-detections,Zero-shot,Video,Embeddings,Plugin

**Qwen/Qwen3-VL-4B-Instruct**

Qwen3-VL is a multimodal vision-language model that processes and understands both text and visual input, enabling it to analyze images, video, and perform advanced reasoning and tasks involving both modalities.

Classification,Detections,PyTorch,Temporal-detections,Zero-shot,Video,Embeddings,Plugin

**Qwen/Qwen3-VL-2B-Instruct**

Qwen3-VL is a multimodal vision-language model that processes and understands both text and visual input, enabling it to analyze images, video, and perform advanced reasoning and tasks involving both modalities.

Classification,Detections,PyTorch,Temporal-detections,Zero-shot,Video,Embeddings,Plugin

**nv_labs/c-radio_v4-h**

C-RADIOv4-H (631M params) - Visual feature extraction model using multi-teacher distillation from SigLIP2, DINOv3, and SAM3. Generates image embeddings and spatial attention features.

Embeddings,Heatmap,Plugin

**nv_labs/c-radio_v4-so400m**

C-RADIOv4-SO400M (412M params) - Efficient visual feature extraction model. Competitive with ViT-H at lower computational cost.

Embeddings,Heatmap,Plugin

**nomic-ai/nomic-embed-multimodal-7b**

nomic-embed-multimodal-7b is a dense state-of-the-art multimodal embedding model that excels at visual document retrieval tasks.

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**nomic-ai/nomic-embed-multimodal-3b**

nomic-embed-multimodal-3b is a dense state-of-the-art multimodal embedding model that excels at visual document retrieval tasks.

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**FriedFeid/oVDA-c16**

Online Video Depth Anything (cache_size=16). Estimates temporally-consistent monocular depth for videos using a DINOv2 backbone with a rolling temporal cache. Outputs per-frame fo.Heatmap depth maps normalised to [0, 1].

Depth-estimation,Video,Temporal,Heatmap,Plugin

**FriedFeid/oVDA-c8**

Online Video Depth Anything (cache_size=8). Lighter variant with a smaller temporal cache; faster and lower memory than c16 at some cost to temporal consistency.

Depth-estimation,Video,Temporal,Heatmap,Plugin

**google/Gemini-Vision**

Gemini Vision remote model for VQA via Google Gemini API

Gemini,Vision,Vqa,Multimodal,Plugin

**jinaai/jina-embeddings-v4**

jina-embeddings-v4 is a universal embedding model for multimodal and multilingual retrieval. The model is specially designed for complex document retrieval, including visually rich documents with charts, tables, and illustrations.

Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**moondream/moondream3-preview**

Moondream 3 (Preview) is an vision language model with a mixture-of-experts architecture (9B total parameters, 2B active).

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**nv_labs/c-radio_v3-g**

C-RADIOv3-g model (ViT-H/14)

Embeddings,Heatmap,Plugin

**nv_labs/c-radio_v3-h**

C-RADIOv3-H model (ViT-H/16)

Embeddings,Heatmap,Plugin

**nv_labs/c-radio_v3-l**

C-RADIOv3-L model (ViT-L/16))

Embeddings,Heatmap,Plugin

**nv_labs/c-radio_v3-b**

C-RADIOv3-B model (ViT-B/16)

Embeddings,Heatmap,Plugin

**Qwen/Qwen3-VL-Embedding-8B**

Qwen3-VL-Embedding Specifically designed for multimodal information retrieval and cross-modal understanding, this suite accepts diverse inputs including text, images, screenshots, and videos, as well as inputs containing a mixture of these modalities

Classification,PyTorch,Zero-shot,Video,Embeddings,Plugin

**Qwen/Qwen3-VL-Embedding-2B**

Qwen3-VL-Embedding Specifically designed for multimodal information retrieval and cross-modal understanding, this suite accepts diverse inputs including text, images, screenshots, and videos, as well as inputs containing a mixture of these modalities

Classification,PyTorch,Zero-shot,Video,Embeddings,Plugin

**Qwen/Qwen3.5-35B-A3B-FP8**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-27B**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-27B-FP8**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-9B**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-4B**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-2B**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**Qwen/Qwen3.5-0.8B**

Qwen3.5 is a multimodal vision-language model supporting images and videos. Image operations\: detect, point, classify, vqa, detect_3d. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,3d-detection,Plugin

**google/gemma-4-E2B-it**

Gemma 4 E2B is a 2.3B effective parameter multimodal model supporting text, image, video, and audio. Image operations\: detect, point, classify, vqa. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,Vlm,Plugin

**google/gemma-4-E4B-it**

Gemma 4 E4B is a 4.5B effective parameter multimodal model supporting text, image, video, and audio. Image operations\: detect, point, classify, vqa. Video operations\: description, temporal_localization, tracking, ocr, comprehensive, custom.

Detection,Classification,Keypoints,Vqa,Temporal-detections,PyTorch,Zero-shot,Image,Video,Vlm,Plugin

**google/gemma-4-26B-A4B-it**

Gemma 4 26B-A4B is a 3.8B active parameter (25.2B total) MoE multimodal model supporting text and image. Image operations\: detect, point, classify, vqa. No video support.

Detection,Classification,Keypoints,Vqa,PyTorch,Zero-shot,Image,Vlm,Plugin

**google/gemma-4-31B-it**

Gemma 4 31B is a 30.7B dense multimodal model supporting text and image. Image operations\: detect, point, classify, vqa. No video support.

Detection,Classification,Keypoints,Vqa,PyTorch,Zero-shot,Image,Vlm,Plugin

**PerceptronAI/Isaac-0.2-2B-Preview**

Isaac 0.2 2B (Preview) is an open-source, 2B-parameter model built for real-world applications. Isaac 0.2 is part of Perceptron AI's family of models built to be the intelligence layer for the physical world.

Detection,Ocr,Vlm,Classification,Zero-shot,Plugin

**PerceptronAI/Isaac-0.2-1B**

Isaac 0.2 1B is an open-source, 1B-parameter model built for real-world applications. Isaac 0.2 is part of Perceptron AI's family of models built to be the intelligence layer for the physical world.

Detection,Ocr,Vlm,Classification,Zero-shot,Plugin

**allenai/MolmoPoint-8B**

MolmoPoint-8B is a vision-language model that locates and tracks objects in images and videos by pointing. For images, it returns normalized keypoint coordinates per instance. For videos, it supports frame-level tracking (follows objects over time) and sparse pointing (identifies objects across sampled frames).

Keypoints,Pointing,Tracking,Video,Vlm,Zero-shot,Image-text-to-text,Plugin

**allenai/MolmoPoint-Vid-4B**

MolmoPoint-Vid-4B is a 4B vision-language model specialised for video pointing and tracking. Given a text prompt, it returns keypoint coordinates for each matching object across video frames. Supports frame-level tracking and sparse pointing modes.

Keypoints,Pointing,Tracking,Video,Vlm,Zero-shot,Image-text-to-text,Plugin

**allenai/MolmoPoint-Img-8B**

MolmoPoint-Img-8B is a vision-language model specialised for pointing at UI elements and objects in screenshots. Given a text prompt, it returns normalized keypoint coordinates for each matching element found.

Keypoints,Pointing,Vlm,Zero-shot,Image-text-to-text,Ui,Screenshots,Plugin

**lightonai/LightOnOCR-2-1B**

LightOnOCR is a 2.1B-parameter vision-language model optimized for optical character recognition. It uses a chat-based interface to extract text from images with high accuracy across various document types, handwritten text, and scene text.

Ocr,Text-extraction,Vlm,Document-understanding,Plugin

**moonshotai/Kimi-VL-A3B-Instruct**

Kimi-VL is an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilitiesâall while activating only 2.8B parameters in its language decoder

Agentic,Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**moonshotai/Kimi-VL-A3B-Thinking**

Kimi-VL is an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilitiesâall while activating only 2.8B parameters in its language decoder

Agentic,Detection,Segmentation,Ocr,Vlm,Zero-shot,Visual-agent,Plugin

**moonshotai/Kimi-VL-A3B-Thinking-2506**

Kimi-VL is an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilitiesâall while activating only 2.8B parameters in its language decoder

Agentic,Detection,Segmentation,Ocr,Vlm,Zero-shot,Visual-agent,Plugin

**google/siglip2-base-patch16-224**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-base-patch16-256**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-base-patch16-384**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-base-patch16-512**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-large-patch16-256**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-large-patch16-384**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-large-patch16-512**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-base-patch32-256**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-giant-opt-patch16-256**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-giant-opt-patch16-384**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch14-224**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch14-384**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch16-256**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch16-384**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch16-512**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-base-patch16-naflex**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**google/siglip2-so400m-patch16-naflex**

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**allenai/Molmo2-4B**

Molmo2 is a family of open vision-language models developed by the Allen Institute for AI (Ai2) that support image, video and multi-image understanding and grounding.

PyTorch,Keypoints,Zero-shot,Video,Plugin

**allenai/Molmo2-O-7B**

Molmo2 is a family of open vision-language models developed by the Allen Institute for AI (Ai2) that support image, video and multi-image understanding and grounding.

PyTorch,Keypoints,Zero-shot,Video,Plugin

**allenai/Molmo2-8B**

Molmo2 is a family of open vision-language models developed by the Allen Institute for AI (Ai2) that support image, video and multi-image understanding and grounding.

PyTorch,Keypoints,Zero-shot,Video,Plugin

**allenai/Molmo2-VideoPoint-4B**

Molmo2 is a family of open vision-language models developed by the Allen Institute for AI (Ai2) that support image, video and multi-image understanding and grounding.

PyTorch,Keypoints,Zero-shot,Video,Plugin

**facebook/sam3**

SAM3 (Segment Anything Model 3) performs promptable segmentation on images using text or visual prompts. Supports concept segmentation (find all instances), visual segmentation (specific instances), automatic segmentation, and visual embeddings.

Embeddings,PyTorch,Zero-shot,Segmentation,Segment-anything,Detections,Instance-segmentation,Visual-prompting,Plugin

**apple/FastVLM-0.5B**

FastVLM is a vision-language model from Apple that excels at visual question answering and image classification tasks. It supports both zero-shot classification and open-ended VQA with customizable prompts.

Vision-language,Vqa,Multimodal,Transformers,PyTorch,Plugin

**apple/FastVLM-1.5B**

FastVLM is a vision-language model from Apple that excels at visual question answering and image classification tasks. It supports both zero-shot classification and open-ended VQA with customizable prompts.

Vision-language,Vqa,Multimodal,Transformers,PyTorch,Plugin

**apple/FastVLM-7B**

FastVLM is a vision-language model from Apple that excels at visual question answering and image classification tasks. It supports both zero-shot classification and open-ended VQA with customizable prompts.

Vision-language,Vqa,Multimodal,Transformers,PyTorch,Plugin

**zai-org/GLM-OCR**

GLM-OCR is a vision-language model for document understanding. Supports text recognition, formula recognition, table recognition, and custom structured extraction via JSON prompts.

Ocr,Document-understanding,Visual-document-retrieval,Plugin

**microsoft/GUI-Actor-3B-Qwen2.5-VL**

GUI-Actor is Coordinate-Free Visual Grounding for GUI Agents

Keypoints,Visual-agent,Plugin

**microsoft/GUI-Actor-7B-Qwen2.5-VL**

GUI-Actor is Coordinate-Free Visual Grounding for GUI Agents

Keypoints,Visual-agent,Plugin

**google/medgemma-1.5-4b-it**

MedGemma 1.5 4B is an updated version of the MedGemma 1 4B model. MedGemma is a collection of Gemma 3 variants that are trained for performance on medical text and image comprehension

Vlm,Zero-shot,Plugin

**PerceptronAI/Isaac-0.1**

Isaac 0.1 is an open-source, 2B-parameter model built for real-world applications. Isaac 0.1 is the first in Perceptron AI's family of models built to be the intelligence layer for the physical world.

Detection,Ocr,Vlm,Classification,Zero-shot,Plugin

**Apple/SHARP**

SHARP is an approach to photorealistic view synthesis from a single image. Given a single photograph, SHARP regresses the parameters of a 3D Gaussian representation of the depicted scene.

Threed,Plugin

**opendatalab/MinerU2.5-2509-1.2B**

MinerU2.5 is a 1.2B-parameter vision-language model for document parsing. It adopts a two-stage parsing strategy\: first conducting efficient global layout analysis on downsampled images, then performing fine-grained content recognition on native-resolution crops for text, formulas, and tables.

Detection,Ocr,Vlm,Plugin

**nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1**

Llama Nemotron Nano VL is a leading document intelligence vision language model (VLMs) that enables the ability to query and summarize images from the physical or virtual world.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**facebook/VGGT-1B**

Visual Geometry Grounded Transformer (VGGT) is a feed-forward neural network that directly infers all key 3D attributes of a scene.

Depth,Threed,Keypoints,Plugin

**google/medsiglip-448**

MedSigLIP is a variant of SigLIP that is trained to encode medical images and text into a common embedding space.

Classification,Logits,Embeddings,PyTorch,Clip,Zero-shot,Plugin

**nanonets/Nanonets-OCR2-3B**

Nanonets-OCR2 are image-to-markdown OCR models that go far beyond traditional text extraction. It transforms documents into structured markdown with intelligent content recognition and semantic tagging, making it ideal for downstream processing by Large Language Models (LLMs).

Detection,Ocr,Vlm,Plugin

**allenai/olmOCR-2-7B-1025**

olmOCR-2 is an advanced OCR model from AllenAI that uses Qwen2.5-VL architecture for document text extraction. Returns markdown output with YAML front matter containing document metadata (language, rotation, tables, diagrams). Converts equations to LaTeX and tables to HTML.

Ocr,Document-understanding,Vlm,Vision-language,Plugin

**deepseek-ai/DeepSeek-OCR**

DeepSeek-OCR is an open-source vision-language model (VLM) developed by DeepSeek to perform optical character recognition (OCR) and context compression for long and complex documents

Detection,Ocr,Vlm,Plugin

**microsoft/kosmos-2.5**

Kosmos-2.5 is a multimodal literate model for machine reading of text-intensive images.

Detection,Ocr,Vlm,Plugin

**google/medgemma-4b-it**

MedGemma is a collection of Gemma 3 variants that are trained for performance on medical text and image comprehension

Vlm,Zero-shot,Plugin

**ModernVBERT/bimodernvbert**

The ModernVBERT suite is a suite of compact 250M-parameter vision-language encoders. BiModernVBERT is the bi-encoder version that is fine-tuned for visual document retrieval tasks.

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**ModernVBERT/colmodernvbert**

The ModernVBERT suite is a suite of compact 250M-parameter vision-language encoders. ColModernVBERT is the late-interaction version that is fine-tuned for visual document retrieval tasks, the most performant model on this task.

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**vidore/colqwen2.5-v0.2**

ColQwen is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features. It is a Qwen2.5-VL-3B extension that generates ColBERT- style multi-vector representations of text and images.

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**ByteDance-Seed/UI-TARS-1.5-7B**

UI-TARS-1.5 is an open-source multimodal agent capable of effectively performing diverse tasks within virtual worlds.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**vidore/colpali-v1.3-merged**

ColPali is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features. It is a PaliGemma-3B extension that generates ColBERT- style multi-vector representations of text and images

Classification,Logits,Embeddings,PyTorch,Visual-document-retrieval,Zero-shot,Plugin

**google/paligemma2-3b-mix-448**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**google/paligemma2-10b-mix-448**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**google/paligemma2-28b-mix-448**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**google/paligemma2-3b-mix-224**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**google/paligemma2-10b-mix-224**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**google/paligemma2-28b-mix-224**

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**openbmb/MiniCPM-V-4_5**

MiniCPM-V 4.5 is the latest and most capable model in the MiniCPM-V series. The model is built on Qwen3-8B and SigLIP2-400M with a total of 8B parameters.

Detection,Keypoints,Ocr,Vlm,Classification,Zero-shot,Plugin

**vikhyatk/moondream2**

Moondream is a small vision language model designed to run efficiently on edge devices.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**microsoft/Florence-2-base**

Florence-2 is a vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks (https\://arxiv.org/abs/2311.06242).

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**microsoft/Florence-2-large**

Florence-2 is a vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks (https\://arxiv.org/abs/2311.06242).

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**microsoft/Florence-2-base-ft**

Florence-2 is a vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks (https\://arxiv.org/abs/2311.06242).

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**microsoft/Florence-2-large-ft**

Florence-2 is a vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks (https\://arxiv.org/abs/2311.06242).

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**showlab/ShowUI-2B**

ShowUI is a lightweight (2B) vision-language-action model designed for GUI agents.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**XiaomiMiMo/MiMo-VL-7B-RL**

MiMo-VL-7B is a compact yet powerful vision-language model developed through extensive pre-training and reinforcement learning to achieve state-of-the-art performance on a variety of visual-language tasks.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**XiaomiMiMo/MiMo-VL-7B-SFT**

MiMo-VL-7B is a compact yet powerful vision-language model developed through extensive pre-training and reinforcement learning to achieve state-of-the-art performance on a variety of visual-language tasks.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**XiaomiMiMo/MiMo-VL-7B-SFT-GGUF**

MiMo-VL-7B is a compact yet powerful vision-language model developed through extensive pre-training and reinforcement learning to achieve state-of-the-art performance on a variety of visual-language tasks.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**OS-Copilot/OS-Atlas-Base-7B**

OS-Atlas provides a series of models specifically designed for GUI agents.

Detection,Ocr,Vlm,Classification,Zero-shot,Visual-agent,Plugin

**Qwen/Qwen2.5-VL-3B-Instruct**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Ocr,Vlm,Classification,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-3B-Instruct-AWQ**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-7B-Instruct**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-7B-Instruct-AWQ**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-32B-Instruct**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-32B-Instruct-AWQ**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-72B-Instruct**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**Qwen/Qwen2.5-VL-72B-Instruct-AWQ**

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud.

Detection,Segmentation,Ocr,Vlm,Zero-shot,Plugin

**llamaindex/vdr-2b-v1**

vdr-2b-v1 is an english only embedding model designed for visual document retrieval. It encodes document page screenshots into dense single-vector representations, this will effectively allow to search and query visually rich multilingual documents without the need for any OCR, data extraction pipelines, and chunking.

Embeddings,Ocr,Vlm,Document-retrieval,Plugin

**llamaindex/vdr-2b-multi-v1**

vdr-2b-multi-v1 is a multilingual embedding model designed for visual document retrieval across multiple languages and domains. It encodes document page screenshots into dense single-vector representations, this will effectively allow to search and query visually rich multilingual documents without the need for any OCR, data extraction pipelines, and chunking. It's trained on ð®ð¹ Italian, ðªð¸ Spanish, ð¬ð§ English, ð«ð· French and ð©ðª German

Embeddings,Ocr,Vlm,Document-retrieval,Plugin

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
