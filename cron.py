#!/usr/bin/python3

import steam_requests
import requests as req
import json

# Updates the json file/rewrites it with newer content.

steam_all_games = "http://api.steampowered.com/ISteamApps/GetAppList/v2"
r = req.get(steam_all_games).json()
serialize = json.dumps(r, indent=4)
with open("games.json", "w") as jcron:
    jcron.write(serialize)


# Makes the dict in "steam_requests.py" update
steam_requests.gamesdict = steam_requests.update_dict()
