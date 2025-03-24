import os
import asyncio
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import signal

# Load environment variables from .env file
load_dotenv()

# Set up intents (using only non-privileged intents)
intents = disnake.Intents.default()
# Enable message content intent for prefix commands
intents.message_content = True
intents.members = False

class JuliaBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=intents,
            description="A cutie patootie"
        )
        self.initial_extensions = [
            'cogs.basic',
            'cogs.utility',
            'cogs.help'
        ]
    
    async def setup_hook(self):
        # Load extensions
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Loaded extension: {extension}')
            except Exception as e:
                # Only print errors that aren't the specific NoneType error we want to ignore
                if "object NoneType can't be used in 'await' expression" not in str(e):
                    print(f'Failed to load extension {extension}: {e}')
    
    async def on_ready(self):
        print("\n------")
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

    async def restart(self):
        """Gracefully shut down the bot and trigger a restart"""
        try:
            # Close the bot's HTTP session
            if hasattr(self.http, '_HTTPClient__session'):
                await self.http._HTTPClient__session.close()
            
            # Close the bot
            await self.close()
            
            # Send SIGUSR1 signal to trigger restart
            os.kill(os.getpid(), signal.SIGUSR1)
            
            # Wait a moment to ensure the signal is processed
            await asyncio.sleep(1)
            
            # If we get here, something went wrong with the restart
            print("Restart failed, shutting down...")
            try:
                exit()
            except SystemExit:
                pass
        except Exception as e:
            print(f"Error during restart: {e}")
            try:
                exit()
            except SystemExit:
                pass

async def main():
    bot = JuliaBot()
    # Load extensions before starting the bot
    await bot.setup_hook()
    # Run the bot with the token
    await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    asyncio.run(main()) 