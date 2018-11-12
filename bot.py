# import discord
# from discord.ext import commands

# bot = commands.Bot(command_prefix='$')

# @bot.event
# async def on_ready():
    # print('Logged in as')
    # print(bot.user.name)
    # print(bot.user.id)
    # print('------')

# @bot.command()
# async def greet(ctx):
    # await ctx.send(":smiley: :wave: Hello, there!")
	
# @bot.event
# async def on_message(message):
    # channel = bot.get_channel('jukebox')
    # if message.server is None and message.author != bot.user:
		# await bot.send_message("WHAT I'D LIKE TO SAY TO THEM")
        # wait bot.delete_message(message)

# bot.run('<YOUR_TOKEN_HERE>')

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(process.env.TOKEN)