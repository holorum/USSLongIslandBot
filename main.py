#!/usr/bin/python3

# To be able to run this script you must first install discord.py, and requests
# https://github.com/Rapptz/discord.py | https://github.com/psf/requests
import discord
import steam_requests
import reddit_requests
from discord.ext import commands


# You must provide a bot token
# For Github we use a file named 'token' with only our token in it
# You may want to encrypt that file to ensure full safety
# For testing it's fastest to just replace this with your bot's token
token = open("token", "r").read()

# The bots description and help command is defined/customised here
desc = "USS Long Island Bot WIP version"
helpcom = commands.DefaultHelpCommand(
    no_category = "Standard"
)

# Defines the bot command prefix, and the variable used to add additional commands.
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or("~"),
    description = desc,
    help_command = helpcom
    )

def start(token):
    # Define what should happen when the bot is all set up and ready.
    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print('------')

    # Create a class that will be defined as a category in the help command.
    class Standard(commands.Cog):
        """Standard simple commands"""

        # Use the discord.py to convert our modules into bot commands.
        @bot.command(description="Basic ping command where the bot responds with a pong message")
        async def ping(ctx):
            """Ping-pong!"""
            await ctx.send('Pong!')
        
        # Steam recommandation command
        # It can be slow because of steam
        @bot.command(description="Recommends a game from steam")
        async def recgame(ctx):
            """Recommend me a game!"""
            rec = steam_requests.recommend_game()
            await ctx.send(rec)
        
        @bot.command(description="Random Art from reddit")
        async def art(ctx):
            """Show me Ghostie!"""
            ghostie = reddit_requests.get_random_art()
            await ctx.send(ghostie)
        

    # Well looks like If the event is overriden then the commands won't procees...,
    # but if we use the listener then it's fine
    @bot.listen()
    async def on_message(msg):
        if msg.author == bot.user:
            return
        if str(msg.channel.type) == "private" and not "~" in msg.content:
            await msg.channel.send("Please use the command prefix(~) to run commands! ")
            return


    # Starts the bot using the provided token.
    bot.run(token)

start(token)