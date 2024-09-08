#!/usr/bin/python3
"""API advanced"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={"User-Agent": "PL"},
        timeout=10,
        allow_redirects=False,
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        json = response.json()
        if "data" in json:
            posts = json["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
    except requests.exceptions.JSONDecodeError:
        print(None)
