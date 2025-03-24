# ProjectJulia Discord Bot

**ProjectJulia** is a modular, scalable Discord bot built using [Disnake](https://docs.disnake.dev/), designed for easy expansion and intelligent interaction. It includes core utilities, restart control, and plans for OpenAI-powered conversational commands.

## ✨ Features

- 🔧 Modular cog-based command system
- 🛠️ Utility commands: bot info, server info, uptime
- 👋 Basic commands: hello, ping
- ♻️ Background controller for restarting the bot remotely
- 🤖 OpenAI API support (coming soon)
- 🧪 Designed for public use, customization, and clean command logic

## 📦 Requirements

- Python 3.8 or higher
- `disnake==2.10.1`
- `python-dotenv==1.0.0`

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

```env
DISCORD_TOKEN=your_token_here
```

### 4. Run the bot controller (launches bot with restart management):

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
- `!info` – Shows basic bot info
- `!serverinfo` – Shows server details
- `!help` – Lists available commands

### Owner Command
- `!restart` – Restarts the bot safely (owner only) 
    - This lets you make changes live and update it by saving and reseting, you dont need to stop it from running each time

## 🔁 Restart Management

The bot is wrapped by a `run.py` controller that monitors for shutdown events and restarts the bot when necessary. This allows remote restarts via `!restart` without manually rebooting the process.

## 🧠 OpenAI Integration (Planned)

A future update will add:
- !`!prompt` commands that send input to OpenAI and return responses

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

This project is licensed under the MIT License.
Feel free to fork and build your own version.

---

**Created by Mikolaj Mikuliszyn**