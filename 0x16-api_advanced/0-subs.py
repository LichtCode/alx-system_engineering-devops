#!/usr/bin/python3
""" this sends a query to Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Makes a request to Reddit API to get the number of subscribers."""

    if subreddit is None:
        return 0
    elif isinstance(subreddit, str):
        headers = {"User-Agent": "beloveyeboah"}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        req = requests.get(url, headers=headers)
        response = req.json()
        try:
            return response.get('data').get('subscribers')
        except (AttributeError, TypeError):
            return 0
