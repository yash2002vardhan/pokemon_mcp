from config.llm import llm
from utils.prompts import strategy_prompt, team_creation_prompt

def generate_strategy(query:str, pokemon_descriptions:list[str]) -> str | None:
    prompt = strategy_prompt.format(user_query=query, pokemon_description=pokemon_descriptions)
    strategy = llm.generate_content(prompt)
    return strategy
