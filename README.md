# ProjectJulia Discord Bot

A feature-rich Discord bot built with disnake, a fork of discord.py.

## Features

- Basic commands: hello, ping
- Utility commands: server info, bot info
- Modular cog-based command system for easy expansion

## Requirements

- Python 3.8 or higher (compatible with Python 3.13)
- disnake 2.10.1 or higher
- python-dotenv

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/miki-przygoda/ProjectJulia-Public.git
   cd ProjectJulia-Public
   ```
2. Create and activate a virtual envirement (recomended):
   ```
   python3 -m venv venv

   source venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Discord bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" tab and click "Add Bot"
   - If you need to use message content or server members data:
     - Under the "Privileged Gateway Intents" section, enable:
       - Message Content Intent
       - Server Members Intent
     - Update the intents in bot.py to set these to True
   - Copy your bot token

5. Configure environment variables:
   - Copy `.env.example` to `.env` (or create a new .env file)
   - Add your bot token: `DISCORD_TOKEN=your_token_here`

6. Run the bot:
   ```
   python3 bot.py
   ```

## Adding the Bot to Your Server

1. Go back to the Discord Developer Portal
2. Navigate to the "OAuth2" tab then "URL Generator"
3. Under "Scopes" select "bot"
4. Under "Bot Permissions" select the permissions your bot needs
   - Recommended minimum: Send Messages, Read Message History, Embed Links
5. Copy the generated URL and open it in a browser
6. Select the server you want to add the bot to

## Commands

Default prefix: `!`

### Basic Commands
- `!hello` - Bot greets you
- `!ping` - Check bot's response time

### Utility Commands
- `!info` - Display information about the bot
- `!serverinfo` - Display information about the current server

### Help
- `!help` - Show all available commands
- `!help [command]` - Show detailed information about a specific command

## Extending the Bot

To add new commands, create a new cog file in the `cogs` directory. Use the existing cogs as templates.

### Important Notes
- If you're using Python 3.13, the bot is configured to use minimal intents to avoid issues with the more recent Python versions.
- If you need message content or member information, you must enable the privileged intents in the Discord Developer Portal AND update the bot.py file.

## License

MIT
 
