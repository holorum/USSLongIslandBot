# For this script to be functioning, it requires the "requests" module
import requests as req
import json
import random

steam = "http://api.steampowered.com"
steam_store = "http://store.steampowered.com"
gamesdict = {}

# Updates the gamesdict
def update_dict():
    jcron = open("games.json", "r")
    gamesdict = json.load(jcron)
    return gamesdict
gamesdict = update_dict()

# Creates a steam store url based on appid and name of the game
def create_store_url(appid, name):
    """Creates a steam store url"""
    newname = name.replace(" ","_")
    return "{}/app/{}/{}".format(steam_store, appid, newname)


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
        return data
    except KeyError:
        return None


# Returns a random game 
def get_random_game():
    """Return a random game"""
    r = gamesdict
    randn = random.randint(0, len(r["applist"]["apps"]))
    game = get_game(r["applist"]["apps"][randn]["appid"])
    while game == None:
        randn = random.randint(0, len(r["applist"]["apps"]))
        game = get_game(r["applist"]["apps"][randn]["appid"])
    return game


# Recommends a random steam game
def recommend_game():
    """Recommends a game returns the name and the store url"""
    game = get_random_game()
    recommend = str(
        "{}\n"
        "{}"
    ).format(game["name"], create_store_url(game["steam_appid"], game["name"]))
    return recommend
