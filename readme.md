# USS Long Island Bot
This project is aiming to create a Discord bot using Python that randomly pings people who opted in and when requested recommends a game to play.

It's WIP, so everything will change.

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

### About Discord Tokens

The discord token is a unique indentifier (something like a password) for a bot, and you can also use it to log into discord and control the bot as you would do with a normal discord account join voice channels, text channels etc.

You can always generate another one from the discord developer page if you feel that your token has been exposed.

To avoid such a case that is mentioned above it is recommended to encrypt your token when you use it. It's definitly not safe to replace the "token" variables value with your token as a string. The only case when you should do is, is when you are testing in a safe environment.

### Using your Token

Here we "secure" our tokens in a simple text file FOR TESTING only and the actual token that is used in the official USS Long Island Bot is encrypted.

To use your token simple create a "token" file in the folder where the main.py file is and you are good to go.

### End
Currently this is all you need to run your own USS Long Island Bot like bot.

## Links

---

- [Discord.py](https://github.com/Rapptz/discord.py)
- [Discord server](https://discord.gg/Bqj5UteMfy)
