---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/fiftyone_qa_pairs_14k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/fiftyone-qa-pairs-14k)

# FiftyOne QA 14k Dataset#

## Overview#

This dataset is derived from the FiftyOne Function Calling 14k dataset and is designed to train AI assistants to understand and answer questions about FiftyOneâs functionality.

## Purpose#

  * Train AI models to understand FiftyOne-related queries

  * Provide examples of FiftyOne syntax

  * Map natural language questions to appropriate FiftyOne code snippets

  * Demonstrate correct usage for FiftyOne functions and method calls




This dataset was synthetically generated using Anthropicâs Claude 3.5 Sonnet with the following prompt:
    
    
    PROMPT = """You are an expert in FiftyOne. Your task is to generate examples of using FiftyOne that will be used to train an AI assistant. 
    
    You will be given a user query along with the function calls and class methods which successfully execute the query.
    
    Your task is to generate a helpful response to the user's query, using the provided function calls and class methods, so that the user can understand how to use FiftyOne to achieve their goal.
    
    Note that common FiftyOne aliases include:
    
    - import fiftyone as fo
    - import fiftyone.zoo as foz
    - import fiftyone.utils as fou
    - import fiftyone.brain as fob
    - import fiftyone.utils.tf as foutf
    - from fiftyone import ViewField as F
    - import fiftyone.utils.data as foud
    - import fiftyone.utils.coco as fouc
    - import fiftyone.utils.labels as foul
    - import fiftyone.utils.torch as fout
    - import fiftyone.utils.huggingface as fouh
    
    Responses should be short and concise, and include required syntax to achieve the FiftyOne user's goal.
    """
    

The code below demonstrates how the [FiftyOne Function Calling 14k dataset](https://huggingface.co/datasets/Voxel51/fiftyone-function-calling-14k) is processed through Claudeâs API in parallel.

The transformation is as flow:

  1. Input Dataset â Convert each row in the original dataset to a string, send to Anthropic API and generate a natural language response to the user query

  2. Parallel Processing:

     * Splits work across 5 threads (default)

     * Each thread has its own Claude API client

     * Sends each query to Claude-3-sonnet with a system prompt

     *   3. Output Transformation:

     * Original query â Claude response

     * Saves as simplified dict: {âqueryâ: original_query, âresponseâ: claude_response}



    
    
    import anthropic
    import json
    from pathlib import Path
    import concurrent.futures
    import threading
    from tqdm import tqdm
    
    def process_item(row, client):
        """
        Process a single dataset item by calling the Claude API.
        
        Args:
            row (dict): A single row from the dataset containing at least a 'query' field
            client (anthropic.Anthropic): An initialized Anthropic client
            
        Returns:
            dict: A dictionary containing the query and Claude's response
            None: If an error occurs during processing
        """
        try:
            # Make API call to Claude with the row content
            response = client.messages.create(
                model="claude-3-5-sonnet-latest",
                max_tokens=1024,
                system=PROMPT,  # System prompt defined elsewhere
                messages=[
                    {"role": "user", "content": str(row)}
                ],
                temperature=0.65  # Lower temperature for more focused responses
            )
            
            # Extract and return just the essential fields
            return {
                'query': row['query'],
                'response': response.content[0].text
            }
        except Exception as e:
            print(f"Error processing row: {e}")
            return None
    
    def process_dataset_parallel(dataset, output_file, api_key, max_workers=5):
        """
        Process a dataset in parallel using multiple threads and save responses incrementally.
        
        This function handles parallel processing of dataset rows, automatic saving of progress,
        and resumption of interrupted processing.
        
        Args:
            dataset (Dataset): A HuggingFace dataset to process
            output_file (str): Path where results should be saved as JSON
            api_key (str): Anthropic API key for authentication
            max_workers (int, optional): Number of parallel worker threads. Defaults to 5.
            
        Returns:
            list: List of processed results containing queries and responses
            
        Note:
            - Uses thread-safe file locking for saving results
            - Automatically resumes from existing results if output file exists
            - Saves progress every 10 processed items
        """
        # Initialize results list and thread-safe file lock
        results = []
        file_lock = threading.Lock()
        
        # Load existing results if output file exists (for resumption)
        if Path(output_file).exists():
            with open(output_file, 'r') as f:
                results = json.load(f)
            
        # Helper function to create new Anthropic client instances
        def get_client():
            return anthropic.Anthropic(api_key=api_key)
        
        # Helper function for thread-safe saving of results
        def save_results():
            with file_lock:
                with open(output_file, 'w') as f:
                    json.dump(results, f, indent=2)
        
        # Main parallel processing loop
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Create separate client for each worker thread
            clients = [get_client() for _ in range(max_workers)]
            
            # Submit all processing tasks to the thread pool
            future_to_row = {
                executor.submit(process_item, row, clients[i % max_workers]): i 
                for i, row in enumerate(dataset)
            }
            
            # Process results as they complete (with progress bar)
            for future in tqdm(concurrent.futures.as_completed(future_to_row), total=len(dataset)):
                result = future.result()
                if result:
                    results.append(result)
                    
                    # Save progress periodically
                    if len(results) % 10 == 0:
                        save_results()
        
        # Save final results
        save_results()
        
        return results
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
