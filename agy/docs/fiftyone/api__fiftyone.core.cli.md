---
source_url: https://docs.voxel51.com/api/fiftyone.core.cli.html
---

# fiftyone.core.cli#

Definition of the fiftyone command-line interface (CLI).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Command`() | Interface for defining commands.  
---|---  
`FiftyOneCommand`() | The FiftyOne command-line interface.  
`QuickstartCommand`() | Launch a FiftyOne quickstart.  
`ConfigCommand`() | Tools for working with your FiftyOne config.  
`ConstantsCommand`() | Print constants from fiftyone.constants.  
`ConvertCommand`() | Convert datasets on disk between supported formats.  
`DatasetsCommand`() | Tools for working with FiftyOne datasets.  
`DatasetsListCommand`() | List FiftyOne datasets.  
`DatasetsInfoCommand`() | Print information about FiftyOne datasets.  
`DatasetsStatsCommand`() | Print stats about FiftyOne datasets on disk.  
`DatasetsCreateCommand`() | Tools for creating FiftyOne datasets.  
`DatasetsHeadCommand`() | Prints the first few samples in a FiftyOne dataset.  
`DatasetsTailCommand`() | Prints the last few samples in a FiftyOne dataset.  
`DatasetsStreamCommand`() | Stream samples in a FiftyOne dataset to the terminal.  
`DatasetsExportCommand`() | Export FiftyOne datasets to disk in supported formats.  
`DatasetsDrawCommand`() | Renders annotated versions of samples in FiftyOne datasets to disk.  
`DatasetsRenameCommand`() | Rename FiftyOne datasets.  
`DatasetsDeleteCommand`() | Delete FiftyOne datasets.  
`AnnotationCommand`() | Tools for working with the FiftyOne annotation API.  
`AnnotationConfigCommand`() | Tools for working with your FiftyOne annotation config.  
`AppCommand`() | Tools for working with the FiftyOne App.  
`AppConfigCommand`() | Tools for working with your FiftyOne App config.  
`AppLaunchCommand`() | Launch the FiftyOne App.  
`AppDebugCommand`() | Launch the FiftyOne App in debug mode.  
`AppViewCommand`() | View datasets in the App without persisting them to the database.  
`AppConnectCommand`() | Connect to a remote FiftyOne App in your web browser.  
`BrainCommand`() | Tools for working with the FiftyOne Brain.  
`BrainConfigCommand`() | Tools for working with your FiftyOne Brain config.  
`EvaluationCommand`() | Tools for working with the FiftyOne evaluation API.  
`EvaluationConfigCommand`() | Tools for working with your FiftyOne evaluation config.  
`ZooCommand`() | Tools for working with the FiftyOne Zoo.  
`DatasetZooCommand`() | Tools for working with the FiftyOne Dataset Zoo.  
`DatasetZooListCommand`() | List datasets in the FiftyOne Dataset Zoo.  
`DatasetZooFindCommand`() | Locate a downloaded zoo dataset on disk.  
`DatasetZooInfoCommand`() | Print information about datasets in the FiftyOne Dataset Zoo.  
`DatasetZooDownloadCommand`() | Download zoo datasets.  
`DatasetZooLoadCommand`() | Load zoo datasets as persistent FiftyOne datasets.  
`DatasetZooDeleteCommand`() | Deletes the local copy of the zoo dataset on disk.  
`ModelZooCommand`() | Tools for working with the FiftyOne Model Zoo.  
`ModelZooListCommand`() | List models in the FiftyOne Model Zoo.  
`ModelZooFindCommand`() | Locate the downloaded zoo model on disk.  
`ModelZooInfoCommand`() | Print information about models in the FiftyOne Model Zoo.  
`ModelZooRequirementsCommand`() | Handles package requirements for zoo models.  
`ModelZooDownloadCommand`() | Download zoo models.  
`ModelZooApplyCommand`() | Apply zoo models to datasets.  
`ModelZooEmbedCommand`() | Generate embeddings for datasets with zoo models.  
`ModelZooDeleteCommand`() | Deletes the local copy of the zoo model on disk.  
`ModelZooListSourcesCommand`() | Lists remote zoo model sources that are registered locally.  
`ModelZooRegisterSourceCommand`() | Registers a remote source of zoo models.  
`ModelZooDeleteSourceCommand`() | Deletes the remote source and all downloaded models associated with it.  
`OperatorsCommand`() | Tools for working with FiftyOne operators and panels.  
`OperatorsListCommand`() | List operators and panels that are installed locally.  
`OperatorsInfoCommand`() | Prints info about operators and panels that are installed locally.  
`DelegatedCommand`() | Tools for working with FiftyOne delegated operations.  
`DelegatedRerunCommand`() | Rerun delegated operations  
`DelegatedLaunchCommand`() | Launches a service for running delegated operations.  
`DelegatedListCommand`() | List delegated operations.  
`DelegatedInfoCommand`() | Prints information about a delegated operation.  
`DelegatedOutputCommand`() | Prints the output for a delegated operation.  
`DelegatedFailCommand`() | Manually mark delegated operations as failed.  
`DelegatedDeleteCommand`() | Delete delegated operations.  
`DelegatedArchiveCommand`() | Archive delegated operations.  
`DelegatedCleanupCommand`() | Cleanup delegated operations.  
`PluginsCommand`() | Tools for working with FiftyOne plugins.  
`PluginsListCommand`() | List plugins that are installed locally.  
`PluginsInfoCommand`() | Prints info about plugins that are installed locally.  
`PluginsDownloadCommand`() | Download plugins from the web.  
`PluginsSearchCommand`() | Search for available plugins in a GitHub repository.  
`PluginsRequirementsCommand`() | Handles package requirements for plugins.  
`PluginsCreateCommand`() | Creates or initializes a plugin.  
`PluginsEnableCommand`() | Enables the given plugin(s).  
`PluginsDisableCommand`() | Disables the given plugin(s).  
`PluginsDeleteCommand`() | Delete plugins from your local machine.  
`SkillsCommand`() | Tools for working with FiftyOne skills.  
`SkillsListCommand`() | List skills provided by installed plugins.  
`LabsCommand`() | Tools for working with FiftyOne Labs.  
`LabsInstallCommand`() | Install FiftyOne Labs features on your local machine.  
`LabsUninstallCommand`() | Uninstall FiftyOne Labs features from your local machine.  
`LabsListCommand`() | List installed FiftyOne Labs features on your local machine.  
`LabsSearchCommand`() | Search for available FiftyOne Labs features.  
`MigrateCommand`() | Tools for migrating the FiftyOne database.  
`UtilsCommand`() | FiftyOne utilities.  
`ComputeMetadataCommand`() | Populates the metadata field of all samples in the dataset.  
`TransformImagesCommand`() | Transforms the images in a dataset per the specified parameters.  
`TransformVideosCommand`() | Transforms the videos in a dataset per the specified parameters.  
  
**Functions:**

`main`() | Executes the fiftyone tool with the given command-line args.  
---|---  
  
class fiftyone.core.cli.Command#
    

Bases: `object`

Interface for defining commands.

Command instances must implement the setup() method, and they should implement the execute() method if they perform any functionality beyond defining subparsers.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.FiftyOneCommand#
    

Bases: `Command`

The FiftyOne command-line interface.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.QuickstartCommand#
    

Bases: `Command`

Launch a FiftyOne quickstart.

Examples:
    
    
    # Launch the quickstart
    fiftyone quickstart
    
    # Launch the quickstart with a video dataset
    fiftyone quickstart --video
    
    # Launch the quickstart as a remote session
    fiftyone quickstart --remote
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ConfigCommand#
    

Bases: `Command`

Tools for working with your FiftyOne config.

Examples:
    
    
    # Print your entire config
    fiftyone config
    
    # Print a specific config field
    fiftyone config <field>
    
    # Print the location of your config on disk (if one exists)
    fiftyone config --locate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ConstantsCommand#
    

Bases: `Command`

Print constants from fiftyone.constants.

Examples:
    
    
    # Print all constants
    fiftyone constants
    
    # Print a specific constant
    fiftyone constants <CONSTANT>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ConvertCommand#
    

Bases: `Command`

Convert datasets on disk between supported formats.

Examples:
    
    
    # Convert an image classification directory tree to TFRecords format
    fiftyone convert \
        --input-dir /path/to/image-classification-directory-tree \
        --input-type fiftyone.types.ImageClassificationDirectoryTree \
        --output-dir /path/for/tf-image-classification-dataset \
        --output-type fiftyone.types.TFImageClassificationDataset
    
    # Convert a COCO detection dataset to CVAT image format
    fiftyone convert \
        --input-dir /path/to/coco-detection-dataset \
        --input-type fiftyone.types.COCODetectionDataset \
        --output-dir /path/for/cvat-image-dataset \
        --output-type fiftyone.types.CVATImageDataset
    
    # Perform a customized conversion via optional kwargs
    fiftyone convert \
        --input-dir /path/to/coco-detection-dataset \
        --input-type fiftyone.types.COCODetectionDataset \
        --input-kwargs max_samples=100 shuffle=True \
        --output-dir /path/for/cvat-image-dataset \
        --output-type fiftyone.types.TFObjectDetectionDataset \
        --output-kwargs force_rgb=True \
        --overwrite
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsCommand#
    

Bases: `Command`

Tools for working with FiftyOne datasets.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsListCommand#
    

Bases: `Command`

List FiftyOne datasets.

Examples:
    
    
    # List available datasets
    fiftyone datasets list
    
    # List datasets matching a given pattern
    fiftyone datasets list --glob-patt 'quickstart-*'
    
    # List datasets with the given tag(s)
    fiftyone datasets list --tags automotive healthcare
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsInfoCommand#
    

Bases: `Command`

Print information about FiftyOne datasets.

Examples:
    
    
    # Print basic information about multiple datasets
    fiftyone datasets info
    fiftyone datasets info --glob-patt 'quickstart-*'
    fiftyone datasets info --tags automotive healthcare
    fiftyone datasets info --sort-by created_at
    fiftyone datasets info --sort-by name --reverse
    
    # Print information about a specific dataset
    fiftyone datasets info <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsStatsCommand#
    

Bases: `Command`

Print stats about FiftyOne datasets on disk.

Examples:
    
    
    # Print stats about the given dataset on disk
    fiftyone datasets stats <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsCreateCommand#
    

Bases: `Command`

Tools for creating FiftyOne datasets.

Examples:
    
    
    # Create a dataset from the given data on disk
    fiftyone datasets create \
        --name <name> --dataset-dir <dataset-dir> --type <type>
    
    # Create a dataset from a random subset of the data on disk
    fiftyone datasets create \
        --name <name> --dataset-dir <dataset-dir> --type <type> \
        --kwargs max_samples=50 shuffle=True
    
    # Create a dataset from the given samples JSON file
    fiftyone datasets create --json-path <json-path>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsHeadCommand#
    

Bases: `Command`

Prints the first few samples in a FiftyOne dataset.

Examples:
    
    
    # Print the first few samples in a dataset
    fiftyone datasets head <name>
    
    # Print the given number of samples from the head of a dataset
    fiftyone datasets head <name> --num-samples <num-samples>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsTailCommand#
    

Bases: `Command`

Prints the last few samples in a FiftyOne dataset.

Examples:
    
    
    # Print the last few samples in a dataset
    fiftyone datasets tail <name>
    
    # Print the given number of samples from the tail of a dataset
    fiftyone datasets tail <name> --num-samples <num-samples>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsStreamCommand#
    

Bases: `Command`

Stream samples in a FiftyOne dataset to the terminal.

Examples:
    
    
    # Stream the samples of the dataset to the terminal
    fiftyone datasets stream <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsExportCommand#
    

Bases: `Command`

Export FiftyOne datasets to disk in supported formats.

Examples:
    
    
    # Export the dataset to disk in the specified format
    fiftyone datasets export <name> \
        --export-dir <export-dir> --type <type> --label-field <label-field>
    
    # Export the dataset to disk in JSON format
    fiftyone datasets export <name> --json-path <json-path>
    
    # Only export cats and dogs from the validation split
    fiftyone datasets export <name> \
        --filters tags=validation ground_truth=cat,dog \
        --export-dir <export-dir> --type <type> --label-field ground_truth
    
    # Perform a customized export of a dataset
    fiftyone datasets export <name> \
        --type <type> \
        --kwargs labels_path=/path/for/labels.json
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsDrawCommand#
    

Bases: `Command`

Renders annotated versions of samples in FiftyOne datasets to disk.

Examples:
    
    
    # Write annotated versions of the media in the dataset with the
    # specified label field(s) overlaid to disk
    fiftyone datasets draw <name> \
        --output-dir <output-dir> --label-fields <list>,<of>,<fields>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsRenameCommand#
    

Bases: `Command`

Rename FiftyOne datasets.

Examples:
    
    
    # Rename the dataset
    fiftyone datasets rename <old-name> <new-name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetsDeleteCommand#
    

Bases: `Command`

Delete FiftyOne datasets.

Examples:
    
    
    # Delete the datasets with the given name(s)
    fiftyone datasets delete <name1> <name2> ...
    
    # Delete the datasets whose names match the given glob pattern
    fiftyone datasets delete --glob-patt <glob-patt>
    
    # Delete all non-persistent datasets
    fiftyone datasets delete --non-persistent
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AnnotationCommand#
    

Bases: `Command`

Tools for working with the FiftyOne annotation API.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AnnotationConfigCommand#
    

Bases: `Command`

Tools for working with your FiftyOne annotation config.

Examples:
    
    
    # Print your entire annotation config
    fiftyone annotation config
    
    # Print a specific annotation config field
    fiftyone annotation config <field>
    
    # Print the location of your annotation config on disk (if one exists)
    fiftyone annotation config --locate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppCommand#
    

Bases: `Command`

Tools for working with the FiftyOne App.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppConfigCommand#
    

Bases: `Command`

Tools for working with your FiftyOne App config.

Examples:
    
    
    # Print your entire App config
    fiftyone app config
    
    # Print a specific App config field
    fiftyone app config <field>
    
    # Print the location of your App config on disk (if one exists)
    fiftyone app config --locate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppLaunchCommand#
    

Bases: `Command`

Launch the FiftyOne App.

Examples:
    
    
    # Launch the App
    fiftyone app launch
    
    # Launch the App with the given dataset loaded
    fiftyone app launch <name>
    
    # Launch a remote App session
    fiftyone app launch ... --remote
    
    # Launch the App in the non-default browser
    fiftyone app launch ... --browser firefox
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppDebugCommand#
    

Bases: `Command`

Launch the FiftyOne App in debug mode.

Examples:
    
    
    # Launch the App in debug mode
    fiftyone app debug
    
    # Launch the App in debug mode with a given dataset loaded
    fiftyone app debug <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppViewCommand#
    

Bases: `Command`

View datasets in the App without persisting them to the database.

Examples:
    
    
    # View a dataset stored on disk in the App
    fiftyone app view --dataset-dir <dataset-dir> --type <type>
    
    # View a zoo dataset in the App
    fiftyone app view --zoo-dataset <name> --splits <split1> ...
    
    # View a directory of images in the App
    fiftyone app view --images-dir <images-dir>
    
    # View a glob pattern of images in the App
    fiftyone app view --images-patt <images-patt>
    
    # View a directory of videos in the App
    fiftyone app view --videos-dir <videos-dir>
    
    # View a glob pattern of videos in the App
    fiftyone app view --videos-patt <videos-patt>
    
    # View a dataset stored in JSON format on disk in the App
    fiftyone app view --json-path <json-path>
    
    # View the dataset in a remote App session
    fiftyone app view ... --remote
    
    # View a random subset of the data stored on disk in the App
    fiftyone app view ... --kwargs max_samples=50 shuffle=True
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.AppConnectCommand#
    

Bases: `Command`

Connect to a remote FiftyOne App in your web browser.

Examples:
    
    
    # Connect to a remote App with port forwarding already configured
    fiftyone app connect
    
    # Connect to a remote App session
    fiftyone app connect --destination <destination> --port <port>
    
    # Connect to a remote App session using an ssh key
    fiftyone app connect ... --ssh-key <path/to/key>
    
    # Connect to a remote App using a custom local port
    fiftyone app connect ... --local-port <port>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.BrainCommand#
    

Bases: `Command`

Tools for working with the FiftyOne Brain.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.BrainConfigCommand#
    

Bases: `Command`

Tools for working with your FiftyOne Brain config.

Examples:
    
    
    # Print your entire brain config
    fiftyone brain config
    
    # Print a specific brain config field
    fiftyone brain config <field>
    
    # Print the location of your brain config on disk (if one exists)
    fiftyone brain config --locate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.EvaluationCommand#
    

Bases: `Command`

Tools for working with the FiftyOne evaluation API.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.EvaluationConfigCommand#
    

Bases: `Command`

Tools for working with your FiftyOne evaluation config.

Examples:
    
    
    # Print your entire evaluation config
    fiftyone evaluation config
    
    # Print a specific evaluation config field
    fiftyone evaluation config <field>
    
    # Print the location of your evaluation config on disk (if one exists)
    fiftyone evaluation config --locate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ZooCommand#
    

Bases: `Command`

Tools for working with the FiftyOne Zoo.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooCommand#
    

Bases: `Command`

Tools for working with the FiftyOne Dataset Zoo.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooListCommand#
    

Bases: `Command`

List datasets in the FiftyOne Dataset Zoo.

Examples:
    
    
    # List available datasets
    fiftyone zoo datasets list
    
    # List available dataset names
    fiftyone zoo datasets list --names-only
    
    # List downloaded datasets
    fiftyone zoo datasets list --downloaded-only
    
    # List available datasets from the given source
    fiftyone zoo datasets list --source <source>
    
    # List available datasets with the given tag
    fiftyone zoo datasets list --tags <tag>
    
    # List available datasets with the given license
    fiftyone zoo datasets list --license <license>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooFindCommand#
    

Bases: `Command`

Locate a downloaded zoo dataset on disk.

Examples:
    
    
    # Print the location of a downloaded zoo dataset on disk
    fiftyone zoo datasets find <name>
    
    # Print the location of a remotely-sourced zoo dataset on disk
    fiftyone zoo datasets find https://github.com/<user>/<repo>
    fiftyone zoo datasets find <url>
    
    # Print the location of a specific split of a dataset
    fiftyone zoo datasets find <name> --split <split>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooInfoCommand#
    

Bases: `Command`

Print information about datasets in the FiftyOne Dataset Zoo.

Examples:
    
    
    # Print information about a zoo dataset
    fiftyone zoo datasets info <name>
    
    # Print information about a remote zoo dataset
    fiftyone zoo datasets info https://github.com/<user>/<repo>
    fiftyone zoo datasets info <url>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooDownloadCommand#
    

Bases: `Command`

Download zoo datasets.

When downloading remotely-sourced zoo datasets, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Download a zoo dataset
    fiftyone zoo datasets download <name>
    
    # Download a remotely-sourced zoo dataset
    fiftyone zoo datasets download https://github.com/<user>/<repo>
    fiftyone zoo datasets download <url>
    
    # Download the specified split(s) of a zoo dataset
    fiftyone zoo datasets download <name> --splits <split1> ...
    
    # Download a zoo dataset that requires extra keyword arguments
    fiftyone zoo datasets download <name> \
        --kwargs source_dir=/path/to/source/files
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooLoadCommand#
    

Bases: `Command`

Load zoo datasets as persistent FiftyOne datasets.

When loading remotely-sourced zoo datasets, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Load the zoo dataset with the given name
    fiftyone zoo datasets load <name>
    
    # Load a remotely-sourced zoo dataset
    fiftyone zoo datasets load https://github.com/<user>/<repo>
    fiftyone zoo datasets load <url>
    
    # Load the specified split(s) of a zoo dataset
    fiftyone zoo datasets load <name> --splits <split1> ...
    
    # Load a zoo dataset with a custom name
    fiftyone zoo datasets load <name> --dataset-name <dataset-name>
    
    # Load a zoo dataset that requires custom keyword arguments
    fiftyone zoo datasets load <name> \
        --kwargs source_dir=/path/to/source_files
    
    # Load a random subset of a zoo dataset
    fiftyone zoo datasets load <name> \
        --kwargs max_samples=50 shuffle=True
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DatasetZooDeleteCommand#
    

Bases: `Command`

Deletes the local copy of the zoo dataset on disk.

Examples:
    
    
    # Delete a zoo dataset from disk
    fiftyone zoo datasets delete <name>
    
    # Delete a remotely-sourced zoo dataset from disk
    fiftyone zoo datasets delete https://github.com/<user>/<repo>
    fiftyone zoo datasets delete <url>
    
    # Delete a specific split of a zoo dataset from disk
    fiftyone zoo datasets delete <name> --split <split>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooCommand#
    

Bases: `Command`

Tools for working with the FiftyOne Model Zoo.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooListCommand#
    

Bases: `Command`

List models in the FiftyOne Model Zoo.

Examples:
    
    
    # List available models
    fiftyone zoo models list
    
    # List available models (names only)
    fiftyone zoo models list --names-only
    
    # List downloaded models
    fiftyone zoo models list --downloaded-only
    
    # List available models with the given tag
    fiftyone zoo models list --tags <tag>
    
    # List available models from the given remote source
    fiftyone zoo models list --source <source>
    
    # List available models with the given license
    fiftyone zoo models list --license <license>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooFindCommand#
    

Bases: `Command`

Locate the downloaded zoo model on disk.

Examples:
    
    
    # Print the location of the downloaded zoo model on disk
    fiftyone zoo models find <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooInfoCommand#
    

Bases: `Command`

Print information about models in the FiftyOne Model Zoo.

Examples:
    
    
    # Print information about a zoo model
    fiftyone zoo models info <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooRequirementsCommand#
    

Bases: `Command`

Handles package requirements for zoo models.

Examples:
    
    
    # Print requirements for a zoo model
    fiftyone zoo models requirements <name> --print
    
    # Install any requirements for the zoo model
    fiftyone zoo models requirements <name> --install
    
    # Ensures that the requirements for the zoo model are satisfied
    fiftyone zoo models requirements <name> --ensure
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooDownloadCommand#
    

Bases: `Command`

Download zoo models.

When downloading remotely-sourced zoo models, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Download a zoo model
    fiftyone zoo models download <name>
    
    # Download a remotely-sourced zoo model
    fiftyone zoo models download https://github.com/<user>/<repo> \
        --model-name <name>
    fiftyone zoo models download <url> --model-name <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooApplyCommand#
    

Bases: `Command`

Apply zoo models to datasets.

When applying remotely-sourced zoo models, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Apply a zoo model to a dataset
    fiftyone zoo models apply <model-name> <dataset-name> <label-field>
    
    # Apply a remotely-sourced zoo model to a dataset
    fiftyone zoo models apply https://github.com/<user>/<repo> \
        <dataset-name> <label-field> --model-name <model-name>
    fiftyone zoo models apply <url> \
        <dataset-name> <label-field> --model-name <model-name>
    
    # Apply a zoo model with some customized parameters
    fiftyone zoo models apply \
        <model-name> <dataset-name> <label-field> \
        --confidence-thresh 0.7 \
        --store-logits \
        --batch-size 32
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooEmbedCommand#
    

Bases: `Command`

Generate embeddings for datasets with zoo models.

When applying remotely-sourced zoo models, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Generate embeddings for a dataset with a zoo model
    fiftyone zoo models embed <model-name> <dataset-name> <embeddings-field>
    
    # Generate embeddings for a dataset with a remotely-sourced zoo model
    fiftyone zoo models embed https://github.com/<user>/<repo> \
        <dataset-name> <embeddings-field> --model-name <model-name>
    fiftyone zoo models embed <url> \
        <dataset-name> <embeddings-field> --model-name <model-name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooDeleteCommand#
    

Bases: `Command`

Deletes the local copy of the zoo model on disk.

Examples:
    
    
    # Delete the zoo model from disk
    fiftyone zoo models delete <name>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooListSourcesCommand#
    

Bases: `Command`

Lists remote zoo model sources that are registered locally.

Examples:
    
    
    # Lists the registered remote zoo model sources
    fiftyone zoo models list-sources
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooRegisterSourceCommand#
    

Bases: `Command`

Registers a remote source of zoo models.

You can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Register a remote zoo model source
    fiftyone zoo models register-source https://github.com/<user>/<repo>
    fiftyone zoo models register-source <url>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ModelZooDeleteSourceCommand#
    

Bases: `Command`

Deletes the remote source and all downloaded models associated with it.

You can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`

  * a publicly accessible URL of an archive (eg zip or tar) file




