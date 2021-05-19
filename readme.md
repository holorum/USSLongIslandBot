# USS Long Island Bot
This project is aiming to create a Discord bot using Python that randomly pings people who opted in with artwork pulled from Reddit and when requested recommends a game to play from Steam.

It's still WIP.

## Setting up

---

### Installing the discord wrapper

<br>

Before installing keep in mind that a Python 3.5.3 or higher is required for the wrapper.<br>
Install [discord.py](https://github.com/Rapptz/discord.py) using one of the following commands:

        # Linux/macOS
        python3 -m pip install -U discord.py

        # Windows
        py -3 -m pip install -U discord.py

For any additional information/documentation about this python discord wrapper, visit the [discord.py](https://github.com/Rapptz/discord.py) github page.

### Installing requests

<br>

Install requests using the following commands:

        python -m pip install requests

Requests is used by the bot to make HTTP GET requests to get image URLs from reddit, 
also to obtain various game data from steam. For more information about how to 
actually use requests visit the [requests](https://github.com/psf/requests) github page.


### About Discord Tokens

The discord token is a unique indentifier (something like a password) for a bot, and you can also use it to log into discord and control the bot as you would do with a normal discord account join voice channels, text channels etc.

You can always generate another one from the discord developer page if you feel that your token has been exposed.

To avoid such a case that is mentioned above it is recommended to encrypt your token when you use it. It's definitly not safe to replace the "token" variables value with your token as a string. The only case when you should do is, is when you are testing in a safe environment.

### Using your Token

Here we "secure" our tokens in a simple text file FOR TESTING only and the actual token that is used in the official USS Long Island Bot is encrypted.

To use your token simple create a "token" file in the folder where the main.py file is and you are good to go.

### About Discord Intents

The server members Intent needs to be enabled on the bot to fully function.
see [Privileged Gateway Intents](https://discordpy.readthedocs.io/en/latest/intents.html)

### cron.py

`cron.py` is to be run every so often so it creates and updates `games.json` from which the bot recommends the games. You should make a cronjob out of it or just run it manually every once in a while.

#### Ignorable files
There are files that should be ignored namely `games.json`, and `opted`.
`opted` is a file where the bot stores the Discord members user ID's who are 
registered for some processes and modifying the file can broke the process and the 
bot won't raise a warning or an error.
`games.json` is a file where the steam app IDs come from it is created with a GET request from the steam api, the bot uses a random app ID from the file then with a GET request from the steam store provides a URL that the bot will then send.

### End
Currently this is all you need to run your own USS Long Island Bot like bot.

## Links

---

- [Discord.py](https://github.com/Rapptz/discord.py)
- [Discord server](https://discord.gg/Bqj5UteMfy)
