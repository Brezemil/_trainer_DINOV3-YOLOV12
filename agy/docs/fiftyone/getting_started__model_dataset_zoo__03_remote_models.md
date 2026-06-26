---
source_url: https://docs.voxel51.com/getting_started/model_dataset_zoo/03_remote_models.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/model_dataset_zoo/03_remote_models.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/model_dataset_zoo/03_remote_models.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/model_dataset_zoo/03_remote_models.ipynb)

# Exploring Remote Zoo Models#

This section walks you through the process of using **remotely-sourced models** from the FiftyOne Model Zooâmodels whose definitions are hosted on public GitHub repositories or accessible via external URLs. With this approach, you can:

  * Seamlessly integrate custom models hosted on GitHub or cloud archives
  * Reproduce and share models across teams and projects using standardized links
  * Apply these models to your datasets within FiftyOne just like built-in zoo models

FiftyOneâs flexible zoo API supports both built-in and remote models. That means whether youâre pulling a model from `voxel51/openai-clip`, `ultralytics/yolov5`, or your own repository, the workflow remains consistent and intuitive.

## In this notebook, youâll learn how to:#

  * Specify remote model sources using GitHub repos, branches, or commit references
  * Load and apply these models to your datasets
  * Visualize the predictions directly in the FiftyOne App


    
    
    [ ]:
    
    
    
    !export GITHUB_TOKEN=<your_token_here>
    

> ð¡ To use private GitHub repositories, be sure to set the `GITHUB_TOKEN` environment variable with your personal access token.
    
    
    [ ]:
    
    
    
    !pip install fiftyone torch torchvision
    

> ð¡ Before starting, ensure youâve installed the required packages:

### Using Florence2 as Remotely Sourced Zoo Model#

