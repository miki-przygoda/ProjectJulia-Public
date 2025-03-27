# TODO: Implement Anthropic API - and make it actually work well with the commands etc 

import os
import anthropic
from .modelHandler import BaseModelHandler

def setup(bot):
    """Setup function for the personality cog"""
    pass

class AnthropicHandler(BaseModelHandler):
    def __init__(self, system_prompt: str, model_name="claude-3-5-sonnet-20240620"):
        super().__init__(system_prompt)
        self.model_name = model_name
        anthropic.api_key = os.getenv("ANTHROPIC_API_KEY")

    def handle(self, prompt: str) -> str:
        response = anthropic.messages.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
