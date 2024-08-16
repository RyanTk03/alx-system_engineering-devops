#!/usr/bin/python3
"""
File that contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    - Print None if not a valid subreddit.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom0"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
