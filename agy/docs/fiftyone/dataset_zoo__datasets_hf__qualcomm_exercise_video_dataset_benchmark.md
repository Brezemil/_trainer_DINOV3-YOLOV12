---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/qualcomm_exercise_video_dataset_benchmark.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/qualcomm-exercise-video-dataset-benchmark)

# Dataset Card for Qualcomm Exercise Video Dataset (Benchmark)#

This is the benchmark split of the dataset [as described here](https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/QSC-QEVD-FIT-COACH-Dataset-Download-Instructions.pdf)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 74 samples.

![image/png](https://huggingface.co/datasets/Voxel51/qualcomm-exercise-video-dataset-benchmark/resolve/main/qevd.gif)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/qualcomm-exercise-video-dataset-benchmark")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# QEVD-FIT-COACH-Benchmark Dataset Card#

## Dataset Details#

### Dataset Description#

The QEVD-FIT-COACH-Benchmark dataset contains 74 workout video sessions with real-time AI fitness coaching feedback. Each session is approximately 2.5-3 minutes long and features a single participant performing 4-5 different exercises with continuous feedback from an AI fitness coach.

The dataset includes temporal annotations for feedback events, including exercise transitions, form corrections, encouragement, and repetition counting. All feedback is aligned with video frames and includes precise timing information.

  * **Curated by:** Qualcomm (based on dataset naming)

  * **Language(s):** English (en)

  * **License:** (Qualcomm Data Research License)[https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Dataset-Research-License-Feb-25-2025.pdf]

  * **Format:** MP4 videos (H.264/AVC codec, 640x360 resolution, 30 FPS) with JSON annotations




### Dataset Sources#

  * **Repository:** https://www.qualcomm.com/developer/software/qevd-dataset

  * **Paper:** https://arxiv.org/pdf/2407.08101v2

  * **Dataset Type:** Video + Temporal Annotations




## Dataset Statistics#

  * **Total Videos:** 74 workout sessions

  * **Total Duration:** ~195 minutes (3.2 hours)

  * **Video Duration:** 150-166 seconds per session (avg: 158s)

  * **Total Feedback Events:** 2,511 temporal detections

    * **Exercise Transitions:** 498 events

    * **Regular Feedback:** 2,013 events (corrections, encouragement, counting)

  * **Unique Feedback Messages:** 1,592 distinct messages

  * **Average Feedback per Session:** 33.9 events




### Video Specifications#

  * **Resolution:** 640x360 pixels (16:9 aspect ratio)

  * **Frame Rate:** 30 FPS

  * **Codec:** H.264/AVC (avc1) - re-encoded from MPEG-4 Part 2

  * **Container:** MP4

  * **Audio:** None (video only)

  * **Average Frames per Video:** ~4,740 frames




## Uses#

### Direct Use#

This dataset is suitable for:

  1. **Video Understanding Research**

     * Temporal action detection and localization

     * Activity recognition in fitness/exercise contexts

     * Video-text alignment and grounding

  2. **Fitness AI Development**

     * Training models for automated form correction

     * Exercise recognition and classification

     * Real-time feedback generation systems

  3. **Human-Computer Interaction**

     * Conversational AI for fitness coaching

     * Multimodal interaction studies

     * Feedback timing and delivery analysis

  4. **Computer Vision Applications**

     * Pose estimation evaluation

     * Action segmentation

     * Temporal event detection




## Dataset Structure#

### FiftyOne Format#

The dataset is structured as a FiftyOne video dataset with temporal detections:
    
    
    Sample {
        'id': ObjectId,
        'filepath': str,  # Path to MP4 video file
        'video_id': str,  # Video identifier (e.g., '0006')
        'metadata': VideoMetadata {
            'duration': float,  # Duration in seconds
            'frame_rate': float,  # 30.0 FPS
            'frame_width': int,  # 640 pixels
            'frame_height': int,  # 360 pixels
            'total_frame_count': int,  # ~4,740 frames
            'encoding_str': str,  # 'avc1' (H.264)
            'mime_type': str,  # 'video/mp4'
        },
        'feedback_events': TemporalDetections {
            'detections': [
                TemporalDetection {
                    'label': str,  # Feedback text
                    'support': [int, int],  # [start_frame, end_frame]
                    'confidence': float,  # 1.0 (ground truth)
                    'is_transition': bool,  # True for exercise changes
                    'feedback_type': str,  # 'transition' or 'feedback'
                },
                ...
            ]
        },
        'transitions': TemporalDetections,  # Subset: transitions only
        'feedbacks': TemporalDetections,  # Subset: regular feedback only
        'num_feedback_events': int,  # Total count
        'num_transitions': int,  # Transition count
        'num_feedbacks': int,  # Regular feedback count
    }
    

### Temporal Detection Format#

Each temporal detection represents a feedback event with:

  * **Frame-based timing:** `support` field contains `[start_frame, end_frame]`

  * **Time-based timing:** Can be calculated as `frame / fps` to get seconds

  * **Feedback text:** The actual coaching message

  * **Type classification:** Transition vs. regular feedback




**Example:**
    
    
    Frame range: [397, 460]
    Time range: 13.23s - 15.33s
    Label: "First up are high knees!"
    Type: transition
    

### Feedback Categories#

The dataset contains four main types of feedback:

  1. **Exercise Transitions (498 events)**

     * Announce new exercises or session end

     * Examples: âFirst up are high knees!â, âMoving on to squats!â, âThatâs the end of the session.â

  2. **Form Corrections**

     * Real-time technique feedback

     * Examples: âYour stance is too narrow!â, âTighten your core!â, âWrong leg pal!â

  3. **Encouragement**

     * Motivation and positive reinforcement

     * Examples: âNice!â, âYou crushed it!â, âLove the high knees!â

  4. **Counting**

     * Repetition tracking

     * Examples: â10â, âWe are at 5 reps!â, â20â




### Exercise Types#

Common exercises in the dataset include:

  * High knees

  * Jumping jacks

  * Squats (regular, jumps, kicks)

  * Pushups

  * Butt kickers

  * Mountain climbers

  * Lunges (walking, jumps)

  * Planks (regular, moving, taps)

  * Stretches (quad, arm cross chest)

  * And moreâ¦




## Dataset Creation#

### Curation Rationale#

The dataset was created to benchmark AI fitness coaching systems, particularly for:

  * Evaluating temporal feedback generation

  * Testing exercise recognition accuracy

  * Assessing form correction capabilities

  * Measuring real-time interaction quality




### Source Data#

#### Data Collection and Processing#

  * **Recording Setup:** Controlled environment with single participant

  * **Video Format:** Originally MPEG-4 Part 2, re-encoded to H.264 for compatibility

  * **Session Structure:** Each session contains 4-5 exercises performed sequentially

  * **Duration:** Sessions are approximately 2.5-3 minutes each

  * **Frame Alignment:** Feedback annotations are frame-synchronized with video




#### Data Processing Pipeline#

  1. **Original Format:** JSON annotations + MP4 videos + NumPy timestamp files

  2. **Frame Alignment:** Feedback array pre-aligned with video frames

  3. **Temporal Detection Extraction:** Contiguous frame ranges identified for each feedback

  4. **Video Re-encoding:** Converted from MPEG-4 to H.264 for browser compatibility

  5. **FiftyOne Integration:** Structured as temporal detection dataset




### Annotations#

#### Annotation Process#

  * **Annotation Type:** Temporal feedback events with frame-level precision

  * **Alignment Method:** Frame-by-frame feedback array synchronized with video

  * **Timestamp Format:** UNIX timestamps (seconds since epoch) for reference

  * **Quality:** Ground truth annotations (confidence = 1.0)




#### Annotation Fields#

  * `feedbacks`: Frame-by-frame feedback array (aligned with video frames)

  * `feedback_timestamps`: UNIX timestamps for each unique feedback event

  * `is_transition`: Boolean flags indicating exercise transitions

  * `video_timestamps`: Frame-level UNIX timestamps in nanoseconds




#### Personal and Sensitive Information#

  * **Contains:** Video recordings of human subjects performing exercises

  * **Identifiable Information:** Visual appearance of participants

  * **Privacy Considerations:** Videos show individuals in workout clothing performing exercises

  * **Anonymization:** No explicit anonymization mentioned in source data




## Citation#
    
    
    @inproceedings{livefit,
       title = {Live Fitness Coaching as a Testbed for Situated Interaction},
       author = {Sunny Panchal and Apratim Bhattacharyya and Guillaume Berger and Antoine Mercier and Cornelius B{\"{o}}hm and Florian Dietrichkeit and Reza Pourreza and Xuanlin Li and Pulkit Madan and Mingu Lee and Mark Todorovich and Ingo Bax and Roland Memisevic},
       booktitle = {NeurIPS (D&B Track)},
       year = {2024},
    }
    

### APA#

Panchal, S., Bhattacharyya, A., Berger, G., Mercier, A., BÃ¶hm, C., Dietrichkeit, F., Pourreza, R., Li, X., Maden, P., Lee, M., Todorovich, M., Bax, I., Memisevic, R. (2024) Live Fitness Coaching as a Testbed for Situated Interaction

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
