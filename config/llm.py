from typing import AsyncGenerator
import google.genai as genai
from config.env import settings


class GeminiLLM:
    def __init__(self):
        self.gemini_client = genai.Client(api_key=settings.GEMINI_API_KEY)
        print(f"this is the api key: {settings.GEMINI_API_KEY}")

    def generate_content(self, prompt: str) -> str | None:
        response = self.gemini_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        return response.text

    async def stream_content(self, prompt: str) -> AsyncGenerator[str | None, None]:
        for chunk in self.gemini_client.models.generate_content_stream(model='gemini-2.0-flash',contents=prompt):
            yield chunk.text


llm = GeminiLLM()
