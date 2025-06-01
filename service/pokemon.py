import aiohttp
import ssl
import certifi


base_url = "https://pokeapi.co/api/v2"


# async def get_pokemon_data(pokemon_name: str):
#     try:
#         # Create SSL context with proper certificates
#         ssl_context = ssl.create_default_context(cafile=certifi.where())
        
#         connector = aiohttp.TCPConnector(ssl=ssl_context)
#         async with aiohttp.ClientSession(connector=connector) as session:
#             async with session.get(f"{base_url}/pokemon/{pokemon_name}") as response:
#                 if response.status == 404:
#                     raise Exception(f"Pokemon {pokemon_name} not found")
#                 data = await response.json()
#                 return data
#     except Exception as e:
#         raise


class PokemonService:

    def __init__(self):
        self.base_url = base_url

    async def get_pokemon_data(self, pokemon_name: str):
        try:
            ssl_context = ssl.create_default_context(cafile=certifi.where())
            connector = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(f"{self.base_url}/pokemon/{pokemon_name}") as response:
                    if response.status == 404:
                        raise Exception(f"Pokemon {pokemon_name} not found")
                    data = await response.json()
                    return data
        except Exception as e:
            raise

async def get_pokemon_service() -> PokemonService:
    return PokemonService()
