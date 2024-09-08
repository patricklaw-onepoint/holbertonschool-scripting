#!/usr/bin/python3
"""
3-main
python api_advanced/3-main.py programming 
'react python java javascript scala no_results_for_this_one'
python: 24
javascript: 16
java: 11
react: 9
"""
import sys

if __name__ == "__main__":
    count_words = __import__("3-count").count_words
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
