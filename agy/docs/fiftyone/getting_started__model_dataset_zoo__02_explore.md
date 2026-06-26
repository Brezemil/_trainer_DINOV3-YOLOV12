---
source_url: https://docs.voxel51.com/getting_started/model_dataset_zoo/02_explore.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/model_dataset_zoo/02_explore.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/model_dataset_zoo/02_explore.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/model_dataset_zoo/02_explore.ipynb)

# Exploring the Model Zoo#

This experience introduces you to the core components of the FiftyOne Zoo:

  * The **Dataset Zoo** for accessing and exploring public datasets
  * The **Model Zoo** for running pre-trained models on your data
  * Creating your **own remotely-sourced datasets** for reuse and collaboration

Whether youâre a researcher, engineer, or educator, these tools help streamline your computer vision workflows in FiftyOne.

> ð¡ Make sure to run `pip install fiftyone torch torchvision` before starting.
    
    
    [ ]:
    
    
    
    #!pip install fiftyone
    #!pip install torch torchvision
    

## FiftyOne Zoo: A Hub for Datasets and Models#

FiftyOne Zoo provides easy access to a vast collection of pre-built datasets and pre-trained models. This notebook will guide you through exploring and using these resources.

### Key Components:#

  * **Dataset Zoo:** Offers a wide range of computer vision datasets, ready for immediate use.
  * **Model Zoo:** Provides pre-trained models for various tasks, enabling quick experimentation and deployment.

Letâs dive in!
    
    
    [1]:
    
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    

# Model Zoo#

## Exploring the Model Zoo#

The Model Zoo provides pre-trained models that can be used for inference and evaluation.

### Listing Available Models#
    
    
    [ ]:
    
    
    
    print("\nAvailable Models:")
    for model_name in foz.list_zoo_models():
        print(f"- {model_name}")
    

