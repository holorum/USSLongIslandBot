# Well this file is created if there will be any more reddit api requests.
import requests as req

# Just some text for reusing if needed
reddit_domain = "https://www.reddit.com"
sub_reddit = "/r/USSLongIsland/"

# A user agent is required to ensure that our bot doesn't get a 429 for requesting once or twice
reddit_agent = {"User-Agent" : "USSLongIsland"}


def get_random_art():

    # Here we use reddits random api call to get a random post then we do this untils it's an Art post.
    # Unfornunately the reddit api doesn't have an api call where you can specify the flair.
    # If anyone has a better Idea DO A FRICKING PULL REQUEST THAT FIXES THIS SHIT BECAUSE IT CAN BE SLOW AS FUCK.
    r = req.get(reddit_domain+sub_reddit+"random.json", headers=reddit_agent).json()
    post = r[0]["data"]["children"][0]["data"]
    type = post["link_flair_text"]
    url = post["url"]

    while type != "Art":
        r = req.get(reddit_domain+sub_reddit+"random.json?", headers=reddit_agent).json()
        post = r[0]["data"]["children"][0]["data"]
        type = post["link_flair_text"]
        url = post["url"]
    if type == "Art":
        return url