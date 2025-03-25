import disnake
from disnake.ext import commands
import os
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
        if prompt is None:
            await ctx.send("Why did you leave it empty?")
            return
        
        if os.getenv("OPENAI_API_ENABLED") == "true":
            await ctx.send("OpenAI API is enabled.")
            await ctx.send("Prompt sent successfully.")
        else:
            await ctx.send("OpenAI API is disabled.")
            await ctx.send("So I couldn't send it through 😓")

def setup(bot):
    bot.add_cog(Basic(bot)) 