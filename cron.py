import requests as req
import json

steam = "http://api.steampowered.com"
# Returns all the "games" (apps) from steam including the dlcs and other types into a file
def get_all_games():
    """Returns all games from steam to a file"""
    all_games = "/ISteamApps/GetAppList/v2"
    r = req.get(steam+all_games).json()
    serialize = json.dumps(r, indent = 4)
    with open("games.json", "w") as jcron:
        jcron.write(serialize)

get_all_games()
