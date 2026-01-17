import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
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