Original documentation of this Remotely Sourced Zoo Model is [here](https://github.com/harpreetsahota204/florence2)
    
    
    [1]:
    
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # Load a dataset
    dataset = foz.load_zoo_dataset("quickstart", overwrite=True)
    dataset=dataset.take(1)
    
    
    
    Overwriting existing directory '/home/harpreet/fiftyone/quickstart'
    Downloading dataset to '/home/harpreet/fiftyone/quickstart'
    Downloading dataset...
     100% |ââââ|  187.5Mb/187.5Mb [468.8ms elapsed, 0s remaining, 400.1Mb/s]
    Extracting dataset...
    Parsing dataset metadata
    Found 200 samples
    Dataset info written to '/home/harpreet/fiftyone/quickstart/info.json'
    Loading existing dataset 'quickstart'. To reload from disk, either delete the existing dataset or provide a custom `dataset_name` to use
    

For context, here is the first image:
    
    
    [2]:
    
    
    
    from PIL import Image
    
    Image.open(dataset.first().filepath)
    
    
    
    [2]:
    

![../../_images/getting_started_model_dataset_zoo_03_remote_models_8_0.png](../../_images/getting_started_model_dataset_zoo_03_remote_models_8_0.png)

# Setup Zoo Model#
    
    
    [ ]:
    
    
    
    foz.register_zoo_model_source("https://github.com/harpreetsahota204/florence2", overwrite=True)
    
    
    
    [ ]:
    
    
    
    foz.download_zoo_model(
        "https://github.com/harpreetsahota204/florence2",
        model_name="microsoft/Florence-2-base-ft",
    )
    
    
    
    [ ]:
    
    
    
    model = foz.load_zoo_model(
        "microsoft/Florence-2-base-ft"
        )
    

The three captioning operations require no additional arguments beyond selecting the operation type. Supported `detail_level` values:

  * `basic`
  * `detailed`
  * `more_detailed`


    
    
    [4]:
    
    
    
    model.operation="caption"
    model.detail_level= "basic"
    
    
    
    [5]:
    
    
    
    dataset.apply_model(model, label_field="captions")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [750.4ms elapsed, 0s remaining, 1.3 samples/s]
    
    
    
    [6]:
    
    
    
    dataset.first()['captions']
    
    
    
    [6]:
    
    
    
    'A birthday cake decorated with surfboards and palm trees.'
    

To change the caption detail level:
    
    
    [7]:
    
    
    
    model.detail_level= "more_detailed"
    
    dataset.apply_model(model, label_field="more_detailed_captions")
    
    dataset.first()['more_detailed_captions']
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [222.7ms elapsed, 0s remaining, 4.5 samples/s]
    
    
    
    [7]:
    
    
    
    'A birthday cake is sitting on a table. The cake is blue. There are two palm trees on top of the cake. There is a white banner on the cake with writing on it.'
    

The operations for `detection`, `dense_region_caption`, `region_proposal` donât require additional parameters for general use. However, `open_vocabulary_detection` requires a `text_prompt` parameter to guide the detection towards specific objects. The results are stored as Detections objects containing bounding boxes and labels:
    
    
    [10]:
    
    
    
    model.operation="detection"
    
    model.detection_type="open_vocabulary_detection"
    
    model.prompt="a surfboard next to palm trees"
    
    dataset.apply_model(model, label_field="ov_prompted_detection")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [108.8ms elapsed, 0s remaining, 9.2 samples/s]
    
    
    
    [11]:
    
    
    
    dataset.first()['ov_prompted_detection']
    
    
    
    [11]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9dcce1d525ba81848cc8',
                'attributes': {},
                'tags': [],
                'label': 'a surfboard next to palm trees',
                'bounding_box': [
                    0.28949998361995805,
                    0.2964999914169312,
                    0.30999999609999,
                    0.16000001430511473,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    

Or you can use the caption field:
    
    
    [12]:
    
    
    
    dataset.apply_model(model, label_field="ov_field_detection", prompt_field="captions")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [125.0ms elapsed, 0s remaining, 8.0 samples/s]
    
    
    
    [13]:
    
    
    
    dataset.first()['ov_field_detection']
    
    
    
    [13]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9dd6e1d525ba81848cc9',
                'attributes': {},
                'tags': [],
                'label': 'A birthday cake decorated with surfboards and palm trees.',
                'bounding_box': [
                    0.09549999541748827,
                    0.02449999898672104,
                    0.8030000022425058,
                    0.9640000239014626,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    

For dense detections, this runs without a prompt and returns all detectable objects.
    
    
    [14]:
    
    
    
    model.operation="detection"
    
    model.detection_type="dense_region_caption"
    
    dataset.apply_model(model, label_field="dense_detections")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [106.1ms elapsed, 0s remaining, 9.4 samples/s]
    
    
    
    [15]:
    
    
    
    dataset.first()['dense_detections']
    
    
    
    [15]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9de2e1d525ba81848cca',
                'attributes': {},
                'tags': [],
                'label': 'surfboard',
                'bounding_box': [
                    0.2914999818649536,
                    0.3644999980926514,
                    0.2639999877149686,
                    0.09099998474121093,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
            <Detection: {
                'id': '67ed9de2e1d525ba81848ccb',
                'attributes': {},
                'tags': [],
                'label': 'surfboard',
                'bounding_box': [
                    0.41449998361995805,
                    0.3014999866485596,
                    0.1830000222300569,
                    0.10799999237060547,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    

Phrase grounding requires either a direct caption or a reference to a caption field. You can provide this in two ways:
    
    
    [16]:
    
    
    
    model.operation="phrase_grounding"
    
    model.prompt="cake"
    
    dataset.apply_model(model, label_field="cap_phrase_groundings")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [84.9ms elapsed, 0s remaining, 11.8 samples/s]
    
    
    
    [17]:
    
    
    
    dataset.first()['cap_phrase_groundings']
    
    
    
    [17]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9df1e1d525ba81848ccc',
                'attributes': {},
                'tags': [],
                'label': 'cake',
                'bounding_box': [
                    0.09249999804999501,
                    0.02449999898672104,
                    0.8099999473498652,
                    0.963000001013279,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    

When you want to use a Field of a Sample for grounding, you use the following pattern:
    
    
    [18]:
    
    
    
    dataset.apply_model(model,
                        label_field="cap_field_phrase_groundings",
                        prompt_field="more_detailed_captions"
                        )
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [168.3ms elapsed, 0s remaining, 5.9 samples/s]
    
    
    
    [19]:
    
    
    
    dataset.first()['cap_field_phrase_groundings']
    
    
    
    [19]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9dfde1d525ba81848ccd',
                'attributes': {},
                'tags': [],
                'label': 'A birthday cake',
                'bounding_box': [
                    0.08950000068250175,
                    0.02249999940395355,
                    0.8179999525173784,
                    0.9650000005960464,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
            <Detection: {
                'id': '67ed9dfde1d525ba81848cce',
                'attributes': {},
                'tags': [],
                'label': 'The cake',
                'bounding_box': [
                    0.09349999717249276,
                    0.5134999752044678,
                    0.8070000231075591,
                    0.47300000190734864,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
            <Detection: {
                'id': '67ed9dfde1d525ba81848ccf',
                'attributes': {},
                'tags': [],
                'label': 'two palm trees',
                'bounding_box': [
                    0.239500003120008,
                    0.02249999940395355,
                    0.5619999699699231,
                    0.3499999910593033,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
            <Detection: {
                'id': '67ed9dfde1d525ba81848cd0',
                'attributes': {},
                'tags': [],
                'label': 'a white banner',
                'bounding_box': [
                    0.34649999453998603,
                    0.1434999942779541,
                    0.3389999828399561,
                    0.10999999046325684,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    

Segmentation requires either a direct expression or a reference to a field containing expressions. Similar to phrase grounding, you can provide this in two ways:
    
    
    [ ]:
    
    
    
    model.operation="segmentation"
    model.prompt="palm trees"
    dataset.apply_model(model, label_field="prompted_segmentations")
    
    
    
    [ ]:
    
    
    
    dataset.first()['prompted_segmentations']
    

When you want to use a Field of a Sample for grounding, you use the following pattern:
    
    
    [22]:
    
    
    
    dataset.apply_model(model, label_field="sample_field_segmentations", prompt_field="captions")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [4.7s elapsed, 0s remaining, 0.2 samples/s]
    
    
    
    [ ]:
    
    
    
    dataset.first()['sample_field_segmentations']
      
    

Basic OCR (âocrâ) requires no additional parameters and returns text strings. For OCR with region information (`ocr_with_region`), you can set `store_region_info=True` to include bounding boxes for each text region:
    
    
    [24]:
    
    
    
    model.operation="ocr"
    
    model.store_region_info=True
    
    dataset.apply_model(model, label_field="text_regions")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [220.6ms elapsed, 0s remaining, 4.5 samples/s]
    
    
    
    [25]:
    
    
    
    dataset.first()['text_regions']
    
    
    
    [25]:
    
    
    
    <Detections: {
        'detections': [
            <Detection: {
                'id': '67ed9e2de1d525ba81848cd3',
                'attributes': {},
                'tags': [],
                'label': '</s>Sweetness Bakery',
                'bounding_box': [
                    0.03249999890312219,
                    0.032499998807907104,
                    0.3559999831568319,
                    0.03899999856948853,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
            <Detection: {
                'id': '67ed9e2de1d525ba81848cd4',
                'attributes': {},
                'tags': [],
                'label': 'HAPPY 30TH BIRTHDAY',
                'bounding_box': [
                    0.38449998556996307,
                    0.17350000143051147,
                    0.2520000226200579,
                    0.049999988079071044,
                ],
                'mask': None,
                'mask_path': None,
                'confidence': None,
                'index': None,
            }>,
        ],
    }>
    
    
    
    [26]:
    
    
    
    model.store_region_info=False
    
    dataset.apply_model(model, label_field="text_regions_no_region_info")
    
    
    
     100% |âââââââââââââââââââââ| 1/1 [126.7ms elapsed, 0s remaining, 7.9 samples/s]
    
    
    
    [27]:
    
    
    
    dataset.first()['text_regions_no_region_info']
    
    
    
    [27]:
    
    
    
    'Sweetness BakeryHAPPY 30TH BIRTHDAY'
    

Remotely-sourced models expand the power and flexibility of the FiftyOne Model Zoo by allowing you to access and deploy models from external GitHub repositories or public URLs. Whether youâre leveraging a popular open-source model or integrating one from your own team, this workflow makes it easy to apply and visualize predictions in your datasets. IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
