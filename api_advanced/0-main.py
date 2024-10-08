#!/usr/bin/python3
"""
0-main
python api_advanced/0-main.py programming
python api_advanced/0-main.py this_is_a_fake_subreddit
"""
import sys

if __name__ == "__main__":
    number_of_subscribers = __import__("0-subs").number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
