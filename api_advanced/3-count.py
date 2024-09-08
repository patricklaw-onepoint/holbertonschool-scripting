#!/usr/bin/python3
"""API advanced"""

import requests


def count_words(subreddit, word_list, after="", word_counts={}):
    """Recursively parses the title of all hot articles,
    and prints a sorted count of given keywords"""

    base = "https://www.reddit.com"
    response = requests.get(
        f"{base}/r/{subreddit}/hot.json?after={after}&limit=1000",
        headers={"User-Agent": "PL"},
        timeout=10,
    )

    if response.status_code != 200:
        return None

    if not word_counts:  # init
        word_counts = {word.lower(): 0 for word in word_list}

    if after is None:  # base case
        if not word_counts:
            return
        for word in dict(
            sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
        ):
            if word_counts[word] > 0:
                print(f"{word}: {word_counts[word]}")
        return

    json = response.json()
    print(json)
    data = json["data"]
    posts = data["children"]
    after = data["after"]

    for post in posts:
        title = post["data"]["title"].lower()
        for word in word_counts:  # count occurrences
            word_counts[word] += title.split().count(word)

    count_words(subreddit, word_list, after, word_counts)
