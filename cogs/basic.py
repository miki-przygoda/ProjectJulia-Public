import disnake
from disnake.ext import commands
import os
from apiHandler.managePrompt import handle_prompt

def available_providers():
    return ["openai", "anthropic"]


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Checks the bot's latency"""
        try:
            latency = round(self.bot.latency * 1000)
            await ctx.send(f'Pong! Latency: {latency}ms')
        except (AttributeError, TypeError):
            await ctx.send("Sorry, I couldn't check the latency right now.")



    @commands.command(name="prompt")
    async def prompt(self, ctx, *, prompt: str = None):
        """Used to send a prompt to the bot"""
        if prompt is None: # Double checks if the prompt is None - just in case 
            await ctx.send("Why did you leave it empty?")
            return None

        if os.getenv("OPENAI_API_ENABLED") == "true":
            if os.getenv("PROVIDERS") == "openai":
                await ctx.send("OpenAI API is enabled.")
            if os.getenv("PROVIDERS") == "anthropic":
                await ctx.send("Anthropic API is enabled.")

            
            try:
                prompt = str(prompt)
                response = handle_prompt(prompt)
                await ctx.send(response)
            except Exception as e:
                if os.getenv("PROVIDERS") == "openai":
                    await ctx.send("Something went wrong with the OpenAI API. Probably forgot the API key dummy...")
                    print(str(f"Error: {str(type(e))[8:-2]}")) #Remove the <class ' and '> from the error so its just the error type
                    # print(f"Error: {type(e)}") #Alt in case you want to see the full error
                if os.getenv("PROVIDERS") == "anthropic":
                    await ctx.send("Something went wrong with the Anthropic API. Probably forgot the API key dummy...")
                    print(str(f"Error: {str(type(e))[8:-2]}")) #Remove the <class ' and '> from the error so its just the error type
                    print(f"Error: {type(e)}") #Alt in case you want to see the full error
        else:
            await ctx.send("OpenAI API is disabled.")
            await ctx.send("So I couldn't send it through 😓")

    # @commands.command(name="switch")
    # async def switch(self, ctx, *, model: str = None):
    #     """Used to switch the model provider""" # TODO: Implement this -- need to make it so the model can be choosen by the user
    #     if model is None:
    #         await ctx.send("Please specify a model provider. Available providers: openai, anthropic")
    #         return None
        
    #     if model not in available_providers():
    #         await ctx.send(f"Invalid model provider. Available providers: {available_providers()}")
    #         return None
        
    #     os.environ["MODEL_PROVIDER"] = model
    #     await ctx.send(f"Model provider switched to {model}")
     


def setup(bot):
    bot.add_cog(Basic(bot)) 