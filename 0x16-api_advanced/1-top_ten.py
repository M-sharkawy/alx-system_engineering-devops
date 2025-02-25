#!/usr/bin/python3
'''fetch first 10 hot posts title of subreddit'''

import requests


def top_ten(subreddit):
    """Return the first 10 hot posts title of subreddit"""
    limit = 10
    posts = []
    url = f"https://www.reddit.com/r/{subreddit}/top.json?Limit={limit}"
    headers = {
        "Users-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if not data.get('data').get('children'):
            return None
        for post in data['data']['children']:
            x = post['data']['title']
            posts.append(x)
        return posts
    return None
