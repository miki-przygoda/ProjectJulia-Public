import os
import asyncio
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import signal
import importlib

# Load environment variables from .env file
load_dotenv()

def detect_api_handler_modules():
    """Automatically detect all Python modules in apiHandler and its subdirectories."""
    api_modules = []
    api_handler_dir = 'apiHandler'
    
    # Walk through the apiHandler directory and its subdirectories
    for root, dirs, files in os.walk(api_handler_dir):
        # Skip __pycache__ directories
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        
        # Convert directory path to module path
        module_path = root.replace(os.sep, '.')
        
        # Add Python files as modules
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                module_name = f"{module_path}.{file[:-3]}"
                api_modules.append(module_name)
    
    return api_modules

# Core modules that should always be loaded
core_modules = [
    'cogs.basic',
    'cogs.utility',
    'cogs.help',
]

# Combine core modules with automatically detected API handler modules
modules = core_modules + detect_api_handler_modules()

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
        self.initial_extensions = modules
    
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
        load_dotenv(override=True)

        try:
            # Reload OpenAI modules
            for module in modules:
                try:
                    importlib.reload(importlib.import_module(module))
                    print(f'Reloaded module: {module}')
                except Exception as e:
                    print(f'Failed to reload module {module}: {e}')
            
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
    # Reload OpenAI 

if __name__ == "__main__":
    asyncio.run(main()) 