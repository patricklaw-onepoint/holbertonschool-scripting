#!/usr/bin/python3
"""
API advanced

https://www.reddit.com/dev/api/
Write a function that queries the Reddit API 
and returns the number of subscribers 
(not active users, total subscribers) 
for a given subreddit. If an invalid subreddit 
is given, the function should return 0.

Hint: No authentication is necessary 
for most features of the Reddit API. 
If you're getting errors related to Too Many Requests, 
ensure you're setting a custom User-Agent.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "PL"},
        timeout=10,
        allow_redirects=False,
    )

    if response.status_code != 200:
        return 0

    try:
        json = response.json()
        if "data" in json:
            return int(json["data"]["subscribers"])
        return 0
    except requests.exceptions.JSONDecodeError:
        return 0
