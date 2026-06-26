---
source_url: https://docs.voxel51.com/agents/using_agents.html
---

# Using Agents#

## What Are Skills and MCP?#

Skills and MCP solve different parts of the same problem. MCP is about connection: it lets an agent talk to real systems, run real operations, and get real results instead of just generating text. Skills are about guidance: they teach the agent how to use those capabilities correctly for a specific task. MCP exposes what the system can do, while skills explain how and when to do it.

On their own, tools are powerful but ambiguous. Skills turn those tools into repeatable workflows. They encode experience, decisions, and guardrails. Together, they let agents move from _âI can call functionsâ_ to _âI know how to complete this task end to end.â_

### Two Parts, One System#

**FiftyOne MCP Server** connects agents to FiftyOneâs 80+ operators, dataset management, model inference, brain computations, and the App. It implements the open [Model Context Protocol](https://modelcontextprotocol.io) standard, giving any compatible agent direct access to your data and tools.

**FiftyOne Skills** are expert workflows built on top. Each skill teaches the agent how to complete a specific task: import data, find duplicates, visualize embeddings. Skills handle the nuances so you donât have to.

## Quick Start#

### Step 1: Install the MCP Server#
    
    
    pip install fiftyone-mcp-server
    

Warning

Install into the same Python environment where FiftyOne is installed. If you use a virtual environment or conda environment, activate it first or use the full path to the executable in your AI tool config.

To verify the installation:
    
    
    fiftyone-mcp
    

You should see:
    
    
    Starting fiftyone-mcp server...
    fiftyone-mcp server initialized successfully
    

Press `Ctrl+C` to stop it. Your AI tool manages the server lifecycle automatically once configured.

### Step 2: Configure Your AI Tool#
    
    
    claude mcp add fiftyone -- fiftyone-mcp
    

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
    
    
    {
      "mcpServers": {
        "fiftyone": {
          "command": "fiftyone-mcp"
        }
      }
    }
    

Add to `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project-scoped):
    
    
    {
      "mcpServers": {
        "fiftyone": {
          "command": "fiftyone-mcp"
        }
      }
    }
    

Or use the one-click install: [Install FiftyOne MCP in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=fiftyone&config=eyJjb21tYW5kIjoiZmlmdHlvbmUtbWNwIn0)

Restart Cursor after saving.

Add to `.vscode/mcp.json`:
    
    
    {
      "servers": {
        "fiftyone": {
          "command": "fiftyone-mcp",
          "type": "stdio"
        }
      }
    }
    

Or use the one-click install: [Install FiftyOne MCP in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=fiftyone&config=%7B%22command%22%3A%22fiftyone-mcp%22%7D)

The Gemini CLI extension registers the MCP server automatically. Install skills and MCP together:
    
    
    gemini extensions install https://github.com/voxel51/fiftyone-skills.git --consent
    

If `fiftyone-mcp` is not on your PATH, edit the extension config to use the full path to the executable.

Create or edit `.antigravity/mcp.json` in your project directory:
    
    
    {
      "mcpServers": {
        "fiftyone": {
          "command": "fiftyone-mcp"
        }
      }
    }
    

Restart Antigravity after saving.

If you have [uv](https://github.com/astral-sh/uv) installed, skip the `pip install` step entirely:
    
    
    {
      "mcpServers": {
        "fiftyone": {
          "command": "uvx",
          "args": ["fiftyone-mcp-server"]
        }
      }
    }
    

### Step 3: Install Skills#

Skills teach your agent how to complete complex FiftyOne workflows end to end. Run the command below to download the [universal installer](https://skil.sh) and install the default skills pack from [voxel51/fiftyone-skills](https://github.com/voxel51/fiftyone-skills):
    
    
    curl -sL skil.sh | sh -s -- voxel51/fiftyone-skills
    

You can also [develop and install your own skills](agents__developing_skills.md#developing-skills-authoring) to teach agents custom workflows specific to your project.

See the [Agent Ecosystem](https://docs.voxel51.com/agents/index.html#agents-skills) for the full list of available skills and per-agent install instructions.

### Step 4: Use It#
    
    
    "List all my datasets"
    "Load quickstart dataset and show summary"
    "Open the map panel and show me the embeddings"
    "Select samples with confidence above 0.9"
    "What plugins are available? Install the brain plugin"
    "Find near-duplicate images in my dataset"
    

Your agent automatically discovers operators and executes the appropriate tools.

## Available Tools#

| Category | Tools | Description  
---|---|---|---  
ð | Dataset Management | 3 | List, load, and summarize datasets  
ð¯ | App Operations | 29 | Control the App UI (views, panels, selection, â¦)  
â¡ | Operator System | 3 | Discover and execute any FiftyOne operator  
ð | Pipelines | 2 | Run pipelines and manage delegated operations  
ð | Plugin Management | 5 | Discover, install, and manage plugins  
ð¥ï¸ | Session | 1 | Launch the FiftyOne App server  
ð | Aggregations | 8 | Count, distinct, bounds, mean, histogram, â¦  
ð§¬ | Samples | 5 | Add, tag, untag, and set values on samples  
ðï¸ | Schema | 2 | Inspect and modify dataset field schemas  
ð¨ | App Config | 6 | Color scheme, sidebar groups, active fields  
  
## Tool Modes#

Which tools are available depends on your integration:

Integration | Modes | Use case  
---|---|---  
Voxel-Agent | `app` \+ `sdk` | Agent in [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise) (full UI control + data operations)  
Terminal / CLI | `session` \+ `sdk` | Headless agent (launch the App, query data, execute operators)  
  
## Resources#

Resource | Description  
---|---  
[FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server) | Source code and contributing guide  
[FiftyOne Skills](https://github.com/voxel51/fiftyone-skills) | Expert workflows for AI assistants  
[FiftyOne Plugins](https://github.com/voxel51/fiftyone-plugins) | Official plugin collection  
[Model Context Protocol](https://modelcontextprotocol.io) | MCP specification  
[PyPI Package](https://pypi.org/project/fiftyone-mcp-server/) | MCP server on PyPI  
[Discord Community](https://discord.gg/fiftyone-community) | Get help and share ideas  
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