Examples:
    
    
    # Delete a remote zoo model source
    fiftyone zoo models delete-source https://github.com/<user>/<repo>
    fiftyone zoo models delete-source <url>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.OperatorsCommand#
    

Bases: `Command`

Tools for working with FiftyOne operators and panels.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.OperatorsListCommand#
    

Bases: `Command`

List operators and panels that are installed locally.

Examples:
    
    
    # List all available operators and panels
    fiftyone operators list
    
    # List operators and panels whose URI matches the given glob pattern
    fiftyone operators list --glob-patt '*/compute_*'
    
    # List enabled operators and panels
    fiftyone operators list --enabled
    
    # List disabled operators and panels
    fiftyone operators list --disabled
    
    # List non-builtin operators and panels
    fiftyone operators list --no-builtins
    
    # List panels
    fiftyone operators list --panels-only
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.OperatorsInfoCommand#
    

Bases: `Command`

Prints info about operators and panels that are installed locally.

Examples:
    
    
    # Prints information about an operator or panel
    fiftyone operators info <uri>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedCommand#
    

Bases: `Command`

Tools for working with FiftyOne delegated operations.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedRerunCommand#
    

Bases: `Command`

Rerun delegated operations

Examples:
    
    
    # Rerun the given operation id
    fiftyone delegated rerun <operation-id>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedLaunchCommand#
    

