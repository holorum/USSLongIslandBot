import discord
from discord.ext import commands


def start(token):

    #Defines the bot command prefix.
    bot = commands.Bot(command_prefix='~')

    #Here we use the discord.py to convert our module into a bot command.
    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    #starts the bot using the provided token
    bot.run(token)
