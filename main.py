import discord
import json
from discord.ext import commands
from classes.embed import battleCog

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    
botIntents = discord.Intents.all()
tryhardasBot = commands.Bot(config['prefix'], intents = botIntents)

@tryhardasBot.event
async def on_ready():
    print("Estou online!")
    tryhardasBot.add_cog(battleCog(tryhardasBot))

tryhardasBot.run(config['token'])