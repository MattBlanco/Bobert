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
from discord.ext import commands
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['BOT_TOKEN'])
TOKEN = os.environ['BOT_TOKEN'] # The token is also substituted for security reasons
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run(TOKEN)