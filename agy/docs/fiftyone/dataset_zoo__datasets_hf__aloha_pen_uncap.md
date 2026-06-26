---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/aloha_pen_uncap.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/aloha_pen_uncap)

# Dataset Card for aloha_pen_uncap#

![image/png](https://huggingface.co/datasets/Voxel51/aloha_pen_uncap/resolve/main/aloha-uncap-fo-hq.gif)

This dataset is a [FiftyOne](https://github.com/voxel51/fiftyone) conversion in LeRobot format of the `aloha_pen_uncap_diverse` subset of BiPlay.

The **aloha_pen_uncap_diverse** subset is a task-specific segment of BiPlay focusing on the long-horizon, dexterous bimanual task of un-capping a pen under diverse conditions. It contains episodes where the robot is required to grasp a pen and successfully remove its capâan action requiring coordination and dexterityâacross a wide range of object placements, backgrounds, and distractor objects. This diversity is designed specifically to benchmark policy generalization and to test the ability of learned policies (such as diffusion transformer-based ones) to adapt to varied real-world scenarios[4][5].

Key attributes of the **aloha_pen_uncap_diverse** subset:

  * **Task:** Bimanual pen uncapping with an ALOHA robot, including significant variation in scene and object arrangement.

  * **Format:** Converted into the LeRobot dataset v2.0 format for compatibility with common robotics learning frameworks[6][4].

  * **Data Contents:** The dataset includes state sequences, action sequences, velocities, efforts, and high-resolution images from multiple camera viewpoints for each time step.

  * **Research Use:** Commonly used to benchmark methods such as Diffusion Transformer Policies (DiT-Policy), which aim for robust, generalizable robotic manipulation through large-scale, language-annotated data[3][7].




## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/aloha_pen_uncap")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Sources#

â¢ Paper: https://huggingface.co/papers/2410.10088

â¢ Code: https://github.com/sudeepdasari/dit-policy

Learn more about converting LeRobot format datasets into FiftyOne format: https://github.com/harpreetsahota204/fiftyone_lerobot_importer

### Citation#
    
    
    @inproceedings{dasari2025ingredients,
      title={The Ingredients for Robotic Diffusion Transformers},
      author={Sudeep Dasari and Oier Mees and Sebastian Zhao and Mohan Kumar Srirama and Sergey Levine},
      booktitle = {Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
      year={2025},
      address = {Atlanta, USA}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
