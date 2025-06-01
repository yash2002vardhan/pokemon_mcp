# server.py
from mcp.server.fastmcp import FastMCP
from utils.parse_pokemon_data import parse_pokemon_data
from utils.generate_strategy import generate_strategy
from utils.generate_team import generate_team
import json
import os
# Create an MCP server
mcp = FastMCP("Pokebase", dependencies = ["google-genai"])



pokemon_descriptions_path = os.path.join(os.path.dirname(__file__), "pokemon_descriptions.json")

with open(pokemon_descriptions_path, "r") as f:
    pokemon_descriptions = json.load(f)

# Add an addition tool
@mcp.tool()
async def get_pokemon_info(name:str) -> dict | None:
    """
    Retrieves detailed information about a specific Pokemon.
    
    Args:
        name (str): The name of the Pokemon to look up
        
    Returns:
        dict | None: A dictionary containing the Pokemon's data including:
            - abilities
            - moves
            - types
            - stats
            - base_experience
            - height
            - id
            - species
            - weight
            - role_type
        Returns None if the Pokemon is not found
    """
    data = await parse_pokemon_data(name)
    return data


@mcp.tool()
async def compare_pokemon(p1:str, p2:str) -> tuple[dict | None, dict | None]:
    """
    Compares two Pokemon by retrieving their data side by side.
    
    Args:
        p1 (str): Name of the first Pokemon
        p2 (str): Name of the second Pokemon
        
    Returns:
        tuple[dict | None, dict | None]: A tuple containing the data for both Pokemon.
        Each dictionary contains the same fields as get_pokemon_info().
        Returns (None, None) if either Pokemon is not found
    """
    p1_data = await parse_pokemon_data(p1)
    p2_data = await parse_pokemon_data(p2)
    return p1_data, p2_data


@mcp.tool()
def create_strategy(query:str) -> str | None:
    """
    Creates a battle strategy based on a query and Pokemon descriptions.
    
    Args:
        query (str): The user's strategy query
        pokemon_descriptions (list[str]): List of Pokemon descriptions to analyze
        
    Returns:
        str: A formatted strategy prompt for analysis
    """
    strategy = generate_strategy(query, pokemon_descriptions)
    return strategy


@mcp.tool()
def create_team(query:str) -> str | None:
    """
    Creates a team of 6 Pokemon based on a query and Pokemon descriptions.
    
    Args:
        query (str): The user's team creation query
        pokemon_descriptions (list[str]): List of Pokemon descriptions to analyze
        
    Returns:
        str: A formatted team creation prompt for analysis
    """
    team_response = generate_team(query, pokemon_descriptions)
    return team_response
