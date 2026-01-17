# Discord Bot Setup Guide:
Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/docs/intro)

## Linux/macOS
```python3 -m venv venv```
```source venv/bin/activate```

## Windows
```python -m venv venv```
```venv\Scripts\activate```

## Install dependencies
```pip install -r requirements.txt```
```pip install discord```
```pip install python-dotenv```

## Create a .env file
```DISCORD_TOKEN=your_token_here```
## Edit bot.py and replace
```bot.run('your_token_here')```
## Run the Bot
```python bot.py```
