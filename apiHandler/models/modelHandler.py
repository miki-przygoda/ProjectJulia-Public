def setup(bot):
    """Setup function for the personality cog"""
    pass

class BaseModelHandler:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def handle(self, prompt: str) -> str:
        raise NotImplementedError("Each model handler must implement the handle method.") 