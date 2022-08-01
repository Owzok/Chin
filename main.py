import discord
from discord.ext import commands
import music
import os

cogs = [music]

client = commands.Bot(command_prefix='-', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.environ.get("Chinchinator_token"))