Bases: `Command`

Launches a service for running delegated operations.

Examples:
    
    
    # Launch a local service
    fiftyone delegated launch
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedListCommand#
    

Bases: `Command`

List delegated operations.

Examples:
    
    
    # List all delegated operations
    fiftyone delegated list
    
    # List some specific delegated operations
    fiftyone delegated list \
        --dataset quickstart \
        --operator @voxel51/io/export_samples \
        --state COMPLETED \
        --sort-by COMPLETED_AT \
        --limit 10
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedInfoCommand#
    

Bases: `Command`

Prints information about a delegated operation.

Examples:
    
    
    # Print information about a delegated operation
    fiftyone delegated info <id>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedOutputCommand#
    

Bases: `Command`

Prints the output for a delegated operation.

Examples:
    
    
    # Print the output for a delegated operation
    fiftyone delegated output <id>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedFailCommand#
    

Bases: `Command`

Manually mark delegated operations as failed.

Examples:
    
    
    # Manually mark the specified operation(s) as FAILED
    fiftyone delegated fail <id1> <id2> ...
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedDeleteCommand#
    

Bases: `Command`

Delete delegated operations.

Examples:
    
    
    # Delete the specified operation(s)
    fiftyone delegated delete <id1> <id2> ...
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedArchiveCommand#
    

