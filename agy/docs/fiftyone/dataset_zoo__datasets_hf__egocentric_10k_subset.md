---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/egocentric_10k_subset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Egocentric_10K_subset)

# Dataset Card for Egocentric 10K (subset - Factory 51, first 51 videos)#

![image/png](https://huggingface.co/datasets/Voxel51/Egocentric_10K_subset/resolve/main/egocentric10_subset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 416 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/Egocentric_10K_subset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

Hereâs a filled-out dataset card for your Factory 51 subset:

## Dataset Details#

### Dataset Description#

This is a curated subset of the Egocentric-10K dataset, focusing exclusively on Factory 51 with limited video sequences per worker. The subset contains egocentric video data captured from head-mounted cameras worn by factory workers during their daily tasks, providing first-person perspective footage of real manufacturing environments and hand-object interactions.

The subset includes the first 51 video clips (indices 0-50) from each worker in Factory 51, making it a more manageable dataset for research, development, and prototyping while maintaining the diversity of worker perspectives and temporal coverage.

  * **Curated by:** Build AI (original dataset)

  * **Funded by:** Build AI (original dataset)

  * **Language(s) (NLP):** N/A (video dataset, no speech/text)

  * **License:** Apache 2.0




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/builddotai/Egocentric-10K (original dataset)




## Uses#

### Direct Use#

This dataset subset is suitable for:

  * **Egocentric vision research** : Developing and testing algorithms for first-person video understanding

  * **Hand detection and tracking** : Training models to detect and track hands in industrial environments

  * **Action recognition** : Recognizing manipulation actions and work activities in factory settings

  * **Object interaction analysis** : Understanding how workers interact with tools and materials

  * **Temporal action segmentation** : Segmenting continuous work activities into discrete actions

  * **Prototyping and development** : Testing computer vision pipelines on real-world industrial data with manageable dataset size

  * **Educational purposes** : Teaching egocentric vision concepts with authentic factory footage

  * **Transfer learning** : Pre-training or fine-tuning models for industrial or egocentric vision tasks




### Out-of-Scope Use#

This dataset should not be used for:

  * **Worker surveillance or monitoring** : The dataset is intended for research purposes, not for tracking individual worker productivity or behavior

  * **Performance evaluation of individual workers** : Videos should not be used to assess or compare worker performance

  * **Biometric identification** : The dataset should not be used to develop facial recognition or worker identification systems

  * **Safety compliance enforcement** : While useful for safety research, it should not be used punitively

  * **Generalization to all factories** : This is data from a single factory (Factory 51) and may not represent all manufacturing environments

  * **Real-time production systems without validation** : Models trained on this subset should be thoroughly validated before deployment




## Dataset Structure#

The dataset is organized as a FiftyOne video dataset with the following structure:

### Fields#

Each video sample contains:

  * **filepath** : Path to the MP4 video file

  * **metadata** : VideoMetadata object containing:

    * `size_bytes`: File size in bytes

    * `mime_type`: âvideo/mp4â

    * `frame_width`: 1920 pixels

    * `frame_height`: 1080 pixels

    * `frame_rate`: 30.0 fps

    * `duration`: Video duration in seconds

    * `encoding_str`: âh265â (H.265/HEVC codec)

  * **worker_id** : Unique identifier for the worker (e.g., âworker_001â, âworker_002â, etc.)

  * **video_index** : Sequential index of the video for that worker (0-50)

  * **factory_id** : âfactory_051â (constant for this subset)




### Statistics#

  * **Factory** : 1 (Factory 51 only)

  * **Workers** : 8 workers (worker_001 through worker_008)

  * **Videos per worker** : Up to 51 (indices 0-51)

  * **Total videos** : 408 video clips

  * **Resolution** : 1080p (1920x1080)

  * **Frame rate** : 30 fps

  * **Video codec** : H.265/HEVC

  * **Format** : MP4

  * **Field of view** : 128Â° horizontal, 67Â° vertical

  * **Camera type** : Monocular head-mounted (Build AI Gen 1)

  * **Audio** : No




## Dataset Creation#

### Curation Rationale#

This subset was created to provide a more manageable version of the Egocentric-10K dataset for researchers and developers who:

  * Need a representative sample of factory egocentric video data

  * Have limited computational resources or storage capacity

  * Want to prototype and test algorithms before scaling to the full dataset

  * Require data from a single factory environment for controlled experiments

  * Need temporal coverage (51 sequential videos per worker) without the full dataset size




By limiting to Factory 51 and the first 51 videos per worker, this subset maintains:

  * **Temporal diversity** : Sequential videos capture different times and activities

  * **Worker diversity** : Multiple workers provide varied perspectives and work styles

  * **Environmental consistency** : Single factory reduces environmental variability

  * **Manageable scale** : Suitable for development and testing workflows




### Source Data#

#### Data Collection and Processing#

**Original Data Collection** (by Build AI):

  * Videos captured using Build AI Gen 1 head-mounted cameras

  * Recorded in Factory 51 during normal work operations

  * Workers wore monocular cameras with 128Â° horizontal FOV

  * Captured at 1080p resolution, 30 fps

  * Encoded in H.265/HEVC for efficient storage

  * No audio recorded




**Subset Curation Process** :

  1. Downloaded Factory 51 data from Hugging Face: `https://huggingface.co/datasets/builddotai/Egocentric-10K/tree/main/factory_051`

  2. Extracted tar archives containing video and metadata pairs

  3. Filtered to retain only videos with `video_index` 0-50 (first 51 videos per worker)

  4. Deleted videos with `video_index` > 50

  5. Organized into FiftyOne dataset structure with metadata preservation




### Recommendations#

Users should:

  * **Validate on diverse data** : Test models on data from other factories, environments, and contexts before deployment

  * **Consider ethical implications** : Use data responsibly and avoid surveillance or punitive applications

  * **Acknowledge limitations** : Report the single-factory, limited-temporal nature of the subset in publications

  * **Respect privacy** : Implement additional privacy protections if sharing derived data or visualizations

  * **Supplement with annotations** : Consider adding task-specific annotations for supervised learning applications

  * **Combine with other datasets** : Use alongside other egocentric datasets (Ego4D, EPIC-KITCHENS, etc.) for robustness

  * **Monitor for bias** : Evaluate models for fairness across different worker characteristics and conditions




## Citation#
    
    
    @dataset{buildaiegocentric10k2025,
      author = {Build AI},
      title = {Egocentric-10K},
      year = {2025},
      publisher = {Hugging Face Datasets},
      url = {https://huggingface.co/datasets/builddotai/Egocentric-10K}
    }
    

**APA:**

Build AI. (2025). _Egocentric-10K_ [Dataset]. Hugging Face Datasets. https://huggingface.co/datasets/builddotai/Egocentric-10K

## More Information#

For more information about the original Egocentric-10K dataset:

  * **Dataset page** : https://huggingface.co/datasets/builddotai/Egocentric-10K

  * **Evaluation set** : https://huggingface.co/datasets/builddotai/Egocentric-10K-Evaluation

  * **Build AI** : https://build.ai




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
