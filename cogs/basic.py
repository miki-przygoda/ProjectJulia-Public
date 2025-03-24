import disnake
from disnake.ext import commands

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
    async def prompt(self, ctx, *, prompt: str):
        """Prompts the bot to do something"""
        if not prompt:
            await ctx.send("Please provide a prompt.")
            return
        
        if not isinstance(prompt, str):
            await ctx.send("Please provide a prompt that is a string.")
            return
        
        await ctx.send(f"{prompt}")
        
        


def setup(bot):
    bot.add_cog(Basic(bot)) 