Bases: `Command`

Archive delegated operations.

Examples:
    
    
    # Archive the specified operation(s)
    fiftyone delegated archive <id1> <id2> ...
    
    # Unarchive the specified operation(s)
    fiftyone delegated archive <id1> <id2> ... --unarchive
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.DelegatedCleanupCommand#
    

Bases: `Command`

Cleanup delegated operations.

Examples:
    
    
    # Delete all failed operations associated with a given dataset
    fiftyone delegated cleanup --dataset quickstart --state FAILED
    
    # Delete all delegated operations associated with non-existent datasets
    fiftyone delegated cleanup --orphan
    
    # Print information about operations rather than actually deleting them
    fiftyone delegated cleanup --orphan --dry-run
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsCommand#
    

Bases: `Command`

Tools for working with FiftyOne plugins.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsListCommand#
    

Bases: `Command`

List plugins that are installed locally.

Examples:
    
    
    # List all available plugins
    fiftyone plugins list
    
    # List plugins whose name matches the given glob pattern
    fiftyone plugins list --glob-patt '@voxel51/*'
    
    # List plugins with the given tag
    fiftyone plugins list --tags <tag>
    
    # List enabled plugins
    fiftyone plugins list --enabled
    
    # List disabled plugins
    fiftyone plugins list --disabled
    
    # List non-builtin plugins
    fiftyone plugins list --no-builtins
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsInfoCommand#
    

