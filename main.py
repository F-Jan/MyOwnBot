import os
import discord
from discord.ext import commands

print('Starting...')

TOKEN = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your Discord-Server"))
    print('The Bot is ready to Work')

client.run(TOKEN)
