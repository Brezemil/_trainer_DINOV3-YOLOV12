---
source_url: https://docs.voxel51.com/tutorials/gemini_fiftyone_skills.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/tutorials/gemini_fiftyone_skills.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/tutorials/gemini_fiftyone_skills.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/tutorials/gemini_fiftyone_skills.ipynb)

# Using FiftyOne Skills with Gemini CLI#

Natural language interfaces (NLIs) allow humans to interact with software systems using everyday language instead of rigid commands, scripts, or UI clicks. Instead of learning a domain-specific API or remembering exact function signatures, you describe what you want to accomplish, and the system translates that intent into concrete actions. In practice, a natural language interface sits on top of existing tools and workflows. It doesnât replace themâit orchestrates them. The interface parses intent, asks clarifying questions when needed, and executes real operations against real systems. The key difference from chatbots or code generators is execution: a true NLI doesnât just suggest what to do, it actually does it. When connected to the right backend, a natural language interface becomes a control plane for complex systemsâlowering the barrier to entry without dumbing down whatâs possible. In this tutorial, weâll demonstrate how to use [FiftyOne Skills](https://github.com/voxel51/fiftyone-skills) and the [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server) with Googleâs Gemini CLI to build natural language workflows for computer vision tasks. Specifically, this walkthrough covers:

  * Understanding what MCP servers and agent skills provide
  * Installing and configuring the FiftyOne MCP Server with Gemini CLI
  * Installing FiftyOne Skills for common computer vision workflows
  * Loading datasets using natural language commands
  * Running model inference with multiple models
  * Evaluating model predictions and comparing results

**So, whatâs the takeaway?** By combining FiftyOneâs 80+ operators with natural language interfaces, you can dramatically accelerate computer vision workflows. Tasks that previously required writing custom scriptsâloading data, running inference, evaluating modelsâcan now be accomplished through simple conversational commands.

## Why Natural Language Interfaces Matter for Computer Vision#

Computer vision workflows are powerful, but theyâre also fragmented. Loading datasets, converting formats, running inference, inspecting failures, fixing labelsâeach step lives in a different tool, file, or script. Even experienced engineers spend more time wrangling data than improving models. Natural language interfaces compress this complexity. They let you express intent instead of implementation: âFind duplicate images,â âRun detection and show false positives,â âVisualize embeddings for this class.â For CV teams, this matters because:

  * **Iteration gets faster** : You move from idea to execution in one step
  * **Expertise is shared** : Hard-won workflows become reusable instead of tribal knowledge
  * **More people can contribute** : Researchers, data scientists, and PMs can explore datasets without writing glue code
  * **Focus shifts to data quality** : The real bottleneck in model performance



## What Are Skills and MCP?#

Agent skills and MCP solve different parts of the same problem. **MCP (Model Context Protocol)** is about connection: it lets an agent talk to real systems, run real operations, and get real results instead of just generating text. **Skills** are about guidance: they teach the agent how to use those capabilities correctly for a specific task. MCP exposes _what_ the system can do, while skills explain _how_ and _when_ to do it. On their own, tools are powerful but can be ambiguous. Skills turn those tools into repeatable workflows. They encode experience, decisions, and guardrails. Together, they let agents move from âI can call functionsâ to âI know how to complete this task end to end.â

### FiftyOne MCP Server#

The [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server) connects agents to FiftyOneâs 80+ operators, dataset management, model inference, brain computations, and the App. Itâs the bridge between natural language and FiftyOne tools.

### FiftyOne Skills#

[FiftyOne Skills](https://github.com/voxel51/fiftyone-skills) are expert workflows built on top of the MCP server. Each skill teaches the agent how to complete a specific task: import data, find duplicates, visualize embeddings. Skills handle the nuances so you donât have to.

## Setup#

This tutorial is designed to run interactively with Google Colab and the Gemini CLI. Youâll execute commands directly in the terminal rather than in notebook cells. First, verify that you have access to a GPU for faster model inference:
    
    
    [ ]:
    
    
    
    !nvidia-smi
    

![gpu](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/gpu.webp) The next step is to open the terminal so you can interact with Gemini. Google Colab already includes Gemini, so thereâs no need to install anything. ![gif_terminal](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/gif_terminal.webp) Add your Gemini API key, when you open the Gemini CLI for the first time, youâll be prompted to add your Gemini API key. ![gemini_init](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/gemini_init.webp)

### Enable Gemini Preview Features and Skills#

Before installing skills, you must manually enable Gemini Preview Features (e.g. models) and allow Skills. Run the required Gemini configuration commands shown in the next step. ![settings](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/settings.webp)

### Install and validate FiftyOne MCP (agent-managed)#

Open a terminal in Colab and ask the agent to handle the full setup,
    
    
    Install the FiftyOne MCP Server by running:
    
    pip install fiftyone-mcp-server
    
    Then register it with Gemini using:
    
    gemini mcp add fiftyone-mcp <commandOrUrl>
    
    Finally, verify that the MCP is correctly integrated and available for use.
    

The agent will install the MCP server, add it to Gemini, and validate that the connection is working. Once completed, the agent can immediately run FiftyOne workflows through MCP â no manual configuration required.

### Install FiftyOne Skills (agent-managed)#

Now, weâll use the dataset import, inference, and evaluation skills. You can explore the full list of available skills at: [fiftyone-skills](https://github.com/voxel51/fiftyone-skills). Open a terminal in Colab and ask the agent to handle the installation.
    
    
    Install the FiftyOne Skills from the official repository by running:
    
    gemini skills install https://github.com/voxel51/fiftyone-skills.git
    
    Then verify that the skills are correctly installed and available for use.
    

The agent will install the skills, register them with Gemini, and validate that they are ready. Once installed, the agent can immediately use these skills to load datasets, run inference, and evaluate results in FiftyOne.

### Restart the Session#

After installing the MCP server and skills, restart your terminal session to ensure all configurations are loaded properly. Exit the current session and relaunch the Gemini CLI.

### Verify Configuration#

Before proceeding, verify that the MCP server and skills are configured correctly. When you open the Gemini CLI, you should see a message similar to: **``1 MCP server | 9 skills``** If you donât see this, the setup is not complete. In the Gemini CLI, enter:
    
    
    Check if the Fiftyone MCP and fiftyone skills are configured correctly in this environment and can be executed. For MCP Run: gemini mcp list, if itâs not installed, add it with: gemini mcp add fiftyone-mcp <local_path>, double check after this.
    

The agent should confirm that it has access to FiftyOne operators and the installed skills. ![config_ready](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/config_ready.webp)

## Running Computer Vision Workflows with Natural Language#

Now that the environment is configured, we can use natural language to perform complex computer vision tasks. In this example, weâll:

  1. Load a dataset from the FiftyOne Zoo
  2. Run object detection with multiple models
  3. Store predictions for comparison
  4. Evaluate model performance against ground truth
  5. Determine which model performs best

You can execute this entire workflow with a single natural language prompt. You can also load your own data by uploading images to Colab and specifying the path in your prompt.

### Example Prompt#

In the Gemini CLI, enter the following prompt:
    
    
    Use the MCP and Skills to:
    1. Load the FiftyOne quickstart dataset and create a new dataset with only 10 image samples
    2. Run object detection using YOLOv8 and store the predictions as "yolov8_pred"
    3. Run object detection using a ResNet-based model and store the predictions as "resnet_pred"
    4. Compare all predictions against the ground-truth labels using the evaluation skills
    5. Determine which model performs best for this specific use case and report the results
    6. Launch the FiftyOne App and print the session URL
    

![final_fast](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/final_fast.webp)

### Understanding Permission Prompts#

As the agent executes the workflow, you may be prompted to approve certain actions. You have several options:

  * **Allow individual actions** : Review and approve each step one at a time to understand what the agent is doing
  * **Allow all actions** : Approve all actions at once to let the agent complete the workflow without interruption

For learning purposes, we recommend allowing individual actions so you can observe each step of the workflow.

## Viewing Results in the FiftyOne App#

Once the workflow completes, the agent will launch the FiftyOne App and provide a URL. You can also manually launch the App at any time:
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    
    session = fo.launch_app(auto=False)
    print(session.url)
    

Open the URL in a new browser tab to explore your dataset, view predictions from different models, and analyze evaluation results interactively. ![final_results](https://cdn.voxel51.com/tutorial_gemini_fiftyone_skills/final_results.webp)

## Working with Your Own Data#

The workflows demonstrated in this tutorial work with any dataset. To use your own data:

  1. Upload your images to Google Colab
  2. Note the file path where your data is stored
  3. Use a natural language prompt to import the data, for example:


    
    
    Import the images from /content/my_images as a new FiftyOne dataset called "my_dataset"
    

The FiftyOne Skills will automatically detect the data format and handle the import process.

## Summary#

In this tutorial, we demonstrated how to use natural language interfaces to streamline computer vision workflows with FiftyOne: **Key concepts covered:**

  * **MCP servers** provide the connection layer between AI agents and FiftyOneâs capabilities
  * **FiftyOne Skills** encode expert knowledge for specific tasks like data import, inference, and evaluation
  * **Natural language commands** can orchestrate complex multi-step workflows

**Practical skills learned:**

  * Installing and configuring the FiftyOne MCP Server with Gemini CLI
  * Loading datasets using conversational commands
  * Running inference with multiple models
  * Evaluating and comparing model performance

Natural language interfaces donât replace traditional programmatic workflowsâthey complement them. Use NLIs for rapid exploration and iteration, then switch to Python scripts when you need fine-grained control or reproducible pipelines. For more information:

  * [FiftyOne MCP Server](https://github.com/voxel51/fiftyone-mcp-server)
  * [FiftyOne Skills](https://github.com/voxel51/fiftyone-skills)
  * [FiftyOne Documentation](https://docs.voxel51.com)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
