---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/audio_loader.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/danielgural/audio_loader)

# Audio Loader#

![audio_loader](https://raw.githubusercontent.com/danielgural/audio_loader/main/assets/audio.gif)

This FiftyOne plugin is a Python plugin that allows for you to load in your audio datasets as spectograms in FiftyOne!

Explore a whole new modality with FiftyOne!

# Installation#
    
    
    fiftyone plugins download https://github.com/danielgural/audio_loader
    

# Operators#

## `load_audio`#

Loads audio files in that are saved as â.wavâ files based on classification directory tree. Such as:
    
    
    <dataset_dir>/
        <classA>/
            <audio1>.wav
            <audio2>.wav
            ...
        <classB>/
            <audio1>.wav
            <audio2>.wav
            ...
        ...
    

When loading, spectograms will be created for each audio file and saved to the output directory. For example, if input directory = output directory:
    
    
    <dataset_dir>/
        <classA>/
            <audio1>.wav
            <audio2>.wav
            ...
        <classsA_spectograms>/
            <spectogram1>.png
            <spectogram2>.png
            ...
        <classB>/
            <audio1>.wav
            <audio2>.wav
            ...
        <classsB_spectograms>/
            <spectogram1>.png
            <spectogram2>.png
            ...
        ...
    

Additionally, frame_rate, duration, channels, sample_width, and total_frame_count will be added as fields to the sample as well!

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
