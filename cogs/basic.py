import disnake
from disnake.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        """Says hello to the user"""
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Checks the bot's latency"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! Latency: {latency}ms')

def setup(bot):
    bot.add_cog(Basic(bot)) 