import openai
import os

#Import the personality of the bot from the personality.py file - same dir
from OpenAI.personality import personality


def setup(bot):
    """Setup function for the managePrompt cog"""
    pass  # No commands/listeners to add in this file, but setup needed for bot loading


def handle_prompt(prompt_text: str) -> str:
    system_prompt = personality.personality

    # Load the OpenAI API key from .env
    openai.api_key = os.getenv("OPENAI_API_KEY")


    # Make a simple completion request
    response = openai.chat.completions.create(
        model="gpt-4o",  # or another model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_text}
        ]
    )
    
    return response.choices[0].message["content"]

