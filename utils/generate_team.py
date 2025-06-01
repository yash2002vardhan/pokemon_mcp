from config.llm import llm
from utils.prompts import team_creation_prompt

def generate_team(query:str, pokemon_descriptions:list[str]) -> str | None:
    prompt = team_creation_prompt.format(user_query=query, pokemon_description=pokemon_descriptions)
    team = llm.generate_content(prompt)
    return team
