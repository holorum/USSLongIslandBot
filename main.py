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
intents.message_content = True
intents.members = True

# Whether you run the cron.py in a cronjob or would like to use auto-update at 5 hour intervals.
# This is True by default because the official bot uses cronjob.
# The interval can be changed via c_hours.
# NOTE: The cron.py is still required if the internal cron is used because that's a CTRL+C, CTRL+V and that's too much work.
cron = True
c_hours = 5.0

# Defines the bot command prefix, the description, and the variable used to add additional commands.
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("~"),
    intents=intents,
    description=desc
)

# Store the id's of the users in a List, the id's in the List are used every "haunt_h" interval
opted = []

# Reads the opted file and stores the id's in the opted List
o = open("opted")
for line in o:
    line = line.strip("\n")
    if line != "":
        opted.append(line)

# "haunt_h" is an interval used in a internal loop that runs like a subprocess.
# It defines how much time is needed before the bot will send a random art from reddit to an opted user.
haunt_h = 2.0

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

    # This command registers the messages author, for haunting.
    # Here adding another ID t the List is easy, and writing to the file is easy too,
    # but the ID needs to be converted to String, for the List it's not necessary.

    @commands.command(description="opt in for occasional haunt")
    async def haunt(self, ctx):
        """Haunting you!"""
        h = False
        for op in opted:
            if op == ctx.author:
                h = True
            else:
                h = False
        if not h:
            opted.append(ctx.author.id)
            o = open("opted", "a")
            o.write(str(ctx.author.id))
            await ctx.send("Alright, I'm gonna scare you from time to time!")
        else:
            await ctx.send("I'm already trying to scare you... is it not enough?")

    # Removes the messages author from the haunting process.
    # For the List it's easy because we can just use the List's remove() method,
    # but for the file we need to... well rewrite the file.

    @commands.command(description="opt out of haunt")
    async def dehaunt(self, ctx):
        """De Haunting you..."""
        try:
            opted.remove(ctx.author.id)
            with open("opted", "r") as f:
                data = f.readlines()
            with open("opted", "w") as f:
                for line in data:
                    if line.strip("\n") != str(ctx.author.id):
                        f.write(line)

            await ctx.send("Eh...? You think I was too scary? Okay, I'll stop.")
        except Exception:
            await ctx.send("I'm not even trying to scare you!")

    # Steam recommandation command.
    # It can be slow because of steam.
    # see "steam_requests.py" to understand how it works.

    @commands.command(description="Recommends a game from Steam")
    async def recgame(self, ctx):
        """Recommend me a game!"""
        rec = steam_requests.recommend_game()
        await ctx.send("Hey Commander, have you tried this one?")
        await ctx.send(rec)


# See "reddit_requests.py" to understand how it works.
class Art(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    """Art commands"""

    # Art command see reddit_requests
    @commands.command(description="Random Art from reddit")
    async def art(self, ctx):
        """Sends a selfie from Reddit"""
        ghostie = reddit_requests.get_random_art()
        await ctx.send(ghostie)

    # NSFW command see reddit_requests
    @commands.command(description="Random NSFW Art from reddit")
    async def nsfw(self, ctx):
        """Sends a naughty selfie from Reddit"""
        n_ghostie = reddit_requests.get_random_nsfw()
        await ctx.send(n_ghostie)


def start(token):
    # Define what should happen when the bot is all set up and ready.
    @bot.event
    async def on_ready():
        # These prints are only here for debug purposes
        print('Logged in as')
        print(bot.user.name)
        print('------')

        # Here we add the commands that are inside of our classes, Cogs are basically lists of commands, but they aren't exactly, they're more than that...
        await bot.add_cog(Standard(bot))
        await bot.add_cog(Art(bot))

    # Initialize Tasks.
    # Tasks are internal loops that allows you to do something every given interval. (For more info see the discord.py docs)
    @tasks.loop(hours=c_hours)
    async def crontask():
        os.system("cron.py")

    # This task here is the haunting process, it sends a random art from reddit to a random opted in user, based on the users ID.
    @tasks.loop(hours=haunt_h)
    async def surprise():
        try:
            ro = r(0, len(opted))
            all = bot.get_all_members()
            for member in all:
                if member.id == int(opted[ro]):
                    ch = await member.create_dm()
                    await ch.send(reddit_requests.get_random_art())
                    break
        except Exception:
            pass

    # Start the task if relevant.
    if cron == False:
        crontask.start()

    # Well looks like if the events on_message is overridden then the commands won't procees...,
    # but if we use the listener then it's fine.
    # (Figured that if the "on_message()" is overriden, then we need to call the "command_process()", or something like that but using a listener instead was faster.)
    # NOTE: when using vscode pylance says that it isn't accessed, bullshit. It Is AcCeSsEd. (Tested)

    @bot.listen()
    async def on_message(msg) -> None:
        if msg.author == bot.user:
            return
        if str(msg.channel.type) == "private" and not "~" in msg.content:
            await msg.channel.send("Please use the command prefix(~) to run commands! ")
            return

    # Starts the bot using the provided token.
    # NOTE: This file only runs once, if more control is required over the loop use "bot.start(token)" instead, but first visit the discord.py docs.
    bot.run(token, reconnect=True)


start(token)
