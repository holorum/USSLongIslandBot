# For this script to be functioning, it requires the "requests" module
import requests as req
import random

steam = "http://api.steampowered.com"
steam_store = "http://store.steampowered.com"


# Returns all the "games" (apps) from steam including the dlcs and other types
def get_all_games():
    """Returns all games from steam"""
    all_games = "/ISteamApps/GetAppList/v2"
    r = req.get(steam+all_games).json()
    return r


# Some apps might be not games so it needs to be checked, also because the request returns a {'succes' : false} tuple
def get_game(appid):
    """Returns the game with the given 'appid'"""
    game = "{}/api/appdetails?appids={}".format(steam_store,appid)
    r = req.get(game).json()
    fk = list(r.keys())[0]
    try:
        data = r[fk]["data"]
        if data["type"] != "game":
            raise KeyError
        return data["type"]
    except KeyError:
        return None


# While the "get_game()" returns "None" tries another one,
# Returns a random game 
def get_random_game():
    """Return a random game"""
    r = get_all_games()
    randn = random.randint(0, len(r["applist"]["apps"]))
    game = get_game(r["applist"]["apps"][randn]["appid"])
    while game == None:
        randn = random.randint(0, len(r["applist"]["apps"]))
        game = get_game(r["applist"]["apps"][randn]["appid"])
    return game