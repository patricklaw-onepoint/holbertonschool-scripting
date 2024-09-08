#!/usr/bin/python3
"""API advanced"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively returns a list containing the
    titles of all hot articles for a given subreddit"""

    base = "https://www.reddit.com"
    response = requests.get(
        f"{base}/r/{subreddit}/hot.json?after={after}&limit=1000",
        headers={"User-Agent": "PL"},
        timeout=10,
    )

    if response.status_code != 200:
        return None

    json = response.json()
    data = json["data"]
    posts = data["children"]

    if posts:
        for post in posts:
            title = post["data"]["title"]
            if title:
                hot_list.append(title)
        after = data["after"]
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)

    return hot_list if not posts else None
