import discord
from discord.ext import commands


def start(token):

    #Defines the bot command prefix.
    #Definiálja a parancs prefixet
    bot = commands.Bot(command_prefix='~')

    #Here we use the discord.py to convert our module into a bot command.
    #itt a discord.py-t használva konvertáljuk a modult egy bot paranccsá
    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    #starts the bot using the provided token
    #elindítja a botot a megadott tokennel
    bot.run(token)
