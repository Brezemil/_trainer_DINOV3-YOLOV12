---
source_url: https://docs.voxel51.com/plugins/contributing_plugins.html
---

# Contributing Plugins#

This page describes how to share your FiftyOne plugins with the community.

Note

For complete plugin development documentation, see [Developing Plugins](plugins__developing_plugins.md#developing-plugins).

## Why share your plugin?#

By sharing your plugin, you:

  * Help others solve similar problems

  * Get feedback and contributions from the community

  * Showcase your work in the official plugin ecosystem

  * Build your reputation as a FiftyOne contributor




## Sharing via GitHub#

The simplest way to share a plugin is to publish it on GitHub:

  1. Create a public GitHub repository for your plugin

  2. Include a clear `README.md` with:

     * What the plugin does

     * Installation instructions

     * Usage examples with code snippets

     * Screenshots or GIFs showing the plugin in action




Users can then install your plugin directly:
    
    
    fiftyone plugins download https://github.com/your-username/your-plugin
    

## Submitting to the Plugin Ecosystem#

Get your plugin featured in the official [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem).

### How the Plugin Ecosystem works#

The [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem) page renders the README directly from your pluginâs GitHub repository. This means that whatever you write in your pluginâs README will be displayed in the documentation.

Make sure your README is well-crafted with clear descriptions, usage examples, and screenshotsâthis is exactly what users will see when browsing the plugin ecosystem.

### Submission process#

Follow these steps to submit your plugin:

  1. **Fork the repository** : Fork [voxel51/fiftyone-plugins](https://github.com/voxel51/fiftyone-plugins) on GitHub

  2. **Add your plugin to the community table** : Edit the README and add a new row that matches the content/formatting of the existing rows

  3. **Submit a pull request** : Create a PR with:

     * A clear title (e.g., âAdd my-awesome-plugin to community pluginsâ)

     * Brief description of what your plugin does

     * Category/tags for discoverability

  4. **Review process** : The FiftyOne team will review your PR. If everything looks good, your PR will be merged and your plugin will appear in the [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem)




## Quality checklist#

Before sharing your plugin, verify that it meets these requirements:

â | Has a clear, descriptive name  
---|---  
â | Includes a comprehensive README with installation and usage  
â | Handles errors gracefully with helpful messages  
â | Works with the latest FiftyOne version  
â | Does not hardcode secrets or sensitive data  
â | Has been tested on sample datasets  
  
## Ready to share your plugin?#

Once your plugin meets the quality checklist, submit it to the Plugin Ecosystem and join the growing community of FiftyOne plugin developers!

[ Submit your plugin ](https://github.com/voxel51/fiftyone-plugins)

## Getting help#

Need assistance with your plugin contribution?

  * **Discord** : Ask questions on [community.voxel51.com](https://community.voxel51.com/)

  * **Plugin examples** : Browse the [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem) for inspiration

  * **Development guide** : See [Developing Plugins](plugins__developing_plugins.md#developing-plugins) for complete documentation




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
