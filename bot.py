import os
import discord
import asyncio
from discord.ext import commands

JUKEBOX_ID = os.environ['JUKEBOX_ID']
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
    if message.channel.id == 511741087954501634:
        await client.send_message(message.channel, 'What the fuck')
    if message.content.startswith('!test'):
		await client.send_message(message.channel, message.channel.id)
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(BOT_TOKEN)