Bases: `Command`

Prints info about plugins that are installed locally.

Examples:
    
    
    # Prints information about a plugin
    fiftyone plugins info <name>
    
    # Prints information about a plugin in a given directory
    fiftyone plugins info <dir>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsDownloadCommand#
    

Bases: `Command`

Download plugins from the web.

When downloading plugins from GitHub, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`




Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Download plugins from a GitHub repository URL
    fiftyone plugins download <github-repo-url>
    
    # Download plugins by specifying the GitHub repository details
    fiftyone plugins download <user>/<repo>[/<ref>]
    
    # Download specific plugins from a URL
    fiftyone plugins download <url> --plugin-names <name1> <name2> <name3>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsSearchCommand#
    

Bases: `Command`

Search for available plugins in a GitHub repository.

When searching for plugins, you can provide any of the following formats:

  * a GitHub repo URL like `https://github.com/<user>/<repo>`

  * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * a GitHub ref string like `<user>/<repo>[/<ref>]`




Note

To read from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Examples:
    
    
    # Search for plugins by specifying a GitHub repository URL
    fiftyone plugins search <github-repo-url>
    
    # Search for plugins by specifying the GitHub repository details
    fiftyone plugins search <user>/<repo>[/<ref>]
    
    # Search for plugins by specifying a path inside the repository
    fiftyone plugins search <github-repo-url> --path path/to/dir
    fiftyone plugins search <user>/<repo>[/<ref>] --path path/to/dir
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsRequirementsCommand#
    

