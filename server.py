# server.py
import os
import glob
import json
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("AgentAnalyzer")


# New tool to generate the agent UI and analyze the repository
@mcp.tool()
def generateAgensightConfig() -> str:
    
    """Create an echo prompt"""

    message = """
        You are an advanced agent information extractor. Your task is to scan the contents of all files in a directory recursively to extract the following information and save it in a file called `agensight.config.json`.
        When extracting prompt information, prioritize the system prompt if available. If not, use the user prompt or any other prompt that is present.


        Follow these steps:

        1. **Agent's Name**:
        - Focus ONLY on identifying AI agents - entities that are making LLM calls or interacting with AI models
        - Identify the agent's name from all files in the directory and its subdirectories. This could be part of a class, function, or a specific variable in the code.
        - If the agent is defined as a class, extract the name of the class.
        - If it's a function, extract the name of the function.
        - Only include entities that are performing some LLM call or functioning as AI agents

        2. **Prompts**:
        - EXTRACT THE FULL TEXT of any prompt templates across all files.
        - Prioritize extracting the **system prompt** if one is clearly identifiable. If no explicit system prompt is found, then extract the **user prompt** or any other primary prompt associated with the agent.
        - IMPORTANT: Follow all variable references, dictionary lookups, imports, and file references to find the actual complete prompt text.
        - For any prompt stored in variables, dictionaries, or imported from other files, trace the references to get the complete text.
        - For each prompt, extract the **variables** (i.e., placeholders) that are used inside the template.
        - If the prompt is dynamically generated and not defined as a static string anywhere in the codebase, set "prompt": "dynamic" for that agent
        - Be thorough in tracing all references - this might require examining multiple files to locate the actual text.

        3. **Tools**:
        - Look for any references to tools used by the agent in any file. Tools can be identified by looking for function calls, variables, or imported modules.
        - Some examples of tools are `log_abuse_check`, `model_predict`, `extract_text_from_pdf`, etc.
        - Tool definitions and their usage may be spread across different files, so correlate this information carefully.

        4. **Connections**:
        - Identify if the agent interacts with other agents across all files. Look for references to other agent names.
        - If there is an agent-to-agent connection, specify the type of connection: `instantiation`, `transition`, or any other relevant relationship.
        - These connections might only be apparent when analyzing multiple files together.

        5. **Generate the `agensight.config.json` file**:
        - After extracting the information from all files, including agent details, prompts,varaibles, tools, and definitions, save it in a structured `JSON` format as described below:

        ### JSON Format:

        ```json
        {
            "agents": [
                {
                "name": "AgentName",
                "prompt": "Full prompt text with all {va1} included exactly as {var2} found in the source files",
                "variables": ["var1", "var2"],
                },
                {
                    "name": "DynamicAgent",
                    "prompt": "some prompt text",
                    "variables": ["var1", "var2"],
                }
            ],
            "connections": [
                {
                    "from":start
                    "to": "AgentName",
                },
                {
                    "from": "AgentName",
                    "to": "OtherAgentName",
                },
                {
                    "from": "OtherAgentName",
                    "to": "End",
                }
            ]
        }
    """

    return message

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")

