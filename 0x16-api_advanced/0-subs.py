#!/usr/bin/python3
"""
File that contains a function to query
subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Custom"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data['data']['subscribers']
    else:
        return 0