Bases: `Command`

Handles package requirements for plugins.

Examples:
    
    
    # Print requirements for a plugin
    fiftyone plugins requirements <name> --print
    
    # Install any requirements for the plugin
    fiftyone plugins requirements <name> --install
    
    # Ensures that the requirements for the plugin are satisfied
    fiftyone plugins requirements <name> --ensure
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsCreateCommand#
    

Bases: `Command`

Creates or initializes a plugin.

Examples:
    
    
    # Initialize a new plugin
    fiftyone plugins create <name>
    
    # Create a plugin from existing files
    fiftyone plugins create \
        <name> \
        --from-files /path/to/dir \
        --description <description>
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsEnableCommand#
    

Bases: `Command`

Enables the given plugin(s).

Examples:
    
    
    # Enable a plugin
    fiftyone plugins enable <name>
    
    # Enable multiple plugins
    fiftyone plugins enable <name1> <name2> ...
    
    # Enable all plugins
    fiftyone plugins enable --all
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsDisableCommand#
    

Bases: `Command`

Disables the given plugin(s).

Examples:
    
    
    # Disable a plugin
    fiftyone plugins disable <name>
    
    # Disable multiple plugins
    fiftyone plugins disable <name1> <name2> ...
    
    # Disable all plugins
    fiftyone plugins disable --all
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.PluginsDeleteCommand#
    

