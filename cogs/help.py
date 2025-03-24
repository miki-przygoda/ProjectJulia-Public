import disnake
from disnake.ext import commands
from typing import Optional

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.original_help_command = bot.remove_command('help')

    def cog_unload(self):
        self.bot.add_command(self.original_help_command)

    @commands.command(name='help')
    async def help(self, ctx, command: Optional[str] = None):
        """Shows all available commands or detailed information about a specific command"""
        if command is None:
            # Show all commands grouped by cog
            embed = disnake.Embed(
                title="📚 Help Menu",
                description="Here are all available commands:",
                color=disnake.Color.blue()
            )
            
            # Group commands by cog
            cogs = {}
            for cmd in self.bot.commands:
                if not cmd.hidden:
                    cog_name = cmd.cog_name if cmd.cog_name else "Miscellaneous"
                    if cog_name not in cogs:
                        cogs[cog_name] = []
                    cogs[cog_name].append(cmd)
            
            # Add each cog's commands to the embed
            for cog_name, commands_list in cogs.items():
                commands_text = ""
                for cmd in sorted(commands_list, key=lambda x: x.name):
                    commands_text += f"`{cmd.name}` - {cmd.short_doc or 'No description'}\n"
                embed.add_field(
                    name=f"📑 {cog_name}",
                    value=commands_text,
                    inline=False
                )
            
            embed.set_footer(text=f"Use {ctx.prefix}help [command] for more information about a specific command")
            
        else:
            # Show detailed information about a specific command
            cmd = self.bot.get_command(command)
            if cmd is None:
                await ctx.send(f"❌ Command `{command}` not found.")
                return
            
            embed = disnake.Embed(
                title=f"📖 Command: {cmd.name}",
                description=cmd.help or "No description available",
                color=disnake.Color.blue()
            )
            
            if cmd.aliases:
                embed.add_field(
                    name="Aliases",
                    value=", ".join(f"`{alias}`" for alias in cmd.aliases),
                    inline=False
                )
            
            if cmd.signature:
                embed.add_field(
                    name="Usage",
                    value=f"`{ctx.prefix}{cmd.name} {cmd.signature}`",
                    inline=False
                )
            
            if cmd.cog_name:
                embed.add_field(
                    name="Category",
                    value=cmd.cog_name,
                    inline=True
                )
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot)) 