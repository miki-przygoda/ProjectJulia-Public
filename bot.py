import os
import asyncio
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up intents (using only non-privileged intents)
intents = disnake.Intents.default()
# Both of these are privileged intents
intents.message_content = False
intents.members = False

class JuliaBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=intents,
            description="A Discord bot built with disnake"
        )
        self.initial_extensions = [
            'cogs.basic',
            'cogs.utility'
        ]
    
    async def setup_hook(self):
        # Load extensions
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Loaded extension: {extension}')
            except Exception as e:
                print(f'Failed to load extension {extension}: {e}')
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print(f'Bot ID: {self.user.id}')
        print(f'Disnake Version: {disnake.__version__}')
        print(f'Running on {len(self.guilds)} server(s)')
        print('------')
        
        # Set the bot's status
        activity = disnake.Game(name="!help for commands")
        await self.change_presence(activity=activity)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing required argument: {error.param.name}")
            return
            
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Command on cooldown. Try again in {error.retry_after:.2f} seconds.")
            return
            
        # Print the error to console for debugging
        print(f'Error in command {ctx.command}:')
        print(error)

async def main():
    bot = JuliaBot()
    # Load extensions before starting the bot
    await bot.setup_hook()
    # Run the bot with the token
    await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main()) 