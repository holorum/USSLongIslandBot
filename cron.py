#!/usr/bin/python3

import requests as req
import json

# Updates the json file/Rewrites it with newer content.
# Actually this method is unnecessary, but it will remain here in because why not?
def update_json():
    """Returns all games from steam to a file"""
    steam_all_games = "http://api.steampowered.com/ISteamApps/GetAppList/v2"
    r = req.get(steam_all_games).json()
    serialize = json.dumps(r, indent = 4)
    with open("games.json", "w") as jcron:
        jcron.write(serialize)

update_json()

import steam_requests

# Makes the dict in "steam_requests.py" update 
steam_requests.gamesdict = steam_requests.update_dict()
