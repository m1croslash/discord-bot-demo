# Discord Bot Setup Guide:
Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/docs/intro)

## Linux/MacOS
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

## Windows
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```
```bash
pip install discord
```
```bash
pip install python-dotenv
```

## Create a .env file
```bash
DISCORD_TOKEN=your_token_here
```
## Edit bot.py and replace
```bash
bot.run('your_token_here')
```
## Run the Bot
```bash
python bot.py
```
