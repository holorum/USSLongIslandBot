import requests as req
import json

steam = "http://api.steampowered.com"
# Returns all the "games" (apps) from steam including the dlcs and other types
def get_all_games():
    """Returns all games from steam to a file"""
    all_games = "/ISteamApps/GetAppList/v2"
    r = req.get(steam+all_games).json()
    with open("games.json", "w") as jcron:
        json.dump(r, jcron)

get_all_games()
