---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/stanford_dogs_imbalanced.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Stanford-Dogs-Imbalanced)

# Dataset Card for StanfordDogsImbalanced#

![image/png](https://huggingface.co/datasets/Voxel51/Stanford-Dogs-Imbalanced/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 19060 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Stanford-Dogs-Imbalanced")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

An imbalanced version of the [Stanford Dogs dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/) designed for testing class imbalance mitigation techniques, including but not limited to synthetic data generation.

This version of the dataset was constructed by randomly splitting the original dataset into train, val, and test sets with a 60/20/20 split. For 15 randomly chosen classes, we then removed all but 10 of the training examples.
    
    
    # Split the dataset into train, val, and test sets
    import fiftyone.utils.random as four
    train, val, test = four.random_split(dataset, split_fracs=(0.6, 0.2, 0.2))
    splits_dict = { "train": train, "val": val, "test": test }
    
    # Get the classes to limit
    import random
    classes = list(dataset.distinct("ground_truth.label"))
    classes_to_limit = random.sample(classes, 15)
    
    # Limit the number of samples for the selected classes
    for class_name in classes_to_limit:
        class_samples = dataset.match(F("ground_truth.label") == class_name)
        samples_to_keep = class_samples.take(10)
        samples_to_remove = class_samples.exclude(samples_to_keep)
        dataset.delete_samples(samples_to_remove)
    

  * **Curated by:** [More Information Needed]

  * **Funded by [optional]:** [More Information Needed]

  * **Shared by [optional]:** [More Information Needed]

  * **Language(s) (NLP):** en

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Paper:** [More Information Needed]

  * **Homepage:** [More Information Needed]




## Uses#

  * Fine-grained visual classification

  * Class imbalance mitigation strategies




## Dataset Structure#

The following classes only have 10 samples in the train split:

  * Australian_terrier

  * Saluki

  * Cardigan

  * standard_schnauzer

  * Eskimo_dog

  * American_Staffordshire_terrier

  * Lakeland_terrier

  * Lhasa

  * cocker_spaniel

  * Greater_Swiss_Mountain_dog

  * basenji

  * toy_terrier

  * Chihuahua

  * Walker_hound

  * Shih-Tzu

  * Newfoundland




## Citation#

**BibTeX:**
    
    
    @inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,
      author = "Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and Li Fei-Fei",
      title = "Novel Dataset for Fine-Grained Image Categorization",
      booktitle = "First Workshop on Fine-Grained Visual Categorization, IEEE Conference on Computer Vision and Pattern Recognition",
      2011,
      month = "June",
      address = "Colorado Springs, CO",
    }
    

## Dataset Card Author#

[Jacob Marks](https://huggingface.co/jamarks)

## Dataset Contacts#

aditya86@cs.stanford.edu and bangpeng@cs.stanford.edu

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
