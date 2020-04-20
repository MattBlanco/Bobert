import os
import discord
import asyncio
from discord.ext import commands

BOT_TOKEN = os.environ['BOT_TOKEN'] # The token is also substituted for security reasons
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.name == 'jukebox' and not message.content.startswith('!') and not message.author.bot:
        await client.delete_message(message)
        await client.send_message(message.channel, 'Please use #general for general chat.')
    elif message.channel.name != 'jukebox' and message.content.startswith('!') and not message.author.bot:
        await client.delete_message(message)
        await client.send_message(message.channel, 'Please use #jukebox to play music.')

client.run(BOT_TOKEN)
