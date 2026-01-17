import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default()) # Prefix

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}') # Console output

@bot.command()
async def hello(ctx): # Command !hello
    await ctx.send("Hello world")
  
# Direct token (NOT RECOMMENDED for sharing)
bot.run('') # Your Token here

# Environment variable (RECOMMENDED)
# import os
# bot.run(os.getenv('DISCORD_TOKEN'))

# or from .env file
# from dotenv import load_dotenv
# import os
# load_dotenv()
# bot.run(os.getenv('DISCORD_TOKEN'))
