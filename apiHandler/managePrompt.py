import os
from .personality import personality
from .models.modelHandler import BaseModelHandler
from .models.openAI import OpenAIHandler
from .models.anthropic import AnthropicHandler

def setup(bot):
    """Setup function for the personality cog"""
    pass

# Factory to get the appropriate model handler based on environment variables
def get_model_handler() -> BaseModelHandler:
    # Providers will be choosen and stroed by the user - via discord command !switch
    provider = os.getenv("PROVIDERS", "openai").lower() # Default to openai if no provider is set
    model_name = os.getenv("MODEL_NAME", "gpt-4o") # Default to gpt-4o if no model is set

    if provider == "openai":
        return OpenAIHandler(system_prompt=personality, model_name=model_name)

    if provider == "anthropic":
        return AnthropicHandler(system_prompt=personality, model_name=model_name)

    raise ValueError(f"Unknown model provider: {provider}")


# Public method to handle prompt using the appropriate handler
def handle_prompt(prompt_text: str) -> str:
    if prompt_text is None:
        return "Error: Prompt is None"

    model_handler = get_model_handler()
    return model_handler.handle(prompt_text)