Bases: `Command`

Delete plugins from your local machine.

Examples:
    
    
    # Delete a plugin from local disk
    fiftyone plugins delete <name>
    
    # Delete multiple plugins from local disk
    fiftyone plugins delete <name1> <name2> ...
    
    # Delete all plugins from local disk
    fiftyone plugins delete --all
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.SkillsCommand#
    

Bases: `Command`

Tools for working with FiftyOne skills.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.SkillsListCommand#
    

Bases: `Command`

List skills provided by installed plugins.

Examples:
    
    
    # List all available skills
    fiftyone skills list
    
    # List skills from a specific plugin
    fiftyone skills list --plugin @voxel51/my-plugin
    
    # List skills in a specific category
    fiftyone skills list --category data-ingestion
    
    # List enabled skills
    fiftyone skills list --enabled
    
    # List skill names only
    fiftyone skills list --names-only
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.LabsCommand#
    

Bases: `Command`

Tools for working with FiftyOne Labs.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.LabsInstallCommand#
    

Bases: `Command`

Install FiftyOne Labs features on your local machine.

Examples:
    
    
    # Install specific FiftyOne labs feature(s)
    fiftyone labs install <name1> <name2> ...
    
    # Install all FiftyOne Labs features
    fiftyone labs install --all
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.LabsUninstallCommand#
    

