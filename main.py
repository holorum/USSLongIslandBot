#!/usr/bin/python3

# To be able to run this script you must first install discord.py
# https://github.com/Rapptz/discord.py
import discord
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


def start(token):

    # Defines the bot command prefix, and the variable used to add additional commands.
    bot = commands.Bot(
        command_prefix = commands.when_mentioned_or("~"),
        description = desc,
        help_command = helpcom
        )

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
        @bot.command(description="basic ping command where the bot responds with a pong message")
        async def ping(ctx):
            """Ping-pong!"""
            await ctx.send('Pong!')

    # Removed because if I use this the commands doesn't seem to work at all.
    # This defines what should happen when the bot gets a message.
    # @bot.event
    # async def on_message(msg):
    #     if msg.author == bot.user:
    #         return
    #
    #     if str(msg.channel.type) == "private":
    #         await msg.channel.send("Please use the command prefix(~) to run commands! ")
    #         return


    # Starts the bot using the provided token.
    bot.run(token)


start(token)
