import disnake
from disnake.ext import commands
import time
import platform

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name='info')
    async def info(self, ctx):
        """Shows bot information"""
        embed = disnake.Embed(
            title="Bot Information",
            description="A Discord bot created with disnake",
            color=disnake.Color.blue()
        )
        
        embed.add_field(name="Python Version", value=platform.python_version(), inline=True)
        embed.add_field(name="Disnake Version", value=disnake.__version__, inline=True)
        
        uptime = int(time.time() - self.start_time)
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{hours}h {minutes}m {seconds}s"
        
        embed.add_field(name="Uptime", value=uptime_str, inline=True)
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo')
    async def serverinfo(self, ctx):
        """Shows server information"""
        guild = ctx.guild
        
        embed = disnake.Embed(
            title=f"{guild.name} Information",
            description=guild.description if guild.description else "No description",
            color=disnake.Color.green()
        )
        
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot)) 