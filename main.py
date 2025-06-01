# server.py
from mcp.server.fastmcp import FastMCP
from utils.parse_pokemon_data import parse_pokemon_data

# Create an MCP server
mcp = FastMCP("Pokebase")


# Add an addition tool
@mcp.tool()
async def get_pokemon_info(name:str) -> dict | None:
    data = await parse_pokemon_data(name)
    return data


@mcp.tool()
def compare_pokemon(p1:str, p2:str) -> str | None:
    pass


@mcp.tool()
def create_strategy(query:str) -> str | None:
    pass


@mcp.tool()
def create_team(query:str) -> str | None:
    pass
