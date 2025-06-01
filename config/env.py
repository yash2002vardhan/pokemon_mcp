import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    POKEMON_API_URL: str = "https://pokeapi.co/api/v2"
    GEMINI_API_KEY: str = "..."



    class Config:
        case_sensitive = True
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
    
settings = Settings()
