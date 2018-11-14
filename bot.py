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
    if message.channel.name == 'burn-the-evidence' and not message.content.startswith('!'):
        await client.delete_message(message)
        await client.send_message(message.channel, 'WHAT THE FUCK')

client.run(BOT_TOKEN)