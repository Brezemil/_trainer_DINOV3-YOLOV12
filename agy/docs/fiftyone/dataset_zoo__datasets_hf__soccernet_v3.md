---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/soccernet_v3.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/SoccerNet-V3)

# Dataset Card for SoccerNet-V3#

SoccerNet is a large-scale dataset for soccer video understanding. It has evolved over the years to include various tasks such as action spotting, camera calibration, player re-identification and tracking. It is composed of 550 complete broadcast soccer games and 12 single camera games taken from the major European leagues. SoccerNet is not only dataset, but also yearly challenges where the best teams compete at the international level.

![image/png](https://huggingface.co/datasets/Voxel51/SoccerNet-V3/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1799 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/SoccerNet-V3")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Language(s) (NLP):** en

  * **License:** mit




### Dataset Sources#

  * **Repository:** https://github.com/SoccerNet

  * **Paper** [SoccerNet 2023 Challenges Results](https://arxiv.org/abs/2309.06006)

  * **Demo:** https://try.fiftyone.ai/datasets/soccernet-v3/samples

  * **Homepage** https://www.soccer-net.org/




## Dataset Creation#

Dataset Authors:

Copyright (c) 2021 holders:

  * University of LiÃ¨ge (ULiÃ¨ge), Belgium.

  * King Abdullah University of Science and Technology (KAUST), Saudi Arabia.

  * Marc Van Droogenbroeck (M.VanDroogenbroeck@uliege.be), Professor at the University of LiÃ¨ge (ULiÃ¨ge).




Code Contributing Authors:

  * Anthony Cioppa (anthony.cioppa@uliege.be), University of LiÃ¨ge (ULiÃ¨ge), Montefiore Institute, TELIM.

  * Adrien DeliÃ¨ge (adrien.deliege@uliege.be), University of LiÃ¨ge (ULiÃ¨ge), Montefiore Institute, TELIM.

  * Silvio Giancola (silvio.giancola@kaust.edu.sa), King Abdullah University of Science and Technology (KAUST), Image and Video Understanding Laboratory (IVUL), part of the Visual Computing Center (VCC).




Supervision from:

  * Bernard Ghanem, King Abdullah University of Science and Technology (KAUST).

  * Marc Van Droogenbroeck, University of LiÃ¨ge (ULiÃ¨ge).




### Funding#

Anthony Cioppa is funded by the FRIA, Belgium. This work is supported by the DeepSport and TRAIL projects of the Walloon Region, at the University of LiÃ¨ge (ULiÃ¨ge), Belgium. This work was supported by the Service Public de Wallonie (SPW) Recherche under the DeepSport project and Grant No.326 2010235 (ARIAC by https://DigitalWallonia4.ai) This work is also supported by the King Abdullah University of Science and Technology (KAUST) Office of Sponsored Research (OSR) (award327 OSR-CRG2017-3405).

## Citation#

**BibTeX:**
    
    
    @inproceedings{Giancola_2018,
       title={SoccerNet: A Scalable Dataset for Action Spotting in Soccer Videos},
       url={http://dx.doi.org/10.1109/CVPRW.2018.00223},
       DOI={10.1109/cvprw.2018.00223},
       booktitle={2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)},
       publisher={IEEE},
       author={Giancola, Silvio and Amine, Mohieddine and Dghaily, Tarek and Ghanem, Bernard},
       year={2018},
       month=jun }
    
    @misc{deliÃ¨ge2021soccernetv2,
          title={SoccerNet-v2: A Dataset and Benchmarks for Holistic Understanding of Broadcast Soccer Videos}, 
          author={Adrien DeliÃ¨ge and Anthony Cioppa and Silvio Giancola and Meisam J. Seikavandi and Jacob V. Dueholm and Kamal Nasrollahi and Bernard Ghanem and Thomas B. Moeslund and Marc Van Droogenbroeck},
          year={2021},
          eprint={2011.13367},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
    
    @misc{cioppa2022soccernettracking,
          title={SoccerNet-Tracking: Multiple Object Tracking Dataset and Benchmark in Soccer Videos}, 
          author={Anthony Cioppa and Silvio Giancola and Adrien Deliege and Le Kang and Xin Zhou and Zhiyu Cheng and Bernard Ghanem and Marc Van Droogenbroeck},
          year={2022},
          eprint={2204.06918},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
    
    @article{Cioppa2022,
      title={Scaling up SoccerNet with multi-view spatial localization and re-identification},
      author={Cioppa, Anthony and Deli{\`e}ge, Adrien and Giancola, Silvio and Ghanem, Bernard and Van Droogenbroeck, Marc},
      journal={Scientific Data},
      year={2022},
      volume={9},
      number={1},
      pages={355},
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
