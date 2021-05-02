#!/usr/bin/python3

import requests as req
import steam_requests
import json

steam = "http://api.steampowered.com"


# Updates the json file
def update_json():
    """Returns all games from steam to a file"""
    all_games = "/ISteamApps/GetAppList/v2"
    r = req.get(steam+all_games).json()
    serialize = json.dumps(r, indent = 4)
    with open("games.json", "w") as jcron:
        jcron.write(serialize)

update_json()
# Makes the dict in steam_requests.py update 
steam_requests.gamesdict = steam_requests.update_dict()
