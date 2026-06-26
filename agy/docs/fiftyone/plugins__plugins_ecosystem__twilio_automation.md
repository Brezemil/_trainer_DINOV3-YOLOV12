---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/twilio_automation.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/twilio-automation-plugin)

# Twilio Automation Plugin#

![twilio](https://github.com/jacobmarks/twilio-automation-plugin/assets/12500356/5c25c312-9890-4bd3-b194-ca33ee0819fd)

This plugin is a Python plugin that allows you to automate data ingestion with [twilio](https://www.twilio.com/en-us). Take pictures with your phone and send them to a Twilio number. The plugin will automatically download the images and add them to your dataset.

This plugin is a direct byproduct of the hackathon at the [Twilio SIGNAL Creator Summit 2023](https://signal.twilio.com/2023/creator-summit).

This plugin demonstrates how to do the following:

  * use Python to create an operator with different options depending on user choices

  * add a custom operator icon via the operators `icon` property

  * download images from URL â with authentication â and add them to the dataset




# Installation#

## Twilio Setup#

Before installing this plugin, you must set up your Twilio account:

  1. [Create a Twilio account](https://www.twilio.com/try-twilio). Twilio offers a free trial, so you can try this out without paying anything.

  2. Buy (with the free trial credits) a toll-free phone number that can receive MMS messages. You can do this from the [Twilio Console](https://www.twilio.com/console/phone-numbers/search).

  3. Go to the [Twilio Console](https://console.twilio.com/) and copy the âAccount SIDâ, âAuth Tokenâ, and âMy Twilio phone numberâ values. Add these values as environment variables in your shell rc (`.bashrc`, `.zshrc`, etc.)):



    
    
    export TWILIO_ACCOUNT_SID=<your account SID>
    export TWILIO_AUTH_TOKEN=<your auth token>
    export TWILIO_PHONE_NUMBER=<your Twilio phone number>
    

You will need to restart your shell for these environment variables to take effect.

  4. Install the [twilio Python helper library](https://github.com/twilio/twilio-python/tree/main).



    
    
    pip install twilio
    

## Plugin Installation#

To install the plugin, run the following command:
    
    
    fiftyone plugins download https://github.com/jacobmarks/twilio-automation-plugin
    

# Operators#

## `add_twilio_images`#

Add images received by your Twilio number to the dataset. This operator only adds images that have not already been added to the dataset.

When you run the operator, it will download the images, assign them a filepath, and add them to the dataset with metadata.

### Filtering by message body#

When executing the operator, you can filter the images that are added to the dataset by the message body.

# Notes#

## Local datasets only#

This plugin is only meant for local datasets. If you are working with large-scale, remotely hosted datasets, you likely need a more robust solution [FiftyOne Teams](https://voxel51.com/fiftyone-teams/)

## Cost#

This plugin uses Twilioâs MMS service, which costs $0.02 message received. You can send up to 10 images per message, so the cost is $0.002 per image. If you are using the free trial, you will have $13 in credits left after buying a phone number, which is enough for 6,500 images.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
