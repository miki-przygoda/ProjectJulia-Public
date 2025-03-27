# ProjectJulia Discord Bot

**ProjectJulia** is a modular, scalable Discord bot built using [Disnake](https://docs.disnake.dev/), designed for easy expansion and intelligent interaction. It includes core utilities, restart control, and plans for OpenAI-powered conversational commands.

## ✨ Features

- 🔧 Modular cog-based command system
- 🛠️ Utility commands: `!info`, `!serverinfo`
- 👋 Basic commands: `!info`, `!ping`, `!help`
- 👑 `!restart` command: Instantly reloads core modules from Discord without stopping the process - update the bot through a command on discord - no need to stop the entire bot each time
- 🤖 OpenAI API support
- 🧪 Designed for public use, customization, and clean command logic

## ⏲️ Future Features

- 📼 Live changes to what AI model is used `!switch`
- 🤖 Anthropic API support

## 📦 Requirements

- Python 3.8 or higher
- `disnake==2.10.1`
- `python-dotenv==1.0.0`
- `openai` (for OpenAI integration)
- `anthropic` (for Anthropic integration)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repo:

```bash
git clone https://github.com/miki-przygoda/ProjectJulia-Public.git
cd ProjectJulia-Public
```

### 2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Add your environment variables:

Create a `.env` file and add your Discord bot token:

`See .env.example` for what it should look like

### 4. Run the bot controller (wrapper) - (launches bot with restart management):

```bash
python run.py
```

Or directly:

```bash
python bot.py
```

## 🔧 Commands

Default prefix: `!`

### General Commands
- `!ping` – Measure bot latency
- `!info` – Shows basic bot info (includes Python version, Disnake version, uptime, and server count)
- `!serverinfo` – Shows server details
- `!help` – Lists available commands with descriptions
- `!help [command]` – Shows detailed information about a specific command

### OpenAI Commands
- `!prompt [text]` – Send a prompt to OpenAI (requires OpenAI API to be enabled)

### Owner Command
- `!restart` – Restarts the bot safely (owner only) 
    - This lets you make changes live and update it by saving and reseting, you dont need to stop it from running each time

## 🔁 Restart Management

The bot is wrapped by a `run.py` controller that monitors for shutdown events and restarts the bot when necessary. This allows remote restarts via `!restart` without manually rebooting the process.

## 🧠 OpenAI Integration

The bot includes basic OpenAI integration through the `!prompt` command. To use this feature:
1. Set `OPENAI_API_ENABLED=true` in your `.env` file
2. Add your OpenAI API key as `OPENAI_API_KEY` in the `.env` file
3. Use the `!prompt` command followed by your text

## 🧩 Extending Julia

To add a new feature:
1. Create a `.py` file in the cogs folder (e.g. `julia/cogs/your_feature.py`)
2. Define a class with `commands.Cog`
3. Register it in `basic.py` or in `bot.py` dynamically

## 🛡️ Permissions

Make sure to enable the following in the [Discord Developer Portal](https://discord.com/developers/applications):
- ✅ Message Content Intent
- ✅ Server Members Intent (if needed)

## 🪪 License

This project is licensed under the Attribution License.
You are free to use, modify, and distribute this code as long as you provide appropriate credit to Mikolaj Mikuliszyn as the original creator.

---

**Created by Mikolaj Mikuliszyn**
