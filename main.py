#!/usr/bin/python3

# To be able to run this script you must first install discord.py, and requests
# https://github.com/Rapptz/discord.py | https://github.com/psf/requests
import os
import discord
import steam_requests
import reddit_requests
from random import randint as r
from discord.ext import commands, tasks


# You must provide a bot token.
# For Github we use a file named 'token' with only our token in it.
# You may want to encrypt that file to ensure full safety.
# For testing it's fastest to just replace this with your bot's token.
token = open("token", "r").read()

# The bots description is defined/customised here, also the intent gateways that are used.
desc = "USS Long Island Bot WIP version"
intents = discord.Intents.default()
intents.members = True

# Whether you run the cron.py in a cronjob or would like to use auto-update at 5 hour intervals.
# This is True by default because the official bot uses cronjob.
# The interval can be changed via c_hours.
# NOTE: The cron.py is still required if the internal cron is used because that's a CTRL+C, CTRL+V and that's too much work.
cron = True
c_hours = 5.0

# Defines the bot command prefix, the description, and the variable used to add additional commands.
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or("~"),
    intents=intents,
    description = desc
    )

opted = []
haunt_h = 1.0

def start(token):
    # Define what should happen when the bot is all set up and ready.
    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print('------')

    # Create a class that will be defined as a category in the help command.
    # In the discord.py docs this is refered as a "Cog".
    class Standard(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
        """Standard simple commands"""

        # Use the discord.py to convert our modules into bot commands.
        @commands.command(description="Basic ping command where the bot responds with a pong message")
        async def ping(self, ctx):
            """Ping-pong!"""
            await ctx.send('Pong!')
        

        @commands.command(description="opt in for haunt")
        async def haunt(self, ctx):
            """Haunting you!"""
            h = False
            for op in opted:
                if op == ctx.author:
                    h = True
                else:
                    h = False
            if not h:
                opted.append(ctx.author)
                await ctx.send("Haunt!")
            else:
                await ctx.send("Already Haunting you!")


        @commands.command(description="opt out for haunt")
        async def dehaunt(self, ctx):
            """De Haunting you..."""
            try:
                opted.remove(ctx.author)
                await ctx.send("...")
            except Exception:
                await ctx.send("I'm not even haunting you!")

        
        # Steam recommandation command.
        # It can be slow because of steam.
        @commands.command(description="Recommends a game from steam")
        async def recgame(self, ctx):
            """Recommend me a game!"""
            rec = steam_requests.recommend_game()
            await ctx.send(rec)
        
    class Art(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
        """Art commands"""
        
        # Art command see reddit_requests
        @commands.command(description="Random Art from reddit")
        async def art(self, ctx):
            """Show me Ghostie!"""
            ghostie = reddit_requests.get_random_art()
            await ctx.send(ghostie)

        # NSFW command see reddit_requests
        @commands.command(description="Random NSFW Art from reddit")
        async def nsfw(self, ctx):
            """Show me Naughty Ghostie!"""
            n_ghostie = reddit_requests.get_random_nsfw()
            await ctx.send(n_ghostie)
    
    # Initialize Tasks.
    # Tasks are internal loops that allows you to do something every given interval. (For more info see the discord.py docs)
    @tasks.loop(hours=c_hours)
    async def crontask():
        os.system("cron.py")
    @tasks.loop(hours=haunt_h)
    async def surprise():
        try:
            ro = r(0, len(opted))
            await opted[ro].dm_channel.send(reddit_requests.get_random_art())
        except Exception:
            pass
    
    # Start the task if relevant.
    if cron == False:
        crontask.start()
    surprise.start()


    # Here we add the commands that are inside of our classes, Cogs are basically lists of commands, but they aren't exactly, they're more than that...
    bot.add_cog(Standard(bot))
    bot.add_cog(Art(bot))
        

    # Well looks like If the events on_message is overriden then the commands won't procees...,
    # but if we use the listener then it's fine.
    # (Figured that if the "on_message()" is overriden, then we need to call the "command_process()", or smthg like that but using a listener instead was faster.)
    # NOTE: when using vscode pylance says that it isn't accessed, bullshit. It Is AcCeSsEd. (Tested)
    @bot.listen()
    async def on_message(msg):
        if msg.author == bot.user:
            return
        if str(msg.channel.type) == "private" and not "~" in msg.content:
            await msg.channel.send("Please use the command prefix(~) to run commands! ")
            return


    # Starts the bot using the provided token.
    # NOTE: This file only runs once, if more control is required over the loop use "bot.start(token)" instead, but first visit the discord.py docs.
    bot.run(token)

start(token)