import os
import openai
from .modelHandler import BaseModelHandler

def setup(bot):
    """Setup function for the personality cog"""
    pass

class OpenAIHandler(BaseModelHandler):
    def __init__(self, system_prompt: str, model_name="gpt-4o"):
        super().__init__(system_prompt)
        self.model_name = model_name
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def handle(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
