# This will be replaced with asyncpraw just need to have some free time, until then this will do.
#
# Well this file is created if there will be any more reddit api requests.
# Install requests via pip to try it out.
import requests as req

# Just some text for reusing if needed.
reddit_domain = "https://www.reddit.com"
sub_reddit = "/r/USSLongIsland/"

# A user agent is required to ensure that our bot doesn't get a 429 for requesting once or twice
reddit_agent = {"User-Agent": "USSLongIslandBot"}

# These two modules use requests, process:
# 1. Does a HTTP GET request to obtain a random post.
# 2. Converts the returned value into a Dictionary.
# 3. if the over_18 value is false or the link_flair_text value is Art and it isn't a reddit gallery link, then returns the post URL that is a picture.


def get_random_art():

    # Here we use reddits random api call to get a random post then we do this untils it's an Art post.
    # Unfornunately the reddit api doesn't have an api call where you can specify the flair.
    # If anyone has a better Idea DO A FRICKING PULL REQUEST THAT FIXES THIS SHIT BECAUSE IT CAN BE SLOW AS FUCK.
    r = req.get(reddit_domain+sub_reddit+"random.json",
                headers=reddit_agent).json()
    post = r[0]["data"]["children"][0]["data"]
    type = post["link_flair_text"]
    nsfw = post["over_18"]
    url = post["url"]

    while type != "Art" or reddit_domain+"/gallery" in url or bool(nsfw) != False:
        r = req.get(reddit_domain+sub_reddit+"random.json?",
                    headers=reddit_agent).json()
        post = r[0]["data"]["children"][0]["data"]
        type = post["link_flair_text"]
        nsfw = post["over_18"]
        url = post["url"]
    if type == "Art" and nsfw == False:
        return url


# Same procedure only the 3. step differs a bit,
# "Art" isn't checked because NSFW content is usually Art in the current subreddit.
def get_random_nsfw():

    # Uses the same method but requests an nsfw post.
    r = req.get(reddit_domain+sub_reddit+"random.json",
                headers=reddit_agent).json()
    post = r[0]["data"]["children"][0]["data"]
    nsfw = post["over_18"]
    url = post["url"]

    while reddit_domain+"/gallery" in url or bool(nsfw) == False:
        r = req.get(reddit_domain+sub_reddit+"random.json?",
                    headers=reddit_agent).json()
        post = r[0]["data"]["children"][0]["data"]
        nsfw = post["over_18"]
        url = post["url"]
    if nsfw == True:
        return url