Bases: `Command`

Uninstall FiftyOne Labs features from your local machine.

Examples:
    
    
    # Uninstall specific Labs feature(s)
    fiftyone labs uninstall <name1> <name2> ...
    
    # Uninstall all Labs features
    fiftyone labs uninstall --all
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.LabsListCommand#
    

Bases: `Command`

List installed FiftyOne Labs features on your local machine.

Examples:
    
    
    # List installed Labs features
    fiftyone labs list
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.LabsSearchCommand#
    

Bases: `Command`

Search for available FiftyOne Labs features.

Examples:
    
    
    # List available Labs features
    fiftyone labs search
    
    # List available Labs features in a specific Labs repository branch
    fiftyone labs search --branch <branch_name>
    
    # List available Labs features in a specific Labs repository directory
    fiftyone labs search --path path/to/dir
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.MigrateCommand#
    

Bases: `Command`

Tools for migrating the FiftyOne database.

See [this page](user_guide__config.md#database-migrations) for more information about migrating FiftyOne deployments.

Examples:
    
    
    # Print information about the current revisions of all datasets
    fiftyone migrate --info
    
    # Migrate the database and all datasets to the current client version
    fiftyone migrate --all
    
    # Migrate to a specific revision
    fiftyone migrate --all --version <VERSION>
    
    # Migrate a specific dataset
    fiftyone migrate ... --dataset-name <DATASET_NAME>
    
    # Update the database version without migrating any existing datasets
    fiftyone migrate
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.UtilsCommand#
    

Bases: `Command`

FiftyOne utilities.

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.ComputeMetadataCommand#
    

Bases: `Command`

Populates the metadata field of all samples in the dataset.

Examples:
    
    
    # Populate all missing `metadata` sample fields
    fiftyone utils compute-metadata <dataset-name>
    
    # (Re)-populate the `metadata` field for all samples
    fiftyone utils compute-metadata <dataset-name> --overwrite
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.TransformImagesCommand#
    

Bases: `Command`

Transforms the images in a dataset per the specified parameters.

Examples:
    
    
    # Convert the images in the dataset to PNGs
    fiftyone utils transform-images <dataset-name> --ext .png --delete-originals
    
    # Ensure that no images in the dataset exceed 1920 x 1080
    fiftyone utils transform-images <dataset-name> --max-size 1920,1080
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




class fiftyone.core.cli.TransformVideosCommand#
    

Bases: `Command`

Transforms the videos in a dataset per the specified parameters.

Examples:
    
    
    # Re-encode the videos in the dataset as H.264 MP4s
    fiftyone utils transform-videos <dataset-name> --reencode
    
    # Ensure that no videos in the dataset exceed 1920 x 1080 and 30fps
    fiftyone utils transform-videos <dataset-name> \
        --max-size 1920,1080 --max-fps 30.0
    

**Methods:**

`setup`(parser) | Setup the command-line arguments for the command.  
---|---  
`execute`(parser,Â args) | Executes the command on the given args.  
  
static setup(_parser_)#
    

Setup the command-line arguments for the command.

Parameters:
    

**parser** â an argparse.ArgumentParser instance

static execute(_parser_ , _args_)#
    

Executes the command on the given args.

Parameters:
    

  * **parser** â the argparse.ArgumentParser instance for the command

  * **args** â an argparse.Namespace instance containing the arguments for the command




fiftyone.core.cli.main()#
    

Executes the fiftyone tool with the given command-line args.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
