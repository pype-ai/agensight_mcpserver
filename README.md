# AgentSight MCP Server

A tool to automatically extract agent information from codebases.

## Quick Setup

```bash
# Clone repository
git clone https://github.com/pype-ai/agensight_mcpserver.git
cd agensight_mcpserver

# Create virtual environment
python -m venv mcp-env
source mcp-env/bin/activate  # On Windows: mcp-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Use with Cursor

1. Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "agensight-server": {
      "command": "/path/to/agensight_mcpserver/mcp-env/bin/python",
      "args": ["/path/to/agensight_mcpserver/server.py"],
      "description": "tool to generate agensight config"
    }
  }
}
```

**Note:** Replace `/path/to/agensight_mcp_server` with your actual installation path. The virtual environment's Python is located at `mcp-env/bin/python` relative to your installation directory.

2. In Cursor, ask:
```
Please analyze this codebase using the generateAgensightConfig MCP tool
```

3. Get a `agensight.config.json` file with all agents, prompts, tools, and connections.

## Features

- **Agent Discovery**: Automatically identifies AI agents in your codebase
- **Prompt Extraction**: Locates and extracts the full text of prompt templates
- **Tool Identification**: Maps all tools used by each agent
- **Connection Mapping**: Visualizes how agents interact with each other
- **JSON Output**: Generates a structured configuration file for easy integration

## How It Works

The server uses the Machine Conversation Protocol to provide a tool that analyzes your codebase. When invoked, it:

1. Recursively scans all files in your project
2. Identifies classes and functions that interact with LLMs
3. Extracts complete prompt templates by following variable references
4. Maps the connections between agents
5. Outputs a structured JSON configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