FiftyOne supports a wide range of models for classification, detection, and segmentation, please visit the [Model Zoo](https://docs.voxel51.com/model_zoo/models.html) for the full, up-to-date catalog.

### Loading a Model (Example: AlexNet on ImageNet)#
    
    
    [ ]:
    
    
    
    model = foz.load_zoo_model("alexnet-imagenet-torch")
    print(model)
    
    
    
    Downloading model from 'https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth'...
     100% |ââââââ|    1.8Gb/1.8Gb [3.7s elapsed, 0s remaining, 527.5Mb/s]
    
    
    
    Downloading: "https://download.pytorch.org/models/alexnet-owt-7be5be79.pth" to /home/paula/.cache/torch/hub/checkpoints/alexnet-owt-7be5be79.pth
    100.0%
    
    
    
    <fiftyone.zoo.models.torch.TorchvisionImageModel object at 0x7798cad07340>
    

![imagenet](https://cdn.voxel51.com/getting_started_model_dataset_zoo/notebook2/imagenet.webp)

### Applying a Model to a Dataset#
    
    
    [ ]:
    
    
    
    try:
        dataset = foz.load_zoo_dataset("imagenet-sample")
        predictions = dataset.apply_model(model, label_field="predictions")
        print(predictions)
    except:
        print("imagenet-sample dataset is not available, please install it if needed.")
    
    session = fo.launch_app(dataset, port=5152, auto=False)
    
    
    
    Dataset already downloaded
    Loading existing dataset 'imagenet-sample'. To reload from disk, either delete the existing dataset or provide a custom `dataset_name` to use
     100% |âââââââââââââââ| 1000/1000 [4.6s elapsed, 0s remaining, 277.2 samples/s]
    None
    Session launched. Run `session.show()` to open the App in a cell output.
    

### Evaluating Model Performance#
    
    
    [ ]:
    
    
    
    !fiftyone plugins download https://github.com/voxel51/fiftyone-plugins --plugin-names @voxel51/evaluation
    
    
    
    Downloading voxel51/fiftyone-plugins...
      329.3Mb [12.2s elapsed, ? remaining, 32.9Mb/s]
    Skipping existing plugin '@voxel51/evaluation'
    
    
    
    [ ]:
    
    
    
    eval_key = "class_eval"
        # Now evaluate on the "defect2" field
    eval_classif_padim = dataset.evaluate_classifications(
        "predictions",
        gt_field="ground_truth",
        method="simple", #method is important to see data in the FO app
        eval_key=eval_key,  # <--- store this run under "classification_eval"
    )
    eval_classif_padim.print_report()
    
    
    
                                    precision    recall  f1-score   support
    
                      Afghan hound       1.00      1.00      1.00         1
                 African chameleon       0.33      1.00      0.50         1
                 African crocodile       1.00      1.00      1.00         1
                  African elephant       0.00      0.00      0.00         0
                      African grey       1.00      1.00      1.00         1
               African hunting dog       1.00      1.00      1.00         1
                          Airedale       1.00      1.00      1.00         1
    American Staffordshire terrier       0.00      0.00      0.00         1
                American alligator       0.00      0.00      0.00         1
               American black bear       0.00      0.00      0.00         1
                American chameleon       0.00      0.00      0.00         1
                     American coot       0.00      0.00      0.00         1
                    American egret       0.00      0.00      0.00         1
                  American lobster       1.00      1.00      1.00         1
                            Angora       0.33      1.00      0.50         1
                       Appenzeller       0.00      0.00      0.00         1
                     Arabian camel       0.25      1.00      0.40         1
                        Arctic fox       0.50      1.00      0.67         1
                Australian terrier       0.00      0.00      0.00         1
                          Band Aid       0.00      0.00      0.00         1
                Bedlington terrier       1.00      1.00      1.00         1
              Bernese mountain dog       0.00      0.00      0.00         1
                  Blenheim spaniel       1.00      1.00      1.00         1
                     Border collie       0.00      0.00      0.00         1
                    Border terrier       0.00      0.00      0.00         1
                       Boston bull       1.00      1.00      1.00         1
              Bouvier des Flandres       0.00      0.00      0.00         1
                 Brabancon griffon       1.00      1.00      1.00         1
                  Brittany spaniel       1.00      1.00      1.00         1
                         CD player       0.00      0.00      0.00         0
                          Cardigan       0.00      0.00      0.00         2
          Chesapeake Bay retriever       0.00      0.00      0.00         1
                         Chihuahua       0.00      0.00      0.00         1
                    Dandie Dinmont       0.00      0.00      0.00         1
                          Doberman       0.50      1.00      0.67         1
                        Dutch oven       0.00      0.00      0.00         1
                      Egyptian cat       0.00      0.00      0.00         0
                    English setter       0.00      0.00      0.00         1
                  English springer       0.00      0.00      0.00         1
                       EntleBucher       1.00      1.00      1.00         1
                        Eskimo dog       0.00      0.00      0.00         2
          European fire salamander       1.00      1.00      1.00         1
                European gallinule       0.00      0.00      0.00         1
                    French bulldog       1.00      1.00      1.00         1
                       French horn       1.00      1.00      1.00         1
                   German shepherd       1.00      1.00      1.00         1
       German short-haired pointer       1.00      1.00      1.00         1
                      Gila monster       1.00      1.00      1.00         1
                     Gordon setter       0.00      0.00      0.00         1
                      Granny Smith       1.00      1.00      1.00         1
                        Great Dane       0.00      0.00      0.00         1
                    Great Pyrenees       1.00      0.33      0.50         3
                      Ibizan hound       0.00      0.00      0.00         1
                      Indian cobra       1.00      1.00      1.00         1
                   Indian elephant       0.00      0.00      0.00         0
                      Irish setter       1.00      1.00      1.00         1
                     Irish terrier       1.00      1.00      1.00         1
               Irish water spaniel       0.50      1.00      0.67         1
                   Irish wolfhound       0.00      0.00      0.00         1
                 Italian greyhound       1.00      1.00      1.00         2
                  Japanese spaniel       1.00      1.00      1.00         1
                Kerry blue terrier       0.50      1.00      0.67         1
                     Komodo dragon       0.50      1.00      0.67         1
                  Lakeland terrier       1.00      1.00      1.00         1
                          Leonberg       1.00      1.00      1.00         1
                             Lhasa       1.00      1.00      1.00         1
                            Loafer       1.00      1.00      1.00         1
                    Madagascar cat       0.50      1.00      0.67         1
                       Maltese dog       0.50      1.00      0.67         1
                  Mexican hairless       0.00      0.00      0.00         0
                           Model T       0.50      1.00      0.67         1
                      Newfoundland       1.00      1.00      1.00         1
                   Norfolk terrier       1.00      1.00      1.00         1
                Norwegian elkhound       1.00      1.00      1.00         1
                   Norwich terrier       0.00      0.00      0.00         1
              Old English sheepdog       0.00      0.00      0.00         1
                          Pekinese       1.00      1.00      1.00         1
                          Pembroke       0.00      0.00      0.00         0
                       Persian cat       1.00      1.00      1.00         1
                        Petri dish       0.50      1.00      0.67         1
                   Polaroid camera       0.50      0.50      0.50         2
                        Pomeranian       1.00      1.00      1.00         1
               Rhodesian ridgeback       0.00      0.00      0.00         1
                        Rottweiler       0.00      0.00      0.00         2
                     Saint Bernard       1.00      1.00      1.00         1
                            Saluki       0.50      0.50      0.50         2
                           Samoyed       0.50      1.00      0.67         1
                    Scotch terrier       1.00      1.00      1.00         1
                Scottish deerhound       0.50      1.00      0.67         1
                  Sealyham terrier       0.00      0.00      0.00         1
                 Shetland sheepdog       0.00      0.00      0.00         1
                          Shih-Tzu       0.50      0.50      0.50         2
                       Siamese cat       0.50      1.00      0.67         1
                    Siberian husky       0.33      1.00      0.50         1
         Staffordshire bullterrier       1.00      1.00      1.00         1
                    Sussex spaniel       0.00      0.00      0.00         1
                   Tibetan terrier       0.00      0.00      0.00         1
                      Walker hound       0.00      0.00      0.00         2
                        Weimaraner       0.50      1.00      0.67         1
            Welsh springer spaniel       0.50      1.00      0.67         1
       West Highland white terrier       1.00      1.00      1.00         1
                 Yorkshire terrier       0.00      0.00      0.00         1
                             abaya       0.00      0.00      0.00         0
                         accordion       0.00      0.00      0.00         1
                             acorn       1.00      1.00      1.00         1
                      acorn squash       0.50      1.00      0.67         1
                   acoustic guitar       0.00      0.00      0.00         1
                           admiral       0.00      0.00      0.00         1
                     affenpinscher       1.00      1.00      1.00         1
                             agama       0.00      0.00      0.00         0
                            agaric       1.00      1.00      1.00         2
                  aircraft carrier       0.00      0.00      0.00         2
                          airliner       1.00      1.00      1.00         1
                           airship       0.00      0.00      0.00         2
                         albatross       0.00      0.00      0.00         1
                  alligator lizard       0.00      0.00      0.00         1
                             altar       0.00      0.00      0.00         1
                         ambulance       0.50      1.00      0.67         1
                      anemone fish       1.00      0.50      0.67         2
                               ant       0.00      0.00      0.00         1
                            apiary       0.50      1.00      0.67         1
                             apron       1.00      1.00      1.00         1
                         armadillo       1.00      1.00      1.00         1
                         artichoke       0.00      0.00      0.00         0
                            ashcan       0.00      0.00      0.00         1
                           axolotl       0.50      1.00      0.67         1
                            baboon       0.00      0.00      0.00         1
                          backpack       0.00      0.00      0.00         0
                            bakery       1.00      1.00      1.00         1
                      balance beam       0.00      0.00      0.00         1
                        bald eagle       0.33      0.50      0.40         2
                           balloon       1.00      1.00      1.00         1
                        ballplayer       0.00      0.00      0.00         1
                         ballpoint       0.50      1.00      0.67         1
                            banana       0.00      0.00      0.00         0
                      banded gecko       0.00      0.00      0.00         1
                             banjo       1.00      1.00      1.00         1
                         bannister       0.00      0.00      0.00         0
                           barbell       1.00      1.00      1.00         1
                      barber chair       0.50      1.00      0.67         1
                        barbershop       0.00      0.00      0.00         1
                              barn       0.50      1.00      0.67         1
                       barn spider       1.00      1.00      1.00         1
                         barometer       1.00      1.00      1.00         1
                        barracouta       1.00      1.00      1.00         1
                            barrel       1.00      1.00      1.00         1
                            barrow       0.00      0.00      0.00         1
                          baseball       1.00      1.00      1.00         1
                           basenji       0.00      0.00      0.00         1
                        basketball       1.00      1.00      1.00         1
                            basset       0.00      0.00      0.00         2
                          bassinet       0.00      0.00      0.00         1
                           bassoon       0.00      0.00      0.00         1
                        bath towel       0.00      0.00      0.00         0
                       bathing cap       0.00      0.00      0.00         1
                           bathtub       0.00      0.00      0.00         2
                       beach wagon       0.50      0.50      0.50         2
                            beacon       0.00      0.00      0.00         1
                            beagle       0.67      0.67      0.67         3
                            beaker       0.00      0.00      0.00         1
                          bearskin       1.00      1.00      1.00         1
                            beaver       0.50      1.00      0.67         1
                               bee       1.00      0.50      0.67         2
                         bee eater       0.00      0.00      0.00         0
                       beer bottle       1.00      1.00      1.00         1
                        beer glass       1.00      1.00      1.00         1
                         bell cote       0.00      0.00      0.00         1
                       bell pepper       1.00      1.00      1.00         1
                               bib       0.00      0.00      0.00         1
             bicycle-built-for-two       1.00      0.50      0.67         2
                           bighorn       1.00      1.00      1.00         1
                            bikini       1.00      1.00      1.00         1
                            binder       0.50      1.00      0.67         1
                        binoculars       0.00      0.00      0.00         1
                         birdhouse       1.00      1.00      1.00         1
                             bison       0.50      1.00      0.67         1
                           bittern       0.00      0.00      0.00         1
      black and gold garden spider       1.00      1.00      1.00         1
                      black grouse       1.00      1.00      1.00         1
                       black stork       0.00      0.00      0.00         1
                        black swan       0.50      1.00      0.67         1
                       black widow       1.00      1.00      1.00         1
               black-footed ferret       1.00      1.00      1.00         1
                          bluetick       0.33      1.00      0.50         1
                   boa constrictor       0.00      0.00      0.00         1
                         boathouse       0.25      1.00      0.40         1
                           bobsled       0.00      0.00      0.00         2
                            bolete       1.00      1.00      1.00         1
                          bolo tie       0.00      0.00      0.00         1
                            bonnet       0.00      0.00      0.00         2
                       book jacket       0.00      0.00      0.00         1
                          bookcase       1.00      1.00      1.00         1
                          bookshop       0.00      0.00      0.00         1
                            borzoi       0.00      0.00      0.00         1
                         bottlecap       1.00      1.00      1.00         1
                               bow       1.00      1.00      1.00         1
                           bow tie       0.00      0.00      0.00         0
                             boxer       0.50      1.00      0.67         1
                       brain coral       1.00      1.00      1.00         1
                         brambling       0.00      0.00      0.00         1
                             brass       0.33      1.00      0.50         1
                         brassiere       0.00      0.00      0.00         0
                        breakwater       0.00      0.00      0.00         2
                       breastplate       0.00      0.00      0.00         2
                            briard       0.50      0.50      0.50         2
                          broccoli       1.00      1.00      1.00         1
                             broom       0.50      1.00      0.67         2
                        brown bear       1.00      1.00      1.00         1
                            bubble       1.00      1.00      1.00         1
                            bucket       0.00      0.00      0.00         0
                           buckeye       1.00      1.00      1.00         1
                            buckle       0.50      1.00      0.67         1
                            bulbul       0.00      0.00      0.00         1
                      bull mastiff       0.50      1.00      0.67         1
                      bullet train       0.50      0.50      0.50         2
                  bulletproof vest       0.50      1.00      0.67         1
                          bullfrog       0.00      0.00      0.00         1
                           burrito       0.50      1.00      0.67         1
                           bustard       0.00      0.00      0.00         1
                      butcher shop       1.00      1.00      1.00         1
                  butternut squash       0.00      0.00      0.00         1
                               cab       0.00      0.00      0.00         2
                 cabbage butterfly       0.50      1.00      0.67         1
                             cairn       0.50      1.00      0.67         1
                           caldron       0.00      0.00      0.00         1
                        can opener       1.00      1.00      1.00         1
                            candle       0.00      0.00      0.00         0
                            cannon       0.00      0.00      0.00         0
                             canoe       1.00      1.00      1.00         1
                          capuchin       0.00      0.00      0.00         1
                        car mirror       1.00      1.00      1.00         1
                         car wheel       0.00      0.00      0.00         1
                         carbonara       0.00      0.00      0.00         1
                          cardigan       1.00      0.50      0.67         2
                           cardoon       1.00      0.50      0.67         2
                          carousel       0.00      0.00      0.00         1
                   carpenter's kit       0.00      0.00      0.00         1
                            carton       0.00      0.00      0.00         0
                      cash machine       0.50      1.00      0.67         1
                          cassette       1.00      1.00      1.00         1
                   cassette player       0.00      0.00      0.00         1
                            castle       1.00      1.00      1.00         1
                         catamaran       1.00      1.00      1.00         1
                       cauliflower       1.00      1.00      1.00         1
                             cello       1.00      1.00      1.00         1
                cellular telephone       0.50      0.50      0.50         2
                             chain       1.00      1.00      1.00         1
                        chain mail       0.50      1.00      0.67         1
                         chain saw       0.00      0.00      0.00         1
                   chainlink fence       1.00      0.50      0.67         2
                chambered nautilus       1.00      0.50      0.67         2
                      cheeseburger       1.00      1.00      1.00         1
                           cheetah       1.00      1.00      1.00         2
                             chest       0.00      0.00      0.00         0
                         chickadee       0.00      0.00      0.00         1
                        chiffonier       0.00      0.00      0.00         1
                             chime       0.00      0.00      0.00         2
                        chimpanzee       1.00      1.00      1.00         1
                     china cabinet       1.00      0.50      0.67         2
                            chiton       0.50      1.00      0.67         1
                              chow       1.00      1.00      1.00         1
                            church       0.50      1.00      0.67         1
                            cicada       1.00      1.00      1.00         1
                            cinema       1.00      1.00      1.00         1
                           cleaver       0.00      0.00      0.00         1
                    cliff dwelling       1.00      1.00      1.00         1
                             cloak       0.00      0.00      0.00         0
                              clog       0.00      0.00      0.00         0
                           clumber       1.00      1.00      1.00         1
                    cocker spaniel       0.00      0.00      0.00         1
                         cockroach       0.50      1.00      0.67         1
                         coffeepot       0.00      0.00      0.00         1
                              coho       0.50      1.00      0.67         1
                              coil       0.00      0.00      0.00         0
                            collie       0.00      0.00      0.00         1
                        comic book       0.00      0.00      0.00         0
                     common iguana       1.00      1.00      1.00         1
                       common newt       0.00      0.00      0.00         1
                 computer keyboard       0.00      0.00      0.00         1
                             conch       0.50      1.00      0.67         1
                     confectionery       1.00      1.00      1.00         1
                          consomme       0.00      0.00      0.00         1
                    container ship       1.00      1.00      1.00         1
                       convertible       0.00      0.00      0.00         1
                      coral fungus       1.00      1.00      1.00         1
                        coral reef       1.00      0.50      0.67         2
                         corkscrew       1.00      1.00      1.00         1
                              corn       0.00      0.00      0.00         1
                            cornet       0.50      1.00      0.67         1
                            coucal       1.00      1.00      1.00         1
                            cougar       1.00      1.00      1.00         1
                       cowboy boot       0.00      0.00      0.00         0
                        cowboy hat       0.00      0.00      0.00         1
                            coyote       0.00      0.00      0.00         0
                            cradle       1.00      1.00      1.00         1
                             crane       0.67      0.67      0.67         3
                      crash helmet       0.00      0.00      0.00         2
                             crate       0.00      0.00      0.00         2
                          crayfish       0.00      0.00      0.00         1
                              crib       1.00      1.00      1.00         1
                           cricket       0.00      0.00      0.00         1
                      croquet ball       0.00      0.00      0.00         1
                  crossword puzzle       1.00      1.00      1.00         1
                            crutch       0.00      0.00      0.00         0
                          cucumber       0.00      0.00      0.00         1
                           cuirass       0.00      0.00      0.00         0
                               cup       0.00      0.00      0.00         1
            curly-coated retriever       0.00      0.00      0.00         1
                     custard apple       1.00      1.00      1.00         1
                             daisy       0.00      0.00      0.00         1
                         dalmatian       1.00      1.00      1.00         1
                               dam       0.00      0.00      0.00         1
                         damselfly       1.00      1.00      1.00         1
                              desk       1.00      0.67      0.80         3
                  desktop computer       0.00      0.00      0.00         1
                             dhole       0.00      0.00      0.00         1
                    dial telephone       1.00      1.00      1.00         1
                       diamondback       0.00      0.00      0.00         1
                            diaper       0.33      1.00      0.50         1
                     digital clock       0.00      0.00      0.00         1
                     digital watch       1.00      0.50      0.67         2
                      dining table       1.00      1.00      1.00         1
                           dishrag       0.50      1.00      0.67         1
                        dishwasher       0.67      1.00      0.80         2
                        disk brake       1.00      1.00      1.00         1
                              dock       0.00      0.00      0.00         0
                           dogsled       1.00      1.00      1.00         1
                              dome       0.00      0.00      0.00         2
                             dough       1.00      1.00      1.00         1
                         dowitcher       0.33      1.00      0.50         1
                         dragonfly       0.00      0.00      0.00         1
                             drake       1.00      1.00      1.00         1
                 drilling platform       0.00      0.00      0.00         0
                              drum       0.00      0.00      0.00         1
                         drumstick       0.00      0.00      0.00         1
                          dumbbell       1.00      0.50      0.67         2
                       dung beetle       1.00      1.00      1.00         1
                               ear       1.00      1.00      1.00         1
                         earthstar       1.00      1.00      1.00         1
                           echidna       0.50      1.00      0.67         1
                               eel       0.50      1.00      0.67         1
                               eft       0.50      1.00      0.67         1
                            eggnog       0.00      0.00      0.00         1
                      electric fan       0.00      0.00      0.00         1
                   electric guitar       1.00      1.00      1.00         1
               electric locomotive       1.00      1.00      1.00         1
                      electric ray       0.50      1.00      0.67         1
              entertainment center       1.00      0.50      0.67         2
                          envelope       0.00      0.00      0.00         0
                          espresso       1.00      1.00      1.00         1
                       face powder       0.00      0.00      0.00         1
                       feather boa       1.00      1.00      1.00         1
                      fiddler crab       0.00      0.00      0.00         2
                               fig       1.00      0.50      0.67         2
                              file       1.00      0.50      0.67         2
                       fire engine       1.00      1.00      1.00         1
                       fire screen       0.00      0.00      0.00         1
                          fireboat       1.00      1.00      1.00         1
                          flagpole       0.00      0.00      0.00         0
                          flamingo       1.00      1.00      1.00         1
             flat-coated retriever       0.33      1.00      0.50         1
                          flatworm       1.00      1.00      1.00         1
                             flute       0.00      0.00      0.00         1
                   football helmet       0.00      0.00      0.00         1
                          forklift       0.00      0.00      0.00         1
                          fountain       0.50      0.50      0.50         2
                      fountain pen       1.00      1.00      1.00         1
                       four-poster       0.50      1.00      0.67         1
                      fox squirrel       0.00      0.00      0.00         0
                       freight car       1.00      1.00      1.00         1
                    frilled lizard       0.00      0.00      0.00         1
                        frying pan       0.00      0.00      0.00         1
                          fur coat       1.00      1.00      1.00         1
                     garbage truck       1.00      1.00      1.00         1
                     garden spider       0.00      0.00      0.00         0
                      garter snake       0.33      0.50      0.40         2
                          gas pump       1.00      1.00      1.00         1
                           gasmask       0.00      0.00      0.00         1
                           gazelle       0.00      0.00      0.00         1
                            geyser       1.00      1.00      1.00         1
                       giant panda       1.00      0.50      0.67         2
                   giant schnauzer       1.00      1.00      1.00         1
                            gibbon       1.00      0.50      0.67         2
                           go-kart       0.00      0.00      0.00         1
                            goblet       1.00      0.50      0.67         2
                         goldfinch       1.00      1.00      1.00         1
                          goldfish       0.00      0.00      0.00         1
                          golfcart       0.00      0.00      0.00         1
                           gondola       0.50      1.00      0.67         1
                              gong       0.00      0.00      0.00         0
                             goose       1.00      1.00      1.00         1
                           gorilla       0.00      0.00      0.00         1
                              gown       0.00      0.00      0.00         0
                       grand piano       0.33      1.00      0.50         1
                       grasshopper       0.33      1.00      0.50         1
                    great grey owl       1.00      1.00      1.00         1
                 great white shark       1.00      1.00      1.00         1
                      green lizard       0.00      0.00      0.00         1
                       green mamba       0.00      0.00      0.00         2
                       green snake       0.00      0.00      0.00         0
                        greenhouse       0.00      0.00      0.00         0
                        grey whale       1.00      1.00      1.00         2
                     grocery store       1.00      0.50      0.67         2
                       groenendael       0.00      0.00      0.00         1
                             groom       1.00      0.50      0.67         2
                     ground beetle       0.00      0.00      0.00         1
                         guacamole       0.00      0.00      0.00         1
                        guillotine       1.00      0.50      0.67         2
                        guinea pig       0.50      1.00      0.67         1
                         gyromitra       1.00      0.50      0.67         2
                        hair slide       0.00      0.00      0.00         2
                        half track       0.00      0.00      0.00         1
                        hammerhead       1.00      1.00      1.00         1
                           hamster       0.00      0.00      0.00         2
                       hand blower       0.50      1.00      0.67         1
                      handkerchief       0.50      1.00      0.67         1
                         hard disc       0.00      0.00      0.00         1
                              hare       1.00      1.00      1.00         2
                         harmonica       0.00      0.00      0.00         1
                              harp       0.00      0.00      0.00         1
                        hartebeest       0.00      0.00      0.00         0
                         harvester       1.00      1.00      1.00         2
                        harvestman       0.50      0.50      0.50         2
                           hatchet       0.00      0.00      0.00         0
                      head cabbage       0.50      1.00      0.67         1
                               hen       1.00      1.00      1.00         2
                  hen-of-the-woods       0.00      0.00      0.00         0
                       hermit crab       1.00      1.00      1.00         1
                               hip       0.50      1.00      0.67         1
                      hippopotamus       1.00      1.00      1.00         1
                     hognose snake       0.50      1.00      0.67         1
                           holster       0.33      1.00      0.50         1
                      home theater       0.50      1.00      0.67         1
                         honeycomb       0.00      0.00      0.00         0
                              hook       0.00      0.00      0.00         2
                         hoopskirt       1.00      1.00      1.00         1
                    horizontal bar       0.67      1.00      0.80         2
                      horned viper       0.00      0.00      0.00         1
                        horse cart       1.00      1.00      1.00         1
                           hot pot       1.00      0.75      0.86         4
                            hotdog       0.00      0.00      0.00         2
                         hourglass       0.00      0.00      0.00         1
                       house finch       1.00      1.00      1.00         1
                     howler monkey       0.50      0.50      0.50         2
                       hummingbird       0.50      1.00      0.67         1
                             hyena       0.00      0.00      0.00         1
                              iPod       0.50      1.00      0.67         1
                              ibex       0.00      0.00      0.00         1
                          ice bear       0.00      0.00      0.00         1
                         ice cream       0.00      0.00      0.00         1
                         ice lolly       0.00      0.00      0.00         1
                            impala       1.00      1.00      1.00         1
                    indigo bunting       0.00      0.00      0.00         1
                             indri       1.00      1.00      1.00         1
                              iron       0.00      0.00      0.00         0
                            isopod       0.00      0.00      0.00         1
                           jacamar       1.00      1.00      1.00         2
                   jack-o'-lantern       1.00      1.00      1.00         1
                         jackfruit       1.00      1.00      1.00         1
                            jaguar       1.00      1.00      1.00         1
                               jay       0.00      0.00      0.00         1
                              jean       1.00      1.00      1.00         1
                              jeep       1.00      1.00      1.00         1
                         jellyfish       1.00      1.00      1.00         1
                            jersey       1.00      1.00      1.00         1
                     jigsaw puzzle       0.33      1.00      0.50         1
                        jinrikisha       0.33      1.00      0.50         1
                          joystick       0.00      0.00      0.00         1
                             junco       1.00      1.00      1.00         1
                          keeshond       0.50      1.00      0.67         1
                      killer whale       1.00      1.00      1.00         1
                            kimono       0.00      0.00      0.00         1
                         king crab       0.50      1.00      0.67         1
                      king penguin       1.00      1.00      1.00         1
                        king snake       1.00      1.00      1.00         1
                           kit fox       0.50      1.00      0.67         1
                              kite       0.50      0.50      0.50         2
                          knee pad       1.00      1.00      1.00         1
                              knot       1.00      1.00      1.00         1
                             koala       1.00      1.00      1.00         1
                          komondor       0.50      1.00      0.67         1
                            kuvasz       0.00      0.00      0.00         0
                          lab coat       1.00      1.00      1.00         1
                          lacewing       0.00      0.00      0.00         2
                             ladle       0.00      0.00      0.00         2
                           ladybug       0.00      0.00      0.00         1
                          lakeside       0.00      0.00      0.00         1
                         lampshade       0.00      0.00      0.00         1
                            langur       0.00      0.00      0.00         1
                            laptop       0.00      0.00      0.00         0
                        lawn mower       1.00      1.00      1.00         1
                       leaf beetle       0.25      1.00      0.40         1
                        leafhopper       1.00      1.00      1.00         1
                             lemon       0.50      1.00      0.67         1
                          lens cap       0.00      0.00      0.00         2
                           leopard       0.00      0.00      0.00         0
                      lesser panda       0.00      0.00      0.00         0
                     letter opener       0.00      0.00      0.00         2
                           library       0.00      0.00      0.00         1
                          lifeboat       1.00      1.00      1.00         1
                           lighter       0.33      1.00      0.50         1
                         limousine       1.00      1.00      1.00         1
                           limpkin       0.00      0.00      0.00         1
                             liner       1.00      0.67      0.80         3
                              lion       0.50      1.00      0.67         1
                          lionfish       0.50      1.00      0.67         1
                          lipstick       0.33      0.50      0.40         2
                             llama       1.00      1.00      1.00         1
                        loggerhead       1.00      1.00      1.00         1
                long-horned beetle       0.00      0.00      0.00         1
                          lorikeet       1.00      1.00      1.00         1
                       loudspeaker       0.00      0.00      0.00         0
                        lumbermill       1.00      1.00      1.00         1
                          lycaenid       0.00      0.00      0.00         1
                              lynx       0.00      0.00      0.00         2
                           macaque       0.00      0.00      0.00         0
                             macaw       1.00      1.00      1.00         1
                  magnetic compass       0.00      0.00      0.00         1
                            magpie       1.00      1.00      1.00         1
                           mailbag       0.00      0.00      0.00         2
                           mailbox       0.50      1.00      0.67         1
                           maillot       0.33      1.00      0.50         1
                          malamute       0.33      1.00      0.50         1
                          malinois       0.67      1.00      0.80         2
                     manhole cover       1.00      0.50      0.67         2
                            mantis       0.00      0.00      0.00         1
                            maraca       0.00      0.00      0.00         0
                           marimba       0.00      0.00      0.00         1
                          marmoset       1.00      1.00      1.00         1
                            marmot       0.50      1.00      0.67         1
                     mashed potato       1.00      1.00      1.00         1
                              mask       0.50      1.00      0.67         1
                        matchstick       0.00      0.00      0.00         1
                           maypole       0.50      1.00      0.67         1
                              maze       1.00      0.50      0.67         2
                     measuring cup       1.00      1.00      1.00         1
                         meat loaf       0.00      0.00      0.00         1
                    medicine chest       0.00      0.00      0.00         1
                           meerkat       1.00      1.00      1.00         1
                          megalith       1.00      1.00      1.00         1
                              menu       1.00      1.00      1.00         1
                        microphone       0.50      1.00      0.67         1
                         microwave       1.00      1.00      1.00         1
                  military uniform       0.00      0.00      0.00         1
                          milk can       0.00      0.00      0.00         1
                miniature pinscher       1.00      1.00      1.00         2
                  miniature poodle       1.00      1.00      1.00         1
               miniature schnauzer       1.00      1.00      1.00         1
                           minibus       1.00      1.00      1.00         1
                         miniskirt       0.00      0.00      0.00         2
                           minivan       0.00      0.00      0.00         1
                              mink       0.00      0.00      0.00         1
                           missile       1.00      1.00      1.00         1
                            mitten       0.00      0.00      0.00         0
                       mixing bowl       0.00      0.00      0.00         3
                       mobile home       0.25      1.00      0.40         1
                             modem       0.00      0.00      0.00         0
                           monarch       1.00      1.00      1.00         1
                         monastery       1.00      1.00      1.00         1
                          mongoose       0.00      0.00      0.00         1
                           monitor       0.00      0.00      0.00         1
                             moped       0.00      0.00      0.00         1
                            mortar       0.50      1.00      0.67         1
                       mortarboard       0.00      0.00      0.00         2
                            mosque       1.00      1.00      1.00         1
                      mosquito net       0.00      0.00      0.00         1
                     motor scooter       0.00      0.00      0.00         1
                     mountain bike       1.00      1.00      1.00         1
                     mountain tent       1.00      1.00      1.00         1
                             mouse       0.00      0.00      0.00         1
                        moving van       0.00      0.00      0.00         1
                        mud turtle       0.00      0.00      0.00         1
                          mushroom       0.00      0.00      0.00         0
                              nail       0.25      1.00      0.40         1
                        neck brace       0.00      0.00      0.00         1
                          necklace       1.00      0.50      0.67         2
                          nematode       0.00      0.00      0.00         1
                            nipple       0.00      0.00      0.00         1
                          notebook       1.00      0.50      0.67         2
                           obelisk       1.00      0.33      0.50         3
                              oboe       1.00      1.00      1.00         1
                           ocarina       0.00      0.00      0.00         1
                          odometer       1.00      1.00      1.00         1
                        oil filter       0.00      0.00      0.00         1
                            orange       1.00      1.00      1.00         1
                         orangutan       1.00      1.00      1.00         1
                      oscilloscope       0.50      0.50      0.50         2
                           ostrich       1.00      1.00      1.00         1
                             otter       0.00      0.00      0.00         1
                         overskirt       0.00      0.00      0.00         1
                                ox       1.00      1.00      1.00         1
                            oxcart       1.00      1.00      1.00         1
                       oxygen mask       0.00      0.00      0.00         1
                     oystercatcher       1.00      1.00      1.00         1
                            packet       0.00      0.00      0.00         1
                            paddle       0.00      0.00      0.00         0
                           padlock       0.33      0.50      0.40         2
                        paintbrush       0.00      0.00      0.00         1
                            pajama       0.50      0.50      0.50         2
                            palace       1.00      1.00      1.00         1
                           panpipe       0.00      0.00      0.00         1
                       paper towel       1.00      0.50      0.67         2
                          papillon       1.00      1.00      1.00         1
                         parachute       1.00      1.00      1.00         1
                        park bench       0.67      1.00      0.80         2
                     parking meter       0.00      0.00      0.00         1
                         partridge       1.00      0.50      0.67         2
                     passenger car       0.50      1.00      0.67         1
                             patas       1.00      0.33      0.50         3
                             patio       0.00      0.00      0.00         1
                         pay-phone       1.00      1.00      1.00         1
                           peacock       0.00      0.00      0.00         1
                          pedestal       0.00      0.00      0.00         0
                           pelican       1.00      1.00      1.00         1
                        pencil box       1.00      0.50      0.67         2
                  pencil sharpener       0.00      0.00      0.00         1
                           perfume       1.00      1.00      1.00         1
                       photocopier       1.00      1.00      1.00         1
                              pick       0.50      1.00      0.67         1
                       pickelhaube       1.00      1.00      1.00         1
                      picket fence       1.00      0.50      0.67         2
                            pickup       0.00      0.00      0.00         1
                              pier       0.00      0.00      0.00         1
                        piggy bank       0.00      0.00      0.00         1
                       pill bottle       0.00      0.00      0.00         1
                            pillow       0.00      0.00      0.00         0
                         pineapple       0.00      0.00      0.00         1
                    ping-pong ball       0.50      1.00      0.67         1
                          pinwheel       1.00      1.00      1.00         1
                            pirate       1.00      1.00      1.00         1
                           pitcher       1.00      0.50      0.67         2
                             pizza       1.00      1.00      1.00         1
                             plane       0.00      0.00      0.00         1
                       planetarium       1.00      1.00      1.00         1
                       plastic bag       0.00      0.00      0.00         2
                             plate       0.00      0.00      0.00         1
                          platypus       0.50      1.00      0.67         1
                              pole       0.00      0.00      0.00         1
                           polecat       0.00      0.00      0.00         1
                       pomegranate       1.00      1.00      1.00         1
                            poncho       0.50      1.00      0.67         1
                        pool table       1.00      1.00      1.00         1
                        pop bottle       0.00      0.00      0.00         1
                         porcupine       0.33      1.00      0.50         1
                               pot       1.00      0.50      0.67         2
                            potpie       0.00      0.00      0.00         1
                    potter's wheel       1.00      1.00      1.00         1
                       power drill       0.00      0.00      0.00         1
                   prairie chicken       1.00      1.00      1.00         1
                        prayer rug       0.33      1.00      0.50         1
                           printer       1.00      0.50      0.67         2
                            prison       1.00      1.00      1.00         1
                  proboscis monkey       1.00      1.00      1.00         1
                         projector       0.00      0.00      0.00         0
                        promontory       1.00      1.00      1.00         2
                         ptarmigan       1.00      1.00      1.00         1
                            puffer       0.00      0.00      0.00         1
                               pug       1.00      0.50      0.67         2
                      punching bag       0.00      0.00      0.00         1
                             purse       0.00      0.00      0.00         2
                             quail       1.00      1.00      1.00         1
                             quill       0.00      0.00      0.00         2
                             racer       0.00      0.00      0.00         1
                            racket       1.00      1.00      1.00         1
                          radiator       1.00      1.00      1.00         1
                             radio       1.00      1.00      1.00         1
                   radio telescope       0.50      1.00      0.67         1
                       rain barrel       0.00      0.00      0.00         1
                               ram       0.00      0.00      0.00         1
                          rapeseed       1.00      1.00      1.00         1
              recreational vehicle       1.00      1.00      1.00         1
                           red fox       0.33      0.50      0.40         2
                          red wine       0.00      0.00      0.00         0
                          red wolf       0.00      0.00      0.00         2
              red-backed sandpiper       0.00      0.00      0.00         1
            red-breasted merganser       1.00      1.00      1.00         1
                           redbone       0.00      0.00      0.00         1
                          redshank       0.50      1.00      0.67         1
                              reel       0.00      0.00      0.00         1
                     reflex camera       0.00      0.00      0.00         0
                      refrigerator       0.00      0.00      0.00         0
                        restaurant       0.00      0.00      0.00         3
                          revolver       1.00      1.00      1.00         1
                             rifle       0.00      0.00      0.00         2
                           ringlet       0.50      1.00      0.67         1
                    ringneck snake       0.00      0.00      0.00         1
                             robin       0.50      1.00      0.67         1
                       rock beauty       0.00      0.00      0.00         0
                         rock crab       0.00      0.00      0.00         1
                       rock python       0.00      0.00      0.00         1
                     rocking chair       1.00      1.00      1.00         1
                        rotisserie       1.00      0.50      0.67         2
                     rubber eraser       0.00      0.00      0.00         1
                   ruddy turnstone       1.00      1.00      1.00         1
                     ruffed grouse       0.00      0.00      0.00         0
                        rugby ball       0.00      0.00      0.00         1
                              rule       1.00      0.50      0.67         2
                      running shoe       0.00      0.00      0.00         1
                              safe       0.50      0.50      0.50         2
                        safety pin       1.00      1.00      1.00         2
                        saltshaker       0.00      0.00      0.00         0
                            sandal       1.00      1.00      1.00         1
                           sandbar       1.00      1.00      1.00         1
                            sarong       0.00      0.00      0.00         1
                               sax       0.00      0.00      0.00         1
                          scabbard       1.00      0.33      0.50         3
                             scale       0.00      0.00      0.00         1
                        schipperke       0.50      1.00      0.67         2
                        school bus       0.50      1.00      0.67         1
                        scoreboard       0.33      1.00      0.50         1
                          scorpion       0.00      0.00      0.00         1
                             screw       1.00      1.00      1.00         1
                       scuba diver       1.00      1.00      1.00         1
                       sea anemone       0.00      0.00      0.00         0
                      sea cucumber       1.00      1.00      1.00         1
                          sea lion       0.50      1.00      0.67         1
                          sea slug       1.00      1.00      1.00         1
                        sea urchin       0.00      0.00      0.00         1
                         seat belt       0.25      1.00      0.40         1
                    sewing machine       0.00      0.00      0.00         1
                            shield       0.00      0.00      0.00         0
                         shoe shop       1.00      1.00      1.00         1
                             shoji       1.00      1.00      1.00         1
                   shopping basket       0.50      1.00      0.67         1
                     shopping cart       0.00      0.00      0.00         0
                            shovel       0.00      0.00      0.00         1
                        shower cap       0.33      1.00      0.50         1
                    shower curtain       0.50      1.00      0.67         1
                           siamang       0.00      0.00      0.00         2
                        sidewinder       0.00      0.00      0.00         1
                     silky terrier       1.00      1.00      1.00         1
                               ski       1.00      0.50      0.67         2
                          ski mask       0.00      0.00      0.00         0
                             skunk       0.50      1.00      0.67         2
                      sleeping bag       0.50      1.00      0.67         1
                        slide rule       0.00      0.00      0.00         1
                      sliding door       0.67      1.00      0.80         2
                              slot       0.50      1.00      0.67         1
                        sloth bear       1.00      1.00      1.00         1
                              slug       0.00      0.00      0.00         1
                             snail       0.00      0.00      0.00         1
                           snorkel       1.00      0.50      0.67         2
                      snow leopard       1.00      1.00      1.00         1
                        snowmobile       1.00      1.00      1.00         1
                          snowplow       0.50      1.00      0.67         1
                    soap dispenser       0.00      0.00      0.00         3
                       soccer ball       1.00      1.00      1.00         1
       soft-coated wheaten terrier       1.00      0.33      0.50         3
                        solar dish       0.00      0.00      0.00         1
                          sombrero       0.00      0.00      0.00         1
                            sorrel       0.50      0.50      0.50         2
                         soup bowl       0.50      1.00      0.67         1
                  spaghetti squash       0.00      0.00      0.00         1
                         speedboat       1.00      1.00      1.00         1
                        spider web       1.00      1.00      1.00         1
                           spindle       0.00      0.00      0.00         0
                     spiny lobster       1.00      1.00      1.00         1
                         spoonbill       1.00      1.00      1.00         1
                        sports car       0.00      0.00      0.00         1
                         spotlight       0.00      0.00      0.00         1
                spotted salamander       1.00      1.00      1.00         1
                   squirrel monkey       0.00      0.00      0.00         1
                             stage       0.25      1.00      0.40         1
                standard schnauzer       0.00      0.00      0.00         1
                          starfish       0.00      0.00      0.00         1
                  steam locomotive       0.50      1.00      0.67         1
                 steel arch bridge       0.00      0.00      0.00         0
                        steel drum       0.50      1.00      0.67         1
                       stethoscope       0.00      0.00      0.00         1
                          stingray       0.50      1.00      0.67         1
                         stinkhorn       0.00      0.00      0.00         1
                             stole       0.00      0.00      0.00         1
                        stone wall       1.00      1.00      1.00         1
                             stove       0.50      1.00      0.67         1
                          strainer       0.50      1.00      0.67         1
                        strawberry       0.00      0.00      0.00         1
                       street sign       0.00      0.00      0.00         1
                         streetcar       0.50      1.00      0.67         1
                         stretcher       0.00      0.00      0.00         1
                      studio couch       1.00      1.00      1.00         1
                             stupa       1.00      1.00      1.00         1
                          sturgeon       0.00      0.00      0.00         1
                         submarine       0.00      0.00      0.00         1
                              suit       0.00      0.00      0.00         1
                 sulphur butterfly       1.00      1.00      1.00         1
          sulphur-crested cockatoo       0.00      0.00      0.00         1
                           sundial       0.00      0.00      0.00         0
                          sunglass       0.00      0.00      0.00         1
                         sunscreen       1.00      0.50      0.67         2
                 suspension bridge       0.00      0.00      0.00         1
                              swab       0.00      0.00      0.00         0
                        sweatshirt       0.00      0.00      0.00         0
                   swimming trunks       0.50      1.00      0.67         1
                             swing       0.00      0.00      0.00         3
                            switch       0.00      0.00      0.00         0
                           syringe       0.00      0.00      0.00         1
                             tabby       1.00      0.50      0.67         2
                        table lamp       0.50      1.00      0.67         1
                       tailed frog       0.50      0.50      0.50         2
                              tank       1.00      0.50      0.67         2
                       tape player       0.00      0.00      0.00         2
                         tarantula       1.00      1.00      1.00         1
                            teapot       1.00      1.00      1.00         1
                             teddy       1.00      1.00      1.00         1
                        television       0.00      0.00      0.00         1
                             tench       1.00      1.00      1.00         1
                       tennis ball       0.50      1.00      0.67         1
                          terrapin       1.00      0.67      0.80         3
                            thatch       0.00      0.00      0.00         1
                   theater curtain       0.50      1.00      0.67         1
                           thimble       0.00      0.00      0.00         2
                  three-toed sloth       0.50      1.00      0.67         1
                            throne       0.50      1.00      0.67         1
                     thunder snake       0.00      0.00      0.00         1
                              tick       0.00      0.00      0.00         0
                             tiger       1.00      1.00      1.00         2
                      tiger beetle       0.00      0.00      0.00         1
                       tiger shark       1.00      1.00      1.00         2
                         tile roof       1.00      1.00      1.00         1
                       timber wolf       0.00      0.00      0.00         1
                           toaster       0.00      0.00      0.00         0
                       toilet seat       1.00      1.00      1.00         2
                     toilet tissue       0.20      0.50      0.29         2
                        totem pole       0.50      1.00      0.67         1
                            toucan       1.00      1.00      1.00         1
                         tow truck       0.50      1.00      0.67         1
                        toy poodle       0.00      0.00      0.00         1
                           toyshop       0.00      0.00      0.00         1
                           tractor       1.00      1.00      1.00         1
                     traffic light       1.00      0.50      0.67         2
                     trailer truck       1.00      1.00      1.00         1
                              tray       0.00      0.00      0.00         1
                         tree frog       1.00      1.00      1.00         1
                       trench coat       0.00      0.00      0.00         1
                       triceratops       0.00      0.00      0.00         2
                          tricycle       0.00      0.00      0.00         3
                            trifle       1.00      1.00      1.00         1
                         trilobite       0.50      1.00      0.67         1
                          trimaran       1.00      1.00      1.00         1
                            tripod       1.00      1.00      1.00         1
                    triumphal arch       0.50      1.00      0.67         1
                        trolleybus       0.00      0.00      0.00         1
                          trombone       0.00      0.00      0.00         1
                         turnstile       0.00      0.00      0.00         1
                            tusker       1.00      0.50      0.67         2
               typewriter keyboard       1.00      0.50      0.67         2
                          umbrella       0.50      0.50      0.50         2
                          unicycle       0.50      1.00      0.67         1
                           upright       0.50      1.00      0.67         1
                            vacuum       1.00      0.50      0.67         2
                            valley       1.00      0.50      0.67         2
                              vase       0.00      0.00      0.00         0
                             vault       1.00      0.33      0.50         3
                            velvet       0.00      0.00      0.00         1
                   vending machine       1.00      1.00      1.00         1
                           viaduct       1.00      1.00      1.00         1
                        vine snake       0.00      0.00      0.00         1
                            violin       1.00      1.00      1.00         1
                            vizsla       0.00      0.00      0.00         1
                           volcano       1.00      1.00      1.00         1
                        volleyball       1.00      1.00      1.00         1
                           vulture       0.00      0.00      0.00         1
                       waffle iron       0.00      0.00      0.00         1
                     walking stick       0.00      0.00      0.00         1
                        wall clock       1.00      1.00      1.00         2
                           wallaby       1.00      1.00      1.00         1
                            wallet       0.00      0.00      0.00         0
                          wardrobe       0.50      1.00      0.67         1
                          warplane       0.00      0.00      0.00         0
                           warthog       0.50      1.00      0.67         1
                         washbasin       0.00      0.00      0.00         3
                            washer       1.00      1.00      1.00         1
                     water buffalo       1.00      0.50      0.67         2
                         water jug       0.00      0.00      0.00         2
                       water ouzel       1.00      1.00      1.00         1
                       water snake       1.00      1.00      1.00         1
                       water tower       1.00      1.00      1.00         2
                            weasel       0.00      0.00      0.00         0
                          web site       1.00      0.33      0.50         3
                            weevil       0.00      0.00      0.00         1
                          whiptail       0.00      0.00      0.00         2
                       whiskey jug       1.00      1.00      1.00         1
                           whistle       1.00      1.00      1.00         1
                       white stork       1.00      1.00      1.00         1
                               wig       0.00      0.00      0.00         1
                         wild boar       0.00      0.00      0.00         1
                     window screen       1.00      0.50      0.67         2
                      window shade       1.00      1.00      1.00         1
                       wine bottle       0.00      0.00      0.00         1
                              wing       1.00      1.00      1.00         1
           wire-haired fox terrier       1.00      1.00      1.00         1
                       wolf spider       1.00      0.50      0.67         2
                            wombat       0.00      0.00      0.00         1
                       wood rabbit       0.00      0.00      0.00         0
                      wooden spoon       0.50      0.50      0.50         2
                              wool       0.00      0.00      0.00         2
                        worm fence       1.00      1.00      1.00         1
                             wreck       0.50      1.00      0.67         1
                              yawl       1.00      1.00      1.00         1
             yellow lady's slipper       1.00      1.00      1.00         1
                              yurt       1.00      1.00      1.00         1
                             zebra       0.00      0.00      0.00         1
                          zucchini       1.00      1.00      1.00         1
    
                          accuracy                           0.54      1000
                         macro avg       0.47      0.52      0.47      1000
                      weighted avg       0.53      0.54      0.51      1000
    
    

![imagenet_evaluation](https://cdn.voxel51.com/getting_started_model_dataset_zoo/notebook2/imagenet_evaluation.webp)

## Conclusion#

FiftyOne Zoo simplifies the process of working with computer vision datasets and models. It provides a valuable resource for researchers, developers, and enthusiasts.

### Further Exploration:#

  * Explore the [FiftyOne documentation](https://docs.voxel51.com/) for more advanced features.
  * Try different datasets and models from the Zoo.
  * Integrate FiftyOne Zoo into your computer vision workflows.



## Next Steps#

To continue exploring, check out:

  * [Getting Started with FiftyOne](https://beta-docs.voxel51.com/getting_started/)
  * [Other Datasets](https://beta-docs.voxel51.com/data/dataset_zoo/)
  * [Other Models](https://beta-docs.voxel51.com/models/model_zoo/)
  * Join our [Discord community](https://community.voxel51.com)
  * Follow us on [LinkedIn](https://www.linkedin.com/company/voxel51/)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
