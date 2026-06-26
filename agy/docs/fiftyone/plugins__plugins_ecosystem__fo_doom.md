---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/fo_doom.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/Burhan-Q/fo-doom)

[![](https://user-images.githubusercontent.com/25985824/106288517-2422e000-6216-11eb-871d-26ad2e7b1e59.png) ![](https://user-images.githubusercontent.com/25985824/106288518-24bb7680-6216-11eb-8f10-60052c519586.png)](https://voxel51.com/fiftyone/) [![FiftyOne, it runs Doom](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/runs-doom.png)](https://knowyourmeme.com/memes/it-runs-doom)

Play **DOOM** inside a [FiftyOne](https://docs.voxel51.com/) panel - right in your browser, powered by WebAssembly.

![FiftyOne Doom](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/fo-doom-run.webp)

# ![Overview](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/overview.png)#

This is a free and non-commercial [FiftyOne plugin](https://docs.voxel51.com/plugins/index.html) that embeds the DOOM engine as a playable panel inside the [FiftyOne App](https://docs.voxel51.com/user_guide/app.html). The game runs entirely locally in your browser - no remote servers. The engine is [Dwasm](https://github.com/GMH-Code/Dwasm), a WebAssembly port of [PrBoom+](https://prboom-plus.sourceforge.net/) compiled with [Emscripten](https://emscripten.org/). It provides native Web Audio output for full sound support (music and sound effects).

# ![Game Files \(WAD\)](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/game-files.png)#

**No WAD file is bundled with this plugin.** You must provide your own WAD file when launching the game. The WAD is cached in your browser after the first upload, so you only need to select it once.

The shareware version of DOOM (`doom1.wad`) is freely available and can be obtained from:

  * [DOOM Shareware on the Internet Archive](https://archive.org/details/DoomsharewareEpisode)

  * The original DOS shareware archive `doom19s.zip` (widely available online) - see the [Dwasm README](https://github.com/GMH-Code/Dwasm#playing-the-shareware-version-of-doom) for extraction instructions and file checksums




**Please only use legal copies and ensure you comply with the licences.** The shareware licence only permits duplication of the original archive; its contents cannot be distributed or embedded separately. Do not host commercial titles on a public server without permission from the copyright holder.

## ![Compatible WAD files](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/game-files.png)#

  * **DOOM1.WAD** \- Doom shareware (freely distributable)

  * **DOOM.WAD** \- Doom registered (full game)

  * **DOOM2.WAD** \- Doom II

  * **The Ultimate DOOM** , **Final DOOM** (TNT: Evilution, The Plutonia Experiment)

  * **HACX** , **Chex Quest**

  * **[FreeDoom](https://freedoom.github.io/)** \- Free, open-source WADs compatible with the Doom engine




Any total conversion mods based on these variants should also work.

# ![Requirements](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/requirements.png)#

  * [FiftyOne](https://github.com/voxel51/fiftyone) >= 1.13.0 ([install](https://docs.voxel51.com/getting_started/install.html))

  * A modern browser (tested on Firefox and Chrome)

  * A compatible WAD file (see above)




# ![Platform Compatibility](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/compatibility.png)#

This plugin was built and tested on **Linux**. It is unclear whether it will run correctly on other operating systems (macOS, Windows). If you encounter issues on another OS, please open an issue.

# ![Installation](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/compatibility.png)#

Install directly from GitHub using the FiftyOne CLI:
    
    
    fiftyone plugins download https://github.com/Burhan-Q/doom
    

Or using the Python SDK:
    
    
    import fiftyone.plugins as fop
    
    fop.download_plugin("https://github.com/Burhan-Q/doom")
    

Then restart your FiftyOne server. See the [FiftyOne plugins documentation](https://docs.voxel51.com/plugins/using_plugins.html) for more details on managing plugins.

# ![Usage](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/usage.png)#

  1. Launch the [FiftyOne App](https://docs.voxel51.com/user_guide/app.html)

  2. Open the command palette (press ``` or `+` icon to add a new panel)

  3. Search for **âPlay Doomâ** and execute it

  4. The DOOM panel opens with a WAD file selection screen

  5. Click **SELECT WAD FILE** and choose your WAD

  6. The game loads and starts automatically




Your WAD file is cached in the browser. On subsequent launches, the game loads automatically from the cache - no need to re-select the file. Use the âClear cached WADâ link to switch to a different WAD.

# ![Credits](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/credits.png)#

  * **DOOM** by [id Software](https://www.idsoftware.com/) (1993) see also [DOOM source code](https://github.com/id-Software/DOOM)

  * **Dwasm** (PrBoom+ WASM port) by [GMH-Code](https://github.com/GMH-Code/Dwasm)

  * **FiftyOne** by [Voxel51](https://voxel51.com/) \- [GitHub](https://github.com/voxel51/fiftyone) | [Docs](https://docs.voxel51.com/) | [Plugins](https://docs.voxel51.com/plugins/index.html)

  * **Header Images** by [eeveeâs](https://github.com/eevee) [DOOM text generator](https://github.com/eevee/doom-text-generator) see ATTRIBUTION.md for additional details




# ![Disclaimer](https://raw.githubusercontent.com/Burhan-Q/fo-doom/main/assets/disclaimer.png)#

This project is not affiliated with, endorsed by, or in any way connected to id Software, Bethesda Softworks, or ZeniMax Media. All trademarks and copyrights are the property of their respective owners.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
