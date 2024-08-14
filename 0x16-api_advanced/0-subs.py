#!/usr/bin/python3
""" this sends a query to Reddit API"""

import json
import requests


def number_of_subscribers(subreddit):
    """ for making a request Reddit Api """

    if subreddit is None:
        return 0
    elif type(subreddit) == "str":
        return 0
    user = {"User-Agent": "beloveyeboah"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=user)
    response = req.json()
    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
