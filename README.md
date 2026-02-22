# Discord Bot Setup Guide:
* Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/docs/intro)

# Git
```bash
git clone https://github.com/username/repository-name.git
```
```bash
cd repository-name
```
___
## Linux/MacOS
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

## Windows 10/11
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
___
## Install dependencies
```bash
pip install -r requirements.txt
```
```bash
pip install discord.py
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
