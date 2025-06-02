# Pokemon MCP Server

A Model Context Protocol (MCP) server that provides Pokemon data analysis, battle strategy generation, and team building capabilities for **Claude Desktop**. Powered by PokéAPI and Google Gemini AI.

## Features

### Available Tools for Claude Desktop

- **🔍 Pokemon Information Lookup** (`get_pokemon_info`)
  - Get detailed stats, abilities, moves, types, and battle roles for any Pokemon
  - Includes height, weight, base experience, and automatically assigned battle roles

- **⚖️ Pokemon Comparison** (`compare_pokemon`) 
  - Side-by-side comparison of two Pokemon with complete stat breakdowns
  - Perfect for matchup analysis and team planning

- **🎯 Battle Strategy Generation** (`create_strategy`)
  - AI-powered counter-strategy recommendations
  - Type matchups, effective moves, and tactical suggestions

- **👥 Team Building** (`create_team`)
  - Generate balanced 6-Pokemon teams based on your preferences
  - Considers type coverage, role diversity, and team synergy

## Setup for Claude Desktop

### Prerequisites

- Python 3.13+
- Google Gemini API key
- Claude Desktop app

### Installation

1. **Clone and install**
   ```bash
   git clone <repository-url>
   cd pokemon_mcp
   uv sync
   ```

2. **Configure environment**
   ```bash
   # Create .env file in the root directory
   echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
   ```

3. **Install to Claude Desktop**
   ```bash
   uv run mcp install main.py
   ```

4. **Restart Claude Desktop** to load the Pokemon MCP server

## Usage in Claude Desktop

Once configured, you can ask Claude to:

- "Get information about Charizard"
- "Compare Pikachu and Raichu"
- "Create a strategy to counter Mewtwo"
- "Build me a balanced competitive team"

Claude will automatically use the appropriate Pokemon tools to provide detailed responses with real Pokemon data and AI-generated strategies.

## Battle Role System

The server automatically assigns battle roles based on Pokemon stats:

- **Sweeper**: High speed + attack (fast damage dealers)
- **Tank**: High defensive stats (damage soakers)
- **Glass Cannon**: High offense, low defense (risky but powerful)
- **Support**: Utility-focused Pokemon
- **Balanced**: Well-rounded across all stats
- **Generic**: Doesn't fit other categories

## Requirements

- **mcp[cli]**: Model Context Protocol framework
- **aiohttp**: For PokéAPI requests
- **google-genai**: Google Gemini AI integration
- **certifi**: SSL certificate handling

## Data Sources

- **PokéAPI**: Real-time Pokemon data
- **Google Gemini 2.0**: AI-powered analysis
- **1000+ Pokemon**: Comprehensive pre-processed dataset
